---
name: calcul-plus-value
description: >
  Calcul ou estimation de plus-value pour ECA EXPERTISE : immobilière (immeuble,
  terrain, parts de SCI ou de société à prépondérance immobilière, LMNP,
  non-résidents), mobilière (parts sociales, actions, BSPCE, actifs numériques,
  PEA, actions gratuites, management package), professionnelle (BIC, BNC, BA,
  marchand de biens), à l'IS (titres de participation), report et sursis
  (150-0 B, 150-0 B ter), exit tax, CEHR, CDHR, comparaison de scénarios de
  cession. Déclencher sur : calcul plus-value, impôt cession, PV immobilière,
  PV mobilière, cession titres, vente immeuble, CEHR, CDHR, Quémener, BSPCE,
  LMNP, 244 bis, abattement retraite, purge du report, « combien je vais payer
  si je vends ». NE PAS utiliser si la demande est purement stratégique sans
  données chiffrées (→ strategie-patrimoniale) ou porte sur des droits de
  donation ou de succession seuls (→ strategie-patrimoniale).
---

# Calcul de plus-value — ECA EXPERTISE

> **Socle** : charger `socle-eca` (ouverture du dossier, connecteurs,
> vérification, pièges datés § 5, Word, fin de livrable). Aucun taux, seuil,
> abattement ou barème n'est repris de mémoire ni de ce skill : chacun se lit à
> la source, **dans sa version applicable à la date de la cession**.

Chaque type de plus-value obéit à un régime distinct et étanche. Confondre les
régimes coûte des dizaines de milliers d'euros au client. Le calcul est
**exécuté par script** (jamais de tête) et chaque paramètre est sourcé.

---

## Phase 0 — Données et aiguillage

```
Données chiffrées disponibles (prix, prix de revient, dates) ? → continuer
Phase exploratoire, données manquantes                     → strategie-patrimoniale
Question de régime à trancher d'abord                       → consultation-juridique
```

Données à réunir (socle § 1 ; Pennylane si client du cabinet ; Data.gouv
(valeurs foncières) pour étayer une valeur immobilière ; Legal Data Hunter pour
une convention fiscale) :
- cédant : personne physique / société IR / société IS ; résidence fiscale ;
  situation familiale et RFR prévisible (CEHR, CDHR) ;
- bien : nature, date et mode d'acquisition (onéreux / gratuit / apport),
  prix ou valeur d'origine, frais, travaux, amortissements, démembrement ;
- cession : date, prix, compléments de prix, comptes courants inclus ou non ;
- antécédents : reports ou sursis en cours, abattements déjà utilisés.

Paramètre manquant : `⚠️ INCERTAIN — [paramètre] : hypothèse retenue [X].
Résultat à recalculer si différent.`

## Phase 1 — Qualification (arbre)

```
Q1 Activité habituelle d'achat-revente ?              OUI → marchand de biens (BIC)
Q2 Bien inscrit à l'actif d'une entreprise IR ?        OUI → PV professionnelle
Q3 Cédant soumis à l'IS ?                              OUI → PV à l'IS
Q4 Cédant non-résident ?                               OUI → prélèvement spécifique
                                                            (immobilier / titres) + convention
Q5 Nature du bien :
   immeuble, droit immobilier, parts de société IR à prépondérance immobilière
        → PV immobilière des particuliers (+ correctif Quémener sur parts)
   meublé (LMNP)          → PV immobilière avec minoration du prix d'acquisition
                            par les amortissements, sous réserve des exceptions
                            (socle § 5)
   parts d'une société de personnes où le cédant exerce → PV professionnelle
   titres de société IS   → PV mobilière des particuliers
   régimes spéciaux       → BSPCE, actifs numériques, management package,
                            actions gratuites, PEA
```
Annoncer le régime retenu et pourquoi ; si deux régimes sont plausibles,
chiffrer les deux.

## Phase 2 — Sources à lire pour le régime retenu

| Régime | Textes à lire (version à la date de cession) | Doctrine |
|---|---|---|
| PV immobilière PP | CGI art. 150 U à 150 VH ; surtaxe art. 1609 nonies G ; prélèvements sociaux CSS L. 136-7 et L. 136-8 | BOFiP RFPI-PVI (Legal Data Hunter) |
| LMNP | CGI art. 150 VB III (et ses exceptions) | BOFiP correspondant ; module de formation du dépôt sur l'immobilier |
| PV mobilière PP | CGI art. 150-0 A à 150-0 E, 200 A ; abattements éventuels (dont départ à la retraite art. 150-0 D ter) | BOFiP RPPM-PVBMI |
| Report / sursis | CGI art. 150-0 B, 150-0 B ter ; état de suivi annuel | BOFiP RPPM-PVBMI-30 |
| PV professionnelle | CGI art. 39 duodecies s. ; exonérations art. 151 septies, 151 septies A, 238 quindecies, 151 nonies selon le cas | BOFiP BIC-PVMV |
| PV à l'IS | CGI art. 219 I a quinquies (titres de participation) ; taux d'IS en vigueur | BOFiP IS-BASE |
| Non-résidents | CGI art. 244 bis A, 244 bis B ; convention fiscale | Legal Data Hunter (convention) |
| Contributions | CEHR art. 223 sexies ; CDHR art. 224 ; prélèvements sociaux CSS L. 136-8 | — |
| Exit tax | CGI art. 167 bis | BOFiP |

Pour chaque paramètre utilisé (taux, abattement, seuil), noter : texte, version,
date de lecture. Ces paramètres alimentent le script de calcul.

## Phase 3 — Calcul

1. Écrire un script (Python) dont chaque paramètre est une variable nommée et
   sourcée en commentaire ; l'exécuter ; joindre le détail.
2. Positions ECA à appliquer (socle § 5 et base Positions) :
   - report 150-0 B ter et quotient : **deux thèses, deux chiffrages**, rescrit
     recommandé ; jamais « acquis » ni « inapplicable » ;
   - CDHR chiffrée dans **chaque** scénario comparé.
3. Comparaison de scénarios si pertinent : cession directe / apport-cession /
   donation avant cession / purge du report — mêmes hypothèses, mêmes années.

## Phase 4 — Sortie

```
CALCUL DE PLUS-VALUE — [Client — Date — YD]

I.   QUALIFICATION — régime, base légale, motifs (et régime alternatif écarté)
II.  PARAMÈTRES — tableau : paramètre / valeur / texte et version / date de lecture
III. CALCUL — prix de cession, prix de revient corrigé (détail), PV brute,
     abattements et correctifs, PV nette
IV.  IMPOSITION — impôt sur le revenu ou IS, prélèvements sociaux, surtaxe,
     CEHR, CDHR, total et taux effectif
V.   SCÉNARIOS COMPARÉS (le cas échéant)
VI.  OBLIGATIONS DÉCLARATIVES — formulaires et délais lus à la source
VII. POINTS D'INCERTITUDE et hypothèses à confirmer
```

Droits de donation ou de succession demandés en complément → renvoi
`strategie-patrimoniale` (le barème et les abattements se lisent à la source).

## Checklist avant remise

- [ ] Régime qualifié et justifié ; alternative chiffrée si doute
- [ ] Chaque paramètre sourcé avec sa version et sa date de lecture
- [ ] Calcul exécuté par script, résultat recoupé
- [ ] Positions ECA appliquées (150-0 B ter ; CDHR dans chaque scénario)
- [ ] Obligations déclaratives mentionnées
- [ ] Incertitudes balisées
- [ ] Fin de livrable du socle § 9 (checker bloquant, positions, échéances)
