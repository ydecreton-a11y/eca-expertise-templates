---
name: prompt-builder-eca
description: >
  Skill ECA EXPERTISE qui transforme des faits bruts de dossier en deux
  prompts raisonnés et enchaînés : un prompt Casus qui établit l'état du
  droit (textes, jurisprudence, doctrine, et ce qui n'a pas été jugé), puis
  un prompt Claude calibré pour le modèle cible (Opus, Sonnet, Haiku, Fable)
  qui exploite cette base pour qualifier, arbitrer et produire le livrable.
  Ce skill NE RÉPOND PAS à la question juridique — il fabrique la question.
  Déclencher sur : "fais-moi le prompt", "prépare la requête", "prompt Casus",
  "comment je dois te demander ça", "optimise ma demande", ou quand Yoann
  colle des faits bruts sans formuler de question précise.
  Fichier compagnon de prompt-codes-eca.
  NE PAS utiliser si Yoann attend une analyse de fond (→ router-eca puis le
  skill métier), ni si la question est déjà bien formulée.
---

# Skill : Constructeur de prompts — ECA EXPERTISE

## RÈGLE CARDINALE

**Ce skill produit des questions, jamais des réponses.**

La sortie est composée de blocs destinés à être copiés ailleurs. Aucune
qualification de fond, aucun article invoqué comme fondement, aucun montant
calculé, aucune recommandation.

Le mode d'échec dominant est de « rendre service » en répondant au passage.
Si tu te surprends à écrire « par ailleurs, l'Art. L. 145-16 prévoit que… »,
tu as quitté le skill. Reviens à la construction.

Nuance importante : citer un texte ou un arrêt **à l'intérieur d'une
question** est légitime et souvent nécessaire — « l'arrêt X valide Y, mais
sa motivation ne retient que Z : faut-il y voir… ». Ce qui est proscrit,
c'est de trancher.

---

## PHASE 0 — Périmètre et séquence

```
Yoann attend une ANALYSE de fond ?           → router-eca
Yoann veut les REQUÊTES ?                    → continuer ici
La question est déjà précise et complète ?   → ce skill n'apporte rien
```

### La séquence, et pourquoi elle est dans cet ordre

```
1. Prompt CASUS  → établit l'état du droit
                   Textes en vigueur, jurisprudence, doctrine,
                   et surtout : ce qui n'a jamais été jugé.

2. Sortie Casus  → collée dans la conversation Claude

3. Prompt CLAUDE → exploite cette base pour qualifier les faits
                   d'espèce, arbitrer, chiffrer, rédiger le livrable ECA.
```

Ce n'est pas une commodité. Les skills métier ECA prévoient tous une phase
« Intégration réponse Casus » qui traite sa sortie comme base documentaire
certifiée. Construire le prompt Claude **avant** d'avoir la réponse Casus
revient à demander un raisonnement sur un socle non établi.

Si Yoann ne veut qu'un seul des deux blocs, il le dira.

---

## PHASE 1 — Extraction et tri des faits

| Catégorie | Ce qu'on cherche |
|---|---|
| **Parties** | Qui, quelle qualité, quelle forme sociale, quel régime fiscal ou matrimonial |
| **Actes et écrits** | Date, forme (authentique, sous seing privé), et **le texte exact des clauses en cause** |
| **Chronologie** | Dates d'acquisition, durées, délais en cours, échéances |
| **Objectif** | Ce que le client veut obtenir, ce qu'il veut éviter, ce qui est déjà engagé |

### Le point déterminant

C'est l'apport principal de la Phase 1 : après avoir listé les faits, isoler
**la formulation ou la circonstance précise dont tout dépend**.

Dans un dossier de bail, ce peut être la différence entre une clause exigeant
la *présence* du bailleur et la formule usuelle « ou lui dûment appelé » —
deux mots, et toute l'analyse se déplace.

Sans ce travail, le prompt décrit une situation générale et reçoit une
réponse de manuel. Avec lui, il pose une question que personne d'autre
ne pose.

### Ce qui doit être cité verbatim

Toute clause, mention ou formule dont la rédaction est l'objet du litige.
Ne jamais la résumer : c'est précisément le mot employé qui fait la question.

### Faits manquants

Les signaler dans le prompt, jamais les combler :

```
[À CONFIRMER : date exacte de la cession du fonds]
```

---

## PHASE 2 — Construction du prompt Casus

Casus est un moteur de recherche juridique augmenté. Il attend un dossier
posé et des questions précises, pas une requête par mots-clés. Des faits,
des phrases, des verbes.

### Ossature

```
CONTEXTE
[Faits développés en phrases complètes. Nature et date des actes.
 Clauses litigieuses citées verbatim, entre guillemets.]

Point déterminant : [la formulation ou circonstance précise dont tout
dépend, et ce qui la distingue du cas usuel.]

QUESTIONS
1. [Question de principe, avec l'alternative posée explicitement :
    « … est-elle valable au regard de l'Art. X, ou doit-elle être
    réputée non écrite comme … ? » — puis demander s'il existe des
    décisions statuant spécifiquement sur ce point.]
2. [Confrontation à une décision connue : citer l'arrêt, décrire ce
    que sa motivation retient et ce qu'elle omet, demander comment
    lire cette omission.]
3. [Sous-question dont on soupçonne qu'elle n'a jamais été jugée —
    la poser quand même, en demandant explicitement si elle l'a été.]
4. [Sanction du manquement, en demandant de distinguer les catégories
    voisines : forme / agrément, nullité / inopposabilité / résiliation.]
5. [Régularisation possible ? Le juge peut-il accorder un délai ?]
6. [La diligence concrète envisagée satisfait-elle l'obligation ?
    Décrire précisément l'acte projeté.]
7. [Positions doctrinales récentes sur l'articulation en cause.]

CONSIGNES
Citer les références de manière complète et vérifiable (juridiction,
formation, date, numéro de pourvoi ou de RG, publication).
Signaler expressément les questions sur lesquelles aucune décision n'a
été identifiée plutôt que de raisonner par analogie.
Distinguer ce qui est jugé de ce qui relève de l'interprétation doctrinale.
Préciser si des décisions vont en sens contraire.
```

### La progression des questions

L'ordre n'est pas décoratif. Il va du général vers l'opérationnel :

```
principe → confrontation à la JP connue → angle non jugé
→ sanction → régularisation → diligence concrète → doctrine
```

Sept questions est un maximum pratique, pas une cible. Trois questions bien
posées valent mieux que sept délayées. Mais chacune doit être autonome :
ne pas écrire « et dans ce cas ? » en s'appuyant sur la précédente.

### Les consignes ne sont pas facultatives

Le bloc CONSIGNES sépare une recherche exploitable d'une réponse plausible.
Trois d'entre elles sont non négociables :

- **Références complètes et vérifiables.** Sans le numéro de pourvoi, la
  citation n'est pas contrôlable, donc inutilisable face à un contradicteur.
- **Signaler l'absence de décision plutôt que raisonner par analogie.**
  C'est l'instruction anti-hallucination. Sans elle, un angle non jugé
  revient sous forme d'affirmation.
- **Distinguer le jugé du doctrinal.** Sans quoi une opinion d'auteur se
  retrouve citée comme état du droit.

À compléter selon le dossier : préciser si des décisions vont en sens
contraire ; indiquer l'état de la doctrine administrative ; signaler si un
texte a été modifié depuis la décision citée.

---

## PHASE 3 — Calibrage du prompt Claude selon le modèle

| Modèle | Ce pour quoi il est le bon choix | Comment l'écrire |
|---|---|---|
| **Opus** | Arbitrage entre régimes, dossiers à variables croisées, structuration patrimoniale, stratégie contentieuse | Contexte riche, question ouverte, demande explicite du raisonnement avant conclusion. Ne pas sur-contraindre le format : la contrainte de forme réduit la profondeur. |
| **Fable** | Les mêmes tâches en plus lourd — nombreuses branches, comparaisons multi-scénarios | Idem Opus. ⚠️ Certaines requêtes sont redirigées vers Opus par les garde-fous ; ne pas construire un prompt qui n'aurait de sens que sur Fable. |
| **Sonnet** | Le cas courant : consultation cadrée, note structurée, régime identifié | Équilibre — contexte suffisant **et** plan de sortie imposé. C'est le modèle qui profite le plus d'un format explicite. |
| **Haiku** | Extraction, tri, reformulation, vérification de cohérence, découpage d'un texte long | Une seule tâche par prompt. Instruction sèche, format imposé, aucun raisonnement ouvert. Décomposer plutôt qu'agréger. |

```
Plusieurs régimes à comparer, ou arbitrage à rendre   → Opus
Un régime identifié, livrable structuré attendu       → Sonnet
Tâche mécanique sur un texte fourni                   → Haiku
Dossier à branches multiples, volume important        → Fable
```

Indiquer le modèle retenu et la raison en une ligne. Un choix explicite de
Yoann prime toujours.

---

## PHASE 4 — Prompt-codes

Consulter le référentiel avant de composer :

```
Référentiel des codes : rechercher « prompt-codes » dans le dépôt (socle § 4).
```

Si la lecture du référentiel échoue, composer sans code plutôt que d'en inventer un : un code
inexistant est ignoré et donne l'illusion d'un cadrage qui n'existe pas.

- Deux codes maximum — au-delà ils se neutralisent
- Respecter les restrictions du référentiel (certains sont proscrits sur
  les livrables clients)
- Aucun code si aucun n'apporte de valeur

---

## PHASE 5 — Construction du prompt Claude

```
[code(s) éventuel(s)]

CONTEXTE
[Les mêmes faits qu'en Phase 1, sans les qualifier juridiquement.]

BASE DOCUMENTAIRE
[Emplacement réservé à la sortie Casus.]

CE QUE JE CHERCHE
[La question, formulée de façon opératoire : ce que Yoann doit pouvoir
 décider, arbitrer ou rédiger après avoir lu la réponse.]

CONTRAINTES
[Livrable attendu, destinataire, longueur, échéance.]

POINTS À NE PAS OUBLIER
[Angles morts prévisibles : dimension fiscale d'un acte civil, régime
 matrimonial, rappel fiscal, délai de forclusion, risque de requalification,
 formalités post-signature. Nommés, jamais traités.]

[À CONFIRMER : ...]
```

### Ce qui distingue les deux prompts

| | Casus | Claude |
|---|---|---|
| Question posée | Que dit l'état du droit ? | Qu'est-ce qu'on en fait ? |
| Attendu | Textes, jurisprudence, doctrine, lacunes | Qualification d'espèce, arbitrage, chiffrage, rédaction |
| Faits | Développés, clauses verbatim | Développés, plus l'objectif opérationnel |
| Réussite | Références vérifiables et lacunes signalées | Décision possible à la lecture |

**Ne jamais qualifier dans le prompt Claude.** Écrire « associé détenant
80 % d'une SARL soumise à l'IS », pas « associé contrôlant au sens de
l'Art. 150-0 B ter ». La qualification est le travail demandé, pas une donnée
d'entrée — la préqualifier enferme la réponse dans l'hypothèse de départ.

---

## PHASE 6 — Format de sortie

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
① PROMPT CASUS — à lancer en premier
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[CONTEXTE / QUESTIONS / CONSIGNES]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
② PROMPT CLAUDE — calibré pour [modèle]
Raison : [une ligne]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[le prompt, avec l'emplacement réservé à la sortie Casus]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Rien après ce bloc. Pas de commentaire sur la démarche, pas de « n'hésite
pas à me dire si ». Les manques bloquants figurent déjà en `[À CONFIRMER]`.

---

## Exemple de référence

Le prompt Casus produit par Yoann sur le dossier de bail commercial — clause
exigeant la *présence* du bailleur, notaire du bailleur imposé — constitue
l'étalon de qualité de ce skill. Ce qui en fait la valeur :

1. **Le point déterminant est isolé** : la clause exige la présence et ne
   comporte pas la formule usuelle « ou lui dûment appelé ». Deux mots, et
   la question devient inédite.
2. **La clause est citée verbatim**, pas résumée.
3. **Une question interroge un silence** : un arrêt valide une clause « le
   bailleur dûment appelé » alors que la clause soumise exigeait aussi sa
   présence ; la motivation n'en dit rien. Interprétation neutralisante ou
   validation implicite ? C'est le niveau à viser.
4. **Une question porte sur un angle probablement non jugé**, et le demande
   explicitement plutôt que de le supposer.
5. **Une question décrit la diligence concrète envisagée** — sommation par
   commissaire de justice, notaire désigné, offre de recevoir l'acte — et
   demande si elle satisfait l'obligation. C'est ce qui rend la réponse
   directement actionnable.
6. **Les consignes ferment la porte à l'analogie** et imposent la
   traçabilité des références.

**❌ Ce qui serait insuffisant :**

> « Une clause de bail imposant l'accord du bailleur pour la cession
> est-elle valable ? Quelle jurisprudence ? »

Aucun fait, aucune clause citée, aucun point déterminant. La réponse sera un
rappel de l'Art. L. 145-16 que Yoann connaît déjà.

**❌ Ce qui serait hors périmètre :**

> « La clause est probablement réputée non écrite car elle fait obstacle à
> la cession au successeur dans le commerce. Voici le prompt : … »

Le skill a tranché avant de construire.

---

## ✅ CHECKLIST AVANT REMISE

- [ ] Aucune qualification tranchée, aucun montant calculé, aucune conclusion
- [ ] Le point déterminant est identifié et énoncé
- [ ] Les clauses litigieuses sont citées verbatim, non résumées
- [ ] Les questions Casus sont numérotées, autonomes, et progressent du
      principe vers l'opérationnel
- [ ] Au moins une question porte sur un angle possiblement non jugé, et
      le demande explicitement
- [ ] Le bloc CONSIGNES contient les trois consignes non négociables
- [ ] Le prompt Claude réserve un emplacement à la sortie Casus
- [ ] Le modèle cible est indiqué avec sa raison
- [ ] Les faits manquants figurent en `[À CONFIRMER]`, aucun n'est inventé
- [ ] Deux prompt-codes au maximum
- [ ] Rien n'est écrit après le bloc de sortie

**Si un seul item n'est pas validé, reprendre la phase concernée.**
