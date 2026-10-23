---
name: socle-eca
description: "Socle commun de tous les skills ECA EXPERTISE (remplace « shared ») : ouverture de dossier, carte des connecteurs (quel besoin → quel outil), règles de vérification, pièges datés, standard de rédaction M&A international, corpus documentaire évolutif du dépôt (inventaire du jour, recherche plein texte, lecture intégrale du verbatim des documents pertinents), charte et méthode Word ECA, garde-fous (pseudonymisation, périmètre, confidentialité). Chargé automatiquement par tout skill métier ECA. Déclencher sur : socle, shared, référentiel ECA, charte, méthode Word, carte des connecteurs, pièges fiscaux, corpus, Royal Formation, accès dépôt. NE PAS utiliser seul pour répondre à une question de fond : il équipe les autres skills."
---

# Socle ECA EXPERTISE

Ce fichier contient des **règles et des process**, pas des données. Un taux, un
seuil, un délai chiffré ou un numéro de jurisprudence ne s'écrit jamais de
mémoire ni depuis un skill : il se lit à la source, au jour du livrable, dans la
version applicable au fait générateur. Exceptions : la liste courte des pièges
(§ 5), datée et sourcée, qui sert d'alarme, et les références marquées
« vérifié JJ/MM/AAAA » dans les skills. Les unes et les autres sont inscrites à
l'index des références du dépôt (rechercher « references-index ») et
contrôlées par `maintenance-skills` ; elles se relisent à la source avant tout
usage, dans la version applicable.

---

## 1. Ouverture de tout dossier — exécuter dans cet ordre

```
1. Mémoire dossier   → si un client, une société ou une personne est nommé :
                       consulter la liste mémoire, lire la fiche /areas/<dossier>.md
                       (et /people/ concernés). C'est la source la plus fiable.
2. Historique        → recherche dans les conversations passées sur le nom exact.
3. Réunions / mails  → Granola (compte rendu du dernier RDV) et Microsoft 365
                       (échanges et pièces) si le dossier est actif.
4. Identité légale   → Radar (fiche entreprise, dirigeants, structures du
                       dirigeant). Sauf pièce pseudonymisée (§ 7.1).
5. Données comptables→ Pennylane si le chiffre conditionne la réponse
                       (balance, capitaux propres, comptes courants, résultat).
6. Positions ECA     → skill positions-eca (base Notion « 📌 Positions ECA »).
7. Corpus            → inventaire du jour, recherche plein texte sur tout le
                       corpus, lecture intégrale des documents pertinents (§ 4 bis).
8. Annoncer en une ligne : « Suite du dossier X — [dernier état] » ou
                       « Nouveau dossier ».
```

Ne pas bloquer sur une demande générique sans nom propre : passer directement au § 2.
Un dossier déjà engagé ne repart jamais de zéro.

**Planification (règle permanente)** : pour toute tâche non triviale
(consultation, acte, analyse multi-sections), présenter un plan numéroté et
attendre la validation de Yoann avant de rédiger. Si la direction s'avère
fausse en cours de route, s'arrêter et replanifier.

---

## 2. Carte des connecteurs — quel besoin, quel outil

Le skill nomme le **besoin** ; la syntaxe d'appel se lit dans le schéma de
l'outil au moment de l'utiliser (ne jamais la recopier dans un skill : elle
change). Si un outil est indisponible, le dire et passer au suivant.

