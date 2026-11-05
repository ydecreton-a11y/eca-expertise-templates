#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contrôleur de livrable ECA EXPERTISE — version 1 (modules A à E).

Contrôles mécaniques d'un livrable Word (.docx), texte (.txt) ou Markdown (.md)
avant remise. Le contrôleur ne juge pas le fond : il repère, il ne certifie pas.

  A. Délais non qualifiés (« 15 jours » sans ouvrés / ouvrables / calendaires,
     terme défini « Jour(s) Ouvré(s) » utilisé sans définition).
  B. Inventaire des références juridiques (articles de code, textes, BOI,
     jurisprudence, taux en contexte fiscal), destiné au
     legal-hallucination-checker. Les renvois internes sont listés à part.
  C. Mentions interdites (auteurs et sources de modèles, outils d'IA, noms de
     précédents clients) — corps, notes, en-têtes, commentaires, métadonnées.
  D. Résidus de rédaction (champs non remplis, suivi des modifications,
     commentaires, surlignages, texte masqué, métadonnées d'auteur).
  E. Discordances entre montants ou nombres en chiffres et en lettres.

Usage :
  python3 controle_livrable.py LIVRABLE.docx [--config fichier.json]
                               [--rapport rapport.md] [--json rapport.json]

Code de sortie : 2 si au moins une anomalie bloquante, 0 sinon, 1 si erreur.
Aucune dépendance hors de la bibliothèque standard de Python.
"""

import argparse
import json
import os
import re
import sys
import unicodedata
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
NS_CORE = {
    "dc": "http://purl.org/dc/elements/1.1/",
    "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
}
NS_APP = "{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}"
NS_CUSTOM = "{http://schemas.openxmlformats.org/officeDocument/2006/custom-properties}"

GRAVITES = ("bloquant", "a_verifier", "information")
LIBELLE_GRAVITE = {"bloquant": "BLOQUANT", "a_verifier": "À vérifier", "information": "Information"}
LETTRE = r"A-Za-zÀ-ÖØ-öø-ÿŒœ"


# --------------------------------------------------------------------------
# Lecture du document
# --------------------------------------------------------------------------

class Bloc:
    """Un paragraphe de texte avec sa localisation."""

    def __init__(self, partie, numero, section, texte):
        self.partie = partie      # corps, note, en-tête, pied, commentaire
        self.numero = numero      # rang du paragraphe dans sa partie
        self.section = section    # dernier titre ou article rencontré
        self.texte = texte

    def lieu(self):
        lieu = "%s, § %d" % (self.partie, self.numero)
        if self.section:
            lieu += " (%s)" % self.section
        return lieu


def _texte_paragraphe(p):
    morceaux = []
    for el in p.iter():
        if el.tag == W + "t" or el.tag == W + "delText":
            # Le texte supprimé en suivi des modifications n'est pas du texte visible.
            if el.tag == W + "delText":
                continue
            morceaux.append(el.text or "")
        elif el.tag in (W + "tab",):
            morceaux.append("\t")
        elif el.tag in (W + "br", W + "cr"):
            morceaux.append(" ")
        elif el.tag == W + "noBreakHyphen":
            morceaux.append("-")
    return "".join(morceaux)


def _style(p):
    ppr = p.find(W + "pPr")
    if ppr is None:
        return ""
    ps = ppr.find(W + "pStyle")
    return ps.get(W + "val", "") if ps is not None else ""


RE_TITRE = re.compile(r"^\s*(?:ARTICLE|Article|TITRE|Titre|CHAPITRE|Chapitre)\s+[\dIVXLC]+(?:[.\-]\d+)*\b")


def _est_titre(p, texte):
    st = _style(p).lower()
    if any(k in st for k in ("heading", "titre", "title")):
        return True
    return bool(RE_TITRE.match(texte)) and len(texte) < 140


def lire_docx(chemin):
    blocs, meta, constats_bruts = [], {}, []
    with zipfile.ZipFile(chemin) as z:
        noms = z.namelist()

        def parties(prefixe, libelle):
            res = []
            for n in sorted(noms):
                if n.startswith("word/" + prefixe) and n.endswith(".xml"):
                    res.append((n, libelle))
            return res

        sources = [("word/document.xml", "corps")]
        sources += parties("footnotes", "note de bas de page")
        sources += parties("endnotes", "note de fin")
        sources += parties("header", "en-tête")
        sources += parties("footer", "pied de page")
        sources += parties("comments", "commentaire")

        for nom, libelle in sources:
            if nom not in noms:
                continue
            racine = ET.fromstring(z.read(nom))
            section, numero = "", 0
            for p in racine.iter(W + "p"):
                texte = _texte_paragraphe(p)
                if not texte.strip():
                    continue
                numero += 1
                if libelle == "corps" and _est_titre(p, texte):
                    section = re.sub(r"\s+", " ", texte.strip())[:70]
                blocs.append(Bloc(libelle, numero, section, texte))

            if libelle == "corps":
                n_ins = sum(1 for _ in racine.iter(W + "ins"))
                n_del = sum(1 for _ in racine.iter(W + "del"))
                n_mv = sum(1 for _ in racine.iter(W + "moveFrom")) + sum(1 for _ in racine.iter(W + "moveTo"))
                if n_ins or n_del or n_mv:
                    constats_bruts.append(("D", "bloquant", "Document",
                        "Suivi des modifications non accepté (%d insertion(s), %d suppression(s), %d déplacement(s))" % (n_ins, n_del, n_mv),
                        "Accepter ou refuser toutes les modifications avant remise."))
                surlignes = []
                masques = []
                for r in racine.iter(W + "r"):
                    rpr = r.find(W + "rPr")
                    if rpr is None:
                        continue
                    t = "".join((x.text or "") for x in r.iter(W + "t")).strip()
                    if not t:
                        continue
                    if rpr.find(W + "highlight") is not None or rpr.find(W + "shd") is not None and rpr.find(W + "shd").get(W + "fill", "auto") not in ("auto", "FFFFFF", "ffffff"):
                        surlignes.append(t)
                    if rpr.find(W + "vanish") is not None:
                        masques.append(t)
                if surlignes:
                    constats_bruts.append(("D", "a_verifier", "Document",
                        "%d passage(s) surligné(s) ou ombré(s)" % len(surlignes),
                        "Exemples : " + " | ".join(_court(s, 50) for s in surlignes[:5])))
                if masques:
                    constats_bruts.append(("D", "bloquant", "Document",
                        "%d passage(s) en texte masqué (lisible par le client s'il affiche les marques)" % len(masques),
                        "Exemples : " + " | ".join(_court(s, 50) for s in masques[:5])))

        n_com = 0
        for nom in noms:
            if nom.startswith("word/comments") and nom.endswith(".xml") and "Extended" not in nom and "Ids" not in nom:
                n_com += sum(1 for _ in ET.fromstring(z.read(nom)).iter(W + "comment"))
        if n_com:
            constats_bruts.append(("D", "bloquant", "Document",
                "%d commentaire(s) en marge" % n_com, "Supprimer les commentaires avant remise."))

        if "docProps/core.xml" in noms:
            c = ET.fromstring(z.read("docProps/core.xml"))
            for cle, xp in (("Auteur", "dc:creator"), ("Dernière modification par", "cp:lastModifiedBy"),
                            ("Titre", "dc:title"), ("Sujet", "dc:subject"), ("Mots-clés", "cp:keywords"),
                            ("Description", "dc:description"), ("Catégorie", "cp:category")):
                el = c.find(xp, NS_CORE)
                if el is not None and (el.text or "").strip():
                    meta[cle] = el.text.strip()
        if "docProps/app.xml" in noms:
            a = ET.fromstring(z.read("docProps/app.xml"))
            for cle, tag in (("Société", "Company"), ("Gestionnaire", "Manager"), ("Modèle Word", "Template")):
                el = a.find(NS_APP + tag)
                if el is not None and (el.text or "").strip():
                    meta[cle] = el.text.strip()
        if "docProps/custom.xml" in noms:
            cu = ET.fromstring(z.read("docProps/custom.xml"))
            for prop in cu.findall(NS_CUSTOM + "property"):
                val = "".join(prop.itertext()).strip()
                if val:
                    meta["Propriété « %s »" % prop.get("name", "?")] = val
    return blocs, meta, constats_bruts


def lire_texte(chemin):
    with open(chemin, encoding="utf-8") as f:
        lignes = f.read().split("\n")
    blocs, section, numero = [], "", 0
    for ligne in lignes:
        if not ligne.strip():
            continue
        numero += 1
        if ligne.lstrip().startswith("#") or RE_TITRE.match(ligne):
            section = ligne.strip("# ").strip()[:70]
        blocs.append(Bloc("texte", numero, section, ligne))
    return blocs, {}, []


# --------------------------------------------------------------------------
# Outils
# --------------------------------------------------------------------------

def _court(s, n=90):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def _extrait(texte, debut, fin, marge=55):
    a = max(0, debut - marge)
    b = min(len(texte), fin + marge)
    ext = texte[a:b]
    return ("…" if a > 0 else "") + _court(ext, 2 * marge + (fin - debut) + 10) + ("…" if b < len(texte) else "")


def _sans_accent(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


class Constat:
    def __init__(self, module, gravite, lieu, objet, detail=""):
        self.module, self.gravite, self.lieu, self.objet, self.detail = module, gravite, lieu, objet, detail

    def dict(self):
        return {"module": self.module, "gravite": self.gravite, "lieu": self.lieu,
                "objet": self.objet, "detail": self.detail}


# --------------------------------------------------------------------------
# Nombres en lettres (français)
# --------------------------------------------------------------------------

UNITES = {
    "zero": 0, "un": 1, "une": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5,
    "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10, "onze": 11, "douze": 12,
    "treize": 13, "quatorze": 14, "quinze": 15, "seize": 16, "vingt": 20,
    "vingts": 20, "trente": 30, "quarante": 40, "cinquante": 50, "soixante": 60,
    "septante": 70, "huitante": 80, "octante": 80, "nonante": 90,
}
MULTIPLES = {"cent": 100, "cents": 100, "mille": 1000, "milles": 1000,
             "million": 10 ** 6, "millions": 10 ** 6, "milliard": 10 ** 9, "milliards": 10 ** 9}
BRUIT = {"et", "d", "de", "des", "pourcent", "euro", "euros", "eur", "centime", "centimes",
         "hors", "taxes", "ht", "ttc", "toutes", "comprises", "net", "nets", "virgule"}
MOTS_NOMBRE = set(UNITES) | set(MULTIPLES)


def _jetons(s):
    s = _sans_accent(s.lower())
    s = s.replace("’", "'").replace("'", " ")
    s = re.sub(r"pour\s*cent|pourcent", " ", s)
    s = s.replace("-", " ")
    return [t for t in re.split(r"[\s,;:.]+", s) if t]


def _entier_lettres(jetons):
    total, courant, precedent = 0, 0, None
    vu = False
    for t in jetons:
        if t == "et":
            precedent = t
            continue
        if t in ("vingt", "vingts") and precedent == "quatre":
            courant += 80 - 4
            vu = True
        elif t in UNITES:
            courant += UNITES[t]
            vu = True
        elif t in ("cent", "cents"):
            courant = (courant if courant else 1) * 100
            vu = True
        elif t in ("mille", "milles"):
            total += (courant if courant else 1) * 1000
            courant = 0
            vu = True
        elif t in ("million", "millions", "milliard", "milliards"):
            total += (courant if courant else 1) * MULTIPLES[t]
            courant = 0
            vu = True
        else:
            return None
        precedent = t
    return total + courant if vu else None


def valeur_lettres(texte):
    """Valeur d'un montant écrit en lettres, ou None si ce n'en est pas un."""
    jetons = _jetons(texte)
    if not jetons or not any(t in MOTS_NOMBRE for t in jetons):
        return None
    if any(t not in MOTS_NOMBRE and t not in BRUIT for t in jetons):
        return None
    # Euros et centimes
    if "centime" in jetons or "centimes" in jetons:
        i_eur = next((i for i, t in enumerate(jetons) if t in ("euro", "euros")), None)
        if i_eur is None:
            return None
        e = _entier_lettres([t for t in jetons[:i_eur] if t not in BRUIT or t == "et"])
        c = _entier_lettres([t for t in jetons[i_eur + 1:] if t not in BRUIT or t == "et"])
        if e is None or c is None:
            return None
        return e + c / 100.0
    if "virgule" in jetons:
        i = jetons.index("virgule")
        e = _entier_lettres([t for t in jetons[:i] if t not in BRUIT or t == "et"])
        dec = [t for t in jetons[i + 1:] if t not in BRUIT]
        zeros = 0
        while dec and dec[0] == "zero":
            zeros += 1
            dec = dec[1:]
        d = _entier_lettres(dec) if dec else 0
        if e is None or d is None:
            return None
        return e + d / (10 ** (zeros + len(str(d)))) if d else float(e)
    return _entier_lettres([t for t in jetons if t not in BRUIT or t == "et"])


NOMBRE = r"\d{1,3}(?:[   .]\d{3})+(?:,\d+)?|\d+(?:,\d+)?"


def valeur_chiffres(s):
    s = s.replace(" ", "").replace(" ", "").replace(" ", "")
    if re.match(r"^\d{1,3}(?:\.\d{3})+(?:,\d+)?$", s):
        s = s.replace(".", "")
    s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


# --------------------------------------------------------------------------
# Module A — Délais
# --------------------------------------------------------------------------

MOT_NOMBRE_RE = (r"(?:un|une|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|onze|douze|treize|"
                 r"quatorze|quinze|seize|vingts?|trente|quarante|cinquante|soixante|cents?|mille)")
RE_DELAI = re.compile(
    r"(?<![%s\d])(\d+|%s(?:[\s\-]+(?:et[\s\-]+)?%s)*)(\s*\(\s*[^()]{1,40}\))?\s+(jours?)(?![%s])"
    % (LETTRE, MOT_NOMBRE_RE, MOT_NOMBRE_RE, LETTRE), re.IGNORECASE)
RE_QUALIF = re.compile(r"^\s*(?:ouvr[ée]s?|ouvrables?|calendaires?|calendaire|francs?|pleins?\s+et\s+entiers|entiers\s+et\s+cons[ée]cutifs)\b",
                       re.IGNORECASE)
RE_JOUR_DEFINI = re.compile(r"\bJours?\s+(Ouvr[ée]s?|Ouvrables?|Calendaires?)\b")


RE_REGLE_DEFAUT = re.compile(
    r"(?:[àa]\s+d[ée]faut\s+de\s+pr[ée]cision|sauf\s+(?:stipulation|pr[ée]cision)\s+(?:contraire|expresse)|sauf\s+indication\s+contraire)"
    r"[^.]{0,160}?jours?\s+(?:calendaires?|ouvr[ée]s?|ouvrables?)", re.IGNORECASE)


def module_a(blocs, constats):
    texte_total = "\n".join(b.texte for b in blocs)
    termes_utilises = set()
    regle = RE_REGLE_DEFAUT.search(texte_total)
    note_defaut = ("Le document contient une règle de computation par défaut (« %s ») : le délai est juridiquement couvert, "
                   "mais la règle ECA demande de le qualifier. " % _court(regle.group(0), 90)) if regle else ""
    for b in blocs:
        for m in RE_DELAI.finditer(b.texte):
            nombre = m.group(1).strip()
            if nombre.lower() in ("un", "une") and not m.group(2):
                # « un jour » n'est un délai que précédé d'un marqueur de délai.
                avant = b.texte[max(0, m.start() - 25):m.start()].lower()
                if not re.search(r"(?:d[ée]lai\s+d['’]?|dans|sous|pendant|apr[èe]s|avant|au\s+plus\s+tard|d['’]au\s+moins|de)\s*$", avant):
                    continue
                gravite = "a_verifier"
            else:
                gravite = "bloquant"
            suite = b.texte[m.end():m.end() + 40]
            mot_jour = m.group(3)
            if RE_QUALIF.match(suite):
                continue
            avant_m = b.texte[:m.start()]
            dans_citation = avant_m.count("«") > avant_m.count("»") or avant_m.count("“") > avant_m.count("”")
            if dans_citation:
                constats.append(Constat("A", "a_verifier", b.lieu(),
                                        "Délai en jours dans une citation : « %s »" % _court(m.group(0), 50),
                                        "Ne pas modifier la citation ; si le délai engage les parties, préciser son mode de computation hors citation. "
                                        + _extrait(b.texte, m.start(), m.end())))
                continue
            constats.append(Constat("A", gravite, b.lieu(),
                                    "Délai en jours non qualifié : « %s »" % _court(m.group(0), 50),
                                    note_defaut + _extrait(b.texte, m.start(), m.end())))
        for m in RE_JOUR_DEFINI.finditer(b.texte):
            termes_utilises.add(re.sub(r"\s+", " ", m.group(0)))
    # Terme défini utilisé sans définition
    for terme in sorted(termes_utilises):
        rac = re.escape(terme.split()[1][:5])
        defini = re.search(
            r"[«\"“]\s*Jours?\s+%s[^»\"”]{0,12}[»\"”]"
            r"|Jours?\s+%s\w*\s*(?:»|\")?\s*(?:d[ée]signe|signifie|s'entend|s’entend|d[ée]signent|signifient|s'entendent|s’entendent)"
            r"|(?:^|\n)\s*(?:[-–•]\s*)?Jours?\s+%s\w*\s*(?:»|\")?\s*[:–—-]"
            % (rac, rac, rac),
            texte_total, re.IGNORECASE)
        if not defini and terme[0].isupper():
            constats.append(Constat("A", "bloquant", "Document",
                                    "Terme défini « %s » utilisé sans définition repérée" % terme,
                                    "Ajouter la définition à l'article Définitions, ou écrire le délai en toutes lettres qualifiées."))


# --------------------------------------------------------------------------
# Module B — Inventaire des références
# --------------------------------------------------------------------------

SOURCES_LEGALES = (
    r"CGI|C\.\s?G\.\s?I\.|Code\s+g[ée]n[ée]ral\s+des\s+imp[ôo]ts|LPF|Livre\s+des\s+proc[ée]dures\s+fiscales|"
    r"C\.\s?civ\.?|Code\s+civil|C\.\s?com\.?|Code\s+de\s+commerce|C\.\s?trav\.?|Code\s+du\s+travail|"
    r"CSS|Code\s+de\s+la\s+s[ée]curit[ée]\s+sociale|CMF|Code\s+mon[ée]taire\s+et\s+financier|"
    r"CPC|Code\s+de\s+proc[ée]dure\s+civile|C\.\s?p[ée]n\.?|Code\s+p[ée]nal|C\.\s?consom\.?|Code\s+de\s+la\s+consommation|"
    r"CIBS|Code\s+des\s+impositions\s+sur\s+les\s+biens\s+et\s+services|Code\s+rural|Code\s+de\s+l'urbanisme|"
    r"Code\s+de\s+la\s+construction|Code\s+de\s+la\s+sant[ée]\s+publique|CSP|CRPA|Code\s+[a-zé]+(?:\s+[a-zé']+){0,4}|"
    r"annexe\s+[IV]+|loi|d[ée]cret|ordonnance|arr[êe]t[ée]|r[èe]glement|directive|dudit\s+code|du\s+m[êe]me\s+code|de\s+ce\s+code|pr[ée]cit[ée]e?s?"
)
RE_ARTICLE = re.compile(
    r"\b(?:art(?:icles?)?\.?)\s+((?:(?-i:[LRDA])\.?\s?\*{0,2}\s?)?\d+(?:[-‑–]\d+)*(?:\.\d+)*(?:\s?(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies)\b)?(?:\s?(?-i:[A-Z]{1,2})\b(?!\.))?"
    r"(?:\s*(?:,|et|à|ou)\s*(?:(?-i:[LRDA])\.?\s?\*{0,2}\s?)?\d+(?:[-‑–]\d+)*(?:\.\d+)*(?:\s?(?:bis|ter|quater|quinquies|sexies)\b)?(?:\s?(?-i:[A-Z]{1,2})\b(?!\.))?)*)",
    re.IGNORECASE)
RE_SOURCE_APRES = re.compile(r"^[^.;:()\n]{0,60}?\b(?:du|de\s+la|des|de\s+l'|de\s+l’|au|à\s+la)?\s*(" + SOURCES_LEGALES + r")\b", re.IGNORECASE)
RE_SOURCE_COLLEE = re.compile(r"^\s*(?:,\s*)?(?:I+|al\.\s*\d+|\d+°|[IV]+\s*[A-Z]?)?[\s,]*(" + SOURCES_LEGALES + r")\b", re.IGNORECASE)
RE_INTERNE_APRES = re.compile(
    r"^[^;\n]{0,25}?\b(?:des\s+pr[ée]sentes|des\s+pr[ée]sents?|du\s+pr[ée]sent|de\s+la\s+pr[ée]sente|ci-dessus|ci-dessous|ci-apr[èe]s|ci-avant|"
    r"des\s+statuts|du\s+(?:Protocole|Pacte|Contrat|Compromis|Acte|Trait[ée]|R[èe]glement\s+int[ée]rieur)|de\s+l['’](?:Acte|Accord|Avenant)|de\s+la\s+(?:Convention|Garantie|Promesse))",
    re.IGNORECASE)
RE_SOURCE_AVANT = re.compile(r"\b(" + SOURCES_LEGALES + r")\s*,?\s*(?:[IV]+\s*,?\s*)?$", re.IGNORECASE)
RE_BOI = re.compile(r"\bBOI-[A-Z0-9]+(?:-[A-Z0-9]+)*(?:\s*,?\s*(?:§|n°)\s*\d+)?")
RE_TEXTE = re.compile(r"\b(?:loi|ordonnance|d[ée]cret|arr[êe]t[ée])\s+(?:organique\s+)?n[°o]\s?\d{2,4}-\d+(?:\s+du\s+\d{1,2}(?:er)?\s+[a-zéû]+\s+\d{4})?"
                      r"|\b(?:loi|ordonnance|d[ée]cret)\s+du\s+\d{1,2}(?:er)?\s+[a-zéû]+\s+\d{4}", re.IGNORECASE)
RE_JURIS = re.compile(
    r"\b(?:Cass\.?\s*(?:com|civ|soc|crim|ass\.?\s*pl[ée]n|ch\.?\s*mixte|[123](?:re|e|[èe]me)?\s*civ)?\.?|Cour\s+de\s+cassation|CE|Conseil\s+d['’][ÉEé]tat|CAA|Cour\s+administrative\s+d['’]appel|"
    r"CA|Cour\s+d['’]appel|TA|Tribunal\s+administratif|TJ|Tribunal\s+judiciaire|T\.?\s?com\.?|Tribunal\s+de\s+commerce|"
    r"Cons\.\s*const\.?|Conseil\s+constitutionnel|CJUE|CJCE|CEDH)\b[^;\n]{0,90}?(?:n[°o]\s?[\dA-Z][\w./\-]*|\b\d{2}-\d{2}\.\d{3}\b|ECLI:[\w:.]+|\b\d{4}-\d+\s?(?:QPC|DC)\b)")
RE_POURVOI = re.compile(r"\b\d{2}-\d{2}\.\d{3}\b|ECLI:[A-Z]{2}:[\w:.]+")
RE_RM = re.compile(r"\bR[ée]p(?:onse)?\.?\s*min(?:ist[ée]rielle)?\.?[^;\n]{0,80}?(?:n[°o]\s?\d+|JOAN|JO\s+S[ée]nat)", re.IGNORECASE)
RE_TAUX = re.compile(r"(?<![\d,])\d{1,3}(?:,\d{1,3})?\s?%")


def module_b(blocs, constats, config, inventaire):
    mots_fiscaux = config.get("mots_contexte_fiscal", [])
    re_fiscal = re.compile(r"\b(?:%s)\b" % "|".join(re.escape(m) for m in mots_fiscaux)) if mots_fiscaux else None
    vus = set()

    def ajouter(categorie, ref, b, debut, fin):
        cle = (categorie, re.sub(r"\s+", " ", ref.strip().lower()), b.lieu())
        if cle in vus:
            return
        vus.add(cle)
        inventaire.append({"type": categorie, "reference": _court(ref, 120), "lieu": b.lieu(),
                           "contexte": _extrait(b.texte, debut, fin, 70)})

    for b in blocs:
        t = b.texte
        occupe = []
        for m in RE_JURIS.finditer(t):
            ajouter("jurisprudence", m.group(0), b, m.start(), m.end())
            occupe.append((m.start(), m.end()))
        for m in RE_POURVOI.finditer(t):
            if not any(a <= m.start() < z for a, z in occupe):
                ajouter("jurisprudence", m.group(0), b, m.start(), m.end())
        for m in RE_RM.finditer(t):
            ajouter("réponse ministérielle", m.group(0), b, m.start(), m.end())
        for m in RE_BOI.finditer(t):
            ajouter("BOFiP", m.group(0), b, m.start(), m.end())
        for m in RE_TEXTE.finditer(t):
            ajouter("texte (loi, ordonnance, décret)", m.group(0), b, m.start(), m.end())
        for m in RE_ARTICLE.finditer(t):
            num = m.group(1).strip()
            suite = t[m.end():m.end() + 80]
            avant = t[max(0, m.start() - 30):m.start()]
            s = RE_SOURCE_COLLEE.match(suite) or RE_SOURCE_APRES.match(suite)
            sa = RE_SOURCE_AVANT.search(avant)
            if RE_INTERNE_APRES.match(suite):
                ajouter("renvoi interne", m.group(0), b, m.start(), m.end())
            elif s:
                ref = m.group(0) + " " + s.group(1)
                ajouter("article (%s)" % _court(s.group(1), 40), ref, b, m.start(), m.end() + s.end())
            elif sa:
                ajouter("article (%s)" % _court(sa.group(1), 40), sa.group(1) + ", " + m.group(0), b, m.start(), m.end())
            elif re.match(r"^[LRDA]\.?\s?\*{0,2}\s?\d", num) or re.search(r"\d[-‑–]\d", num):
                ajouter("article (source à préciser)", m.group(0), b, m.start(), m.end())
            else:
                premier = re.match(r"\d+", num)
                n = int(premier.group(0)) if premier else 0
                if re.match(r"^\d+\.\d", num) or n <= 60:
                    ajouter("renvoi interne", m.group(0), b, m.start(), m.end())
                else:
                    ajouter("article (source à préciser)", m.group(0), b, m.start(), m.end())
        if re_fiscal and re_fiscal.search(t):
            for m in RE_TAUX.finditer(t):
                ajouter("taux en contexte fiscal", m.group(0), b, m.start(), m.end())

    for item in inventaire:
        if item["type"] == "renvoi interne":
            continue
        grav = "a_verifier"
        objet = "%s : %s" % (item["type"][0].upper() + item["type"][1:], item["reference"])
        if item["type"] == "article (source à préciser)":
            objet += " — code ou texte non identifié"
        constats.append(Constat("B", grav, item["lieu"], objet, item["contexte"]))


# --------------------------------------------------------------------------
# Module C — Mentions interdites
# --------------------------------------------------------------------------

def module_c(blocs, meta, constats, config):
    deja = []  # (lieu, début, fin) déjà signalés, pour ne pas compter deux fois « Violaine Schmidt » et « Schmidt »
    deja_meta = set()
    for entree in config.get("termes_interdits", []):
        terme = entree["terme"]
        flags = 0 if entree.get("sensible_casse") else re.IGNORECASE
        corps = terme if entree.get("regex") else re.escape(terme)
        motif = re.compile(r"(?<![%s])(?:%s)(?![%s])" % (LETTRE, corps, LETTRE), flags)
        grav = entree.get("gravite", "bloquant")
        for b in blocs:
            for m in motif.finditer(b.texte):
                if any(l == b.lieu() and a <= m.start() and m.end() <= z for (l, a, z) in deja):
                    continue
                deja.append((b.lieu(), m.start(), m.end()))
                constats.append(Constat("C", grav, b.lieu(),
                                        "Mention « %s » — %s" % (m.group(0), entree.get("motif", "")),
                                        _extrait(b.texte, m.start(), m.end())))
        for cle, val in meta.items():
            for m in motif.finditer(val):
                if cle in deja_meta:
                    continue
                deja_meta.add(cle)
                constats.append(Constat("C", "bloquant", "Métadonnées (%s)" % cle,
                                        "Mention « %s » dans les propriétés du fichier — %s" % (m.group(0), entree.get("motif", "")),
                                        _court(val, 120)))


# --------------------------------------------------------------------------
# Module D — Résidus de rédaction
# --------------------------------------------------------------------------

def module_d(blocs, meta, constats_bruts, constats, config):
    for (mod, grav, lieu, objet, detail) in constats_bruts:
        constats.append(Constat(mod, grav, lieu, objet, detail))
    for entree in config.get("residus", []):
        flags = 0 if entree.get("sensible_casse") else re.IGNORECASE
        motif = re.compile(entree["motif"], flags)
        for b in blocs:
            for m in motif.finditer(b.texte):
                constats.append(Constat("D", entree.get("gravite", "bloquant"), b.lieu(),
                                        "%s : « %s »" % (entree.get("libelle", "Résidu"), _court(m.group(0), 40)),
                                        _extrait(b.texte, m.start(), m.end())))
    norm = lambda x: re.sub(r"\s+", " ", unicodedata.normalize("NFC", x)).strip().lower()
    autorises = [norm(a) for a in config.get("auteurs_autorises", [])]
    for cle in ("Auteur", "Dernière modification par", "Société", "Gestionnaire"):
        val = meta.get(cle)
        if val and norm(val) not in autorises:
            constats.append(Constat("D", "a_verifier", "Métadonnées (%s)" % cle,
                                    "Propriété du fichier « %s » = « %s »" % (cle, _court(val, 60)),
                                    "Lisible par le client (Fichier > Informations). La remplacer ou la vider si elle désigne un tiers ou un modèle."))
    for cle in ("Titre", "Sujet", "Mots-clés", "Description", "Catégorie", "Modèle Word"):
        val = meta.get(cle)
        if val and not (cle == "Modèle Word" and val.lower() in ("normal.dotm", "normal.dot", "normal")):
            constats.append(Constat("D", "information", "Métadonnées (%s)" % cle,
                                    "Propriété du fichier « %s » = « %s »" % (cle, _court(val, 60)),
                                    "Vérifier qu'elle ne désigne ni un autre client ni un modèle."))


# --------------------------------------------------------------------------
# Module E — Montants en chiffres et en lettres
# --------------------------------------------------------------------------

RE_CHIFFRES_PUIS_LETTRES = re.compile(
    r"(?<![\d,.])(" + NOMBRE + r")\s*(€|euros?|EUR|%)?\s*\(\s*([^()]{2,200}?)\s*\)", re.IGNORECASE)
RE_LETTRES_PUIS_CHIFFRES = re.compile(
    r"\(\s*(" + NOMBRE + r")\s*(€|euros?|EUR|%)?\s*\)", re.IGNORECASE)


def _comparer(a, b):
    return abs(a - b) < 0.005


def module_e(blocs, constats):
    for b in blocs:
        t = b.texte
        for m in RE_CHIFFRES_PUIS_LETTRES.finditer(t):
            v_chiffres = valeur_chiffres(m.group(1))
            v_lettres = valeur_lettres(m.group(3))
            if v_chiffres is None or v_lettres is None:
                continue
            if not _comparer(v_chiffres, v_lettres):
                constats.append(Constat("E", "bloquant", b.lieu(),
                                        "Discordance chiffres / lettres : %s ≠ « %s » (= %s)" % (
                                            m.group(1), _court(m.group(3), 60), _fmt(v_lettres)),
                                        _extrait(t, m.start(), m.end())))
        for m in RE_LETTRES_PUIS_CHIFFRES.finditer(t):
            v_chiffres = valeur_chiffres(m.group(1))
            if v_chiffres is None:
                continue
            avant = re.sub(r"pour\s+cent", "pourcent", t[max(0, m.start() - 200):m.start()], flags=re.IGNORECASE)
            # Remonter tant que les mots sont des mots de nombre ou du bruit.
            pris = []
            for j in reversed([x for x in re.split(r"\s+", avant.strip()) if x]):
                jj = _jetons(j)
                if jj and all(x in MOTS_NOMBRE or x in BRUIT for x in jj):
                    pris.insert(0, j)
                else:
                    break
            while pris and all(x in BRUIT for x in _jetons(pris[0])):
                pris.pop(0)
            if not pris:
                continue
            v_lettres = valeur_lettres(" ".join(pris))
            if v_lettres is None:
                continue
            if not _comparer(v_chiffres, v_lettres):
                constats.append(Constat("E", "bloquant", b.lieu(),
                                        "Discordance lettres / chiffres : « %s » (= %s) ≠ %s" % (
                                            _court(" ".join(pris), 60), _fmt(v_lettres), m.group(1)),
                                        _extrait(t, m.start() - len(" ".join(pris)) - 1, m.end())))


def _fmt(v):
    if abs(v - round(v)) < 1e-9:
        return "{:,}".format(int(round(v))).replace(",", " ")
    return ("{:,.2f}".format(v)).replace(",", " ").replace(".", ",")


# --------------------------------------------------------------------------
# Rapport
# --------------------------------------------------------------------------

NOMS_MODULES = {
    "A": "A. Délais non qualifiés",
    "B": "B. Références à soumettre au legal-hallucination-checker",
    "C": "C. Mentions interdites",
    "D": "D. Résidus de rédaction et métadonnées",
    "E": "E. Montants en chiffres et en lettres",
}


def rapport_markdown(nom, constats, inventaire, nb_blocs):
    compte = {g: sum(1 for c in constats if c.gravite == g) for g in GRAVITES}
    verdict = "BLOQUÉ — ne pas remettre en l'état" if compte["bloquant"] else "Aucune anomalie bloquante"
    l = []
    l.append("# Contrôle de livrable — %s" % nom)
    l.append("")
    l.append("**Verdict : %s**" % verdict)
    l.append("")
    l.append("Bloquant : %d · À vérifier : %d · Information : %d · Paragraphes lus : %d"
             % (compte["bloquant"], compte["a_verifier"], compte["information"], nb_blocs))
    l.append("")
    l.append("Contrôle mécanique de forme : il ne vérifie ni l'exactitude juridique ni le contenu des références "
             "(rôle du legal-hallucination-checker et de la relecture).")
    for mod in "ACDEB":
        liste = [c for c in constats if c.module == mod]
        l.append("")
        l.append("## %s (%d)" % (NOMS_MODULES[mod], len(liste)))
        if not liste:
            l.append("")
            l.append("Rien à signaler.")
            continue
        l.append("")
        ordre = {g: i for i, g in enumerate(GRAVITES)}
        for c in sorted(liste, key=lambda c: ordre[c.gravite]):
            l.append("- **%s** — %s — %s" % (LIBELLE_GRAVITE[c.gravite], c.lieu, c.objet))
            if c.detail:
                l.append("  > %s" % c.detail.replace("\n", " "))
    internes = [i for i in inventaire if i["type"] == "renvoi interne"]
    if internes:
        l.append("")
        l.append("## Renvois internes repérés (%d) — contrôle de cohérence en version 2" % len(internes))
        l.append("")
        l.append(", ".join(sorted(set(i["reference"] for i in internes)))[:1500])
    return "\n".join(l) + "\n"


def charger_config(chemin):
    if chemin is None:
        chemin = os.path.join(os.path.dirname(os.path.abspath(__file__)), "controle_livrable_config.json")
    if not os.path.exists(chemin):
        print("Configuration introuvable : %s" % chemin, file=sys.stderr)
        return {}
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def controler(chemin, config):
    ext = os.path.splitext(chemin)[1].lower()
    if ext == ".docx":
        blocs, meta, bruts = lire_docx(chemin)
    elif ext in (".txt", ".md"):
        blocs, meta, bruts = lire_texte(chemin)
    else:
        raise ValueError("Format non pris en charge : %s (attendu : .docx, .txt, .md)" % ext)
    constats, inventaire = [], []
    module_a(blocs, constats)
    module_b(blocs, constats, config, inventaire)
    module_c(blocs, meta, constats, config)
    module_d(blocs, meta, bruts, constats, config)
    module_e(blocs, constats)
    return constats, inventaire, len(blocs), meta


def main():
    ap = argparse.ArgumentParser(description="Contrôleur de livrable ECA EXPERTISE (modules A à E).")
    ap.add_argument("livrable")
    ap.add_argument("--config")
    ap.add_argument("--rapport", help="Chemin du rapport Markdown (sinon affiché)")
    ap.add_argument("--json", help="Chemin d'un export JSON des constats et de l'inventaire")
    args = ap.parse_args()
    try:
        config = charger_config(args.config)
        constats, inventaire, nb, meta = controler(args.livrable, config)
    except Exception as e:  # le contrôle ne doit jamais échouer en silence
        print("ÉCHEC DU CONTRÔLE — %s : %s" % (type(e).__name__, e), file=sys.stderr)
        return 1
    md = rapport_markdown(os.path.basename(args.livrable), constats, inventaire, nb)
    if args.rapport:
        with open(args.rapport, "w", encoding="utf-8") as f:
            f.write(md)
    else:
        print(md)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump({"livrable": args.livrable, "paragraphes": nb, "metadonnees": meta,
                       "constats": [c.dict() for c in constats], "inventaire_references": inventaire},
                      f, ensure_ascii=False, indent=2)
    return 2 if any(c.gravite == "bloquant" for c in constats) else 0


if __name__ == "__main__":
    sys.exit(main())
