---
name: note-information-client
description: >
  Skill ECA EXPERTISE pour toute communication destinée à un client non-juriste :
  note d'information, note pédagogique, synthèse vulgarisée, lettre explicative,
  fiche pratique, résumé client. À utiliser après qu'une analyse de fond a été
  faite (consultation-juridique ou veille-juridique). Mots-clés : note client,
  expliquer à mon client, vulgariser, reformuler pour un client, fiche pratique,
  lettre d'information, résumé non technique, synthèse client.
---

# Skill : Note d'information client — ECA EXPERTISE

## PHASE 0 — Initialisation (exécuter en premier, toujours)

### 0a — Recherche dossier en cours

Si un nom de client est mentionné dans la demande :

```
conversation_search(query="[nom client ou société]")
```

- Si historique trouvé → lire les échanges pertinents avant de rédiger.
  Une note client doit s'inscrire dans la continuité de ce qui a déjà été
  expliqué ou conseillé — ne jamais contredire silencieusement une position antérieure.
- Si aucun historique → continuer normalement
- Si demande générique sans nom propre → pas de recherche

### 0b — Prérequis de fond

Ce skill produit un document client, pas une analyse de fond.
Le fond doit être arrêté avant de vulgariser.

```
Analyse de fond disponible ? → continuer ici
Fond pas encore établi ? → consultation-juridique ou patrimonial-structuring d'abord,
                            puis revenir ici pour la note client
```

### 0c — Intégration réponse Casus

Si Yoann colle un output Casus dans la conversation :
- L'utiliser comme base factuelle et fiscale vérifiée
- La note client est la vulgarisation de cet output pour le destinataire
- Indiquer : "Base Casus intégrée — je vulgarise pour le client"

---

## PHASE 1 — Calibrage du destinataire

Avant de rédiger, identifier le profil du client pour calibrer le registre :

| Profil | Registre | Ce qu'il faut éviter |
|--------|----------|---------------------|
| Dirigeant PME (non-juriste) | Clair, concret, chiffré, orienté décision | Jargon juridique non défini |
| Entrepreneur individuel | Simple, rassurant, étapes pratiques | Complexité excessive |
| Particulier (succession, cession) | Pédagogique, empathique, étapes claires | Termes techniques bruts |
| Associé averti | Plus technique accepté, mais pas de jargon inutile | Longueur excessive |

La note doit permettre au client de :
1. **Comprendre** sa situation sans formation juridique préalable
2. **Décider** ce qu'il veut faire
3. **Agir** sur la base d'instructions claires

---


### Sources (si la note nécessite de citer un taux ou une règle)

Fetcher avant de citer un taux fiscal :
```
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md")
```
Ne jamais citer un taux ou un abattement de mémoire dans une note client.
Un taux erroné dans une note client crée une responsabilité directe du cabinet.

## PHASE 2 — Règles rédactionnelles

**Vocabulaire :**
- Remplacer "cédant" par "vendeur", "cessionnaire" par "acheteur"
- Remplacer "prépondérance immobilière" par "société dont l'actif est
  principalement composé d'immobilier"
- Expliquer entre parenthèses tout terme technique conservé
- Ne jamais utiliser un article de code sans l'expliquer

**Structure :**
- Accroche : le fait concret qui impacte le client
- Contexte : pourquoi c'est important maintenant
- Explication : ce que ça signifie concrètement
- Ce que vous avez à faire : liste d'actions numérotées, avec délais
- Contact : pour aller plus loin

**Ton :**
- Neutre et professionnel (ni alarmiste, ni minimisant)
- Direct : aller à l'essentiel
- Actionnable : toujours terminer par ce que le client doit faire

---

## PHASE 3 — Structure de sortie

```
[Objet : titre court et explicite]

[Accroche : 2 lignes maximum — le fait et son impact direct]

I. CE QUI CHANGE / VOTRE SITUATION
   [Explication en langage clair — pas de jargon sans définition]

II. CE QUE CELA SIGNIFIE POUR VOUS
   [Impact concret, chiffré si possible]
   [Exemples si utile]

III. CE QUE VOUS DEVEZ FAIRE
   1. [Action — délai]
   2. [Action — délai]
   3. [Action — délai]

IV. VOS QUESTIONS ?
   [Nom du contact ECA, coordonnées]
```

