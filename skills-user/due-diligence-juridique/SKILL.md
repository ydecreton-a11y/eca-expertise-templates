---
name: due-diligence-juridique
description: >
  Skill ECA EXPERTISE pour tout audit de due diligence dans le cadre d'une
  acquisition, cession, entrée au capital ou fusion : audit juridique, fiscal,
  social, revue de contrats, analyse de passif, data room, GAP, LOI, protocole.
  Déclencher sur : due diligence, audit juridique, audit d'acquisition, audit
  fiscal, revue de passif, cession de fonds, cession de titres, acquisition,
  fusion, data room, garantie de passif, garantie d'actif, LOI, protocole.
  NE PAS utiliser pour une consultation de droit pur sans cible identifiée
  (→ consultation-juridique), ni pour l'analyse d'un seul contrat (→ analyse-contrat).
---

# Skill : Due diligence juridique et fiscale — ECA EXPERTISE

## PHASE 0 — Contexte dossier (exécuter en premier, toujours)

### Recherche automatique dans les dossiers en cours

Avant toute analyse, vérifier si ce client ou dossier a déjà été traité :

```
conversation_search(query="[nom client ou société mentionné dans la demande]")
```

Si des conversations passées existent sur ce dossier :
- Les lire pour récupérer : décisions prises, documents produits, positions
  retenues, points de vigilance identifiés
- Ne jamais reprendre de zéro un dossier déjà engagé
- Signaler en début de réponse : "Dossier retrouvé — suite de la consultation
  du [date]" ou "Nouveau dossier — aucun antécédent trouvé"

Si le nom du client n'est pas mentionné explicitement dans la demande :
- Continuer sans recherche (ne pas bloquer sur une demande générique)
- La recherche s'active uniquement si un nom propre de client ou de société
  est identifiable dans la requête

## PHASE 0b — Routing

```
Cible identifiée, opération d'acquisition/cession en cours ? → continuer ici
Question de droit théorique sans cible ? → consultation-juridique
Un seul contrat à analyser ? → analyse-contrat
```


### 0c — Intégration réponse Casus

Si Yoann colle un output Casus dans la conversation (ex: bilan fiscal de la cible) :
- L utiliser comme base documentaire fiscale certifiée
- Claude complète : analyse juridique, sociale, contractuelle, rédaction rapport DD Word
- Indiquer : "Base Casus intégrée — je construis la DD sur sa documentation"

---

## PHASE 1 — Sources et vérifications

### Fetch dynamique GitHub (obligatoire avant toute vérification)

Fetcher systématiquement avant d'utiliser un taux, un outil MCP ou une
référence BOFiP :

```
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md")
```

Ce fetch (2 secondes) garantit que tu travailles avec les taux et références
à jour — pas avec des valeurs mémorisées potentiellement périmées après
une LF. C'est la différence entre 30 % et 31,4 % de PFU.

### Vérifications complémentaires

Fetcher `shared/sources-legales.md` via GitHub (voir bloc Sources ci-dessus) pour les outils MCP et BOFiP.

**Points de vérification prioritaires pour une DD :**
- Droits d'enregistrement : cession parts 3%, actions 0,1%, fonds barème
- Art. L1224-1 C. trav. : transfert automatique des contrats de travail
- Art. 1583 C. civ. et suivants : conditions de la cession
- Garanties légales vs conventionnelles
- Jurisprudence récente sur les clauses de GAP

**Balise incertitude :**
```
⚠️ INCERTAIN — [point] : information à confirmer via [source/data room].
```

---

## PHASE 2 — Périmètre de la DD selon l'opération

| Type d'opération | Focus prioritaire |
|------------------|-------------------|
| Cession de titres | Passif fiscal latent, litiges sociaux, contrats clés, pacte d'associés |
| Cession de fonds | Baux commerciaux, contrats de travail L1224-1, licences, marques |
| Fusion / TUP | Traité d'apport, valeurs d'apport, passif transmis, agrément clients |
| Entrée au capital | Statuts, pacte, valorisation, droits préférentiels, anti-dilution |

---

## PHASE 3 — Grille d'analyse standard

