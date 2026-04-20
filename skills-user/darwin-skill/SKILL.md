---
name: darwin-skill
description: >
  Optimiseur autonome de SKILL.md pour l'écosystème ECA EXPERTISE.
  Évalue les skills selon un rubric 8 dimensions (structure + effet réel),
  applique un hill-climbing avec versioning git, valide les améliorations
  par test prompts. Déclencher sur : "optimise mes skills", "évalue mes skills",
  "skill review", "améliore le skill [nom]", "score mes skills", "darwin",
  "auto optimize skills", "skill quality check", "skill scoring",
  "améliorer workflow", "quels skills sont faibles".
---

# Darwin.skill — Optimiseur de l'écosystème ECA EXPERTISE

> Inspiré du concept autoresearch de Karpathy : évaluer → modifier une variable
> → tester → garder si mieux → rollback sinon.
> Philosophie : **évaluation → amélioration → validation réelle → confirmation humaine → conserver ou rollback**

---

## Principes de conception

1. **Un asset modifié à la fois** — chaque itération ne touche qu'un SKILL.md
2. **Double évaluation** — structure (analyse statique) + effet (test sur prompt réel)
3. **Mécanisme ratchet** — on ne garde que les améliorations, rollback automatique sinon
4. **Évaluateur indépendant** — l'évaluation de l'effet ne se fait pas dans le même contexte que la modification
5. **Humain dans la boucle** — pause et confirmation après chaque skill optimisé

Différence avec un audit de structure pur : on ne regarde pas seulement si le SKILL.md
est bien rédigé, mais si **l'output produit après modification est réellement meilleur**.

---

## Rubric d'évaluation (8 dimensions — 100 points)

### Dimensions structurelles (60 pts) — analyse statique

| # | Dimension | Poids | Critère |
|---|-----------|-------|---------|
| 1 | **Qualité du frontmatter** | 8 | name normalisé, description = quoi + quand + triggers, ≤ 1024 chars |
| 2 | **Clarté du workflow** | 15 | Étapes numérotées, inputs/outputs explicites, séquence exécutable |
| 3 | **Couverture des cas limites** | 10 | Gestion des exceptions, chemins alternatifs, fallback en cas d'échec |
| 4 | **Points de contrôle** | 7 | Confirmations utilisateur aux décisions clés, anti-dérive autonome |
| 5 | **Spécificité des instructions** | 15 | Aucune ambiguïté, paramètres concrets, exemples, directement exécutable |
| 6 | **Intégration des ressources** | 5 | Références GitHub correctes, chemins MCP valides, sources vérifiables |

### Dimensions d'effet (40 pts) — nécessitent un test

| # | Dimension | Poids | Critère |
|---|-----------|-------|---------|
| 7 | **Architecture globale** | 15 | Structure cohérente, non redondante, cohérence avec l'écosystème ECA |
| 8 | **Performance réelle** | 25 | Output sur test prompt : meilleur qu'avant ? Meilleur que sans skill ? |

### Règles de calcul
- Dimensions 1-7 : note 1-10 × poids = score dimensionnel
- Dimension 8 : 2-3 prompts de test, qualité output notée 1-10
- **Score total = Σ(note × poids) / 10**, max 100
- Un skill amélioré doit avoir un score **strictement supérieur** au score initial

