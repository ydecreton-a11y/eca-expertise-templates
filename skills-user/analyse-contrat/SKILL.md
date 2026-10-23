---
name: analyse-contrat
description: >
  Skill ECA EXPERTISE pour toute analyse, relecture, rédaction ou sécurisation
  d'un document contractuel : contrat, convention, bail, CGV, pacte, NDA, MOU,
  lettre de mission, protocole, acte de cession, garantie. Déclencher dès qu'un
  document contractuel est fourni ou qu'une clause doit être analysée ou rédigée.
  Mots-clés : analyser, relire, vérifier, sécuriser, rédiger, améliorer un contrat,
  une clause, un accord, un avenant.
  NE PAS utiliser si : la demande est une consultation de droit pur sans document
  fourni (→ consultation-juridique), si un acte de droit des sociétés doit être
  créé de zéro (→ redaction-acte), ou si le document est un pacte d'associés
  (→ pacte-associes), un protocole ou une cession de titres (→ protocole-cession),
  une GAP (→ gap) ou une cession de fonds (→ cession-fonds).
---

# Skill : Analyse contractuelle — ECA EXPERTISE

> **Socle** : charger `socle-eca` — ouverture du dossier (§ 1), carte des
> connecteurs (§ 2), règles de vérification (§ 3), accès aux modèles (§ 4),
> pièges datés (§ 5), standard de rédaction (§ 6), garde-fous (§ 7), Word ECA
> (§ 8), fin de livrable (§ 9). Un output Casus collé est une base documentaire
> à recouper (§ 3.4). Aucun taux, seuil ou délai n'est repris de mémoire.

## PHASE 0b — Qualification et routing

```
Document contractuel fourni ? → continuer ici
Pas de document, question de droit pur ? → skill consultation-juridique
Acte de droit des sociétés à créer (statuts, PV, cession) ? → skill redaction-acte
```

---

## PHASE 1 — Raisonnement préalable (avant lecture détaillée)

Avant d'analyser clause par clause, poser mentalement :

1. **Quelle est la nature juridique de ce contrat ?**
   La qualification conditionne le régime impératif applicable.

2. **Quel est le déséquilibre apparent ?**
   Qui a rédigé ? En faveur de qui ? Quel est le contexte de négociation ?

3. **Quels sont les enjeux prioritaires pour ECA et son client ?**
   Protection du prix ? Maintien de l'activité ? Limitation de responsabilité ?

4. **Y a-t-il une dimension fiscale évidente ?**
   Flux financiers, cession d'actifs, droits d'enregistrement.

---

## PHASE 2 — Posture, sources et vérifications

**Posture** : identifier qui ECA conseille (signataire, cocontractant, tiers) ;
s'il est incertain, demander. Les recommandations et les rédactions de
remplacement servent ce camp ; signaler loyalement les clauses qu'un juge
risque d'écarter même si elles le favorisent.

