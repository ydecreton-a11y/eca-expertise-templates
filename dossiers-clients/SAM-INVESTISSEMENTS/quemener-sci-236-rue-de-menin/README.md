# Quémener — SAM INVESTISSEMENTS / SCI 236 RUE DE MENIN

## Objectif

Reconstitution du tableau Quémener pour le calcul de la MV fiscale sur annulation des parts SCI dans la liasse IS 2025 de SAM INVESTISSEMENTS.

## Structure du dossier

```
quemener-sci-236-rue-de-menin/
├── README.md                   ← ce fichier
├── liasses-sam/                ← Liasses IS SAM année par année (2058-A)
├── declarations-sci/           ← Déclarations SCI 2072 / bilans annuels SCI
├── tableaux-excel/             ← Tableaux Excel de calcul fiscal
└── actes/                      ← Acte d'acquisition immeuble SCI (ventilation terrain/constructions)
```

## Informations clés

- **Associé IS** : SAM INVESTISSEMENTS
- **Quote-part** : 85 % (85 parts / 100)
- **VNC comptable** : 118 750 € (261) + 6 510 € (26141) = **125 260 €**
- **Valeur de réalisation** : 85 % × 230 176,07 € = **195 649,65 €**
- **Date liquidation** : 1er août 2025

## Ce qu'il faut déposer

| Fichier recherché | Contenu utile pour le Quémener |
|---|---|
| Liasses IS SAM (2058-A) par an | Ligne quote-part SCI Menin intégrée chaque année |
| Déclarations SCI 2072 par an | Résultat fiscal SCI 100% — base pour reconstitution IS |
| Tableaux Excel fiscaux SAM | Ligne quote-part SCI si liasse non disponible |
| Acte acquisition immeuble SCI | Prix ventilé terrain/constructions — reconstitution VNC IS |

## Méthodologie

1. Reconstituer le plan d'amortissement IS de l'immeuble (VNC IS < VNC comptable)
2. Calculer le résultat IS reconstitué pour chaque année depuis l'acquisition
3. Appliquer la formule Quémener :
   `PR corrigé = 125 260 € + Σ résultats IS taxés chez SAM − Σ pertes déduites − Σ distributions reçues`
4. MV fiscale = 195 649,65 € − PR corrigé

## Références juridiques

- CGI art. 238 bis K I
- CE 16/02/2000 n° 133296 Quémener
- CE 24/04/2019 n° 412503 Fra SCI
- CE 26/04/2024 n° 472855 CMM Finances
