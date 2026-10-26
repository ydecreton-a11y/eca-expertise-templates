---
name: contentieux-fiscal
description: "Skill ECA EXPERTISE pour toute procédure de défense fiscale : réponse à proposition de rectification, réclamation contentieuse, mémoire hiérarchique, saisine de la Commission des impôts directs (CID), transaction fiscale, recours juridictionnel (TA, CAA, CE). Déclencher sur : contrôle fiscal, vérification de comptabilité, ESFP, proposition de rectification, redressement, réclamation, Commission des impôts, contentieux fiscal, défense fiscale, mémoire en réponse, provision déductible, chef de redressement, pénalités fiscales, manquement délibéré, abus de droit, transaction. NE PAS utiliser pour des questions de droit fiscal pur sans procédure en cours (→ consultation-juridique)."
---

# Skill : Contentieux fiscal — ECA EXPERTISE

> **Socle** : charger `socle-eca` — ouverture du dossier (§ 1), carte des
> connecteurs (§ 2), règles de vérification (§ 3), accès aux modèles (§ 4),
> pièges datés (§ 5), standard de rédaction (§ 6), garde-fous (§ 7), Word ECA
> (§ 8), fin de livrable (§ 9). Un output Casus collé est une base documentaire
> à recouper (§ 3.4). Aucun taux, seuil ou délai n'est repris de mémoire.

Ce skill existe parce que la défense fiscale obéit à des règles procédurales
strictes avec des délais de forclusion qui ne pardonnent pas. Une réponse
hors délai ou mal dirigée peut faire perdre des droits définitivement.
La maîtrise du calendrier procédural est aussi importante que les arguments
de fond.

---

## PHASE 0b — Routing et identification de l'étape procédurale

```
Question de droit fiscal sans procédure en cours ? → consultation-juridique
Calcul de l'impôt redressé à vérifier ? → calcul-plus-value en complément
→ Procédure en cours : continuer ici
```

**Identifier impérativement l'étape procédurale avant tout :**

```
PROPOSITION DE RECTIFICATION reçue (3924/3926) ?
  → PHASE A : Réponse dans le délai légal, prorogeable sur demande expresse
              (LPF L. 57 et R*57-1 — délai et conditions lus à la source)

RÉPONSE AUX OBSERVATIONS DU CONTRIBUABLE reçue ?
  → PHASE B : Évaluer recours hiérarchique (supérieur du vérificateur puis
              interlocuteur départemental ou régional, selon la charte des
              droits et obligations du contribuable vérifié, opposable — LPF L. 10),
              saisine de la commission, acceptation partielle

MISE EN RECOUVREMENT reçue (AMR) ?
  → PHASE C : Réclamation préalable obligatoire dans délai légal

REJET DE RÉCLAMATION reçu (ou silence) ?
  → PHASE D : Recours juridictionnel (TA / TJ selon l'impôt) — délai de saisine
              lu dans le LPF (R*199-1) ; ne pas confondre avec les délais de droit commun

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
- Jurisprudence récente favorable (recherchée et lue à la source : Légifrance,
  LibreJustice, Pourvoi)

---

## PHASE 2 — Recherche et vérification des sources

Carte des connecteurs (socle § 2) :
- **Procédure** : LPF dans la version applicable à chaque étape (LibreJustice
  à date) — garanties, délais, motivation, débat oral et contradictoire.
- **Charte du contribuable vérifié** : version remise au contribuable ; ses
  garanties sont opposables.
- **Fond** : CGI à la date du fait générateur ; BOFiP opposable (L. 80 A) via
  Legal Data Hunter, avec le paragraphe exact.
- **Jurisprudence** : CE, CAA, TA (Légifrance, LibreJustice) ; Pourvoi
  seulement pour le contentieux judiciaire (enregistrement, IFI, DMTG).
- **Pièces comptables** : Pennylane (comptes concernés par chaque chef :
  provisions, charges, TVA) pour reconstituer les faits.
- **Historique** : fiche mémoire du dossier, Granola (rendez-vous avec le
  service), mails (Microsoft 365) — ne jamais rédiger sans la dernière position
  écrite de l'administration.

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

### 4.2 Réclamation préalable (LPF L. 190 et R*196-1 s.)

**Délai de forclusion — à calculer à la source, jamais de mémoire :**
- délai général : LPF R*196-1 (version en vigueur depuis le 30/07/2026,
  décret n° 2026-692 — l'« événement » ouvrant un nouveau délai a été restreint) ;
- **après une procédure de reprise ou de rectification : LPF R*196-3**, délai
  égal à celui dont dispose l'administration — souvent plus long, à vérifier
  systématiquement ;
- autres délais spéciaux (R*196-2 et suivants) selon l'impôt.
Indiquer la date limite calculée **en tête** du livrable.

```
[Identification]
[Référence AMR et date]

