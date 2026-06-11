# CLAUDE.md — Manifeste d'orchestration ECA EXPERTISE

> Ce fichier est un index de routage. Il ne contient aucune donnée métier.
> Chaque information vit à un seul endroit ; ce manifeste y pointe.

---

## 1. Carte de l'écosystème (14 skills + 1 référentiel)

| Skill | Rôle en une ligne |
|-------|------------------|
| `router-eca` | Point d'entrée : qualifie la demande, active le bon skill, reformule si ambigu |
| `consultation-juridique` | Analyse de fond juridique ou fiscale |
| `redaction-acte` | Rédaction/modification d'actes de droit des sociétés ou civil |
| `analyse-contrat` | Relecture, sécurisation, rédaction contractuelle |
| `calcul-plus-value` | Calcul PV immobilière, mobilière, professionnelle, IS, report/sursis |
| `contentieux-fiscal` | Défense fiscale : réponse à PR, réclamation, CID, TA/CAA/CE |
| `diagnostic-transmission` | Bilan patrimonial exploratoire avant structuration |
| `patrimonial-structuring` | Démembrement, quasi-usufruit, régimes matrimoniaux, successions |
| `due-diligence-juridique` | Audit d'acquisition/cession (juridique, fiscal, social) |
| `veille-juridique` | Synthèse de textes législatifs/réglementaires nouveaux |
| `note-information-client` | Communication vulgarisée post-analyse pour client non-juriste |
| `positions-eca` | Boucle rétroactive : consulte Notion AVANT, propose ajout APRÈS |
| `legal-hallucination-checker` | Vérification MCP Légifrance de TOUTES les références citées |
| `darwin-skill` | Optimiseur autonome de SKILL.md (scoring, hill-climbing, git) |
| `shared` | Référentiel partagé : charte graphique, Notion, équipe, méthode DOCX, AUREP |

---

## 2. Chaîne d'activation systémique

Tout livrable juridique/fiscal suit cette séquence :

```
1. positions-eca     → Chercher position existante dans Notion (DB f201a44e)
2. shared            → Fetch GitHub : charte, méthode DOCX, bases Notion, AUREP
3. sources-legales   → Fetch GitHub : taux, seuils, articles, règles vérifiées
4. Légifrance MCP    → Vérifier TOUTES les références avant citation
5. [skill métier]    → Exécuter le livrable (plan → validation → rédaction)
6. hallucination-checker → Vérifier TOUTES les références citées post-rédaction
7. Proposition Notion → Ajouter nouvelle position si consultation tranchée
```

---

## 3. Sources de vérité (un seul endroit par type de donnée)

| Donnée | Source canonique unique | Emplacement |
|--------|----------------------|-------------|
| Taux fiscaux, seuils, articles CGI, règles vérifiées | `sources-legales.md` | `skills/shared/sources-legales.md` sur GitHub |
| Charte graphique, méthode DOCX, bases Notion, équipe ECA, AUREP URLs | `shared/SKILL.md` | `skills-user/shared/SKILL.md` sur GitHub |
| Positions ECA validées | Notion | DB `f201a44e` (veille) · DB `cadd1870` (consultations) |
| Modèles d'actes | GitHub | Dossiers `01_Statuts` à `11_Consultations` |
| Modules AUREP | GitHub | `aurep/` (M5, M8, M10 + Royal Formation 2026 PDF) |
| Prompt-codes ECA | GitHub | `skills-user/prompt-codes-eca.md` |

---

## 4. Règles transverses (applicables à TOUS les skills)

Ces règles vivent dans les mémoires Claude (userMemories) car elles doivent être lues
même sans fetch GitHub. Elles ne sont PAS dupliquées dans les skills.

- **Planning mode obligatoire** : plan structuré → validation Yoann → exécution
- **Vérification Légifrance systématique** : jamais de référence de mémoire
- **Vérification seuils fiscaux** : jamais de chiffre de mémoire → BOFiP/web_search
- **Information Yoann → vérification** : toute position fournie en conversation = vérifier avant d'intégrer
- **Truncation rule** : signaler immédiatement toute lecture partielle
- **Hallucination checker** : obligatoire après TOUT livrable, sans exception
- **SIREN reflex** : auto-lookup API entreprises dès qu'un SIREN apparaît
- **Casus = base documentaire** : construire dessus, ne pas redoublonner

---

## 5. Anti-patterns à éviter

- ❌ Ne jamais dupliquer un taux ou un seuil dans un skill → pointer vers `sources-legales.md`
- ❌ Ne jamais dupliquer la charte graphique → pointer vers `shared/SKILL.md`
- ❌ Ne jamais figer une position jurisprudentielle comme "absolue" sans arrêt CE
- ❌ Ne jamais rédiger un acte ECA from scratch → méthode ref_sas/ref_sci
- ❌ Ne jamais livrer sans rapport hallucination-checker

---

*Dernière mise à jour : 10/06/2026 — Migration vers manifeste d'orchestration pur.*
