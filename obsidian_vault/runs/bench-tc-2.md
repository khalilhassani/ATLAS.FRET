---
id: bench-tc-2
date: 2026-07-03 15:47:48
status: SUCCESS
conformity_score: 0.92
latency_seconds: 3.3951
api_cost_usd: 0.000150
carrier: "Atlas Transit Maroc"
---

# Rapport d'Audit ATLASFret - [[bench-tc-2]]

- **ID de Corrélation** : `bench-tc-2`
- **Date de Supervision** : `2026-07-03 15:47:48`
- **Statut Final de Requête** : `SUCCESS`
- **Score Global de Conformité (SkillSpector)** : `92.0/100`

## 📝 Alerte ONCF Reçue
> Incident ONCF : Ligne Kenitra-Casablanca bloquée. Rerouter un chargement de ciment de 15 tonnes (valeur 15000 MAD) depuis la gare de Kenitra vers Casablanca.

## 🛡️ Vérification de Sécurité (Obsidian Oversight)
- **Alerte d'intrusion (Jailbreak / Injection)** : ✅ Requête Saine
- **Détails de l'anomalie** : Aucune anomalie détectée.
- **Type de cargaison** : `standard`
- **Poids de fret** : `15.0 tonnes`
- **Valeur déclarée** : `15000.0 MAD`

## 🚛 Solution Alternative Proposée (Transbordement Routier)
- **Transporteur Recommandé** : [[Atlas Transit Maroc]]
- **Numéro de Patente** : `MA-9102394`
- **Conformité CNSS (Loi 16-99)** : `Conforme (OK)`
- **Plan de Route Proposé** : Gare-Kenitra ➔ Hub Kenitra Zone Franche ➔ Autoroute A3 - Reroutage vers Kenitra

## 🔐 Gestion des Séquestres (Escrow Gate)
- **État d'Escrow** : RELEASED (Auto-Approuvé)
- **Montant Bloqué** : `6300.00 MAD`
- **Justification de suspension** : Validation automatique standard.

## 📋 Journal d'Audit Détaillé (LangGraph Log)
- 🛡️ Nœud 'Sanitize Input' : Démarrage du filtrage de sécurité...
- ✅ Requête saine. Pas d'attaque détectée.
- 📈 Nœud 'Query Knowledge Graph' : Analyse de la topologie de transport...
- 📦 Type de fret identifié : Standard
- ⚖️ Poids : 15.0 tonnes
- 💰 Valeur : 15000.0 MAD
- 📍 Destination : Kenitra
- 🚧 Ligne ONCF bloquée : Ligne-Kenitra-Casa
- 🚉 Gare de blocage identifiée : Gare de Kenitra (Kenitra)
- 🏢 Hub de transbordement : Hub Kenitra Zone Franche
- 🚛 Flottes routières de secours candidates : 1 trouvé(s)
- 🧐 Nœud 'Skill Spector' : Audit de conformité réglementaire...
- 📝 Audit de Atlas Transit Maroc complété. Score = 0.92
- 🔒 Nœud 'Obsidian Security Gate' : Vérification des seuils Obsidian...
- 📊 Score de conformité : 0.92 (Seuil requis : 0.7)
- 💼 Nœud 'Finalize Routing' : Clôture du plan de déroutement...
- 🔐 Paiement Séquestre initié: ESC-D9FD5CD6 d'un montant de 6300.00 MAD bloqué.
