import os
import json
import sqlite3
import sys
from backend.orchestrator import AstraDBConnector, load_api_config, DB_PATH

# Force UTF-8 encoding for Windows console compatibility
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass


# =====================================================================
# METADATA INITIALIZATION DICTIONARIES
# =====================================================================

# Gares (Stations)
STATIONS_DATA = [
    {"id": "Gare-Tanger-Med", "label": "Gare", "name": "Gare de Tanger Med", "properties": {"ville": "Tanger", "capacite_fret": 5000}},
    {"id": "Gare-Kenitra", "label": "Gare", "name": "Gare de Kenitra", "properties": {"ville": "Kenitra", "capacite_fret": 4000}},
    {"id": "Gare-Casa-Voyageurs", "label": "Gare", "name": "Gare de Casa Voyageurs", "properties": {"ville": "Casablanca", "capacite_fret": 8000}},
    {"id": "Gare-Fes-Ville", "label": "Gare", "name": "Gare de Fès-Ville", "properties": {"ville": "Fès", "capacite_fret": 3000}},
    {"id": "Gare-Oujda", "label": "Gare", "name": "Gare de Oujda", "properties": {"ville": "Oujda", "capacite_fret": 2000}},
    {"id": "Gare-Marrakech", "label": "Gare", "name": "Gare de Marrakech", "properties": {"ville": "Marrakech", "capacite_fret": 3500}}
]

# Hubs Logistiques (Logistics Hubs)
HUBS_DATA = [
    {"id": "Hub-Tanger-TFZ", "label": "HubLogistique", "name": "Plateforme Logistique Tanger Free Zone", "properties": {"ville": "Tanger"}},
    {"id": "Hub-Kenitra-ZF", "label": "HubLogistique", "name": "Hub Kenitra Zone Franche", "properties": {"ville": "Kenitra"}},
    {"id": "Hub-Casa-Mita", "label": "HubLogistique", "name": "Plateforme Logistique Casa Mita", "properties": {"ville": "Casablanca"}},
    {"id": "Hub-Fes-Saiss", "label": "HubLogistique", "name": "Plateforme Logistique Fès-Saïss", "properties": {"ville": "Fès"}},
    {"id": "Hub-Oujda-Angad", "label": "HubLogistique", "name": "Hub Logistique Oujda Angad", "properties": {"ville": "Oujda"}},
    {"id": "Hub-Marrakech-Ghanem", "label": "HubLogistique", "name": "Hub Logistique Marrakech Sidi Ghanem", "properties": {"ville": "Marrakech"}}
]

# Lignes Ferroviaires (Rail Tracks)
RAILS_DATA = [
    {"id": "Ligne-Tanger-Kenitra", "label": "LigneFerroviaire", "name": "Ligne Ferroviaire Tanger-Kenitra", "properties": {"code": "LTK", "statut_voie": "OPERATIONNELLE"}},
    {"id": "Ligne-Kenitra-Casa", "label": "LigneFerroviaire", "name": "Ligne Ferroviaire Kenitra-Casablanca", "properties": {"code": "LKC", "statut_voie": "OPERATIONNELLE"}},
    {"id": "Ligne-Kenitra-Fes", "label": "LigneFerroviaire", "name": "Ligne Ferroviaire Kenitra-Fès", "properties": {"code": "LKF", "statut_voie": "OPERATIONNELLE"}},
    {"id": "Ligne-Fes-Oujda", "label": "LigneFerroviaire", "name": "Ligne Ferroviaire Fès-Oujda", "properties": {"code": "LFO", "statut_voie": "OPERATIONNELLE"}},
    {"id": "Ligne-Casa-Marrakech", "label": "LigneFerroviaire", "name": "Ligne Ferroviaire Casablanca-Marrakech", "properties": {"code": "LCM", "statut_voie": "OPERATIONNELLE"}}
]

# Transporteurs (Carriers)
CARRIERS_DATA = [
    {"id": "Trans-Maro-Fret", "label": "Transporteur", "name": "Trans-Maro-Fret SARL", "properties": {"patente": "MA-8923011", "statut_cnss": True, "score_confiance": 0.98}},
    {"id": "Atlas-Transit-Maroc", "label": "Transporteur", "name": "Atlas Transit Maroc", "properties": {"patente": "MA-9102394", "statut_cnss": True, "score_confiance": 0.92}},
    {"id": "Maghrib-Logistique", "label": "Transporteur", "name": "Maghrib Logistique S.A.", "properties": {"patente": "MA-7748190", "statut_cnss": True, "score_confiance": 0.95}},
    {"id": "Fret-Express-Maroc", "label": "Transporteur", "name": "Fret Express Maroc", "properties": {"patente": "MA-5512399", "statut_cnss": False, "score_confiance": 0.40}}
]