---

## PHASE 4 — Livrable Word

- Corps : Raleway sz=22, justifié, **#999999**
- H1/H2 : Raleway gras, **#C00000**
- Signature : Raleway gras sz=22, **#495864**, centré
- Charger skill docx pour la mise en forme
- Vérifier que la note ne contient aucune référence légale non expliquée

---

## Exemple de note bien formée

**Objet : Impact de la réforme des prélèvements sociaux sur vos dividendes 2026**

Dès le 1er janvier 2026, le taux des prélèvements sociaux sur les dividendes
et les plus-values de cession de parts augmente de 1,4 point.

**Ce que ça change pour vous :**
Si vous percevez des dividendes de votre société en 2026, le taux global
d'imposition (impôt sur le revenu + prélèvements sociaux) passe de 30 %
à 31,4 % sur chaque euro distribué.

**Exemple chiffré :**
Sur une distribution de 50 000 €, le coût supplémentaire est de 700 €.

**Ce que vous devez faire :**
Aucune démarche immédiate n'est requise. Si vous envisagiez une distribution
importante en début d'année, votre conseiller ECA peut vous aider à évaluer
s'il est préférable de l'anticiper ou de la moduler.

Contactez [Nom] au [Téléphone] pour en discuter.

**❌ Ce qui est insuffisant :**
> "Suite à la LFSS 2026 (loi n°2025-1403), le taux de CSG sur les revenus
> du patrimoine est porté à 10,6% conformément à l'Art. L136-8 CSS."


---

## ENRICHISSEMENT — Template Fiche Pratique 1 page

Format compact pour les sujets où le client a besoin d'un calendrier, d'une checklist
ou d'un tableau de bord, plutôt qu'un texte explicatif.

```
[TITRE — sujet en 4-7 mots]
Fiche pratique ECA EXPERTISE — [date]

EN BREF
[3 à 4 lignes — le sujet, son enjeu, la décision à prendre]

CALENDRIER
| Étape | Quand | Qui |
|-------|-------|-----|
| [...] | J+0 | Client |
| [...] | J+30 | ECA |
| [...] | J+90 | Notaire |

POINTS D'ATTENTION
🔴 [point bloquant si pas traité]
🟠 [point à anticiper]
🟢 [point favorable]

QUESTIONS FRÉQUENTES
Q : [question 1]
R : [réponse en 2-3 lignes]

CONTACT
[Nom] — [téléphone] — [email]
```

**Quand utiliser ce format :**
- Le sujet a une dimension temporelle (Dutreil, donation progressive, OBO)
- Le client doit suivre des étapes successives
- Le sujet est récurrent dans la clientèle ECA et bénéficie d'un format réutilisable

---

## ENRICHISSEMENT — Profils clients étendus

| Profil | Registre | Spécificités |
|--------|----------|--------------|
| Héritier (succession en cours) | Empathique, pédagogique, pas de pression temporelle (deuil) | Délai 6 mois prolongé / option succession |
| Conjoint survivant | Rassurant, étapes claires, focus sur ses droits | Quasi-usufruit, pension de réversion, droit viager |
| Dirigeant en cession imminente | Direct, chiffré, orienté décision | Calendrier serré, fiscalité chiffrée |
| Bénéficiaire d'assurance-vie | Pédagogique sur la fiscalité spécifique (990 I / 757 B) | Distinguer primes < 70 ans / > 70 ans |
| Donataire (donation reçue) | Explicatif sur les obligations futures (rappel 15 ans) | Réintégration successorale, base de calcul |
| Particulier en patrimoine immo | Concret, illustré par cas chiffrés | Régime matrimonial impact, IFI seuil 1,3M€ |

**Règle transverse** : un client en situation émotionnelle (deuil, divorce, conflit
familial) ne lit pas une note de la même façon qu'un dirigeant en pleine forme.
Calibrer le ton avant d'optimiser le contenu.

---

## EXEMPLE — Fiche pratique Dutreil bien formée

