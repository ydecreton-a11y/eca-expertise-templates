---
name: redaction-acte
description: >
  Moteur de rédaction des actes de droit des sociétés ECA EXPERTISE : statuts,
  décisions et PV (AGE, unanimes, associé unique), nomination ou révocation de
  dirigeant, transfert de siège, objet, capital, transformation, pouvoirs.
  Standard M&A international, modèle du dépôt par défaut, références vérifiées.
  Déclencher sur : rédige, acte, statuts, PV, procès-verbal, décision d'associé
  unique, AGE, nomination, révocation, transfert de siège, objet social,
  augmentation ou réduction de capital, transformation, pouvoir.
  NE PAS utiliser si un skill de process couvre l'acte : pacte (→ pacte-associes),
  comptes et dividendes (→ juridique-annuel), apport à holding (→ holding-apport),
  dissolution, liquidation, TUP (→ dissolution-liquidation-tup), cession de titres
  (→ protocole-cession), cession de fonds (→ cession-fonds), contrat entre
  parties (→ analyse-contrat). Pas d'actes réservés au notaire.
---

# Rédaction d'actes — moteur ECA

Ce skill est aussi le **moteur commun** des skills de process (pacte-associes,
juridique-annuel, holding-apport, dissolution-liquidation-tup) : ils renvoient
à ses étapes 3 à 8 pour la rédaction proprement dite.

Charger d'abord `socle-eca` (ouverture du dossier, connecteurs, standard de
rédaction § 6, méthode Word § 8).

---

## Étape 0 — Aiguillage

```
Acte couvert par un skill de process ?           → ce skill (voir description)
Question de fond non tranchée (fiscalité, validité, régime) ?
                                                 → consultation-juridique d'abord
Donation, contrat de mariage, acte sur immeuble  → note ou projet de clauses
  nécessitant la forme authentique                 pour le notaire (socle § 7.3)
Sinon                                            → continuer
```

## Étape 1 — Ouverture du dossier (socle § 1)

Mémoire dossier, historique, Granola/mails, **Radar** pour l'identité exacte
(dénomination, forme, capital, siège, RCS, dirigeants). Ne jamais reporter dans
un acte une donnée d'identification non vérifiée ; en cas d'écart entre Radar,
les statuts et les dires du client, le signaler et demander.

Recueillir les **statuts en vigueur** : un acte se rédige au regard des
stipulations statutaires (convocation, quorum, majorités, agrément, pouvoirs).
S'ils manquent, les demander — ne pas présumer le régime légal supplétif.

## Étape 2 — Plan et validation

Présenter un plan numéroté : acte(s) à produire, décisions, majorités requises,
formalités consécutives, pièces manquantes. **Attendre la validation de Yoann.**

## Étape 3 — Modèle du dépôt

1. Rechercher dans le dépôt (socle § 4) le ou les précédents correspondant au
   type d'acte et à la forme sociale ; lister ceux trouvés, retenir le plus proche.
2. Lire le modèle **intégralement** (corps, tableaux, notes, champs surlignés).
3. Vérifier toutes ses références légales à la source ; signaler tout écart et
   proposer la clause corrigée.
4. Purger toute donnée d'un autre client.
5. Aucun modèle pertinent : le dire, rédiger depuis le standard du socle § 6.

## Étape 4 — Points d'entrée juridiques par famille d'acte

Ces points sont des **pistes à vérifier**, pas des règles à recopier : lire
chaque texte dans sa version en vigueur et confronter aux statuts.

| Acte | À contrôler |
|---|---|
| Statuts (constitution, refonte) | Mentions obligatoires selon la forme ; clauses d'agrément, de préemption, d'inaliénabilité, d'exclusion, de changement de contrôle et leurs majorités d'adoption propres ; dirigeants et leurs pouvoirs ; exercice, affectation ; cohérence avec un pacte existant |
| Décisions collectives / AGE | Organe compétent, convocation, quorum et majorité selon statuts et forme ; décisions relevant de l'unanimité ; droit de vote en cas de démembrement des titres |
| Associé unique | Forme (registre, mentions) ; décisions réservées |
| Nomination / révocation | Compétence, juste motif selon la forme et les statuts ; rémunération et son organe ; déclaration des bénéficiaires effectifs si changement |
| Transfert de siège / objet | Compétence (organe de direction ou collectif selon forme et statuts) ; ratification ; conséquences fiscales d'un changement d'activité |
| Capital (augmentation, réduction) | Droit préférentiel, renonciation, rapport, commissaire aux apports selon seuils en vigueur, réduction non motivée par des pertes et opposition des créanciers |
| Transformation | Rapport du commissaire à la transformation selon les cas ; unanimité éventuelle ; conséquences fiscales (cessation ou non) |

Si l'acte touche une **distribution**, renvoyer à juridique-annuel ; une
**cession de titres** à protocole-cession (mode cession simple).

## Étape 5 — Tableau de décision clausale

Avant de rédiger, pour tout acte de plus de quelques décisions (statuts, refonte,
PV complexe), produire un tableau : clause / option retenue / justification
(statuts, dossier, demande) / risque si exclue / question au client. Poser les
questions ouvertes **avant** de rédiger.

## Étape 6 — Rédaction

Appliquer intégralement le **standard du socle § 6** (définitions et
interprétation, numérotation, paragraphes en bloc, délais qualifiés, clauses de
procédure et de style, option la plus sécurisante, annexe « Points de vigilance
ECA »). Reprendre le texte du modèle quand il est juste ; ne le paraphraser que
pour l'adapter aux termes définis du dossier.

## Étape 7 — Contrôle de cohérence

- Renvois internes, numérotation, termes définis tous utilisés et tous définis.
- Cohérence avec les statuts, le pacte, les actes antérieurs du dossier.
- Répercussions de chaque modification sur le reste du document (socle § 6.10).
- Délais : tous qualifiés, point de départ et notification précisés.
- Aucune trace d'un autre client, d'un modèle ou d'un auteur tiers.

## Étape 8 — Livrable et formalités

1. Word ECA selon socle § 8 (titres d'actes en noir gras).
2. Liste des **formalités consécutives** (dépôt, publicité, enregistrement,
   bénéficiaires effectifs, pouvoirs) avec leurs délais **lus à la source**.
3. `legal-hallucination-checker` (bloquant), puis `avocat-adverse` si l'acte
   engage des intérêts divergents, puis `positions-eca`.
4. Section « Échéances » si un délai court à compter de l'acte.

---

## Comportements à éviter

- Rédiger avant d'avoir les statuts en vigueur ou avant validation du plan.
- Recopier un délai, un seuil ou un taux du modèle sans le vérifier.
- Laisser une mention d'un autre dossier dans un acte issu d'un précédent.
- Mélanger dans un même PV des décisions relevant d'organes ou de majorités
  différentes sans les distinguer.
