---
id: bench-tc-6
date: 2026-07-03 15:47:57
status: PENDING_HUMAN_VALIDATION
conformity_score: 0.95
latency_seconds: 3.1654
api_cost_usd: 0.000150
carrier: "Maghrib Logistique S.A."
---

# Rapport d'Audit ATLASFret - [[bench-tc-6]]

- **ID de Corrélation** : `bench-tc-6`
- **Date de Supervision** : `2026-07-03 15:47:57`
- **Statut Final de Requête** : `PENDING_HUMAN_VALIDATION`
- **Score Global de Conformité (SkillSpector)** : `95.0/100`

## 📝 Alerte ONCF Reçue
> Déroutement routier depuis la gare de Casa Voyageurs pour un chargement géant de 80 tonnes de marchandises industrielles (valeur 450000 MAD) vers Marrakech. Ligne Casa-Marrakech bloquée.

## 🛡️ Vérification de Sécurité (Obsidian Oversight)
- **Alerte d'intrusion (Jailbreak / Injection)** : ✅ Requête Saine
- **Détails de l'anomalie** : Aucune anomalie détectée.
- **Type de cargaison** : `standard`
- **Poids de fret** : `80.0 tonnes`
- **Valeur déclarée** : `450000.0 MAD`

## 🚛 Solution Alternative Proposée (Transbordement Routier)
- **Transporteur Recommandé** : [[Maghrib Logistique S.A.]]
- **Numéro de Patente** : `MA-7748190`
- **Conformité CNSS (Loi 16-99)** : `Conforme (OK)`
- **Plan de Route Proposé** : Gare-Casa-Voyageurs ➔ Plateforme Logistique Casa Mita ➔ Autoroute A3 - Reroutage vers Marrakech

## 🔐 Gestion des Séquestres (Escrow Gate)
- **État d'Escrow** : LOCKED (Validation HITL Requise)
- **Montant Bloqué** : `33600.00 MAD`
- **Justification de suspension** : Coût estimé 33600.00 MAD supérieur au seuil S_max (15000.0 MAD).

## 📋 Journal d'Audit Détaillé (LangGraph Log)
- 🛡️ Nœud 'Sanitize Input' : Démarrage du filtrage de sécurité...
- ✅ Requête saine. Pas d'attaque détectée.
- 📈 Nœud 'Query Knowledge Graph' : Analyse de la topologie de transport...
- 📦 Type de fret identifié : Standard
- ⚖️ Poids : 80.0 tonnes
- 💰 Valeur : 450000.0 MAD
- 📍 Destination : Marrakech
- 🚧 Ligne ONCF bloquée : Ligne-Casa-Marrakech
- 🚉 Gare de blocage identifiée : Gare de Casa Voyageurs (Casablanca)
- 🏢 Hub de transbordement : Plateforme Logistique Casa Mita
- 🚛 Flottes routières de secours candidates : 2 trouvé(s)
- 🧐 Nœud 'Skill Spector' : Audit de conformité réglementaire...
- 📝 Audit de Atlas Transit Maroc complété. Score = 0.92
- 📝 Audit de Maghrib Logistique S.A. complété. Score = 0.95
- 🔒 Nœud 'Obsidian Security Gate' : Vérification des seuils Obsidian...
- 📊 Score de conformité : 0.95 (Seuil requis : 0.7)
- 💲 Suspension HITL : Alerte dépassement budget S_max.
- 💼 Nœud 'Finalize Routing' : Clôture du plan de déroutement...
