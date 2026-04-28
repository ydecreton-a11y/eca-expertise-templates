---
name: analyse-contrat
description: >
  Skill ECA EXPERTISE pour toute analyse, relecture, rédaction ou sécurisation
  d'un document contractuel : contrat, convention, bail, CGV, pacte, NDA, MOU,
  lettre de mission, protocole, acte de cession, garantie. Déclencher dès qu'un
  document contractuel est fourni ou qu'une clause doit être analysée ou rédigée.
  Mots-clés : analyser, relire, vérifier, sécuriser, rédiger, améliorer un contrat,
  une clause, un accord, un avenant.
  NE PAS utiliser si : la demande est une consultation de droit pur sans document
  fourni (→ consultation-juridique), si un acte de droit des sociétés doit être
  créé de zéro (→ redaction-acte).
---

# Skill : Analyse contractuelle — ECA EXPERTISE

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
- La recherche s'active uniquement si un nom propre de client ou de société
  est identifiable dans la requête


### 0c — Intégration réponse Casus

Si Yoann colle un output Casus dans la conversation :
- L utiliser comme base documentaire CGI/BOFiP certifiée
- Ne pas redupliquer les vérifications fiscales déjà faites
- Rôle Claude : analyse des clauses, risques contractuels, rédaction Word ECA
- Indiquer : "Base Casus intégrée"

## PHASE 0b — Qualification et routing

```
Document contractuel fourni ? → continuer ici
Pas de document, question de droit pur ? → skill consultation-juridique
Acte de droit des sociétés à créer (statuts, PV, cession) ? → skill redaction-acte
```

---

## PHASE 1 — Raisonnement préalable (avant lecture détaillée)

Avant d'analyser clause par clause, poser mentalement :

1. **Quelle est la nature juridique de ce contrat ?**
   La qualification conditionne le régime impératif applicable.

2. **Quel est le déséquilibre apparent ?**
   Qui a rédigé ? En faveur de qui ? Quel est le contexte de négociation ?

3. **Quels sont les enjeux prioritaires pour ECA et son client ?**
   Protection du prix ? Maintien de l'activité ? Limitation de responsabilité ?

4. **Y a-t-il une dimension fiscale évidente ?**
   Flux financiers, cession d'actifs, droits d'enregistrement.

---

## PHASE 2 — Sources et vérifications

### Fetch dynamique GitHub (obligatoire avant toute vérification)

Fetcher systématiquement avant d'utiliser un taux, un outil MCP ou une
référence BOFiP :

```
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md")
```

Ce fetch (2 secondes) garantit que tu travailles avec les taux et références
à jour — pas avec des valeurs mémorisées potentiellement périmées après
une LF. C'est la différence entre 30 % et 31,4 % de PFU.

### Vérifications complémentaires à vérifier

Fetcher `shared/sources-legales.md` via GitHub (voir bloc Sources ci-dessus) pour les outils MCP et BOFiP.

Points à vérifier systématiquement :
- Articles du Code civil invoqués (force majeure Art. 1218, imprévision Art. 1195)
- Règles d'ordre public sectorielles (droit conso, droit commercial)
- Jurisprudence récente sur les clauses litigieuses

**Balise incertitude :**
```
⚠️ INCERTAIN — [point précis] : à vérifier via [source] avant conseil définitif.
```

---

## PHASE 3 — Analyse structurée

### 3.1 Qualification juridique
- Nature du contrat (prestation, vente, bail, cession, pacte…)
- Régime applicable (droit commun / règles spéciales)
- Parties et capacité juridique

### 3.2 Analyse des clauses essentielles

Examiner dans cet ordre :
1. Objet et périmètre de la prestation
2. Obligations principales de chaque partie
3. Conditions financières (prix, révision, indexation, TVA)
4. Durée, reconduction, résiliation (Art. 1211 s. C. civ.)
5. Responsabilité, limitations, garanties, clauses pénales
6. Force majeure (Art. 1218 C. civ.) et imprévision (Art. 1195 C. civ.)
7. Confidentialité et non-sollicitation
8. Non-concurrence (proportionnalité, durée, zone, contrepartie)
9. Propriété intellectuelle (Art. L131-3 CPI pour cessions écrites)
10. Attribution de juridiction / arbitrage

### 3.3 Détection des déséquilibres
- Clauses abusives B2C (Art. L212-1 C. conso.)
- Déséquilibre significatif B2B (Art. L442-1 C. com.)
- Clauses potentiellement réputées non écrites

### 3.4 Dimension fiscale
Tout contrat impliquant des flux financiers doit traiter :
- Qualification fiscale des sommes (honoraires, redevances, prix de cession…)
- Régime TVA (exonération, autoliquidation, taux)
- Droits d'enregistrement (cessions, baux commerciaux)
- Risque de requalification (prix anormal, acte anormal de gestion)

---

## PHASE 4 — Structure de sortie

```
I. QUALIFICATION JURIDIQUE ET CADRE APPLICABLE
   1.1 Nature du contrat et régime
   1.2 Parties, capacité, pouvoir de signature

II. ANALYSE DES CLAUSES ESSENTIELLES
   [Clause par clause avec : résumé → risque → recommandation]

III. DIMENSION FISCALE ET RÉGLEMENTAIRE

IV. COTATION DES RISQUES
   [Tableau : Clause | Risque | Nature | Criticité 🔴🟠🟢 | Recommandation]

V. RECOMMANDATIONS ET SÉCURISATION
   5.1 Modifications rédactionnelles prioritaires (avec texte suggéré)
   5.2 Points à négocier
   5.3 Stratégie globale

VI. CONCLUSION
   Appréciation globale du niveau de sécurité juridique.
```

