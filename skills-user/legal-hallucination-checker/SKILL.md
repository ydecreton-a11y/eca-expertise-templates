---
name: legal-hallucination-checker
description: >
  Vérification systématique des références juridiques françaises. Déclencher
  après TOUT livrable juridique ou fiscal (consultation, acte, calcul PV,
  analyse contrat, veille, DD). Détecte : références inexistantes, numéros
  erronés, citations déformées, textes abrogés, jurisprudences fictives.
  Fonctionne via MCP Légifrance (OpenLegi). Ne pas attendre que l'utilisateur
  le demande — ce skill doit s'auto-déclencher en fin de tout livrable.
---

# Legal Hallucination Checker — ECA EXPERTISE

Ce skill existe parce qu'un modèle de langage peut produire des références
juridiques plausibles mais fausses — numéro de décision inversé, article
inexistant, jurisprudence composite. Dans un contexte professionnel, une
référence erronée citée à un client ou devant un tribunal est une faute.
Ce skill est le filet de sécurité final.

---

## Règle de départ — Références à ne pas vérifier

Les références suivantes sont définitivement vérifiées et ne nécessitent
pas de re-vérification :

| Référence | Statut |
|-----------|--------|
| TA Bordeaux n°2301446 du 19/12/2024 | ✅ Vérifié — 150-0 B ter + quotient |
| Cons. const. n°2016-538 QPC 22/04/2016 | ✅ Vérifié — Art. 200 A 2 ter |
| Art. 150-0 B ter CGI | ✅ En vigueur |
| Art. 200 A, 2 ter CGI | ✅ En vigueur |

Pour toute autre référence, appliquer le workflow ci-dessous.

---

## Workflow de vérification en 4 phases

### Phase 1 — Extraction des références

Identifier dans le livrable toutes les références du format :

| Pattern | Type | Exemples |
|---------|------|---------| 
| `Art. [N] CGI` / `Art. [N] C. civ.` / `Art. L[N] LPF` | Article de code | Art. 150-0 B ter CGI |
| `Loi n°[AAAA-NNN] du [date]` | Loi | Loi n°78-17 du 6 janvier 1978 |
| `Ord. n°[AAAA-NNN]` | Ordonnance | |
| `CE [date], n°[N]` | Jurisprudence CE | CE 27/11/2020, n°425986 |
| `Cass. [ch.], [date], n°[N]` | Jurisprudence Cass. | Cass. com. 12/02/2025 n°23-11410 |
| `CA [ville], [date], n°[N]` | Cour d'appel | |
| `BOI-[identifiant]` | BOFiP | BOI-RPPM-PVBMI-30-10-60 |
| `Cons. const. n°[N]-[N] QPC` | Décision CC | n°2016-538 QPC |
| `TA [ville], [date], n°[N]` | Tribunal administratif | TA Bordeaux n°2301446 |

---

### Phase 2 — Vérification via MCP Légifrance

Pour chaque référence extraite :

**Articles de code :**
```
rechercher_code(code_name="[Code]", search="[numéro article]", champ="NUM_ARTICLE")
```
Vérifier : article existe, alinéa cité correspond, article en vigueur (non abrogé).

**Jurisprudence judiciaire :**
```
rechercher_jurisprudence_judiciaire(search="[numéro pourvoi]", champ="NUM_AFFAIRE")
```

**Jurisprudence administrative (CE, CAA, TA) :**
```
rechercher_jurisprudence_administrative(search="[numéro]", champ="NUM_AFFAIRE")
```

**Décisions constitutionnelles :**
```
rechercher_decisions_constitutionnelles(search="[numéro décision]")
```

**Lois et ordonnances :**
```
recherche_journal_officiel(search="[numéro ou titre]", text_types=["LOI"])
```

**Règle de robustesse — CRITIQUE :**
Avant de conclure à l'inexistence, tenter **au minimum 2 stratégies différentes** :
1. Recherche par numéro exact
2. Recherche par mots-clés du sujet + date approximative
3. Si toujours non trouvé → signaler "non trouvé" (≠ "inexistant")

**Une référence non trouvée via MCP ≠ référence inexistante.**
Le MCP peut avoir des lacunes sur certaines décisions récentes ou tribunaux de première instance.
En cas de doute persistant, indiquer : "Non confirmée via MCP — à vérifier manuellement sur Légifrance.fr"

**Règle anti-faux positif pour les TA :**
Les décisions de TA ne sont pas toutes indexées dans le MCP Légifrance.
Si une décision de TA n'est pas trouvée → signaler "Non trouvée via MCP — recherche manuelle recommandée"
sans conclure à une hallucination.

---

### Phase 3 — Classification des résultats

| Score | Statut | Signification |
|-------|--------|---------------|
| 100 | ✅ VÉRIFIÉ_EXACT | Référence exacte, en vigueur, contenu conforme |
| 80-99 | 🟡 VÉRIFIÉ_MINEUR | Existe mais erreur mineure (coquille, date approx.) |
| 50-79 | 🟠 PARTIELLEMENT_EXACT | Existe mais contenu partiellement inexact |
| 20-49 | 🔴 SUBSTANTIELLEMENT_ERRONÉ | Erreurs majeures sur le contenu ou la portée |
| 0-19 | ⛔ HALLUCINATION | Inexistant ou totalement fictif |
| N/A | ⚪ NON_CONFIRMÉ | Non trouvé via MCP — vérification manuelle recommandée |

**Types d'erreurs fréquentes à détecter :**
- Numéro de décision CE ou Cass. inversé (ex: 425986 → 425689)
- Article CGI inexistant ou abrogé
- Date de jurisprudence incorrecte
- Portée de l'arrêt déformée (tenant/rejetant inversés)
- Référence BOFiP périmée ou modifiée
- Numéros de QPC ou SIREN transposés

---

### Phase 4 — Rapport de vérification

```
RAPPORT LEGAL HALLUCINATION CHECKER
Date : [ISO]
Livrable vérifié : [titre]
Score global : [N]/100

SYNTHÈSE
Total références : N | Exactes : N | Erreurs mineures : N
Erreurs majeures : N | Hallucinations : N | Non confirmées MCP : N

DÉTAIL PAR RÉFÉRENCE
[Référence] → [Statut] → [Observation]

RÉFÉRENCES À CORRIGER AVANT REMISE
[Liste des corrections prioritaires avec texte corrigé proposé]

RÉFÉRENCES NON CONFIRMÉES (vérification manuelle recommandée)
[Liste avec raison de la non-confirmation]
```

Le rapport est produit en fin de livrable, avant remise au client.
Si aucune correction n'est nécessaire : "Toutes les références vérifiées ✅"

---


## Point de contrôle — Avant livraison

Ne pas livrer le livrable si le rapport contient des ⛔ HALLUCINATION non corrigées.
Attendre validation de Yoann avant livraison si le score global < 70/100.

```
if score < 70:
    → NE PAS livrer
    → Corriger les hallucinations identifiées
    → Re-déclencher le checker sur la version corrigée
    → Attendre confirmation de Yoann
```

## Règle d'auto-déclenchement

Ce skill doit se déclencher automatiquement à la fin de :
- consultation-juridique
- analyse-contrat
- redaction-acte
- calcul-plus-value
- diagnostic-transmission
- due-diligence-juridique
- veille-juridique
- contentieux-fiscal
- patrimonial-structuring

Il ne doit pas être déclenché manuellement — il fait partie du workflow
de remise, pas d'une étape optionnelle.