RÉCLAMATION CONTENTIEUSE

En application des articles L. 190 et R*196-1 [ou R*196-3] du LPF, [contribuable]
entend contester les impositions mises en recouvrement le [date]
pour les motifs suivants :

[Développer les arguments — reprendre ceux de la réponse en les renforçant]

Par ces motifs, nous demandons la décharge totale / partielle des
impositions contestées.

[Pièces jointes : AMR, proposition de rectification, réponse initiale, justificatifs]
```

### 4.2 bis Recours hiérarchique et interlocuteur

Structure : rappel de la procédure et des points restés en désaccord ; pour
chaque chef, l'argument décisif (droit, doctrine opposable, preuve) et la pièce
qui le porte ; demande précise (abandon, réduction, modération des pénalités) ;
proposition d'entretien. Préparer en parallèle une **fiche d'entretien**
(arguments en 1 page, réponses aux objections attendues, concessions possibles,
ligne rouge). Après l'entretien : compte rendu (Granola) et courrier de
confirmation des points actés.

### 4.3 Saisine de la commission (LPF L. 59 s.)

**Conditions :**
- Désaccord persistant après réponse de l'administration
- Compétence de la commission (LPF L. 59 A, vérifié 26/10/2026 ; nouvelle
  rédaction au 01/01/2027, « taxes sur les biens et services », issue de
  l'ordonnance n° 2025-1247) : désaccord sur le montant du résultat BIC, BNC,
  BA ou du chiffre d'affaires déterminé selon un régime réel ; sur les régimes
  d'exonération ou d'allégement des entreprises nouvelles (hors qualification
  des dépenses de recherche) ; sur les rémunérations non déductibles
  (CGI art. 39, 1, 1° et 111, d) et les dépenses du relevé de l'article
  54 quater ; sur la valeur vénale servant de base à la TVA immobilière.
  Elle se prononce sur les faits sans trancher de question de droit, mais peut
  se prononcer sur l'acte anormal de gestion, le principe et le montant des
  amortissements et des provisions, et la qualification de charge déductible
  ou d'immobilisation
- Délai : à compter de la réponse aux observations — délai et commission
  compétente (départementale, nationale) lus dans le LPF en vigueur (L. 59 s., R*59-1)

**La Commission rend un avis consultatif** — non contraignant mais
avec un fort poids pratique. L'administration suit généralement l'avis.

```
Madame, Monsieur le Président de la Commission [départementale] des
impôts directs et des taxes sur le chiffre d'affaires [sur les biens et
services à compter du 01/01/2027],

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
> En second lieu, la doctrine administrative (BOI-BIC-PROV-40-20 pour les
> créances douteuses ou litigieuses, BOI-BIC-PROV-20-10-30 pour le
> caractère probable de la perte, § [X]) admet qu'une créance fait l'objet
> d'un risque probable dès lors que [position favorable — paragraphe lu à
> la source avant citation].
>
> ⚠️ INCERTAIN — Identifiants BOFiP vérifiés le 26/10/2026 ; lire le paragraphe
> applicable (Legal Data Hunter), dans sa version à la date de clôture, avant
> intégration dans la réponse définitive.
>
> En conséquence, nous demandons l'abandon de ce chef de rectification."

**❌ Ce qui est insuffisant :**
> "Les provisions sont justifiées car les créances sont douteuses."

---

## ✅ CHECKLIST AVANT REMISE

Valider mentalement chaque point avant d'envoyer la réponse :

- [ ] Toutes les références citées vérifiées à la source primaire en vigueur (socle § 2 et § 3)
- [ ] Zones d'incertitude explicitement balisées avec ⚠️ INCERTAIN
- [ ] La conclusion répond directement et précisément à la question posée
- [ ] Niveau de risque justifié par un argumentaire (pas seulement affiché)
- [ ] Aucune position incertaine présentée comme certaine
- [ ] legal-hallucination-checker déclenché sur 100 % des références, sans référence non vérifiée restante (bloquant)
- [ ] Word ECA conforme au socle § 8 (corps noir ; titres d'actes noir gras)
- [ ] Référence YD + expert-comptable signataire mentionnée
- [ ] Étape procédurale identifiée (Phase A/B/C/D/E)
- [ ] Délai de forclusion calculé et signalé en tête
- [ ] Vices de procédure soulevés en priorité si applicables
- [ ] Position BOFiP opposable (Art. L80 A LPF) recherchée
- [ ] Stratégie globale (résistance / transaction / acceptation partielle) tranchée

**Si un seul item n'est pas validé → ne pas livrer. Reprendre la phase concernée.**

---