# Camions (Trucks)
TRUCKS_DATA = [
    {"id": "Camion-TMF-Frigo-12T", "label": "Camion", "name": "12345-A-40 (Trans-Maro-Fret)", "properties": {"immatriculation": "12345-A-40", "type_frigo": True, "capacite_tonnes": 12, "chauffeur": "Abdelkader Alami"}},
    {"id": "Camion-TMF-Frigo-8T", "label": "Camion", "name": "67890-B-50 (Trans-Maro-Fret)", "properties": {"immatriculation": "67890-B-50", "type_frigo": True, "capacite_tonnes": 8, "chauffeur": "Karim Bennani"}},
    {"id": "Camion-ATM-Standard-15T", "label": "Camion", "name": "11223-D-60 (Atlas Transit)", "properties": {"immatriculation": "11223-D-60", "type_frigo": False, "capacite_tonnes": 15, "chauffeur": "Omar Tazi"}},
    {"id": "Camion-FEM-Standard-5T", "label": "Camion", "name": "44556-F-70 (Fret Express)", "properties": {"immatriculation": "44556-F-70", "type_frigo": False, "capacite_tonnes": 5, "chauffeur": "Said Mezouar"}},
    {"id": "Camion-ML-Frigo-18T", "label": "Camion", "name": "99887-A-20 (Maghrib Logistique)", "properties": {"immatriculation": "99887-A-20", "type_frigo": True, "capacite_tonnes": 18, "chauffeur": "Youssef Kadiri"}}
]

# Relationships (Edges)
EDGES_DATA = [
    # LigneFerroviaire -> Gare (RELIER)
    {"source": "Ligne-Tanger-Kenitra", "target": "Gare-Tanger-Med", "relationship": "RELIER", "properties": {"distance_km": 140}},
    {"source": "Ligne-Tanger-Kenitra", "target": "Gare-Kenitra", "relationship": "RELIER", "properties": {"distance_km": 140}},
    {"source": "Ligne-Kenitra-Casa", "target": "Gare-Kenitra", "relationship": "RELIER", "properties": {"distance_km": 40}},
    {"source": "Ligne-Kenitra-Casa", "target": "Gare-Casa-Voyageurs", "relationship": "RELIER", "properties": {"distance_km": 40}},
    {"source": "Ligne-Kenitra-Fes", "target": "Gare-Kenitra", "relationship": "RELIER", "properties": {"distance_km": 210}},
    {"source": "Ligne-Kenitra-Fes", "target": "Gare-Fes-Ville", "relationship": "RELIER", "properties": {"distance_km": 210}},
    {"source": "Ligne-Fes-Oujda", "target": "Gare-Fes-Ville", "relationship": "RELIER", "properties": {"distance_km": 350}},
    {"source": "Ligne-Fes-Oujda", "target": "Gare-Oujda", "relationship": "RELIER", "properties": {"distance_km": 350}},
    {"source": "Ligne-Casa-Marrakech", "target": "Gare-Casa-Voyageurs", "relationship": "RELIER", "properties": {"distance_km": 240}},
    {"source": "Ligne-Casa-Marrakech", "target": "Gare-Marrakech", "relationship": "RELIER", "properties": {"distance_km": 240}},
    
    # Transporteur -> Camion (POSSEDER)
    {"source": "Trans-Maro-Fret", "target": "Camion-TMF-Frigo-12T", "relationship": "POSSEDER", "properties": {}},
    {"source": "Trans-Maro-Fret", "target": "Camion-TMF-Frigo-8T", "relationship": "POSSEDER", "properties": {}},
    {"source": "Atlas-Transit-Maroc", "target": "Camion-ATM-Standard-15T", "relationship": "POSSEDER", "properties": {}},
    {"source": "Fret-Express-Maroc", "target": "Camion-FEM-Standard-5T", "relationship": "POSSEDER", "properties": {}},
    {"source": "Maghrib-Logistique", "target": "Camion-ML-Frigo-18T", "relationship": "POSSEDER", "properties": {}},
    
    # Transporteur -> HubLogistique (EST_AGREE_POUR)
    {"source": "Trans-Maro-Fret", "target": "Hub-Fes-Saiss", "relationship": "EST_AGREE_POUR", "properties": {"date_agreement": "2025-01-10"}},
    {"source": "Trans-Maro-Fret", "target": "Hub-Kenitra-ZF", "relationship": "EST_AGREE_POUR", "properties": {"date_agreement": "2025-02-15"}},
    {"source": "Atlas-Transit-Maroc", "target": "Hub-Casa-Mita", "relationship": "EST_AGREE_POUR", "properties": {"date_agreement": "2024-11-20"}},
    {"source": "Atlas-Transit-Maroc", "target": "Hub-Fes-Saiss", "relationship": "EST_AGREE_POUR", "properties": {"date_agreement": "2025-03-01"}},
    {"source": "Atlas-Transit-Maroc", "target": "Hub-Kenitra-ZF", "relationship": "EST_AGREE_POUR", "properties": {"date_agreement": "2025-01-01"}},
    {"source": "Maghrib-Logistique", "target": "Hub-Tanger-TFZ", "relationship": "EST_AGREE_POUR", "properties": {"date_agreement": "2025-04-18"}},
    {"source": "Maghrib-Logistique", "target": "Hub-Casa-Mita", "relationship": "EST_AGREE_POUR", "properties": {"date_agreement": "2025-01-01"}},
    {"source": "Fret-Express-Maroc", "target": "Hub-Oujda-Angad", "relationship": "EST_AGREE_POUR", "properties": {"date_agreement": "2025-05-22"}}
]


