---
name: shared
description: >
  Référentiel partagé ECA EXPERTISE. Contient : charte graphique, méthode DOCX,
  bases Notion, équipe ECA, URLs AUREP. Les taux fiscaux, seuils et règles
  juridiques sont dans sources-legales.md (unique source de vérité).
  Fetché dynamiquement par les autres skills via GitHub.
  NE PAS utiliser comme skill standalone — c'est un référentiel.
---
# Shared — Référentiel ECA EXPERTISE

## Sources de vérité — Routage

| Besoin | Fichier à fetcher |
|--------|------------------|
| Taux fiscaux, seuils, articles, règles définitives | `sources-legales.md` (même dossier) |
| Charte graphique, méthode DOCX, Notion, équipe, AUREP | Ce fichier (`shared/SKILL.md`) |
| Orchestration / chaîne d'activation | `CLAUDE.md` (racine repo) |

URL canonique sources-legales :
```
https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md
```

---

## Charte graphique ECA EXPERTISE — SPECS COMPLÈTES

### Typographie corps et titres

| Élément | Police | Taille | Couleur | Style |
|---------|--------|--------|---------|-------|
| Corps | Raleway | 11pt (sz=22) | **#999999** | Justifié |
| H1 | Raleway | 14pt (sz=28) | **#C00000** | Gras |
| H2 | Raleway | 12pt (sz=24) | **#C00000** | Gras |
| Signature | Raleway | 11pt (sz=22) | **#495864** | Gras, centré |

⚠️ **JAMAIS #808080** — utiliser **#999999** pour le corps.

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

---

## Bases Notion ECA

| Base | Data source ID | Usage |
|------|---------------|-------|
| Veille Juridique ECA | `f201a44e-556f-4420-8f61-eec1f8cb2d5a` | Entrées veille hebdomadaire |
| Consultations | `cadd1870-11e1-4dfa-9298-7d5c5977f564` | Suivi consultations clients |
| Modèles juridiques | `bc7cbd3e-164e-4b7d-a71c-c5c5b39dbb75` | Bibliothèque actes |

---

## URLs AUREP actives

Base : `https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/`

| Module | Fichier |
|--------|---------|
| M1 | `M1_actualites_SCI.md` |
| M5 | `M5_usufruit_article_13_5_CGI.md` |
| M7 | `M7_retroplanning_transmission.md` |
| M8 | `M8_usufruit_droits_sociaux.md` |
| M9 | `M9_holdings_transmissions.md` |
| M10 | `M10_actualites_patrimoniales.md` |
| M10b | `M10b_enjeux_pacte_dutreil.md` |
| M11 | `M11_patrimoine_immobilier.md` |
| M12 | `M12_outils_civils_transmission.md` |
| DUTREIL 2026 | `DUTREIL_2026/` (4 fichiers) |

Sujets couverts et mots-clés déclencheurs détaillés → `sources-legales.md` section 9.

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

## Équipe ECA

- **Frédéric Verclytte** — Expert-Comptable Associé
- **Ludovic Jolda** — Expert-Comptable
- **Stéphane Hachette** — Expert-Comptable
- **Perrine Loiseaux** — Expert-Comptable
- **Yoann Decreton (YD)** — Juriste Droit des Affaires + Responsable Fiscal

---

## Utilisation de ce référentiel

Ce document est fetché en Phase 2 de chaque skill ECA.
Lire les sections pertinentes selon le contexte :

```
Livrable Word               → Section "Charte graphique ECA EXPERTISE"
Base de données              → Section "Bases Notion ECA"
Vérification référence       → Section "Outils MCP Légifrance"
Démembrement / LMNP          → Section "URLs AUREP actives"
Calcul fiscal, taux, seuils  → Fetcher sources-legales.md (pas ce fichier)
```

Après fetch, retourner immédiatement au skill en cours.
