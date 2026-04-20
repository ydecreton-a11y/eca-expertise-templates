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
