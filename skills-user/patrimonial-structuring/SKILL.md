---
name: patrimonial-structuring
description: >
  Skill ECA EXPERTISE pour toute question de structuration patrimoniale,
  successorale ou familiale : démembrement de propriété, quasi-usufruit,
  régimes matrimoniaux, contrat de mariage, changement de régime, droit des
  successions, assurance-vie, pacte successoral (RAAR), SCI patrimoniale,
  stratégies intergénérationnelles. Déclencher sur : quasi-usufruit, usufruit,
  nue-propriété, démembrement, régime matrimonial, communauté, séparation de
  biens, participation aux acquêts, contrat de mariage, succession, héritage,
  donation, assurance-vie, clause bénéficiaire, RAAR, réserve héréditaire,
  quotité disponible, SCI familiale, stratégie patrimoniale complexe.
  NE PAS utiliser si la demande porte uniquement sur la transmission d'entreprise
  sans dimension patrimoniale personnelle (→ diagnostic-transmission), ou sur
  un calcul de PV pur (→ calcul-plus-value).
---

# Skill : Structuration patrimoniale et successorale — ECA EXPERTISE

Ce skill existe parce que les dossiers patrimoniaux complexes mobilisent
simultanément le droit civil (régimes matrimoniaux, successions, libéralités),
le droit fiscal (DMTG, IFI, assurance-vie) et des mécanismes spécifiques
(quasi-usufruit, RAAR, démembrement) que les skills généralistes ne traitent
pas avec la profondeur requise. C'est aussi le cœur du module AUREP RS6827.

---

## PHASE 0 — Recherche dossier en cours

Si un nom de client ou de famille est mentionné :

```
conversation_search(query="[nom client ou famille]")
```

- Historique trouvé → lire avant d'analyser, signaler discrètement
- Nouveau dossier → continuer normalement

---

## PHASE 0b — Routing

```
Transmission d'entreprise pure sans dimension familiale ? → diagnostic-transmission
Calcul PV ou coût fiscal ? → calcul-plus-value en complément
Rédaction acte (statuts SCI, donation, contrat de mariage) ? → redaction-acte
→ Analyse de fond patrimoniale : continuer ici
```

---

## PHASE 1 — Raisonnement préalable

Avant toute recherche, identifier mentalement :

1. **Situation familiale** — marié (quel régime ?), pacsé, concubin, divorcé,
   veuf. Le régime matrimonial conditionne tout le reste.
2. **Composition du patrimoine** — professionnel, immobilier, financier,
   assurance-vie. Distinguer biens propres / biens communs / indivis.
3. **Objectif prioritaire** — protéger le conjoint ? Transmettre aux enfants ?
   Réduire la fiscalité ? Anticiper une incapacité ?
4. **Horizon temporel** — transmission immédiate, progressive sur 15 ans,
   ou successorale à terme.
5. **Contraintes** — réserve héréditaire, enfants de lits différents,
   héritiers vulnérables, dette fiscale latente.

---

## PHASE 1b — AUREP fetch obligatoire

Si la demande touche démembrement, quasi-usufruit, régimes matrimoniaux, successions ou LMNP :

```
# Usufruit, quasi-usufruit, Art. 13-5 CGI
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/M5_usufruit_article_13_5_CGI.md")

# Usufruit de droits sociaux
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/M8_usufruit_droits_sociaux.md")

# Actualités patrimoniales (LMNP, abattement retraite, LF 2026)
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/aurep/M10_actualites_patrimoniales.md")
```

Ne pas improviser sur ces sujets sans avoir chargé le module correspondant.
Les modules AUREP contiennent la doctrine vérifiée — ils priment sur la mémoire du modèle.

---

## PHASE 2 — Sources

Fetcher avant toute vérification :

```
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md")
```

Charger le fichier de référence correspondant au domaine :

| Sujet | Fichier |
|-------|---------|
| Démembrement, quasi-usufruit | `references/demembrement-quasi-usufruit.md` |
| Régimes matrimoniaux | `references/regimes-matrimoniaux.md` |
| Successions, libéralités | `references/successions-liberalites.md` |
| Assurance-vie | `references/assurance-vie.md` |

**Balise incertitude :**
```
⚠️ INCERTAIN — [point] : à vérifier via [source] avant conseil définitif.
```

---

## PHASE 3 — Analyse par domaine

Charger le fichier de référence du domaine concerné avant d'analyser.
Ne pas improviser sur ces sujets sans avoir lu le fichier correspondant —
les mécanismes sont techniques et les erreurs coûteuses.

---

## PHASE 4 — Structure de sortie

```
ANALYSE PATRIMONIALE ET SUCCESSORALE
[Client — Date — Référence YD]

I. SITUATION FAMILIALE ET PATRIMONIALE
   1.1 Régime matrimonial applicable
   1.2 Composition du patrimoine (propres / communs / indivis)
   1.3 Héritiers réservataires et quotité disponible
   1.4 Fiscalité latente identifiée

II. PROBLÉMATIQUE(S) IDENTIFIÉE(S)

III. ANALYSE
   [Par domaine selon la situation]
   [Balises ⚠️ INCERTAIN sur toutes les zones grises]

IV. OUTILS ET STRATÉGIES RECOMMANDÉS
   [Tableau : Outil | Avantage | Condition | Coût fiscal | Risque]

V. CHIFFRAGE INDICATIF
   [Avant/après optimisation — caractère indicatif rappelé]

VI. POINTS DE VIGILANCE
   — Réserve héréditaire respectée ?
   — Risque abus de droit ?
   — Garanties à prévoir ?
   — Notaire obligatoire ?

VII. PROCHAINES ÉTAPES
```

---

## PHASE 5 — Livrable Word

- Corps : Raleway sz=22, justifié, **#999999**
- H1/H2 : Raleway gras, **#C00000**
- Signature : Raleway gras sz=22, **#495864**, centré
- Charger skill `docx` + déclencher `legal-hallucination-checker`

---

## Intégration réponse Casus

Si Yoann colle un output Casus dans la conversation :
- L'utiliser comme base documentaire CGI/BOFiP certifiée
- Ne pas redupliquer les vérifications déjà faites par Casus
- Rôle Claude : raisonnement patrimonial global, jurisprudence civile (Cass., CA),
  rédaction Word ECA, analyse régimes matrimoniaux
- Indiquer : "Base Casus intégrée — construction sur sa documentation"