# =====================================================================
# SEEDING FUNCTIONS
# =====================================================================

def init_sqlite_db():
    """Initialise le schéma et les tables SQL locales."""
    print("🎲 Initialisation de SQLite local...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nodes (
            id TEXT PRIMARY KEY, label TEXT NOT NULL, name TEXT NOT NULL, properties TEXT
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS edges (
            source TEXT NOT NULL, target TEXT NOT NULL, relationship TEXT NOT NULL, properties TEXT,
            PRIMARY KEY (source, target, relationship)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id TEXT PRIMARY KEY, source_title TEXT NOT NULL, content TEXT NOT NULL, category TEXT
        );
    """)
    try:
        cursor.execute("CREATE VIRTUAL TABLE IF NOT EXISTS documents_fts USING fts5(id, source_title, content, category);")
    except Exception:
        pass
        
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS traces (
            id INTEGER PRIMARY KEY AUTOINCREMENT, correlation_id TEXT NOT NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            query TEXT, status TEXT, latency REAL, cost REAL, security_score REAL, hitl_status TEXT, logs TEXT
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS escrow_ledger (
            id TEXT PRIMARY KEY, mission_id TEXT NOT NULL, carrier TEXT NOT NULL, amount REAL NOT NULL,
            status TEXT NOT NULL, signed_by TEXT, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    cursor.execute("CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT);")
    
    cursor.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('agent_maintenance_mode', 'false');")
    cursor.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('seuil_obsidien', '0.7');")
    cursor.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('s_max_cost', '15000');")
    
    conn.commit()
    conn.close()
    print("✅ Tables SQLite initialisées.")

def seed_sqlite_graph():
    """Injecte la topologie physique logistique dans SQLite local."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM nodes;")
    cursor.execute("DELETE FROM edges;")
    
    all_nodes = STATIONS_DATA + HUBS_DATA + RAILS_DATA + CARRIERS_DATA + TRUCKS_DATA
    for n in all_nodes:
        cursor.execute(
            "INSERT INTO nodes (id, label, name, properties) VALUES (?, ?, ?, ?);",
            (n["id"], n["label"], n["name"], json.dumps(n["properties"]))
        )
        
    for e in EDGES_DATA:
        cursor.execute(
            "INSERT OR REPLACE INTO edges (source, target, relationship, properties) VALUES (?, ?, ?, ?);",
            (e["source"], e["target"], e["relationship"], json.dumps(e["properties"]))
        )
        
    conn.commit()
    conn.close()
    print("✅ Topologie physique chargée dans SQLite local.")

