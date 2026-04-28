---
name: patrimonial-structuring
description: >
  Skill ECA EXPERTISE pour toute question de structuration patrimoniale,
  successorale ou familiale : démembrement de propriété, quasi-usufruit,
  régimes matrimoniaux, contrat de mariage, changement de régime, droit des
  successions, assurance-vie, pacte successoral (RAAR), SCI patrimoniale,
  stratégies intergénérationnelles. Déclencher sur : quasi-usufruit, usufruit,
  nue-propriété, démembrement, régime matrimonial, communauté, séparation de
  biens, participation aux acquêts, contrat de mariage, succession, héritage,
  donation, assurance-vie, clause bénéficiaire, RAAR, réserve héréditaire,
  quotité disponible, SCI familiale, stratégie patrimoniale complexe.
  NE PAS utiliser si la demande porte uniquement sur la transmission d'entreprise
  sans dimension patrimoniale personnelle (→ diagnostic-transmission), ou sur
  un calcul de PV pur (→ calcul-plus-value).
---

# Skill : Structuration patrimoniale et successorale — ECA EXPERTISE

Ce skill existe parce que les dossiers patrimoniaux complexes mobilisent
simultanément le droit civil (régimes matrimoniaux, successions, libéralités),
le droit fiscal (DMTG, IFI, assurance-vie) et des mécanismes spécifiques
(quasi-usufruit, RAAR, démembrement) que les skills généralistes ne traitent
pas avec la profondeur requise. C'est aussi le cœur du module AUREP RS6827.

---

## PHASE 0 — Recherche dossier en cours

Si un nom de client ou de famille est mentionné :

```
conversation_search(query="[nom client ou famille]")
```

- Historique trouvé → lire avant d'analyser, signaler discrètement
- Nouveau dossier → continuer normalement

---

## PHASE 0b — Routing

```
Transmission d'entreprise pure sans dimension familiale ? → diagnostic-transmission
Calcul PV ou coût fiscal ? → calcul-plus-value en complément
Rédaction acte (statuts SCI, donation, contrat de mariage) ? → redaction-acte
→ Analyse de fond patrimoniale : continuer ici
```

---

## PHASE 1 — Raisonnement préalable

Avant toute recherche, identifier mentalement :

1. **Situation familiale** — marié (quel régime ?), pacsé, concubin, divorcé,
   veuf. Le régime matrimonial conditionne tout le reste.
2. **Composition du patrimoine** — professionnel, immobilier, financier,
   assurance-vie. Distinguer biens propres / biens communs / indivis.
3. **Objectif prioritaire** — protéger le conjoint ? Transmettre aux enfants ?
   Réduire la fiscalité ? Anticiper une incapacité ?
4. **Horizon temporel** — transmission immédiate, progressive sur 15 ans,
   ou successorale à terme.
5. **Contraintes** — réserve héréditaire, enfants de lits différents,
   héritiers vulnérables, dette fiscale latente.

---

## PHASE 1b — AUREP fetch obligatoire

Si la demande touche démembrement, quasi-usufruit, régimes matrimoniaux, successions ou LMNP :

```
# Usufruit, quasi-usufruit, Art. 13-5 CGI
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/M5_usufruit_article_13_5_CGI.md")

# Usufruit de droits sociaux
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/M8_usufruit_droits_sociaux.md")

# Actualités patrimoniales (LMNP, abattement retraite, LF 2026)
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/M10_actualites_patrimoniales.md")
```

Ne pas improviser sur ces sujets sans avoir chargé le module correspondant.
Les modules AUREP contiennent la doctrine vérifiée — ils priment sur la mémoire du modèle.

---

## PHASE 2 — Sources

Fetcher avant toute vérification :

```
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md")
```

Charger le fichier de référence correspondant au domaine :

| Sujet | Fichier |
|-------|---------|
| Démembrement, quasi-usufruit | `references/demembrement-quasi-usufruit.md` |
| Régimes matrimoniaux | `references/regimes-matrimoniaux.md` |
| Successions, libéralités | `references/successions-liberalites.md` |
| Assurance-vie | `references/assurance-vie.md` |

**Balise incertitude :**
```
⚠️ INCERTAIN — [point] : à vérifier via [source] avant conseil définitif.
```

---

## PHASE 3 — Analyse par domaine

Charger le fichier de référence du domaine concerné avant d'analyser.
Ne pas improviser sur ces sujets sans avoir lu le fichier correspondant —
les mécanismes sont techniques et les erreurs coûteuses.

---

## PHASE 4 — Structure de sortie

