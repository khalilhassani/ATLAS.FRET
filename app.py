import os
import json
import sqlite3
import time
import sys
import uuid
from typing import Any
from flask import Flask, request, jsonify, render_template
from backend.orchestrator import (
    run_langgraph_pipeline, 
    load_physical_graph, 
    DB_PATH, 
    CONFIG_FILE, 
    load_api_config
)

# Force UTF-8 encoding for Windows console compatibility
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')
app.secret_key = uuid.uuid4().hex


# =====================================================================
# DATABASE UTILITIES
# =====================================================================

def query_db(query: str, args: tuple = (), one: bool = False) -> Any:
    """Exécute une requête SQL en lecture seule sur la base SQLite locale."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

def update_db(query: str, args: tuple = ()) -> None:
    """Exécute une commande de mise à jour SQL sur la base SQLite locale."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()


# =====================================================================
# HTML PAGES ROUTING
# =====================================================================

@app.route("/")
def index():
    """Rend la page du tableau de bord de supervision principal."""
    return render_template("index.html")


# =====================================================================
# API ENDPOINTS
# =====================================================================

@app.route("/api/submit", methods=["POST"])
def submit_query():
    """
    Traite une alerte d'incident ONCF en exécutant le pipeline LangGraph.
    Retourne la décision finale au format JSON et l'historique d'audit.
    """
    data = request.json or {}
    user_query = data.get("query", "").strip()
    if not user_query:
        return jsonify({"error": "La requête utilisateur ne peut pas être vide."}), 400
        
    corr_id = f"run-{uuid.uuid4().hex[:8]}"
    print(f"📥 Réception d'alerte logistique. Correl-ID: {corr_id}")
    
    try:
        result = run_langgraph_pipeline(user_query, corr_id)
        return jsonify({
            "correlation_id": corr_id,
            "response": result["response"],
            "logs": result["logs"],
            "latency": result["latency"],
            "cost": result["cost"],
            "hitl_reason": result["hitl_reason"],
            "requires_hitl": result["response"]["statut_requete"] == "PENDING_HUMAN_VALIDATION"
        })
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution du pipeline LangGraph: {e}")
        return jsonify({"error": f"Erreur d'exécution de l'agent: {str(e)}"}), 500

@app.route("/api/graph", methods=["GET"])
def get_graph():
    """
    Extrait les nœuds et relations logistiques depuis le graphe NetworkX
    et les formate au format de visualisation Vis.js.
    """
    try:
        # Load the graph dynamically using the unified physical graph loader
        G = load_physical_graph()
        
        nodes = []
        for node_id, attrs in G.nodes(data=True):
            group = attrs.get("label", "Unknown")
            name = attrs.get("name", node_id)
            label_text = f"<b>{name}</b>"
            
            # Styles configuration according to node type
            if group == "Gare":
                color = "#EF4444"
                shape = "dot"
                label_text += f"\n(Capacité: {attrs.get('capacite_fret')}t)"
            elif group == "HubLogistique":
                color = "#3B82F6"
                shape = "dot"
            elif group == "LigneFerroviaire":
                color = "#F59E0B"
                shape = "triangle"
                label_text += f"\n[{attrs.get('code')}]"
            elif group == "Transporteur":
                color = "#10B981"
                shape = "square"
                label_text += f"\nCNSS: {'Conforme' if attrs.get('statut_cnss') else 'Défaut'}"
            elif group == "Camion":
                color = "#8B5CF6"
                shape = "database"
                label_text += f"\n({attrs.get('capacite_tonnes')}t - Frigo: {'Oui' if attrs.get('type_frigo') else 'Non'})"
            else:
                color = "#9CA3AF"
                shape = "ellipse"
                
            nodes.append({
                "id": node_id,
                "label": label_text,
                "title": f"Propriétés: {json.dumps(attrs, indent=2, ensure_ascii=False)}",
                "group": group,
                "color": {"background": color, "border": "#1E293B", "highlight": {"background": "#60A5FA", "border": "#3B82F6"}},
                "shape": shape,
                "font": {"multi": "html", "color": "#E2E8F0"}
            })
            
        edges = []
        for u, v, data in G.edges(data=True):
            rel = data.get("relationship", "LINK")
            label = rel
            
            if rel == "RELIER" and "distance_km" in data:
                label += f" ({data['distance_km']} km)"
                
            dashes = (rel == "EST_AGREE_POUR")
            
            edges.append({
                "from": u,
                "to": v,
                "label": label,
                "title": f"Détails: {json.dumps(data, ensure_ascii=False)}",
                "arrows": "to" if rel == "RELIER" else "",
                "color": {"color": "#64748B", "highlight": "#3B82F6"},
                "dashes": dashes,
                "width": 1.5
            })
            
        return jsonify({"nodes": nodes, "edges": edges})
    except Exception as e:
        print(f"❌ Erreur lors de la génération du graphe Vis.js: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/api/traces", methods=["GET"])
