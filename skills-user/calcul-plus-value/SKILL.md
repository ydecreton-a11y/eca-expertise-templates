---
name: calcul-plus-value
description: >
  Skill ECA EXPERTISE pour tout calcul ou estimation de plus-value :
  immobilière (vente d'immeuble, terrain, parts SCI/SPI, LMNP, non-résidents),
  mobilière (cession de parts sociales, actions, BSPCE, crypto, PEA, AGA),
  professionnelle (BIC/BNC/BA, marchand de biens), IS (titres de participation,
  fusions 210 A/B), report/sursis (150-0 B, 150-0 B ter), exit tax, CEHR, CDHR.
  Déclencher sur : calcul plus-value, impôt cession, PV immobilière, PV mobilière,
  cession titres, vente immeuble, CEHR, CDHR, Quémener, BSPCE, LMNP, 244 bis,
  "combien je vais payer si je vends", "quel impôt si je vends mes parts".
  NE PAS utiliser si la demande est purement stratégique sans données chiffrées
  disponibles (→ diagnostic-transmission d'abord pour collecter les données).
---

# Skill : Calcul de plus-value — ECA EXPERTISE

---

## ⚡ RÈGLES FISCALES VÉRIFIÉES — ANCRÉES DANS CE SKILL

Ces règles ont été vérifiées et ne doivent JAMAIS être recalculées de mémoire.
Elles priment sur toute valeur mémorisée à l'entraînement.

| Règle | Valeur 2026 | Source vérifiée |
|-------|-------------|-----------------|
| PFU mobilier (dividendes, PV titres, intérêts) | **31,4 %** (12,8 % IR + 18,6 % PS) | LFSS loi 2025-1403 |
| PS revenus fonciers nus | **17,2 %** (inchangé) | LFSS 2025-1403 |
| PS plus-values immobilières | **17,2 %** → charge totale 36,2 % | LFSS 2025-1403 |
| PV 150-0 B ter + quotient 163-0 A | **JAMAIS applicable** | TA Bordeaux n°2301446 du 19/12/2024 |
| Mécanisme PV 150-0 B ter | Art. 200 A, 2 ter CGI (taux historique) ≠ barème Art. 197 | Cons. const. n°2016-538 QPC 22/04/2016 |
| DAS2 seuil déclaration 2024+ | **2 400 €** / bénéficiaire / an | BOFiP 12/02/2025, BOI-BIC-DECLA-30-70-20 §140 |
| LMNP réintégration amortissements | Depuis **15/02/2025** (LF 2025 Art. 84, Art. 150 VB III) | Vérifier via MCP |

**Règle 150-0 B ter + quotient — rappel critique :**
PV en report d'imposition (150-0 B ter) → soumise à Art. 200 A, 2 ter CGI (régime dérogatoire avec
taux historique) → JAMAIS au barème Art. 197 → JAMAIS au quotient Art. 163-0 A.
Ne jamais conclure à l'applicabilité du quotient sur une PV en report, même si le client invoque
une imposition exceptionnelle. Cette règle est définitive.

---

## PHASE 0 — Contexte dossier (exécuter en premier, toujours)

### Recherche automatique dans les dossiers en cours

Avant toute analyse, vérifier si ce client ou dossier a déjà été traité :

```
conversation_search(query="[nom client ou société mentionné dans la demande]")
```

Si des conversations passées existent sur ce dossier :
- Les lire pour récupérer : décisions prises, documents produits, positions
  retenues, points de vigilance identifiés
- Ne jamais reprendre de zéro un dossier déjà engagé
- Signaler en début de réponse : "Dossier retrouvé — suite de la consultation
  du [date]" ou "Nouveau dossier — aucun antécédent trouvé"

Si le nom du client n'est pas mentionné explicitement dans la demande :
- Continuer sans recherche (ne pas bloquer sur une demande générique)

## PHASE 0b — Routing

```
Données chiffrées disponibles (prix, prix de revient, dates) ? → continuer ici
Données manquantes, phase exploratoire ? → diagnostic-transmission d'abord
Besoin d'une consultation juridique sur le régime ? → consultation-juridique
  (puis revenir ici pour le chiffrage)
```

**Intégration réponse Casus :** Si Yoann colle un output Casus dans la conversation,
utiliser sa réponse comme base documentaire CGI/BOFiP certifiée, construire dessus
sans redupliquer les vérifications déjà effectuées. Indiquer : "Base Casus intégrée."

**Balise incertitude :**
```
⚠️ INCERTAIN — [paramètre] : hypothèse retenue [X]. Résultat à recalculer
   si ce paramètre est différent.
```

---

## Sources — Fetch dynamique GitHub (obligatoire avant toute vérification)

Fetcher avant d'utiliser un taux, un outil MCP ou une référence BOFiP :

```
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md")
```

Ce fetch (2 secondes) garantit les taux et références à jour.

---

## PHASE 1 — Principe cardinal

Chaque type de plus-value obéit à un régime distinct et étanche.
Confondre les régimes est une erreur professionnelle grave qui peut coûter
des dizaines de milliers d'euros au client.

**Séquence obligatoire :**
Qualifier (§2) → lire le(s) fichier(s) de référence (§3)
→ calculer → appliquer contributions (references/contributions.md)
→ vérifier obligations déclaratives (references/obligations-declaratives.md)

Vérifier les taux via `../shared/sources-legales.md` avant tout calcul.

---

## PHASE 2 — Arbre de qualification

QUESTION 1 : LE CÉDANT EXERCE-T-IL UNE ACTIVITÉ HABITUELLE D'ACHAT-REVENTE ?
  OUI → Marchand de biens (BIC) → references/pv-professionnelle.md § 10
  NON → Continuer

QUESTION 2 : LE BIEN EST-IL INSCRIT À L'ACTIF D'UNE EI/BIC/BNC/BA ?
  OUI → PV PROFESSIONNELLE → references/pv-professionnelle.md
  NON → Continuer

QUESTION 3 : LE CÉDANT EST-IL UNE PERSONNE MORALE SOUMISE À L'IS ?
  OUI → PV IS → references/pv-is.md
  NON → Continuer (PP ou société de personnes IR)

QUESTION 4 : LE CÉDANT EST-IL NON-RÉSIDENT FISCAL FRANÇAIS ?
  OUI ET bien immobilier ou SPI → Art. 244 bis A → references/regimes-speciaux.md § 4
  OUI ET titres de société française → Art. 244 bis B → references/regimes-speciaux.md § 5
  NON → Continuer

QUESTION 5 : QUEL EST LE BIEN CÉDÉ ?

  IMMEUBLE, TERRAIN, DROITS RÉELS, PARTS SCI IR :
    → Vérifier si SCI à prépondérance immobilière (SPI) → Art. 150 UB
    → PV IMMOBILIÈRE PP → references/pv-immobiliere.md
    → Correctif Quémener obligatoire si cession de parts de société de personnes
    ⚠️ LMNP : réintégration amortissements dans PV depuis 15/02/2025
      (LF 2025 Art. 84, CGI Art. 150 VB III) — vérifier via MCP
    ⚠️ AUREP fetch obligatoire si LMNP :
      web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/M10_actualites_patrimoniales.md")

  PARTS SOCIALES, ACTIONS, VALEURS MOBILIÈRES :
    → Vérifier : CCA inclus dans le prix ? → Déduire du prix de cession
    → Société liquidée ? Boni de liquidation → references/pv-mobiliere.md § 13
    → Art. 151 nonies : UNIQUEMENT sociétés de personnes IR (SNC, SCP, SARL
      de famille IR, EURL IR) — PAS les sociétés IS
    → OUI (société IR) → PV PROFESSIONNELLE → references/pv-professionnelle.md § 4
    → NON (SARL IS, SAS, SASU, EURL IS) → PV MOBILIÈRE PP → references/pv-mobiliere.md

  BSPCE → references/regimes-speciaux.md § 1
  ACTIFS NUMÉRIQUES (crypto) → references/regimes-speciaux.md § 2
  MANAGEMENT PACKAGE → references/regimes-speciaux.md § 7

---

## PHASE 3 — Fichiers de référence

Lire le fichier correspondant au type de PV qualifié en Phase 2 :

| Type | Fichier |
|------|---------| 
| PV immobilière PP | references/pv-immobiliere.md |
| PV mobilière PP | references/pv-mobiliere.md |
| PV professionnelle | references/pv-professionnelle.md |
| PV à l'IS | references/pv-is.md |
| Régimes spéciaux | references/regimes-speciaux.md |
| Contributions (CEHR, CDHR, PS) | references/contributions.md |
| Obligations déclaratives | references/obligations-declaratives.md |

---

## PHASE 4 — Structure de sortie du calcul

```
CALCUL DE PLUS-VALUE
[Client — Date — Référence YD]

I. QUALIFICATION
   Type de PV retenu, base légale, régime applicable.
   ⚠️ INCERTAIN si données manquantes.

II. CALCUL DE LA PV BRUTE
   Prix de cession : X €
   Prix de revient corrigé : X € [détail des corrections]
   PV brute : X €

III. ABATTEMENTS ET CORRECTIONS
   [Durée de détention, abattements spéciaux, Quémener si applicable]
   PV nette imposable : X €

IV. IMPOSITION
   IR (taux applicable) : X €
   Prélèvements sociaux : X €   [rappel : 18,6% PV mobilières / 17,2% PV immo]
   CEHR (si applicable) : X €
   CDHR (si applicable) : X €
   TOTAL : X € [taux effectif global : X%]

V. OBLIGATIONS DÉCLARATIVES
   Formulaire(s), délai(s), points de vigilance.

VI. COMPARAISON DE SCÉNARIOS (si pertinent)
   [Cession directe vs apport-cession, donation avant cession, etc.]
   [⚠️ Si apport-cession envisagé : vérifier CDHR obligatoirement avant de conclure
    à un avantage — voir Règle CDHR ci-dessous]
```

---

## DMTG — Fiscalité des donations et successions

Hors périmètre strict du skill (PV), mais souvent posé en complément.
Pour toute question de calcul de droits de mutation à titre gratuit :
→ Renvoyer vers **patrimonial-structuring** pour l'analyse
→ Utiliser le barème Art. 777 CGI + abattements Art. 779 CGI
→ Abattement enfant : 100 000 € / 15 ans — vérifier via MCP

---

## Règle CDHR — À vérifier systématiquement

La Contribution Différentielle sur les Hauts Revenus (Art. 150-0 F ter CGI)
neutralise mécaniquement le gain fiscal de l'apport-cession dès que le RFR
dépasse 500 000 €. Ne jamais conclure à un avantage de l'apport-cession
sans avoir calculé l'impact CDHR. Voir references/contributions.md.

**Rappel règle 150-0 B ter + quotient :** PV en report → Art. 200 A, 2 ter → JAMAIS
barème Art. 197 → JAMAIS quotient Art. 163-0 A. Règle définitive (TA Bordeaux 2301446).


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
- [ ] Type de PV qualifié (immo / mobilière / pro / IS / régime spécial)
- [ ] Taux PFU 31,4% / PS 18,6% / PV immo 17,2% appliqués selon le régime
- [ ] CDHR vérifiée si apport-cession ou RFR > 250k€ / 500k€
- [ ] Règle 150-0 B ter + quotient 163-0 A INAPPLICABLE rappelée si pertinent
- [ ] Obligations déclaratives (formulaires, délais) mentionnées

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
