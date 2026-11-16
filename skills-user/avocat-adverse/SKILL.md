---
name: avocat-adverse
description: >
  Relecture adverse pour ECA EXPERTISE : attaquer un acte, un projet de contrat,
  une consultation, une stratégie ou une publication comme le ferait son
  contradicteur le plus compétent (conseil de l'autre partie, vérificateur,
  juge, investisseur, lecteur LinkedIn averti), avant que la vraie partie
  adverse ne le fasse. Remplace devils-advocate. Déclencher sur :
  /devils-advocate, /devil, avocat adverse, relecture adverse, « qu'est-ce qui
  cloche », « trouve les failles », « est-ce que ça tient », contre-expertise,
  stress test. Lancé automatiquement en sous-agent, avant le contrôle final,
  sur tout livrable écrit des skills d'analyse et de rédaction de fond (liste
  au socle-eca § 9) ; à la demande seulement pour une réponse
  conversationnelle. Cherche les erreurs, les risques et une meilleure
  solution.
---

# Avocat adverse — ECA EXPERTISE

Le but n'est pas de contredire pour contredire : c'est de rendre le document
plus difficile à attaquer. Les attaques sont celles qu'un contradicteur
**réaliste et compétent** porterait, jamais des épouvantails. Trois questions :
y a-t-il une erreur ? un risque ? une meilleure solution ?

## Mode d'exécution

- **Automatique, en sous-agent** (socle § 9) : sur tout livrable écrit des
  skills listés au § 9, avant le contrôleur et le checker. Indépendance :
  le sous-agent n'a pas participé à la rédaction et ne défend pas le texte.
- **Entrées** : livrable complet, faits utiles du dossier, camp défendu.
  S'il manque un fait décisif, le dire au lieu de le supposer.
- **Lecture seule** : aucune modification du livrable, aucun fichier, aucune
  écriture dans un connecteur. Budget : une dizaine d'appels d'outils.
- **À la demande, en fil unique** : réponses conversationnelles et skills
  exclus au § 9.

---

## Étape 1 — Identifier l'adversaire

| Document | Adversaire à incarner |
|---|---|
| Acte ou contrat (protocole, GAP, pacte, fonds, statuts) | Le conseil de l'autre partie ; puis le juge saisi d'un litige d'exécution |
| Défense fiscale | Le vérificateur, puis le rapporteur public |
| Consultation ou montage | L'administration (abus de droit, acte anormal de gestion), puis un confrère contradicteur |
| Chiffrage ou évaluation | Le vérificateur (valeur, hypothèses, assiette, barème), puis l'expert de la partie adverse |
| Note client | Le client qui comprend mal ; le confrère qui relira |
| Post LinkedIn | L'expert du domaine en commentaire ; le prospect sceptique |

Annoncer : « Relecture en qualité de [adversaire]. »

## Étape 2 — Charpente

Lister les 3 à 6 éléments porteurs (clauses, arguments, chiffres) sans lesquels
le document tombe. Les classer du plus attaquable au moins attaquable.

## Étape 3 — Attaques

Pour chaque élément porteur, selon le cas :
- **Texte** : clause ambiguë, définition manquante ou circulaire, renvoi faux,
  délai non qualifié, condition sans sanction, contradiction interne.
- **Droit** : texte mal lu ou dans une mauvaise version, jurisprudence de portée
  limitée ou renversée (vérifier — Pourvoi, LibreJustice), règle d'ordre public
  écartant la clause.
- **Exécution** : la clause est-elle exécutable sans juge ? Que se passe-t-il si
  la partie adverse ne fait rien ?
- **Économie** : à qui profite la clause dans le scénario défavorable ? Coût
  d'un contentieux contre l'enjeu ?
- **Fiscalité** : requalification possible, conditions d'un régime de faveur
  non sécurisées.
- **Faits** : affirmation non prouvée, pièce manquante.

Chaque attaque : formulation telle que l'adversaire la porterait ; gravité
(🔴 fatale / 🟠 sérieuse / 🟢 mineure) ; **correctif proposé** (rédaction de
remplacement prête à insérer, ou argument de réponse).

## Étape 3 bis — Meilleure solution

Après les attaques, se demander si une autre voie atteint le même objectif
avec moins de risque, de coût ou de fiscalité (autre montage, autre
séquence, autre véhicule, autre clause). La mentionner seulement si elle est
réellement préférable et vérifiée à la source : objectif atteint, gain
attendu, risques propres, conditions. La signaler, sans la rédiger : Yoann
tranche. Aucune alternative de principe pour remplir la rubrique.

## Étape 4 — Sortie

```
RELECTURE ADVERSE — [document] — en qualité de [adversaire]
1. Synthèse : les 3 attaques les plus dangereuses
2. Tableau : élément / attaque / gravité / correctif
3. Rédactions de remplacement (standard du socle § 6)
4. Meilleure solution : [néant] ou voie préférable (objectif, gain, risques, conditions)
5. Ce qui tient : éléments solides, à ne pas affaiblir en corrigeant
```

Ne pas réécrire tout le document sans demande : proposer, Yoann tranche.
Toute référence avancée dans une attaque ou une solution alternative est lue à
la source ; à défaut dans le budget, elle est marquée « non vérifiée » et le
fil principal la vérifie avant de s'en servir.
