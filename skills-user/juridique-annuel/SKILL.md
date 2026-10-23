---
name: juridique-annuel
description: >
  Cycle juridique annuel des sociétés clientes d'ECA EXPERTISE : approbation des
  comptes, affectation du résultat, distribution de dividendes (y compris en
  cours d'exercice ou sur réserves), conventions réglementées, rémunération des
  dirigeants, capitaux propres inférieurs à la moitié du capital, dépôt des
  comptes et option de confidentialité, prorogation du délai d'approbation.
  Pré-remplit les actes à partir des données comptables (Pennylane) et peut
  traiter un lot de sociétés. Déclencher sur : AGOA, AGO annuelle, approbation
  des comptes, affectation du résultat, dividendes, distribution, report à
  nouveau, réserve légale, décision de l'associé unique sur les comptes,
  conventions réglementées, rapport de gestion, capitaux propres négatifs,
  perte de la moitié du capital, dépôt des comptes, confidentialité des comptes,
  prorogation AGO, juridique annuel. NE PAS utiliser pour une modification
  statutaire (→ redaction-acte) ou une question de stratégie de rémunération
  dirigeant sans acte (→ consultation-juridique).
---

# Juridique annuel — ECA EXPERTISE

Le juridique annuel est l'acte le plus répété du cabinet. L'objectif : un PV
exact du premier coup, nourri des vrais chiffres, avec les alertes que le
dossier impose — sans recopier un taux ou un seuil de mémoire.

Charger `socle-eca`. Pour la rédaction, ce skill s'appuie sur les étapes 3 à 8
de `redaction-acte`.

---

## Phase 0 — Mode

```
Une société, un exercice            → MODE UNITAIRE
Liste de sociétés (campagne)        → MODE LOT : produire d'abord le tableau de
                                       contrôle (phase 2) pour toutes, puis les
                                       actes après validation
Distribution hors approbation       → MODE DISTRIBUTION (acompte, réserves)
```

## Phase 1 — Données (ne rien saisir à la main si une source existe)

1. **Identité** : Radar (forme, capital, dirigeants, CAC éventuel) ; écart avec
   les statuts → signaler.
2. **Statuts en vigueur** : forme des décisions, organe compétent, majorités,
   consultation écrite possible, affectation statutaire, rémunération des
   dirigeants (organe compétent).
3. **Comptes** : Pennylane (balance et états de l'exercice) — résultat,
   report à nouveau antérieur, réserves (légale, statutaires, facultatives),
   capital, capitaux propres, comptes courants d'associés, rémunérations
   comptabilisées des dirigeants, conventions identifiables (loyers, prêts,
   prestations entre la société et ses associés, dirigeants ou sociétés liées).
   Si les comptes ne sont pas arrêtés : le dire et travailler sur projet balisé.
4. **Historique** : PV de l'exercice précédent (fiche mémoire, dépôt, mails),
   distributions antérieures, acomptes déjà versés.
5. **Associés** : répartition du capital, démembrements, associé personne morale
   (régime des dividendes reçus), dirigeant non salarié.

## Phase 2 — Tableau de contrôle (avant tout acte)

Pour chaque société, une ligne ; chaque point se vérifie à la source en vigueur.

| Contrôle | À vérifier | Points d'entrée (lire la version en vigueur) |
|---|---|---|
| Délai d'approbation | Respect du délai légal ; prorogation à demander si dépassé | C. com. L. 223-26 (SARL), L. 225-100 (SA), L. 227-9 et statuts (SAS) |
| Organe et forme | AGO, consultation écrite, acte unanime, associé unique (registre, approbation par dépôt dans certains cas d'EURL) | C. com. L. 223-27, L. 223-31, L. 227-9 ; statuts |
| Affectation | Dotation de la réserve légale jusqu'au plafond ; bénéfice distribuable ; pertes antérieures à apurer | C. com. L. 232-10 et L. 232-11 |
| Distribution | Bénéfice distribuable suffisant ; décision de l'organe compétent (distribution irrégulière = risque de nullité et de répétition) | C. com. L. 232-11, L. 232-12 ; Cass. com. 12 févr. 2025, n° 23-11.410 (à relire avant citation) |
| Dividendes de dirigeants non salariés | Fraction des dividendes soumise aux cotisations sociales selon le statut et la détention familiale | CSS L. 136-3 en vigueur (règle refondue depuis 2025) — ne jamais appliquer un seuil de mémoire |
| Fiscalité de la distribution | Prélèvement à la source et déclaration des revenus distribués ; associé personne morale | CGI art. 117 quater, 242 ter, 145 et 216 ; formulaires en vigueur |
| Conventions réglementées | Rapport spécial, vote, associé intéressé exclu du vote selon la forme ; conventions courantes | C. com. L. 223-19 à L. 223-21 (SARL), L. 227-10 (SAS), L. 225-38 s. (SA) |
| Rémunération des dirigeants | Organe compétent selon statuts (SARL : statuts ou décision collective ; gérant associé votant selon la jurisprudence en vigueur) ; ratification si versée sans décision préalable | Statuts ; jurisprudence Cass. com. à vérifier (Pourvoi) — aucun article du code ne fixe l'organe pour la SARL |
| Capitaux propres < ½ capital | Décision de dissolution ou non dans le délai légal, publicité, régularisation dans le délai | C. com. L. 223-42 (SARL), L. 225-248 (SA, et SAS par renvoi) |
| Comptes courants débiteurs | Associé ou dirigeant personne physique : interdiction et sanctions possibles | C. com. L. 223-21 (SARL), L. 225-43 (SA) et L. 227-12 (SAS) ; relier au dossier si déjà identifié |
| Dépôt et confidentialité | Dépôt dans le délai ; option de non-publicité selon la taille et l'appartenance à un groupe | C. com. L. 232-21 à L. 232-23, L. 232-25 |
| Commissaire aux comptes | Rapports à viser ; fin de mandat à renouveler ou non | C. com. L. 823-1 s. |

Toute anomalie → colonne « Alerte » + action proposée. **Point de contrôle :
présenter le tableau à Yoann (ou au collaborateur du dossier) avant les actes.**

## Phase 3 — Rédaction des actes

1. Modèle du dépôt (socle § 4) correspondant à la forme : PV d'AGO, décisions
   unanimes, décision de l'associé unique, acompte sur dividende, prorogation.
   Le dépôt ne contient pas de modèle d'approbation complet à ce jour : le
   signaler et, après validation, en proposer un **anonymisé** à y ajouter.
2. Contenu minimal :
   - mentions d'identification exactes ; organe, convocation ou modalité,
     présents et représentés, quorum et majorité, documents communiqués ;
   - approbation des comptes et quitus (si les statuts le prévoient) ;
   - affectation détaillée au centime (bénéfice ou perte, réserve légale,
     autres réserves, dividendes, report à nouveau) avec contrôle arithmétique
     **par calcul**, pas de tête ;
   - distribution : montant global, montant par titre, date de mise en
     paiement, prélèvement sur quels postes ; rappel des distributions des
     trois exercices précédents si la loi l'exige pour la forme ;
   - conventions réglementées ; rémunérations ; renouvellements de mandats ;
   - décision sur les capitaux propres si le seuil est franchi ;
   - pouvoirs pour formalités.
3. Standard du socle § 6 pour la forme ; Word ECA (socle § 8).
4. **Démembrement** : identifier qui vote quoi (affectation des bénéfices,
   autres décisions) selon les statuts et la loi ; qui perçoit le dividende ;
   distribution prélevée sur des réserves → question du quasi-usufruit à
   signaler (renvoi strategie-patrimoniale si enjeu).

## Phase 4 — Contrôles et suites

- Arithmétique de l'affectation recalculée par script.
- Cohérence entre PV, liasse et Pennylane (résultat, réserves, dividendes).
- `legal-hallucination-checker` sur toute référence citée dans le PV ou la note.
- « Échéances » : dépôt des comptes, paiement des dividendes, déclarations des
  revenus distribués, régularisation des capitaux propres, fin de mandat CAC.
- MODE LOT : un tableau récapitulatif final (société / statut / alertes /
  actes produits / échéances) à transmettre au collaborateur en charge.

---

## Pièges récurrents

- Distribuer des sommes sans décision de l'organe compétent, ou au-delà du
  bénéfice distribuable.
- Oublier la réserve légale ou l'imputer sur le mauvais poste.
- Ignorer une convention réglementée visible en comptabilité (loyer versé à la
  SCI du dirigeant, prêt d'associé).
- Laisser passer un franchissement du seuil des capitaux propres sans décision.
- Appliquer de mémoire un seuil de cotisations sur dividendes : le régime a été
  refondu, lire le texte en vigueur.
