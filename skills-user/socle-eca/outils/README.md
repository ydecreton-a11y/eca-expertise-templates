# Contrôleur de livrable ECA — version 2

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
python3 controle_livrable.py PV.docx --modele MODELE_DU_DEPOT.docx      # module G
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
| F | Numérotation des articles (y compris numérotation automatique de Word, tables des matières écartées), sous-numérotation, renvois internes vers un article inexistant, termes définis jamais utilisés ou définis deux fois, expressions en majuscules employées sans définition (10 au plus par document) | Bloquant pour une numérotation saisie discontinue ou un renvoi au-delà du dernier article d'une structure fiable ; à vérifier sinon |
| G | Avec `--modele` : rédaction modifiée par rapport au modèle hors données du dossier (accords en genre et en nombre, dates, noms, adresses et numéros tolérés), paragraphes supprimés ou ajoutés, données du précédent restées dans le livrable | À vérifier |

## Banc d'essai (05/11/2026)

- Documents fictifs à erreurs insérées (modules A à F) et dérivés du modèle de
  procuration du dépôt (module G : version fidèle, reformulée, avec reliquat) :
  34 erreurs détectées sur 34 ; aucune alerte sur les versions propres.
- Module F sur les 94 livrables du dépôt : 3 numérotations d'articles
  discontinues, toutes réelles (article manquant dans deux statuts et une
  cession) ; points « à vérifier » limités, dont des noms propres en
  majuscules qu'il faut ignorer.
- 94 livrables réels du dépôt : aucun échec de lecture ; sur un échantillon
  aléatoire de 30 alertes bloquantes hors modèles, 30 correspondent à la règle
  ou à un champ non rempli, dont 3 à 4 reproductions de textes légaux non
  placées entre guillemets (non détectables comme citations).

Limites connues : un délai reproduit d'un texte légal sans guillemets est
signalé comme bloquant (à vérifier si une règle de computation par défaut
existe dans l'acte) ; un nombre en lettres n'est comparé que s'il est accolé à
sa forme en chiffres entre parenthèses ; la reconstitution de la
numérotation automatique couvre les formats usuels (décimal, lettres,
romains), pas les numérotations liées à des champs ; le module G compare au
modèle désigné et ne choisit pas le modèle lui-même ; une phrase entièrement
réécrite apparaît comme un paragraphe supprimé et un paragraphe ajouté.
