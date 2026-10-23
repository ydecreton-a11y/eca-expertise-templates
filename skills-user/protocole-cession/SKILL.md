---
name: protocole-cession
description: "Skill ECA EXPERTISE pour tout protocole de cession de titres sociaux (parts sociales ou actions) : négociation, analyse d'un projet reçu, rédaction du protocole sous conditions suspensives ou de la promesse (synallagmatique ou unilatérale), prix et ajustement, earn-out, crédit-vendeur, gestion intercalaire, non-concurrence, ainsi que la cession simple signée en un temps. TOUJOURS pour un camp. Déclencher sur : protocole de cession, SPA, promesse de cession, cession de parts sociales, cession d'actions, cession de titres, condition suspensive, ajustement de prix, complément de prix, earn-out, crédit-vendeur, séquestre du prix, gestion intercalaire. NE PAS utiliser pour la lettre d'intention ou la term sheet (→ lettre-intention), l'acte définitif ou le closing après levée des conditions (→ acte-definitif-titres), la GAP (→ gap), un audit de cible (→ due-diligence-juridique), un chiffrage de plus-value (→ calcul-plus-value), un pacte (→ pacte-associes) ou un fonds de commerce (→ cession-fonds)."
---

# Skill : Protocole de cession de titres — ECA EXPERTISE

> **Socle** : charger `socle-eca` — ouverture du dossier (§ 1), carte des
> connecteurs (§ 2), règles de vérification (§ 3), accès aux modèles (§ 4),
> pièges datés (§ 5), standard de rédaction (§ 6), garde-fous (§ 7), Word ECA
> (§ 8), fin de livrable (§ 9). Un output Casus collé est une base documentaire
> à recouper (§ 3.4). Aucun taux, seuil ou délai n'est repris de mémoire.

> Le protocole fixe le prix, le calendrier et les conditions du transfert. La GAP
> fixe le risque. Les deux se lisent ensemble mais se négocient séparément, et
> une incohérence entre eux est la première cause de contentieux post-closing.

> **Chaîne documentaire** : `lettre-intention` (LOI, term sheet) →
> **ce skill** (protocole sous conditions suspensives) → `gap` →
> `acte-definitif-titres` (réitération et closing après levée des conditions).

---

## 🚪 PHASE 0-P — PORTE DE POSTURE (BLOQUANTE)

⚠️ **Aucune analyse, aucune clause, aucune recommandation avant clôture de cette phase.**

### Étape 1 — Déduire le camp

| Indice | Camp |
|---|---|
| ECA a rédigé la LOI pour le repreneur | **ACQUÉREUR** |
| ECA conduit la due diligence | **ACQUÉREUR** |
| Le client est l'associé sortant / le dirigeant qui se retire | **CÉDANT** |
| ECA prépare l'info memo ou le dossier de présentation de la cible | **CÉDANT** |
| ECA est l'expert-comptable de la cible, le cédant est le client | **CÉDANT** — alerte conflit |
| Projet reçu d'un confrère adverse | Camp = celui du client d'ECA, à confirmer |

### Étape 2 — Si indéterminable : s'arrêter et demander

> « Avant toute production : ECA défend le cédant ou l'acquéreur sur ce dossier ?
> L'ensemble des clauses en dépend. »

### Étape 3 — Verrouiller et annoncer

> **Posture : PRO [CÉDANT / ACQUÉREUR].**
> Toutes les positions défendent [X]. Les positions adverses ne sont exposées
> que pour anticiper les objections.

### Étape 4 — Règles verrouillées

- **Interdit** : rédaction présentée comme « équilibrée »
- **Interdit** : « les parties pourraient convenir que… »
- **Obligatoire** : chaque curseur part au maximum défendable ; le repli est une
  décision de négociation, pas un point de départ

### Étape 5 — Limites déontologiques

- Ne pas proposer une clause manifestement nulle en la présentant comme valable ;
  si une position est agressive mais fragile, le dire
- Ne pas organiser la dissimulation d'un fait connu (Art. 1137 C. civ.) : la
  réticence dolosive ouvre la nullité de la cession, c'est un mauvais conseil
  même pour un cédant
- Ne jamais recommander l'omission d'une formalité d'ordre public (information
  des salariés, agrément, consentement du conjoint) : le gain de temps est
  toujours inférieur au risque
- Signaler tout conflit d'intérêts si ECA intervient pour la cible

### Étape 6 — Changement de posture : instruction explicite de Yoann uniquement

---

## PHASE 0-S — Cession simple (sans négociation M&A)

Cession de parts ou d'actions entre parties d'accord, signée **en un seul
temps** sans protocole préalable (entrée ou sortie d'associé, reclassement
familial ou intragroupe, cession à la holding) : la porte de posture
s'applique (qui conseille-t-on ?), mais la table des curseurs est allégée.
Si un protocole sous conditions a été signé auparavant, l'acte de cession
relève de `acte-definitif-titres`. Produire :
1. décision d'agrément ou de renonciation à la préemption (statuts et pacte) ;
2. acte de cession au standard du socle § 6 (définitions, déclarations du
   cédant par rubrique, prix et paiement, transfert de propriété, garantie
   proportionnée — renvoi `gap` si garantie négociée) ;