---

## PHASE 5 — Livrable Word (si demandé)

- Corps : Raleway sz=22, justifié, **#999999** ← couleur correcte
- H1/H2 : Raleway gras, **#C00000**
- Signature : Raleway gras sz=22, **#495864**, centré
- Méthode : XML injection template ECA validé

---

## Exemple de sortie bien formée

**Input :** "Analyse ce contrat de prestation de services informatiques"

**Risque détecté et formulé correctement :**
> "**Clause de limitation de responsabilité (Art. 8)** — La clause plafonne
> la responsabilité du prestataire au montant des honoraires de la dernière
> mensualité. Ce plafond est disproportionné si la prestation défaillante
> peut causer un préjudice commercial significatif au client.
> **Criticité : 🔴 Élevé**
> **Recommandation :** Négocier un plafond au montant total du contrat annuel
> ou à un multiple des honoraires mensuels (x3 à x6 selon l'enjeu)."

**❌ Ce qui est insuffisant :**
> "La clause de limitation de responsabilité pourrait poser problème."



---

## ENRICHISSEMENT — Templates de modifications rédactionnelles courantes

Quand l'analyse identifie un risque 🔴, ne jamais s'arrêter à « clause à renégocier ».
Toujours proposer la rédaction de remplacement. Voici les patterns ECA validés.

### 1. Clause de limitation de responsabilité — version équilibrée
```
« La responsabilité du Prestataire au titre de l'exécution du présent contrat
ne pourra excéder, tous préjudices confondus, un montant équivalent à [N×]
les honoraires versés au titre des [12] mois précédant le fait générateur,
sous réserve des cas pour lesquels la loi exclut toute limitation
(dol, faute lourde, atteinte aux personnes). »
```

### 2. Clause de non-concurrence — version sécurisée (Cass. soc. 10/07/2002)
```
« Pendant une durée de [X] mois suivant la cessation du présent contrat, le
[Salarié/Prestataire] s'interdit, dans la zone géographique de [périmètre
précis et limité], d'exercer une activité de [activité précisément définie
et limitée à ce qui est nécessaire à la protection des intérêts du Client].
En contrepartie, le [Client] versera mensuellement au [Salarié/Prestataire]
une indemnité d'un montant égal à [au minimum 30 % de la rémunération mensuelle
moyenne]. »
```
Quatre conditions cumulatives (proportionnalité, limitation espace/temps,
intérêts légitimes, contrepartie financière) — l'absence d'une seule entraîne nullité.

### 3. Clause de force majeure — version Art. 1218 C. civ. enrichie
```
« Constitue un cas de force majeure tout événement échappant au contrôle du
débiteur, qui ne pouvait être raisonnablement prévu lors de la conclusion du
contrat et dont les effets ne peuvent être évités par des mesures appropriées,
empêchant l'exécution de son obligation par le débiteur (Art. 1218 C. civ.).
La Partie qui invoque la force majeure notifiera l'autre Partie par écrit dans
un délai de [X jours] suivant la survenance de l'événement. Si l'empêchement
est définitif ou excède [X mois], chaque Partie pourra résilier le contrat
sans indemnité, par lettre recommandée avec accusé de réception. »
```

### 4. Clause d'imprévision — version Art. 1195 C. civ. négociée
```
« En cas de changement de circonstances imprévisible lors de la conclusion du
contrat rendant l'exécution excessivement onéreuse pour l'une des Parties, et
sous réserve qu'elle n'ait pas accepté d'en assumer le risque, cette Partie
pourra demander une renégociation à l'autre Partie. À défaut d'accord dans un
délai de [X mois], les Parties pourront, d'un commun accord, résoudre le contrat
ou demander d'un commun accord au juge de procéder à son adaptation. »
```
**Vigilance** : l'Art. 1195 C. civ. est supplétif — il peut être écarté par
les parties. L'absence ou l'aménagement de la clause doit être un choix conscient.

### 5. Clause d'indexation — version sécurisée
```
« Le prix sera révisé chaque [période] selon la formule suivante :
P = P₀ × (I_n / I_n-1)
où I est l'indice [INSEE / professionnel précis], dans sa dernière publication
disponible à la date de révision, et I_n-1 sa valeur de référence à la date
[de signature/de la révision précédente].
En cas de disparition de l'indice, il sera remplacé par l'indice de
substitution publié par l'organisme compétent ou, à défaut, par l'indice
ayant le périmètre le plus proche. »
```

---

## CAS — Contrat partiel ou en langue étrangère

### Contrat fourni en extrait seulement
- Signaler dès le début : « Analyse partielle — clauses non communiquées : [...] »
- Identifier les clauses absentes structurellement (résiliation, juridiction, force majeure)
- Demander les clauses manquantes avant analyse finale
- Ne jamais conclure sur la sécurité globale d'un contrat sur la base d'extraits

### Contrat en langue étrangère
- Si la langue est maîtrisée (anglais, allemand) : analyser, mais signaler que la
  version juridiquement opposable est celle du droit applicable
- Si traduction nécessaire : refuser l'analyse de fond avant traduction certifiée
  pour les clauses critiques (responsabilité, juridiction, prix)
- Mentionner systématiquement la clause de langue applicable


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
- [ ] Qualification juridique du contrat explicitée (Art. applicable)
- [ ] Cotation 🔴/🟠/🟢 portée sur chaque clause sensible
- [ ] Recommandation rédactionnelle proposée pour chaque risque 🔴

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
