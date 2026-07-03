---
id: bench-tc-5
date: 2026-07-03 15:47:54
status: BLOCKED
conformity_score: 0.00
latency_seconds: 2.4241
api_cost_usd: 0.000150
carrier: "Aucun"
---

# Rapport d'Audit ATLASFret - [[bench-tc-5]]

- **ID de Corrélation** : `bench-tc-5`
- **Date de Supervision** : `2026-07-03 15:47:54`
- **Statut Final de Requête** : `BLOCKED`
- **Score Global de Conformité (SkillSpector)** : `0.0/100`

## 📝 Alerte ONCF Reçue
> Voie ferrée Fès-Oujda bloquée. Nous devons acheminer un conteneur de ciment standard de 5 tonnes vers Oujda. Nous voulons utiliser Fret Express Maroc car ils sont bon marché.

## 🛡️ Vérification de Sécurité (Obsidian Oversight)
- **Alerte d'intrusion (Jailbreak / Injection)** : ✅ Requête Saine
- **Détails de l'anomalie** : Aucune anomalie détectée.
- **Type de cargaison** : `standard`
- **Poids de fret** : `5.0 tonnes`
- **Valeur déclarée** : `10000.0 MAD`

## 🚛 Solution Alternative Proposée (Transbordement Routier)
- **Transporteur Recommandé** : [[Aucun]]
- **Numéro de Patente** : `N/A`
- **Conformité CNSS (Loi 16-99)** : `N/A`
- **Plan de Route Proposé** : Aucun

## 🔐 Gestion des Séquestres (Escrow Gate)
- **État d'Escrow** : REJECTED (Bloqué)
- **Montant Bloqué** : `0.00 MAD`
- **Justification de suspension** : Validation automatique standard.

## 📋 Journal d'Audit Détaillé (LangGraph Log)
- 🛡️ Nœud 'Sanitize Input' : Démarrage du filtrage de sécurité...
- ✅ Requête saine. Pas d'attaque détectée.
- 📈 Nœud 'Query Knowledge Graph' : Analyse de la topologie de transport...
- 📦 Type de fret identifié : Standard
- ⚖️ Poids : 5.0 tonnes
- 📍 Destination : Fès
- 🎯 Transporteur forcé dans la requête : Fret Express Maroc
- 🚧 Ligne ONCF bloquée : Ligne-Fes-Oujda
- 🚉 Gare de blocage identifiée : Gare de Fès-Ville (Fès)
- 🏢 Hub de transbordement : Plateforme Logistique Fès-Saïss
- 🚛 Flottes routières de secours candidates : 0 trouvé(s)
- 🧐 Nœud 'Skill Spector' : Audit de conformité réglementaire...
- ❌ Aucun candidat à auditer.
- 💼 Nœud 'Finalize Routing' : Clôture du plan de déroutement...