3. ordre de mouvement de titres (actions) ou formalités d'opposabilité (parts) ;
4. déclaration fiscale de cession et courrier au service de l'enregistrement
   (formulaire et droits lus à la source) ;
5. mise à jour des statuts (SARL, sociétés civiles) et des bénéficiaires effectifs ;
6. avenant ou adhésion au pacte (→ `pacte-associes`, mode avenant).
Contrôles : formalités d'ordre public (§ 2.3), consentement du conjoint,
information des salariés, cohérence du prix avec la valorisation et les
comptes courants.

## PHASE 0-M — Mode de travail

```
LOI / term sheet à rédiger ou analyser → lettre-intention (hors de ce skill)
Projet reçu de la partie adverse       → MODE ANALYSE      (§ 5.1)
Aucun texte, protocole à produire      → MODE RÉDACTION    (§ 5.2)
Aller-retour, arbitrages à rendre      → MODE NÉGOCIATION  (§ 5.3)
Protocole signé, closing à organiser   → acte-definitif-titres (§ 5.4)
```

---

## PHASE 2 — Qualification préalable

### 2.1 Nature de l'engagement

| Instrument | Effet | Vigilance |
|---|---|---|
| LOI / term sheet | Engageant sur ce qu'il formule fermement | Traitée par `lettre-intention` ; vérifier ici sa cohérence avec le protocole (Phase 6) |
| Promesse unilatérale de vente | Engage le seul promettant ; le bénéficiaire dispose d'une option | Indemnité d'immobilisation, durée de l'option |
| Promesse synallagmatique | Vente parfaite dès l'accord sur la chose et le prix (Art. 1583 C. civ.), sous conditions suspensives | C'est le cas usuel du « protocole » |
| Cession définitive | Transfert immédiat | Cession simple (Phase 0-S) ou réitération (`acte-definitif-titres`) |

**Conséquence majeure** : le protocole synallagmatique **est la vente**. Le
closing n'est que son exécution. Une partie qui refuse de closer sans motif tiré
d'une condition non réalisée s'expose à l'exécution forcée, pas seulement à des
dommages-intérêts.

- *Pro cédant* — cette force est un atout une fois le protocole signé : sécuriser
  la signature rapidement, limiter les portes de sortie de l'acquéreur.
- *Pro acquéreur* — l'inverse : ne signer qu'une fois la DD achevée, ou assortir
  la signature de conditions suspensives réellement libératoires.

**Préparer la réitération dès le protocole** : prévoir si un acte réitératif
sera exigé, la date et le lieu de réalisation, la liste des remises, la clause
de survie et la règle de primauté entre protocole et acte définitif. Ce que le
protocole ne prévoit pas devra être négocié au closing, au pire moment.

### 2.2 Forme sociale et régime du transfert

| Forme | Agrément | Formalisme du transfert | Enregistrement |
|---|---|---|---|
| SARL | Art. L. 223-14 C. com. — agrément légal pour les cessions à tiers | Écrit ; opposabilité à la société par signification (C. civ. 1690) ou dépôt d'un original au siège contre attestation du gérant ; opposabilité aux tiers après ces formalités et publication des statuts modifiés au RCS (Art. L. 223-17 renvoyant à L. 221-14 C. com. — vérifié 23/10/2026) | CGI Art. 726 — taux et abattement à lire à la source en vigueur |
| SAS | Art. L. 227-14 C. com. — agrément **statutaire** seulement | Ordre de mouvement, inscription au registre des mouvements et aux comptes d'actionnaires | CGI Art. 726 |
| SA non cotée | Art. L. 228-23 C. com. — clause statutaire | Ordre de mouvement, registre | CGI Art. 726 |
| Société à prépondérance immobilière | — | Selon la forme | CGI Art. 726 I 2° — taux majoré |

⚠️ **Ne jamais présumer les statuts.** Une SAS peut avoir un agrément, un droit
de préemption, une clause d'inaliénabilité, une clause de sortie conjointe. Les
statuts et le pacte existant doivent être lus **avant** la rédaction du protocole,
et leur respect érigé en condition suspensive ou en déclaration.

### 2.3 Formalités préalables d'ordre public — carte de vigilance

