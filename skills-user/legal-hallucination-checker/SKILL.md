---
name: legal-hallucination-checker
description: "Vérification bloquante de 100 % des références juridiques (articles, décisions, BOFiP, textes) en fin de tout livrable juridique ou fiscal ECA EXPERTISE, par recoupement Légifrance, LibreJustice, Casus, Legal Data Hunter, Pourvoi et OpenEU selon la compétence de chaque outil ; contrôle de l'existence, de la version applicable, du contenu, de la fidélité des citations (guillemets, pincites, signaux), de l'adéquation du fondement (l'article de code, le texte ou le BOI pose-t-il bien la règle qu'on lui attribue), de la portée et du sort procédural. Déclencher automatiquement en fin de livrable, et sur : vérifie les références, checker, hallucination, contrôle des citations, est-ce que cet arrêt existe, cet article est-il en vigueur."
---

# Legal Hallucination Checker — ECA EXPERTISE

Ce skill existe parce qu'un modèle de langage peut produire des références
juridiques plausibles mais fausses — numéro de décision inversé, article
inexistant, jurisprudence composite. Dans un contexte professionnel, une
référence erronée citée à un client ou devant un tribunal est une faute.
Une décision réelle mais cassée, ou un arrêt d'espèce présenté comme un
principe, l'est tout autant. Ce skill est le filet de sécurité final.

---

## Règle de départ — Références déjà contrôlées

Aucune référence n'est dispensée de vérification. Celles ci-dessous ont déjà été
contrôlées : leur **existence** est acquise, mais leur **version applicable** et
leur **contenu** se revérifient à chaque usage, car un texte en vigueur
aujourd'hui peut être modifié par la prochaine loi de finances (suivi : index
des références du dépôt et `maintenance-skills`).

| Référence | Acquis | À revérifier à chaque usage |
|-----------|--------|-----------------------------|
| TA Bordeaux n°2301446 du 19/12/2024 | Existe (LibreJustice ; point 8 lu le 29/10/2026). Jugement inédit, rejet : les plus-values du I de l'art. 150-0 B ter relèvent du taux spécifique du 2 ter de l'art. 200 A et non du barème de l'art. 197, d'où l'exclusion du quotient (III de l'art. 163-0 A) | ⚠️ Décision de TA : application d'espèce, jamais une règle générale. Décision convergente identifiée : TA Paris 17/12/2025 n°2413796 (même raisonnement, quotient écarté). Les deux décisions longtemps citées comme « divergentes » (TA Bordeaux 13/11/2025 n°2304900 ; TA Paris 13/02/2025 n°2212919) portent sur le quotient appliqué aux gains d'acquisition d'actions gratuites imposés au barème (art. 80 quaterdecies) : elles ne statuent pas sur l'art. 150-0 B ter et ne sont pas des décisions contraires (textes lus le 29/10/2026) ; ne pas les présenter comme telles. Rechercher toute décision postérieure (CAA, CE) |
| Cons. const. n°2016-538 QPC 22/04/2016 (Époux M. D.) | Existe (Légifrance CONSTEXT000032453721 ; texte lu le 29/10/2026). Porte sur les 1 ter et 1 quater de l'art. 150-0 D (exclusion de l'abattement pour durée de détention des plus-values mobilières placées en report avant le 01/01/2013) : conformité sous les réserves des cons. 11 et 15. Ne porte ni sur l'art. 150-0 B ter ni sur le 2 ter de l'art. 200 A | Version de l'art. 150-0 D applicable. Citer les réserves (cons. 11 : coefficient d'érosion monétaire ; cons. 15 : règles d'assiette et de taux applicables au fait générateur pour une plus-value en report obligatoire), jamais « conforme » sans réserve ni « régime du report validé » |
| Art. 150-0 B ter CGI | Existe | Version à la date de l'apport |
| Art. 200 A, 2 ter CGI | Existe | Version à la date du fait générateur |

Pour toute autre référence, appliquer le workflow ci-dessous.

---

## Matrice de compétence des outils — À LIRE AVANT TOUTE VÉRIFICATION

Chaque outil ne couvre qu'une partie des sources. Un échec de recherche
n'a de valeur probante que sur un outil **compétent** pour le type de
référence. Interroger Pourvoi sur un arrêt du Conseil d'État ne prouve rien.

