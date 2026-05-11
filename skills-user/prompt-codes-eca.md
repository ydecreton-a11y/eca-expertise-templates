---
name: prompt-codes-eca
description: >
  Codes de prompt opérationnels pour l'écosystème ECA EXPERTISE.
  Référentiel des modificateurs de comportement validés — à consulter
  EN DÉBUT DE SESSION pour choisir le bon code selon le livrable attendu.
  Fichier compagnon du router-eca.
version: 1.0
---

# Prompt-Codes ECA — Mémo d'utilisation

> **🔔 RÉFLEXE DE DÉBUT DE SESSION**
> Avant de lancer une demande, demande-toi :
> *"Quel type de livrable est-ce que j'attends ?"*
> Puis ajoute le code correspondant EN DÉBUT de ton message.
> Exemple : `/critique Analyse ce protocole de cession...`

---

## 📋 Tableau de référence rapide

| Code | Position | Effet réel | Skills compatibles | ⚠️ Restrictions |
|------|----------|------------|-------------------|-----------------|
| `/think` | Avant | Raisonnement visible étape par étape avant conclusion | Tous | — |
| `/critique` | Avant | Analyse des failles, incohérences, angles morts | analyse-contrat, consultation-juridique, due-diligence | — |
| `/devil` | Avant | Argumente contre ta propre position | consultation-juridique, contentieux-fiscal | — |
| `/steelman` | Avant | Construit l'argument le plus solide pour une thèse | contentieux-fiscal, consultation-juridique | — |
| `/gaps` | Avant | Identifie ce qui manque dans une analyse | Tous les livrables | — |
| `/verbose` | Avant | Développe chaque point avec profondeur maximale | consultation-juridique, patrimonial-structuring | — |
| `/concise` | Avant | Réponse la plus courte sans perdre l'essentiel | note-information-client, veille-juridique | — |
| `/brutal` | Avant | Direct, sans précautions de forme ni fioritures | Tous (usage interne) | ❌ Jamais sur livrables client |
| `/nohedge` | Avant | Supprime les formules de prudence excessives | Livrables internes | ❌ Jamais sur livrables juridiques clients — obligation de distinguer certitudes/incertitudes |
| `/human` | Avant | Ton chaleureux, naturel, zéro jargon juridique | note-information-client | ❌ Incompatible avec consultations techniques |
| `/bulletproof` | Avant | Structure en points clairs, sans prose superflue | veille-juridique, note-information-client | — |
| `/firstperson` | Avant | Écrit à la 1ʳᵉ personne (style Yoann) | Posts LinkedIn ECA, ghostwriting | ❌ Jamais sur consultations ou actes |
| `/inversethink` | Avant | Part du résultat pour remonter aux causes | diagnostic-transmission, consultation-juridique | — |
| `/compare` | Avant | Compare des options sur critères précis et objectifs | diagnostic-transmission, calcul-plus-value | — |
| `/dashboard` | Après | Tableau de bord interactif (Artifact) | calcul-plus-value (simulations) | — |
| `/calculator` | Après | Outil de calcul interactif (Artifact) | calcul-plus-value | — |
| `/chart` | Après | Graphique ou visualisation de données (Artifact) | veille-juridique, calcul-plus-value | — |
| `/mindmap` | Après | Carte mentale visuelle interactive (Artifact) | diagnostic-transmission | — |
| `/kanban` | Après | Tableau Kanban interactif (Artifact) | Suivi dossiers M&A | — |

---

## 🎯 Cas d'usage types ECA

### Consultations juridiques / fiscales
```
/think [ta question]
/verbose [ta question complexe]
/critique [ta question sur une position fiscale]
```

### Analyse de contrats
```
/critique Analyse ce protocole de cession...
/gaps Voici le pacte d'associés — qu'est-ce qui manque ?
/devil Cette clause de garantie de passif est-elle suffisante ?
```

### Contentieux fiscal
```
/steelman La position de l'administration sur les provisions...
/devil Voici notre argument de défense MISEROLLE — joue l'inspecteur
/think Quelle stratégie pour la Commission des impôts ?
```

### Transmission / structuration patrimoniale
```
/inversethink Objectif = réduire les droits sous X€ — comment y arriver ?
/compare Holding IS vs apport-cession vs Dutreil pour ce dossier
/mindmap Cartographie la transmission de ce groupe familial /mindmap
```

### Notes client / communication
```
/human /concise Explique la règle Dutreil à mon client
/human /bulletproof Résume les enjeux de l'opération
```

### Posts LinkedIn ECA
```
/firstperson /human Rédige un post sur la nouveauté LF 2026 sur...
```

### Simulations chiffrées
```
Calcule la PV sur cette cession /calculator
Compare ces 3 scénarios de transmission /dashboard
```

---

## ⚡ Combinaisons puissantes validées ECA

| Combinaison | Usage |
|------------|-------|
| `/think` + `/critique` | Consultation à enjeu fort — raisonnement visible + identification des failles |
| `/steelman` + `/devil` | Préparation audience contentieuse — tester la solidité des arguments des deux côtés |
| `/verbose` + `/gaps` | Due diligence — profondeur maximale + détection de ce qui manque |
| `/inversethink` + `/compare` | Diagnostic transmission — partir de l'objectif client et comparer les chemins |
| `/human` + `/bulletproof` | Note client — accessible et structurée |
| `/concise` + `/brutal` | Brief interne ECA — aller droit au but sans fioritures |

---

## 🚫 Règles d'exclusion strictes ECA

1. `/nohedge` **interdit** sur tout livrable destiné à un client ou à l'administration fiscale
   → L'obligation de distinguer certitudes / incertitudes reste impérative (charte juridique ECA)

2. `/ghost` / `/human` **interdits** sur consultations, actes, notes juridiques
   → Réservés aux communications non-juridiques (LinkedIn, emails commerciaux)

3. `/firstperson` **interdit** sur tous les livrables officiels ECA
   → Réservé au ghostwriting LinkedIn ou aux communications internes

4. Les codes Artifacts (`/dashboard`, `/calculator`, etc.) ne remplacent pas la vérification Légifrance
   → Un outil interactif de calcul doit toujours être précédé d'une vérification des taux via BOFiP/shared

---

## 🔄 Interaction avec les règles permanentes ECA

Ces codes **ne suspendent jamais** :
- Le mode planification obligatoire (plan → validation → exécution)
- La vérification Légifrance/BOFiP avant toute assertion juridique
- Le legal-hallucination-checker en fin de livrable
- La règle de troncature (⚠️ si fichier partiel)
- La règle quotient 163-0 A / 150-0 B ter (inapplicable)

