---
name: consultation-juridique
description: >
  Skill central ECA EXPERTISE pour toute question juridique ou fiscale nécessitant
  une analyse de fond : régime fiscal, qualification juridique, règle applicable,
  risque, optimisation, transmission, report d'imposition, droit social, procédure.
  Déclencher sur : "quel est le régime", "comment qualifier", "quelles conséquences",
  "est-il possible de", "quels risques", "comment optimiser", "y a-t-il un risque",
  "fais un point sur", "analyse fiscalement", "rédige une consultation",
  consultation, note juridique, note fiscale, analyse fiscale, avis juridique.
  NE PAS utiliser si : un document contractuel est fourni (→ analyse-contrat),
  le client est en phase exploratoire sans opération définie (→ strategie-patrimoniale),
  la demande porte sur un texte nouveau (→ veille-juridique),
  un acte doit être rédigé sans question de fond (→ redaction-acte).
---

# Skill : Consultation juridique et fiscale — ECA EXPERTISE

> **Socle** : charger `socle-eca` — ouverture du dossier (§ 1), carte des
> connecteurs (§ 2), règles de vérification (§ 3), accès aux modèles (§ 4),
> pièges datés (§ 5), standard de rédaction (§ 6), garde-fous (§ 7), Word ECA
> (§ 8), fin de livrable (§ 9). Un output Casus collé est une base documentaire
> à recouper (§ 3.4). Aucun taux, seuil ou délai n'est repris de mémoire.

## PHASE 0 — Aiguillage

```
Document contractuel fourni                    → analyse-contrat
Chiffrage d'abord                              → calcul-plus-value
Phase exploratoire (transmission, patrimoine)  → strategie-patrimoniale
Texte nouveau à analyser                       → veille-juridique
Procédure fiscale en cours                     → contentieux-fiscal
Acte à rédiger sans question de fond           → redaction-acte ou skill de process
Sinon                                          → continuer ici
```

## PHASE 1 — Raisonnement préalable (avant toute recherche, avant toute rédaction)

Cette phase est interne — elle précède la réponse visible. Elle est la raison
pour laquelle la consultation sera juste plutôt que plausible.

**Exécuter mentalement dans cet ordre :**

1. **Qualification des faits** — Qui sont les parties ? Quelle est la nature
   juridique de l'opération ? Quelles sont les dates et montants clés ?
   Quelle forme sociale ? Quel régime fiscal ?

2. **Identification de la question de droit** — Formuler en une phrase la
   question juridique centrale. Une consultation qui ne pose pas clairement
   sa question ne peut pas y répondre clairement.

3. **Mapping des règles applicables** — Quels articles, quels régimes,
   quelle jurisprudence ? Identifier les zones de certitude et d'incertitude
   avant d'ouvrir Légifrance.

4. **Identification des risques de requalification** — Abus de droit ?
   Acte anormal de gestion ? Fiction juridique ? Anticiper avant de conseiller.

5. **Niveau de confiance initial** — Sur quels points suis-je certain ?
   Sur quels points dois-je impérativement vérifier ?

⚠️ Si les faits sont insuffisants pour cette phase, identifier précisément
ce qui manque et le demander avant de continuer.

---

## PHASE 2 — Recherche et vérification des sources

Suivre la carte des connecteurs (socle § 2) et les règles du socle § 3 :
- **Textes** : version en vigueur à la date du fait générateur (LibreJustice
  pour la lecture à date, Légifrance en recoupement).
- **Doctrine fiscale** : BOFiP via Legal Data Hunter ; noter le paragraphe et
  sa date de publication (opposabilité art. L. 80 A LPF).
- **Jurisprudence** : administrative (Légifrance, LibreJustice) ; judiciaire
  (Pourvoi, avec parcours procédural) ; Union (OpenEU). Lire la décision, pas
  son résumé ; qualifier sa portée (principe / espèce, publiée ou non).
- **Positions ECA** et **modules de formation du dépôt** couvrant le sujet
  (socle § 4) : compléments, jamais substituts.
- Une recherche qui n'aboutit pas est consignée (outil, requête) et le point
  est balisé `⚠️ INCERTAIN`.

## PHASE 3 — Rédaction de la consultation

### Format standard

