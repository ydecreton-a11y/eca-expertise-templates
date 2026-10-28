# CLAUDE.md — Manifeste d'orchestration ECA EXPERTISE

> Index de routage. Aucune donnée métier volatile (taux, seuil, délai, chemin) :
> chaque information vit à un seul endroit, ce manifeste y pointe.
> Dernière mise à jour : 23/10/2026 — refonte de l'écosystème (socle unique) ;
> ajout de `lettre-intention`, `acte-definitif-titres`, `restructurations` et
> `maintenance-skills` ; index des références et maintenance trimestrielle.
> 28/10/2026 : ajout de `evaluation-titres-fonds` (documentation dans `12_évaluation_entreprise`).

---

## 1. Carte de l'écosystème (29 skills)

| Couche | Skill | Rôle |
|---|---|---|
| Transverse | `socle-eca` | Ouverture de dossier, carte des connecteurs, vérification, pièges datés, standard M&A, corpus documentaire, charte Word, garde-fous |
| Transverse | `positions-eca` | Base Notion des positions : consultée avant, enrichie après |
| Transverse | `legal-hallucination-checker` | Vérification bloquante de 100 % des références en fin de livrable |
| Orientation | `router-eca` | Reformulation d'intention, enchaînements de skills, codes de prompt |
| Orientation | `prompt-builder-eca` | Fabrique les prompts Casus / Claude à partir de faits bruts |
| Analyse | `consultation-juridique` | Analyse de fond juridique ou fiscale |
| Analyse | `strategie-patrimoniale` | Transmission, patrimoine, donation, démembrement, régimes, successions |
| Analyse | `calcul-plus-value` | Chiffrage des plus-values et contributions, scénarios |
| Analyse | `evaluation-titres-fonds` | Évaluation de titres non cotés et de fonds de commerce ; classeur Excel interne |
| Analyse | `contentieux-fiscal` | Défense fiscale : rectification, recours, réclamation, juridiction |
| Analyse | `analyse-contrat` | Analyse et sécurisation d'un contrat entre parties |
| Analyse | `due-diligence-juridique` | Audit de cible et rapport de DD |
| M&A à posture | `lettre-intention` | Lettre d'intention, term sheet, offre indicative (titres ou fonds) |
| M&A à posture | `protocole-cession` | Protocole ou promesse de cession de titres sous conditions, cession simple |
| M&A à posture | `acte-definitif-titres` | Acte définitif et closing après levée des conditions (titres) |
| M&A à posture | `gap` | Garantie d'actif et de passif |
| M&A à posture | `cession-fonds` | Cession de fonds de commerce ou artisanal (compromis, acte définitif) |
| Process d'actes | `redaction-acte` | Moteur de rédaction et fiches de toutes les modifications statutaires |
| Process d'actes | `pacte-associes` | Pacte d'associés à partir des trois documents de référence |
| Process d'actes | `juridique-annuel` | Approbation des comptes, dividendes, capitaux propres |
| Process d'actes | `holding-apport` | Holding, apport de titres par une personne physique, report 150-0 B ter |
| Process d'actes | `restructurations` | Fusion, fusion simplifiée, scission, apport partiel d'actif, choix TUP ou fusion |
| Process d'actes | `dissolution-liquidation-tup` | Dissolution, liquidation, exécution d'une TUP |
| Sortie | `note-information-client` | Notes client, courriers, réponses aux collègues |
| Sortie | `avocat-adverse` | Relecture par le contradicteur le plus compétent |
| Sortie | `veille-juridique` | Veille ; post LinkedIn du lundi, veille PowerPoint ECA du mercredi |
| Outillage | `darwin-skill` | Évaluation et optimisation des skills |
| Outillage | `pieces-pseudonymisees` | Travail sur pièces pseudonymisées |
| Outillage | `maintenance-skills` | Contrôle périodique des références citées dans les skills (trimestre, loi de finances) et mise à jour |

Retirés le 23/10/2026 : `shared` (→ `socle-eca`), `diagnostic-transmission` et
`patrimonial-structuring` (→ `strategie-patrimoniale`), `devils-advocate`
(→ `avocat-adverse`).

---

## 2. Chaîne d'activation de tout livrable

```
1. socle-eca § 1   → ouverture du dossier (mémoire, historique, Granola, mails, Radar, Pennylane)
2. positions-eca   → positions existantes (base Positions ECA)
3. skill métier    → plan → validation de Yoann → recherche à la source → rédaction
4. checker         → 100 % des références vérifiées (bloquant)
5. positions-eca   → proposition des positions nouvellement tranchées
6. avocat-adverse  → proposé pour tout acte engageant une partie
7. Échéances       → signalées en fin de livrable
```

---

## 3. Sources de vérité

| Donnée | Où |
|---|---|
| Taux, seuils, délais, articles | À la source primaire au jour du livrable (Légifrance, LibreJustice, Legal Data Hunter) — jamais dans un skill |
| Pièges datés (alarmes) | `socle-eca` § 5 |
| Carte des connecteurs | `socle-eca` § 2 |
| Standard de rédaction M&A | `socle-eca` § 6 |
| Charte et méthode Word | `socle-eca` § 8 |
| Corpus documentaire (Dutreil 2026, Royal Formation, démembrement de l'immobilier d'entreprise, Revue Fiduciaire, AUREP) | Ce dépôt — repéré par titre, voir `socle-eca` § 4 bis |
| Modèles et précédents d'actes | Ce dépôt (dossiers `01_` à `11_`) — trouvés par recherche, pas par chemin |
| Positions ECA | Notion, collection `6dc1e530-7996-4a62-b5b6-b378b4c8f204` |
| Veille | Notion, `f201a44e-556f-4420-8f61-eec1f8cb2d5a` (ne pas confondre avec la base Positions) |
| Consultations | Notion, `cadd1870-11e1-4dfa-9298-7d5c5977f564` |
| Skills (source) | `skills-user/` de ce dépôt, réinstallés dans claude.ai après chaque modification |
| Références citées dans les skills (« vérifié JJ/MM/AAAA »), pièges datés, échéances annoncées | `skills-user/maintenance/references-index.json` (vue lisible : `references-index.md`), tenu par `maintenance-skills` |
| Rapports de maintenance des skills | `skills-user/maintenance/rapports/` |
| Codes de prompt | `skills-user/prompt-codes-eca.md` |

---

## 4. Anti-patterns

- ❌ Écrire un taux, un seuil, un délai, un chemin de fichier ou une syntaxe
  d'outil dans un skill métier — seule exception : une référence datée
  « vérifié JJ/MM/AAAA », inscrite à l'index des références et suivie par
  `maintenance-skills`.
- ❌ Citer une référence sans l'avoir lue à la source dans la version applicable.
- ❌ Reprendre une donnée d'un précédent client dans un nouvel acte.
- ❌ Mentionner un modèle ou un auteur tiers dans un livrable client.
- ❌ Laisser un délai en « jours » non qualifié.
- ❌ Interroger un connecteur nominatif sur une pièce pseudonymisée.
- ❌ Livrer sans rapport du checker.