### Sur la dimension 8 — test réel
1. Concevoir 2-3 prompts typiques (cas d'usage fréquent, pas edge case)
2. Exécuter : une fois avec skill, une fois sans (baseline)
3. Comparer selon :
   - L'output répond-il à l'intention utilisateur ?
   - Le gain vs baseline est-il visible ?
   - Le skill n'introduit-il pas de dégradation (verbosité, dérive) ?

Si l'exécution d'un sous-agent est impossible, mode **dry_run** :
lire le skill puis simuler mentalement le flux d'exécution sur le prompt de test.
Annoter `dry_run` dans results.tsv — ne jamais sauter la dimension 8 entièrement.

---

## Boucle d'optimisation autonome

### Phase 0 — Initialisation

```
1. Confirmer le périmètre :
   - Tous les skills → scanner /mnt/skills/user/*/SKILL.md
   - Skills ciblés → liste fournie par l'utilisateur
2. Créer une branche git : auto-optimize/YYYYMMDD-HHMM
3. Initialiser results.tsv si inexistant
4. Lire results.tsv pour connaître l'historique des optimisations
```

**Spécificités ECA à garder en tête pendant toute la session :**
- Tous les skills sont en français, pour un usage professionnel juridique/fiscal
- Chaque skill doit respecter : workflow plan→validation→rédaction→vérification
- Les skills critiques ont des contraintes non négociables (hallucination checker, fetch GitHub)
- L'écosystème est interconnecté — modifier un skill peut affecter le routing

### Phase 0.5 — Conception des test prompts

Avant d'évaluer, concevoir les prompts de test. Sans eux, la dimension 8 est non testable.

```
Pour chaque skill :
  1. Lire le SKILL.md — comprendre ce qu'il fait
  2. Concevoir 2-3 prompts couvrant :
     - Cas d'usage principal (happy path)
     - Cas ambigü ou complexe
  3. Sauvegarder dans skill-dir/test-prompts.json :
     [
       {"id": 1, "prompt": "...", "expected": "description courte de l'output attendu"},
       {"id": 2, "prompt": "...", "expected": "..."}
     ]
```

Présenter tous les prompts de test à l'utilisateur. **Attendre confirmation avant d'évaluer.**

### Phase 1 — Évaluation baseline

```
Pour chaque skill dans le périmètre :

  # Évaluation structurelle (contexte principal)
  1. Lire le SKILL.md en entier
  2. Scorer les dimensions 1-7 avec justification courte

  # Évaluation d'effet (contexte indépendant ou dry_run)
  3. Pour chaque test prompt, comparer output avec/sans skill
  4. Scorer la dimension 8

  # Consolidation
  5. Calculer le score pondéré total
  6. Enregistrer dans results.tsv
```

Après la baseline, présenter le tableau de scoring :

```
┌──────────────────────────────┬───────┬─────────────────┬─────────────────┐
│ Skill                        │ Score │ Faiblesse struct │ Faiblesse effet │
├──────────────────────────────┼───────┼─────────────────┼─────────────────┤
│ router-eca                   │ 72    │ cas limites      │ cas ambigü      │
│ calcul-plus-value            │ 78    │ spécificité      │ baseline proche │
└──────────────────────────────┴───────┴─────────────────┴─────────────────┘
```

**Pause — attendre confirmation avant d'entrer dans la boucle d'optimisation.**

### Phase 2 — Boucle d'optimisation

Trier par score croissant, commencer par les plus faibles.

```
Pour chaque skill :
  round = 0
  while round < MAX_ROUNDS (défaut 3) :
    round += 1

    # Étape 1 : Diagnostic
    Identifier la dimension avec le score le plus faible

    # Étape 2 : Proposition d'amélioration
    Générer 1 amélioration ciblée sur cette dimension :
      - Ce qui change (paragraphe/ligne précis)
      - Pourquoi (critère rubric correspondant)
      - Gain attendu (estimation)

    # Étape 3 : Exécution
    Modifier le SKILL.md
    git add + commit ("optimize {skill}: {résumé amélioration}")

    # Étape 4 : Réévaluation
    - Structure : re-scorer les dimensions 1-7
    - Effet : relancer test prompts (sous-agent ou dry_run indépendant)

    # Étape 5 : Décision
    si nouveau score > ancien score :
      status = "keep", mettre à jour le score de référence
    sinon :
      status = "revert"
      git revert HEAD (nouveau commit de rollback — ne pas utiliser reset --hard)
      noter la tentative dans results.tsv
      break  # ce skill a atteint son plafond, passer au suivant

    # Étape 6 : Log
    Ajouter ligne dans results.tsv

  # === Point de contrôle humain après chaque skill ===
  Présenter :
    - git diff (avant/après)
    - Évolution du score (quelles dimensions)
    - Comparaison output test (si disponible)
  Attendre confirmation. Si "non", rollback complet du skill.
```

### Phase 2.5 — Réécriture exploratoire (optionnel)

Quand le hill-climbing bloque 2 skills consécutifs dès le round 1 :

```
1. Choisir le skill le plus bloqué
2. git stash de la version optimale actuelle
3. Réécrire de zéro le SKILL.md (restructuration complète, pas micro-ajustement)
4. Réévaluer
5. si réécriture > stash : adopter la réécriture
   sinon : git stash pop
```

Résout le problème des optima locaux du hill-climbing.
**Obligatoire d'obtenir l'accord de l'utilisateur avant d'exécuter.**

### Phase 3 — Rapport de synthèse

```
## Rapport d'optimisation Darwin.skill

### Vue d'ensemble
- Skills optimisés : N
- Expérimentations totales : M
- Améliorations conservées : X (Y%)
- Rollbacks : Z
- Tests réels : A | Dry runs : B

### Évolution des scores
┌──────────────────────────┬────────┬────────┬────────┐
│ Skill                    │ Avant  │ Après  │ Δ      │
├──────────────────────────┼────────┼────────┼────────┤
│ router-eca               │ 72     │ 83     │ +11    │
└──────────────────────────┴────────┴────────┴────────┘

### Principales améliorations
1. [skill-A] ...
2. [skill-B] ...
```

---

## Format results.tsv

```tsv
timestamp	commit	skill	old_score	new_score	status	dimension	note	eval_mode
2026-04-20T10:00	baseline	router-eca	-	72	baseline	-	évaluation initiale	dry_run
2026-04-20T10:05	a1b2c3d	router-eca	72	79	keep	cas limites	ajout fallback Casus	dry_run
2026-04-20T10:10	b2c3d4e	router-eca	79	77	revert	spécificité	sur-spécification	dry_run
```

Colonnes : `eval_mode` = `full_test` (sous-agent) ou `dry_run` (simulation mentale).
Emplacement : `.claude/skills/auto-optimize-results.tsv`

---

## Catalogue de stratégies d'optimisation

Par priorité décroissante (ne traiter qu'une priorité par round) :

### P0 — Problèmes d'effet (détectés par test)
- Output dévie de l'intention → vérifier les instructions pour formulations ambiguës
- Skill + dégradation vs baseline → sur-contrainte, simplifier
- Format output non conforme → ajouter template de sortie explicite

### P1 — Problèmes structurels
- Frontmatter sans triggers français → ajouter mots-clés en français
- Pas de structure Phase/Étape → réorganiser en flux linéaire numéroté
- Pas de point de contrôle utilisateur → insérer aux décisions critiques

### P2 — Problèmes de spécificité
- Étape vague ("traiter le document") → préciser : outil, paramètre, format
- Pas de spec input/output → ajouter format, chemin, exemple
- Pas de gestion d'exception → ajouter "si X échoue → Y"

### P3 — Problèmes de lisibilité
- Paragraphes trop longs → découper + tableaux
- Répétitions → fusionner
- Pas de synthèse rapide → ajouter TL;DR ou arbre de décision

---

## Règles contraignantes (non négociables)

1. **Ne pas changer la fonction cœur du skill** — optimiser "comment", pas "quoi"
2. **Pas de nouvelles dépendances externes** — ne pas ajouter de scripts/ressources absent à l'origine
3. **Une dimension modifiée par round** — impossible de localiser la cause si plusieurs changements simultanés
4. **Taille raisonnable** — le SKILL.md optimisé ne doit pas dépasser 150% de la taille originale
5. **Tout doit être rollbackable** — utiliser git revert, jamais reset --hard
6. **Indépendance de l'évaluateur** — la dimension 8 ne peut jamais être évaluée dans le même contexte que la modification
7. **Respecter l'écosystème ECA** — charte graphique, workflow validation, MCP Légifrance obligatoire, hallucination-checker

---


## Ressources et URLs

### Repository ECA EXPERTISE
Base GitHub : `https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/`
Skills : `/mnt/skills/user/[skill-name]/SKILL.md`
Résultats : `.claude/skills/auto-optimize-results.tsv`

### Vérification des skills via MCP
Pour vérifier si une référence dans un skill est correcte, utiliser MCP Légifrance :
```
rechercher_code(code_name="Code général des impôts", search="[article]")
rechercher_jurisprudence_administrative(search="[numéro]")
```

### Fetch shared avant toute session
```
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md")
```

## Modes d'utilisation

### Optimisation complète (recommandé en première utilisation)
```
"Optimise tous mes skills" / "Lance darwin sur mes skills"
→ Flux complet Phase 0 à Phase 3
→ Conseil : commencer par la baseline, cibler les 3-5 skills avec le score le plus faible
```

### Optimisation ciblée
```
"Améliore le skill router-eca" / "Darwin sur calcul-plus-value"
→ Phases 0.5 à 2 sur le skill ciblé uniquement
```

### Évaluation seule (sans modification)
```
"Score mes skills" / "Évalue la qualité de mes skills sans modifier"
→ Phases 0.5 à 1 uniquement — produit le tableau de scoring, aucune modification
```

### Historique
```
"Montre l'historique des optimisations"
→ Lecture et présentation de results.tsv
```

---

## Template de rapport rapide (si une seule optimisation demandée)

```
RAPPORT DARWIN — [skill optimisé] — [date]

I. SCORE BASELINE : [N]/100
   Dimension faible : [dimension] ([score]/10, poids [N])

II. MODIFICATION APPLIQUÉE
   Fichier : SKILL.md
   Section modifiée : [section]
   Nature : [ajout / remplacement / suppression]
   Justification rubric : [critère]

III. SCORE POST-MODIFICATION : [N]/100
   Delta : [+/-N]
   Verdict : ✅ keep / 🔄 revert

IV. PROCHAINES ÉTAPES
   → Confirmer avec Yoann (`git diff` si demandé)
   → Passer au skill suivant
   → [Si revert : analyser la cause avant nouvelle tentative]
```

Niveau de risque d'une optimisation :
- 🔴 Réécriture complète : rollback impératif si score baisse
- 🟠 Restructuration : vérifier que le sens est conservé
- 🟢 Ajout ciblé : risque faible, vérifier la cohérence
