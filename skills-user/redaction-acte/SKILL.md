---
name: redaction-acte
description: "Moteur de rédaction des actes de droit des sociétés ECA EXPERTISE et fiches de toutes les modifications statutaires : statuts, décisions et PV (AGE, unanimes, associé unique), dénomination, siège, objet, date de clôture, durée et prorogation, capital (augmentation, réduction, incorporation), transformation, dirigeants, clauses statutaires, mise en harmonie, passage à l'associé unique, pouvoirs. Organe, majorité, répercussions, formalités, standard M&A. Déclencher sur : rédige, acte, statuts, PV, AGE, décision d'associé unique, nomination, révocation, dénomination, transfert de siège, objet social, date de clôture, prorogation, capital, transformation, mise à jour des statuts, pouvoir. NE PAS utiliser si un skill de process couvre l'acte : pacte (→ pacte-associes), comptes (→ juridique-annuel), apport à holding (→ holding-apport), fusion, scission, APA (→ restructurations), dissolution, TUP (→ dissolution-liquidation-tup), cession (→ protocole-cession, cession-fonds), contrat (→ analyse-contrat)."
---

# Rédaction d'actes — moteur ECA

Ce skill est aussi le **moteur commun** des skills de process (pacte-associes,
juridique-annuel, holding-apport, restructurations,
dissolution-liquidation-tup, acte-definitif-titres) : ils renvoient à ses
étapes 3 à 8 pour la rédaction proprement dite.

Charger d'abord `socle-eca` (ouverture du dossier, connecteurs, standard de
rédaction § 6, méthode Word § 8). Les références marquées « vérifié
23/10/2026 » ont été lues à la source à cette date ; elles se relisent dans
leur version applicable à la date de l'acte. Toute autre référence est un
point d'entrée à lire avant d'être citée.

---

## Étape 0 — Aiguillage

```
Acte couvert par un skill de process ?           → ce skill (voir description)
Question de fond non tranchée (fiscalité, validité, régime) ?
                                                 → consultation-juridique d'abord
Donation, contrat de mariage, acte sur immeuble  → note ou projet de clauses
  nécessitant la forme authentique                 pour le notaire (socle § 7.3)
Transfert de siège à l'étranger, transformation  → consultation-juridique
  transfrontalière                                 puis restructurations
Sinon                                            → continuer
```

## Étape 1 — Ouverture du dossier (socle § 1)

Mémoire dossier, historique, Granola/mails, **Radar** pour l'identité exacte
(dénomination, forme, capital, siège, RCS, dirigeants). Ne jamais reporter dans
un acte une donnée d'identification non vérifiée ; en cas d'écart entre Radar,
les statuts et les dires du client, le signaler et demander.

Recueillir les **statuts en vigueur**, le **pacte** éventuel et le **dernier
PV** : un acte se rédige au regard des stipulations statutaires (convocation,
quorum, majorités, agrément, pouvoirs). S'ils manquent, les demander — ne pas
présumer le régime légal supplétif. Si le dossier du client est connecté à la
session (Cowork, application de bureau, Microsoft 365), y chercher d'abord ces
pièces.

## Étape 2 — Plan et validation

Présenter un plan numéroté : acte(s) à produire, décisions, organe et majorité
de chacune, répercussions identifiées (fiches Étape 4 bis), formalités
consécutives, pièces manquantes. **Attendre la validation de Yoann.**

## Étape 3 — Modèle : hiérarchie des sources

1. **Dépôt** (socle § 4) : rechercher le ou les précédents correspondant au
   type d'acte et à la forme sociale ; lister ceux trouvés, retenir le plus
   proche ; le lire **intégralement** (corps, tableaux, notes, champs
   surlignés) ; vérifier toutes ses références légales à la source, signaler
   tout écart et proposer la clause corrigée ; purger toute donnée d'un autre
   client.