```
DONATION-TRANSMISSION DUTREIL — VOTRE CALENDRIER
Fiche pratique ECA EXPERTISE — Avril 2026

EN BREF
Vous transmettez votre entreprise familiale via un Pacte Dutreil. Cette opération
réduit l'impôt de donation de 75 %, mais impose des engagements précis sur 6 ans
(LF 2026). Voici le calendrier à suivre.

CALENDRIER
| Étape | Quand | Qui |
|-------|-------|-----|
| Engagement collectif de conservation (2 ans min.) | M-24 | Vous + co-signataires |
| Évaluation de la société (méthode validée) | M-3 | Expert-comptable + auditeur |
| Donation devant notaire (acte authentique) | M-0 | Vous + notaire + donataires |
| Engagement individuel des donataires (4 ans) | À la donation | Donataires (signature acte) |
| Direction effective par un signataire (3 ans) | À la donation et après | Vous ou un donataire |

POINTS D'ATTENTION
🔴 Cession partielle pendant l'engagement = remise en cause totale de l'avantage
🟠 Distribution trop importante de réserves pourrait être requalifiée
🟢 Possibilité de cumul avec donation en nue-propriété (réduction supplémentaire)

QUESTIONS FRÉQUENTES
Q : Que se passe-t-il si je décède pendant l'engagement collectif ?
R : Vos héritiers reprennent l'engagement à votre place. Pas de remise en cause si
   l'engagement est tenu jusqu'au terme initial.

Q : Puis-je vendre une partie des titres pour faire face à un besoin urgent ?
R : Non, sauf cession entre signataires de l'engagement collectif. Toute autre
   cession entraîne perte de l'abattement.

CONTACT
Yoann Decreton — 03 27 72 00 10 — accueilcambrai@eca-groupe.com
```


---

## 🛡️ PHASE FINALE — Auto-déclenchement legal-hallucination-checker

⚠️ **OBLIGATOIRE — Étape non sautable.**

Avant remise du livrable au client ou à Yoann, déclencher automatiquement :

```
1. Charger skill legal-hallucination-checker
2. Extraire toutes les références citées :
   — Articles de code (CGI, C. civ., C. com., LPF, CMF, CSS, CPI...)
   — Jurisprudence (CE, Cass., CAA, TA, Cons. const.)
   — BOFiP (BOI-...)
   — Lois, ordonnances, décrets
3. Vérifier chacune via MCP Légifrance avec au minimum 2 stratégies de recherche
4. Produire le rapport de vérification (score /100)
5. Décision :
   — Si score ≥ 70 et 0 ⛔ HALLUCINATION → livrer + mentionner « Vérifié — score [N]/100 »
   — Si score < 70 ou présence de ⛔ HALLUCINATION → NE PAS LIVRER
     → Corriger les références fautives → relancer le checker → attendre validation Yoann
```

**Marquage final obligatoire dans le livrable :**
> *« Vérifié via legal-hallucination-checker — [N] références contrôlées — score [X]/100 »*

Cette mention est la signature qualité ECA. Sa présence engage Yoann ;
son absence signifie que la vérification n'a pas eu lieu.


---

## ✅ CHECKLIST AVANT REMISE

Valider mentalement chaque point avant d'envoyer la réponse :

- [ ] Toutes les références citées vérifiées via MCP Légifrance (Pattern 3 ci-dessous)
- [ ] Zones d'incertitude explicitement balisées avec ⚠️ INCERTAIN
- [ ] La conclusion répond directement et précisément à la question posée
- [ ] Niveau de risque justifié par un argumentaire (pas seulement affiché)
- [ ] Aucune position incertaine présentée comme certaine
- [ ] legal-hallucination-checker déclenché et score ≥ 70/100
- [ ] Charte graphique ECA respectée si livrable Word (#999999 / #C00000 / #495864)
- [ ] Référence YD + expert-comptable signataire mentionnée
- [ ] Profil destinataire identifié et registre calibré
- [ ] Aucun terme technique non défini en langage courant
- [ ] Tout taux ou abattement cité a été fetché (jamais de mémoire)
- [ ] Action concrète demandée au client en fin de note
- [ ] Coordonnées du contact ECA mentionnées

**Si un seul item n'est pas validé → ne pas livrer. Reprendre la phase concernée.**