```
ANALYSE PATRIMONIALE ET SUCCESSORALE
[Client — Date — Référence YD]

I. SITUATION FAMILIALE ET PATRIMONIALE
   1.1 Régime matrimonial applicable
   1.2 Composition du patrimoine (propres / communs / indivis)
   1.3 Héritiers réservataires et quotité disponible
   1.4 Fiscalité latente identifiée

II. PROBLÉMATIQUE(S) IDENTIFIÉE(S)

III. ANALYSE
   [Par domaine selon la situation]
   [Balises ⚠️ INCERTAIN sur toutes les zones grises]

IV. OUTILS ET STRATÉGIES RECOMMANDÉS
   [Tableau : Outil | Avantage | Condition | Coût fiscal | Risque]

V. CHIFFRAGE INDICATIF
   [Avant/après optimisation — caractère indicatif rappelé]

VI. POINTS DE VIGILANCE
   — Réserve héréditaire respectée ?
   — Risque abus de droit ?
   — Garanties à prévoir ?
   — Notaire obligatoire ?

VII. PROCHAINES ÉTAPES
```

---

## PHASE 5 — Livrable Word

- Corps : Raleway sz=22, justifié, **#999999**
- H1/H2 : Raleway gras, **#C00000**
- Signature : Raleway gras sz=22, **#495864**, centré
- Charger skill `docx` + déclencher `legal-hallucination-checker`

---

## Intégration réponse Casus

Si Yoann colle un output Casus dans la conversation :
- L'utiliser comme base documentaire CGI/BOFiP certifiée
- Ne pas redupliquer les vérifications déjà faites par Casus
- Rôle Claude : raisonnement patrimonial global, jurisprudence civile (Cass., CA),
  rédaction Word ECA, analyse régimes matrimoniaux
- Indiquer : "Base Casus intégrée — construction sur sa documentation"


---

## ENRICHISSEMENT — Exemples bien formés

### Exemple 1 — Donation de la nue-propriété de la holding (chef d'entreprise 58 ans)

**Input :**
> « Mon client, dirigeant 58 ans, marié sous communauté légale, détient 100 % d'une
> holding animatrice valorisée 4 M€ qui contrôle 3 sociétés opérationnelles. Il
> veut transmettre à ses 2 enfants tout en conservant le pouvoir et les revenus.
> Quelle structuration ? »

**Structure de réponse attendue :**

I. Situation : régime communauté légale → titres acquis pendant le mariage = communs.
   Donation de titres communs nécessite consentement du conjoint (Art. 1422 C. civ.).

II. Problématique : double objectif — démembrement (transmission NP + maintien pouvoir
   et revenus via usufruit) + Dutreil (abattement 75 %).

III. Règles : Art. 669 CGI (barème usufruit/NP — 58 ans = NP 60 % / USU 40 %),
    Art. 787 B CGI (Dutreil EIC 6 ans depuis LF 2026), Art. 1832-2 C. civ. (info
    conjoint commun), Art. 1844 C. civ. (droit de vote USU/NP), AUREP M5 + M8.

IV. Schéma recommandé :
    1. Engagement collectif de conservation 2 ans avec dirigeant + enfants
    2. Donation NP des titres aux enfants (60 % de 4 M€ = 2,4 M€ valeur taxable)
    3. Application Dutreil 75 % → assiette = 600 k€
    4. Abattement 100 k€ × 2 enfants = 200 k€
    5. Assiette taxable nette = 400 k€ → DMTG ≈ 70 k€ (barème Art. 777)
    6. Engagement individuel 4 ans + direction effective 3 ans

V. Chiffrage indicatif :
    Sans Dutreil ni NP : DMTG ~ 770 k€
    Avec Dutreil seul : DMTG ~ 170 k€
    Avec Dutreil + NP : DMTG ~ 70 k€
    Économie : 700 k€ vs scénario sans optimisation.

VI. Vigilance :
    ⚠️ INCERTAIN — qualification holding animatrice à confirmer (vérifier critères
       Cass. com. + BOFiP BOI-ENR-DMTG-10-20-40-10)
    🔴 Consentement du conjoint obligatoire (titres communs) — acte irrévocable
    🟠 Co-signature de l'engagement collectif par les enfants si donation à terme rapproché

VII. Prochaines étapes : RDV notaire / convocation conjoint / signature ECC dans le mois.

### Exemple 2 — Donation + quasi-usufruit signée AVANT cession (risque fictivité)

**Position recommandée :**
> « La convention de quasi-usufruit doit être prévue **avant ou pendant** la cession
> et formalisée par acte notarié pour être opposable. Une convention signée
> postérieurement à la cession est susceptible d'être qualifiée de fictive (CE
> 5 décembre 2014 n°370432, et 14 octobre 2015 n°374288).
>
> Pour sécuriser :
> 1. Acte de donation NP avec clause de quasi-usufruit prévue ab initio
> 2. Réserve d'emploi ou garanties (caution, hypothèque) au profit du nu-propriétaire
> 3. Convention de quasi-usufruit signée concomitamment à la donation, pas après cession
> 4. Mention dans l'acte de cession de l'existence de la convention »

---

## ENRICHISSEMENT — Mini-template décision changement de régime matrimonial

