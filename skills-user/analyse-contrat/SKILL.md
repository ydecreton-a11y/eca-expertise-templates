---
name: analyse-contrat
description: >
  Skill ECA EXPERTISE pour toute analyse, relecture, rédaction ou sécurisation
  d'un document contractuel : contrat, convention, bail, CGV, pacte, NDA, MOU,
  lettre de mission, protocole, acte de cession, garantie. Déclencher dès qu'un
  document contractuel est fourni ou qu'une clause doit être analysée ou rédigée.
  Mots-clés : analyser, relire, vérifier, sécuriser, rédiger, améliorer un contrat,
  une clause, un accord, un avenant.
  NE PAS utiliser si : la demande est une consultation de droit pur sans document
  fourni (→ consultation-juridique), si un acte de droit des sociétés doit être
  créé de zéro (→ redaction-acte).
---

# Skill : Analyse contractuelle — ECA EXPERTISE

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


### 0c — Intégration réponse Casus

Si Yoann colle un output Casus dans la conversation :
- L utiliser comme base documentaire CGI/BOFiP certifiée
- Ne pas redupliquer les vérifications fiscales déjà faites
- Rôle Claude : analyse des clauses, risques contractuels, rédaction Word ECA
- Indiquer : "Base Casus intégrée"

## PHASE 0b — Qualification et routing

```
Document contractuel fourni ? → continuer ici
Pas de document, question de droit pur ? → skill consultation-juridique
Acte de droit des sociétés à créer (statuts, PV, cession) ? → skill redaction-acte
```

---

## PHASE 1 — Raisonnement préalable (avant lecture détaillée)

Avant d'analyser clause par clause, poser mentalement :

1. **Quelle est la nature juridique de ce contrat ?**
   La qualification conditionne le régime impératif applicable.

2. **Quel est le déséquilibre apparent ?**
   Qui a rédigé ? En faveur de qui ? Quel est le contexte de négociation ?

3. **Quels sont les enjeux prioritaires pour ECA et son client ?**
   Protection du prix ? Maintien de l'activité ? Limitation de responsabilité ?

4. **Y a-t-il une dimension fiscale évidente ?**
   Flux financiers, cession d'actifs, droits d'enregistrement.

---

## PHASE 2 — Sources et vérifications

### Fetch dynamique GitHub (obligatoire avant toute vérification)

Fetcher systématiquement avant d'utiliser un taux, un outil MCP ou une
référence BOFiP :

```
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md")
```

Ce fetch (2 secondes) garantit que tu travailles avec les taux et références
à jour — pas avec des valeurs mémorisées potentiellement périmées après
une LF. C'est la différence entre 30 % et 31,4 % de PFU.

### Vérifications complémentaires à vérifier

Fetcher `shared/sources-legales.md` via GitHub (voir bloc Sources ci-dessus) pour les outils MCP et BOFiP.

Points à vérifier systématiquement :
- Articles du Code civil invoqués (force majeure Art. 1218, imprévision Art. 1195)
- Règles d'ordre public sectorielles (droit conso, droit commercial)
- Jurisprudence récente sur les clauses litigieuses

**Balise incertitude :**
```
⚠️ INCERTAIN — [point précis] : à vérifier via [source] avant conseil définitif.
```

---

## PHASE 3 — Analyse structurée

### 3.1 Qualification juridique
- Nature du contrat (prestation, vente, bail, cession, pacte…)
- Régime applicable (droit commun / règles spéciales)
- Parties et capacité juridique

### 3.2 Analyse des clauses essentielles

Examiner dans cet ordre :
1. Objet et périmètre de la prestation
2. Obligations principales de chaque partie
3. Conditions financières (prix, révision, indexation, TVA)
4. Durée, reconduction, résiliation (Art. 1211 s. C. civ.)
5. Responsabilité, limitations, garanties, clauses pénales
6. Force majeure (Art. 1218 C. civ.) et imprévision (Art. 1195 C. civ.)
7. Confidentialité et non-sollicitation
8. Non-concurrence (proportionnalité, durée, zone, contrepartie)
9. Propriété intellectuelle (Art. L131-3 CPI pour cessions écrites)
10. Attribution de juridiction / arbitrage

### 3.3 Détection des déséquilibres
- Clauses abusives B2C (Art. L212-1 C. conso.)
- Déséquilibre significatif B2B (Art. L442-1 C. com.)
- Clauses potentiellement réputées non écrites

### 3.4 Dimension fiscale
Tout contrat impliquant des flux financiers doit traiter :
- Qualification fiscale des sommes (honoraires, redevances, prix de cession…)
- Régime TVA (exonération, autoliquidation, taux)
- Droits d'enregistrement (cessions, baux commerciaux)
- Risque de requalification (prix anormal, acte anormal de gestion)

---

## PHASE 4 — Structure de sortie

```
I. QUALIFICATION JURIDIQUE ET CADRE APPLICABLE
   1.1 Nature du contrat et régime
   1.2 Parties, capacité, pouvoir de signature

II. ANALYSE DES CLAUSES ESSENTIELLES
   [Clause par clause avec : résumé → risque → recommandation]

III. DIMENSION FISCALE ET RÉGLEMENTAIRE

IV. COTATION DES RISQUES
   [Tableau : Clause | Risque | Nature | Criticité 🔴🟠🟢 | Recommandation]

V. RECOMMANDATIONS ET SÉCURISATION
   5.1 Modifications rédactionnelles prioritaires (avec texte suggéré)
   5.2 Points à négocier
   5.3 Stratégie globale

VI. CONCLUSION
   Appréciation globale du niveau de sécurité juridique.
```

---

## PHASE 5 — Livrable Word (si demandé)

- Corps : Raleway sz=22, justifié, **#999999** ← couleur correcte
- H1/H2 : Raleway gras, **#C00000**
- Signature : Raleway gras sz=22, **#495864**, centré
- Méthode : XML injection template ECA validé

---

## Exemple de sortie bien formée

**Input :** "Analyse ce contrat de prestation de services informatiques"

**Risque détecté et formulé correctement :**
> "**Clause de limitation de responsabilité (Art. 8)** — La clause plafonne
> la responsabilité du prestataire au montant des honoraires de la dernière
> mensualité. Ce plafond est disproportionné si la prestation défaillante
> peut causer un préjudice commercial significatif au client.
> **Criticité : 🔴 Élevé**
> **Recommandation :** Négocier un plafond au montant total du contrat annuel
> ou à un multiple des honoraires mensuels (x3 à x6 selon l'enjeu)."

**❌ Ce qui est insuffisant :**
> "La clause de limitation de responsabilité pourrait poser problème."

