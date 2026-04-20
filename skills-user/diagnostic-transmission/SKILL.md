---
name: diagnostic-transmission
description: >
  Skill ECA EXPERTISE pour tout diagnostic patrimonial ou de transmission en
  phase exploratoire : bilan patrimonial, audit avant cession, choix entre
  donation/cession/apport/holding/Dutreil/nue-propriété. À utiliser AVANT
  de structurer une opération, quand le client ne sait pas encore quel outil
  est le mieux pour lui. Mots-clés : transmission, bilan patrimonial, diagnostic,
  stratégie patrimoniale, optimiser la transmission, préparer la cession,
  quel outil, holding familiale, Dutreil, apport-cession, optimisation successorale.
  NE PAS utiliser si l'outil est déjà choisi et qu'une consultation approfondie
  est nécessaire (→ consultation-juridique) ou si un acte doit être rédigé
  (→ redaction-acte).
---

# Skill : Diagnostic de transmission — ECA EXPERTISE

## PHASE 0 — Contexte dossier (exécuter en premier, toujours)

### 0a — Recherche automatique dans les dossiers en cours

Avant toute analyse, vérifier si ce client ou dossier a déjà été traité :

```
conversation_search(query="[nom client ou société mentionné dans la demande]")
```

- Si des conversations passées existent → les lire avant d'analyser.
  Signaler : "Suite du dossier [client] — [date dernière conversation]"
- Si aucun historique → nouveau dossier, continuer normalement
- Si demande générique sans nom propre → pas de recherche

### 0b — SIREN fourni ?

Si un numéro SIREN est mentionné dans la demande :
```
web_fetch("https://recherche-entreprises.api.gouv.fr/search?q=[SIREN]&per_page=1")
```
Pré-remplir automatiquement : dénomination, forme juridique, adresse, code APE, dirigeants.

### 0c — Intégration réponse Casus

Si Yoann colle un output Casus dans la conversation :
- L'utiliser comme base documentaire CGI/BOFiP certifiée
- Construire l'analyse patrimoniale dessus sans redupliquer les vérifications fiscales
- Indiquer : "Base Casus intégrée — je construis l'analyse de transmission sur sa documentation"

### 0d — Vérification du périmètre

**Signal de renvoi vers patrimonial-structuring :**
Si la demande révèle une problématique patrimoniale personnelle profonde
(quasi-usufruit, régime matrimonial complexe, succession contentieuse,
assurance-vie démembrée, RAAR) → déclencher patrimonial-structuring
en complément ou à la place selon la dimension dominante.

```
Client a déjà choisi son outil (ex: "je veux faire un Dutreil") ?
  → skill consultation-juridique directement
Client explore ses options ?
  → continuer ici, puis orienter vers consultation-juridique sur l'outil retenu
```

---

## Sources — Fetch dynamique GitHub (obligatoire avant toute vérification)

Fetcher avant d'utiliser un taux, un outil MCP ou une référence BOFiP :

```
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md")
```

Ce fetch (2 secondes) garantit les taux et références à jour.

## PHASE 0e — AUREP fetch (obligatoire si démembrement / patrimoine / LMNP)

Si la demande touche usufruit, nue-propriété, démembrement, quasi-usufruit,
régimes matrimoniaux, LMNP ou abattement retraite :

```
# Usufruit, quasi-usufruit, Art. 13-5 CGI
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/M5_usufruit_article_13_5_CGI.md")

# Usufruit de droits sociaux
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/M8_usufruit_droits_sociaux.md")

# Actualités patrimoniales (LMNP, abattement retraite, LF 2026)
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/M10_actualites_patrimoniales.md")
```

Ces modules priment sur la mémoire du modèle pour ces sujets.

---

## PHASE 1 — Collecte des données (demander si manquantes)

Un diagnostic sans données précises produit des recommandations génériques
sans valeur. Identifier et demander les éléments manquants avant d'analyser.

### Sur la structure patrimoniale
- Nature des actifs : société(s) opérationnelle(s), holding, SCI, immobilier,
  valeurs mobilières, liquidités — avec valorisation estimée
- Forme sociale de chaque entité et régime fiscal (IS / IR)
- Fiscalité latente : PV en report, amortissements LMNP non déduits,
  CCA détenus dans des sociétés
- Régime matrimonial du dirigeant + situation familiale précise

### Sur le dirigeant
- Âge et horizon de transmission (immédiat / 3 ans / 10 ans)
- Besoins de liquidités post-transmission
- Donations antérieures (rappel fiscal 15 ans — capital critique)
- Contrats d'assurance-vie et clause bénéficiaire
- Testament existant ?

