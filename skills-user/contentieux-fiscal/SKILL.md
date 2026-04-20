---
name: contentieux-fiscal
description: >
  Skill ECA EXPERTISE pour toute procédure de défense fiscale : réponse à
  proposition de rectification, réclamation contentieuse, mémoire hiérarchique,
  saisine de la Commission des impôts directs (CID), transaction fiscale,
  recours juridictionnel (TA, CAA, CE). Déclencher sur : contrôle fiscal,
  vérification de comptabilité, ESFP, proposition de rectification, redressement,
  réclamation, Commission des impôts, contentieux fiscal, défense fiscale,
  mémoire en réponse, provision déductible, chef de redressement, pénalités
  fiscales, manquement délibéré, abus de droit, transaction.
  NE PAS utiliser pour des questions de droit fiscal pur sans procédure en cours
  (→ consultation-juridique).
---

# Skill : Contentieux fiscal — ECA EXPERTISE

Ce skill existe parce que la défense fiscale obéit à des règles procédurales
strictes avec des délais de forclusion qui ne pardonnent pas. Une réponse
hors délai ou mal dirigée peut faire perdre des droits définitivement.
La maîtrise du calendrier procédural est aussi importante que les arguments
de fond.

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
- La recherche s'active uniquement si un nom propre de client ou de société
  est identifiable dans la requête

### 0c — Intégration réponse Casus

Si Yoann colle un output Casus dans la conversation :
- L utiliser comme base documentaire CGI/LPF certifiée pour les arguments fiscaux
- Claude complète : stratégie procédurale, jurisprudence CE/CAA, rédaction des actes de procédure
- Indiquer : "Base Casus intégrée — stratégie procédurale construite dessus"

## PHASE 0b — Routing et identification de l'étape procédurale

```
Question de droit fiscal sans procédure en cours ? → consultation-juridique
Calcul de l'impôt redressé à vérifier ? → calcul-plus-value en complément
→ Procédure en cours : continuer ici
```

**Identifier impérativement l'étape procédurale avant tout :**

```
PROPOSITION DE RECTIFICATION reçue (3924/3926) ?
  → PHASE A : Réponse dans le délai de 30 jours (prorogeable 30 j sur demande)

RÉPONSE AUX OBSERVATIONS DU CONTRIBUABLE reçue ?
  → PHASE B : Évaluer CID / Recours hiérarchique / Acceptation

MISE EN RECOUVREMENT reçue (AMR) ?
  → PHASE C : Réclamation préalable obligatoire dans délai légal

REJET DE RÉCLAMATION reçu ?
  → PHASE D : Recours juridictionnel (TA / TJ selon impôt)

TRANSACTION proposée ?
  → PHASE E : Analyse opportunité + négociation
```

**Indiquer l'étape procédurale identifiée.**

---

## PHASE 1 — Cartographie du dossier (à compléter avant toute rédaction)

### Éléments à collecter impérativement

**Sur la procédure :**
- Type de contrôle : Vérification de Comptabilité (VC) / ESFP / Contrôle sur pièces
- Dates clés : début contrôle, réception proposition, délai de réponse
- Impôt(s) en cause et années vérifiées
- Montant total des rectifications proposées (base + pénalités)

**Sur les chefs de redressement :**
- Lister chaque chef séparément avec : montant, fondement légal invoqué par
  l'administration, qualification proposée par l'administration
- Identifier les chefs contestables vs ceux à accepter
- Identifier les vices de procédure éventuels (délais, notification, motivation)

**Sur les faits :**
- Éléments factuels contradictoires à l'argumentaire de l'administration
- Pièces justificatives disponibles
- Positions BOFiP favorables applicables (Art. L80 A LPF)
- Jurisprudence récente favorable (vérifier via MCP Légifrance)

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

Fetcher `shared/sources-legales.md` via GitHub (voir bloc Sources ci-dessus) pour les outils MCP.

**Vérifications prioritaires en contentieux :**

