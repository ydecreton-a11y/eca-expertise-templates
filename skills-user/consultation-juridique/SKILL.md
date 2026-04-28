---
name: consultation-juridique
description: >
  Skill central ECA EXPERTISE pour toute question juridique ou fiscale nécessitant
  une analyse de fond : régime fiscal, qualification juridique, règle applicable,
  risque, optimisation, transmission, report d'imposition, droit social, procédure.
  Déclencher sur : "quel est le régime", "comment qualifier", "quelles conséquences",
  "est-il possible de", "quels risques", "comment optimiser", "y a-t-il un risque",
  "fais un point sur", "analyse fiscalement", "rédige une consultation",
  consultation, note juridique, note fiscale, analyse fiscale, avis juridique.
  NE PAS utiliser si : un document contractuel est fourni (→ analyse-contrat),
  le client est en phase exploratoire sans opération définie (→ diagnostic-transmission),
  la demande porte sur un texte nouveau (→ veille-juridique),
  un acte doit être rédigé sans question de fond (→ redaction-acte).
---

# Skill : Consultation juridique et fiscale — ECA EXPERTISE


## PHASE 0 — Initialisation (exécuter dans cet ordre, toujours)

### 0a — Recherche dossier en cours

Si un nom de client ou de société est mentionné dans la demande :

```
conversation_search(query="[nom exact du client ou de la société]")
```

- Si historique trouvé → lire les conversations pertinentes avant d'analyser.
  Indiquer discrètement : "Suite du dossier [client] — [date dernière conversation]"
- Si aucun historique → continuer normalement, nouveau dossier.
- Si la demande est générique sans nom propre → pas de recherche, continuer directement.

### 0b — SIREN fourni ?

Si un numéro SIREN est mentionné dans la demande :
```
web_fetch("https://recherche-entreprises.api.gouv.fr/search?q=[SIREN]&per_page=1")
```
Pré-remplir automatiquement : dénomination, forme juridique, adresse, dirigeants.

### 0c — Routing

Vérifier que ce skill est le bon avant de continuer.

```
Document contractuel fourni ? → skill analyse-contrat
Besoin de chiffrage PV en priorité ? → skill calcul-plus-value d'abord
Client en phase exploratoire transmission ? → skill diagnostic-transmission
Texte législatif récent à analyser ? → skill veille-juridique
Acte à rédiger sans question de fond ? → skill redaction-acte
→ Aucune de ces situations : continuer ici
```

### 0d — Intégration réponse Casus

Si Yoann colle un output Casus dans la conversation :
- L'utiliser comme base documentaire CGI/BOFiP certifiée (source de confiance)
- Ne pas redupliquer les vérifications CGI/BOFiP déjà faites par Casus
- Rôle Claude : raisonnement juridique global, jurisprudence Légifrance, rédaction Word ECA
- Indiquer en début de réponse : "Base Casus intégrée — construction sur sa documentation"
- Ne jamais contredire silencieusement Casus sans vérification Légifrance préalable

---

## PHASE 1 — Raisonnement préalable (avant toute recherche, avant toute rédaction)

Cette phase est interne — elle précède la réponse visible. Elle est la raison
pour laquelle la consultation sera juste plutôt que plausible.

**Exécuter mentalement dans cet ordre :**

1. **Qualification des faits** — Qui sont les parties ? Quelle est la nature
   juridique de l'opération ? Quelles sont les dates et montants clés ?
   Quelle forme sociale ? Quel régime fiscal ?

2. **Identification de la question de droit** — Formuler en une phrase la
   question juridique centrale. Une consultation qui ne pose pas clairement
   sa question ne peut pas y répondre clairement.

3. **Mapping des règles applicables** — Quels articles, quels régimes,
   quelle jurisprudence ? Identifier les zones de certitude et d'incertitude
   avant d'ouvrir Légifrance.

4. **Identification des risques de requalification** — Abus de droit ?
   Acte anormal de gestion ? Fiction juridique ? Anticiper avant de conseiller.

5. **Niveau de confiance initial** — Sur quels points suis-je certain ?
   Sur quels points dois-je impérativement vérifier ?

⚠️ Si les faits sont insuffisants pour cette phase, identifier précisément
ce qui manque et le demander avant de continuer.

---

## PHASE 2 — Vérification des sources

### Fetch dynamique GitHub (obligatoire avant toute vérification)

Fetcher systématiquement avant d'utiliser un taux, un outil MCP ou une
référence BOFiP :

```
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md")
```

Ce fetch (2 secondes) garantit que tu travailles avec les taux et références
à jour — pas avec des valeurs mémorisées potentiellement périmées après
une LF. C'est la différence entre 30 % et 31,4 % de PFU.

### Vérifications complémentaires

**Règle de vérification :**
- Tout article cité → vérifié via MCP Légifrance
- Tout point fiscal → vérifié via BOFiP en complément
- Toute jurisprudence → numéro et date vérifiés

**Signal d'incertitude obligatoire :**
Utiliser la balise suivante dès qu'une vérification échoue ou reste partielle :

```
⚠️ INCERTAIN — [point précis] : [raison de l'incertitude].
   À vérifier via [source] avant usage opérationnel.
```

---

## PHASE 3 — Rédaction de la consultation

### Format standard

