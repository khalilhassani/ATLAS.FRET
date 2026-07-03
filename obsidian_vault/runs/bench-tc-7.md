---
id: bench-tc-7
date: 2026-07-03 15:48:00
status: PENDING_HUMAN_VALIDATION
conformity_score: 0.85
latency_seconds: 3.3177
api_cost_usd: 0.000150
carrier: "Maghrib Logistique S.A."
---

# Rapport d'Audit ATLASFret - [[bench-tc-7]]

- **ID de Corrélation** : `bench-tc-7`
- **Date de Supervision** : `2026-07-03 15:48:00`
- **Statut Final de Requête** : `PENDING_HUMAN_VALIDATION`
- **Score Global de Conformité (SkillSpector)** : `85.5/100`

## 📝 Alerte ONCF Reçue
> Axe Tanger-Kenitra bloqué. Rerouter en urgence un conteneur d'Acide Nitrique toxique (15 tonnes, valeur 140000 MAD) depuis le port Tanger Med vers Kenitra.

## 🛡️ Vérification de Sécurité (Obsidian Oversight)
- **Alerte d'intrusion (Jailbreak / Injection)** : ✅ Requête Saine
- **Détails de l'anomalie** : Aucune anomalie détectée.
- **Type de cargaison** : `chemical`
- **Poids de fret** : `15.0 tonnes`
- **Valeur déclarée** : `140000.0 MAD`

## 🚛 Solution Alternative Proposée (Transbordement Routier)
- **Transporteur Recommandé** : [[Maghrib Logistique S.A.]]
- **Numéro de Patente** : `MA-7748190`
- **Conformité CNSS (Loi 16-99)** : `Conforme (OK)`
- **Plan de Route Proposé** : Gare-Tanger-Med ➔ Plateforme Logistique Tanger Free Zone ➔ Autoroute A3 - Reroutage vers Tanger

## 🔐 Gestion des Séquestres (Escrow Gate)
- **État d'Escrow** : LOCKED (Validation HITL Requise)
- **Montant Bloqué** : `6300.00 MAD`
- **Justification de suspension** : Transport de produits chimiques classés exigeant une double signature.

## 📋 Journal d'Audit Détaillé (LangGraph Log)
- 🛡️ Nœud 'Sanitize Input' : Démarrage du filtrage de sécurité...
- ✅ Requête saine. Pas d'attaque détectée.
- 📈 Nœud 'Query Knowledge Graph' : Analyse de la topologie de transport...
- 📦 Type de fret identifié : Chimique classé
- ⚖️ Poids : 15.0 tonnes
- 💰 Valeur : 140000.0 MAD
- 📍 Destination : Tanger
- 🚧 Ligne ONCF bloquée : Ligne-Tanger-Kenitra
- 🚉 Gare de blocage identifiée : Gare de Tanger Med (Tanger)
- 🏢 Hub de transbordement : Plateforme Logistique Tanger Free Zone
- 🚛 Flottes routières de secours candidates : 1 trouvé(s)
- 🧐 Nœud 'Skill Spector' : Audit de conformité réglementaire...
- 📝 Audit de Maghrib Logistique S.A. complété. Score = 0.85
- 🔒 Nœud 'Obsidian Security Gate' : Vérification des seuils Obsidian...
- 📊 Score de conformité : 0.85 (Seuil requis : 0.7)
- ⚠️ Suspension HITL : Fret chimique détecté.
- 💼 Nœud 'Finalize Routing' : Clôture du plan de déroutement...
