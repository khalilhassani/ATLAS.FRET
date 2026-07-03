---
id: bench-tc-4
date: 2026-07-03 15:47:51
status: SUCCESS
conformity_score: 0.92
latency_seconds: 3.1298
api_cost_usd: 0.000150
carrier: "Atlas Transit Maroc"
---

# Rapport d'Audit ATLASFret - [[bench-tc-4]]

- **ID de Corrélation** : `bench-tc-4`
- **Date de Supervision** : `2026-07-03 15:47:51`
- **Statut Final de Requête** : `SUCCESS`
- **Score Global de Conformité (SkillSpector)** : `92.0/100`

## 📝 Alerte ONCF Reçue
> Demande de déroutement routier sur l'axe Fès-Oujda pour M. Benjelloun (Téléphone: 0612345678, CIN: AB123456, salaire: 8500 MAD). Chargement de ciment de 5 tonnes.

## 🛡️ Vérification de Sécurité (Obsidian Oversight)
- **Alerte d'intrusion (Jailbreak / Injection)** : ✅ Requête Saine
- **Détails de l'anomalie** : Aucune anomalie détectée.
- **Type de cargaison** : `standard`
- **Poids de fret** : `5.0 tonnes`
- **Valeur déclarée** : `8500.0 MAD`

## 🚛 Solution Alternative Proposée (Transbordement Routier)
- **Transporteur Recommandé** : [[Atlas Transit Maroc]]
- **Numéro de Patente** : `MA-9102394`
- **Conformité CNSS (Loi 16-99)** : `Conforme (OK)`
- **Plan de Route Proposé** : Gare-Fes-Ville ➔ Plateforme Logistique Fès-Saïss ➔ Autoroute A3 - Reroutage vers Fès

## 🔐 Gestion des Séquestres (Escrow Gate)
- **État d'Escrow** : RELEASED (Auto-Approuvé)
- **Montant Bloqué** : `2100.00 MAD`
- **Justification de suspension** : Validation automatique standard.

## 📋 Journal d'Audit Détaillé (LangGraph Log)
- 🛡️ Nœud 'Sanitize Input' : Démarrage du filtrage de sécurité...
- ℹ️ Masquage PII : CIN masquée.
- ℹ️ Masquage PII : Téléphone masqué.
- ℹ️ Masquage PII : Rémunération masquée.
- ✅ Requête saine. Pas d'attaque détectée.
- 📈 Nœud 'Query Knowledge Graph' : Analyse de la topologie de transport...
- 📦 Type de fret identifié : Standard
- ⚖️ Poids : 5.0 tonnes
- 💰 Valeur : 8500.0 MAD
- 📍 Destination : Fès
- 🚧 Ligne ONCF bloquée : Ligne-Fes-Oujda
- 🚉 Gare de blocage identifiée : Gare de Fès-Ville (Fès)
- 🏢 Hub de transbordement : Plateforme Logistique Fès-Saïss
- 🚛 Flottes routières de secours candidates : 3 trouvé(s)
- 🧐 Nœud 'Skill Spector' : Audit de conformité réglementaire...
- 📝 Audit de Trans-Maro-Fret SARL complété. Score = 0.88
- 📝 Audit de Trans-Maro-Fret SARL complété. Score = 0.88
- 📝 Audit de Atlas Transit Maroc complété. Score = 0.92
- 🔒 Nœud 'Obsidian Security Gate' : Vérification des seuils Obsidian...
- 📊 Score de conformité : 0.92 (Seuil requis : 0.7)
- 💼 Nœud 'Finalize Routing' : Clôture du plan de déroutement...
- 🔐 Paiement Séquestre initié: ESC-D10AE7EC d'un montant de 2100.00 MAD bloqué.