| Formalité | Fondement | Déclencheur | Sanction |
|---|---|---|---|
| Information des salariés | **C. com. Art. L. 23-10-1** | Sociétés sans obligation de CSE à attributions élargies ; vente de plus de 50 % des parts de SARL ou de titres donnant accès à la majorité du capital d'une société par actions | Amende civile ≤ **0,5 %** du montant de la vente, sur action en responsabilité et à la demande du ministère public |
| Information-consultation du CSE | C. com. Art. L. 23-10-7 ; C. trav. Art. L. 2312-8 | Sociétés dotées d'un CSE à attributions élargies | Délit d'entrave, suspension |
| Consentement du conjoint | **C. civ. Art. 1424** | Parts sociales (droits sociaux **non négociables**) dépendant d'une communauté | Nullité relative (Art. 1427 C. civ.) |
| Agrément | Statuts / L. 223-14, L. 227-14, L. 228-23 C. com. | Selon forme et statuts | Nullité de la cession |
| Droit de préemption | Statuts ou pacte | Clause | Inopposabilité, dommages-intérêts |
| Contrôle des concentrations | C. com. Art. L. 430-1 s. | Franchissement des seuils — **seuils à lire à la source en vigueur** | Nullité de l'opération, amende |
| Contrôle des investissements étrangers | CMF Art. L. 151-3 | Investisseur étranger, secteur sensible | Nullité, injonctions |

### ⚠️ ALERTE — Information des salariés : dispositif modifié en 2026

**Vérifié via LibreJustice le 23/10/2026** (versions en vigueur depuis le
28/05/2026). Les articles L. 23-10-1 et L. 23-10-7 C. com. ont été réécrits
par la **loi n° 2026-403 du 26 mai 2026** (art. 22) ; ils s'appliquent aux
**ventes conclues deux mois au moins après la promulgation**. Deux
changements que les modèles antérieurs ne reflètent pas :

1. **Le champ n'est plus indexé sur le seuil de 50 salariés** mais sur l'absence
   d'obligation de mettre en place un CSE exerçant les attributions du deuxième
   alinéa de l'article L. 2312-1 C. trav. Information au plus tard **un mois
   avant la vente** ; vente possible avant si chaque salarié a fait connaître
   sa décision de ne pas présenter d'offre.
2. **L'amende civile est ramenée à 0,5 %** du montant de la vente, et son
   prononcé suppose qu'une action en responsabilité soit engagée, à la
   demande du ministère public.

⚠️ **Discordance confirmée sur L. 23-10-7** — le corps de l'article, placé
dans le chapitre relatif aux titres, reproduit mot pour mot celui de
L. 141-28 et vise « tout projet de vente d'un **fonds de commerce** », tout
en renvoyant aux articles L. 23-10-1 à L. 23-10-6 (titres) en l'absence de
CSE. Les intitulés de sections mentionnent encore les seuils de 50 et 249
salariés. Erreur de coordination probable, non corrigée à cette date.
**Conduite à tenir** : traiter par excès de prudence — dans une société
dotée d'un CSE à attributions élargies, informer-consulter le CSE sur le
projet de cession de titres ; à défaut de CSE constaté, appliquer
L. 23-10-1 à L. 23-10-6. Le coût d'une formalité inutile est nul ; celui
d'une omission ne l'est pas. Revérifier le texte à la date de la vente.

**Point de départ — « avant la vente »** : le protocole synallagmatique
pouvant constituer la vente (§ 2.1), **notifier les salariés au moins un
mois avant la signature du protocole**, et non avant le closing.
⚠️ INCERTAIN — la date de « la vente » en présence de conditions
suspensives n'est pas tranchée par le texte : retenir la date la plus
précoce.

**Conséquence de posture** :
- *Pro acquéreur* — exiger les justificatifs de notification (et leur date)
  avant signature, et une déclaration du cédant sur leur accomplissement.
- *Pro cédant* — la formalité pèse sur le cédant ; l'accomplir tôt, car le délai
  d'un mois retarde mécaniquement le calendrier.

**Point de vigilance conjoint (Art. 1424 C. civ., vérifié 23/10/2026)** — le
texte impose la cogestion non seulement pour l'aliénation des droits sociaux non
négociables communs (parts sociales), mais aussi pour la **perception des
capitaux** qui en proviennent. Le conjoint doit donc intervenir à l'acte à double
titre. Omission fréquente dans les protocoles : le conjoint peut demander
l'annulation pendant deux années à partir du jour où il a eu connaissance de
l'acte, sans pouvoir agir plus de deux ans après la dissolution de la communauté
(Art. 1427 C. civ., vérifié 23/10/2026).

---

## PHASE 3 — LA TABLE DES CURSEURS

> La colonne « atterrissage fréquent » est **indicative** et tirée de la pratique
> des cessions de PME. Aucune valeur normative ; à recalibrer selon le rapport de
> force et la qualité des comptes. Ne jamais la présenter à un client comme un
> standard opposable.

### 3.1 Prix et ajustement