```
I. RAPPEL DES FAITS PERTINENTS
   Synthèse neutre et précise. Mentionner les éléments déterminants
   pour la qualification : forme sociale, régime fiscal, dates, montants,
   structure du capital, opération envisagée.

II. PROBLÉMATIQUE(S) JURIDIQUE(S)
   Formuler la ou les questions de droit en termes précis.
   Exemple : "La question est de savoir si l'apport de titres réalisé
   par M. X, associé contrôlant à 80%, remplit les conditions de l'Art.
   150-0 B ter CGI pour bénéficier du report d'imposition."

III. RÈGLES DE DROIT APPLICABLES
   Textes, articles, principes généraux, jurisprudence.
   [Références lues et vérifiées à la source : Légifrance, LibreJustice,
    Legal Data Hunter (BOFiP), Pourvoi]
   Distinguer : droit positif / doctrine administrative / jurisprudence

IV. ANALYSE
   4.1 Qualification juridique des faits
   4.2 Application des règles — discussion argumentée
       (confronter les faits aux conditions légales, une par une)
   4.3 Points d'incertitude, risques d'interprétation, positions contraires
       [Utiliser la balise ⚠️ INCERTAIN pour chaque zone grise]

V. CONCLUSION OPÉRATIONNELLE
   — Position principale retenue (argumentée, pas affirmée)
   — Niveau de risque : 🔴 Élevé / 🟠 Modéré / 🟢 Faible
     (avec justification en une ligne)
   — Recommandations pratiques et points de vigilance
   — Prochaine étape concrète recommandée
```

### Complément si dominante fiscale

```
VI. CONSÉQUENCES FISCALES CHIFFRÉES (si données disponibles)
    Calcul du coût fiscal, comparaison d'options, simulations.
    [Paramètres sourcés et datés ; calcul par script ; renvoi calcul-plus-value si chiffrage lourd]

VII. RISQUES DE REDRESSEMENT
     — Qualification du risque fiscal
     — Pénalités et intérêts applicables (CGI art. 1727 et s., LPF L. 64 — taux lus à la source)
     — Position BOFiP et jurisprudence récente

VIII. STRATÉGIE D'OPTIMISATION ET ALTERNATIVES
      Options légales recommandées, séquencement, conditions de sécurisation.
```

---

## PHASE 4 — Repères par domaine

Il n'existe pas de fiche de domaine : pour chaque domaine, lire les sources
primaires et la base Positions ECA. Renvois vers les skills spécialisés :
transmission et patrimoine → `strategie-patrimoniale` ; holding et apport →
`holding-apport` ; chiffrage → `calcul-plus-value` ; procédure → `contentieux-fiscal`.
Droit social : consulter Gilberto Da Veiga (responsable social du cabinet) si
la question excède le droit des dirigeants.

---

## PHASE 5 — Livrable

Consultation au format Word ECA (socle § 8), signée YD et l'expert-comptable
du dossier. Si le destinataire est le client non juriste : produire en plus
une note via `note-information-client`.

## PHASE 6 — Contrôle qualité avant remise

Avant de finaliser la réponse, vérifier mentalement :

- [ ] Toutes les références citées ont été vérifiées (MCP ou BOFiP)
- [ ] Les zones d'incertitude sont signalées avec la balise ⚠️ INCERTAIN
- [ ] La conclusion répond directement à la question posée au §II
- [ ] Le niveau de risque est justifié, pas seulement affiché
- [ ] Aucune position incertaine n'est présentée comme certaine
- [ ] La dimension fiscale d'une opération impliquant des flux est traitée
- [ ] Le legal-hallucination-checker a été déclenché sur le livrable final

---

## Exemples de consultations bien formées

### Exemple 1 — Apport-cession (niveau de détail attendu)

**Input :**
> "Mon client détient 80% d'une SARL plâtrerie valorisée 1,2M€. Il veut
> apporter ses titres à une holding avant cession à un industriel. Est-ce
> possible ? Quel est l'intérêt ?"

**Structure de réponse attendue :**

I. Faits : SARL IS, associé majoritaire 80%, valorisation 1,2M€, opération
   envisagée : apport à holding IS avant cession à tiers.

II. Problématique : Conditions d'application de l'Art. 150-0 B ter CGI
    (report d'imposition) + analyse de l'intérêt par rapport à une cession
    directe + risques CDHR.

III. Règles : art. 150-0 B ter CGI dans sa version à la date de l'apport
     (condition de contrôle, quotité, nature et délai du réinvestissement —
     lus à la source, jamais de mémoire), CDHR (art. 224 CGI), doctrine BOFiP
     du report d'imposition (identifiant et paragraphe vérifiés).

[Suite de l'analyse avec chiffrage comparatif et recommandation]

**❌ Ce qui est insuffisant :**
> "L'Art. 150-0 B ter permet un report. Il faut contrôler la holding."

**❌ Ce qui est une erreur :**
> Conclure sur le report sans avoir vérifié, dans le texte en vigueur, que la
> condition de contrôle est remplie à la date de l'apport.

---

### Exemple 2 — Signal ⚠️ INCERTAIN correctement utilisé

**Situation :** Jurisprudence récente sur la holding animatrice, position
non encore consolidée dans le BOFiP.

**Formulation correcte :**
> "La jurisprudence du CE admet la qualification de holding animatrice sous
> conditions [référence vérifiée]. Toutefois :
> ⚠️ INCERTAIN — La position BOFiP sur les holdings mixtes (activité animatrice
> partielle) n'est pas encore stabilisée depuis [arrêt]. À vérifier via
> BOI-ENR-DMTG-10-20-40-10 avant de structurer le Dutreil."

---

