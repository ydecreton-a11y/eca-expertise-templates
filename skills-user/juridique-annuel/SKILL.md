---
name: juridique-annuel
description: "Cycle juridique annuel des sociétés clientes d'ECA EXPERTISE : approbation des comptes, affectation du résultat, dividendes (acompte, réserves), conventions réglementées, rémunération des dirigeants, capitaux propres inférieurs à la moitié du capital, dépôt et confidentialité des comptes, prorogation. Part de la trame N-1 du dossier interne connecté, ou, pour un dossier repris d'un confrère ou une société nouvellement immatriculée, des modèles du dépôt et des précédents ECA. Pré-remplit les actes depuis Pennylane ; traite un lot. Déclencher sur : AGOA, AGO annuelle, approbation des comptes, affectation du résultat, dividendes, acompte sur dividende, report à nouveau, réserve légale, associé unique, conventions réglementées, capitaux propres négatifs, dépôt des comptes, prorogation AGO, juridique annuel, premier exercice, reprise de dossier. NE PAS utiliser pour une modification statutaire (→ redaction-acte) ou une stratégie de rémunération sans acte (→ consultation-juridique)."
---

# Juridique annuel — ECA EXPERTISE

Le juridique annuel est l'acte le plus répété du cabinet. L'objectif : un PV
exact du premier coup, nourri des vrais chiffres, avec les alertes que le
dossier impose — sans recopier un taux ou un seuil de mémoire.

Charger `socle-eca`. Pour la rédaction, ce skill s'appuie sur les étapes 3 à 8
de `redaction-acte`. Les références marquées « vérifié 23/10/2026 » ont été
lues à la source à cette date ; elles se relisent dans leur version applicable
à l'exercice traité.

---

## Phase 0 — Mode et situation du dossier

```
Une société, un exercice            → MODE UNITAIRE
Liste de sociétés (campagne)        → MODE LOT : produire d'abord le tableau de
                                       contrôle (phase 2) pour toutes, puis les
                                       actes après validation
Distribution hors approbation       → MODE DISTRIBUTION (acompte, réserves) :
                                       lire d'abord l'encadré de la Phase 2
```

Qualifier en même temps la **situation du dossier**, qui détermine la source
de la trame (Phase 1 bis) :

