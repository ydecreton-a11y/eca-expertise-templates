---
name: maintenance-skills
description: "Maintenance des skills ECA EXPERTISE : contrôle à la source de toutes les références citées dans les skills (articles, BOFiP, jurisprudence, textes, pièges datés du socle, échéances), détection des modifications, abrogations, renumérotations et versions à effet différé, mesure de l'effet sur chaque passage, correction dans le dépôt (mécanique directe, fond soumis à validation), cartes de mise à jour, rapport. Exécuté chaque trimestre et après chaque loi de finances (lancé par la veille du mercredi), ou à la demande. Déclencher sur : maintenance des skills, mise à jour des skills, skills à jour, vérifier les références des skills, index des références, impact de la loi de finances sur les skills, contrôle trimestriel. NE PAS utiliser pour vérifier les références d'un livrable (→ legal-hallucination-checker), améliorer la rédaction ou la structure d'un skill (→ darwin-skill) ou analyser un texte nouveau pour les clients (→ veille-juridique)."
---

# Maintenance des skills — ECA EXPERTISE

Une référence marquée « vérifié JJ/MM/AAAA » ou un piège daté du socle ne vaut
qu'à sa date. Ce skill les relit à la source chaque trimestre et après chaque
loi de finances, mesure l'effet de tout changement sur chaque passage qui les
cite, corrige et fait valider.

Charger `socle-eca` (vérification § 3, dépôt § 4, garde-fous § 7) et
`legal-hallucination-checker` (matrice de compétence des outils, règle « non
trouvé ≠ inexistant »).

> **Limite à connaître.** Aucune exécution ne peut installer ni modifier un
> skill dans claude.ai : seule la validation de Yoann le fait (carte de mise à
> jour, ou réinstallation depuis le dépôt). Ce skill tient à jour la source de
> vérité (le dépôt), prépare les cartes et prévient.

---

## 0. Modes

| Mode | Déclenchement | Périmètre |
|---|---|---|
| Complet | Tâche trimestrielle ; demande de « maintenance complète » | Toutes les entrées de l'index, pièges datés du socle, échéances du trimestre à venir |
| Loi de finances | Lancé par la veille du mercredi, texte précisé au lancement ; demande | Dispositions du texte publié au JORF, puis toutes les entrées de l'index qu'elles touchent |
| Ciblé | Lancé par la veille (textes ou articles précisés) ; demande sur une référence | Références listées et toutes leurs occurrences |

Le message de lancement précise le mode et, le cas échéant, les textes ou
articles ; à défaut : mode complet. Exécution sans surveillance : ne poser
aucune question, décider selon le mode mixte (§ 5) et tout consigner dans le
rapport.

## 1. Préparation

1. Cloner le dépôt (socle § 4) avec droit d'écriture ; créer la branche
   `maintenance/AAAAMMJJ` à partir de `main` à jour.
2. Charger l'index des références (rechercher « references-index » dans le
   dépôt : le `.json` est la source, le `.md` sa vue lisible) et l'outil
   `refs.py` placé à côté.
3. Réextraire les références de tous les skills du dépôt (`refs.py extract`),
   puis réconcilier avec l'index (`refs.py reconcile`) : références nouvelles →
   « à vérifier » ; références plus citées → retirées. Relire la liste produite :
   l'extraction est heuristique ; toute attribution de code fausse se corrige
   dans l'outil (tables de correction), jamais en silence.
4. Contrôler que les skills du dépôt sont ceux installés : si la copie
   synchronisée des skills installés est disponible dans la session, comparer le
   corps de chaque skill. Tout écart est signalé en tête du rapport
   (désynchronisation) : corriger une version que Yoann n'utilise pas ne sert à
   rien.

## 2. Contrôle à la source, par type

### 2.1 Articles de code

Outil : LibreJustice (statut, chronologie des versions, textes modificateurs) ;
recoupement Légifrance. Pour chaque entrée, lire la fiche de l'article et la
classer par comparaison avec sa date de dernière vérification :