```
I. RAPPEL DES FAITS PERTINENTS
   Synthèse neutre et précise. Mentionner les éléments déterminants
   pour la qualification : forme sociale, régime fiscal, dates, montants,
   structure du capital, opération envisagée.

II. PROBLÉMATIQUE(S) JURIDIQUE(S)
   Formuler la ou les questions de droit en termes précis.
   Exemple : "La question est de savoir si l'apport de titres réalisé
   par M. X, associé contrôlant à 80%, remplit les conditions de l'Art.
   150-0 B ter CGI pour bénéficier du report d'imposition."

III. RÈGLES DE DROIT APPLICABLES
   Textes, articles, principes généraux, jurisprudence.
   [Références vérifiées via MCP Légifrance et/ou BOFiP]
   Distinguer : droit positif / doctrine administrative / jurisprudence

IV. ANALYSE
   4.1 Qualification juridique des faits
   4.2 Application des règles — discussion argumentée
       (confronter les faits aux conditions légales, une par une)
   4.3 Points d'incertitude, risques d'interprétation, positions contraires
       [Utiliser la balise ⚠️ INCERTAIN pour chaque zone grise]

V. CONCLUSION OPÉRATIONNELLE
   — Position principale retenue (argumentée, pas affirmée)
   — Niveau de risque : 🔴 Élevé / 🟠 Modéré / 🟢 Faible
     (avec justification en une ligne)
   — Recommandations pratiques et points de vigilance
   — Prochaine étape concrète recommandée
```

### Complément si dominante fiscale

```
VI. CONSÉQUENCES FISCALES CHIFFRÉES (si données disponibles)
    Calcul du coût fiscal, comparaison d'options, simulations.
    [Rappeler systématiquement : vérifier les taux via references/sources-legales.md]

VII. RISQUES DE REDRESSEMENT
     — Qualification du risque fiscal
     — Pénalités applicables (40 % manquement délibéré / 80 % abus de droit)
     — Position BOFiP et jurisprudence récente

VIII. STRATÉGIE D'OPTIMISATION ET ALTERNATIVES
      Options légales recommandées, séquencement, conditions de sécurisation.
```

---

## PHASE 4 — Instructions par domaine prioritaire

Charger le fichier de domaine pertinent depuis `references/domaines/` :

| Domaine | Fichier |
|---------|---------|
| Transmission d'entreprise, Dutreil | `references/domaines/transmission-dutreil.md` |
| Apport-cession, report 150-0 B ter | `references/domaines/apport-cession.md` |
| LMNP / LMP | `references/domaines/lmnp-lmp.md` |
| Cession de titres, PFU, QPFC | `references/domaines/cession-titres.md` |
| Contentieux fiscal, procédure | `references/domaines/contentieux-fiscal.md` |
| Patrimonial, succession, régimes matrim. | `→ skill patrimonial-structuring` |
| Droit social, dirigeants | `references/domaines/droit-social.md` |

Ne pas improviser sur ces domaines sans avoir chargé le fichier correspondant.

---

## PHASE 5 — Livrable Word (si demandé)

1. Charger le skill `docx`
2. Appliquer la charte ECA EXPERTISE :
   - Corps : Raleway 11pt (sz=22), justifié, **#999999** ← couleur correcte
   - H1 : Raleway gras 14pt, **#C00000**
   - H2 : Raleway gras 12pt, **#C00000**
   - Signature : Raleway gras sz=22, **#495864**, centré
3. Utiliser la méthode XML injection dans le template ECA validé
4. Mentionner référence signataire YD + expert-comptable (SH/LJ/FV/PL)

---

## PHASE 6 — Contrôle qualité avant remise

Avant de finaliser la réponse, vérifier mentalement :

- [ ] Toutes les références citées ont été vérifiées (MCP ou BOFiP)
- [ ] Les zones d'incertitude sont signalées avec la balise ⚠️ INCERTAIN
- [ ] La conclusion répond directement à la question posée au §II
- [ ] Le niveau de risque est justifié, pas seulement affiché
- [ ] Aucune position incertaine n'est présentée comme certaine
- [ ] La dimension fiscale d'une opération impliquant des flux est traitée
- [ ] Le legal-hallucination-checker a été déclenché sur le livrable final

---

## Exemples de consultations bien formées

### Exemple 1 — Apport-cession (niveau de détail attendu)

**Input :**
> "Mon client détient 80% d'une SARL plâtrerie valorisée 1,2M€. Il veut
> apporter ses titres à une holding avant cession à un industriel. Est-ce
> possible ? Quel est l'intérêt ?"

**Structure de réponse attendue :**

I. Faits : SARL IS, associé majoritaire 80%, valorisation 1,2M€, opération
   envisagée : apport à holding IS avant cession à tiers.

II. Problématique : Conditions d'application de l'Art. 150-0 B ter CGI
    (report d'imposition) + analyse de l'intérêt par rapport à une cession
    directe + risques CDHR.

III. Règles : Art. 150-0 B ter CGI (vérifier via MCP), condition de contrôle
     (>50% droits de vote), obligation de réinvestissement 70% dans 3 ans,
     CDHR (Art. 150-0 F ter), BOFiP BOI-RPPM-PVBMI-30-10-60.

[Suite de l'analyse avec chiffrage comparatif et recommandation]

**❌ Ce qui est insuffisant :**
> "L'Art. 150-0 B ter permet un report. Il faut contrôler la holding."

**❌ Ce qui est une erreur :**
> Analyser sans vérifier que la condition de contrôle est remplie au moment
> de l'apport (80% des droits de vote suffit — à vérifier via MCP).

---

### Exemple 2 — Signal ⚠️ INCERTAIN correctement utilisé

**Situation :** Jurisprudence récente sur la holding animatrice, position
non encore consolidée dans le BOFiP.

**Formulation correcte :**
> "La jurisprudence du CE admet la qualification de holding animatrice sous
> conditions [référence vérifiée]. Toutefois :
> ⚠️ INCERTAIN — La position BOFiP sur les holdings mixtes (activité animatrice
> partielle) n'est pas encore stabilisée depuis [arrêt]. À vérifier via
> BOI-ENR-DMTG-10-20-40-10 avant de structurer le Dutreil."


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