| # | Paramètre | Curseur CÉDANT | Curseur ACQUÉREUR | Atterrissage fréquent |
|---|---|---|---|---|
| 1 | Mécanique | **Locked box** — prix figé sur comptes de référence audités | **Closing accounts** — ajustement sur situation à la date de closing | Selon la qualité des comptes |
| 2 | Ajustement | Plafonné, à la hausse comme à la baisse | Non plafonné à la baisse | Symétrique et plafonné |
| 3 | Dette nette | Définition étroite | Définition large (provisions, engagements de retraite, comptes courants, dividendes votés) | Définition négociée poste par poste |
| 4 | BFR normatif | Référence favorable (moyenne haute) | Référence prudente | Moyenne sur 12 à 24 mois |
| 5 | Expert en cas de désaccord | Expert-comptable désigné d'accord | Expert indépendant, décision définitive | Tiers estimateur, Art. 1592 C. civ. |
| 6 | Paiement | Intégral au closing | Fractionné, séquestre, crédit-vendeur | Séquestre partiel adossé à la GAP |

**Locked box contre closing accounts — la vraie question.** En locked box, le
risque économique passe à l'acquéreur dès la date des comptes de référence, avant
même le transfert de propriété ; en contrepartie, le cédant s'interdit toute
« fuite » (dividendes, rémunérations exceptionnelles, avantages). En closing
accounts, le cédant conserve les fruits jusqu'au closing mais supporte l'aléa de
l'ajustement.

- *Pro cédant* — la locked box donne un prix certain et supprime le contentieux
  d'ajustement, qui est presque toujours défavorable au vendeur puisque
  l'acquéreur en établit les comptes. Position à privilégier quand les comptes
  sont fiables et le délai jusqu'au closing court.
- *Pro acquéreur* — les closing accounts, sauf si l'audit a été poussé et le
  délai très court. Et dans tous les cas : **c'est l'acquéreur qui doit établir
  la situation d'ajustement**, le cédant disposant d'un droit de contestation.
  Qui tient le stylo tient l'ajustement.

**Tiers estimateur (Art. 1592 C. civ.)** — sa décision s'impose aux parties.
Rédiger sa mission avec le même soin que le prix lui-même : périmètre exact,
méthode comptable imposée, délai, sort des frais, et surtout référentiel
comptable applicable. Une mission floue transfère le pouvoir de fixation du prix
à un tiers sans instruction.

### 3.2 Complément de prix et crédit-vendeur

| # | Paramètre | Curseur CÉDANT | Curseur ACQUÉREUR | Atterrissage fréquent |
|---|---|---|---|---|
| 7 | Earn-out — indicateur | EBITDA ou marge, peu manipulable | Résultat net, après charges du repreneur | EBITDA retraité, définition contractuelle fermée |
| 8 | Earn-out — protection | Engagements de gestion du repreneur, interdiction de refacturations intragroupe, audit contradictoire | Liberté totale de gestion | Engagements de gestion limités et listés |
| 9 | Crédit-vendeur | Refusé, ou garanti par nantissement des titres cédés | Large, adossé à la GAP par compensation | Fraction du prix, avec sûreté |
| 10 | Séquestre | Court, dégressif, rémunéré au profit du cédant | Long, aligné sur la durée de la GAP | Adossé à la durée de la GAP |

**Earn-out — le piège structurel.** Le cédant accepte un prix dont la réalisation
dépend d'une entreprise qu'il ne dirige plus. Sans encadrement, l'acquéreur peut
légitimement prendre des décisions de gestion qui compriment l'indicateur.

*Pro cédant* — verrouiller par : indicateur peu manipulable (EBITDA plutôt que
résultat net), définition contractuelle fermée de son mode de calcul avec exemple
chiffré annexé, interdiction des refacturations de frais de groupe et des
management fees, engagement de continuité des méthodes comptables, information
trimestrielle, audit contradictoire, et clause de déchéance du terme rendant
l'earn-out immédiatement exigible en cas de revente, de fusion ou de
restructuration de la cible pendant la période.

*Pro acquéreur* — résister à toute clause limitant la liberté de gestion,
préférer un earn-out à seuil unique (tout ou rien) qui simplifie le contentieux,
et exiger la compensation avec les appels en garantie.

**Point d'articulation à ne jamais manquer** : si l'earn-out sert aussi de
garantie de la garantie par compensation, l'acquéreur devient juge et partie.
Traiter explicitement, en renvoyant à la clause correspondante de la GAP.

### 3.3 Conditions suspensives

| # | Paramètre | Curseur CÉDANT | Curseur ACQUÉREUR | Atterrissage fréquent |
|---|---|---|---|---|
| 11 | Liste | Minimale : agréments et autorisations légales | Étendue : financement, DD confirmatoire, contrats clés, absence de MAC | Autorisations + financement |
| 12 | Condition de financement | Refusée, ou assortie d'une lettre d'engagement bancaire ferme préalable | Large, avec obligation de moyens seulement | Financement avec obligation de diligence et délai ferme |
| 13 | Délai de réalisation | Court, avec caducité automatique | Long, prorogeable | Ordre de 60 à 120 jours calendaires (à motiver par le calendrier des conditions) |
| 14 | Renonciation | Réciproque | Au seul bénéfice de l'acquéreur | Au bénéfice de la partie protégée |
| 15 | Défaillance | Caducité sans indemnité | Caducité + restitution de l'indemnité d'immobilisation | Caducité, sort des frais réglé |

