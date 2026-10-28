---
name: "evaluation-titres-fonds"
description: "Évaluation de titres de société non cotée (100 % ou bloc) et/ou de fonds de commerce pour ECA EXPERTISE : choix des méthodes, retraitements, décotes et classeur Excel formulé."
---

# Évaluation de titres non cotés et de fonds de commerce – méthode ECA

**Déclencher sur :**
- évaluation de parts ou d'actions, valeur des titres, valeur d'une société ;
- sortie ou rachat d'un associé, valeur d'un bloc ;
- évaluation d'un fonds de commerce, d'un fonds artisanal ou d'une clientèle, droit au bail ;
- barème de fonds, multiple d'EBE, valeur mathématique, valeur de productivité ;
- décote de minorité ou d'illiquidité.

**NE PAS utiliser pour :**
- le calcul de la plus-value ou de l'impôt du cédant (→ calcul-plus-value) ;
- la rédaction d'un protocole ou d'un acte de cession de titres (→ protocole-cession) ;
- un compromis ou un acte de cession de fonds (→ cession-fonds) ;
- une GAP (→ gap).

**Articulation avec les skills voisins :** ce skill fournit la valeur, les autres traitent l'opération. Il s'enchaîne en amont de `lettre-intention` (prix indicatif), `protocole-cession`, `cession-fonds`, `holding-apport` (valeur d'apport), `strategie-patrimoniale` (valeur de transmission) et `calcul-plus-value` (prix de cession). Quand l'un de ces skills a besoin d'une valeur motivée, il appelle celui-ci plutôt que de la recalculer.

Les références marquées « vérifié 28/10/2026 » ont été lues à la source à cette date ; elles se relisent dans leur version applicable à la date d'évaluation.

## Principes non négociables

1. **Deux phases, validation entre les deux.**
   - Phase 1 : analyse et note de méthodes, SANS calcul.
   - Phase 2 : calculs, uniquement après validation expresse de Yoann.
2. **Lecture intégrale à 100 % du verbatim**, dans cet ordre :
   - les pièces du dossier, y compris les scans ;
   - la documentation d'évaluation du dépôt GitHub ydecreton-a11y/eca-expertise-templates : extraits du Mémento Lefebvre (titres non cotés, fonds de commerce, barèmes par profession), guide DGFiP de l'évaluation et tout document ajouté depuis.
   - Le dépôt est évolutif : le reparcourir à chaque dossier, sans s'en tenir à son contenu connu.
   - Pour un scan illisible : rastérisation et OCR en français, avec vérification visuelle de tout tableau chiffré décisif.
   - Si l'accès est refusé : ne pas contourner, le dire et demander.
3. **Aucune référence de mémoire.**
   - Articles, décisions, taux, seuils, coefficients de barème : lus à la source primaire (Légifrance, LibreJustice, Pourvoi, Legal Data Hunter / BOFiP) ou dans la pièce ou le document du dépôt.
   - Un résumé doctrinal (Mémento, guide) n'est pas une source primaire : relire la décision et signaler tout écart avec le résumé.
4. **Chaque hypothèse de jugement est isolée, sourcée et modifiable** : coefficient de barème, taux, multiple, décote, part de CA perdue.
5. **Pas de double emploi** entre les flux normatifs, la prime de taux et les décotes. Un risque n'est traité qu'à un seul endroit.
6. **Livrable par défaut : le seul classeur Excel**, document de travail interne.
   - Pas de brouillon de mail automatique : un mail n'est rédigé que si Yoann le demande, et reste alors un brouillon jamais envoyé.
   - Pas de document Word ou PowerPoint à en-tête ECA, ni de courrier à la cliente, sans consigne expresse de Yoann.
   - Les livrables client ne mentionnent ni modèle ni auteur tiers.

## Phase 0 – Cadrage et déontologie (préalable bloquant)

- **Identifier qui demande, pour quoi et à quelle date :**
  - cession à un tiers, sortie ou rachat d'un associé, donation / succession, apport, valeur fiscale ;
  - 100 % ou bloc ;
  - paquet majoritaire, minorité de blocage ou minoritaire.
- **Si la demande émane d'un associé alors qu'ECA est l'expert-comptable de la société :** signaler le risque de conflit d'intérêts (code de déontologie, décret n° 2012-432, art. 145, 5° — vérifié 28/10/2026) et le secret professionnel (ordonnance n° 45-2138, art. 21 — vérifié 28/10/2026), en relisant ces deux textes. Proposer, de la plus sûre à la moins sûre :
  - A. Évaluation neutre commandée par la société ou par tous les associés, avec le même rapport pour tous (recommandée).
  - B. Mission personnelle avec lettre de mission distincte (ECA ne pourra plus être expert au sens de l'art. 1843-4).
  - C. Décliner et orienter vers un évaluateur indépendant.
- **Date d'évaluation :** par défaut, les derniers comptes clos. Une situation intermédiaire n'est retenue que si le cabinet l'a arrêtée.

## Phase 1 – Collecte et diagnostic

**Pièces à réunir :**
- comptes clos (N et N-1 au minimum) ;
- statuts et pacte ;
- bail commercial ;
- PV d'AG, rapport de gestion, rapport spécial (conventions réglementées) ;
- demande du client.

**Pennylane :**
- états financiers de l'exercice clos ;
- grand livre des comptes à expliquer (charges à payer, comptes d'attente, salaires) ;
- détail des rémunérations et charges des dirigeants (comptes 641/644, CSG en 637) ;
- contrôle des totaux du bilan.

**Statuts – points à relever systématiquement :**
- clauses d'agrément et de préemption, entre associés et pour les tiers ;
- clause de prix ou de valorisation : si elle existe, l'expert de l'art. 1843-4 doit l'appliquer ;
- exclusion, retrait, non-concurrence ;
- majorités (ordinaire, extraordinaire, révocation du gérant) ;
- comptes courants (durée, blocage) ;
- droits attachés aux parts (égaux ou non).

**Diagnostic de la cible :**
- taille et ancienneté ;
- dépendance aux dirigeants ou praticiens ;
- fonds créé (non inscrit au bilan) ou acquis ;
- bail (bailleur lié ?) ;
- trésorerie et BFR (avances clients, cartes cadeaux) ;
- politique de distribution ;
- rotation des stocks ;
- événements postérieurs à la clôture.

**Livrable de phase 1 :** une réponse dans la conversation, pas un document, comprenant :
- le cadre ;
- les méthodes retenues et exclues, avec leur motif ;
- les retraitements prévus ;
- la pondération ;
- les primes et décotes, en distinguant ce qui est certain, ce qui relève de la doctrine ou de la jurisprudence et ce qui est incertain ;
- les pièces manquantes ;
- le plan numéroté de la phase 2, avec les décisions attendues de Yoann.

## Catalogue des méthodes (choisir et motiver)

### Titres de société

- **Comparaison avec des cessions des mêmes titres :** prioritaire si des transactions récentes ont eu lieu dans des conditions équivalentes.
- **Valeur mathématique / actif net réévalué :**
  - capitaux propres ;
  - plus-value sur le fonds = valeur du fonds − VNC des incorporels, du matériel et des agencements compris dans le barème ;
  - réévaluation de l'immobilier par comparaison ;
  - stock à son coût, décoté si sa rotation est lente ;
  - pas d'impôt latent sur les actifs d'exploitation.
- **Valeur de productivité :** résultat d'exploitation normatif net d'IS capitalisé au coût du capital k = Rf + βa × PRM + prime spécifique (guide DGFiP), g prudent.
- **Multiple d'EBE retraité :**
  - valeur d'entreprise = multiple × EBE normatif ;
  - passage à la valeur des titres par l'endettement financier net retraité (CCA inclus), la trésorerie excédentaire et l'IS dû.
- **Valeur de rendement :** seulement s'il y a une politique de distribution régulière.
- **DCF :** seulement s'il existe un prévisionnel fiable et un historique suffisant.
- **Survaleur (rente du superbénéfice) :** recoupement, sans double emploi avec le fonds.
- **Comparables boursiers, PER, multiples CCEF, MBA :** à exclure pour les TPE et PME (taille sans commune mesure).

### Fonds de commerce, fonds artisanal, clientèle

- **Comparaison** avec des cessions de fonds intrinsèquement similaires : prioritaire. Source possible : prix publiés au BODACC.
- **Barème professionnel** en % du CA HT :
  - CA moyen des trois derniers exercices, en écartant les années non significatives ;
  - matériel compris, stock exclu ;
  - positionnement motivé dans la fourchette : population de la commune, emplacement, ancienneté, montant du CA (taux inversement proportionnels au CA), dépendance à l'exploitant ;
  - coefficient lu dans le barème du dépôt ou du dossier, jamais de mémoire.
- **EBE − économie de loyer, × coefficient (indépendants / enseignes), + valeur du droit au bail.**
- **Droit au bail :** plancher de la valeur du fonds ; méthode du différentiel de loyer × coefficient de situation, ou comparaison.
- **Stock :** évalué séparément, avec décote si la rotation est lente.

## Retraitements normatifs (phase 2)

- **Éléments non récurrents :** cartes cadeaux périmées, régularisations, produits ou charges exceptionnels.
- **Rémunération des dirigeants :**
  - garder la rémunération normale ;
  - réintégrer l'excédent si elle est excessive ;
  - déduire l'insuffisance si elle est trop faible.
- **Départ d'un associé exploitant :** raisonner en scénarios.
  - S1 – Remplacement au coût actuel de l'associé (statu quo).
  - S2 – Non-remplacement : perte de la part de CA attachée, moins les charges variables économisées, plus le coût de l'associé économisé.
  - Calculer les deux seuils de perte de CA : EBE S2 = EBE S1, puis EBE S2 = 0.
- **Loyer normatif** si le bailleur est lié ; sinon, présomption de loyer de marché, à signaler.
- **IS normatif :** relire l'art. 219 du CGI en vigueur (taux réduit PME, plafond, conditions).

## Pondération, primes et décotes

**Pondération :**
- Présenter une valeur centrale et ses variantes, en citant la source de chaque formule lue dans le dépôt (Mémento, guide DGFiP) : petit commerce ou petite société de services, pouvoir de décision ou non, minorité de blocage.
- En cas de divergence entre la doctrine et le guide DGFiP, l'exposer et trancher de façon motivée.

**Décotes – illiquidité :** jamais écartée par principe.
- **Certain :** elle n'est pas justifiée lorsque les titres bénéficient d'un engagement de rachat garantissant une liquidité permanente à une valeur fixée à dire d'expert (CE 3/07/2009 n° 301299 — vérifié 28/10/2026 ; le juge doit « rechercher si cet engagement leur garantissait une liquidité permanente »).
- **Position à motiver :** la procédure légale de la SARL (C. com. art. L. 223-14 — vérifié 28/10/2026 ; prix fixé selon C. civ. art. 1843-4 — vérifié 28/10/2026) n'offre qu'une sortie conditionnelle : un cessionnaire tiers doit être présenté et refusé, les parts détenues depuis au moins deux ans, et rien ne joue pour une cession libre entre associés. L'assimiler à l'engagement de rachat de l'arrêt de 2009 relève de l'analogie, pas de la jurisprudence.
- **En pratique :** relire la clause statutaire, retenir une décote nulle ou faible si la sortie est réellement assurée (clause de rachat, retrait statutaire, engagement des associés), et faire figurer une sensibilité avec décote dans le classeur.

**Décotes – minorité :** à étayer ; une décote non étayée est écartée (CE 3/07/2009 n° 301299 — vérifié 28/10/2026). Le caractère minoritaire peut passer par la pondération en faveur de la valeur patrimoniale (CAA Bordeaux 22/11/2016 n° 14BX03020 — vérifié 28/10/2026).

**Décotes – agrément :** seulement si la clause affecte réellement la cessibilité.
- Cass. com. 1/04/1997 n° 95-12.723 (vérifié 28/10/2026) : l'influence de la clause sur la valeur s'apprécie au regard de ses avantages et de ses inconvénients (10 % retenus en l'espèce, appréciation des juges du fond).
- CAA Bordeaux 22/11/2016 n° 14BX03020 (vérifié 28/10/2026) : pas d'abattement supplémentaire lorsque la clause n'affecte pas la cessibilité des titres.

**Décotes – personne clé :** soit dans les flux, soit dans la prime spécifique, soit en décote, jamais cumulées. Précédent : CAA Bordeaux 22/11/2016 n° 14BX03020 (vérifié 28/10/2026), décote générale portée de 30 à 40 % pour la dépendance à un homme-clé.

**Comptes courants d'associés :** toujours présentés à part, dus en sus du prix des titres.

## Livrable Excel (skill xlsx) – seul livrable par défaut

Fichier nommé `<CLIENT>_Evaluation_<objet>_<date>_TRAVAIL_INTERNE.xlsx`. Onglets :

1. **Synthèse** : valeur de 100 %, valeur unitaire, blocs par associé, comptes courants pour mémoire, contrôles de cohérence (valeur / EBE, valeur / CA, écart entre valeur mathématique et valeur de rentabilité).
2. **Données** : compte de résultat et bilan issus de Pennylane, avec des contrôles de totaux égaux aux comptes approuvés et la source de chaque ligne.
3. **Hypothèses** : cellules jaunes et texte bleu, avec justification et source sur chaque ligne.
4. **EBE_normatif** : un tableau des retraitements par scénario et les seuils.
5. **Valeur_mathématique** (et/ou **Fonds**).
6. **Rentabilité** : coût du capital, éléments de passage, productivité, multiple d'EBE.
7. **Sensibilités** : coefficient de barème, pondérations, scénario de perte de CA, taux.
8. **Méthodes_Références** : méthodes retenues et exclues, références avec leur statut de vérification.

**Règles de construction :**
- Formules uniquement ; aucune valeur calculée en dur.
- Planchers de valeur à 0, motivés.
- Recalcul avec `recalc.py` jusqu'à zéro erreur.
- Rendu visuel contrôlé.
- Copier le fichier dans le dossier client sur le poste s'il est relié.

## Livrables optionnels – uniquement sur consigne expresse de Yoann

- **Mail :** brouillon Outlook, jamais envoyé. HTML limité aux balises autorisées (tableau sans attributs). Rappeler qu'il faut joindre le fichier Excel à la main.
- **Rapport ou courrier Word, ou présentation PowerPoint à en-tête ECA :** sur demande explicite seulement, en suivant la méthode Word ECA et les modèles du dépôt.

## Contrôle final

- Recalcul et rapprochement de chaque chiffre résumé dans la réponse avec le classeur.
- 100 % des références relues, avec leur statut affiché : primaire, doctrine du dépôt, ou secondaire (taux de marché, prime de risque, population).
- Liste explicite des pièces non vues (bail, inventaire, répartition du CA…).
- Réponse finale courte, avec une section « Sources ».