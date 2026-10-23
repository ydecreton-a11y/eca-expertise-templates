---
name: due-diligence-juridique
description: >
  Audit de due diligence juridique, fiscal et social d'une cible pour ECA
  EXPERTISE (acquisition, cession, entrée au capital, fusion), toujours pour un
  camp : grille d'analyse, revue de la data room et des contrats clés, passif
  latent, rapport de DD avec cotation des risques et traduction en instructions
  de négociation (prix, conditions, garanties). Déclencher sur : due diligence,
  DD, audit juridique, audit d'acquisition, audit fiscal de cible, revue de
  passif, data room, rapport de DD, vendor due diligence.
  NE PAS utiliser pour rédiger la GAP (→ gap), le protocole ou la lettre
  d'intention (→ protocole-cession), une cession de fonds (→ cession-fonds),
  une question de droit sans cible (→ consultation-juridique) ou un seul contrat
  (→ analyse-contrat).
---

# Skill : Due diligence juridique et fiscale — ECA EXPERTISE

> **Socle** : charger `socle-eca` — ouverture du dossier (§ 1), carte des
> connecteurs (§ 2), règles de vérification (§ 3), accès aux modèles (§ 4),
> pièges datés (§ 5), standard de rédaction (§ 6), garde-fous (§ 7), Word ECA
> (§ 8), fin de livrable (§ 9). Un output Casus collé est une base documentaire
> à recouper (§ 3.4). Aucun taux, seuil ou délai n'est repris de mémoire.

## PHASE 0b — Routing

```
Cible identifiée, opération d'acquisition/cession en cours ? → continuer ici
Question de droit théorique sans cible ? → consultation-juridique
Un seul contrat à analyser ? → analyse-contrat
```

## PHASE 1 — Sources et vérifications

Carte des connecteurs (socle § 2) : Radar (identité, dirigeants, groupe,
dépôts des comptes), Pennylane si la cible est cliente, Data.gouv, Légifrance
(conventions collectives applicables), jurisprudence (Pourvoi, LibreJustice)
sur les litiges identifiés. Chaque constat renvoie à la pièce de la data room
qui le fonde (référence de la pièce).

## PHASE 2 — Périmètre de la DD selon l'opération

| Type d'opération | Focus prioritaire |
|------------------|-------------------|
| Cession de titres | Passif fiscal latent, litiges sociaux, contrats clés, pacte d'associés |
| Cession de fonds | Baux commerciaux, contrats de travail L1224-1, licences, marques |
| Fusion / TUP | Traité d'apport, valeurs d'apport, passif transmis, agrément clients |
| Entrée au capital | Statuts, pacte, valorisation, droits préférentiels, anti-dilution |

---

## PHASE 3 — Grille d'analyse standard

### Juridique
- Forme sociale, capital, actionnariat actuel (historique des cessions)
- Statuts : clauses d'agrément, préemption, inaliénabilité
- Pacte d'associés en vigueur : droits préférentiels, tag-along, drag-along
- Litiges en cours ou menaces identifiées
- Contrats essentiels : durée, renouvellement, clauses de résiliation
  automatique en cas de changement de contrôle

### Fiscal
- Déclarations IS des 3 dernières années — cohérence
- Redressements fiscaux en cours ou prescrits depuis moins de 3 ans
- TVA : régularisations en cours, rappels potentiels
- Dividendes distribués : régularité, base légale
- PV latentes sur actifs

### Social
- Effectif, contrats atypiques, CDD/intérim en cours
- Accords collectifs opposables
- Provisions pour litiges prud'homaux
- Art. L1224-1 : transfert automatique si cession de fonds

### Immobilier / actifs
- Titres de propriété ou baux : durée résiduelle, loyers, renouvellement
- Actifs incorporels : marques déposées (vérifier INPI), brevets, licences

---

## PHASE 4 — Structure du rapport DD