⚠️ **Art. 1304-2 C. civ.** — la condition dont la réalisation dépend de la seule
volonté du débiteur est nulle. Une condition suspensive de financement rédigée
sans aucune obligation de diligence frôle la condition potestative.
⚠️ **Art. 1304-3 C. civ.** — la condition est réputée accomplie si celui qui y
avait intérêt en a empêché l'accomplissement.

- *Pro cédant* — exploiter l'article 1304-3 : assortir la condition de financement
  d'obligations précises et vérifiables (dépôt de dossiers auprès d'au moins
  [N] établissements sous [X] Jours Ouvrés, communication des refus écrits). Un acquéreur
  qui ne les respecte pas voit la condition réputée accomplie.
- *Pro acquéreur* — accepter une obligation de diligence, jamais une obligation
  de résultat, et refuser toute clause faisant du refus bancaire une faute.

**Forme de la levée et de la renonciation** — prévoir dès le protocole comment
chaque condition est constatée (pièce, notification) et comment son
bénéficiaire y renonce (écrit, délai). C'est ce tableau que
`acte-definitif-titres` reprendra au closing.

### 3.4 Gestion intercalaire et MAC

| # | Paramètre | Curseur CÉDANT | Curseur ACQUÉREUR | Atterrissage fréquent |
|---|---|---|---|---|
| 16 | Engagements de gestion | Gestion en bon père de famille, formulation générale | Liste fermée d'actes interdits sans accord écrit | Liste d'actes soumis à accord, avec seuils |
| 17 | Clause MAC | Refusée | Large, appréciation par l'acquéreur | Étroite, objectivée, chiffrée |
| 18 | Distributions | Libres jusqu'au closing | Interdites | Interdites, sauf dividende prévu au protocole |