**Conditions cumulatives (Art. 1397 C. civ.) :**
- Mariage de plus de 2 ans (depuis loi 23/03/2019, le délai 2 ans + intérêt famille a évolué)
- Acte notarié homologué par le tribunal si enfants mineurs ou opposition
- Information personnelle des enfants majeurs et créanciers (3 mois opposition)
- Publicité : mention en marge de l'acte de mariage

**Cas typique — passage communauté → participation aux acquêts :**
1. Liquidation préalable de la communauté (acte notarié)
2. Adoption du nouveau régime (acte notarié)
3. Calcul de la créance de participation au moment de la dissolution
4. Coût fiscal : droit de partage 1,1 % sur l'actif partagé (Art. 746 CGI)

⚠️ INCERTAIN — la qualification de l'opération comme « partage » au sens fiscal
   varie selon les juridictions. Vérifier la position du SIE compétent avant chiffrage.


---

## 🛡️ PHASE FINALE — Auto-déclenchement legal-hallucination-checker

⚠️ **OBLIGATOIRE — Étape non sautable.**

Avant remise du livrable au client ou à Yoann, déclencher automatiquement :

```
1. Charger skill legal-hallucination-checker
2. Extraire toutes les références citées :
   — Articles de code (CGI, C. civ., C. com., LPF, CMF, CSS, CPI...)
   — Jurisprudence (CE, Cass., CAA, TA, Cons. const.)
   — BOFiP (BOI-...)
   — Lois, ordonnances, décrets
3. Vérifier chacune via MCP Légifrance avec au minimum 2 stratégies de recherche
4. Produire le rapport de vérification (score /100)
5. Décision :
   — Si score ≥ 70 et 0 ⛔ HALLUCINATION → livrer + mentionner « Vérifié — score [N]/100 »
   — Si score < 70 ou présence de ⛔ HALLUCINATION → NE PAS LIVRER
     → Corriger les références fautives → relancer le checker → attendre validation Yoann
```

**Marquage final obligatoire dans le livrable :**
> *« Vérifié via legal-hallucination-checker — [N] références contrôlées — score [X]/100 »*

Cette mention est la signature qualité ECA. Sa présence engage Yoann ;
son absence signifie que la vérification n'a pas eu lieu.


---

## ✅ CHECKLIST AVANT REMISE

Valider mentalement chaque point avant d'envoyer la réponse :

- [ ] Toutes les références citées vérifiées via MCP Légifrance (Pattern 3 ci-dessous)
- [ ] Zones d'incertitude explicitement balisées avec ⚠️ INCERTAIN
- [ ] La conclusion répond directement et précisément à la question posée
- [ ] Niveau de risque justifié par un argumentaire (pas seulement affiché)
- [ ] Aucune position incertaine présentée comme certaine
- [ ] legal-hallucination-checker déclenché et score ≥ 70/100
- [ ] Charte graphique ECA respectée si livrable Word (#999999 / #C00000 / #495864)
- [ ] Référence YD + expert-comptable signataire mentionnée
- [ ] Régime matrimonial qualifié et conséquences analysées
- [ ] Réserve héréditaire vérifiée si donation ou démembrement
- [ ] Module(s) AUREP fetché(s) si sujet couvert (M5 / M8 / M10)
- [ ] Risque d'abus de droit / fictivité examiné explicitement
- [ ] Notaire requis identifié si acte authentique nécessaire

**Si un seul item n'est pas validé → ne pas livrer. Reprendre la phase concernée.**


---

## 🔍 ANNEXE — Commandes MCP Légifrance exactes

Ne plus écrire « via MCP Légifrance » sans la commande. Utiliser les patterns suivants :

### Articles de code
```
rechercher_code(code_name="Code général des impôts", search="[numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Code de commerce", search="[numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Code civil", search="[numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Livre des procédures fiscales", search="L. [numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Code monétaire et financier", search="L. [numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Code du travail", search="L. [numéro]", champ="NUM_ARTICLE")
```

### Jurisprudence
```
# Conseil d'État, CAA, TA
rechercher_jurisprudence_administrative(search="[numéro affaire]", champ="NUM_AFFAIRE")
# Cour de cassation
rechercher_jurisprudence_judiciaire(search="[numéro pourvoi]", champ="NUM_AFFAIRE")
# Conseil constitutionnel
rechercher_decisions_constitutionnelles(search="[N°-AAAA QPC]")
```

### Doctrine et textes officiels
```
# BOFiP
web_fetch("https://bofip.impots.gouv.fr/bofip/[identifiant]")
# Loi / ordonnance / décret
recherche_journal_officiel(search="[numéro ou titre]", text_types=["LOI"])
# Texte consolidé
rechercher_dans_texte_legal(search="[mots-clés]")
```

**Règle de robustesse** : avant de conclure à l'inexistence d'une référence,
tenter au minimum 2 stratégies (numéro exact + mots-clés + date approximative).
Une référence non trouvée via MCP ≠ référence inexistante.
