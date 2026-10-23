---
name: holding-apport
description: >
  Création d'une holding et apport de titres (ou de fonds) pour ECA EXPERTISE :
  choix de l'opération (apport, apport-cession, cession à soi-même / OBO),
  report d'imposition 150-0 B ter, commissaire aux apports, traité d'apport,
  statuts de la holding, nomination de la holding comme dirigeante, conventions
  d'animation ou de prestations, régime mère-fille et intégration, suivi annuel
  du report. Déclencher sur : holding, apport de titres, apport en nature,
  apport-cession, 150-0 B ter, traité d'apport, commissaire aux apports, holding
  présidente, holding animatrice, convention d'animation, management fees,
  filialisation, OBO, réinvestissement, attestation de report.
  NE PAS utiliser en phase exploratoire sans opération choisie
  (→ strategie-patrimoniale), pour un pur chiffrage (→ calcul-plus-value) ou
  pour un apport d'immeuble isolé sans holding (→ consultation-juridique).
---

# Holding et apport — ECA EXPERTISE

Opération récurrente du cabinet : un dirigeant apporte ses titres à une holding
qu'il contrôle, souvent avant une cession, une transmission, une exigence
bancaire ou une recomposition de la gouvernance. L'enjeu est de sécuriser à la
fois le **report d'imposition**, la **valeur d'apport** et la **gouvernance**.

Charger `socle-eca`. Rédaction : étapes 3 à 8 de `redaction-acte`.

---

## Phase 0 — Qualification de l'objectif

Identifier l'objectif réel (une ligne) : préparer une cession, transmettre,
répondre à une exigence bancaire, faire entrer un associé ou un salarié,
remonter de la trésorerie, structurer un groupe, désigner une holding
dirigeante. L'objectif conditionne l'outil ; s'il n'est pas tranché, renvoyer
vers `strategie-patrimoniale`.

## Phase 1 — Données

Ouverture du dossier (socle § 1). Collecter : capital et détention de la société
apportée, forme et statuts (agrément applicable à l'apport ?), pacte existant,
valorisation et méthode, comptes (Pennylane : capitaux propres, trésorerie,
résultats), projet de cession éventuel (calendrier, prix), régime matrimonial de
l'apporteur (titres communs → consentement), démembrements, garanties bancaires.

## Phase 2 — Analyse et points d'entrée (à lire en vigueur)

| Sujet | Contrôle | Points d'entrée |
|---|---|---|
| Report d'imposition | Condition de contrôle de la holding, obligations de conservation, cession dans le délai et réinvestissement (quotité, nature, délai), déclarations annuelles | CGI art. 150-0 B ter (version à la date de l'apport, LF récentes) + BOFiP correspondant via Legal Data Hunter |
| Coût global | Purge vs report, CEHR et CDHR des années concernées | Renvoi `calcul-plus-value` ; CGI art. 223 sexies et 224 |
| Abus de droit | Substance de la holding, réinvestissement économique, calendrier | LPF L. 64 et L. 64 A ; jurisprudence récente (Légifrance + LibreJustice) |
| Valeur d'apport | Méthode, cohérence avec une cession proche, surévaluation | Rapport du commissaire aux apports |
| Commissaire aux apports | Obligation ou dispense selon la forme et les seuils en vigueur ; responsabilité des associés en cas de dispense | C. com. L. 223-9 (SARL), L. 225-147 (SA, SAS par renvoi), textes réglementaires des seuils |
| Agrément et préemption | Apport = mutation soumise aux clauses statutaires et au pacte | Statuts et pacte de la société apportée |
| Droits d'enregistrement | Apport pur et simple / à titre onéreux (prise en charge de passif) | CGI art. 809 et 810 |
| Holding dirigeante | Personne morale présidente ou gérante selon la forme ; représentant ; responsabilité ; marchés publics et qualifications | C. com. L. 227-7 (SAS) ; impossibilité pour une personne morale d'être gérante de SARL — vérifier |
| Remontée de dividendes | Régime mère-fille (taux de détention, conservation), quote-part de frais et charges ; intégration fiscale | CGI art. 145 et 216 ; art. 223 A s. |
| Holding animatrice | Critères d'animation (Dutreil, IFI, PV) ; convention d'animation et prestations facturées distinctes | Jurisprudence Cass. com. et CE ; BOFiP ; base Positions ECA |
| Conventions intragroupe | Prix de marché, conventions réglementées, TVA des prestations | C. com. conventions réglementées ; CGI art. 57 si international |

## Phase 3 — Schéma et séquence

Présenter un schéma (avant / après) et une **séquence datée** : constitution de
la holding ou apport à une holding existante ; rapport du commissaire ; traité ;
décisions de la société apportée (agrément) ; décisions de la holding
(augmentation de capital) ; nomination de la holding dirigeante ; conventions ;
formalités ; déclarations du report.

**Point de contrôle : validation du schéma et de la séquence par Yoann.**

## Phase 4 — Actes à produire

Partir des précédents du dépôt (socle § 4 : traité d'apport, attestation de
report, nomination du commissaire, statuts de holding) :
1. Statuts de la holding (ou modification) — standard socle § 6.
2. Décision de nomination du commissaire aux apports (ou décision de dispense
   motivée, si permise, avec l'avertissement de responsabilité).
3. **Traité d'apport** : parties, définitions, désignation des titres, origine
   de propriété, valeur et méthode, rémunération (titres émis, soulte limitée),
   date d'effet, déclarations et garanties de l'apporteur, régime fiscal
   (report, engagements), conditions suspensives, pouvoirs.
4. Décisions d'agrément de la société apportée ; décision d'augmentation de
   capital de la holding ; ordre de mouvement ; formalités.
5. Nomination de la holding comme dirigeante ; démission corrélative ;
   rémunération de la holding (convention de prestations ou d'animation),
   conventions réglementées à prévoir.
6. Attestation et déclarations du report ; **fiche de suivi annuel** du report
   (déclaration annuelle, délai de cession et de réinvestissement).

## Phase 5 — Contrôles

- Cohérence des valeurs entre rapport, traité, statuts, déclarations.
- Calendrier de cession et de réinvestissement en « Échéances ».
- `legal-hallucination-checker` (bloquant) ; `avocat-adverse` si un tiers
  (banque, acquéreur, associé minoritaire) est partie ; `positions-eca`.