```
rechercher_code("Livre des procédures fiscales", "Art. [N] LPF")
→ Procédure contradictoire, délais, droits du contribuable

rechercher_jurisprudence_administrative(search="[chef de redressement]", panorama=True)
→ Jurisprudence CE/CAA récente favorable

web_fetch(BOFiP)
→ Doctrine administrative opposable (Art. L80 A LPF) — arme principale
```

**Charger `references/procedure-fiscale.md`** pour les délais et voies de recours.
**Charger `references/arguments-type.md`** pour les arguments par type de chef.

---

## PHASE 3 — Construction de la défense

### 3.1 Analyse de la solidité de chaque chef

Pour chaque chef de redressement, analyser :

| Dimension | Questions à traiter |
|-----------|---------------------|
| **Fondement légal** | L'article invoqué est-il applicable ? Conditions remplies ? |
| **Qualification des faits** | L'administration a-t-elle correctement qualifié les faits ? |
| **Charge de la preuve** | Qui supporte la charge ? (présomption de bonne foi du contribuable) |
| **BOFiP** | Existe-t-il une position administrative plus favorable ? (Art. L80 A LPF) |
| **Jurisprudence** | Arrêts favorables récents du CE ou CAA ? |
| **Vice de procédure** | Délai non respecté ? Motivation insuffisante ? Notification irrégulière ? |

### 3.2 Stratégie de défense globale

**Principes :**
- Ne pas contester des chefs incontestables — cela affaiblit la crédibilité
  sur les chefs réellement discutables
- Commencer par les vices de procédure (si existants) — ils peuvent annuler
  la procédure entière avant même le fond
- Distinguer les arguments de droit (plus forts) des arguments de fait (plus
  fragiles si pièces manquantes)
- Anticiper la réponse possible de l'administration à chaque argument

**Tactiques selon l'enjeu :**

| Enjeu | Stratégie recommandée |
|-------|----------------------|
| Montant élevé, position solide | Résistance totale + CID si désaccord persistant |
| Montant élevé, position incertaine | Résistance + ouverture à transaction ciblée |
| Montant modéré, position fragile | Transaction négociée (abandon partiel) |
| Vice de procédure identifié | Soulever en priorité dans la réponse |

---

## PHASE 4 — Rédaction des actes de procédure

### 4.1 Réponse à la proposition de rectification

**Structure obligatoire :**

```
[Lieu], le [date]

[Identification contribuable]
[Référence de la proposition : n° et date]

À l'attention de [Inspecteur / Service vérificateur]

Madame, Monsieur,

Par courrier du [date], vous avez adressé à [société/contribuable]
une proposition de rectification portant sur [impôts] pour les exercices
[années], pour un montant total de [X] €.

Après examen attentif, nous entendons formuler les observations suivantes :

I. SUR [CHEF N°1 — INTITULÉ]
   [Exposé des faits tels que vus par le contribuable]
   [Argument juridique principal]
   [Référence BOFiP ou jurisprudence favorable]
   [Conclusion : contestation totale / partielle / acceptation]

II. SUR [CHEF N°2 — INTITULÉ]
   [idem]

[Si vice de procédure :]
III. SUR LA RÉGULARITÉ DE LA PROCÉDURE
   [Développer — à placer en premier si argument fort]

En conséquence, nous vous demandons de bien vouloir abandonner les
rectifications visées aux points [N] ci-dessus.

Nous restons à votre disposition pour tout échange complémentaire.

Veuillez agréer, Madame, Monsieur, l'expression de nos salutations distinguées.

[Signature YD + Expert-comptable signataire]
```

### 4.2 Réclamation préalable (Art. R. 190-1 LPF)

**Délai de forclusion :** 31 décembre de la 2e année suivant la mise
en recouvrement (ou l'année du versement pour les impôts à versement
spontané). **Délai impératif — vérifier via MCP avant toute rédaction.**