| Type de référence | Légifrance | LibreJustice | Legal Data Hunter | Pourvoi | Casus |
|---|---|---|---|---|---|
| Article de code, loi, ordonnance, décret | ✅ | ✅ | ✅ | ❌ | ✅ codes (lois et décrets non codifiés : « hors corpus ») |
| BOFiP (BOI-...) | ❌ | ✅ (`get_norm`, `text_id`) | ✅ (doctrine) | ❌ | ✅ (une seule version par document) |
| Cass. (toutes chambres) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cour d'appel | ✅ (partiel) | ✅ | ✅ | ✅ | ✅ |
| CJUE / Tribunal de l'Union, actes de l'Union (CELEX) | ❌ (→ OpenEU, compétent) | ✅ | ✅ | ✅ (décisions) | ✅ (couverture plus courte ; actes de l'Union en texte initial non consolidé) |
| CE, CAA, TA | ✅ (TA partiel) | ✅ | ✅ | ❌ | ✅ (TA depuis 2022) |
| Cons. const. | ✅ (décisions jointes : voir note) | ✅ | ✅ | ❌ | ✅ |
| TJ, tribunal de commerce / TAE | ❌ | ✅ | variable | ❌ | TJ ✅ ; tribunal de commerce ❌ |
| CEDH | ❌ | ✅ | ✅ (CoE) | ❌ | ✅ (couverture plus courte) |

**Note — décisions jointes du Conseil constitutionnel :** Légifrance peut ne
pas retrouver une décision rendue sous plusieurs numéros joints (constaté le
29/10/2026 sur 2016-583/584/585/586 QPC) alors que LibreJustice la retrouve.
Recouper LibreJustice avant de conclure à une absence.

**Casus : un outil de contrôle en lot, jamais une preuve seule.** Le statut
« trouvée » établit l'existence dans le corpus ; il ne valide ni la version
applicable, ni le contenu, ni la portée. Un statut « introuvable » ou « hors
corpus » n'a aucune valeur probante d'inexistence (retard d'intégration, textes
non codifiés absents) : poursuivre sur un autre outil compétent.

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

Pour chaque **article de code, loi, ordonnance, décret et BOI**, relever de
même **la proposition qu'il est censé fonder** dans le livrable : la règle,
la condition, le taux, le seuil, le délai, la sanction ou l'interprétation
que la phrase lui rattache (« conformément à l'article… », « en application
de… », « (art. … ) » placé en fin de phrase, « selon le BOFiP… »). Une
référence citée sans guillemets ni signal reste rattachée à une proposition :
c'est cette proposition qui sera contrôlée en Phase 2quinquies. Une référence
purement indicative, qui ne fonde aucune proposition (ex. un simple renvoi
du type « régime prévu aux articles [N] et suivants »), est relevée comme telle.

---

### Phase 2 — Vérification via MCP Légifrance

Pour chaque référence extraite :

**Articles de code :**
```
rechercher_code(code_name="[Code]", search="[numéro article]", champ="NUM_ARTICLE")
```
Vérifier : article existe, alinéa cité correspond, article en vigueur (non abrogé).
L'existence ne suffit pas : le contenu de l'article au regard de la
proposition qu'il fonde se contrôle en Phase 2quinquies.

**Jurisprudence judiciaire :**
```
rechercher_jurisprudence_judiciaire(search="[numéro pourvoi]", champ="NUM_AFFAIRE")
```

**Jurisprudence administrative (CE, CAA, TA) :**
```
rechercher_jurisprudence_administrative(search="[numéro]")   # champ ALL par défaut : NUM_AFFAIRE n'existe pas pour cette base
```

**Décisions constitutionnelles :**
```
rechercher_decisions_constitutionnelles(search="[numéro décision]", champ="NUM_DEC")
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

### Phase 2bis — Vérification croisée via Casus, LibreJustice, Legal Data Hunter et Pourvoi

**Obligatoire pour toute référence non confirmée en Phase 2, et recommandé
en confirmation croisée pour toute référence à enjeu (🔴 critique, pièges
datés du `socle-eca` § 5).** N'interroger que les outils compétents (matrice
ci-dessus).

**Casus :**
```
# Passage entier ou liste (50 références par appel au plus) : existence, écarts de citation, version à une date
resolve_references(texte="[passage du livrable]", date="[date du fait générateur]")
resolve_references(references=["art. [N] [code]", "BOI-[identifiant]", "[juridiction], [date], n° [numéro]"], date="[JJ/MM/AAAA]")

# Lecture à la source de la référence retenue (toujours passer la date pour un fait daté)
get_code_article(code="[code]", numeros=["[numéro d'article]"], date="[JJ/MM/AAAA]")
get_bofip(identifiant="BOI-[identifiant]")
get_decision(numero="[n° de décision]", juridiction="[juridiction]", date="[JJ/MM/AAAA]")
```
Statuts à traiter : « trouvée avec écart » → corriger la citation selon la note
(date, chambre, numéro) ; « ambiguë » → préciser le code ou la juridiction ;
« non applicable à la date » → l'article était abrogé à cette date ; « indéterminée
à la date » → ne pas conclure, lire la version datée dans LibreJustice ; « hors
corpus » → lire dans Légifrance (JORF). Plusieurs décisions pour un même numéro :
ne jamais choisir arbitrairement, départager par juridiction et date. Une
décision se cite après lecture du texte intégral (`get_decision`), pas sur un
extrait de recherche.

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
- tout arrêt de cassation avec renvoi (vérifier la décision de la cour de renvoi) ;
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

### Phase 2quater — Fidélité des citations, des renvois et des signaux

**Obligatoire pour** toute citation entre guillemets, tout renvoi précis
(point, considérant, paragraphe, alinéa) et tout renvoi introduit par un signal
(« voir », « cf. », « comp. »). Une référence qui existe peut être citée
infidèlement : c'est le cas le plus fréquent d'erreur sur une décision réelle.

- **Citation textuelle** : la comparer mot à mot au texte officiel lu à la
  source (Légifrance, LibreJustice, BOFiP via `get_norm`). Un mot changé, une
  négation retirée ou une troncature qui change le sens (ex. « ne peut
  s'appliquer » devenu « s'applique ») → 🔴 ; une coquille sans incidence sur
  le sens → 🟡. Les coupes « [...] » ne doivent pas altérer le sens.
- **Renvoi précis** : retrouver le passage au numéro cité ; un point ou un
  considérant erroné → 🟠, avec le renvoi corrigé.
- **Signal** : le passage cité doit soutenir la proposition. « Voir » ne couvre
  ni une solution que la source n'énonce pas, ni son contraire ; une réserve
  d'interprétation ne se cite jamais comme une validation pure et simple.
- **Objet de la décision** : vérifier que le livrable lui attribue bien le texte
  qu'elle examine (ex. QPC 2016-538 : art. 150-0 D, non art. 150-0 B ter).
- **Aperçus et résumés** (`ai_summary` de LibreJustice, fiche Pourvoi) : ils
  orientent, ils ne valident ni une citation ni une portée. Lire le texte ; si
  seul un extrait a été lu, le signaler comme lecture partielle.

---

### Phase 2quinquies — Adéquation du fondement (articles de code, textes et BOI)

**Obligatoire pour tout article de code, toute loi, ordonnance ou décret, et
tout BOI relevé en Phase 1 comme fondant une proposition**, y compris quand il
est cité sans guillemets ni signal. Un texte qui existe et qui est en vigueur
peut être cité à l'appui d'une règle qu'il ne pose pas : c'est l'erreur la
plus difficile à voir, parce que la référence est exacte.

**Méthode :**
1. Lire à la source, dans la version applicable à la date du fait générateur,
   le passage pertinent **en entier** (l'alinéa, le I, le 2°, le paragraphe
   du BOI), et non un extrait de recherche ou un résumé. Pour un article long,
   lire au moins toute la subdivision dont relève la proposition, ainsi que
   les renvois et exceptions qu'elle contient (« sous réserve de… », « par
   dérogation… », « sauf… »). Toute lecture partielle est signalée.
2. Confronter la proposition du livrable au texte lu, élément par élément :
   champ d'application (personnes, opérations, biens), conditions, taux,
   seuils, délais, sanctions, date d'effet, exceptions.
3. Pour un BOI : vérifier le numéro de paragraphe cité, la date de
   publication de la version lue, et que la proposition figure bien dans la
   doctrine administrative et non dans un commentaire de tiers.

**Cas à traiter :**
- **Le texte pose la règle telle qu'énoncée** → conforme.
- **Le texte ne pose qu'une partie de la proposition** (une condition omise,
  une exception passée sous silence, un champ élargi ou restreint) → 🟠,
  avec la reformulation exacte proposée.
- **La règle provient d'un autre texte, d'une jurisprudence ou de la
  doctrine administrative**, et non de l'article cité (ex. une interprétation
  jurisprudentielle rattachée à l'article qu'elle interprète, une tolérance
  BOFiP présentée comme une disposition légale) → 🟠, en indiquant la
  véritable source à citer ; la nouvelle source passe elle-même au checker.
- **Le texte pose une règle différente ou contraire** (taux, seuil, délai,
  condition, sanction erronés ; régime d'un autre article attribué à celui-ci)
  → 🔴.
- **Doctrine présentée comme loi** (« la loi prévoit… » appuyé sur un BOI) ou
  **loi présentée comme simple doctrine** → 🟠 ; qualifier correctement la
  source et sa portée (conditions d'opposabilité de la doctrine
  administrative, lues à la source au jour du livrable et soumises
  elles-mêmes au checker).
- **Référence purement indicative** (Phase 1) → contrôle limité à l'existence
  et à la version, mais vérifier qu'elle ne fonde en réalité aucune
  proposition implicite. En cas de doute, elle est traitée comme fondant une
  proposition. Les références classées indicatives sont listées comme telles
  dans le rapport, pour que Yoann puisse contester ce classement.

Cette phase s'ajoute à la Phase 2quater, qui couvre les citations entre
guillemets, les renvois précis et les signaux : un même texte peut relever
des deux.

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

Le statut ✅ n'est attribué qu'une fois exécutés les contrôles obligatoires de la
référence : phase 2ter pour un arrêt de cassation avec renvoi, une décision de
cour d'appel ou une décision du fond administratif ; lecture du texte pour toute
portée citée (la fiche ou le sommaire ne suffisent pas) ; phase 2quinquies pour
tout article, texte ou BOI qui fonde une proposition. À défaut, le statut est
🟡 ou ⚪ avec la mention « contrôle incomplet : [phase non exécutée] ».

**Types d'erreurs fréquentes à détecter :**
- Numéro de décision CE ou Cass. inversé (ex: 425986 → 425689)
- Article CGI inexistant ou abrogé
- Date de jurisprudence incorrecte
- Portée de l'arrêt déformée (tenant/rejetant inversés)
- Décision d'appel citée alors qu'elle a été cassée
- Arrêt d'espèce ou inédit présenté comme jurisprudence établie
- Référence BOFiP périmée ou modifiée
- Article existant et en vigueur cité à l'appui d'une règle qu'il ne pose pas
  (condition omise, exception tue, taux ou seuil d'un autre texte)
- Règle jurisprudentielle ou doctrinale rattachée au texte qu'elle interprète
- Tolérance BOFiP présentée comme disposition légale
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
Adéquation du fondement contrôlée : N textes et BOI | Non conformes : N
Références classées indicatives (non soumises à la Phase 2quinquies) : [liste]

DÉTAIL PAR RÉFÉRENCE
[Référence] → [Statut] → [Outils ayant confirmé] → [Sort procédural ou adéquation du fondement] → [Observation]

RÉFÉRENCES À CORRIGER AVANT REMISE
[Liste des corrections prioritaires avec texte corrigé proposé]

RÉFÉRENCES NON CONFIRMÉES (vérification manuelle recommandée)
[Liste avec outils interrogés et raison de la non-confirmation]
```

Le rapport est produit en fin de livrable, avant remise au client.
Si aucune correction n'est nécessaire : "Toutes les références vérifiées ✅"

---

## Point de contrôle — Avant livraison (bloquant à 100 %)

Aucun livrable n'est remis tant qu'une seule référence n'est pas ✅ VÉRIFIÉ_EXACT
ou 🟡 VÉRIFIÉ_MINEUR corrigée. Le score global du rapport est une information,
jamais un seuil de tolérance.

```
pour chaque référence :
    ⛔ HALLUCINATION ou 🔴 SUBSTANTIELLEMENT_ERRONÉ → corriger ou retirer
    🟠 PARTIELLEMENT_EXACT                         → reformuler (portée, version)
    🟡 VÉRIFIÉ_MINEUR                              → corriger
    ⚪ NON_CONFIRMÉ                                 → retirer, ou signaler à Yoann,
                                                      qui décide ; jamais conservée
                                                      sans mention
puis re-déclencher le checker sur la version corrigée
```

## Règle d'auto-déclenchement

Se déclenche automatiquement à la fin de **tout** livrable juridique ou fiscal
(socle § 9), quel que soit le skill, y compris une réponse conversationnelle
qui cite une référence. Couvre 100 % des références, sans exception pour les
articles « connus ». Il fait partie du workflow de remise : aucun livrable
n'est présenté comme final avant le rapport.

Ajouter au contrôle : **version applicable** (le texte cité est-il celui en
vigueur à la date du fait générateur ? s'il a changé depuis, le signaler),
**application dans le temps** (la loi ou le décret modificateur a-t-il fixé une
entrée en vigueur différée ou une disposition transitoire qui écarte la version
citée pour les faits du dossier ? socle § 3, règle 8) et
**références internes aux skills** (un skill peut contenir une référence
erronée — exemple corrigé : l'« art. 150-0 F ter » inexistant, la CDHR étant à
l'art. 224 CGI).
