---
name: redaction-acte
description: >
  Skill ECA EXPERTISE pour toute rédaction, modification ou vérification d'un
  acte de droit des sociétés ou civil : statuts, PV d'assemblée, décision
  d'associé unique, cession de parts/actions, pacte d'associés, nomination/
  révocation dirigeant, dissolution, liquidation, contrat de mariage, donation,
  acte de donation-partage. Déclencher sur : rédiger, rédaction, draft, acte,
  statuts, PV, procès-verbal, décision, cession, pacte, nomination, dissolution,
  liquidation, assemblée, AGO, AGE, associé unique, contrat de mariage, donation,
  donation-partage, démembrement, acte civil.
  NE PAS utiliser si une question de droit doit d'abord être tranchée
  (→ consultation-juridique d'abord), ou si c'est un contrat entre parties
  (→ analyse-contrat).
---

# Skill : Rédaction d'actes juridiques — ECA EXPERTISE

## PHASE 0 — Contexte dossier (exécuter en premier, toujours)

### 0a — Recherche automatique dans les dossiers en cours

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

### 0b — SIREN fourni ? (auto-lookup systématique)

Si un numéro SIREN ou une dénomination sociale est mentionné(e) dans la demande :

```
web_fetch("https://recherche-entreprises.api.gouv.fr/search?q=[SIREN_ou_denomination]&per_page=1")
```

Récupérer et pré-remplir automatiquement :
- Dénomination sociale exacte
- Forme juridique
- Capital social
- Adresse du siège
- SIREN / RCS
- Dirigeants actuels

Ces données alimentent directement l'acte. Ne jamais rédiger un acte sans
avoir vérifié les données d'identification via cette API — les erreurs sur
la dénomination ou le siège peuvent rendre l'acte inopposable.

### 0c — Routing et séquencement

La rédaction d'un acte est un acte final, pas un acte de réflexion.
Si des questions de droit subsistent sur l'opération, les trancher via
consultation-juridique avant de rédiger.

```
Question de fond non tranchée ? → consultation-juridique d'abord
Acte prêt à rédiger ? → continuer ici
Contrat entre parties (prestation, bail, vente) ? → analyse-contrat
```

---

## Sources — Fetch dynamique GitHub (obligatoire avant toute vérification)

Fetcher avant d'utiliser un taux, un outil MCP ou une référence BOFiP :

```
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md")
```

Ce fetch (2 secondes) garantit les taux et références à jour.

## PHASE 1 — Vérification des sources avant toute rédaction

Toute mention légale, condition de validité ou formalité doit être
vérifiée avant d'être inscrite dans un acte. Un acte fondé sur un texte
abrogé ou modifié peut être nul ou créer une responsabilité.

**Via MCP Légifrance :**
- Articles C. com. encadrant l'acte (statuts : Art. L210-1 s., cession : Art. L221-14 s., AGE : Art. L223-30 s.)
- Articles C. civ. pour les actes civils (SCI, donations, démembrement)
- Lois et ordonnances modificatives récentes
- Jurisprudence sur la validité d'une clause spécifique si doute

**Balise incertitude :**
```
⚠️ INCERTAIN — [point précis] : vérifier via MCP avant signature.
```

---

## PHASE 2 — Structure de l'acte selon son type

### PV d'assemblée générale (AGO / AGE)
```
[Forme sociale] — [Dénomination]
PROCÈS-VERBAL DE L'ASSEMBLÉE GÉNÉRALE [ORDINAIRE / EXTRAORDINAIRE]
Du [date]

ORDRE DU JOUR : [liste numérotée]

L'an [AAAA], le [date], à [heure], les associés/actionnaires de [société],
[forme] au capital de [montant] €, immatriculée au RCS de [ville] sous le
numéro [SIREN], dont le siège social est situé [adresse],

se sont réunis en assemblée générale [ordinaire/extraordinaire] sur
convocation de [gérant/président] adressée le [date] à chaque [associé/
actionnaire], conformément aux stipulations statutaires.

Étaient présents ou représentés : [tableau présences/pouvoirs]
[Quorum : vérifier conditions légales selon forme sociale et type d'AG]

RÉSOLUTIONS
[Numéroter chaque résolution. Pour chaque résolution :
 - Exposé des motifs
 - Texte de la résolution
 - Vote : adoptée/rejetée à [N] voix pour / [N] contre / [N] abstentions]

De tout ce qui précède, il a été dressé le présent procès-verbal, signé
par les membres du bureau.
[Signatures]
```

### Décision d'associé unique
```
[Forme sociale] — [Dénomination]
DÉCISION DE L'ASSOCIÉ UNIQUE
Du [date]

L'associé unique de [société], [forme] au capital de [montant] €,
immatriculée au RCS de [ville] sous le numéro [SIREN],

[M./Mme] [Nom], demeurant [adresse],

a pris les décisions suivantes :

DÉCISION N°1 : [titre]
[Exposé — Décision — Effet]

La présente décision est établie en autant d'exemplaires que nécessaire.
Fait à [ville], le [date]
[Signature]
```

### Cession de parts sociales
- Vérifier clause d'agrément statutaire (Art. L223-14 C. com. pour SARL)
- Procédure d'agrément : notification par acte extrajudiciaire ou LRAR aux
  autres associés (délai légal à vérifier via MCP)
- Mentions obligatoires : prix, nombre de parts, date d'effet, modalités de
  paiement, déclarations du cédant
- Enregistrement : droits de 3% (abattement applicable — vérifier Art. 726 CGI)
- Notification à la société (Art. 1690 C. civ. ou formalité simplifiée SARL)

---

## PHASE 3 — Points de vigilance transversaux

**Démembrement de propriété dans les actes :**
- Convocation USU + NP obligatoire (Art. 1844 al.4 C. civ.)
- Droit de vote : USU pour décisions ordinaires, NP pour décisions
  extraordinaires en SA (à vérifier selon forme sociale)

**Distribution hors AGOA :**
- Distribution RAN sans AGOA = nulle (Cass. com. 12/02/2025 n°23-11410)
- Vérifier la base légale de toute distribution avant de rédiger l'acte

**RBE :**
- Toute modification affectant les bénéficiaires effectifs déclenche une
  mise à jour RBE dans le mois (Art. L561-46 CMF)

**Actes impliquant des apports :**
- Évaluation des apports en nature : commissaire aux apports si > seuils légaux
- Vérifier seuils actuels via MCP avant toute recommandation

---

## PHASE 4 — Livrable Word

- Corps : Raleway sz=22, justifié, **#999999**
- H1/H2 : Raleway gras, **#C00000**
- Signature : Raleway gras sz=22, **#495864**, centré
- Méthode : XML injection template ECA validé (Devis_ECA_Constitution_SAS.docx base)
- Charger skill docx avant génération

---

## Comportements à éviter

- Rédiger une clause encadrée par des dispositions impératives sans avoir
  vérifié le texte en vigueur : les mentions obligatoires changent,
  les délais légaux aussi.
- Omettre le RBE, l'enregistrement ou la publicité légale — ce sont des
  formalités qui déclenchent des sanctions.
- Rédiger un acte de cession sans vérifier la clause d'agrément : une
  cession sans agrément est inopposable à la société.
- Utiliser des données d'identification non vérifiées via l'API Entreprises —
  une dénomination erronée peut invalider l'acte.


---

## ENRICHISSEMENT — Templates d'actes complémentaires

### Décision TUP (Transmission Universelle de Patrimoine — Art. 1844-5 al.3 C. civ.)

**Conditions :**
- Société dissoute détenue à 100 % par une personne morale (associé unique)
- Décision de l'associé unique de prononcer la dissolution sans liquidation
- Délai d'opposition créanciers : 30 jours après publication

**Template décision :**
```
[Forme] — [Dénomination de la société dissoute]
DÉCISION DE L'ASSOCIÉ UNIQUE
PORTANT DISSOLUTION SANS LIQUIDATION (TUP)
Du [date]

L'associé unique de [société dissoute], [forme] au capital de [montant] €,
immatriculée au RCS de [ville] sous le numéro [SIREN], dont le siège social
est situé [adresse],

Soit la société [dénomination de l'associé unique], [forme] au capital de
[montant] €, immatriculée au RCS de [ville] sous le numéro [SIREN], dont le
siège social est situé [adresse], représentée par [Nom], [qualité],

Constatant que la société [société dissoute] est détenue à 100 % par
[associé unique] et qu'il est décidé d'opérer la simplification de la
structure par voie de transmission universelle de patrimoine,

a pris la décision suivante :

DÉCISION UNIQUE — DISSOLUTION SANS LIQUIDATION

Conformément aux dispositions de l'article 1844-5 alinéa 3 du Code civil,
l'associé unique décide la dissolution de la société [dénomination de la
société dissoute] sans qu'il soit nécessaire de procéder à sa liquidation.

L'ensemble du patrimoine de la société [société dissoute], composé de
l'intégralité de son actif et de son passif, est transmis à l'associé unique
[dénomination] avec effet à l'expiration du délai d'opposition des
créanciers prévu à l'article 1844-5 du Code civil, soit 30 jours à compter
de la publication de la présente décision dans un journal d'annonces légales.

Tous pouvoirs sont donnés à [Nom] pour effectuer les formalités de publicité,
de radiation au RCS et toute formalité utile.

Fait à [ville], le [date]
[Signature]
```

**Formalités post-décision :**
1. Publication JAL → délai d'opposition créanciers de 30 j
2. Si pas d'opposition → enregistrement de la décision (droit fixe 375 € si CS < 225k€)
3. Dépôt au greffe : décision + JAL + Cerfa M4
4. Radiation RCS de la société dissoute
5. Mise à jour RBE (radiation)
6. Reprise comptable chez l'associé unique (mali ou boni de confusion)

### PV de dissolution-liquidation amiable (sociétés à plus d'un associé)

**Template synthétique :**
```
PROCÈS-VERBAL DE L'ASSEMBLÉE GÉNÉRALE EXTRAORDINAIRE
DÉCIDANT LA DISSOLUTION ANTICIPÉE

[En-tête société]

L'an [AAAA], le [date], à [heure], les associés/actionnaires de [société]
se sont réunis en AGE sur convocation de [organe de direction],

Après lecture des rapports et discussion, l'AGE :

PREMIÈRE RÉSOLUTION — DISSOLUTION ANTICIPÉE
L'AGE décide la dissolution anticipée de la société [dénomination] à compter
du [date d'effet]. La dénomination sociale sera suivie de la mention
« société en liquidation ».

DEUXIÈME RÉSOLUTION — NOMINATION DU LIQUIDATEUR
L'AGE nomme [Nom du liquidateur] en qualité de liquidateur amiable, avec les
pouvoirs les plus étendus pour réaliser l'actif, apurer le passif et procéder
au partage du boni éventuel. La durée de ses fonctions est fixée à [3 ans
maximum, sauf prorogation par AGE].

TROISIÈME RÉSOLUTION — SIÈGE DE LA LIQUIDATION
Le siège de la liquidation est fixé à [adresse — souvent au siège social ou
au domicile du liquidateur].

QUATRIÈME RÉSOLUTION — POUVOIRS POUR LES FORMALITÉS
Tous pouvoirs sont conférés à [Nom] pour effectuer les formalités légales.
```

**Étapes de la liquidation amiable :**
1. PV dissolution + nomination liquidateur (formalités JAL + greffe + Cerfa M2)
2. Réalisation de l'actif et apurement du passif par le liquidateur
3. Comptes de liquidation établis et approuvés en AGO de clôture
4. AGO approbation comptes + quitus liquidateur + constatation clôture
5. Formalités de radiation (JAL + greffe + Cerfa M4)
6. Délai global : minimum 6 mois, en pratique 12 à 18 mois

⚠️ **Boni de liquidation** : imposé au PFU 31,4 % chez les associés PP,
   éligible au régime mère-fille pour les associés personnes morales IS
   (Art. 145 et 216 CGI sous conditions).

### Cession de fonds de commerce — checklist mentions obligatoires

Toute cession de fonds doit mentionner (Art. L141-1 C. com. abrogé en 2019,
mais bonnes pratiques maintenues + mentions sociales et fiscales) :
- Identité des parties + dénomination du fonds
- Désignation précise des éléments cédés (corporels et incorporels)
- Prix global et ventilation par catégorie d'éléments
- Privilège de vendeur et nantissement éventuels
- Bail commercial : référence, propriétaire, durée résiduelle
- Chiffre d'affaires des 3 derniers exercices et résultats
- Information préalable des salariés (Art. L141-23 et L141-28 C. com. — délai 2 mois)
- Information préalable de la commune (Art. L214-1 C. urbanisme — DCE)


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
- [ ] API recherche-entreprises consultée si SIREN / dénomination
- [ ] Mentions légales obligatoires vérifiées (capital, RCS, siège, dirigeants)
- [ ] Clauses statutaires d'agrément / préemption analysées si cession
- [ ] RBE mis à jour si modification BE (délai 30 jours, Art. L561-46 CMF)
- [ ] Formalités post-signature listées (JAL, BODACC, greffe, enregistrement)

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
