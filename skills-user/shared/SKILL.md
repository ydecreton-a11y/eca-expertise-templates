---
name: shared
description: >
  Référentiel partagé ECA EXPERTISE. Fetcher systématiquement via GitHub
  avant tout calcul fiscal ou vérification BOFiP. Contient : taux fiscaux
  vérifiés 2026 (PFU 31.4%, PS 18.6%), règles définitives (150-0 B ter +
  quotient = jamais applicable), URLs AUREP actives (M5/M8/M10), outils MCP
  Légifrance, charte graphique ECA, bases Notion, équipe ECA. Ce skill est
  fetché dynamiquement depuis GitHub par les autres skills. Déclencher sur :
  fetch shared, sources-legales, taux fiscal, référence ECA, charte graphique,
  AUREP module. NE PAS utiliser comme skill standalone — c est un référentiel.
---
# Shared — Référentiel ECA EXPERTISE

URL canonique GitHub :
```
https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md
```

---

## Taux fiscaux vérifiés 2026 (LFSS loi 2025-1403)

| Paramètre | Valeur | Périmètre |
|-----------|--------|-----------|
| PFU — PV mobilières, dividendes, intérêts | **31,4 %** (12,8 % IR + 18,6 % PS) | Revenus mobiliers PP |
| PS — revenus fonciers nus | **17,2 %** | Inchangé |
| PS — plus-values immobilières | **17,2 %** → charge totale **36,2 %** | PV immo PP |
| Taux IS standard | **25 %** | Sociétés IS |
| Taux IS PME (< 42 500 € bénéfice) | **15 %** | Art. 219 I b CGI — vérifier plafond CA |
| Abattement enfant DMTG | **100 000 €** / 15 ans | Art. 779 CGI |
| DAS2 seuil déclaration 2024+ | **2 400 €** / bénéficiaire / an | BOFiP 12/02/2025 |

---

## Règles fiscales définitivement établies

Ces règles ont été vérifiées et ne doivent JAMAIS être recalculées de mémoire :

**PV 150-0 B ter + quotient 163-0 A → INAPPLICABLE**
- PV en report d'imposition (Art. 150-0 B ter CGI) → soumise à Art. 200 A, 2 ter CGI
- Régime dérogatoire avec taux historique (Cons. const. n°2016-538 QPC 22/04/2016)
- JAMAIS au barème Art. 197 → JAMAIS au quotient Art. 163-0 A
- Règle définitive : TA Bordeaux n°2301446 du 19/12/2024

**LMNP réintégration amortissements**
- Depuis 15/02/2025 (LF 2025 Art. 84, CGI Art. 150 VB III)
- Les amortissements déduits sont réintégrés dans la PV imposable
- Vérifier via MCP Art. 150 VB CGI avant tout calcul LMNP

**Apport-cession + CDHR**
- Art. 150-0 F ter CGI neutralise le gain fiscal si RFR > 500 000 €
- Ne jamais conclure à un avantage de l'apport-cession sans calcul CDHR préalable

---

## URLs AUREP actives

Base : `https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/`

| Module | Fichier | Sujets couverts |
|--------|---------|-----------------|
| M5 | `M5_usufruit_article_13_5_CGI.md` | Usufruit, Art. 13-5 CGI, quasi-usufruit |
| M8 | `M8_usufruit_droits_sociaux.md` | Usufruit de droits sociaux, dividendes en démembrement |
| M10 | `M10_actualites_patrimoniales.md` | LMNP, abattement retraite, actualités LF 2026 |

Fetcher dès que la demande touche : démembrement, quasi-usufruit, LMNP, régimes matrimoniaux,
droit des sociétés patrimonial, abattement retraite.

---

## Outils MCP Légifrance disponibles

| Outil | Usage principal |
|-------|----------------|
| `rechercher_code` | Vérifier un article de code (CGI, C. civ., C. com., LPF) |
| `rechercher_jurisprudence_administrative` | CE, CAA, TA |
| `rechercher_jurisprudence_judiciaire` | Cass., CA |
| `rechercher_decisions_constitutionnelles` | Cons. const., QPC |
| `rechercher_decisions_cnil` | CNIL |
| `recherche_journal_officiel` | Lois, ordonnances, décrets |
| `rechercher_conventions_collectives` | CCN par secteur |

Règle de robustesse : avant de conclure à l'inexistence d'une référence,
tenter au minimum 2 stratégies de recherche différentes.

---

## Charte graphique ECA EXPERTISE (rappel)

| Élément | Spécification |
|---------|---------------|
| Corps | Raleway 11pt (sz=22), justifié, **#999999** |
| H1 | Raleway gras 14pt, **#C00000** |
| H2 | Raleway gras 12pt, **#C00000** |
| Signature | Raleway gras sz=22, **#495864**, centré |
| ⚠️ JAMAIS | #808080 — couleur incorrecte, utiliser #999999 |

Template de base : `Devis_ECA_Constitution_SAS.docx` (ref_sas)
Méthode : unpack → injection XML → repack via pack.py --validate false

---

## Bases Notion ECA

| Base | Data source ID | Usage |
|------|---------------|-------|
| Veille Juridique ECA | `f201a44e-556f-4420-8f61-eec1f8cb2d5a` | Entrées veille hebdomadaire |
| Consultations | `cadd1870-11e1-4dfa-9298-7d5c5977f564` | Suivi consultations clients |
| Modèles juridiques | `bc7cbd3e-164e-4b7d-a71c-c5c5b39dbb75` | Bibliothèque actes |

---

## Équipe ECA

- **Frédéric Verclytte** — Expert-Comptable Associé
- **Ludovic Jolda** — Expert-Comptable
- **Stéphane Hachette** — Expert-Comptable
- **Perrine Loiseaux** — Expert-Comptable
- **Yoann Decreton (YD)** — Juriste Droit des Affaires + Responsable Fiscal

---

## PHASE 0 — Utilisation de ce référentiel

Ce document est fetché en Phase 2 de chaque skill ECA.
Lire les sections pertinentes selon le contexte :

```
Calcul fiscal, taux → Section "Taux fiscaux vérifiés 2026"
Règle controversée → Section "Règles fiscales définitivement établies"
Démembrement / LMNP → Section "URLs AUREP actives"
Vérification référence → Section "Outils MCP Légifrance"
Livrable Word → Section "Charte graphique ECA"
Base de données → Section "Bases Notion ECA"
```

---

## PHASE 1 — Niveaux de criticité des règles

| Règle | Criticité | Conséquence si non respectée |
|-------|-----------|------------------------------|
| PFU 31,4% (non 30%) | 🔴 Critique | Calcul erroné → préjudice client |
| 150-0 B ter + quotient = jamais | 🔴 Critique | Conseil erroné → redressement fiscal |
| LMNP réintégration amortissements | 🔴 Critique | PV sous-estimée → pénalités |
| Charte #999999 (non #808080) | 🟠 Modéré | Document non conforme |
| DAS2 seuil 2 400€ | 🟠 Modéré | Obligation déclarative manquée |

---

## PROCHAINES ÉTAPES après fetch

Une fois ce référentiel fetché, retourner immédiatement au skill en cours.
Ne pas interrompre le workflow — ce fetch est une étape intermédiaire.
