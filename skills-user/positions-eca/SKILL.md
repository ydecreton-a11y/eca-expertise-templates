# Skill : positions-eca

## Trigger

Déclencher ce skill **automatiquement** dans deux situations :

### A. AVANT tout livrable juridique/fiscal (mode CONSULTATION)
Avant de répondre à toute question juridique ou fiscale, **consulter la base Notion "📌 Positions ECA"** pour vérifier si le sujet est déjà couvert par une position validée.

**Déclenchement** : dès qu'un des skills suivants est activé :
- consultation-juridique
- calcul-plus-value
- contentieux-fiscal
- diagnostic-transmission
- patrimonial-structuring
- analyse-contrat
- due-diligence-juridique
- redaction-acte
- veille-juridique
- note-information-client

### B. APRÈS tout livrable juridique/fiscal (mode ENRICHISSEMENT)
Après avoir livré une consultation, un calcul, ou une analyse, **proposer l'ajout** de toute position nouvelle qui a été tranchée dans le livrable.

---

## Phase 1 — Consultation de la base (AVANT le livrable)

### Workflow

```
1. Identifier les mots-clés du sujet demandé par Yoann
   (ex: "PFU", "150-0 B ter", "Dutreil", "quasi-usufruit", "LMNP", etc.)

2. Rechercher dans la base Notion Positions ECA :
   notion-search(query="[mots-clés du sujet]",
                  data_source_url="collection://6dc1e530-7996-4a62-b5b6-b378b4c8f204",
                  page_size=5,
                  max_highlight_length=200)

3. Pour chaque position trouvée pertinente, la CHARGER dans le contexte :
   — Énoncé de la position
   — Niveau de certitude (✅ / ⚠️ / ❓)
   — Référence légale
   — Note interne (pièges à éviter)

4. APPLIQUER les positions actives :
   — Si la réponse est COHÉRENTE avec la position → appliquer silencieusement
   — Si la réponse CONTREDIT une position existante → SIGNALER :
     "⚠️ CONFLIT POSITION ECA : la position [titre] (certitude: [niveau])
      indique [X], mais mon analyse actuelle aboutit à [Y].
      Vérification requise avant de livrer."
   — Si AUCUNE position pertinente trouvée → continuer normalement

5. Si la position trouvée a un statut "🔄 À revérifier" → signaler :
   "ℹ️ Position ECA existante mais à revérifier : [titre].
    Je procède avec prudence — vérification Légifrance MCP recommandée."
```

### Règles de consultation

- **Ne jamais ignorer une position active** qui est pertinente pour le sujet
- **Ne jamais contredire silencieusement** une position active sans signaler le conflit
- **Toujours vérifier** via Légifrance MCP si le conflit est détecté (la position est peut-être obsolète)
- **Ne pas surcharger** : max 3-5 positions consultées par livrable. Si le sujet couvre plus de 5 positions → signaler la densité et prioriser.

---

## Phase 2 — Enrichissement de la base (APRÈS le livrable)

### Workflow

```
1. Après la livraison du livrable (et après le legal-hallucination-checker),
   identifier si UNE OU PLUSIEURS positions nouvelles ont été tranchées :
   — Un taux fiscal appliqué avec source vérifiée
   — Une qualification juridique tranchée par jurisprudence
   — Une règle procédurale confirmée par texte
   — Un piège identifié qui mérite d'être mémorisé

2. Pour chaque position candidate, vérifier qu'elle n'existe pas déjà :
   notion-search(query="[énoncé synthétique]",
                  data_source_url="collection://6dc1e530-7996-4a62-b5b6-b378b4c8f204",
                  page_size=3)

3. Si la position N'EXISTE PAS → proposer l'ajout à Yoann :
   "📌 NOUVELLE POSITION DÉTECTÉE :
    Position : [énoncé synthétique]
    Domaine : [domaine]
    Certitude : [niveau]
    Référence : [source vérifiée]
    Note interne : [piège ou contexte]

    Souhaites-tu que je l'ajoute à la base Positions ECA ?"

4. Si Yoann valide → créer l'entrée Notion :
   notion-create-pages(
     parent={"data_source_id": "6dc1e530-7996-4a62-b5b6-b378b4c8f204"},
     pages=[{
       properties: {
         "Position": "[énoncé]",
         "Domaine": "[domaine]",
         "Certitude": "[niveau]",
         "Référence légale": "[source]",
         "Source secondaire": "[BOFiP ou doctrine]",
         "date:Date vérification:start": "[date du jour]",
         "date:Date vérification:is_datetime": 0,
         "Statut": "🆕 Proposition",
         "Impact client": "[profils concernés]",
         "Note interne": "[piège ou contexte]"
       }
     }]
   )

5. La position est créée avec le statut "🆕 Proposition".
   Yoann peut la passer en "✅ Active" dans Notion après vérification.
   Les futures conversations la verront en Phase 1.
```