| Besoin | Outil principal | Recoupement |
|---|---|---|
| Article de code en vigueur | Légifrance | LibreJustice |
| Article **à une date donnée** (fait générateur, cession, donation) | LibreJustice (version à date) | Légifrance |
| Loi, ordonnance, décret, JORF du jour | Légifrance | LibreJustice |
| Doctrine BOFiP | Legal Data Hunter (doctrine FR) | LibreJustice (BOFiP par identifiant) |
| Jurisprudence administrative fiscale (CE, CAA, TA) | Légifrance | LibreJustice, Legal Data Hunter |
| Jurisprudence judiciaire (Cass., CA) | Pourvoi (portée, parcours procédural) | Légifrance, LibreJustice |
| Droit de l'Union, CJUE, TVA intracom, mère-fille | OpenEU | Pourvoi (CJUE), LibreJustice |
| Droit étranger, conventions fiscales, non-résidents | Legal Data Hunter | — |
| Conventions collectives | Légifrance | — |
| Identité d'une société, dirigeants, groupe | Radar | Data.gouv |
| Valeurs immobilières de marché (DVF) | Data.gouv | — |
| Comptes d'un client du cabinet | Pennylane (lecture seule) | — |
| Compte rendu de rendez-vous | Granola | — |
| Mails, pièces, agenda | Microsoft 365 (brouillons uniquement, jamais d'envoi sans accord) | — |
| Positions du cabinet, veille, consultations | Notion | — |
| Slides de veille | Gamma | — |
| Doctrine, formation et documents de référence internes (tout document présent dans le dépôt le jour de la demande) | Dépôt GitHub (§ 4 bis) | Source primaire |

Identifiants Notion (les vérifier par une recherche si une requête échoue) :
- Positions ECA : collection `6dc1e530-7996-4a62-b5b6-b378b4c8f204`
- Veille juridique ECA : `f201a44e-556f-4420-8f61-eec1f8cb2d5a`
- Consultations : `cadd1870-11e1-4dfa-9298-7d5c5977f564`
- Clients : `9f595806` (identifiant court — compléter par recherche)

⚠️ Ne jamais confondre la base Positions (6dc1e530) et la base Veille (f201a44e).

---

## 3. Règles de vérification

1. **Toute référence citée** (article, décision, BOFiP, texte) est vérifiée
   avant citation, puis contrôlée en fin de livrable par
   `legal-hallucination-checker` — intégralement, sans exception pour les
   articles « connus ».
2. **Version applicable** : un texte fiscal se lit dans sa version en vigueur à
   la date du fait générateur, pas seulement aujourd'hui.
3. **Trois niveaux, toujours distingués** dans le livrable : certitude
   textuelle / position doctrinale ou jurisprudentielle / zone d'incertitude.
   Balise : `⚠️ INCERTAIN — [point] : [raison]. À vérifier via [source].`
4. **Position fiscale donnée par Yoann ou par Casus** : la vérifier avant de
   l'intégrer (« Tu me donnes cette position — je la vérifie avant de
   l'incorporer »). Un output Casus collé reste une base documentaire à
   recouper, jamais une source qui dispense de vérifier un point contesté.
5. **Inexistence** : une référence n'est déclarée introuvable qu'après échec
   sur tous les outils compétents (voir matrice du checker). « Non trouvé » ≠
   « inexistant ».
6. **Lecture tronquée** : si un fichier est lu partiellement, le signaler
   avant tout livrable.
7. **Délai, durée d'engagement, taux** : sans source vérifiée, s'arrêter et le
   dire. Ne jamais estimer.

---

## 4. Accès au dépôt de modèles et au corpus

Dépôt : `ydecreton-a11y/eca-expertise-templates` (public).

**Méthode** : cloner le dépôt (copie légère, une seule fois par session), puis
**rechercher** le document pertinent par type d'acte, par titre et par
mots-clés — ne jamais se fier à un chemin écrit dans un skill. Lister le contenu
réel du dossier concerné avant de choisir.

```
Accès : clone de la session (dépôt rattaché) ; à défaut, clone public.
        Si aucun accès : le dire, demander le fichier à Yoann.
Recherche : lister les dossiers, puis filtrer par nom de fichier et par contenu
        (extraction texte des .docx/.pdf ; reconnaissance de texte si PDF scanné ;
        conversion préalable des .doc).
```

Règles d'usage :
- Pour toute rédaction d'acte, partir **par défaut** d'un modèle du dépôt (règle
  permanente de Yoann, sauf ordre contraire exprès).
- Les fichiers du dépôt issus de dossiers réels sont des **précédents**, pas
  des modèles neutres : n'en reprendre ni nom, ni chiffre, ni donnée d'un autre
  client (erreur type relevée : article au nom d'un tiers resté par copier-coller).
- Avant usage, vérifier toutes les références légales du modèle (règle
  permanente) : signaler tout écart et proposer la clause corrigée.
- Si une ressource attendue manque : le signaler dans le livrable
  (« Ressource absente : [objet] ») et poursuivre par sources primaires.

### 4 bis. Corpus documentaire — base secondaire de toute réponse, **évolutive**

Le dépôt contient, outre les modèles d'actes, des documents de doctrine, de
formation et de référence que Yoann **enrichit en continu** (tous formats). Ce
corpus est la base documentaire secondaire de **toute** demande juridique ou
fiscale. Il ne se limite jamais à une liste figée : ce qui compte est ce qui se
trouve dans le dépôt **le jour de la demande**.

**Process obligatoire, à chaque demande :**

1. **Inventaire du jour** — lister **tous** les fichiers du dépôt (hors `.git`),
   quel que soit leur dossier ou leur nom, avec format, taille, nombre de pages
   ou de mots et sommaire (titres, première page). Un document ajouté la veille
   est traité comme les autres ; aucun document n'est écarté parce qu'il ne
   figure pas dans le tableau ci-dessous.
2. **Extraction intégrale** — extraire le texte complet de chaque document :
   .docx (paragraphes, tableaux, notes, commentaires, passages surlignés),
   .pdf (texte ; reconnaissance de texte si scanné ou si des pages sont des
   images), .md / .txt, .xlsx / .csv (toutes les feuilles), .doc et .pptx après
   conversion, images par lecture visuelle. Signaler tout fichier illisible.
3. **Recherche plein texte sur 100 % du corpus** — chercher les notions de la
   demande (termes juridiques, synonymes, articles, régimes, noms d'opérations)
   dans le texte **complet** de chaque document, pas seulement dans les titres.
4. **Lecture intégrale du verbatim** — pour chaque document qui traite du sujet :
   lire **100 % de son texte**, mot à mot, et non un résumé, des extraits ou les
   seuls passages trouvés par la recherche. Pour un ouvrage en plusieurs
   parties : lire intégralement chaque partie pertinente, son sommaire et les
   annexes auxquelles elle renvoie. Si le volume dépasse ce qui tient en une
   lecture, lire par passes successives jusqu'à la fin, en relevant les passages
   utiles avec leur page ou leur section. Contrôle : mots lus = mots extraits ;
   sinon, le signaler (§ 3.6) avant tout livrable.
5. **Exploitation** — en tirer l'analyse, les pièges, les cas pratiques, les
   décisions et références citées ; vérifier chacune à la source primaire avant
   de la reprendre (§ 3).
6. **Traçabilité** — indiquer dans la réponse : « Corpus consulté : [documents],
   lus intégralement » ; ou « Recherche plein texte sur l'ensemble du corpus :
   aucun document ne traite de [sujet] ». Ne jamais affirmer avoir lu un document
   qui ne l'a pas été en entier.

**Repères au 23/10/2026 — exemples, liste non limitative** (le corpus réel est
celui de l'inventaire du jour) :

| Document (titre) | Contenu | Sujets typiques |
|---|---|---|
| Dossier **DUTREIL 2026** (document maître, checklists, index des sources, note Cass. com. 28/05/2026) | Régime Dutreil après la LF 2026 | Transmission à titre gratuit, holding animatrice, trésorerie excédentaire |
| **Actualités juridiques et fiscales 2026 — gestion de patrimoine** (Royal Formation, Henry Royal) | Fiches LF et LFSS 2026, jurisprudence du 1er semestre 2026 | Toute question patrimoniale ou fiscale récente |
| **Démembrement de l'immobilier d'entreprise** (11 parties, juillet 2023) | Acquisition démembrée, valorisation, cession d'usufruit, sécurisation, cas pratiques | Immeuble professionnel démembré, OBO, SCI à l'IS |
| **Revue Fiduciaire — L'essentiel du patrimoine privé**, chapitres 5 et 6 | Protection et opérations patrimoniales des mineurs | Donation à un mineur, mineur associé |
| **Modules AUREP** | Supports de formation thématiques | Sujet du module |
| **Résidence fiscale des particuliers 2026** | Domicile fiscal, non-résidents, exit tax | Mobilité internationale |
| **Guide du régime social des locations meublées** (juillet 2026) | Affiliation LMNP / LMP | Cotisations des loueurs en meublé |

Règles :
- **Source secondaire** : tout ce qui en est tiré est vérifié à la source
  primaire avant d'être cité ; le corpus ne remplace jamais Légifrance,
  LibreJustice, Legal Data Hunter ou Pourvoi.
- **Date** : comparer la date du document aux textes en vigueur ; un document
  antérieur à une loi de finances est relu à la lumière de celle-ci.
- **Écart** entre un document et la source primaire : retenir la source primaire
  et signaler l'écart à Yoann, en proposant la correction du document du dépôt.
- **Nouveau document** repéré à l'inventaire : le signaler en une ligne à Yoann
  lors de sa première utilisation (titre, objet) ; s'il constitue une ressource
  durable, proposer de l'ajouter aux repères ci-dessus.
- **Documents clients** du dépôt (actes, consultations nominatives) : servent de
  précédents (§ 4), jamais à reprendre de données d'un autre client.

---

## 5. Pièges datés — alarmes, pas valeurs de calcul

Chaque ligne indique la date et la source de sa dernière vérification. Avant
tout usage chiffré : relire la source dans sa version au fait générateur.
Si la source a changé : corriger, signaler à Yoann, mettre à jour cette liste et
l'index des références (`maintenance-skills`).

| Piège | Ce qu'il faut savoir | Vérifié | Source à relire |
|---|---|---|---|
| Prélèvements sociaux du patrimoine | Les taux de CSG sont **différenciés** selon la nature du revenu (dividendes/PV mobilières ≠ revenus fonciers et PV immobilières). Ne jamais appliquer un taux global unique de mémoire (piège historique : 17,2 % / PFU 30 %). | 23/10/2026 — version en vigueur au 27/06/2026 (loi 2026-534) | CSS art. L. 136-8 (I 2° et IV) + CGI art. 200 A et 235 ter |
| LMNP — réintégration des amortissements | Le prix d'acquisition est minoré des amortissements déduits, **mais** des exceptions ont été ajoutées (résidences étudiants/seniors, établissements médico-sociaux…) par la LF 2026. | 23/10/2026 — version au 21/02/2026 | CGI art. 150 VB III, version à la date de cession |
| Barème usufruit / nue-propriété | Lire la tranche « moins de N ans révolus » ; erreur fréquente d'une tranche (58 ans → NP 50 %, pas 60 %). | 23/10/2026 | CGI art. 669 |
| Droit de partage | Taux réduit réservé aux partages consécutifs à un divorce, une séparation de corps ou une rupture de PACS ; un changement de régime matrimonial relève du taux normal. | 23/10/2026 | CGI art. 746 |
| Information des salariés (cession titres / fonds) | Champ indexé sur l'absence d'obligation de CSE « attributions élargies » ; délai d'un mois ; amende civile réduite. | 23/10/2026 — loi 2026-403 | C. com. art. L. 23-10-1 et L. 141-23 |
| Recodification de la TVA | Les articles TVA du CGI (ex. art. 257 bis) sont abrogés à effet différé au **01/01/2027** par l'ordonnance n° 2025-1247 (transfert au Code des impositions sur les biens et services). Pour tout livrable couvrant une opération à cheval sur 2027 : citer la référence applicable à la date de l'opération, et la nouvelle référence en regard. | 23/10/2026 | Ordonnance n° 2025-1247 du 17/12/2025 ; statut de l'article cité à la date de l'opération |
| Délais de réclamation fiscale | R*196-1 LPF modifié par le décret n° 2026-692 (en vigueur au 30/07/2026) ; après une procédure de reprise, le contribuable dispose d'un délai **égal à celui de l'administration** (R*196-3). | 23/10/2026 | LPF R*196-1 et R*196-3 |
| Pacte Dutreil | Régime modifié par la LF 2026 (art. 8) : lire 787 B dans la version à la date de transmission (biens exclus, détention indirecte, durées). Donation avec réserve d'usufruit : droits de vote de l'usufruitier **statutairement limités à l'affectation des bénéfices**. | 23/10/2026 — version au 21/02/2026 | CGI art. 787 B et 787 C ; dossier Dutreil 2026 du dépôt |
| Report 150-0 B ter + quotient | Jurisprudence divergente : **présenter les deux thèses**, recommander un rescrit, ne jamais écrire « acquis » ni « inapplicable ». | Position ECA | Base Positions ECA + checker |
| Contribution différentielle (CDHR) | Elle figure à l'**art. 224 CGI** — l'« art. 150-0 F ter » cité dans les anciennes versions des skills **n'existe pas**. Le texte traite spécifiquement les plus-values 150-0 B ter dont le report expire (II 6° et IV A) et les revenus exceptionnels (« quart »). Chiffrer la CDHR dans chaque scénario comparé (cession directe / apport-cession / purge) avant toute conclusion. | 23/10/2026 — version au 21/02/2026 (LF 2026 art. 2) | CGI art. 224 |

---

## 6. Standard de rédaction ECA — tout contrat et tout acte

Rappel permanent de Yoann : **tout contrat est rédigé au standard M&A
international**, calibré sur le contexte.

1. **Article 1 — Définitions et interprétation** : termes définis en majuscules ;
   règles d'interprétation (titres non interprétatifs, singulier/pluriel,
   référence à un texte = version en vigueur, « notamment » non limitatif,
   primauté du corps sur les annexes, computation des délais).
2. **Structure** : articles et sous-articles numérotés, paragraphes en bloc
   justifié, renvois internes vérifiés.
3. **Délais** : jamais « X jours » nu — préciser jours calendaires / ouvrés /
   ouvrables, ou renvoyer au terme défini « Jour Ouvré ». Préciser le point de
   départ et le mode de notification.
4. **Déclarations et garanties** structurées par rubrique (titre, capacité,
   situation de la société, comptes, litiges, conformité sociale et fiscale,
   contrats significatifs, PI, assurances, absence de changement significatif)
   avec mécanisme d'indemnisation (franchise, seuil, plafond, durée) dès que
   des garanties sont données.
5. **Procédure** : notifications (forme, adresses, date de réception), règlement
   des différends (négociation, médiation, juridiction ou arbitrage), droit
   applicable.
6. **Clauses de style** : intégralité, divisibilité, absence de renonciation,
   frais, cession du contrat, exemplaires et signature électronique.
7. **Annexe finale « Points de vigilance ECA »** (non contractuelle) pour tout
   point restant à vérifier, plutôt que de le noyer dans le corps de l'acte.
8. **Niveau de détail** calibré sur le risque réel, poussé par défaut vers une
   version complète plutôt que minimale.
9. **Option la plus sécurisante d'emblée** : mécanismes en cascade, solutions
   de repli, sans attendre que Yoann le demande.
10. **Répercussions** : toute modification d'une clause est propagée dans le
    reste du document (ex. formule de prix → valeur déterminable → renvoi
    conventionnel exprès à l'art. 1843-4 C. civ. dans la clause d'expertise).
11. **Aucune mention** d'un modèle, d'un auteur tiers ou d'un précédent client
    dans un livrable transmis (texte, commentaires, métadonnées). Yoann est le
    rédacteur. Pas d'appréciation de « friction » dans les commentaires.
12. **Relecture profonde** avant transmission ; signaler soi-même les failles et
    formulations excessives, y compris dans les instructions de Yoann.

---

## 7. Garde-fous

### 7.1 Pièce pseudonymisée
Si la pièce contient des marqueurs `[PERSONNE_1]`, `[SOCIETE_1]`, `[X_1]`,
`{{VARIABLE}}` : appliquer `pieces-pseudonymisees`, et **n'interroger aucun
connecteur nominatif** (Radar, Pennylane, Microsoft 365, Granola, recherche web)
avec un élément susceptible de ré-identifier une personne ou une société.

### 7.2 Confidentialité
Ne pas copier de données client dans un outil tiers non nécessaire, ni dans le
dépôt (public). Pennylane et Microsoft 365 en lecture ; aucune écriture, aucun
envoi sans accord exprès.

### 7.3 Périmètre d'intervention
Si la demande émane d'un prospect ou d'un tiers non client du cabinet (proche,
association, demande relayée), le signaler en une ligne et rappeler l'intérêt
d'une lettre de mission ou d'un devis avant un livrable engageant. Ne pas
rédiger d'actes réservés au notaire (donation, contrat de mariage, partage
portant sur un immeuble) : préparer la note ou le projet de clauses pour le
notaire.

---

## 8. Charte et méthode Word ECA

- **Jamais de document Word construit de zéro** quand un gabarit existe :
  récupérer le gabarit du dépôt (actes : gabarit société / SCI ; courriers et
  consultations : « courrier ECA » et précédents du dossier Consultations),
  dépaqueter, injecter le corps XML avec les styles natifs, rempaqueter.
- **Couleurs (décision de Yoann, en vigueur)** : corps de texte **noir** pour
  tous les livrables ; titres et titres d'articles des **actes** en **noir gras**
  (le rouge charte est réservé aux courriers et consultations) ; bleu-gris
  #495864 pour le bloc destinataire et la signature des courriers.
- Police Raleway sur 100 % des runs ; contrôle par inspection du XML (l'aperçu
  de rendu n'a pas la police et ne prouve rien).
- Lieu de signature : à demander s'il n'est pas précisé.
- Signature : YD + expert-comptable signataire du dossier.

---

## 9. Fin de livrable — toujours

1. `legal-hallucination-checker` sur 100 % des références (bloquant).
2. `positions-eca` : proposer les positions nouvellement tranchées (max. 3).
3. Si l'acte engage une partie : proposer `avocat-adverse`.
4. Si le dossier génère une échéance (délai de recours, engagement Dutreil,
   opposition, déclaration annuelle de suivi) : la signaler en fin de livrable
   sous « Échéances ».
