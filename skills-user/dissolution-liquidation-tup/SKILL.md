---
name: dissolution-liquidation-tup
description: >
  Fin de vie et restructuration simplifiée des sociétés pour ECA EXPERTISE :
  dissolution anticipée, liquidation amiable (dont liquidation « éclair »),
  comptes de liquidation, partage, boni ou mali, transmission universelle de
  patrimoine (TUP) d'une société détenue à 100 %, radiation. Couvre les SCI à
  l'IR et à l'IS, les sociétés commerciales et la fiscalité des associés.
  Déclencher sur : dissolution, liquidation, liquidateur, boni de liquidation,
  mali, comptes de clôture, radiation, TUP, transmission universelle de
  patrimoine, 1844-5, dissolution sans liquidation, mise en sommeil, partage,
  attribution d'un bien à un associé. NE PAS utiliser pour une fusion classique
  avec traité (→ consultation-juridique) ni pour une cession de titres
  (→ protocole-cession).
---

# Dissolution, liquidation, TUP — ECA EXPERTISE

Ces opérations paraissent simples et ne le sont pas : le traitement fiscal du
boni, l'attribution d'un immeuble, le sort des comptes courants et le calendrier
des oppositions concentrent les erreurs.

Charger `socle-eca`. Rédaction : étapes 3 à 8 de `redaction-acte`.

---

## Phase 0 — Choix de la voie

```
Associé unique personne morale, société saine     → TUP (dissolution sans liquidation)
Plusieurs associés ou associé personne physique   → DISSOLUTION + LIQUIDATION AMIABLE
Activité suspendue, reprise possible              → MISE EN SOMMEIL (comparer le coût)
Actif immobilier à attribuer à un associé         → LIQUIDATION avec attribution / partage
                                                     (forme authentique si immeuble)
```
Présenter les voies possibles avec leur coût fiscal et leur calendrier ;
**point de contrôle** avant de rédiger.

## Phase 1 — Données

Ouverture du dossier (socle § 1). Pennylane : bilan à date (actif réalisable,
passif, comptes courants, capitaux propres, provisions), résultats antérieurs.
Statuts, associés et leur régime fiscal (IR / IS, résidence fiscale), actifs
immobiliers, contrats en cours (baux, crédits, crédits-baux), dettes fiscales et
sociales, salariés.

## Phase 2 — Points d'entrée (à lire en vigueur)

| Sujet | Contrôle | Points d'entrée |
|---|---|---|
| TUP | Conditions, délai d'opposition des créanciers, date d'effet, effet fiscal | C. civ. art. 1844-5 al. 3 ; régime de faveur CGI art. 210 A et option, obligations post-opération |
| Dissolution anticipée | Organe et majorité, publicité, mention « en liquidation » | Statuts ; C. civ. art. 1844-7 ; C. com. L. 237-1 s. |
| Liquidateur | Nomination, pouvoirs, durée, rapport | C. com. L. 237-2 s. ; C. civ. art. 1844-8 |
| Comptes de clôture et partage | Approbation, quitus, partage du boni, attribution en nature | C. com. L. 237-9 s. ; C. civ. art. 1844-9 |
| Boni de liquidation — associé PP | Part représentant le remboursement des apports / le surplus imposable ; prélèvements sociaux | CGI art. 112 et 161 ; règles des PV de cession selon le cas — **chiffrer** via `calcul-plus-value` |
| Boni — associé personne morale | Régime mère-fille sur la fraction distribuée, plus-value / moins-value sur titres | CGI art. 145, 216, 219 |
| SCI à l'IR | Correctif de calcul de la plus-value sur parts (quotes-parts imposées / déficits) | Jurisprudence Quémener et suites ; BOFiP |
| SCI à l'IS | Imposition du boni et de l'actif réévalué, partage d'un immeuble | CGI art. 221 ; droits de partage art. 746 |
| Associés non-résidents | Retenue à la source, convention fiscale applicable | Legal Data Hunter (convention) ; CGI art. 119 bis |
| Droits d'enregistrement | Dissolution, partage, attribution | CGI art. 811, 746 et s. |
| Formalités | Publicité, dépôt, radiation, déclaration de cessation | Formalités en vigueur (guichet unique) |

## Phase 3 — Actes

Partir des précédents du dépôt (socle § 4 : décisions de dissolution, de
liquidation, conventions d'abandon de compte courant, crédit-vendeur) :
1. Décision de dissolution (ou de TUP) — standard socle § 6.
2. Nomination du liquidateur, siège de la liquidation.
3. Pendant la liquidation : actes de réalisation de l'actif, apurement,
   abandon ou remboursement des comptes courants (avec leurs effets fiscaux).
4. Comptes de liquidation, quitus, répartition du boni (tableau de partage
   arithmétiquement vérifié par calcul), clôture.
5. Pouvoirs et formalités.

## Phase 4 — Calendrier et contrôles

Rétroplanning : publicité, délai d'opposition (TUP), arrêté des comptes,
clôture, radiation, déclarations fiscales de cessation et de résultat de
liquidation. Délais lus à la source, jours qualifiés.

Puis `legal-hallucination-checker` (bloquant), `positions-eca`, « Échéances ».

---

## Pièges récurrents

- Liquidation « éclair » sans réalisation effective de l'actif ni comptes de
  clôture : risque de remise en cause.
- Boni imposé en bloc sans distinguer le remboursement des apports.
- Attribution d'un immeuble à un associé sans forme authentique ni chiffrage
  des droits de partage.
- TUP : oublier l'option fiscale et les obligations déclaratives qui la
  conditionnent.
