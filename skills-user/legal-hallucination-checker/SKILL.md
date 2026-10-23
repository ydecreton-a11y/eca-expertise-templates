---
name: "legal-hallucination-checker"
description: "Vérification bloquante de 100 % des références juridiques (articles, décisions, BOFiP, textes) en fin de tout livrable juridique ou fiscal ECA EXPERTISE, par recoupement Légifrance, LibreJustice, Legal Data Hunter, Pourvoi et OpenEU selon la compétence de chaque outil ; contrôle de l'existence, de la version applicable, du contenu, de la portée et du sort procédural. Déclencher automatiquement en fin de livrable, et sur : vérifie les références, checker, hallucination, contrôle des citations, est-ce que cet arrêt existe, cet article est-il en vigueur."
---

# Legal Hallucination Checker — ECA EXPERTISE

Ce skill existe parce qu'un modèle de langage peut produire des références
juridiques plausibles mais fausses — numéro de décision inversé, article
inexistant, jurisprudence composite. Dans un contexte professionnel, une
référence erronée citée à un client ou devant un tribunal est une faute.
Une décision réelle mais cassée, ou un arrêt d'espèce présenté comme un
principe, l'est tout autant. Ce skill est le filet de sécurité final.

---

## Règle de départ — Références à ne pas vérifier

Les références suivantes sont définitivement vérifiées et ne nécessitent
pas de re-vérification :

| Référence | Statut |
|-----------|--------|
| TA Bordeaux n°2301446 du 19/12/2024 | ✅ Existe — ⚠️ NE PAS en déduire une règle : JP divergente depuis (TA Bordeaux 13/11/2025 n°2304900, TA Paris 13/02/2025 n°2212919) |
| Cons. const. n°2016-538 QPC 22/04/2016 | ✅ Vérifié — Art. 200 A 2 ter |
| Art. 150-0 B ter CGI | ✅ En vigueur |
| Art. 200 A, 2 ter CGI | ✅ En vigueur |

Pour toute autre référence, appliquer le workflow ci-dessous.

---

## Matrice de compétence des outils — À LIRE AVANT TOUTE VÉRIFICATION

Chaque outil ne couvre qu'une partie des sources. Un échec de recherche
n'a de valeur probante que sur un outil **compétent** pour le type de
référence. Interroger Pourvoi sur un arrêt du Conseil d'État ne prouve rien.

| Type de référence | Légifrance | LibreJustice | Legal Data Hunter | Pourvoi |
|---|---|---|---|---|
| Article de code, loi, ordonnance, décret | ✅ | ✅ | ✅ | ❌ |
| BOFiP (BOI-...) | ❌ | ✅ (`get_norm`, `text_id`) | ✅ (doctrine) | ❌ |
| Cass. (toutes chambres) | ✅ | ✅ | ✅ | ✅ |
| Cour d'appel | ✅ (partiel) | ✅ | ✅ | ✅ |
| CJUE / Tribunal de l'Union, actes de l'Union (CELEX) | ❌ (→ OpenEU, compétent) | ✅ | ✅ | ✅ (décisions) |
| CE, CAA, TA | ✅ (TA partiel) | ✅ | ✅ | ❌ |
| Cons. const. | ✅ | ✅ | ✅ | ❌ |
| TJ, tribunal de commerce / TAE | ❌ | ✅ | variable | ❌ |
| CEDH | ❌ | ✅ | ✅ (CoE) | ❌ |

**Conséquence pratique — fiscal :** le contentieux IS / IR / TVA / pénalités
relève du juge administratif → Pourvoi est hors champ. Pourvoi ne sert en
fiscal que pour le contentieux judiciaire (droits d'enregistrement, IFI,
droits de mutation à titre gratuit).

---

## Workflow de vérification en 5 phases

### Phase 1 — Extraction des références

Identifier dans le livrable toutes les références du format :

| Pattern | Type | Exemples |
|---------|------|---------|
| `Art. [N] CGI` / `Art. [N] C. civ.` / `Art. L[N] LPF` | Article de code | Art. 150-0 B ter CGI |
| `Loi n°[AAAA-NNN] du [date]` | Loi | Loi n°78-17 du 6 janvier 1978 |
| `Ord. n°[AAAA-NNN]` | Ordonnance | |
| `CE [date], n°[N]` | Jurisprudence CE | CE 27/11/2020, n°425986 |
| `Cass. [ch.], [date], n°[NN-NN.NNN]` | Jurisprudence Cass. | Cass. com. 12/02/2025 n°23-11.410 |
| `CA [ville], [date], RG n°[NN/NNNNN]` | Cour d'appel | CA Colmar, 1er avr. 2026, RG n°24/04164 |
| `CJUE, [date], aff. C-[N]/[AA]` / `Trib. UE, aff. T-[N]/[AA]` | Jurisprudence UE | aff. C-292/00 |
| `ECLI:[...]` | Identifiant européen | ECLI:FR:CCASS:2006:CO00559 |
| `BOI-[identifiant]` | BOFiP | BOI-RPPM-PVBMI-30-10-60 |
| `Cons. const. n°[N]-[N] QPC` | Décision CC | n°2016-538 QPC |
| `TA [ville], [date], n°[N]` | Tribunal administratif | TA Bordeaux n°2301446 |

