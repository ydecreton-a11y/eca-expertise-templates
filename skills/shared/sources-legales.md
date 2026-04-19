# Sources juridiques et fiscales — Référentiel partagé ECA EXPERTISE

> ⚠️ CE FICHIER EST LA SOURCE CANONIQUE — hébergé sur GitHub.
> URL raw : https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md
> Toujours fetcher depuis GitHub pour avoir la version à jour.
> Ne jamais utiliser une version locale mise en cache.

---

## 1. MCP Légifrance

Toute référence légale doit y être vérifiée avant citation. Un article CGI
peut avoir été modifié par une LF récente sans que la mémoire du modèle
en soit informée.

| Besoin | Outil MCP | Paramètres clés |
|--------|-----------|-----------------|
| Article de code (CGI, C. civ., C. com., CSS, C. trav., LPF…) | `rechercher_code` | `champ: NUM_ARTICLE` + nom du code |
| Loi, ordonnance | `recherche_journal_officiel` | `text_types: ['LOI']` ou `['ORDONNANCE']` |
| Décret, arrêté | `recherche_journal_officiel` | `text_types: ['DECRET']` |
| Jurisprudence judiciaire (Cass., CA) | `rechercher_jurisprudence_judiciaire` | `panorama: True` |
| Jurisprudence administrative (CE, CAA, TA) | `rechercher_jurisprudence_administrative` | `panorama: True` |
| Décision constitutionnelle (QPC, DC) | `rechercher_decisions_constitutionnelles` | |
| Convention collective | `rechercher_conventions_collectives` | IDCC si connu |
| Recherche dans un texte précis | `rechercher_dans_texte_legal` | `text_id` + `search` |

Avant de conclure à l'inexistence : tenter au moins 2 stratégies différentes.

---

## 2. BOFiP — Doctrine fiscale opposable (Art. L80 A LPF)

**Accès :** `https://bofip.impots.gouv.fr/bofip/recherche.html?q=MOTS_CLES`

| Domaine | Référence BOFiP |
|---------|-----------------|
| Apport-cession, report 150-0 B ter | BOI-RPPM-PVBMI-30-10-60 |
| Pacte Dutreil 787 B CGI | BOI-ENR-DMTG-10-20-40 |
| Plus-values immobilières PP | BOI-RFPI-PVI |
| Plus-values mobilières PP | BOI-RPPM-PVBMI |
| Holdings animatrices | BOI-ENR-DMTG-10-20-40-10 |
| TVA — règles générales | BOI-TVA |
| Droits cession parts sociales | BOI-ENR-DMOM-10-10 |
| Intégration fiscale, QPFC | BOI-IS-GPE / BOI-IS-BASE-10-10-10 |
| DAS2, seuil déclaratif | BOI-BIC-DECLA-30-70-20 §140 |

---

## 3. Sources européennes et internationales

| Source | URL | Usage |
|--------|-----|-------|
| Droit UE | `https://eur-lex.europa.eu` | Directive mères-filiales, TVA, fusions |
| CJUE | `https://curia.europa.eu` | Liberté d'établissement, fiscalité UE |
| CEDH | `https://hudoc.echr.coe.int` | Droits fondamentaux, droit de propriété |
| Conventions fiscales | `https://www.impots.gouv.fr/conventions-fiscales` | Non-résidents |
| CADF | `https://www.impots.gouv.fr/abus-de-droit` | Avis sur 150-0 B ter, Dutreil |
| Réponses ministérielles | `https://www.assemblee-nationale.fr/dyn/recherche` | Doctrine parlementaire |
| INPI | `https://www.inpi.fr` | Marques, brevets |

---

## 4. Taux et seuils fiscaux 2026

> ⚠️ Vérifier via BOFiP/Légifrance avant tout usage opérationnel.
> Ce tableau est mis à jour manuellement après chaque LF — fetcher depuis GitHub.

| Paramètre | Valeur 2026 | Base légale |
|-----------|-------------|-------------|
| PFU global | **31,4 %** (12,8 % IR + 18,6 % PS) | Art. 200 A CGI + LFSS 2026 |
| PS sur PV mobilières/dividendes | **18,6 %** | LFSS loi 2025-1403 |
| PS sur PV immobilières / foncier nu | **17,2 %** (inchangé) | Art. 200 A CGI |
| Taux IS standard | **25 %** | Art. 219 CGI |
| Taux IS PME (≤ 42 500 €) | **15 %** | Art. 219 I b CGI |
| Abattement DMTG enfant | **100 000 €** / 15 ans | Art. 779 CGI |
| Abattement retraite cession | **500 000 €** (prorogé 31/12/2031) | Art. 238 quindecies CGI |
| Droits cession parts sociales | **3 %** | Art. 726 CGI |
| Droits cession actions | **0,1 %** | Art. 726 CGI |
| Intérêts de retard | **0,20 %**/mois | Art. 1727 CGI |
| Majoration manquement délibéré | **40 %** | Art. 1729 CGI |
| Majoration abus de droit | **80 %** | Art. L64 LPF |
| Seuil DAS2 | **2 400 €**/bénéficiaire/an | BOI-BIC-DECLA-30-70-20 §140 |

---

## 5. Articles C. civ. clés — Droit patrimonial et successoral

> Chargés par patrimonial-structuring via MCP Légifrance.
> Vérifier systématiquement avant tout conseil.

| Domaine | Articles | Code |
|---------|---------|------|
| Usufruit / Nue-propriété | Art. 578 à 624 | C. civ. |
| Quasi-usufruit | Art. 587 | C. civ. |
| Successions légales | Art. 720 à 892 | C. civ. |
| Libéralités, donations | Art. 893 à 1099 | C. civ. |
| Réserve héréditaire | Art. 912 à 930-5 | C. civ. |
| RAAR | Art. 929 à 930-5 | C. civ. |
| Régimes matrimoniaux | Art. 1387 à 1581 | C. civ. |
| Changement de régime | Art. 1397 | C. civ. |
| Communauté universelle | Art. 1526 | C. civ. |
| Avantages matrimoniaux | Art. 1515 à 1525 | C. civ. |
| Barème NP/usufruit | Art. 669 | CGI |
| Abattements DMTG | Art. 779 à 790 G | CGI |
| Assurance-vie fiscal | Art. 757 B et 990 I | CGI |
| Exonération conjoint | Art. 796-0 bis | CGI |
| IFI — assiette | Art. 964 à 983 | CGI |