### Juridique
- Forme sociale, capital, actionnariat actuel (historique des cessions)
- Statuts : clauses d'agrément, préemption, inaliénabilité
- Pacte d'associés en vigueur : droits préférentiels, tag-along, drag-along
- Litiges en cours ou menaces identifiées
- Contrats essentiels : durée, renouvellement, clauses de résiliation
  automatique en cas de changement de contrôle

### Fiscal
- Déclarations IS des 3 dernières années — cohérence
- Redressements fiscaux en cours ou prescrits depuis moins de 3 ans
- TVA : régularisations en cours, rappels potentiels
- Dividendes distribués : régularité, base légale
- PV latentes sur actifs

### Social
- Effectif, contrats atypiques, CDD/intérim en cours
- Accords collectifs opposables
- Provisions pour litiges prud'homaux
- Art. L1224-1 : transfert automatique si cession de fonds

### Immobilier / actifs
- Titres de propriété ou baux : durée résiduelle, loyers, renouvellement
- Actifs incorporels : marques déposées (vérifier INPI), brevets, licences

---

## PHASE 4 — Structure du rapport DD

```
RAPPORT DE DUE DILIGENCE
[Cible — Acquéreur — Date — Référence YD]

EXECUTIVE SUMMARY
Appréciation globale du risque : 🔴 Élevé / 🟠 Modéré / 🟢 Faible
Points bloquants identifiés : [liste]
Points à garantir dans la GAP : [liste]

I. PÉRIMÈTRE ET MÉTHODOLOGIE

II. ANALYSE JURIDIQUE
   [Sous-sections selon grille Phase 3]
   [Cotation de chaque risque : 🔴/🟠/🟢]

III. ANALYSE FISCALE
   [Idem]

IV. ANALYSE SOCIALE
   [Idem]

V. SYNTHÈSE DES RISQUES
   [Tableau : Risque | Domaine | Criticité | Recommandation GAP]

VI. RECOMMANDATIONS
   6.1 Points à négocier sur le prix
   6.2 Clauses de GAP recommandées
   6.3 Conditions suspensives suggérées
   6.4 Points à surveiller post-closing
```

---

## PHASE 5 — Livrable Word

- Corps : Raleway sz=22, justifié, **#999999**
- H1/H2 : Raleway gras, **#C00000**
- Signature : Raleway gras sz=22, **#495864**, centré
- Charger skill docx pour la mise en forme



---

## ENRICHISSEMENT — Templates GAP standardisés (Garantie d'Actif et de Passif)

### Clauses GAP fréquemment recommandées

**Clause de garantie générale d'actif et de passif :**
> « Le Cédant garantit au Cessionnaire que les comptes de la Société à la date du
> [date de référence] reflètent fidèlement l'actif et le passif de celle-ci, et
> qu'aucun élément de passif non comptabilisé ou sous-évalué, ni aucune diminution
> d'actif non comptabilisée ou surévaluée, n'est susceptible d'apparaître au-delà
> de [seuil franchise] €, à raison de tout fait, acte ou omission antérieurs à la
> Date de Réalisation. »

**Clause de garantie spécifique fiscale :**
> « Le Cédant garantit au Cessionnaire toute charge fiscale (impôts, taxes,
> cotisations, intérêts, pénalités) afférente à la période antérieure à la Date de
> Réalisation, qui viendrait à être réclamée à la Société dans le délai de
> prescription légale, et non comptabilisée au bilan de référence. »