**Clause MAC (*material adverse change*)** — en droit français, elle est
d'efficacité incertaine et doit être **objectivée** pour être utile : critère
chiffré (perte d'un client représentant plus de X % du chiffre d'affaires,
baisse d'EBITDA supérieure à Y %), exclusion expresse des événements
macroéconomiques et sectoriels, et délai bref d'invocation.

Une MAC subjective (« tout événement de nature à affecter défavorablement… »)
est une clause de confort qui, en pratique, ne permet pas de sortir sans risque
d'exécution forcée. *Pro acquéreur* : ne jamais s'y fier comme unique porte de
sortie. *Pro cédant* : c'est précisément pour cela qu'on peut parfois l'accorder.

⚠️ La gestion intercalaire ne doit pas transférer la direction effective à
l'acquéreur avant le closing — risque au regard du contrôle des concentrations
(*gun jumping*) et du droit de la responsabilité. Border la liste d'actes soumis
à accord préalable, sans instruction de gestion positive.

### 3.5 Closing et engagements post-closing

| # | Paramètre | Curseur CÉDANT | Curseur ACQUÉREUR | Atterrissage fréquent |
|---|---|---|---|---|
| 19 | Non-concurrence | Courte, zone étroite, activité définie strictement | Longue, large, sans contrepartie séparée | 2 à 3 ans, périmètre d'activité réelle |
| 20 | Non-sollicitation | Limitée aux cadres clés | Tout salarié et tout client | Cadres clés et clients actifs |
| 21 | Accompagnement | Bref, rémunéré, obligation de moyens | Long, inclus dans le prix | 3 à 12 mois, contrat distinct |
| 22 | Mainlevée des cautions personnelles | Condition du closing, à défaut contre-garantie de l'acquéreur | Obligation de moyens | Contre-garantie si mainlevée bancaire non obtenue |
| 23 | Comptes courants | Remboursement intégral au closing | Cession au prix nominal ou subordination | Remboursement ou cession, tranché expressément |

**Ligne 22 — l'oubli le plus coûteux pour un cédant.** Le dirigeant cédant reste
personnellement engagé au titre des cautions consenties aux banques de la cible
tant que l'établissement n'a pas donné mainlevée. L'acquéreur ne peut pas la
délivrer : elle dépend d'un tiers. Rédaction pro cédant impérative : mainlevée
érigée en condition suspensive lorsque c'est possible, et à défaut, engagement
de contre-garantie personnelle de l'acquéreur assorti d'une obligation de
substitution sous délai, avec pénalité.

**Ligne 23 — les comptes courants ne sont pas dans le prix des titres.** Confusion
fréquente et lourde : la cession des titres ne transfère pas la créance de compte
courant. Trois traitements possibles, à trancher expressément : remboursement par
la société au closing (vérifier la trésorerie disponible), cession de la créance
à l'acquéreur (prix distinct, formalisme de la cession de créance), ou maintien
avec convention de blocage. Ne jamais laisser cette question implicite.

**Ligne 19 — non-concurrence.** Validité subordonnée à une limitation dans le
temps, dans l'espace et quant à l'activité, et à la proportionnalité aux intérêts
légitimes à protéger. En cession de titres, la contrepartie financière est
regardée comme incluse dans le prix — mais une clause manifestement excessive
reste réductible par le juge.
⚠️ Si une indemnité de non-concurrence distincte est prévue, son traitement
fiscal diffère de celui du prix de cession : à vérifier avant de la stipuler
séparément, car elle peut être plus lourdement imposée qu'un prix de cession
bénéficiant d'abattements.

---

## PHASE 4 — Dimension fiscale du protocole

Traiter systématiquement, jamais en annexe.

### 4.1 Droits d'enregistrement

CGI Art. 726 — taux différenciés selon la forme sociale et le caractère de
prépondérance immobilière. **Lire à la source les taux et l'abattement en
vigueur à la date de la cession.** Trancher expressément dans le protocole qui les supporte : la loi les
met à la charge de l'acquéreur, mais la clause peut en disposer autrement, et le
silence est une source de discussion au closing.

⚠️ Vérifier la prépondérance immobilière avant de conclure sur le taux : une
société d'exploitation propriétaire de ses murs peut y basculer et le
différentiel de taux est significatif.

⚠️ **Protocole sous conditions et enregistrement (vérifié 23/10/2026)** — les
actes portant cession d'actions ou de parts sociales s'enregistrent dans le
délai d'un mois à compter de leur date (CGI art. 635, 2, 7°) ; pour une mutation
affectée d'une condition suspensive, le régime fiscal et les valeurs imposables
s'apprécient à la date de réalisation de la condition (CGI art. 676). Prévoir
dès le protocole l'articulation de son enregistrement avec celui de l'acte
définitif (aucun double paiement, aucun défaut d'enregistrement) et la
partie qui accomplit la formalité.

### 4.2 Fiscalité du cédant

| Point | Règle | Vigilance |
|---|---|---|
| Fait générateur | Date de la cession, c'est-à-dire du transfert de propriété. Sous condition suspensive : la doctrine retient la date de réalisation de la condition pour les plus-values immobilières (BOI-RFPI-PVI-20, § 30, repéré le 23/10/2026) ; pour les titres, lire la doctrine BOI-RPPM-PVBMI avant de l'affirmer | ⚠️ **La fraction séquestrée du prix est imposable dès la cession**, même si elle n'est perçue que plus tard. Piège de trésorerie majeur — l'anticiper avec le client ; l'année d'imposition dépend de la date de levée de la dernière condition |
| Complément de prix (earn-out) | CGI Art. 150-0 A, I, 2 (vérifié 23/10/2026) — imposable au titre de l'année de perception ; le prix d'acquisition retenu par le cessionnaire en est augmenté (150-0 D, 2) | L'application au complément de l'abattement éventuellement applicable au prix principal (CGI Art. 150-0 D, 1) se vérifie à la source avant de l'affirmer au client ; report possible du complément réinvesti : lire CGI Art. 150-0 B bis |
| Crédit-vendeur | **CGI Art. 1681 F, I bis** — plan de règlement échelonné de l'IR sur demande | Conditions cumulatives strictes (voir ci-dessous) |
| Régimes de faveur | 150-0 D ter, 150-0 B ter, exonérations professionnelles | Vérifier l'antériorité des conditions **avant** de figer le calendrier |

**Crédit-vendeur — CGI Art. 1681 F, I bis (vérifié 23/10/2026).** Le plan de
règlement échelonné de l'impôt sur le revenu suppose un paiement différé ou
échelonné de tout ou partie du prix, et la réunion de conditions cumulatives
dont deux sont souvent découvertes trop tard :

- la cession doit porter sur **la majorité du capital social** ;
- à l'issue de la cession, la société ne doit **pas être contrôlée par le cédant**
  au sens du 2° du III de l'Art. 150-0 B ter CGI ;
- la société emploie moins de cinquante salariés, a un total de bilan ou un
  chiffre d'affaires n'excédant pas dix millions d'euros au titre de l'exercice
  de la cession, et répond à la définition de petite entreprise du règlement
  (UE) n° 651/2014 ;
- l'imposition ne résulte ni d'une rectification ni d'une procédure
  d'imposition d'office ;
- le redevable respecte ses obligations fiscales courantes et **constitue des
  garanties** auprès du comptable public (complément exigible en cas
  d'insuffisance) ;
- la demande doit être formulée **au plus tard à la date limite de paiement portée
  sur l'avis d'imposition** — une échéance qu'il faut inscrire au calendrier du
  dossier dès la signature du protocole ;
- la durée du plan ne peut excéder celle du paiement du prix ni se prolonger
  au-delà du 31 décembre de la cinquième année qui suit celle de la cession ;
  les échéances d'impôt suivent les modalités de paiement du prix prévues à
  l'acte.

**Conséquence de posture** : *pro cédant*, calibrer le crédit-vendeur pour rester
dans ces bornes — si le prix est échelonné au-delà, le plan reste plafonné au
31 décembre de la cinquième année qui suit la cession : le cédant paie le solde
de l'impôt avant d'avoir encaissé le solde du prix. *Pro acquéreur*, c'est un
levier de négociation : proposer un crédit-vendeur compatible avec l'Art. 1681 F
rend l'échelonnement acceptable pour le cédant à moindre coût.

### 4.3 Fiscalité de l'acquéreur

- Prix d'acquisition des titres : base de sa plus-value future, diminué le cas
  échéant des sommes reçues au titre de la GAP (CGI Art. 150-0 D, 14)
- Structuration par holding de reprise : intérêts d'emprunt, intégration fiscale,
  régime mère-fille — **hors périmètre de ce skill**, router vers
  `consultation-juridique` ou `strategie-patrimoniale` si le sujet émerge
- Vérifier l'absence de clause du protocole faisant obstacle à une intégration
  fiscale ultérieure (calendrier de closing par rapport à la date de clôture)

### 4.4 Chiffrage

Tout protocole comportant un enjeu de plus-value doit déclencher `calcul-plus-value`
**avant** la signature, jamais après. Un cédant qui découvre son impôt après
signature n'a plus aucun levier de structuration.

---

## PHASE 5 — Structures de sortie par mode

### 5.1 MODE ANALYSE

```
0. POSTURE ET CONTEXTE
I. LECTURE STRATÉGIQUE
   Qui a rédigé, ce que le texte cherche, ce qui est absent
II. QUALIFICATION
   Nature de l'engagement, forme sociale, régime du transfert
III. FORMALITÉS D'ORDRE PUBLIC — CARTE DE CONFORMITÉ
   [Tableau : Formalité | Applicable ? | Traitée dans le projet ? | Risque]
IV. POSITIONNEMENT SUR LA TABLE DES CURSEURS
   [Paramètre | Position du projet | Position cible | Écart | Criticité 🔴🟠🟢]
V. CLAUSES PIÈGES DÉTECTÉES
   [Citation exacte → effet réel → riposte rédactionnelle]
VI. DIMENSION FISCALE
   Droits d'enregistrement, fait générateur, séquestre, earn-out, crédit-vendeur
VII. COHÉRENCE INTER-DOCUMENTS
   LOI ↔ protocole ↔ GAP ↔ statuts ↔ pacte
VIII. PLAN DE RIPOSTE
   Lignes rouges | Priorités | Concessions monnayables et contreparties
IX. CONCLUSION
   Signable en l'état ? À quelles conditions minimales ?
```

### 5.2 MODE RÉDACTION — ossature imposée

```
1.  Comparution et qualités (⚠️ conjoint, Art. 1424 C. civ. si parts communes)
2.  Exposé préalable (valeur interprétative — Art. 1188 C. civ. ; y consigner
    ce qui a déterminé le consentement, notamment côté acquéreur)
3.  Définitions (identiques à celles de la GAP, sans exception)
4.  Objet — titres cédés, quotité, propriété et jouissance
5.  Prix — montant, mécanique d'ajustement, exemple chiffré annexé
6.  Complément de prix / earn-out
7.  Modalités de paiement — séquestre, crédit-vendeur, sûretés
8.  Conditions suspensives — liste, délai, bénéficiaire, forme de la levée et
    de la renonciation, caducité
9.  Formalités préalables — information des salariés, agrément, conjoint,
    préemption, autorisations
10. Gestion intercalaire — liste fermée d'actes soumis à accord
11. Clause MAC (si retenue — objectivée et chiffrée)
12. Réalisation (closing) — lieu, date, acte réitératif exigé ou non, ordre
    des opérations, liste des remises, survie du protocole et règle de
    primauté avec l'acte définitif
13. Déclarations et garanties — renvoi à l'annexe GAP ; réitération à la date
    de réalisation
14. Non-concurrence et non-sollicitation
15. Accompagnement post-closing
16. Cautions personnelles et comptes courants
17. Confidentialité, exclusivité, communication
18. Substitution
19. Frais, droits d'enregistrement, formalités
20. Notifications, intégralité, nullité partielle
21. Loi applicable, attribution de juridiction, conciliation préalable
22. Annexes — comptes de référence, annexe de divulgation, projet de GAP,
    modèle d'ordre de mouvement, projet d'acte réitératif, exemple chiffré
    d'ajustement
```

Faire précéder d'une **note d'intention à Yoann** : positions retenues, points de
repli identifiés à l'avance, clauses qui appelleront une contre-proposition.

Tenir la plume déplace la charge de la contestation sur l'adversaire. Chaque fois
que Yoann peut la tenir, le lui rappeler.

### 5.3 MODE NÉGOCIATION

```
I. ÉTAT DES POSITIONS
   [Clause | Notre position | Leur position | Écart | Statut]
II. GRILLE D'ARBITRAGE
   [Position d'ouverture | Repli acceptable | Ligne rouge | Contrepartie exigée
    | Coût chiffré de la concession]
III. SÉQUENÇAGE
   Concessions précoces (crédibilité) / tardives (monnaie) / jamais
IV. PACKAGE DE SORTIE
```

**Règles de séquençage propres au protocole :**
- Prix, ajustement et séquestre forment un système : ne jamais céder sur les trois
  dans le même aller-retour
- Les conditions suspensives se négocient en bloc avec le délai de réalisation :
  allonger la liste sans raccourcir le délai est une double concession pour le cédant
- La non-concurrence se concède tard : elle coûte peu à l'acquéreur de la réduire
  et rassure le cédant à bon compte

### 5.4 Closing — renvoi

Une fois le protocole signé, la réalisation (constat de levée des conditions,
acte réitératif, pièces de closing, formalités et échéances post-closing)
relève de **`acte-definitif-titres`**. Ce skill reste compétent pour
interpréter le protocole et pour tout avenant (prorogation du délai de
réalisation, modification du prix ou des conditions).

---

## PHASE 6 — Cohérence inter-documents (contrôle final systématique)

Une opération se joue sur plusieurs documents qui doivent parler la même
langue. Ce contrôle est la source la plus fréquente de sinistres post-closing,
et il n'est presque jamais fait.

| Contrôle | Ce qui doit concorder |
|---|---|
| LOI ↔ protocole | Prix, calendrier, exclusivité, conditions annoncées |
| Protocole ↔ GAP | **Définitions identiques**, date des comptes de référence, plafonds, dates de closing, renvois d'articles |
| Protocole ↔ acte définitif | Définitions, survie, primauté, absence de novation (voir `acte-definitif-titres`) |
| Protocole ↔ statuts | Agrément, préemption, inaliénabilité, majorités |
| Protocole ↔ pacte existant | Sortie conjointe, préemption, engagements du cédant survivant à la cession |
| Protocole ↔ contrats de la cible | Clauses de changement de contrôle relevées en DD |
| Protocole ↔ financement de l'acquéreur | Conditions bancaires, sûretés exigées, calendrier de déblocage |

**Contrôles mécaniques à exécuter systématiquement** : chaque renvoi d'article
existe-t-il ? chaque terme défini est-il employé avec sa majuscule et jamais
comme synonyme libre ? les dates du protocole et de la GAP sont-elles les mêmes ?
les montants en chiffres et en lettres concordent-ils ?

---

## ✅ CHECKLIST AVANT REMISE

- [ ] **Posture annoncée explicitement en tête de livrable**
- [ ] **Aucune formulation « équilibrée » ou « les parties pourraient »**
- [ ] Forme sociale identifiée, statuts et pacte lus avant rédaction
- [ ] Carte des formalités d'ordre public complétée, aucune case vide
- [ ] Information des salariés : régime post-loi 2026-403 relu à la date de la
      vente, notification antérieure d'un mois à la signature du protocole,
      discordance L. 23-10-7 traitée par prudence
- [ ] Consentement du conjoint traité si parts communes (Art. 1424 C. civ.),
      pour l'aliénation **et** pour la perception du prix
- [ ] Mécanique de prix tranchée (locked box / closing accounts), exemple chiffré annexé
- [ ] Earn-out : indicateur défini contractuellement, protections calibrées selon la posture
- [ ] Crédit-vendeur : compatibilité avec CGI Art. 1681 F, I bis vérifiée
- [ ] Fait générateur fiscal et sort de la fraction séquestrée expliqués au client
- [ ] Conditions suspensives : bénéficiaire, délai, forme de levée et de
      renonciation, caducité, Art. 1304-2 et 1304-3
- [ ] Réalisation préparée : acte réitératif, survie, primauté, remises
- [ ] Gestion intercalaire bornée, absence de *gun jumping*
- [ ] Cautions personnelles et comptes courants traités expressément
- [ ] Non-concurrence : temps, espace, activité, proportionnalité
- [ ] Cohérence inter-documents contrôlée (Phase 6), renvois vérifiés un à un
- [ ] `calcul-plus-value` déclenché si enjeu de plus-value non chiffré
- [ ] Zones d'incertitude balisées ⚠️ INCERTAIN
- [ ] legal-hallucination-checker déclenché sur 100 % des références, sans référence non vérifiée restante (bloquant)
- [ ] Word ECA conforme au socle § 8 (corps noir ; titres d'actes noir gras)
- [ ] Conflit d'intérêts vérifié si ECA intervient pour la cible

**Si un seul item n'est pas validé → ne pas livrer.**
