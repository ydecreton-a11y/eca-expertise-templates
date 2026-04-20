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