| Constat à la source | Classement | Suite |
|---|---|---|
| En vigueur ; aucune version ni texte modificateur postérieur à la dernière vérification | INCHANGÉ | Date de vérification mise à jour ; relecture du passage seulement si l'entrée était « à vérifier » |
| Version ou texte modificateur postérieur à la dernière vérification | MODIFIÉ | Lire l'ancienne et la nouvelle version ; § 3 |
| Version future annoncée (« en vigueur différée »), y compris quand la version actuelle est marquée « abrogée à effet différé » mais suivie d'une version future | MODIFICATION DIFFÉRÉE | Lire la version future à sa date d'effet ; § 3 ; inscrire l'échéance |
| Version actuelle « abrogée à effet différé » sans version future | ABROGATION DIFFÉRÉE | Chercher le texte de transfert (recodification) ; inscrire l'échéance ; § 3 |
| Abrogé | ABROGÉ | Chercher l'article de reprise ; § 3 |
| Introuvable après deux stratégies sur deux outils compétents | INTROUVABLE | Renumérotation probable : recherche par objet ; ne jamais conclure à l'inexistence sans l'échec concordant exigé par le checker |

Toute entrée « à vérifier », ou classée autrement qu'INCHANGÉ, est lue **en
entier** dans la version utile (en vigueur, future, ou à la date que vise le
skill) et chaque passage qui la cite est confronté au texte (§ 3).

⚠️ **Piège constaté le 23/10/2026 (C. mon. fin. L. 561-46).** Une version
actuelle marquée « abrogée à effet différé », suivie d'une version « en vigueur
différée », n'est **pas** une abrogation : c'est une nouvelle rédaction. Lire la
version future avant de qualifier.

### 2.2 Loi de finances — décalage de consolidation

