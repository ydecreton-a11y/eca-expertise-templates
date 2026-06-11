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

---

## 6. Positions fiscales vérifiées ECA (ne pas recalculer de mémoire)

| Règle | Valeur / Position | Source vérifiée |
|-------|-------------------|-----------------|
| PV 150-0 B ter + quotient 163-0 A | **JP DIVERGENTE — pas de règle absolue.** Contre : TA Bordeaux 19/12/2024 n°2301446 (200 A 2 ter = dérogatoire). Pour : TA Bordeaux 13/11/2025 n°2304900, TA Paris 13/02/2025 n°2212919, Rép. min. Lequiller n°70807 (L.80 A). Aucun arrêt CE. | **Position ECA** : toujours présenter les 2 thèses + recommander rescrit L.80 B + invocation Lequiller L.80 A. Ne jamais dire « inapplicable de facto » ni « acquis ». |
| LMNP réintégration amortissements PV | Depuis **15/02/2025** — LF 2025 Art. 84, CGI Art. 150 VB III | Vérifier Art. 150 VB via MCP avant tout calcul LMNP |
| Apport-cession + CDHR | Art. 150-0 F ter CGI neutralise le gain si RFR > 500 000 € | Vérifier via calcul-plus-value, jamais conclure à un avantage sans calcul CDHR |
| DAS2 seuil 2024+ | **2 400 €** / bénéficiaire / an (ex 1 200 €) | BOFiP 12/02/2025, BOI-BIC-DECLA-30-70-20 §140 |

---

## 7. AUREP — Modules disponibles

Base URL : `https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/`

| Module | Fichier | Sujets |
|--------|---------|--------|
| M5 | `M5_usufruit_article_13_5_CGI.md` | Usufruit, Art. 13-5 CGI, quasi-usufruit, imposition revenus en démembrement |
| M8 | `M8_usufruit_droits_sociaux.md` | Usufruit de droits sociaux, dividendes en démembrement, droits de vote |
| M10 | `M10_actualites_patrimoniales.md` | LMNP réforme 2025, abattement retraite, actualités LF 2026 |

Fetcher si la demande touche : démembrement, quasi-usufruit, LMNP, régimes matrimoniaux, abattement retraite.

---

## 8. API Entreprises — SIREN auto-lookup

```
web_fetch("https://recherche-entreprises.api.gouv.fr/search?q=[SIREN_ou_denomination]&per_page=1")
```

Déclencher systématiquement quand un SIREN ou une dénomination sociale est fournie.
Pré-remplit : dénomination exacte, forme juridique, capital, adresse, RCS, dirigeants.

---

## 9. Index des ressources GitHub — Catalogue complet

> **RÈGLE** : Avant toute réponse, scanner cet index pour identifier les ressources
> pertinentes et les fetcher. Quand Yoann ajoute une nouvelle source au repo,
> l'indexer ici immédiatement (sujet, chemin, mots-clés déclencheurs).

Base URL : `https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/`

### 9.1 Modules AUREP (formation continue — .md lisibles directement)

| Module | Fichier | Sujets / Mots-clés déclencheurs |
|--------|---------|--------------------------------|
| M1 | `aurep/M1_actualites_SCI.md` | SCI, guichet unique, usufruitier parts sociales, unanimité, DPE, valorisation usufruit cédé, réévaluation libre, droit fixe 125€ |
| M5 | `aurep/M5_usufruit_article_13_5_CGI.md` | Art. 13-5 CGI, usufruit onéreux, quasi-usufruit, imposition revenus démembrement |
| M7 | `aurep/M7_retroplanning_transmission.md` | Rétroplanning transmission, planification cession, filialisation, donation avant cession, abattement retraite, PER, réinvestissement holding |
| M8 | `aurep/M8_usufruit_droits_sociaux.md` | Usufruit droits sociaux, dividendes démembrement, droits de vote USU/NP, convention quasi-usufruit |
| M9 | `aurep/M9_holdings_transmissions.md` | Holdings, LBO, apport-cession, mère-fille, QPFC 12%, évaluation titres, paiement différé, intégration fiscale |
| M10 | `aurep/M10_actualites_patrimoniales.md` | LMNP réintégration, abattement retraite 500k€, actualités LF 2025-2026, participation acquêts |
| M10b | `aurep/M10b_enjeux_pacte_dutreil.md` | Dutreil approfondi, engagement collectif/individuel, activités éligibles, holding animatrice, sociétés interposées, valorisation, biens somptuaires |
| M11 | `aurep/M11_patrimoine_immobilier.md` | Immobilier d'entreprise, LMNP, SCI IS, OBO immobilier, apport-donation immo, SARL famille, densification patrimoniale, location nue vs meublée |
| M12 | `aurep/M12_outils_civils_transmission.md` | Donation simple, donation-partage, régime matrimonial chef entreprise, Dutreil civil, libéralités, tarif notarié |

