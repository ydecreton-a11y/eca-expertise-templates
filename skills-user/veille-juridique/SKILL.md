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


---

## ENRICHISSEMENT — Gestion des cas particuliers

### Cas 1 — Erratum publié au JORF
Un texte de loi ou d'ordonnance peut être corrigé par un erratum dans les jours/
semaines suivant sa publication. **Toujours vérifier au JORF la version consolidée
en vigueur.**

```
recherche_journal_officiel(search="erratum [titre du texte ou numéro]", text_types=["LOI"])
```

Si erratum identifié :
- Signaler en tête de la note : « Note rédigée sur la base du texte tel que rectifié
  par l'erratum publié au JORF du [date] »
- Mentionner explicitement les passages corrigés si la veille les concerne

### Cas 2 — Décrets d'application en attente
Une loi peut être votée mais inapplicable tant que ses décrets ne sont pas publiés.

**Workflow :**
1. Identifier les renvois à décret dans le texte (« Un décret en Conseil d'État précise... »)
2. Vérifier sur Légifrance si les décrets ont été publiés
3. Si non publiés :
   - Signaler que le dispositif n'est pas encore opérationnel
   - Estimer le calendrier (référence au programme de travail du gouvernement si disponible)
   - ⚠️ INCERTAIN sur les modalités précises tant que le décret n'est pas paru

### Cas 3 — Jurisprudence à intégrer dans la veille
La veille n'est pas limitée aux textes législatifs. Une jurisprudence majeure
(CE Plénière, Cass. ch. mixte, Cons. const. QPC) peut renverser une position
établie et appelle une analyse veille.

**Critères de déclenchement :**
- Décision de juridiction suprême (CE, Cass., Cons. const.)
- Renversement, précision ou consécration d'une position
- Impact sur au moins un profil client ECA

**Workflow spécifique jurisprudence :**
```
1. Identification : juridiction, formation, date, numéro, mots-clés
2. Étude : faits, question de droit, solution, motivation, portée
3. Comparaison : ancienne position vs nouvelle (jurisprudence antérieure / BOFiP / doctrine)
4. Impact pratique :
   — Dossiers en cours concernés ?
   — Stratégies à réviser ?
   — Communication client requise ?
5. Action ECA recommandée : note d'information, mise à jour skills, RDV ciblés
```

---

## EXEMPLE — Veille jurisprudence bien formée

**CE 14 octobre 2024 n°490685 — Donation usufruit Article 13 5° CGI**

> « **Synthèse en 3 lignes**
> Le Conseil d'État précise que la « première cession à titre onéreux » au sens de
> l'Art. 13, 5° CGI vise la constitution initiale de l'usufruit à titre onéreux, et
> non la prorogation ou le démembrement préalable à titre gratuit.
> **Impact :** la prorogation d'un usufruit préexistant (par renouvellement
> contractuel ou par effet de la donation antérieure) ne déclenche pas la
> qualification de revenu et reste imposable selon le régime de la PV.
> **Applicable :** dossiers en cours et opérations futures. »

> **Impact par profil ECA :**
> | Profil | Impact | Urgence |
> |--------|--------|---------|
> | Démembrement de droits sociaux | 🟢 Sécurisation des montages prorogations | Faible |
> | OBO avec usufruit temporaire | 🟠 Vérifier si prorogation envisagée | Modérée |
> | Donation NP + USU temporaire | 🟢 Confirmation de l'analyse antérieure | Faible |

> **Action ECA :** mise à jour AUREP M5 + skill patrimonial-structuring + entrée Notion.


---

## 🛡️ PHASE FINALE — Auto-déclenchement legal-hallucination-checker

⚠️ **OBLIGATOIRE — Étape non sautable.**

Avant remise du livrable au client ou à Yoann, déclencher automatiquement :

```
1. Charger skill legal-hallucination-checker
2. Extraire toutes les références citées :
   — Articles de code (CGI, C. civ., C. com., LPF, CMF, CSS, CPI...)
   — Jurisprudence (CE, Cass., CAA, TA, Cons. const.)
   — BOFiP (BOI-...)
   — Lois, ordonnances, décrets
3. Vérifier chacune via MCP Légifrance avec au minimum 2 stratégies de recherche
4. Produire le rapport de vérification (score /100)
5. Décision :
   — Si score ≥ 70 et 0 ⛔ HALLUCINATION → livrer + mentionner « Vérifié — score [N]/100 »
   — Si score < 70 ou présence de ⛔ HALLUCINATION → NE PAS LIVRER
     → Corriger les références fautives → relancer le checker → attendre validation Yoann
```

**Marquage final obligatoire dans le livrable :**
> *« Vérifié via legal-hallucination-checker — [N] références contrôlées — score [X]/100 »*

Cette mention est la signature qualité ECA. Sa présence engage Yoann ;
son absence signifie que la vérification n'a pas eu lieu.


---

## ✅ CHECKLIST AVANT REMISE

Valider mentalement chaque point avant d'envoyer la réponse :

- [ ] Toutes les références citées vérifiées via MCP Légifrance (Pattern 3 ci-dessous)
- [ ] Zones d'incertitude explicitement balisées avec ⚠️ INCERTAIN
- [ ] La conclusion répond directement et précisément à la question posée
- [ ] Niveau de risque justifié par un argumentaire (pas seulement affiché)
- [ ] Aucune position incertaine présentée comme certaine
- [ ] legal-hallucination-checker déclenché et score ≥ 70/100
- [ ] Charte graphique ECA respectée si livrable Word (#999999 / #C00000 / #495864)
- [ ] Référence YD + expert-comptable signataire mentionnée
- [ ] Date d'entrée en vigueur ≠ date de publication vérifiée
- [ ] Décrets d'application identifiés (publiés / attendus)
- [ ] Erratum éventuel vérifié au JORF
- [ ] Impact par profil client ECA évalué (au moins 4 profils)
- [ ] Entrée Notion Veille Juridique préparée si demandée

**Si un seul item n'est pas validé → ne pas livrer. Reprendre la phase concernée.**


---

## 🔍 ANNEXE — Commandes MCP Légifrance exactes

Ne plus écrire « via MCP Légifrance » sans la commande. Utiliser les patterns suivants :

### Articles de code
```
rechercher_code(code_name="Code général des impôts", search="[numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Code de commerce", search="[numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Code civil", search="[numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Livre des procédures fiscales", search="L. [numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Code monétaire et financier", search="L. [numéro]", champ="NUM_ARTICLE")
rechercher_code(code_name="Code du travail", search="L. [numéro]", champ="NUM_ARTICLE")
```

### Jurisprudence
```
# Conseil d'État, CAA, TA
rechercher_jurisprudence_administrative(search="[numéro affaire]", champ="NUM_AFFAIRE")
# Cour de cassation
rechercher_jurisprudence_judiciaire(search="[numéro pourvoi]", champ="NUM_AFFAIRE")
# Conseil constitutionnel
rechercher_decisions_constitutionnelles(search="[N°-AAAA QPC]")
```

### Doctrine et textes officiels
```
# BOFiP
web_fetch("https://bofip.impots.gouv.fr/bofip/[identifiant]")
# Loi / ordonnance / décret
recherche_journal_officiel(search="[numéro ou titre]", text_types=["LOI"])
# Texte consolidé
rechercher_dans_texte_legal(search="[mots-clés]")
```

**Règle de robustesse** : avant de conclure à l'inexistence d'une référence,
tenter au minimum 2 stratégies (numéro exact + mots-clés + date approximative).
Une référence non trouvée via MCP ≠ référence inexistante.