Les codes consolidés peuvent ne pas encore intégrer une loi publiée depuis peu.
En mode loi de finances :
1. lire la loi au JORF en texte intégral (Légifrance) et relever chaque
   disposition qui modifie, abroge ou crée un article, avec sa date d'entrée en
   vigueur et ses dispositions transitoires (souvent différentes d'un article à
   l'autre) ;
2. lire la décision du Conseil constitutionnel sur la loi s'il en existe une
   (dispositions censurées ou réserves) avant toute conclusion ;
3. croiser avec l'index, et avec les régimes que les skills traitent sans citer
   d'article (régime désigné par son nom : Dutreil, report, holding animatrice…) ;
4. pour chaque article touché : version consolidée à jour → § 2.1 ; sinon,
   travailler sur le texte de la loi, marquer l'entrée « consolidation en
   attente » et la reprendre au contrôle trimestriel suivant.

### 2.3 BOFiP

Lire la publication par son identifiant (LibreJustice ; Legal Data Hunter,
doctrine). Publication de la série postérieure à la dernière vérification →
relire le paragraphe cité ; § 3.

### 2.4 Jurisprudence

Existence et contenu selon la matrice du checker ; sort procédural (parcours
procédural Pourvoi, chronologie LibreJustice) ; recherche, triée par date, d'une
décision postérieure contraire ou d'un revirement depuis la dernière
vérification. Une référence incomplète (sans numéro) est complétée ou retirée du
skill.

### 2.5 Textes cités

Lois, ordonnances, décrets, actes de l'Union (OpenEU) : existence, erratum,
censure, dates d'entrée en vigueur, décrets d'application attendus.

### 2.6 Pièges datés du socle (§ 5)

Relire chaque source dans sa version en vigueur ; mettre à jour la colonne
« Vérifié ». Un piège devenu sans objet est proposé à la suppression, jamais
supprimé d'office.

### 2.7 Échéances

Toute échéance de l'index qui tombe avant le prochain contrôle trimestriel
(trois mois calendaires) : préparer la bascule (exemple : au 01/01/2027,
référence CIBS en regard de l'ancienne référence CGI). Les échéances nouvelles
repérées (versions différées) sont inscrites à l'index.

## 3. Effet sur chaque passage

Pour chaque référence touchée, relire **chaque occurrence** avec son contexte
(l'extrait de l'index sert d'ancre ; le numéro de ligne est indicatif), puis
qualifier :

| Effet | Définition | Exemples |
|---|---|---|
| NUL | Le passage reste exact au regard du texte nouveau | Modification d'un alinéa que le skill ne vise pas |
| MÉCANIQUE | Rien ne change dans ce que dit le skill : ni règle, ni condition, ni seuil, ni taux, ni délai, ni champ, ni sanction | Date de vérification, renumérotation à droit constant, mention du texte modificateur, renvoi interne |
| DE FOND | Le skill dit autre chose que le texte, ou la règle qu'il décrit change | Seuil, délai, condition, champ, sanction, régime ; passage déjà inexact |

En cas de doute entre mécanique et de fond : **de fond**.

Rédiger chaque correction au standard du skill concerné (mêmes conventions,
référence datée « vérifié JJ/MM/AAAA »), puis la soumettre à
`legal-hallucination-checker` (bloquant). Propager : une correction peut en
appeler d'autres dans le même skill ou dans un skill voisin (frontières, pièges
du socle, routeur, CLAUDE.md du dépôt).

## 4. Mise à jour de l'index

- Chaque entrée lue : date de dernière vérification = date du contrôle ; état
  à la source = statut, date de la version, versions futures, dernier texte
  modificateur.
- Date de dernière maintenance mise à jour ; vue lisible régénérée
  (`refs.py render`).

## 5. Mode mixte — ce qui s'enregistre sans validation

| Nature | Où | Validation |
|---|---|---|
| Index, rapport, corrections MÉCANIQUES | Directement sur `main` | Aucune ; tracé dans le rapport |
| Corrections DE FOND | Branche `maintenance/AAAAMMJJ`, demande de fusion vers `main` | Yoann : carte de mise à jour et fusion |

Règles :
- une seule branche par contrôle ; messages de commit précis (skill, référence,
  nature) ; retour arrière par `git revert`, jamais par réécriture
  d'historique ;
- ne jamais affaiblir une règle de vérification, supprimer un skill, une
  section ou un piège, ni modifier une tâche programmée ;
- aucune donnée client dans le dépôt (il est public) ;
- écriture dans le dépôt refusée : joindre au mail les fichiers corrigés et le
  rapport, et le dire en tête.

## 6. Cartes de mise à jour

Pour chaque skill dont le contenu change (mécanique ou de fond) : lire en entier
sa version installée (copie synchronisée de la session, à défaut celle du
dépôt), puis proposer la carte avec le SKILL.md complet issu de la branche (qui
contient aussi les corrections mécaniques) et la description d'origine
(1 024 caractères au plus, sans chevrons). Outil de proposition absent ou
refusé : joindre les fichiers au mail. Le rapport rappelle que valider une carte
de fond suppose aussi de fusionner la demande de fusion (ou de demander à Claude
de le faire).

## 7. Rapport et livraison

Rapport enregistré dans le dossier des rapports, à côté de l'index, sous le nom
`AAAA-MM-JJ.md` :

```
MAINTENANCE DES SKILLS ECA — [date] — mode [complet / loi de finances / ciblé]
Synthèse : N contrôlées | inchangées | modifiées | différées | abrogées |
           introuvables | consolidation en attente | encore à vérifier
Désynchronisation dépôt / skills installés : [néant / liste]
Corrections
| Référence | Skill (passage) | Changement à la source | Effet | Correction | Statut (main / branche) |
Échéances avant le prochain contrôle
Points ⚠️ INCERTAIN
Actions demandées à Yoann : cartes à valider, demande de fusion, arbitrages
Contrôle des références des corrections : [rapport du checker]
```

Livraison, selon les consignes de la tâche programmée :
- un seul mail à Yoann seul (aucun autre destinataire, ni copie, ni transfert),
  objet « Maintenance des skills ECA – [date] – [n] corrections » : synthèse,
  actions demandées, lien de la demande de fusion, liste des cartes, rapport
  joint ; échec d'envoi → brouillon ;
- une notification courte : « Maintenance skills [date] : X références,
  Y modifiées, Z cartes à valider. » ;
- aucun changement détecté : mail d'une ligne et notification, sans branche.

## 8. Exécution longue

Le mode complet représente plusieurs centaines de lectures. Enregistrer l'index
après chaque lot (commit sur `main`) : une exécution interrompue reprend au
premier lot non traité ; tout lot non traité est signalé dans le rapport.

---

## Pièges

- Conclure à une abrogation sur la seule mention « abrogé à effet différé »
  (§ 2.1).
- Se fier à la version consolidée dans les jours qui suivent une loi de
  finances (§ 2.2).
- Qualifier de mécanique une correction qui change une condition ou un délai.
- Corriger le dépôt sans vérifier qu'il correspond aux skills installés
  (§ 1.4).
- Laisser une entrée « à vérifier » au-delà de deux contrôles : la traiter en
  priorité.