### 9.2 Dossier DUTREIL 2026 (LF 2026 art. 23, ≥ 21/02/2026)

Chemin : `aurep/DUTREIL_2026/`

| Fichier | Contenu | Usage |
|---------|---------|-------|
| `00_DUTREIL_RF2026_MASTER.md` | Synthèse 12 sections, tableaux LF2025 vs LF2026, EIC 6 ans, biens somptuaires, holdings animatrices | Consultation, analyse juridique |
| `CHECKLIST_ENGAGEMENT.md` | Phase pré-transmission, vérifications éligibilité, formules types | Préparation actes, vérifications |
| `CHECKLIST_TRANSMISSION.md` | Pièces justificatives, points critiques DMTG, calendrier suivi | Dépôt DMTG, complétude dossier |
| `SOURCES_LEGIFRANCE.md` | Index articles CGI, LF, BOFiP, jurisprudence Dutreil | Vérification hallucination-checker |

**Mots-clés déclencheurs** : Dutreil, 787 B, 787 C, engagement collectif, engagement individuel, EIC, ECU, ECRA, transmission entreprise gratuite, exonération 75%, holding animatrice, biens somptuaires, LF 2026 art. 23

### 9.3 PDF de référence (web_fetch pour contenu)

| Fichier | Chemin | Sujets / Quand fetcher |
|---------|--------|----------------------|
| Royal Formation 2026 | `aurep/50_Actualites-juridiques-fiscales-2026-gestion-de-patrimoine.pdf` | 53 sujets patrimoine : 150-0 B ter durci, Dutreil, PER, démembrement, CE/CAA T1 2026. **Fetcher sur toute question juridique/fiscale pour vérifier couverture.** |
| Résidence fiscale 2026 | `aurep/UF2026_residence_fiscale_particuliers_E_PARIS.pdf` | Résidence fiscale, domicile fiscal, non-résidents, conventions fiscales internationales, art. 4 B CGI, critères domiciliation, exit tax |
| Revue Fiduciaire Dutreil | `aurep/La Revue Fiduciaire - Impression.pdf` | Dutreil, source RF FH 4134, régime complet post-LF 2026 |
| Revue Fiduciaire (2) | `aurep/La Revue Fiduciaire - Impression.pdf 2.pdf` | Complément RF Dutreil |
| Guide pacte d'associés | `08_Pacte_Associes/guide-de-redaction-de-pacte-d-associés.pdf` | Pacte d'associés, clauses types, rédaction, SAS, préemption, sortie conjointe, exclusion |
| Consultation mère-fille SEL | `11_Consultations/régime mère fille sel holding.pdf` | Régime mère-fille, SEL, SPFPL, holding, intégration fiscale |

### 9.4 Sources documentaires (dossiers multi-PDF)

| Dossier | Chemin | Contenu | Quand fetcher |
|---------|--------|---------|--------------|
| Démembrement immobilier entreprise | `sources/demembrement-immobilier-entreprise/` (11 parties PDF + README) | Démembrement de propriété immobilier d'entreprise, usufruit immeubles, SCI, baux | Démembrement + immobilier d'entreprise, OBO, SCI IS, usufruit immeuble professionnel |

### 9.5 Modèles d'actes (bibliothèque)

| Dossier | Contenu | Quand consulter |
|---------|---------|----------------|
| `01_Statuts/` | Statuts SAS, SARL, SARL holding, SCI, SELARL, SPFPL | Rédaction statuts |
| `02_Cessions_Titres/` | Cessions actions SAS, SELAS, parts SARL, SCI, SCM, patientèle | Cession de titres |
| `03_Fonds_Commerce/` | LOI, compromis, actes définitifs cession fonds | Cession fonds de commerce |
| `04_MA_*/` | Séquences M&A complètes (Exotel, ADEQUA, Garages Lucas) | Due diligence, M&A, protocole, GAP |
| `05_PV_Decisions/` | PV AGE, DU dissolution/liquidation/dividende | Rédaction PV, décisions |
| `06_Apport_Holding/` | Traité apport nature, CAC apports, attestation 150-0 B ter | Apport-cession, constitution holding |
| `07_Sortie_Associe_Liquidation/` | Convention crédit-vendeur, abandon compte courant | Sortie associé, liquidation |
| `08_Pacte_Associes/` | Modèle pacte SAS 42 articles + clauses sanctions | Rédaction pacte |
| `09_Conventions/` | Convention commissionnement intra-groupe (prix transfert) | Prix de transfert, conventions intragroupe |
| `10_Operationnel_Immatriculation/` | Devis ECA template, procuration, attestations | Template charte, immatriculation |
| `11_Consultations/` | Consultations fiscales (ex. filiale belge + entrepôt France) | Consultation fiscale internationale |

---

*Dernière mise à jour index : 11/06/2026*
*Règle : toute nouvelle source ajoutée au repo doit être indexée ici immédiatement.*
