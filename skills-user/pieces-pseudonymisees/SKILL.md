---
name: "pieces-pseudonymisees"
description: "Travail sur des pièces pseudonymisées par le Pseudonymiseur local ECA (marqueurs [PERSONNE_1], [SOCIETE_1], [X_1], {{VARIABLE}}) : conserver les marqueurs à l'identique, ne jamais ré-identifier (ni par recherche web ni par connecteur), livrables restaurables. Déclencher dès qu'une pièce ou un texte contient ces marqueurs, ou sur : pièce pseudonymisée, légende des marqueurs, Pseudonymiseur, code affaire AFF-. S'ajoute au skill métier, ne le remplace pas."
---

# Pièces pseudonymisées — règles de travail

## Quand s'applique ce skill

Dès qu'un document, un texte collé ou une légende contient des marqueurs de la forme `[TYPE_N]` (PERSONNE, SOCIETE, ADRESSE, LIEU, IBAN, SIREN, SIRET, TVA, NIR, DATE_NAISSANCE, EMAIL, TELEPHONE, CADASTRE, NUM_FISCAL, REFERENCE, URL, ENTITE), `[X_N]` (caviardage réversible) ou `{{VARIABLE}}` (modèle), ou que Yoann mentionne une « pièce pseudonymisée » ou une « légende des marqueurs ». Ce skill s'ajoute aux skills métier ECA (consultation-juridique, analyse-contrat, redaction-acte…) : il ne les remplace pas.

## Règles impératives

1. **Conserver chaque marqueur à l'identique** : crochets ou accolades, majuscules, tiret bas et numéro compris. Ne jamais écrire « [Personne 1] », « PERSONNE_1 » sans crochets, ni remplacer un marqueur par « le client », « la société » ou un pronom dans les passages où l'identité compte. La restauration automatique dépend de cette exactitude.
2. **Ne jamais créer de nouveau marqueur.** Une personne ou une entité absente de la pièce se désigne par sa fonction (« le notaire instrumentaire », « l'établissement prêteur ») et est signalée comme telle.
3. **Ne jamais chercher à ré-identifier** une personne ou une société : aucune recherche web, **aucun appel à un connecteur nominatif** (Radar, Pennylane, Microsoft 365, Granola, Notion clients, Data.gouv par adresse), aucune lecture de fiche mémoire client pour combler un marqueur, aucun recoupement à partir du contexte (activité, commune, chiffres), aucune hypothèse sur l'identité réelle.
4. **Fuite détectée** : si une donnée identifiante apparaît en clair dans la pièce (nom, IBAN, adresse…), le signaler immédiatement à Yoann sans la reprendre dans la réponse, et lui conseiller de reprendre la pièce dans l'outil.
5. **Raisonner avec la légende** : nature de chaque marqueur, rôle indiqué (cédant, holding…), relations relevées (même nom de famille, dénomination reprenant un nom). Un « même nom de famille » n'établit pas un lien de parenté : si la qualification en dépend (donation, abus de droit, conjoint, héritier), poser la question.
6. **Demander l'attribut, jamais l'identité** : quand la réponse dépend d'une caractéristique de la personne (âge à une date pour le barème de l'usufruit, résidence fiscale, régime matrimonial, lien de parenté, capacité, qualité de dirigeant), demander cette caractéristique pour le marqueur concerné (« âge de [PERSONNE_1] au jour de la donation ? »).
7. **Genre et accords** : s'appuyer sur la civilité conservée devant le marqueur (« Madame [PERSONNE_2] ») ; à défaut, formulation neutre.
8. **Ce qui reste en clair** (articles, BOFiP, jurisprudence, dates d'actes, montants, formes sociales) est soumis aux contrôles habituels : vérification Légifrance / LibreJustice / Legal Data Hunter et legal-hallucination-checker inchangés.

## Livrables restaurables

- Dans un .docx, écrire chaque marqueur en texte courant, d'un seul tenant, avec une mise en forme homogène ; ne pas le placer dans un commentaire, une note, un champ ou une zone de texte.
- Nom de fichier neutre, construit sur le code affaire (ex. `AFF-2026-014_note.docx`), jamais sur un nom réel.
- En fin de livrable, ajouter une ligne : « Marqueurs utilisés : … — à restaurer dans l'onglet Restaurer du Pseudonymiseur avec le référentiel de l'affaire. »
- Mode modèle (`{{VARIABLE}}`) : conserver les variables telles quelles, y compris dans les clauses ajoutées.

## À ne jamais faire

- Demander à Yoann le référentiel, la table de correspondance ou le mot de passe.
- Proposer de « restaurer » soi-même les vraies données dans la réponse.
- Mémoriser une correspondance marqueur ↔ identité d'une conversation à l'autre.