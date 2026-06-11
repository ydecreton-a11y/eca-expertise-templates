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
> **📋 RESSOURCES** : Pour identifier les modules AUREP, PDF et dossiers
> pertinents, consulter sources-legales.md **section 9 (Index des ressources GitHub)**.


# Router ECA — Orchestrateur de l'écosystème skills juridique

Ce skill résout le problème central de tout écosystème multi-skills :
quand plusieurs skills sont pertinents, lequel déclencher, dans quel ordre,
avec quelle combinaison ? Sans règle explicite, le modèle arbitre mal.
Ce router donne cette règle.

---

## 🔔 MÉMO DÉBUT DE SESSION — Prompt-Codes ECA

> **À chaque nouvelle session, rappeler à Yoann :**
> Tu peux modifier le comportement de Claude en ajoutant un code EN DÉBUT de message.
> Référentiel complet : `skills-user/prompt-codes-eca.md`
>
> **Codes les plus utiles selon le contexte :**
>
> | Besoin du moment | Code à utiliser |
> |-----------------|-----------------|
> | Voir le raisonnement étape par étape | `/think` |
> | Trouver les failles d'une position | `/critique` |
> | Tester l'argument adverse | `/devil` |
> | Construire le meilleur argument | `/steelman` |
> | Détecter ce qui manque | `/gaps` |
> | Réponse longue et développée | `/verbose` |
> | Réponse courte et structurée | `/concise` |
> | Direct sans précautions de forme | `/brutal` |
> | Raisonner à rebours depuis l'objectif | `/inversethink` |
> | Comparer des options | `/compare` |
> | Note client accessible | `/human` + `/bulletproof` |
> | Post LinkedIn ECA | `/firstperson` + `/human` |
> | Tableau de bord interactif | [prompt] + `/dashboard` |
> | Simulation de calcul interactive | [prompt] + `/calculator` |
>
> ⚠️ `/nohedge` et `/human` : jamais sur livrables juridiques clients
> 📄 Référentiel complet des règles d'exclusion → `prompt-codes-eca.md`

---

## Pré-vérifications systématiques (avant l'arbre de décision)

### Code de prompt détecté en début de message ?
Si le message de Yoann commence par un code (`/think`, `/critique`, `/brutal`, etc.) :
→ Appliquer le modificateur de comportement correspondant (voir `prompt-codes-eca.md`)
→ Puis continuer l'arbre de décision normalement pour le routing skill
→ Les codes ne suspendent jamais les règles permanentes ECA (Légifrance, legal-hallucination-checker, etc.)

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

## Reformulateur d'intention — déclenchement automatique

Ce composant absorbe les prompts vagues ou imprécis AVANT d'entrer dans l'arbre
de décision. Il reformule l'intention, propose un routing, et attend confirmation.
Objectif : éliminer les mauvais départs sans pénaliser l'imprécision naturelle.

### Quand activer ?

Activer si AU MOINS 2 de ces signaux sont présents dans le message de Yoann :

| Signal | Exemple |
|--------|---------|
| Absence de mot-clé skill en tête | *"j'ai un client qui vend..."* |
| Marqueur d'hésitation | *"enfin", "c'est un peu compliqué", "je sais pas trop"* |
| Plusieurs sujets mélangés sans question centrale | *"holding + cession + succession"* |
| Absence de livrable spécifié (`→ livrable :` absent) | message sans format de sortie |
| Phrase nominale sans verbe d'action | *"COUSSEMACQ indivision EURL YODA"* |

### Ne PAS activer si (exécution directe) :

- Mot-clé skill présent en tête :
  `consultation` / `calcule` / `rédige` / `DD` / `diagnostic` /
  `contrat` / `contentieux` / `note client` / `veille`
- Document joint → `analyse-contrat` direct
- SIREN fourni → API lookup direct
- Output Casus collé → enrichissement direct
- `→ livrable :` présent dans le message
- Code de prompt `/xxx` présent → appliquer le modificateur + routing direct

### Format de sortie obligatoire

Produire UNIQUEMENT ce bloc — pas de consultation, pas d'analyse, pas de développement :

```
📋 REFORMULATION — avant d'exécuter

Dossier/client   : [détecté via conversation_search, ou "?" si inconnu]
Opération        : [qualifiée en 1 ligne]
Question centrale: [reformulée en 1 phrase nette]
Skill pressenti  : [skill X]
Livrable         : [consultation word / calcul / acte word / note client]

→ Je lance [skill X] sur cette base ?
  Tape "go" pour confirmer, ou corrige ce qui est inexact.
```

### Après confirmation

| Réponse de Yoann | Comportement |
|------------------|-------------|
| `"go"` / `"oui"` / `"ok"` | Exécuter le skill identifié immédiatement |
| Correction courte (1-2 mots) | Intégrer, reformuler une dernière fois, puis exécuter |
| Silence / changement de sujet | Ne pas exécuter — attendre une instruction explicite |
| Désaccord complet | Revenir à la règle de refus élégant (1 question discriminante) |

### Exemples de déclenchement

**Entrée :** *"j'ai un client enfin c'est une situation un peu particulière
avec une indivision et une EURL tu vois le truc..."*
→ 3 signaux détectés (hésitation + sujets mélangés + pas de livrable)
→ Reformulation activée

**Entrée :** `consultation COUSSEMACQ régime fiscal soulte indivision → livrable : note word`
→ Mot-clé skill en tête + livrable présent
→ Reformulation NON activée — routing direct consultation-juridique

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
| LMNP (voir aussi AUREP M11 patrimoine immobilier), LMP, revenus fonciers | `aurep/M10_actualites_patrimoniales.md` |
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