### Sur l'entreprise
- Activité : opérationnelle éligible Dutreil / holding animatrice / mixte
- Valorisation et méthode (méthode des comparables, DCF, actif net…)
- Résultat récurrent, trésorerie disponible (attention aux abus de biens)
- Pacte d'associés existant ? Clauses d'agrément ? Droits préférentiels ?

### Sur les objectifs
- Transmission à titre gratuit (donation) ou onéreux (cession) ?
- Maintien dans la famille ou cession à tiers ?
- Conservation du contrôle ou sortie totale ?
- Contraintes de liquidité à court terme ?

---

## PHASE 2 — Analyse des outils disponibles

Pour chaque situation, évaluer les outils dans cet ordre de priorité :

| Outil | Avantage clé | Condition clé | Signal d'alerte |
|-------|-------------|---------------|-----------------|
| Pacte Dutreil 787 B | Abattement 75 % DMTG | Activité éligible + engagements | Holding mixte, contrôle diffus |
| Donation NP + Dutreil | Double réduction d'assiette | Âge donateur favorable | Perte de liquidité |
| Apport-cession 150-0 B ter | Report PV + réinvestissement | Contrôle holding + 70 % réemploi | CDHR neutralisant le gain |
| Abattement retraite 238 quindecies | 500 k€ net d'impôt | Conditions âge + départ retraite | Délais stricts |
| Donation-partage | Paix familiale, gel valeurs | Accord héritiers | Notaire obligatoire |
| SCI + donation progressive | Transmission immobilier | Mise en place anticipée | IS vs IR |
| Holding familiale + mère-fille | Réinvestissement optimisé | Constitution préalable | Délai de mise en place |

Fetcher `shared/sources-legales.md` via GitHub pour vérifier les conditions légales avant recommandation.

---

## PHASE 3 — Combinaisons optimales fréquentes chez ECA

- **Dutreil + donation en NP** : abattement 75% × décote NP (barème Art. 669 CGI)
- **Apport-cession + holding de réinvestissement** : PV différée + diversification
- **SCI + donation progressive** : transmission immobilière sur 15 ans
- **Holding animatrice + Dutreil** : vérifier impérativement éligibilité via BOFiP
- **PER effet turbo + cession** : déduction des versements + réduction RFR
  avant cession pour limiter CEHR

---

## PHASE 4 — Structure de sortie

```
DIAGNOSTIC DE TRANSMISSION
[Client — Date — Référence YD]

I. SITUATION PATRIMONIALE ET FAMILIALE
   1.1 Cartographie des actifs (tableau valeurs)
   1.2 Situation familiale et objectifs
   1.3 Fiscalité latente identifiée
   1.4 Points de vigilance spécifiques

II. ENJEUX ET CONTRAINTES
   — Enjeux fiscaux (DMTG, PV, IS latent)
   — Enjeux juridiques (gouvernance, agrément, pacte)
   — Enjeux familiaux et successoraux
   — Contraintes temporelles et de liquidité

III. OUTILS ENVISAGEABLES
   [Tableau comparatif : Outil | Avantage | Condition | Coût estimé | Risque]
   [⚠️ INCERTAIN si une condition n'est pas vérifiable sans information complémentaire]

IV. SCHÉMA(S) RECOMMANDÉ(S)
   Scénario 1 : [description, séquencement, intervenants]
   Scénario 2 : [si plusieurs options comparables]
   Recommandation principale motivée

V. CHIFFRAGE FISCAL INDICATIF
   Avant optimisation vs après optimisation — chiffres indicatifs,
   à affiner via skill calcul-plus-value sur données complètes.
   [Toujours préciser le caractère indicatif]

VI. POINTS DE VIGILANCE ET RISQUES
   — Risques d'abus de droit identifiés
   — Conditions suspensives à lever
   — Informations complémentaires nécessaires

VII. PROCHAINES ÉTAPES
   Actions à engager, ordre chronologique, intervenants à mobiliser.
   [Toujours conclure par une action concrète datée si possible]
```

---

## Exemple de diagnostic bien formé

**Ce qui distingue un bon diagnostic :**
> "Le rappel fiscal de 15 ans révèle que M. Martin a déjà utilisé 60 000 €
> de son abattement enfant en 2018. Il lui reste 40 000 € disponibles.
> Dans ces conditions, une donation Dutreil directe est moins efficace
> qu'une donation en nue-propriété qui réduit l'assiette de 40% (âge 58 ans,
> coefficient 0,6), réduisant la valeur taxable de 1 200 000 € à 288 000 €
> après Dutreil et NP — contre 300 000 € en pleine propriété avec Dutreil seul."

**❌ Ce qui est insuffisant :**
> "Nous recommandons une combinaison Dutreil + nue-propriété pour optimiser
> la transmission."