def get_traces():
    """Récupère l'historique d'audit des requêtes pour le tableau d'observabilité."""
    try:
        rows = query_db("""
            SELECT id, correlation_id, timestamp, query, status, latency, cost, security_score, hitl_status, logs 
            FROM traces 
            ORDER BY timestamp DESC 
            LIMIT 30;
        """)
        traces = []
        for r in rows:
            traces.append({
                "id": r["id"],
                "correlation_id": r["correlation_id"],
                "timestamp": r["timestamp"],
                "query": r["query"],
                "status": r["status"],
                "latency": round(r["latency"], 4),
                "cost": round(r["cost"], 6),
                "security_score": round(r["security_score"], 2),
                "hitl_status": r["hitl_status"],
                "logs": json.loads(r["logs"] or "[]")
            })
        return jsonify(traces)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/hitl/approve", methods=["POST"])
def hitl_approve():
    """
    Approuve manuellement un déroutement suspendu.
    Bloque les fonds en séquestre en signant numériquement la transaction.
    """
    data = request.json or {}
    corr_id = data.get("correlation_id")
    signature = data.get("signature", "").strip()
    
    if not corr_id or not signature:
        return jsonify({"error": "correlation_id et signature requis."}), 400
        
    try:
        trace = query_db("SELECT logs FROM traces WHERE correlation_id = ?;", (corr_id,), one=True)
        if not trace:
            return jsonify({"error": "Requête introuvable."}), 404
            
        logs = json.loads(trace["logs"] or "[]")
        logs.append(f"✍️ [HITL] Signature cryptographique de l'opérateur reçue : {signature}")
        logs.append("🔓 [HITL] Contrat de Séquestre validé manuellement. Plan de déroutement autorisé.")
        
        update_db("UPDATE traces SET status = 'SUCCESS', hitl_status = 'APPROVED', logs = ? WHERE correlation_id = ?;", (json.dumps(logs), corr_id))
        
        escrow_id = f"ESC-{uuid.uuid4().hex[:8].upper()}"
        update_db("""
            INSERT INTO escrow_ledger (id, mission_id, carrier, amount, status, signed_by)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (escrow_id, corr_id, "Transporteur Sélectionné (HITL)", 7500.0, "APPROVED", signature))
        
        return jsonify({"status": "SUCCESS", "message": "Déroutement logistique approuvé avec succès.", "escrow_id": escrow_id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/hitl/reject", methods=["POST"])
def hitl_reject():
    """Annule manuellement un plan de déroutement logistique suspendu."""
    data = request.json or {}
    corr_id = data.get("correlation_id")
    if not corr_id:
        return jsonify({"error": "correlation_id manquant."}), 400
        
    try:
        trace = query_db("SELECT logs FROM traces WHERE correlation_id = ?;", (corr_id,), one=True)
        if not trace:
            return jsonify({"error": "Requête introuvable."}), 404
            
        logs = json.loads(trace["logs"] or "[]")
        logs.append("🔴 [HITL] Mission rejetée par l'opérateur de sécurité logistique.")
        
        update_db("UPDATE traces SET status = 'BLOCKED', hitl_status = 'REJECTED', logs = ? WHERE correlation_id = ?;", (json.dumps(logs), corr_id))
        update_db("UPDATE escrow_ledger SET status = 'REJECTED' WHERE mission_id = ?;", (corr_id,))
        
        return jsonify({"status": "REJECTED", "message": "Mission logistique annulée et classée."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/settings", methods=["GET", "POST"])
def settings_handler():
    """
    GET: Renvoie les paramètres actuels de l'agent.
    POST: Met à jour les variables système (Seuil Obsidien, S_max, Maintenance, Clés API, Astra DB).
    """
    if request.method == "GET":
        try:
            cfg = load_api_config()
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT key, value FROM settings;")
            for k, v in cursor.fetchall():
                if k == 'agent_maintenance_mode':
                    cfg[k] = (v.lower() == 'true')
                else:
                    cfg[k] = float(v) if v.replace('.','',1).isdigit() else v
            conn.close()
            return jsonify(cfg)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        data = request.json or {}
        try:
            # Persistent Settings in SQLite
            if "agent_maintenance_mode" in data:
                val = "true" if data["agent_maintenance_mode"] else "false"
                update_db("INSERT OR REPLACE INTO settings (key, value) VALUES ('agent_maintenance_mode', ?);", (val,))
            if "seuil_obsidien" in data:
                update_db("INSERT OR REPLACE INTO settings (key, value) VALUES ('seuil_obsidien', ?);", (str(data["seuil_obsidien"]),))
            if "s_max_cost" in data:
                update_db("INSERT OR REPLACE INTO settings (key, value) VALUES ('s_max_cost', ?);", (str(data["s_max_cost"]),))
                
            # Persistent Config in config_db.json
            config = load_api_config()
            keys = ["endpoint", "token", "keyspace", "groq_api_key", "gemini_api_key", "openai_api_key"]
            for k in keys:
                if k in data:
                    config[k] = data[k]
                    
            with open(CONFIG_FILE, "w") as f:
                json.dump(config, f, indent=2)
                
            return jsonify({"status": "SUCCESS", "message": "Configurations enregistrées."})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# =====================================================================
# RUNBOOK OPERATIONAL ENDPOINTS
# =====================================================================

@app.route("/api/runbook/purge", methods=["POST"])
def runbook_purge():
    """Purge l'ensemble des traces d'observabilité temporaires."""
    try:
        update_db("DELETE FROM traces;")
        update_db("DELETE FROM escrow_ledger;")
        print("🧹 [RUNBOOK] Traces et registres de paiement purgés.")
        return jsonify({"status": "SUCCESS", "message": "Purge effectuée avec succès."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/runbook/integrity", methods=["POST"])
def runbook_integrity():
    """Effectue un audit d'intégrité relationnel du Graphe de Connaissances."""
    try:
        edges = query_db("SELECT source, target FROM edges;")
        orphans = []
        for e in edges:
            src = query_db("SELECT id FROM nodes WHERE id = ?;", (e["source"],), one=True)
            tgt = query_db("SELECT id FROM nodes WHERE id = ?;", (e["target"],), one=True)
            if not src or not tgt:
                orphans.append(f"({e['source']} -> {e['target']})")
                
        if orphans:
            return jsonify({"status": "WARNING", "message": f"Contrôle d'intégrité : Liens orphelins détectés: {', '.join(orphans)}"})
        return jsonify({"status": "SUCCESS", "message": "Contrôle d'intégrité : 100% des liens physiques logistiques sont valides."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =====================================================================
# STARTING SERVER
# =====================================================================

if __name__ == "__main__":
    # Started on port 5050 to avoid address conflict on standard port 5000
    print("🚀 Démarrage du serveur ATLASFret sur http://127.0.0.1:5050")
    app.run(debug=True, port=5050)
