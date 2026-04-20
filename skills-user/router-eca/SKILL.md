---
name: router-eca
description: >
  Point d'entrée intelligent de l'écosystème ECA EXPERTISE. Utiliser ce skill
  en priorité dès qu'une demande juridique ou fiscale arrive et qu'il y a une
  ambiguïté sur le type de livrable attendu. Déclencher sur : "j'ai un client
  qui...", "que faire dans ce cas", "comment traiter", "conseil sur", ou toute
  question où plusieurs skills pourraient s'appliquer. Ce skill identifie
  le bon skill (ou la bonne combinaison) et orchestre la réponse.
---

# Router ECA — Orchestrateur de l'écosystème skills juridique

Ce skill résout le problème central de tout écosystème multi-skills :
quand plusieurs skills sont pertinents, lequel déclencher, dans quel ordre,
avec quelle combinaison ? Sans règle explicite, le modèle arbitre mal.
Ce router donne cette règle.

---

## Pré-vérifications systématiques (avant l'arbre de décision)

### SIREN fourni ?
Si un numéro SIREN est mentionné dans la demande :
```
web_fetch("https://recherche-entreprises.api.gouv.fr/search?q=[SIREN]&per_page=1")
```
Pré-remplir automatiquement la fiche client avant tout traitement.

### Output Casus collé dans la conversation ?
Si Yoann colle un output Casus :
→ Pas de routing → enrichissement direct
→ Casus = base documentaire CGI/BOFiP certifiée
→ Claude = raisonnement juridique complémentaire, jurisprudence Légifrance, rédaction Word ECA
→ Indiquer : "Base Casus intégrée — je construis sur sa documentation"

### Nom de client ou dossier mentionné ?
```
conversation_search(query="[nom client ou société]")
```
Vérifier s'il existe un historique avant de démarrer quoi que ce soit.

---

## Arbre de décision principal

### Étape 0 — Un document est-il fourni ?

```
Document contractuel fourni (contrat, convention, bail, pacte, acte…) ?
  → OUI : skill analyse-contrat (+ consultation-juridique si question fiscale jointe)
  → NON : continuer →
```

### Étape 1 — La demande porte-t-elle sur un calcul chiffré ?

```
Chiffrage d'impôt, simulation PV, coût fiscal d'une opération ?
  → OUI : skill calcul-plus-value EN PREMIER
           puis consultation-juridique si stratégie à développer
  → NON : continuer →
```

### Étape 2 — Le client est-il en amont d'une opération non encore définie ?

```
"Je veux transmettre mon entreprise", "comment optimiser avant cession",
"bilan patrimonial", "qu'est-ce qui est mieux pour moi" ?
  → OUI : skill diagnostic-transmission (cartographie avant tout)
           puis consultation-juridique sur l'outil retenu
  → NON : continuer →
```

### Étape 3 — La demande porte-t-elle sur un texte ou réforme récent ?

```
"Qu'est-ce que change la LF 2026", "impact d'une ordonnance",
"nouvelle règle sur X", "veille sur Y" ?
  → OUI : skill veille-juridique
  → NON : continuer →
```

### Étape 4 — Un acte juridique doit-il être rédigé ?

```
Statuts, PV, cession de parts, dissolution, pacte d'associés ?
  → OUI : skill redaction-acte
           + consultation-juridique si points de droit à trancher avant rédaction
  → NON : continuer →
```

### Étape 5 — Une opération d'acquisition ou de cession est-elle en cours ?

```
Due diligence, audit de cible, analyse de passif, data room ?
  → OUI : skill due-diligence-juridique
  → NON : continuer →
```

### Étape 5b — La demande porte-t-elle sur le patrimoine personnel ou familial ?

```
Quasi-usufruit, régime matrimonial, contrat de mariage, succession,
assurance-vie, démembrement, RAAR, réserve héréditaire, SCI familiale ?
  → OUI : skill patrimonial-structuring
           + calcul-plus-value si chiffrage DMTG ou PV associée
           + redaction-acte si contrat de mariage ou acte de donation
  ⚠️ AUREP fetch obligatoire pour ces sujets (voir ci-dessous)
  → NON : continuer →
```

### Étape 5c — Une procédure fiscale est-elle en cours ?

```
Proposition de rectification, redressement, réclamation, Commission des impôts,
provision refusée, pénalités, abus de droit ?
  → OUI : skill contentieux-fiscal
  → NON : continuer →
```

### Étape 6 — La réponse doit-elle être vulgarisée pour un client non-juriste ?

```
"Explique à mon client", "note pédagogique", "lettre d'information" ?
  → OUI : skill note-information-client
           (après consultation-juridique si le fond n'est pas arrêté)
  → NON : → skill consultation-juridique (cas général)
```

---

## Trigger AUREP — fetch obligatoire

Déclencher le fetch des modules AUREP correspondants dès que la demande touche :

| Sujet | Module à fetcher |
|-------|-----------------|
| Démembrement, usufruit, nue-propriété | `aurep/M5_usufruit_article_13_5_CGI.md` + `M8_usufruit_droits_sociaux.md` |
| LMNP, LMP, revenus fonciers | `aurep/M10_actualites_patrimoniales.md` |
| Régimes matrimoniaux, quasi-usufruit | `aurep/M5_usufruit_article_13_5_CGI.md` |
| Successions, abattement retraite | `aurep/M10_actualites_patrimoniales.md` |

Base URL : `https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/`

---

## Combinaisons fréquentes chez ECA

| Situation | Combinaison recommandée | Ordre |
|-----------|------------------------|-------|
| Client veut céder son entreprise | diagnostic-transmission → calcul-plus-value → consultation-juridique | Séquentiel |
| Apport-cession + holding à créer | consultation-juridique + calcul-plus-value | Parallèle |
| Acquisition de cible | due-diligence-juridique → redaction-acte (GAP) | Séquentiel |
| Donation-partage famille | diagnostic-transmission → consultation-juridique → redaction-acte | Séquentiel |
| Question sur une réforme LF | veille-juridique → note-information-client | Séquentiel |
| Statuts + points fiscaux | redaction-acte + consultation-juridique | Parallèle |
| Output Casus + consultation | intégration Casus → consultation-juridique enrichie | Parallèle |
| SIREN fourni + création société | auto-lookup API → redaction-acte | Séquentiel |

---

## Règle de refus élégant

Si après l'arbre de décision le périmètre reste ambigu, ne pas improviser.
Poser une seule question discriminante :

> "Pour t'orienter précisément : ton client a-t-il déjà une structure définie
> et cherche un conseil sur une opération précise, ou est-il en phase
> exploratoire pour définir la meilleure stratégie ?"

- Réponse "opération précise" → consultation-juridique
- Réponse "phase exploratoire" → diagnostic-transmission

---

## Point de contrôle — Routing ambigu

Si après l'arbre de décision + la règle de refus élégant, le périmètre
reste toujours ambigu : **ne pas procéder**. Attendre la réponse de Yoann
avant de lancer un skill. Un mauvais routing perd du temps sur les deux ends.

## Signalement des conflits de skills

Quand deux skills se déclenchent simultanément sur la même requête,
indiquer explicitement en début de réponse :

> "Cette demande active deux skills : [skill A] pour [raison] et [skill B]
> pour [raison]. Je traite d'abord [skill A] puis [skill B]."

Ne jamais fusionner silencieusement deux frameworks sans le signaler.
