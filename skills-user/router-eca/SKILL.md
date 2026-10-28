---
name: router-eca
description: "Point d'entrée de l'écosystème ECA EXPERTISE quand la demande est floue, mélange plusieurs sujets ou peut relever de plusieurs skills : reformule l'intention, choisit le ou les skills et leur ordre, applique les codes de prompt. Déclencher sur : « j'ai un client qui… », « que faire dans ce cas », « comment traiter », faits bruts sans question, plusieurs opérations mélangées, message commençant par un code (/think, /critique, /gaps…). NE PAS utiliser quand la demande désigne clairement un skill (mot-clé en tête, document joint, livrable précisé) : appeler ce skill directement."
---

# Router ECA

Les descriptions des skills suffisent dans la majorité des cas. Ce skill ne
sert que pour trois choses : **reformuler** une intention floue, **enchaîner**
plusieurs skills dans le bon ordre, **appliquer** un code de prompt.

---

## 1. Codes de prompt

Si le message commence par un code (`/think`, `/critique`, `/devil`,
`/steelman`, `/gaps`, `/verbose`, `/concise`, `/brutal`, `/compare`…) :
appliquer le modificateur décrit dans le référentiel des codes du dépôt
(rechercher « prompt-codes » ; socle § 4), puis router normalement. Les codes
ne suspendent jamais les règles permanentes (vérification, checker, standard
de rédaction). `/nohedge` et `/human` : jamais sur un livrable juridique client.

## 2. Reformulateur d'intention

Activer si au moins **deux** signaux sont présents : pas de mot-clé de skill
en tête ; hésitation (« enfin », « je sais pas trop ») ; plusieurs sujets sans
question centrale ; aucun livrable précisé ; phrase nominale sans verbe
(« MARTIN indivision EURL ALPHA »).

Ne pas activer si : mot-clé de skill en tête, document joint, `→ livrable :`
présent, output Casus collé, code de prompt seul avec demande claire.

Sortie unique, rien d'autre :
```
📋 REFORMULATION — avant d'exécuter
Dossier/client    : [fiche mémoire / historique, ou « ? »]
Opération         : [1 ligne]
Question centrale : [1 phrase]
Skill(s)          : [skill A → skill B]
Livrable          : [consultation Word / acte / calcul / note client / mail]
→ Je lance sur cette base ? « go » ou corrige.
```
« go » → exécuter ; correction courte → intégrer et exécuter ; silence ou
changement de sujet → ne rien exécuter.

## 3. Table de routage

| Signal dominant | Skill |
|---|---|
| Contrat ou clause fourni (hors titres, GAP, pacte, fonds, LOI) | analyse-contrat |
| Pacte d'associés, avenant, clauses de sortie | pacte-associes |
| Lettre d'intention, term sheet, offre indicative (titres ou fonds) | lettre-intention |
| Protocole ou promesse de cession de titres sous conditions, cession simple en un temps | protocole-cession |
| Acte définitif, réitération, closing après levée des conditions (titres) | acte-definitif-titres |
| Garantie d'actif et de passif | gap |
| Cession de fonds de commerce ou artisanal (compromis, acte définitif) | cession-fonds |
| Audit de cible, data room | due-diligence-juridique |
| Holding, apport de titres par une personne physique, 150-0 B ter | holding-apport |
| Fusion, fusion simplifiée, scission, apport partiel d'actif, choix TUP ou fusion | restructurations |
| Dissolution, liquidation, exécution d'une TUP | dissolution-liquidation-tup |
| Approbation des comptes, dividendes, capitaux propres, premier exercice, dossier repris | juridique-annuel |
| Statuts, PV, nomination, dénomination, siège, objet, date de clôture, prorogation, capital, transformation | redaction-acte |
| Question de droit ou de fiscalité, consultation | consultation-juridique |
| Transmission, patrimoine, donation, succession, régime matrimonial | strategie-patrimoniale |
| Évaluation de titres ou d'un fonds, sortie ou rachat d'un associé, valeur d'un bloc, barème | evaluation-titres-fonds |
| Chiffrage d'impôt sur une cession | calcul-plus-value |
| Contrôle fiscal, rectification, réclamation | contentieux-fiscal |
| Texte ou décision nouvelle, veille | veille-juridique |
| Note, courrier, mail pour un client ou un collègue | note-information-client |
| Relecture adverse d'un acte ou d'un argument | avocat-adverse |
| Évaluer ou optimiser un skill | darwin-skill |
| Mise à jour des skills, contrôle périodique des références citées, effet d'une loi de finances sur les skills | maintenance-skills |
| Faits bruts → fabriquer la question pour Casus / Claude | prompt-builder-eca |
| Pièce avec marqueurs [PERSONNE_1]… | pieces-pseudonymisees (en surcouche) |

Transverses toujours actifs : `socle-eca`, `positions-eca`,
`legal-hallucination-checker` (fin de livrable).

## 4. Enchaînements fréquents

| Situation | Ordre |
|---|---|
| Dirigeant qui veut céder | strategie-patrimoniale → calcul-plus-value → holding-apport ou protocole-cession |
| Acquisition de titres (camp acquéreur) | lettre-intention → due-diligence-juridique → protocole-cession → gap → acte-definitif-titres → avocat-adverse |
| Cession de titres (camp cédant) | calcul-plus-value → lettre-intention (analyse ou contre-proposition) → protocole-cession → gap → acte-definitif-titres |
| Reprise d'un fonds | lettre-intention → due-diligence-juridique (allégée) → cession-fonds (compromis puis acte définitif) → avocat-adverse |
| Sortie ou rachat d'un associé | evaluation-titres-fonds → calcul-plus-value (cédant) → protocole-cession (cession simple) ou redaction-acte (réduction de capital) |
| Entrée d'un associé ou d'un salarié | consultation-juridique (mécanisme) → protocole-cession (cession simple) ou redaction-acte (augmentation) → pacte-associes |
| Simplification d'un groupe | restructurations (Phase 1 : TUP, fusion simplifiée ou APA) → dissolution-liquidation-tup si TUP retenue → redaction-acte (statuts de la bénéficiaire) |
| Filialisation d'une activité exploitée par une société | restructurations (APA) → pacte-associes si entrée d'un tiers |
| Clôture d'exercice avec distribution | juridique-annuel (→ calcul si arbitrage rémunération / dividendes) |
| Réforme et clients concernés | veille-juridique → note-information-client |
| Contrôle fiscal | contentieux-fiscal → note-information-client (client) |

Annoncer l'enchaînement en une ligne : « Cette demande active [A] pour [x],
puis [B] pour [y]. » Ne jamais fusionner deux cadres en silence.

## 5. Ambiguïté résiduelle

Une seule question discriminante, puis attendre la réponse. Exemple :
« Ton client a-t-il déjà choisi l'opération, ou cherche-t-il encore la
meilleure stratégie ? »