### Critères de proposition

**PROPOSER** une nouvelle position si :
- Le livrable tranche une question qui se posera à nouveau (récurrence)
- La position repose sur un texte vérifié ou une jurisprudence identifiée
- La position a un impact sur au moins 2 profils clients ECA
- La position n'est pas triviale (pas "les dividendes sont imposables")

**NE PAS PROPOSER** si :
- La position est un calcul spécifique au dossier (montant, date)
- La position est déjà couverte par une entrée existante
- La source n'a pas pu être vérifiée via MCP Légifrance
- Le sujet est en zone d'incertitude totale sans aucune source

---

## Phase 3 — Maintenance de la base (PÉRIODIQUE)

### Détection d'obsolescence

À chaque consultation de la base (Phase 1), si une position active a une "Date vérification" de plus de 6 mois :
- Signaler : "ℹ️ Position ECA [titre] vérifiée il y a plus de 6 mois. Revérification recommandée."
- Si Yoann confirme → relancer la vérification MCP Légifrance et mettre à jour la date
- Si la position a évolué → passer le statut en "🔄 À revérifier" et signaler l'écart

### Détection de conflit inter-positions

Si deux positions actives se contredisent (détecté en Phase 1 ou en cours de livrable) :
- Signaler : "⚠️ CONFLIT INTERNE : positions [A] et [B] semblent contradictoires."
- Proposer la résolution : abrogation de l'une, précision de périmètre, ou fusion.

---

## Identifiants Notion

| Ressource | ID |
|-----------|-----|
| Base "📌 Positions ECA" | Database: `63e0b0adc2104015a55005831f3d605a` |
| Data source (collection) | `collection://6dc1e530-7996-4a62-b5b6-b378b4c8f204` |
| Vue "📊 Par domaine" | `view://351ff3f7-13a7-811b-b3e9-000c45a13487` |
| Vue "✅ Positions actives" | `view://351ff3f7-13a7-8104-b2f9-000cf2b1d93f` |
| Vue "🆕 À valider" | `view://351ff3f7-13a7-8112-bc62-000c5605cd7d` |

---

## Domaines disponibles (valeurs exactes pour le champ SELECT)

- Fiscalité des revenus
- Plus-values mobilières
- Plus-values immobilières
- IS / Holding
- Transmission / Dutreil
- Démembrement / Usufruit
- Droit des sociétés
- Régimes matrimoniaux
- Contentieux fiscal
- LMNP / Immo

## Certitudes disponibles

- ✅ Certitude textuelle (article de loi, texte clair)
- ⚠️ Position doctrinale (jurisprudence, BOFiP interprétatif)
- ❓ Zone d'incertitude (pas de texte clair, positions divergentes)

## Statuts disponibles

- ✅ Active (position validée, à appliquer)
- 🔄 À revérifier (position potentiellement obsolète)
- ❌ Abrogée (position caduque — ne plus appliquer)
- 🆕 Proposition (position proposée par Claude, en attente de validation Yoann)

---

## Exemple de flux complet

**Demande Yoann** : "Mon client veut céder ses parts SARL à un tiers. Quel est le régime fiscal ?"

**Phase 1 (consultation)** :
```
→ notion-search("cession parts SARL PV mobilière PFU")
→ Positions trouvées :
  - "PFU = 31,4 %" (✅ Active, certitude textuelle)
  - "Abattement retraite 500k€" (✅ Active, si dirigeant 60+)
  → Appliquer dans la réponse.
```

**Livrable** : consultation avec PFU 31,4 % appliqué, abattement retraite mentionné si applicable.

**Phase 2 (enrichissement)** :
```
→ Le livrable a tranché : "le droit d'enregistrement de 3 % avec abattement 23 000 €
   s'applique en plus de l'IR/PS sur la PV" (Art. 726 CGI)
→ notion-search("droit enregistrement cession parts SARL 3%")
→ Pas de position existante couvrant ce point
→ Proposition :
  "📌 NOUVELLE POSITION DÉTECTÉE :
   Position : Cession parts SARL : droit d'enregistrement 3 % après abattement 23 000 €
   Domaine : Plus-values mobilières
   Certitude : ✅ Certitude textuelle
   Référence : Art. 726 I 2° CGI
   Souhaites-tu que je l'ajoute ?"
→ Yoann valide → entrée créée en statut "🆕 Proposition"
```

---

## Anti-patterns à éviter

❌ Ne jamais créer une position sans demander la validation de Yoann
❌ Ne jamais passer une position en "✅ Active" sans validation explicite de Yoann
❌ Ne jamais ignorer un conflit entre le livrable et une position existante
❌ Ne jamais surcharger le livrable avec la liste des positions consultées (transparence si demandée, sinon silencieux)
❌ Ne jamais proposer plus de 3 nouvelles positions par livrable (trop = bruit)
❌ Ne jamais dupliquer une position existante avec une formulation légèrement différente
