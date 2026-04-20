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