```
[Identification]
[Référence AMR et date]

RÉCLAMATION CONTENTIEUSE

En application des articles L. 190 et R. 190-1 du LPF, [contribuable]
entend contester les impositions mises en recouvrement le [date]
pour les motifs suivants :

[Développer les arguments — reprendre ceux de la réponse en les renforçant]

Par ces motifs, nous demandons la décharge totale / partielle des
impositions contestées.

[Pièces jointes : AMR, proposition de rectification, réponse initiale, justificatifs]
```

### 4.3 Saisine de la Commission des impôts directs (Art. L. 59 LPF)

**Conditions :**
- Désaccord persistant après réponse de l'administration
- Impôts éligibles : IS, BIC, BNC, BA, TVA (vérifier liste via MCP)
- Délai : 30 jours après réception de la réponse aux observations

**La Commission rend un avis consultatif** — non contraignant mais
avec un fort poids pratique. L'administration suit généralement l'avis.

```
Madame, Monsieur le Président de la Commission [départementale] des
impôts directs et des taxes sur le chiffre d'affaires,

[Identification]
[Référence dossier]

Nous avons l'honneur de solliciter la saisine de la Commission en
application de l'article L. 59 du LPF, eu égard au désaccord persistant
avec l'administration sur les points suivants :

[Résumer les chefs en désaccord — être précis et factuel]
[Joindre : proposition, observations, réponse de l'administration]
```

---

## PHASE 5 — Structure du livrable

```
NOTE DE DÉFENSE FISCALE
[Client — Exercices — Date — Référence YD]

I. SYNTHÈSE DE LA PROCÉDURE
   Contexte, enjeux globaux, délai de réponse.

II. ANALYSE PAR CHEF DE REDRESSEMENT
   [Pour chaque chef :]
   — Rappel de la position de l'administration
   — Analyse de solidité : 🔴 Contestable / 🟠 Incertain / 🟢 À accepter
   — Arguments de défense
   — Recommandation

III. VICES DE PROCÉDURE ÉVENTUELS

IV. STRATÉGIE RECOMMANDÉE
   Position globale + tactique (résistance / transaction / acceptation partielle)

V. ACTE DE PROCÉDURE RÉDIGÉ
   [Réponse / Réclamation / Saisine CID selon étape]

VI. CALENDRIER PROCÉDURAL
   [Délais restants — dates limites]
```

---

## PHASE 6 — Livrable Word

- Corps : Raleway sz=22, justifié, **#999999**
- H1/H2 : Raleway gras, **#C00000**
- Signature : Raleway gras sz=22, **#495864**, centré
- Charger skill docx pour la mise en forme
- Declencher legal-hallucination-checker sur toutes les références citées

---

## Exemple de défense bien formée (extrait)

**Chef de redressement : provisions pour créances douteuses refusées**

> "I. SUR LE REFUS DES PROVISIONS POUR CRÉANCES DOUTEUSES
>
> L'administration refuse la déductibilité des provisions constituées par
> SAS X pour un montant de 137 000 € au titre de l'exercice N, au motif
> que les créances en cause ne présenteraient pas un risque de perte
> suffisamment probable.
>
> Cette position ne saurait être maintenue pour les motifs suivants.
>
> En premier lieu, l'article 39, 1-5° du CGI admet la déductibilité des
> provisions lorsque la perte est probable, résulte d'événements précis
> survenus avant la clôture, et que la créance est individualisée.
> Ces trois conditions sont remplies en l'espèce : [développer avec les
> faits concrets — procédures en cours, historique de défaillance, etc.]
>
> En second lieu, le BOFiP (BOI-BIC-PROV-20-10-10 §X) admet qu'une
> créance fait l'objet d'un risque probable dès lors que [position
> favorable — à vérifier via BOFiP avant citation].
>
> ⚠️ INCERTAIN — Vérifier la référence BOFiP exacte via web_fetch avant
> intégration dans la réponse définitive.
>
> En conséquence, nous demandons l'abandon de ce chef de rectification."

**❌ Ce qui est insuffisant :**
> "Les provisions sont justifiées car les créances sont douteuses."