def seed_sqlite_rag():
    """Injecte les textes de loi réglementaires dans SQLite RAG (FTS5)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM documents;")
    
    docs = [
        ("doc-1", "Loi 16-99 - Agrément Transporteur", 
         "Loi n° 16-99 relative aux transports routiers. Article 5 : L'exercice de l'activité est subordonné à l'inscription au registre. Tout transporteur doit posséder une patente valide (MA-) et être en règle avec la CNSS. En cas de non-conformité CNSS, le transporteur doit être automatiquement bloqué.", 
         "Loi 16-99"),
        ("doc-2", "Loi 16-99 - Denrées Périssables", 
         "Loi n° 16-99. Article 12 : Le transport intercommunal de denrées périssables exige des remorques frigorifiques ou caisses isothermes équipées d'un système d'enregistrement de température, sous peine de blocage.", 
         "Loi 16-99"),
        ("doc-3", "Loi 09-08 - Données Personnelles CNDP", 
         "Loi n° 09-08 (CNDP). Les données personnelles sensibles des chauffeurs (noms, CIN, téléphones, salaires) doivent être anonymisées ou masquées avant tout traitement automatisé par les modèles d'IA.", 
         "Loi 09-08"),
        ("doc-4", "Code de la route - Tonnage et Sécurité", 
         "Code de la route. Section 32 : Le PTAC des camions est réglementé. Les charges lourdes de plus de 15 tonnes ou convois hors normes exigent des autorisations et peuvent être bloqués pour validation manuelle.", 
         "Code de la Route"),
        ("doc-5", "Règlement ONCF - Déroutement de Fret", 
         "Règlement ONCF. Article 44 : En cas d'incident bloquant les voies ferrées nationales, l'ONCF autorise le déroutement routier immédiat vers le hub logistique le plus proche dans la même ville.", 
         "Règlement ONCF")
    ]
    
    for doc_id, title, content, cat in docs:
        cursor.execute("INSERT INTO documents (id, source_title, content, category) VALUES (?, ?, ?, ?);", (doc_id, title, content, cat))
        try:
            cursor.execute("INSERT INTO documents_fts (id, source_title, content, category) VALUES (?, ?, ?, ?);", (doc_id, title, content, cat))
        except Exception:
            pass
            
    conn.commit()
    conn.close()
    print("✅ Textes réglementaires chargés dans SQLite FTS5.")
    return docs

def seed_astra_db_graph():
    """Injecte la topologie physique logistique dans le cloud DataStax Astra DB si configuré."""
    config = load_api_config()
    endpoint = config.get("endpoint")
    token = config.get("token")
    keyspace = config.get("keyspace")
    
    if not (endpoint and token and keyspace):
        print("ℹ️ Astra DB non configuré dans 'config_db.json'. Saut de la synchronisation cloud.")
        return
        
    print("🌐 Connexion à DataStax Astra DB pour initialiser les collections...")
    try:
        connector = AstraDBConnector(endpoint, token, keyspace)
        
        # Create collections nodes & edges
        connector.create_collection("nodes")
        connector.create_collection("edges")
        
        # Purge collections
        connector.delete_many("nodes")
        connector.delete_many("edges")
        print("🧹 Collections 'nodes' et 'edges' purgées sur Astra DB.")
        
        # Insert Nodes
        all_nodes = STATIONS_DATA + HUBS_DATA + RAILS_DATA + CARRIERS_DATA + TRUCKS_DATA
        for n in all_nodes:
            doc = {
                "_id": n["id"],
                "label": n["label"],
                "name": n["name"],
                "properties": n["properties"]
            }
            connector.insert_one("nodes", doc)
            
        # Insert Edges
        for e in EDGES_DATA:
            doc = {
                "_id": f"{e['source']}_{e['target']}_{e['relationship']}",
                "source": e["source"],
                "target": e["target"],
                "relationship": e["relationship"],
                "properties": e["properties"]
            }
            connector.insert_one("edges", doc)
            
        print("✅ Données du graphe chargées avec succès sur DataStax Astra DB.")
    except Exception as err:
        print(f"❌ Échec de l'indexation Astra DB: {err}")

def seed_chroma_db(docs):
    """Indexe les documents dans ChromaDB pour la recherche vectorielle sémantique."""
    try:
        import chromadb
        client = chromadb.PersistentClient(path="./chroma_db")
        collection = client.get_or_create_collection(name="base_obsidienne")
        
        existing = collection.get().get("ids", [])
        if existing:
            collection.delete(ids=existing)
            
        collection.add(
            documents=[d[2] for d in docs],
            metadatas=[{"source_title": d[1], "category": d[3]} for d in docs],
            ids=[d[0] for d in docs]
        )
        print("✅ Documents indexés avec succès dans ChromaDB.")
    except Exception as e:
        print(f"ℹ️ ChromaDB indisponible (bascule sur SQLite FTS5) : {e}")

# =====================================================================
# MAIN RUNNER
# =====================================================================

if __name__ == "__main__":
    print("🚀 AMORÇAGE ET INITIALISATION DU SYSTEME DE DONNÉES ATLASFRET...")
    init_sqlite_db()
    seed_sqlite_graph()
    docs_list = seed_sqlite_rag()
    seed_chroma_db(docs_list)
    seed_astra_db_graph()
    print("🎉 Initialisation complète terminée avec succès !")
