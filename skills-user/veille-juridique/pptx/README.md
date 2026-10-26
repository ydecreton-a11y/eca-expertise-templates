# Générateur PowerPoint de la veille du mercredi — ECA EXPERTISE

Produit le diaporama de la veille juridique et fiscale interne aux couleurs du
cabinet (charte du courrier ECA : logo, ardoise `#495864`, rouge `#E63427`,
police Raleway). **Aucune limite de slides** : résumé, actions et sources sont
paginés automatiquement. Remplace Gamma depuis le 26/10/2026.

## Fichiers

| Fichier | Rôle |
|---|---|
| `generer_veille.js` | Générateur (Node.js + `pptxgenjs`) |
| `logo-eca.png` | Logo ECA extrait de « courrier ECA.docx » (racine du dépôt) |
| `exemple-fictif.json` | Exemple de données **fictives** au format attendu (test de mise en page uniquement) |

## Utilisation

```bash
cd skills-user/veille-juridique/pptx
node -e "require('pptxgenjs')" 2>/dev/null || npm install pptxgenjs
node generer_veille.js /chemin/veille.json "/chemin/Veille ECA - semaine du ....pptx"
```

Facultatif : la variable `PPTX_APPLY_THEME` peut pointer vers
`scripts/apply_theme.js` du skill `pptx` pour écrire aussi le thème ECA dans le
fichier (sans incidence sur le rendu des slides).

Code de sortie `2` = **génération refusée** : un champ dépasse son budget de
caractères (il déborderait de son cadre) ou un champ obligatoire manque. Le
message liste chaque champ en cause. **Raccourcir le texte et relancer — ne
jamais modifier les budgets ni la mise en page.**

## Format du JSON

Schéma commenté ci-dessous (le fichier réel n'admet pas de commentaires — voir
`exemple-fictif.json`).

```json
{
  "semaine": "du 21 au 27 octobre 2026",            // obligatoire
  "date_edition": "28 octobre 2026",
  "resume": [ { "domaine": "Fiscalité des entreprises", "texte": "≤ 230 car." } ],
  "elements": [ {
      "domaine": "Droit des sociétés",                // obligatoire — sert au regroupement
      "nature": "loi | ordonnance | decret | arrete | doctrine | jurisprudence | ue | autre",
      "titre": "≤ 100 car.",                          // obligatoire
      "reference": "≤ 200 car. — NOR, date, juridiction, numéro", // obligatoire
      "lien": "https://… (lien officiel, rendu cliquable)",
      "date_effet": "≤ 40 car.",
      "avant_label": "Avant",                         // jurisprudence : « Faits et question »
      "apres_label": "Après",                         // jurisprudence : « Solution et portée »
      "avant": "≤ 340 car.",
      "apres": "≤ 340 car.",
      "concernes": "≤ 200 car.",
      "incertitudes": "≤ 200 car.",
      "action": "≤ 330 car. — action recommandée au cabinet",   // obligatoire
      "priorite": "haute | moyenne | basse"
  } ],
  "actions":  [ { "action": "≤ 170 car.", "echeance": "≤ 40 car.", "priorite": "haute", "renvoi": "Élément 2" } ],
  "ecartes":  [ { "titre": "≤ 110 car.", "motif": "≤ 120 car." } ],
  "sources":  [ { "libelle": "≤ 130 car.", "lien": "https://…" } ]
}
```

- `resume` absent : le résumé reprend les titres des éléments.
- `sources` absent : les sources reprennent les références des éléments.
- Plusieurs domaines : une slide intercalaire par domaine.
- Aucun nom de client dans le JSON (les dossiers touchés vont dans le mail, jamais dans les slides).
- Tout délai écrit dans le JSON est qualifié (calendaires, ouvrés, ouvrables).

## Structure produite

Couverture → résumé exécutif (5 points par slide) → par domaine : intercalaire
puis une slide par élément (nature, domaine, date d'effet, priorité ; avant /
après ; personnes concernées et incertitudes ; action cabinet ; référence
cliquable) → actions du cabinet (6 par slide) → écartés (9 par slide) →
sources officielles (10 par slide). La référence et le lien de chaque élément
figurent aussi dans les notes de l'orateur.

## Contrôle

Après génération : `python scripts/office/validate.py fichier.pptx` (skill
`pptx`) doit répondre « All validations PASSED ».