2. **Précédents ECA hors dépôt** : dossier client connecté, conversations
   passées (recherche par type d'acte), fiches mémoire.
3. **Contrôle de niveau** : un précédent incomplet, daté ou en deçà du standard
   du socle § 6 n'est pas recopié : il sert de base, et l'acte est **reconstruit
   au standard M&A** (définitions, interprétation, numérotation, délais
   qualifiés, procédure, annexe « Points de vigilance ECA »). Le dire dans la
   note d'intention.
4. **Aucun modèle pertinent** : construire l'acte à partir des textes en
   vigueur (mentions légales obligatoires d'abord) et du standard du socle § 6.
5. **Étalonnage externe, en dernier recours et pour la structure seulement** :
   actes comparables déposés au RCS et consultables en ligne (data.inpi.fr,
   Pappers), publications et formulaires professionnels de référence auxquels
   Yoann a accès. Règles absolues : n'en reprendre aucune phrase (droit
   d'auteur, données de tiers), aucune donnée nominative, aucune mention dans
   le livrable ; vérifier à la source toute règle qui en serait tirée ; ne
   jamais présenter un acte déposé par un tiers comme une norme.
6. Si une ressource manque : « Ressource absente : [objet] » dans la note, et
   proposer à Yoann d'ajouter au dépôt un modèle **anonymisé** une fois l'acte
   validé.

## Étape 4 — Socle commun : organe, majorité, formalités

### 4.1 Organe et majorité (vérifiés 23/10/2026, à confronter aux statuts)

| Forme | Règle | Texte |
|---|---|---|
| SARL | Changement de nationalité : unanimité. Siège : associés représentant plus de la moitié des parts. Autres modifications : trois quarts des parts (SARL constituées avant la loi du 2 août 2005) ; deux tiers des parts des présents ou représentés, avec quorum du quart puis du cinquième (SARL constituées après, ou ayant opté à l'unanimité), statuts pouvant renforcer sans exiger l'unanimité. Incorporation de bénéfices ou de réserves : moitié des parts. Aucune augmentation des engagements d'un associé sans son accord | C. com. L. 223-30 |
| SAS | Les statuts fixent les décisions collectives et leurs conditions ; certaines matières relèvent obligatoirement de la collectivité des associés (capital, fusion, scission, dissolution, transformation, CAC, comptes et bénéfices). Clauses d'inaliénabilité et d'exclusion : adoption ou modification à l'unanimité ; agrément et cession forcée : décision collective selon les statuts | C. com. L. 227-9 ; L. 227-19 |
| SA | AGE ; le conseil peut transférer le siège sur le territoire français et mettre les statuts en harmonie avec la loi, sous réserve de ratification | C. com. L. 225-36 |
| Sociétés civiles | Unanimité à défaut de clause contraire ; jamais d'augmentation des engagements sans consentement | C. civ. 1836 |
| Associé unique | Décision consignée au registre ; pas de délégation (SAS) | C. com. L. 227-9 (SAS) ; L. 223-31 (EURL, à lire) |

Toujours vérifier en outre : décisions qui augmentent les engagements
(unanimité), droits de vote en cas de **démembrement** (statuts), clauses du
**pacte** (majorités renforcées, droits de veto, information préalable),
**actions de préférence** (assemblées spéciales).

### 4.2 Formalités communes (vérifiées 23/10/2026)

| Formalité | Règle | Texte |
|---|---|---|
| Annonce légale | Avis de modification lorsque la modification rend caduque une mention de l'avis de constitution ; il reproduit l'ancienne mention à côté de la nouvelle | C. com. R. 210-9 (liste des mentions de l'avis de constitution : lire R. 210-4) |
| Dépôt des actes | Actes, délibérations ou décisions modifiant les pièces déposées : dépôt dans le délai d'un mois à compter de leur date, avec un exemplaire des statuts à jour certifié conforme | C. com. R. 123-105 |
| Inscription modificative | Demande par le guichet unique dans le mois de tout fait ou acte la rendant nécessaire | C. com. R. 123-66 |
| Bénéficiaires effectifs | Inscription modificative dans les trente jours suivant tout fait ou acte modifiant les informations déclarées | C. mon. fin. R. 561-55 ; L. 561-46 (version en vigueur jusqu'au 31/12/2028, nouvelle rédaction au 01/01/2029 issue de l'ordonnance n° 2025-1091) |
| Enregistrement | Dans le délai d'un mois : actes constatant la transformation d'une société et ceux constatant une augmentation de capital, sauf augmentation en numéraire ou par incorporation de bénéfices, réserves ou provisions | CGI art. 635, 1, 5° ; droits : CGI art. 809 s. (à lire) |

## Étape 4 bis — Fiches par modification

Chaque fiche liste ce qu'il faut **trancher, rédiger et prévenir**. Aucune
modification n'est rédigée sans que sa fiche ait été parcourue en entier et ses
points reportés dans le plan (Étape 2) ou dans l'annexe « Points de vigilance
ECA ».

### F1 — Dénomination sociale
- **Organe** : modification statutaire (4.1).
- **Avant de décider** : recherche d'antériorités (marques françaises, de
  l'Union et internationales, dénominations, noms commerciaux, noms de
  domaine). Une dénomination antérieure peut faire annuler une marque
  postérieure en cas de risque de confusion, et la nouvelle dénomination peut
  elle-même porter atteinte à une marque antérieure (C. prop. intell.
  L. 711-3, vérifié 23/10/2026). Proposer le dépôt de la marque et du nom de
  domaine.
- **Répercussions** : enseigne et nom commercial, papiers et site, contrats et
  conditions générales (information des cocontractants, sans novation),
  banques, assurances, bail, agréments et autorisations, comptes sociaux.
- **Formalités** : 4.2 (annonce, dépôt, inscription modificative).

### F2 — Siège social
- **Organe** : SARL — le gérant peut décider le déplacement sur le territoire
  français, sous réserve de ratification par les associés ; à défaut, plus de
  la moitié des parts (L. 223-18 et L. 223-30, vérifiés). SA — conseil, sous
  réserve de ratification par l'AGO (L. 225-36, vérifié). SAS — statuts.
  Étranger : unanimité en SARL (changement de nationalité) et analyse fiscale
  obligatoire (CGI art. 221, 2 et 3) → consultation-juridique.
- **Répercussions** : changement de ressort du greffe (une seule formalité par
  le guichet unique, mais deux greffes concernés), service des impôts
  compétent, CFE, contrat de bail ou de domiciliation (le siège doit reposer
  sur un titre d'occupation), transfert ou maintien d'un établissement,
  conventions collectives territoriales éventuelles.
- **Formalités** : 4.2 ; annonce dans le département d'origine et d'arrivée si
  changement de département (à vérifier selon R. 210-9 et la pratique du
  guichet unique).

### F3 — Objet social
- **Organe** : modification statutaire (4.1).
- **Fiscal (vérifié 23/10/2026)** : le changement de l'objet social ou de
  l'activité réelle emporte cessation d'entreprise (CGI art. 221, 5, a). Il y a
  notamment changement d'activité réelle en cas d'adjonction d'une activité
  augmentant de plus de 50 %, au titre de l'exercice de survenance ou du
  suivant, soit le chiffre d'affaires, soit l'effectif moyen et le montant brut
  de l'actif immobilisé ; ou d'abandon ou de transfert faisant baisser ces
  agrégats de plus de 50 % (221, 5, b). Agrément possible (221, 5, c).
  → Rédiger l'objet et la résolution pour tracer une **adjonction** ou une
  **extension**, prévoir le suivi des seuils et, en cas de doute, la demande
  d'agrément. Enjeu : déficits reportables, plus-values latentes.
- **Bail commercial** : adjonction d'activités connexes ou complémentaires par
  notification au bailleur, qui dispose de deux mois pour contester, à peine de
  déchéance (C. com. L. 145-47, vérifié) ; activité étrangère à la
  destination → accord du bailleur.
- **Autres** : activité réglementée (diplôme, carte, agrément), assurances,
  code APE, TVA, convention collective, régime de holding animatrice ou
  engagements Dutreil en cours (vérifier qu'une modification d'objet ne les
  remet pas en cause → strategie-patrimoniale).

### F4 — Date de clôture et durée de l'exercice
- **Organe** : modification statutaire (4.1). Décider **avant la clôture** de
  l'exercice concerné ; ne jamais modifier rétroactivement un exercice déjà
  clos. ⚠️ INCERTAIN — durée maximale d'un exercice prolongé : aucun texte lu
  ne la fixe ; s'en tenir à une prolongation limitée et motivée, et vérifier
  la doctrine avant d'aller au-delà de douze mois supplémentaires.
- **Fiscal (vérifié 23/10/2026)** : si l'exercice clos dans l'année dure plus
  ou moins de douze mois, l'impôt est établi d'après les résultats de cet
  exercice ; si aucun bilan n'est dressé au cours d'une année, une imposition
  est établie sur les bénéfices de la période écoulée (CGI art. 37, applicable
  à l'IS par CGI art. 221, 1). Intégration fiscale : exercices ouverts et clos aux mêmes
  dates, en principe de douze mois (CGI art. 223 A). Lire aussi l'incidence sur
  le plafond du taux réduit d'IS (CGI art. 219, I, b) et le calendrier des
  acomptes.
- **Répercussions** : délai d'approbation, mandat du CAC (exprimé en
  exercices), dividendes et conventions, consolidation, engagements dont la
  durée court par exercice, comptes du dirigeant et calendrier social.
- **Formalités** : dépôt des statuts à jour et inscription modificative (4.2) ;
  annonce légale seulement si la mention figure dans l'avis de constitution
  (R. 210-9, à vérifier).

### F5 — Durée de la société et prorogation
- **Règle (vérifiée 23/10/2026)** : prorogation à l'unanimité ou, si les statuts
  le prévoient, à la majorité requise pour leur modification ; consultation
  des associés **un an au moins avant l'expiration** ; à défaut, désignation
  d'un mandataire de justice ou régularisation judiciaire possible dans
  l'année qui suit l'expiration (C. civ. 1844-6).
- **Action** : inscrire la date d'expiration dans les « Échéances » du dossier
  et la signaler dans `juridique-annuel`.

### F6 — Capital
- **Augmentation en numéraire** : droit préférentiel de souscription et
  renonciation ; libération ; certificat du dépositaire. SA et SAS ayant des
  salariés : l'AGE doit se prononcer sur un projet de résolution
  d'augmentation réservée aux salariés (C. com. L. 225-129-6, vérifié ;
  applicable à la SAS par renvoi de L. 227-1, vérifié), sauf exception du
  second alinéa.
- **Augmentation en nature** : commissaire aux apports, désigné à l'unanimité
  ou par décision de justice (SARL : L. 223-33 renvoyant à L. 223-9 ; SA et
  SAS : L. 225-147 — vérifiés) ; cas de dispense et seuils réglementaires à
  lire ; responsabilité des associés en cas de dispense.
- **Incorporation de réserves** : SARL, moitié des parts (L. 223-30).
- **Réduction non motivée par des pertes** : opposition des créanciers
  antérieurs au dépôt du PV, dans le délai réglementaire ; les opérations ne
  peuvent commencer pendant ce délai ; rachat de parts autorisé pour
  annulation ; égalité des associés (SARL L. 223-34 ; SA et SAS L. 225-205 —
  vérifiés). Rédiger sous **condition suspensive** d'absence d'opposition et
  prévoir l'acte constatant la réalisation.
- **Réduction motivée par des pertes**, coup d'accordéon, capital variable :
  points d'entrée à lire (C. com. L. 223-34, L. 225-204, L. 231-1 s.).
- **Fiscal** : CGI art. 635, 1, 5° (enregistrement) ; rachat de titres et
  réduction : régime de l'associé (plus-value ou revenu distribué) →
  calcul-plus-value.

### F7 — Transformation
- **Principe** : la transformation régulière n'entraîne pas la création d'une
  personne morale nouvelle (C. com. L. 210-6, vérifié).
- **SARL → SAS** : unanimité (L. 227-3). **SARL → SA** : majorité de
  modification des statuts, rapport d'un commissaire aux comptes inscrit sur
  la situation de la société (L. 223-43). **SARL → SNC ou commandite** :
  unanimité (L. 223-43).
- **Société sans CAC → société par actions** : commissaire à la transformation
  désigné à l'unanimité ou, à défaut, en justice ; il apprécie la valeur des
  biens et les avantages particuliers ; les associés statuent sur
  l'évaluation, à peine de nullité (L. 224-3).
- **SAS → autre forme** : règles des SA par renvoi de L. 227-1, **à
  l'exclusion de L. 225-243** (la condition de deux ans d'existence et de deux
  bilans approuvés ne s'applique pas à la SAS). Décision sur le rapport du CAC
  s'il en existe, attestant que les capitaux propres sont au moins égaux au
  capital (L. 225-244) ; transformation en SARL aux conditions de modification
  des statuts des SARL (L. 225-245). **SA → autre forme** : L. 225-243
  s'applique. Tous vérifiés 23/10/2026.
- **Fiscal (vérifié)** : cessation d'entreprise si la transformation crée une
  personne morale nouvelle ou si la société cesse d'être soumise à l'IS
  (CGI art. 221, 2) ; à défaut, neutralité. Enregistrement : CGI art. 635, 1,
  5°.
- **Rédaction** : constater les conditions légales dans le PV, adopter les
  nouveaux statuts, nommer les dirigeants de la nouvelle forme, régler le sort
  de l'exercice en cours, des mandats (CAC), du quitus et des conventions.

### F8 — Dirigeants
- Compétence et majorité selon forme et statuts ; juste motif selon la forme ;
  rémunération et son organe ; holding dirigeante (SAS : personne morale
  possible, représentant ; SARL : personne physique obligatoire, L. 223-18,
  vérifié) ; acceptation, déclaration de non-condamnation, inscription
  modificative (R. 123-66) et bénéficiaires effectifs (R. 561-55) ; clause de
  suppléance ou de succession si utile (précédent du dépôt).

### F9 — Clauses statutaires et gouvernance (SAS)
- Inaliénabilité (dix ans au plus, L. 227-13) et exclusion : unanimité pour
  adopter ou modifier ; agrément et cession forcée : décision collective
  (L. 227-19, vérifié). Cohérence obligatoire avec le pacte → pacte-associes.

### F10 — Mise en harmonie et toilettage
- SARL : le gérant peut mettre les statuts en harmonie avec les dispositions
  impératives, sous réserve de ratification (L. 223-18) ; SA : le conseil, sous
  réserve de ratification par l'AGE (L. 225-36) — vérifiés. Profiter de toute
  modification pour purger les références abrogées et les erreurs matérielles,
  en résolutions distinctes.

### F11 — Associé unique et pluralité d'associés
- Réunion de toutes les parts en une main : pas de dissolution de plein droit
  (C. civ. 1844-5, vérifié) ; adapter la gouvernance (registre, décisions).
- Régime fiscal : une SARL devenue unipersonnelle avec un associé personne
  physique peut relever d'un régime fiscal différent — lire CGI art. 8 et 206,
  3 et sécuriser l'option à l'IS si elle doit être maintenue. Retour à la
  pluralité : nouvelle gouvernance, agrément, pacte.

### F12 — Décisions connexes souvent oubliées
- Nomination ou non-renouvellement du CAC (juridique-annuel), ouverture ou
  fermeture d'établissement secondaire (formalité sans modification
  statutaire), option ou renonciation fiscale (consultation-juridique),
  modification des pouvoirs bancaires, mise à jour du registre des mouvements
  de titres.

## Étape 5 — Tableau de décision clausale

Avant de rédiger, pour tout acte de plus de quelques décisions (statuts, refonte,
PV complexe), produire un tableau : clause / option retenue / justification
(statuts, dossier, demande) / risque si exclue / question au client. Poser les
questions ouvertes **avant** de rédiger.

## Étape 6 — Rédaction

Appliquer intégralement le **standard du socle § 6** (définitions et
interprétation, numérotation, paragraphes en bloc, délais qualifiés, clauses de
procédure et de style, option la plus sécurisante, annexe « Points de vigilance
ECA »). Pour un PV : une résolution par décision, organe et majorité rappelés,
documents communiqués et renonciations aux délais consignés, résultat du vote
par résolution, date d'effet expresse, condition suspensive le cas échéant,
statuts mis à jour annexés, pouvoirs pour formalités. Reprendre le texte du
modèle quand il est juste ; ne le paraphraser que pour l'adapter aux termes
définis du dossier.

## Étape 7 — Contrôle de cohérence

- Renvois internes, numérotation, termes définis tous utilisés et tous définis.
- Cohérence avec les statuts, le pacte, les actes antérieurs du dossier.
- Répercussions de chaque modification sur le reste du document (socle § 6.10)
  et sur les fiches de l'Étape 4 bis.
- Délais : tous qualifiés, point de départ et notification précisés.
- Aucune trace d'un autre client, d'un modèle ou d'un auteur tiers.

## Étape 8 — Livrable et formalités

1. Word ECA selon socle § 8 (titres d'actes en noir gras).
2. Liste des **formalités consécutives** (4.2) avec leurs délais **relus à la
   source** et la partie qui les accomplit.
3. `legal-hallucination-checker` (bloquant), puis `avocat-adverse` si l'acte
   engage des intérêts divergents, puis `positions-eca`.
4. Section « Échéances » si un délai court à compter de l'acte (oppositions,
   dépôts, seuils de l'article 221, 5 du CGI, expiration de la durée sociale).

---

## Comportements à éviter

- Rédiger avant d'avoir les statuts en vigueur ou avant validation du plan.
- Recopier un délai, un seuil ou un taux du modèle sans le vérifier.
- Laisser une mention d'un autre dossier dans un acte issu d'un précédent.
- Mélanger dans un même PV des décisions relevant d'organes ou de majorités
  différentes sans les distinguer.
- Modifier l'objet social sans mesurer l'article 221, 5 du CGI ni la
  destination du bail.
- Prolonger un exercice sans mesurer l'article 37 du CGI et l'intégration
  fiscale.
- Changer de dénomination sans recherche d'antériorité.
