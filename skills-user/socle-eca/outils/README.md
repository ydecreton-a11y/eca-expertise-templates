# Contrôleur de livrable ECA — version 1

Contrôle mécanique de forme d'un livrable avant remise (`socle-eca` § 9). Il
repère, il ne certifie pas : ni l'exactitude juridique, ni le contenu des
références (rôle du `legal-hallucination-checker` et de la relecture).

## Fichiers

| Fichier | Rôle |
|---|---|
| `controle_livrable.py` | Le contrôleur. Python 3, bibliothèque standard uniquement. |
| `controle_livrable_config.json` | Termes interdits, auteurs autorisés, résidus, mots du contexte fiscal. Se modifie sans toucher au script. |
| `banc_essai/generer_banc.py` | Banc d'essai : documents fictifs à erreurs connues et leur version propre (nécessite `python-docx`, pour le banc seul). |

## Usage

```
python3 controle_livrable.py LIVRABLE.docx --rapport rapport.md --json rapport.json
```

Formats : `.docx`, `.md`, `.txt`. Code de sortie : `2` si une anomalie
bloquante subsiste, `0` sinon, `1` si le contrôle a échoué (ne jamais conclure
à l'absence d'anomalie dans ce cas).

## Modules

| Module | Contrôle | Gravité |
|---|---|---|
| A | Délai en jours non qualifié ; terme défini « Jours Ouvrés / Ouvrables » sans définition | Bloquant (à vérifier dans une citation entre guillemets) |
| B | Inventaire des références (articles, textes, BOI, jurisprudence, réponses ministérielles, taux en contexte fiscal), à transmettre au checker ; renvois internes listés à part | À vérifier |
| C | Auteurs et sources de modèles, outils d'IA, noms de précédents clients — texte, notes, en-têtes, commentaires, métadonnées | Bloquant ou à vérifier selon la configuration |
| D | Champs non remplis, suivi des modifications, commentaires, texte masqué, surlignages, métadonnées hors auteurs autorisés | Bloquant, à vérifier ou information |
| E | Montant ou nombre en chiffres discordant avec sa forme en lettres | Bloquant |

Version 2 prévue : F (structure : numérotation, renvois internes, termes
définis) et G (fidélité au modèle du dépôt pour les PV et procurations).

## Banc d'essai (05/11/2026)

- Documents fictifs à erreurs insérées : 24 erreurs détectées sur 24 ; aucune
  alerte sur les versions propres.
- 94 livrables réels du dépôt : aucun échec de lecture ; sur un échantillon
  aléatoire de 30 alertes bloquantes hors modèles, 30 correspondent à la règle
  ou à un champ non rempli, dont 3 à 4 reproductions de textes légaux non
  placées entre guillemets (non détectables comme citations).

Limites connues : un délai reproduit d'un texte légal sans guillemets est
signalé comme bloquant ; la numérotation automatique de Word n'est pas lue
(sans effet sur les modules A à E) ; un nombre en lettres n'est comparé que
s'il est accolé à sa forme en chiffres entre parenthèses.
