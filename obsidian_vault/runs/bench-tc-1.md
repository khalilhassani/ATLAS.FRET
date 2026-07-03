---
id: bench-tc-1
date: 2026-07-03 15:47:45
status: SUCCESS
conformity_score: 0.98
latency_seconds: 9.5188
api_cost_usd: 0.000150
carrier: "Trans-Maro-Fret SARL"
---

# Rapport d'Audit ATLASFret - [[bench-tc-1]]

- **ID de Corrélation** : `bench-tc-1`
- **Date de Supervision** : `2026-07-03 15:47:45`
- **Statut Final de Requête** : `SUCCESS`
- **Score Global de Conformité (SkillSpector)** : `98.0/100`

## 📝 Alerte ONCF Reçue
> La ligne ferroviaire Fès-Oujda est interrompue par suite d'intempéries. Quels sont les transporteurs en règle avec la CNSS disposant de camions frigorifiques de plus de 10 tonnes à proximité immédiate pour acheminer le conteneur de poissons frais (12 tonnes, valeur 45000 MAD) vers Oujda ?

## 🛡️ Vérification de Sécurité (Obsidian Oversight)
- **Alerte d'intrusion (Jailbreak / Injection)** : ✅ Requête Saine
- **Détails de l'anomalie** : Aucune anomalie détectée.
- **Type de cargaison** : `perishable`
- **Poids de fret** : `10.0 tonnes`
- **Valeur déclarée** : `45000.0 MAD`

## 🚛 Solution Alternative Proposée (Transbordement Routier)
- **Transporteur Recommandé** : [[Trans-Maro-Fret SARL]]
- **Numéro de Patente** : `MA-8923011`
- **Conformité CNSS (Loi 16-99)** : `Conforme (OK)`
- **Plan de Route Proposé** : Gare-Fes-Ville ➔ Plateforme Logistique Fès-Saïss ➔ Autoroute A3 - Reroutage vers Fès

## 🔐 Gestion des Séquestres (Escrow Gate)
- **État d'Escrow** : RELEASED (Auto-Approuvé)
- **Montant Bloqué** : `4200.00 MAD`
- **Justification de suspension** : Validation automatique standard.

## 📋 Journal d'Audit Détaillé (LangGraph Log)
- 🛡️ Nœud 'Sanitize Input' : Démarrage du filtrage de sécurité...
- ✅ Requête saine. Pas d'attaque détectée.
- 📈 Nœud 'Query Knowledge Graph' : Analyse de la topologie de transport...
- 📦 Type de fret identifié : Périssable
- ⚖️ Poids : 10.0 tonnes
- 💰 Valeur : 45000.0 MAD
- 📍 Destination : Fès
- 🚧 Ligne ONCF bloquée : Ligne-Fes-Oujda
- 🚉 Gare de blocage identifiée : Gare de Fès-Ville (Fès)
- 🏢 Hub de transbordement : Plateforme Logistique Fès-Saïss
- 🚛 Flottes routières de secours candidates : 1 trouvé(s)
- 🧐 Nœud 'Skill Spector' : Audit de conformité réglementaire...
- 📝 Audit de Trans-Maro-Fret SARL complété. Score = 0.98
- 🔒 Nœud 'Obsidian Security Gate' : Vérification des seuils Obsidian...
- 📊 Score de conformité : 0.98 (Seuil requis : 0.7)
- 💼 Nœud 'Finalize Routing' : Clôture du plan de déroutement...
- 🔐 Paiement Séquestre initié: ESC-50E0B3B1 d'un montant de 4200.00 MAD bloqué.
