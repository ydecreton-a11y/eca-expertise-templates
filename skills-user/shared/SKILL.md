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

## Charte graphique ECA EXPERTISE — SPECS COMPLÈTES

### Typographie corps et titres

| Élément | Police | Taille | Couleur | Style |
|---------|--------|--------|---------|-------|
| Corps | Raleway | 11pt (sz=22) | **#999999** | Justifié |
| H1 | Raleway | 14pt (sz=28) | **#C00000** | Gras |
| H2 | Raleway | 12pt (sz=24) | **#C00000** | Gras |
| Signature | Raleway | 11pt (sz=22) | **#495864** | Gras, centré |

⚠️ **JAMAIS #808080** — erreur corrigée, utiliser **#999999** pour le corps.

---

### En-tête première page (header first / rId9)

Structure : Logo ECA à gauche + ligne horizontale rouge #C00000

**3 agences — Raleway 8pt (sz=16), couleur #495864 :**

| Agence | Adresse | Tél | Email |
|--------|---------|-----|-------|
| CAMBRAI | 60 Rue des Rôtisseurs, 59400 | 03 27 72 00 10 | accueilcambrai@eca-groupe.com |
| ARRAS | 92 Rue Raoul Briquet, 62223 — BP 60042 | 03 21 07 45 04 | accueilarras@eca-groupe.com |
| VALENCIENNES | 2 Av. Sénateur Girard, 59300 | 03 74 22 03 08 | accueilvalenciennes@eca-groupe.com |

---

### Pied de page première page (footer first / rId10)

> Société d'Expertise Comptable Inscrite au Tableau de l'Ordre de la Région Nord Pas-de-Calais  
> S.A.R.L. au capital de 300 000 € – Siret : 687 220 087 00021 – 687 220 087 R.C.S. Douai  
> N° TVA Intracommunautaire : FR 60 687 220 087 – Code APE : 6920 Z

Centré, Raleway 8pt (sz=16), couleur #495864.

**Pages 2 et suivantes : en-tête ET pied de page VIDES.**

---

### Template DOCX — méthode complète (ref_sas / ref_sci)

```
Template de base SAS : Devis_ECA_Constitution_SAS.docx  (ref_sas)
Template de base SCI : Devis_ECA_Constitution_SCI.docx  (ref_sci)
Méthode : unpack → injection body XML → repack via pack.py --validate false
JAMAIS recréer from scratch.
```

**Marges validées (dxa) :**

| Côté | Valeur |
|------|--------|
| Top / Right / Bottom / Left | 1417 dxa |
| Header distance | 397 dxa |
| Footer distance | 397 dxa |

**sectPr — relations :**

| rId | Rôle |
|-----|------|
| rId7 | Header default — vide (pages 2+) |
| rId8 | Footer default — vide (pages 2+) |
| rId9 | Header first — logo + agences |
| rId10 | Footer first — mentions légales |

`titlePg` activé. `cols space=720`.

**Prestations SAS (numId=12) :**
1. Conseil/assistance structuration statuts
2. Rédaction statuts SAS
3. PV assemblée constitutive + nomination Président
4. Dépôt capital + attestation bancaire
5. Publicité légale (JAL + BODACC)
6. Immatriculation greffe
7. Ouverture registre mouvements titres + comptes actionnaires
8. RBE
9. Remise Kbis
10. Avis et conseils

> PAS de déclaration de conformité. Honoraires : 1 800 € HT / 2 160 € TTC / 500 € débours.

**Prestations SARL :** PAS d'attestation dépôt CAC. PAS de registre de mouvement de titres. Même grille tarifaire.

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
Calcul fiscal, taux         → Section "Taux fiscaux vérifiés 2026"
Règle controversée          → Section "Règles fiscales définitivement établies"
Démembrement / LMNP         → Section "URLs AUREP actives"
Vérification référence      → Section "Outils MCP Légifrance"
Livrable Word               → Section "Charte graphique ECA EXPERTISE"
Base de données             → Section "Bases Notion ECA"
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