**Clause de garantie sociale (litiges prud'homaux et URSSAF) :**
> « Le Cédant garantit toute condamnation prononcée à l'encontre de la Société au
> titre de litiges prud'homaux ou de redressements URSSAF afférents à des faits
> antérieurs à la Date de Réalisation, à hauteur du montant non provisionné. »

### Paramètres à négocier systématiquement

| Paramètre | Valeur de référence ECA | Justification |
|-----------|------------------------|---------------|
| Plafond global | 25 % à 100 % du prix selon risque | Au-delà = perte de motivation cédant |
| Seuil de franchise (de minimis) | 0,5 % à 1 % du prix | Évite les contentieux mineurs |
| Seuil de déclenchement (panier) | 1 % à 2 % du prix | Cumul des préjudices avant activation |
| Durée garantie générale | 18 à 36 mois | Borne du contrôle fiscal du cessionnaire |
| Durée garantie fiscale/sociale | Prescription légale (3 à 10 ans) | Aligné sur risque de redressement |
| Garantie de la garantie | Séquestre / cautionnement bancaire / GAP miroir | Solvabilité du cédant à long terme |

### Cas spécifiques

**Litige prud'homal en cours dans la cible :**
1. Vérifier provisionnement comptable
2. Si provisionné insuffisamment → demander complément ou clause spécifique pour le delta
3. Cession ne purge pas le risque (contrat de travail transféré L1224-1 ou maintenu)
4. Inclure dans GAP avec seuil zéro (pas de franchise sur litiges identifiés)

**Data room incomplète :**
1. Identifier les zones non documentées (lister précisément)
2. Demander complément avant signature LOI
3. Si refus du cédant → clauses GAP renforcées sur les zones grises
4. Mention « représentations à jour de la connaissance du Cédant » à proscrire seule
5. ⚠️ Signaler dans l'executive summary du rapport DD : « DD partielle — zones non documentées : [liste] »

---

## EXEMPLE — Rapport DD bien formé (extrait)

**Contexte :** Acquisition 100% des titres de SAS Plâtrerie X (25 salariés, CA 4,2 M€).

**Executive Summary (extrait) :**
> « **Appréciation globale : 🟠 Risque modéré.**
>
> Trois points appellent une vigilance particulière :
> 1. Deux contrats clients (60 % du CA cumulé) comportent une clause de
>    changement de contrôle exigeant l'accord préalable du donneur d'ordre.
>    **Action :** purger les clauses avant closing (condition suspensive).
> 2. Un litige prud'homal en cours (réclamation 84 k€) provisionné à 30 k€.
>    **Action :** clause GAP spécifique non plafonnée, sans franchise.
> 3. Redressement URSSAF en cours d'instruction (montant non chiffré).
>    **Action :** clause GAP fiscale/sociale sur prescription légale + séquestre.
>
> Aucun point bloquant identifié, opération réalisable sous réserve des trois
> conditions ci-dessus. »

**❌ Ce qui est insuffisant :**
> « La cible présente quelques risques. Une GAP est recommandée. »


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
- [ ] Périmètre DD (titres / fonds / fusion) confirmé en tête
- [ ] Grille 4 domaines couverte (juridique / fiscal / social / actifs)
- [ ] Cotation 🔴/🟠/🟢 portée sur chaque risque identifié
- [ ] Clauses GAP recommandées formulées concrètement
- [ ] Conditions suspensives suggérées listées
- [ ] Données de la data room manquantes signalées explicitement

**Si un seul item n'est pas validé → ne pas livrer. Reprendre la phase concernée.**


---

## 🔍 ANNEXE — Commandes MCP Légifrance exactes

Ne plus écrire « via MCP Légifrance » sans la commande. Utiliser les patterns suivants :

### Articles de code
```
rechercher_code(code_name="Code général des impôts", search="[numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Code de commerce", search="[numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Code civil", search="[numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Livre des procédures fiscales", search="L. [numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Code monétaire et financier", search="L. [numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Code du travail", search="L. [numéro]", champ="NUM_ARTICLE")
```

### Jurisprudence
```
# Conseil d'État, CAA, TA
rechercher_jurisprudence_administrative(search="[numéro affaire]", champ="NUM_AFFAIRE")
# Cour de cassation
rechercher_jurisprudence_judiciaire(search="[numéro pourvoi]", champ="NUM_AFFAIRE")
# Conseil constitutionnel
rechercher_decisions_constitutionnelles(search="[N°-AAAA QPC]")
```

### Doctrine et textes officiels
```
# BOFiP
web_fetch("https://bofip.impots.gouv.fr/bofip/[identifiant]")
# Loi / ordonnance / décret
recherche_journal_officiel(search="[numéro ou titre]", text_types=["LOI"])
# Texte consolidé
rechercher_dans_texte_legal(search="[mots-clés]")
```

**Règle de robustesse** : avant de conclure à l'inexistence d'une référence,
tenter au minimum 2 stratégies (numéro exact + mots-clés + date approximative).
Une référence non trouvée via MCP ≠ référence inexistante.
