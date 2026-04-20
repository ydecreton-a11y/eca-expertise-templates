---
name: veille-juridique
description: >
  Skill ECA EXPERTISE pour toute veille, synthèse ou analyse d'un texte
  législatif ou réglementaire nouveau. Déclencher sur : loi de finances,
  ordonnance, décret, circulaire, directive européenne, arrêté, instruction
  fiscale, jurisprudence récente à impact client. Mots-clés : veille juridique,
  veille fiscale, actualité, nouveauté fiscale, qu'est-ce que change, analyse
  de la loi, synthèse réforme, impact réforme, LF 2025, LF 2026, décret récent,
  nouveauté législative, ce qui change, impact pour mes clients.
---

# Skill : Veille juridique et fiscale — ECA EXPERTISE

## PHASE 0 — Initialisation (exécuter dans cet ordre, toujours)

### 0a — Recherche dossier en cours

Si un nom de client ou de société est mentionné dans la demande :

```
conversation_search(query="[nom exact du client ou de la société]")
```

- Si historique trouvé → lire avant d'analyser. Signaler discrètement : "Suite du dossier [client]"
- Si aucun historique → nouveau dossier, continuer normalement
- Si demande générique sans nom propre → pas de recherche

### 0b — Vérification du périmètre

La veille produit une analyse d'un texte **nouveau**. Si la demande est une
question de fond sur le droit existant → skill consultation-juridique.
Si le texte est connu et qu'un acte doit en découler → skill redaction-acte.

### 0c — Intégration réponse Casus

Si Yoann colle un output Casus dans la conversation :
- L'utiliser comme base documentaire certifiée pour la partie CGI/BOFiP
- Claude complète : jurisprudence Légifrance, impact profil client ECA, note Notion
- Indiquer : "Base Casus intégrée"

---

## PHASE 1 — Sourcing

### Fetch dynamique GitHub (obligatoire avant toute vérification)

Fetcher systématiquement avant d'utiliser un taux, un outil MCP ou une
référence BOFiP :

```
web_fetch("https://raw.githubusercontent.com/ydecreton-a11y/eca-expertise-templates/main/skills/shared/sources-legales.md")
```

Ce fetch (2 secondes) garantit que tu travailles avec les taux et références
à jour — pas avec des valeurs mémorisées potentiellement périmées après
une LF. C'est la différence entre 30 % et 31,4 % de PFU.

### Sources primaires (ne jamais rédiger de mémoire)

Un texte récent peut avoir été modifié, corrigé par erratum, ou ses décrets
d'application pas encore publiés. Rédiger une veille sans sourcing est une
faute méthodologique — les clients vont l'appliquer.

**Sources primaires — ordre de consultation :**

1. **MCP Légifrance** (texte intégral, date d'entrée en vigueur)
   ```
   recherche_journal_officiel(search="[titre ou numéro]", text_types=["LOI"])
   rechercher_code(search="[articles modifiés]", champ="NUM_ARTICLE")
   ```

2. **BOFiP** (doctrine administrative d'application)
   — Vérifier si une instruction a déjà été publiée
   — `https://bofip.impots.gouv.fr/bofip/recherche.html?q=MOTS_CLES`

3. **DGFiP / Impots.gouv.fr** pour formulaires et FAQ officielles
4. **EUR-Lex** si directive européenne transposée

---

## PHASE 2 — Analyse du texte

### 2.1 Identification précise
- Référence complète : numéro, date, JORF
- Date d'entrée en vigueur (≠ date de publication)
- Décrets d'application publiés ? Attendus ?
- Rétroactivité éventuelle ?

### 2.2 Analyse substantielle
- Quoi change exactement ? (droit antérieur vs droit nouveau)
- Conditions d'application : qui est concerné, à partir de quand ?
- Exceptions et régimes transitoires
- ⚠️ Zones d'incertitude : texte en attente d'instruction, questions
  d'interprétation non tranchées

---

## PHASE 3 — Impact par profil client ECA (clé de valeur ajoutée)

Cette phase est ce qui distingue une veille cabinet d'un copier-coller
Légifrance. Pour chaque texte analysé, évaluer l'impact sur les profils
clients ECA :

| Profil client | Impact du texte | Urgence | Action recommandée |
|---------------|-----------------|---------|-------------------|
| LMNP/LMP | [impact spécifique] | 🔴/🟠/🟢 | [action] |
| Dirigeants SARL/SAS IS | [impact] | | |
| SCI à l'IS | [impact] | | |
| Transmission en cours | [impact] | | |
| Apport-cession en report | [impact] | | |
| Particuliers (dividendes, PV) | [impact] | | |

**Si impact nul ou marginal sur un profil → le dire explicitement.**
Ne pas gonfler l'impact pour donner l'impression de veille exhaustive.

---

## PHASE 4 — Structure de sortie

```
NOTE DE VEILLE JURIDIQUE ET FISCALE
[Référence — Date — YD]

I. TEXTE ANALYSÉ
   Référence complète, date JO, date d'entrée en vigueur.

II. SYNTHÈSE EN 3 LIGNES
   Ce que ça change. Pour qui. À partir de quand.
   [La synthèse doit être lisible par un expert-comptable en 30 secondes]

III. ANALYSE DÉTAILLÉE
   3.1 Droit antérieur
   3.2 Droit nouveau
   3.3 Dispositions transitoires
   3.4 ⚠️ Points d'incertitude / en attente d'instruction

IV. IMPACT PAR PROFIL CLIENT
   [Tableau §3 ci-dessus]

V. ACTIONS RECOMMANDÉES PAR LE CABINET
   — Dossiers à revoir en urgence (liste si applicable)
   — Conseils préventifs à déclencher
   — Points à aborder lors des prochains RDV clients concernés

VI. SOURCES
   Texte(s) vérifié(s) via Légifrance : [références]
   BOFiP consulté : [oui/non — instruction disponible : oui/non]
```

---

## PHASE 5 — Entrée Notion (si demandé ou si semaine de veille S[N])

Après rédaction de la note, proposer systématiquement l'entrée dans la base
Notion Veille Juridique ECA (data source ID : `f201a44e-556f-4420-8f61-eec1f8cb2d5a`).

Champs à renseigner :
- **Titre** : "[Référence courte] — [Sujet en 5 mots]"
- **Semaine** : S[N] AAAA
- **Domaine** : Fiscalité IS / Fiscalité mobilière / LMNP / Transmission / Droit sociétés / Autre
- **Résumé** : synthèse en 3 lignes (§II de la note)
- **Impact client** : profils concernés + urgence
- **Source** : référence Légifrance + BOFiP si disponible

---

## Exemple de veille bien formée (extrait)

**Synthèse en 3 lignes (bonne pratique) :**
> "La LFSS 2026 porte le taux de CSG sur les revenus du patrimoine à 10,6%,
> portant les prélèvements sociaux à 18,6% sur les PV mobilières et dividendes.
> Exception : PV immobilières et revenus fonciers nus maintenus à 17,2%.
> Applicable aux revenus perçus à compter du 1er janvier 2026."

**Impact client correctement formulé :**
> "Dirigeants percevant des dividendes : hausse de 1,4 point de PS.
> Sur une distribution de 200 000 €, surcoût de 2 800 €.
> Action : vérifier si la distribution 2025 peut être avancée avant le 31/12."

**❌ Ce qui est insuffisant :**
> "Les prélèvements sociaux augmentent. À surveiller pour vos clients."
