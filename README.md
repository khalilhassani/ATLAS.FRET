# ATLASFret Intelligence — Agent Sécurisé de Logistique & Transport Multimodal

**ATLASFret Intelligence** est une plateforme de supervision logistique et de conformité réglementaire conçue pour l'**Office National des Chemins de Fer (ONCF)** et le transport multimodal au Royaume du Maroc. 

La plateforme utilise un pipeline d'agents **LangGraph** connecté à un graphe de connaissances hébergé sur **DataStax Astra DB** afin de calculer des déroutements routiers d'urgence lors de ruptures de charge ferroviaires, tout en garantissant la conformité légale (Loi 16-99 CNSS) et la sécurité financière (Ledger d'Escrow).

---

## 🎨 Interface Neumorphic 3D (ONCF Edition)

Le tableau de bord adopte un design 3D skeuomorphique moderne en mode clair aux couleurs nationales (Vert émeraude royal, Bleu cobalt ONCF, Or et Argent) :
*   **Supervision en direct** : Compteurs d'alertes en relief 3D, barres de progression de transport et sélection rapide de scénarios d'incident ferroviaire.
*   **3D Physical Map du Maroc** : Tracé SVG complet du réseau national incluant le **Sahara Marocain** (Laâyoune et Dakhla) avec indicateur de rupture clignotant.
*   **3D Multi-Hop Graph** : Rendu interactif du graphe topologique extrait en direct de la base cloud **Astra DB**.
*   **Timeline de Sécurité** : Suivi des 6 étapes de l'agent LangGraph en temps réel.
*   **SkillSpector Checklist** : Visualisation en direct des alertes réglementaires (Sécurité, Flotte, CNSS, Budget).
*   **Obsidian Vault Logs** : Liste de défilement des rapports d'audit.

---

## 📂 Architecture Modulaire du Projet

Le projet est organisé de manière propre et structurée selon les standards d'ingénierie logicielle :

```text
ATLASFret/
├── app.py                     # Serveur Flask principal (API REST & Services de rendu)
├── run_benchmarks.py          # Suite de tests et d'évaluation réglementaire (7 Scénarios)
├── config_db.json.example     # Modèle de configuration des secrets et clés d'API
│
├── backend/                   # ⚙️ LOGIQUE BACKEND
│   ├── __init__.py            # Initialisation du package
│   ├── orchestrator.py        # Graphe d'état LangGraph, Audit RAG, Guardrails & LLM
│   └── initialize_data.py     # Script de peuplement de la topologie sur Astra DB
│
├── frontend/                  # 🎨 DESIGN & INTERFACE FRONTEND
│   ├── templates/
│   │   └── index.html         # Template HTML5 du tableau de bord ONCF
│   └── static/
│       ├── app.css            # Charte graphique neumorphique light-mode
│       ├── app.js             # Logique d'interaction et d'appels API AJAX
│       ├── oncf_logo.jpg      # Logo officiel ONCF
│       ├── royal_crest_morocco.png  # Armoiries Royales du Royaume
│       └── map_morocco_sahara.jpg   # Carte physique du Maroc avec son Sahara
│
└── obsidian_vault/            # 📁 COFFRE D'AUDIT REGLEMENTAIRE (Obsidian)
    ├── Audit_Index.md         # Index général des audits logistiques sous forme de table
    └── runs/                  # Fiches d'audit Markdown structurées avec frontmatter YAML
```

---

## ⚙️ Installation et Configuration

### 1. Prérequis
Installez les dépendances nécessaires au projet :
```bash
pip install flask networkx langgraph sqlite3 chromadb
```

### 2. Secrets et Clés de Base de Données
Copiez le modèle de configuration et renommez-le :
```bash
cp config_db.json.example config_db.json
```
Éditez le fichier `config_db.json` avec vos propres informations d'accès :
*   `endpoint` : Votre URL DataStax Astra DB JSON API.
*   `token` : Votre token d'accès Astra DB.
*   `groq_api_key` / `gemini_api_key` : Vos clés de modèles de langage (LLM).

### 3. Amorçage et Synchronisation Cloud (Astra DB)
Pour purger les anciennes données et synchroniser la topologie ferroviaire marocaine (26 nœuds, 23 relations) dans votre base cloud Astra DB, exécutez :
```bash
python backend/initialize_data.py
```

---

## 🧪 Exécution et Tests

### 1. Démarrage de la Plateforme
Lancez le serveur Web local :
```bash
python app.py
```
Accédez à l'application dans votre navigateur : **`http://127.0.0.1:5050`**

### 2. Suite de Benchmarks de Sécurité (7/7 Cas)
Pour évaluer la résilience réglementaire de la plateforme face aux attaques par injection, vérifications de conformité CNSS et dépassements de budgets :
```bash
python run_benchmarks.py
```

---

## 📓 Intégration du Coffre d'Audit (Obsidian Vault)

Chaque déroutement logistique est sauvegardé dans le dossier `obsidian_vault/` sous forme de fiches Markdown structurées et inter-liées :
*   **YAML Frontmatter** : Idéal pour requêter les données avec des plugins Obsidian comme *Dataview*.
*   **Wiki-links (`[[run-id]]`, `[[Transporteur]]`)** : Permet à un auditeur de naviguer visuellement dans le réseau de résilience logistique.
*   **Ouvrir dans Obsidian** : Sélectionnez simplement le dossier `obsidian_vault` comme coffre (Vault) dans votre application Obsidian pour explorer le journal d'audit.