```
RAPPORT DE DUE DILIGENCE
[Cible — Acquéreur — Date — Référence YD]

EXECUTIVE SUMMARY
Appréciation globale du risque : 🔴 Élevé / 🟠 Modéré / 🟢 Faible
Points bloquants identifiés : [liste]
Points à garantir dans la GAP : [liste]

I. PÉRIMÈTRE ET MÉTHODOLOGIE

II. ANALYSE JURIDIQUE
   [Sous-sections selon grille Phase 3]
   [Cotation de chaque risque : 🔴/🟠/🟢]

III. ANALYSE FISCALE
   [Idem]

IV. ANALYSE SOCIALE
   [Idem]

V. SYNTHÈSE DES RISQUES
   [Tableau : Risque | Domaine | Criticité | Recommandation GAP]

VI. RECOMMANDATIONS
   6.1 Points à négocier sur le prix
   6.2 Clauses de GAP recommandées
   6.3 Conditions suspensives suggérées
   6.4 Points à surveiller post-closing
```

---

## Passage de relais à la GAP et au protocole

Chaque risque de la synthèse est traduit, dans le rapport, en **instruction de
négociation** : ajustement du prix, condition suspensive, déclaration
spécifique, garantie spécifique sans franchise, séquestre. La rédaction et le
calibrage des garanties relèvent du skill `gap` (avec la même posture), les
conditions et le prix du skill `protocole-cession`. Ne pas rédiger ici de
clauses de garantie concurrentes.

Data room incomplète : lister précisément les zones non documentées, les
signaler dans le résumé (« DD partielle — zones non documentées : [...] ») et
demander les compléments avant la signature de la lettre d'intention.

## EXEMPLE — Rapport DD bien formé (extrait)

**Contexte :** Acquisition 100% des titres de SAS Plâtrerie X (25 salariés, CA 4,2 M€).

**Executive Summary (extrait) :**
> « **Appréciation globale : 🟠 Risque modéré.**
>
> Trois points appellent une vigilance particulière :
> 1. Deux contrats clients (60 % du CA cumulé) comportent une clause de
>    changement de contrôle exigeant l'accord préalable du donneur d'ordre.
>    **Action :** purger les clauses avant closing (condition suspensive).
> 2. Un litige prud'homal en cours (réclamation 84 k€) provisionné à 30 k€.
>    **Action :** clause GAP spécifique non plafonnée, sans franchise.
> 3. Redressement URSSAF en cours d'instruction (montant non chiffré).
>    **Action :** clause GAP fiscale/sociale sur prescription légale + séquestre.
>
> Aucun point bloquant identifié, opération réalisable sous réserve des trois
> conditions ci-dessus. »

**❌ Ce qui est insuffisant :**
> « La cible présente quelques risques. Une GAP est recommandée. »

---

## ✅ CHECKLIST AVANT REMISE

Valider mentalement chaque point avant d'envoyer la réponse :

- [ ] Toutes les références citées vérifiées via MCP Légifrance (voir annexe en fin de skill)
- [ ] Zones d'incertitude explicitement balisées avec ⚠️ INCERTAIN
- [ ] La conclusion répond directement et précisément à la question posée
- [ ] Niveau de risque justifié par un argumentaire (pas seulement affiché)
- [ ] Aucune position incertaine présentée comme certaine
- [ ] legal-hallucination-checker déclenché et score ≥ 70/100
- [ ] Word ECA conforme au socle § 8 (corps noir ; titres d'actes noir gras)
- [ ] Référence YD + expert-comptable signataire mentionnée
- [ ] Périmètre DD (titres / fonds / fusion) confirmé en tête
- [ ] Grille 4 domaines couverte (juridique / fiscal / social / actifs)
- [ ] Cotation 🔴/🟠/🟢 portée sur chaque risque identifié
- [ ] Clauses GAP recommandées formulées concrètement
- [ ] Conditions suspensives suggérées listées
- [ ] Données de la data room manquantes signalées explicitement

**Si un seul item n'est pas validé → ne pas livrer. Reprendre la phase concernée.**

---