**Sources** (socle § 2) : droit commun des contrats (C. civ., version à la date
de conclusion — les contrats antérieurs à la réforme de 2016 restent régis par
l'ancien droit), règles d'ordre public sectorielles (consommation, commerce,
travail, baux), jurisprudence récente sur les clauses litigieuses (Pourvoi pour
la portée), droit de l'Union si le contrat est international (OpenEU), droit
étranger applicable (Legal Data Hunter).


## PHASE 3 — Analyse structurée

### 3.1 Qualification juridique
- Nature du contrat (prestation, vente, bail, cession, pacte…)
- Régime applicable (droit commun / règles spéciales)
- Parties et capacité juridique

### 3.2 Analyse des clauses essentielles

Examiner dans cet ordre :
1. Objet et périmètre de la prestation
2. Obligations principales de chaque partie
3. Conditions financières (prix, révision, indexation, TVA)
4. Durée, reconduction, résiliation (Art. 1211 s. C. civ.)
5. Responsabilité, limitations, garanties, clauses pénales
6. Force majeure (Art. 1218 C. civ.) et imprévision (Art. 1195 C. civ.)
7. Confidentialité et non-sollicitation
8. Non-concurrence (proportionnalité, durée, zone, contrepartie)
9. Propriété intellectuelle (Art. L131-3 CPI pour cessions écrites)
10. Attribution de juridiction / arbitrage

### 3.3 Détection des déséquilibres
- Clauses abusives B2C (Art. L212-1 C. conso.)
- Déséquilibre significatif B2B (Art. L442-1 C. com.)
- Clauses potentiellement réputées non écrites

### 3.4 Dimension fiscale
Tout contrat impliquant des flux financiers doit traiter :
- Qualification fiscale des sommes (honoraires, redevances, prix de cession…)
- Régime TVA (exonération, autoliquidation, taux)
- Droits d'enregistrement (cessions, baux commerciaux)
- Risque de requalification (prix anormal, acte anormal de gestion)

---

## PHASE 4 — Structure de sortie

```
I. QUALIFICATION JURIDIQUE ET CADRE APPLICABLE
   1.1 Nature du contrat et régime
   1.2 Parties, capacité, pouvoir de signature

II. ANALYSE DES CLAUSES ESSENTIELLES
   [Clause par clause avec : résumé → risque → recommandation]

III. DIMENSION FISCALE ET RÉGLEMENTAIRE

IV. COTATION DES RISQUES
   [Tableau : Clause | Risque | Nature | Criticité 🔴🟠🟢 | Recommandation]

V. RECOMMANDATIONS ET SÉCURISATION
   5.1 Modifications rédactionnelles prioritaires (avec texte suggéré)
   5.2 Points à négocier
   5.3 Stratégie globale

VI. CONCLUSION
   Appréciation globale du niveau de sécurité juridique.
```

---

## Exemple de sortie bien formée

**Input :** "Analyse ce contrat de prestation de services informatiques"

**Risque détecté et formulé correctement :**
> "**Clause de limitation de responsabilité (Art. 8)** — La clause plafonne
> la responsabilité du prestataire au montant des honoraires de la dernière
> mensualité. Ce plafond est disproportionné si la prestation défaillante
> peut causer un préjudice commercial significatif au client.
> **Criticité : 🔴 Élevé**
> **Recommandation :** Négocier un plafond au montant total du contrat annuel
> ou à un multiple des honoraires mensuels (x3 à x6 selon l'enjeu)."

**❌ Ce qui est insuffisant :**
> "La clause de limitation de responsabilité pourrait poser problème."

---

## ENRICHISSEMENT — Templates de modifications rédactionnelles courantes

Quand l'analyse identifie un risque 🔴, ne jamais s'arrêter à « clause à renégocier ».
Toujours proposer la rédaction de remplacement. Voici les patterns ECA validés.

### 1. Clause de limitation de responsabilité — version équilibrée
```
« La responsabilité du Prestataire au titre de l'exécution du présent contrat
ne pourra excéder, tous préjudices confondus, un montant équivalent à [N×]
les honoraires versés au titre des [12] mois précédant le fait générateur,
sous réserve des cas pour lesquels la loi exclut toute limitation
(dol, faute lourde, atteinte aux personnes). »
```

### 2. Clause de non-concurrence — version sécurisée (Cass. soc. 10/07/2002)
```
« Pendant une durée de [X] mois suivant la cessation du présent contrat, le
[Salarié/Prestataire] s'interdit, dans la zone géographique de [périmètre
précis et limité], d'exercer une activité de [activité précisément définie
et limitée à ce qui est nécessaire à la protection des intérêts du Client].
En contrepartie, le [Client] versera mensuellement au [Salarié/Prestataire]
une indemnité d'un montant égal à [montant conforme à la convention collective
applicable et à la jurisprudence en vigueur, vérifiés — pourcentage de la rémunération mensuelle
moyenne]. »
```
Quatre conditions cumulatives (proportionnalité, limitation espace/temps,
intérêts légitimes, contrepartie financière) — l'absence d'une seule entraîne nullité.

### 3. Clause de force majeure — version Art. 1218 C. civ. enrichie
```
« Constitue un cas de force majeure tout événement échappant au contrôle du
débiteur, qui ne pouvait être raisonnablement prévu lors de la conclusion du
contrat et dont les effets ne peuvent être évités par des mesures appropriées,
empêchant l'exécution de son obligation par le débiteur (Art. 1218 C. civ.).
La Partie qui invoque la force majeure notifiera l'autre Partie par écrit dans
un délai de [X] Jours Ouvrés suivant la survenance de l'événement. Si l'empêchement
est définitif ou excède [X mois], chaque Partie pourra résilier le contrat
sans indemnité, par lettre recommandée avec accusé de réception. »
```

### 4. Clause d'imprévision — version Art. 1195 C. civ. négociée
```
« En cas de changement de circonstances imprévisible lors de la conclusion du
contrat rendant l'exécution excessivement onéreuse pour l'une des Parties, et
sous réserve qu'elle n'ait pas accepté d'en assumer le risque, cette Partie
pourra demander une renégociation à l'autre Partie. À défaut d'accord dans un
délai de [X mois], les Parties pourront, d'un commun accord, résoudre le contrat
ou demander d'un commun accord au juge de procéder à son adaptation. »
```
**Vigilance** : l'Art. 1195 C. civ. est supplétif — il peut être écarté par
les parties. L'absence ou l'aménagement de la clause doit être un choix conscient.

### 5. Clause d'indexation — version sécurisée
```
« Le prix sera révisé chaque [période] selon la formule suivante :
P = P₀ × (I_n / I_n-1)
où I est l'indice [INSEE / professionnel précis], dans sa dernière publication
disponible à la date de révision, et I_n-1 sa valeur de référence à la date
[de signature/de la révision précédente].
En cas de disparition de l'indice, il sera remplacé par l'indice de
substitution publié par l'organisme compétent ou, à défaut, par l'indice
ayant le périmètre le plus proche. »
```

---

## CAS — Contrat partiel ou en langue étrangère

### Contrat fourni en extrait seulement
- Signaler dès le début : « Analyse partielle — clauses non communiquées : [...] »
- Identifier les clauses absentes structurellement (résiliation, juridiction, force majeure)
- Demander les clauses manquantes avant analyse finale
- Ne jamais conclure sur la sécurité globale d'un contrat sur la base d'extraits

### Contrat en langue étrangère
- Si la langue est maîtrisée (anglais, allemand) : analyser, mais signaler que la
  version juridiquement opposable est celle du droit applicable
- Si traduction nécessaire : refuser l'analyse de fond avant traduction certifiée
  pour les clauses critiques (responsabilité, juridiction, prix)
- Mentionner systématiquement la clause de langue applicable

---

## ✅ CHECKLIST AVANT REMISE

Valider mentalement chaque point avant d'envoyer la réponse :

- [ ] Toutes les références citées vérifiées via MCP Légifrance (voir annexe en fin de skill)
- [ ] Zones d'incertitude explicitement balisées avec ⚠️ INCERTAIN
- [ ] La conclusion répond directement et précisément à la question posée
- [ ] Niveau de risque justifié par un argumentaire (pas seulement affiché)
- [ ] Aucune position incertaine présentée comme certaine
- [ ] legal-hallucination-checker déclenché et score ≥ 70/100
- [ ] Word ECA conforme au socle § 8 (corps noir ; titres d'actes noir gras)
- [ ] Référence YD + expert-comptable signataire mentionnée
- [ ] Qualification juridique du contrat explicitée (Art. applicable)
- [ ] Cotation 🔴/🟠/🟢 portée sur chaque clause sensible
- [ ] Recommandation rédactionnelle proposée pour chaque risque 🔴

**Si un seul item n'est pas validé → ne pas livrer. Reprendre la phase concernée.**

---