```
Client historique du cabinet        → SITUATION A (trame N-1 interne)
Dossier repris d'un confrère        → SITUATION B (reconstitution)
Société nouvellement immatriculée   → SITUATION C (premier exercice)
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
4. **Historique et trame** : voir Phase 1 bis.
5. **Associés** : répartition du capital, démembrements, associé personne morale
   (régime des dividendes reçus), dirigeant non salarié.

## Phase 1 bis — Hiérarchie des sources de la trame

**Règle transversale : la trame fournit la structure, jamais la vérité.** Toute
mention reprise d'un PV antérieur (organe, quitus, majorité, conventions,
mandats, répartition du capital) est contrôlée contre les statuts en vigueur,
Radar et les comptes de l'exercice. Une erreur de N-1 recopiée en N devient
une erreur répétée.

| Situation | Ordre de recherche de la trame | Contrôles spécifiques |
|---|---|---|
| **A — Client historique** | 1. Dossier interne du client s'il est connecté à la session (dossier relié au poste via Cowork ou l'application de bureau ; SharePoint ou mails via Microsoft 365) : PV et rapports N-1, registre des décisions ; 2. fiche mémoire du dossier et conversations passées (recherche sur le nom de la société) ; 3. modèle du dépôt | Trame N-1 conforme aux statuts actuels (modifications statutaires intervenues depuis ?) ; mandats arrivant à échéance ; conventions nouvelles visibles en comptabilité |
| **B — Reprise d'un confrère** | 1. PV antérieurs remis par le client ou par le confrère prédécesseur ; 2. pièces déposées au greffe : avec les comptes annuels sont déposées la proposition d'affectation et la résolution ou décision d'affectation (C. com. L. 232-22 pour les SARL, L. 232-23 pour les sociétés par actions — vérifiés 23/10/2026) ; 3. modèle du dépôt ; 4. précédents ECA anonymisés de même forme | Approbations des exercices antérieurs effectivement décidées ? Comptes déposés ? Registre des décisions tenu et à jour ? Historique des distributions et acomptes ? Conventions réglementées antérieures et leur approbation ? Rémunérations décidées par l'organe compétent ? Toute lacune → alerte et proposition de régularisation (décisions de régularisation par exercice), à valider avec Yoann avant l'acte de l'exercice |
| **C — Nouvelle immatriculation** | 1. Statuts constitutifs et pièces de constitution du dossier interne ; 2. modèle du dépôt ; 3. précédents ECA anonymisés de même forme ; 4. conversations passées sur des premiers exercices comparables | Durée et dates du premier exercice selon les statuts ; reprise des engagements de la période de formation : à défaut de reprise, les personnes ayant agi en restent tenues solidairement et indéfiniment (C. com. L. 210-6) ; reprise automatique par la signature des statuts pour les actes figurant à l'état annexé, ou par l'immatriculation pour les actes déterminés couverts par un mandat (R. 210-5 pour les SARL, R. 210-6 pour les sociétés par actions — vérifiés 23/10/2026) ; les autres engagements exigent une décision de reprise ; première dotation de la réserve légale ; absence d'historique de distributions ; premières conventions (bail, compte courant d'apport) |

Traçabilité : indiquer dans la note « Trame : [source] » ; si aucune trame
n'est trouvée, le dire (« Ressource absente : PV N-1 ») et partir du modèle.

Confidentialité : un précédent d'un autre client ne sert que de structure ;
aucun nom, chiffre ou donnée n'en est repris (socle § 4 et § 7.2).

## Phase 2 — Tableau de contrôle (avant tout acte)

Pour chaque société, une ligne ; chaque point se vérifie à la source en vigueur.

| Contrôle | À vérifier | Points d'entrée (lire la version en vigueur) |
|---|---|---|
| Délai d'approbation | Respect du délai légal ; prorogation à demander si dépassé | C. com. L. 223-26 (SARL), L. 225-100 (SA), L. 227-9 et statuts (SAS) |
| Organe et forme | AGO, consultation écrite, acte unanime, associé unique (registre, approbation par dépôt dans certains cas d'EURL) | C. com. L. 223-27, L. 223-31, L. 227-9 ; statuts |
| Affectation | Dotation de la réserve légale jusqu'au plafond ; bénéfice distribuable = bénéfice de l'exercice, diminué des pertes antérieures et des dotations aux réserves légales ou statutaires, augmenté du report bénéficiaire | C. com. L. 232-10 ; L. 232-11, al. 1 (vérifié 23/10/2026) |
| Distribution | Sommes distribuables constatées après approbation ; décision de l'organe compétent ; aucune distribution si les capitaux propres sont ou deviendraient inférieurs au capital augmenté des réserves indisponibles ; dividende distribué en violation = dividende fictif | C. com. L. 232-11, al. 3 ; L. 232-12 (vérifiés 23/10/2026) |
| Dividendes de dirigeants non salariés | Part des dividendes intégrée à l'assiette sociale au-delà d'un seuil calculé sur le capital, les primes et les comptes courants détenus par le travailleur indépendant et sa famille proche | CSS L. 136-3, II, 2° (vérifié 23/10/2026) — relire la version applicable à l'année, ne jamais appliquer le seuil de mémoire |
| Fiscalité de la distribution | Prélèvement à la source et déclaration des revenus distribués ; associé personne morale | CGI art. 117 quater, 242 ter, 145 et 216 ; formulaires en vigueur |
| Conventions réglementées | Rapport spécial, vote, associé intéressé exclu du vote selon la forme ; conventions courantes | C. com. L. 223-19 à L. 223-21 (SARL), L. 227-10 (SAS), L. 225-38 s. (SA) |
| Rémunération des dirigeants | Organe compétent selon statuts (SARL : statuts ou décision collective ; gérant associé votant selon la jurisprudence en vigueur) ; ratification si versée sans décision préalable | Statuts ; jurisprudence Cass. com. à rechercher via Pourvoi — aucun article du code ne fixe l'organe pour la SARL |
| Capitaux propres < ½ capital | Décision de dissolution ou non dans le délai légal, publicité, régularisation dans le délai | C. com. L. 223-42 (SARL), L. 225-248 (SA, et SAS par renvoi) |
| Comptes courants débiteurs | Associé ou dirigeant personne physique : interdiction et sanctions possibles | C. com. L. 223-21 (SARL), L. 225-43 (SA) et L. 227-12 (SAS) ; relier au dossier si déjà identifié |
| Dépôt et confidentialité | Dépôt dans le délai (un mois après l'approbation, deux mois par voie électronique) avec la proposition et la décision d'affectation ; option de non-publicité selon la taille et l'appartenance à un groupe | C. com. L. 232-21, L. 232-22 et L. 232-23 (vérifiés 23/10/2026 pour L. 232-22 et L. 232-23), L. 232-25 |
| Commissaire aux comptes | Rapports à viser ; fin de mandat à renouveler ou non | C. com. L. 823-1 s. |
| Historique (situations B et C) | Lacunes des exercices antérieurs, reprise des engagements de la période de formation | Phase 1 bis |

### ⚠️ MODE DISTRIBUTION — ce qui peut être distribué, et par quel organe

- **Report à nouveau bénéficiaire** : il entre dans le bénéfice distribuable
  de l'exercice suivant ; **seule l'assemblée qui approuve les comptes de cet
  exercice** peut décider son affectation et, le cas échéant, sa
  distribution. Une décision prise par une autre assemblée encourt la
  nullité — mais s'impose aux associés tant que la nullité n'a pas été
  prononcée (Cass. com., 12 févr. 2025, n° 23-11.410, publié — sommaires
  officiels lus via Pourvoi le 23/10/2026 ; lire le texte intégral avant de
  le citer dans un acte ou une note client).
- **Réserves disponibles** : l'assemblée peut décider la distribution de
  sommes prélevées sur les réserves dont elle a la disposition, en indiquant
  **expressément les postes** prélevés ; les dividendes sont prélevés par
  priorité sur le bénéfice distribuable de l'exercice (L. 232-11, al. 2,
  vérifié 23/10/2026).
- **Acompte sur dividende** : uniquement au vu d'un bilan établi en cours ou
  en fin d'exercice et **certifié par un commissaire aux comptes**, dans la
  limite du bénéfice réalisé depuis la clôture précédente (L. 232-12, al. 2,
  vérifié 23/10/2026). Société sans CAC : prévoir la certification de ce
  bilan, sinon pas d'acompte.
- Tout dividende distribué en violation de ces règles est un **dividende
  fictif** (L. 232-12, al. 3) : risque de répétition et de responsabilité.

Toute anomalie → colonne « Alerte » + action proposée. **Point de contrôle :
présenter le tableau à Yoann (ou au collaborateur du dossier) avant les actes.**

## Phase 3 — Rédaction des actes

1. Trame retenue en Phase 1 bis. À défaut de trame propre au dossier :
   rechercher dans le dépôt, à la date du jour (inventaire, socle § 4 et
   § 4 bis), le modèle correspondant à la forme : PV d'AGO, décisions
   unanimes, décision de l'associé unique, acompte sur dividende, prorogation.
   Si aucun modèle complet n'y figure : le signaler et, après validation, en
   proposer un **anonymisé** à y ajouter.
2. Contenu minimal :
   - mentions d'identification exactes ; organe, convocation ou modalité,
     présents et représentés, quorum et majorité, documents communiqués ;
   - approbation des comptes et quitus (si les statuts le prévoient) ;
   - affectation détaillée au centime (bénéfice ou perte, réserve légale,
     autres réserves, dividendes, report à nouveau) avec contrôle arithmétique
     **par calcul**, pas de tête ;
   - distribution : montant global, montant par titre, date de mise en
     paiement, postes prélevés (expressément pour les réserves) ; rappel des
     distributions des trois exercices précédents si la loi l'exige pour la
     forme ;
   - conventions réglementées ; rémunérations ; renouvellements de mandats ;
   - décision sur les capitaux propres si le seuil est franchi ;
   - situation C : reprise des engagements de la période de formation non
     couverts par l'état annexé ou le mandat, à valider avec Yoann ;
   - pouvoirs pour formalités.
3. Standard du socle § 6 pour la forme ; Word ECA (socle § 8).
4. **Démembrement** : identifier qui vote quoi (affectation des bénéfices,
   autres décisions) selon les statuts et la loi ; qui perçoit le dividende ;
   distribution prélevée sur des réserves → question du quasi-usufruit à
   signaler (renvoi strategie-patrimoniale si enjeu).

## Phase 4 — Contrôles et suites

- Arithmétique de l'affectation recalculée par script.
- Cohérence entre PV, liasse et Pennylane (résultat, réserves, dividendes).
- Cohérence entre PV de N et trame N-1 : tout écart (capital, dirigeants,
  mandats, répartition) est justifié ou signalé.
- `legal-hallucination-checker` sur toute référence citée dans le PV ou la note.
- « Échéances » : dépôt des comptes, paiement des dividendes, déclarations des
  revenus distribués, régularisation des capitaux propres, fin de mandat CAC,
  régularisations d'exercices antérieurs (situation B).
- MODE LOT : un tableau récapitulatif final (société / situation A-B-C /
  source de la trame / statut / alertes / actes produits / échéances) à
  transmettre au collaborateur en charge.

---

## Pièges récurrents

- Distribuer des sommes sans décision de l'organe compétent, ou au-delà du
  bénéfice distribuable.
- Distribuer le report à nouveau en cours d'exercice, hors de l'assemblée
  d'approbation suivante (Cass. com., 12 févr. 2025, n° 23-11.410).
- Prélever sur les réserves sans indiquer expressément les postes.
- Verser un acompte sans bilan certifié par un commissaire aux comptes.
- Oublier la réserve légale ou l'imputer sur le mauvais poste.
- Ignorer une convention réglementée visible en comptabilité (loyer versé à la
  SCI du dirigeant, prêt d'associé).
- Laisser passer un franchissement du seuil des capitaux propres sans décision.
- Appliquer de mémoire un seuil de cotisations sur dividendes : lire
  CSS L. 136-3 dans sa version applicable.
- Recopier la trame N-1 sans la confronter aux statuts en vigueur (quitus non
  prévu, organe erroné, mandat expiré).
- Dossier repris : produire l'acte de l'exercice sans avoir vérifié que les
  exercices antérieurs ont été approuvés et déposés.