Pour chaque référence jurisprudentielle, relever aussi **ce que le livrable
lui fait dire** (solution, portée, « jurisprudence constante », « principe
posé par... ») : c'est ce contenu qui sera contrôlé en Phases 2bis et 2ter.

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

### Phase 2bis — Vérification croisée via LibreJustice, Legal Data Hunter et Pourvoi

**Obligatoire pour toute référence non confirmée en Phase 2, et recommandé
en confirmation croisée pour toute référence à enjeu (🔴 critique du
référentiel `shared`).** N'interroger que les outils compétents (matrice
ci-dessus).

**LibreJustice :**
```
# Article de code / texte
search_norms(query="[objet de l'article]", code="[slug du code, ex: code-general-des-impots]")
get_norm(code="[slug]", article="[clé article en minuscules, ex: 150-0-b-ter ou l761-1]", as_of="[AAAA-MM-JJ si version antérieure applicable]")

# BOFiP
get_norm(text_id="BOI-[identifiant]")

# Jurisprudence — recherche sémantique, filtrable (domaine, siège, date, article cité)
search_decisions(query="[n° ou question de droit]", mode="reference")   # référence précise
search_decisions(query="[question de droit]", legal_article=["[slug-code]|[n° article]"])
get_decision(url="[url renvoyée par search_decisions]")
```
`get_decision` renvoie notamment `case_chronology` (décisions antérieures ET
postérieures de la même affaire, avec leur solution) et `official_url`
(preuve d'authenticité). Ces deux champs servent en Phase 2ter.

**Legal Data Hunter :**
```
# Résolution directe d'une référence précise (articles, décisions, BOFiP) — à tenter en premier
resolve_reference(reference="[art. N / n° décision / BOI-...]", hint_country="FR", hint_type="legislation")
resolve_reference(reference="[n° pourvoi ou d'affaire]", hint_country="FR", hint_type="case_law")

# Recherche large si resolve_reference échoue (couvre aussi la doctrine BOFiP)
search(query="[sujet]", namespace="doctrine", country=["FR"])
```

**Pourvoi (Cass., CA, CJUE / Tribunal UE uniquement) :**
```
# Retrouver la décision par sa référence — à tenter en premier
trouver_decision(reference="[n° pourvoi 25-11.362 / RG 22/01717 / C-292/00 / ECLI]")

# Contrôler le contenu : la fiche est un résumé IA, insuffisant pour valider
# une solution ou une citation → lire le texte officiel
lire_decision(id="[id]", contenu="dispositif")
lire_decision(id="[id]", contenu="motivations")

# Si la référence est introuvable par numéro : recherche par question de droit
rechercher_jurisprudence(question="[question de droit]", contexte="[faits anonymisés]", depuis="[date - 1 mois]", jusqu_au="[date + 1 mois]")
```
Apport spécifique de Pourvoi : les champs **Question tranchée / Solution /
Portée** de la fiche permettent de détecter une portée déformée (tenant /
rejetant inversés, arrêt d'espèce présenté comme principe). Ces champs
sont un signal d'alerte, pas une preuve : toute divergence se tranche sur
le texte (`lire_decision`, `contenu="motivations"`).

**Limite connue de Pourvoi :** `rechercher_jurisprudence` ne renvoie que les
décisions jugées comme tranchant la question ; le filtre peut être sévère
(résultat vide ou d'une seule décision sur une question abondamment jugée).
Une absence de résultat en recherche thématique ne prouve rien — seul
`trouver_decision` a valeur de vérification d'existence.

**Règle de vérification croisée — CRITIQUE :**
Une référence n'est déclarée ⛔ HALLUCINATION ou ⚪ NON_CONFIRMÉ qu'après
échec concordant sur **tous les outils compétents** pour ce type de
référence (matrice de compétence) — au minimum trois. Un résultat positif
sur un seul outil suffit à confirmer l'existence ; en cas de désaccord
entre outils sur le contenu ou la portée, signaler explicitement la
divergence dans le rapport plutôt que de trancher arbitrairement.

---

### Phase 2ter — Contrôle du sort procédural et de la portée

Une décision qui existe peut néanmoins ne plus faire autorité.

**Obligatoire pour :**
- toute décision de cour d'appel citée (risque de cassation) ;
- tout arrêt de Cassation de cassation avec renvoi (vérifier la décision de la cour de renvoi) ;
- toute décision de juridiction du fond administrative (CAA, TA) citée comme autorité (risque d'annulation ou de réformation en CE / CAA).

**Outils :**
```
# Ordre judiciaire (CA, Cass.) — outil dédié
parcours_procedural(id="[id Pourvoi]")

# Toutes juridictions, y compris ordre administratif — confirmation croisée
get_decision(url="[url LibreJustice]")  → lire case_chronology
```

**Contrôle de portée :**
- Une décision de cour d'appel, de TA ou de CAA ne peut pas être présentée
  comme « jurisprudence constante » ou « principe » : la qualifier
  d'« application d'espèce » ou d'« illustration ».
- Un arrêt de Cassation non publié (ni Bulletin, ni Rapport, ni Lettre de
  chambre) a une autorité moindre : ne pas le présenter comme arrêt de
  principe. Vérifier via le filtre `publiees_seulement` de Pourvoi ou le
  filtre `publication` de LibreJustice.
- Pour toute référence 🔴 critique, rechercher un éventuel revirement :
  `rechercher_jurisprudence(question=..., depuis="[date de la décision citée]", ordre="date")`
  (Pourvoi, ordre judiciaire) ou `search_decisions(..., date_from=..., sort="date_desc")`
  (LibreJustice, toutes juridictions).

**Effet sur la classification :**
- Décision cassée, annulée ou infirmée sur le point cité, présentée comme
  faisant autorité → 🔴 SUBSTANTIELLEMENT_ERRONÉ.
- Arrêt d'espèce ou décision du fond présentée comme principe → 🟠
  PARTIELLEMENT_EXACT, avec reformulation proposée.
- Revirement postérieur identifié → 🔴 SUBSTANTIELLEMENT_ERRONÉ si le
  livrable s'appuie sur la solution abandonnée.

---

### Phase 3 — Classification des résultats

| Score | Statut | Signification |
|-------|--------|---------------|
| 100 | ✅ VÉRIFIÉ_EXACT | Référence exacte, en vigueur, contenu conforme, sort procédural vérifié |
| 80-99 | 🟡 VÉRIFIÉ_MINEUR | Existe mais erreur mineure (coquille, date approx.) |
| 50-79 | 🟠 PARTIELLEMENT_EXACT | Existe mais contenu ou portée partiellement inexact (ex. arrêt d'espèce présenté comme principe) |
| 20-49 | 🔴 SUBSTANTIELLEMENT_ERRONÉ | Erreurs majeures sur le contenu ou la portée, décision cassée / infirmée / abandonnée par revirement |
| 0-19 | ⛔ HALLUCINATION | Inexistant ou totalement fictif |
| N/A | ⚪ NON_CONFIRMÉ | Non trouvé sur aucun des outils compétents — vérification manuelle recommandée |

**Types d'erreurs fréquentes à détecter :**
- Numéro de décision CE ou Cass. inversé (ex: 425986 → 425689)
- Article CGI inexistant ou abrogé
- Date de jurisprudence incorrecte
- Portée de l'arrêt déformée (tenant/rejetant inversés)
- Décision d'appel citée alors qu'elle a été cassée
- Arrêt d'espèce ou inédit présenté comme jurisprudence établie
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
Erreurs majeures : N | Hallucinations : N | Non confirmées : N
Sort procédural contrôlé : N décisions | Cassées / infirmées / renversées : N

DÉTAIL PAR RÉFÉRENCE
[Référence] → [Statut] → [Outils ayant confirmé] → [Sort procédural] → [Observation]

RÉFÉRENCES À CORRIGER AVANT REMISE
[Liste des corrections prioritaires avec texte corrigé proposé]

RÉFÉRENCES NON CONFIRMÉES (vérification manuelle recommandée)
[Liste avec outils interrogés et raison de la non-confirmation]
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

Se déclenche automatiquement à la fin de **tout** livrable juridique ou fiscal
(socle § 9), quel que soit le skill, y compris une réponse conversationnelle
qui cite une référence. Couvre 100 % des références, sans exception pour les
articles « connus ». Il fait partie du workflow de remise : aucun livrable
n'est présenté comme final avant le rapport.

Ajouter au contrôle : **version applicable** (le texte cité est-il celui en
vigueur à la date du fait générateur ? s'il a changé depuis, le signaler) et
**références internes aux skills** (un skill peut contenir une référence
erronée — exemple corrigé : l'« art. 150-0 F ter » inexistant, la CDHR étant à
l'art. 224 CGI).
