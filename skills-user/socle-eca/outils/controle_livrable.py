#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contrôleur de livrable ECA EXPERTISE — version 2 (modules A à G).

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
  F. Structure : numérotation des articles (y compris numérotation automatique
     de Word), renvois internes vers un article inexistant, termes définis non
     utilisés, définis deux fois, ou employés sans définition.
  G. Fidélité au modèle (option --modele) : paragraphes dont la rédaction
     s'écarte du modèle au-delà des données du dossier, paragraphes ajoutés ou
     supprimés, données du précédent restées dans le livrable.

Usage :
  python3 controle_livrable.py LIVRABLE.docx [--config fichier.json]
                               [--rapport rapport.md] [--json rapport.json]
                               [--modele modele_du_depot.docx]

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

    def __init__(self, partie, numero, section, texte, label="", style=""):
        self.partie = partie      # corps, note, en-tête, pied, commentaire
        self.numero = numero      # rang du paragraphe dans sa partie
        self.section = section    # dernier titre ou article rencontré
        self.texte = texte
        self.label = label        # numéro automatique affiché par Word (« ARTICLE 3 : », « 2.1 »), absent du texte
        self.style = style        # identifiant du style de paragraphe Word

    def affiche(self):
        return (self.label + " " + self.texte).strip() if self.label else self.texte

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


# --------------------------------------------------------------------------
# Numérotation automatique de Word
# --------------------------------------------------------------------------

def _romain(n):
    vals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    r = ""
    for v, l in vals:
        while n >= v:
            r += l
            n -= v
    return r


def _format_num(n, fmt):
    if fmt in ("upperRoman",):
        return _romain(n)
    if fmt in ("lowerRoman",):
        return _romain(n).lower()
    if fmt in ("upperLetter",):
        return chr(64 + ((n - 1) % 26) + 1) if n > 0 else ""
    if fmt in ("lowerLetter",):
        return chr(96 + ((n - 1) % 26) + 1) if n > 0 else ""
    if fmt in ("bullet", "none"):
        return None
    return str(n)  # decimal et formats assimilés


class Numerotation:
    """Reconstitue les numéros affichés par Word (numbering.xml et styles.xml)."""

    def __init__(self, z, noms):
        self.abstraits, self.nums, self.styles = {}, {}, {}
        self.compteurs = {}
        if "word/numbering.xml" in noms:
            r = ET.fromstring(z.read("word/numbering.xml"))
            for a in r.findall(W + "abstractNum"):
                niveaux = {}
                for lvl in a.findall(W + "lvl"):
                    il = int(lvl.get(W + "ilvl", "0"))
                    st = lvl.find(W + "start")
                    fm = lvl.find(W + "numFmt")
                    tx = lvl.find(W + "lvlText")
                    niveaux[il] = (int(st.get(W + "val", "1")) if st is not None else 1,
                                   fm.get(W + "val", "decimal") if fm is not None else "decimal",
                                   tx.get(W + "val", "") if tx is not None else "")
                self.abstraits[a.get(W + "abstractNumId")] = niveaux
            for n in r.findall(W + "num"):
                ref = n.find(W + "abstractNumId")
                surcharges = {}
                for o in n.findall(W + "lvlOverride"):
                    so = o.find(W + "startOverride")
                    if so is not None:
                        surcharges[int(o.get(W + "ilvl", "0"))] = int(so.get(W + "val", "1"))
                if ref is not None:
                    self.nums[n.get(W + "numId")] = (ref.get(W + "val"), surcharges)
        if "word/styles.xml" in noms:
            r = ET.fromstring(z.read("word/styles.xml"))
            base = {}
            for st in r.findall(W + "style"):
                sid = st.get(W + "styleId")
                bo = st.find(W + "basedOn")
                base[sid] = bo.get(W + "val") if bo is not None else None
                ppr = st.find(W + "pPr")
                np_ = ppr.find(W + "numPr") if ppr is not None else None
                if np_ is not None:
                    ni = np_.find(W + "numId")
                    il = np_.find(W + "ilvl")
                    self.styles[sid] = (ni.get(W + "val") if ni is not None else None,
                                        int(il.get(W + "val", "0")) if il is not None else 0)
            for sid in list(base):
                vu, cur = 0, sid
                while cur and cur not in self.styles and vu < 5:
                    cur, vu = base.get(cur), vu + 1
                if cur and cur in self.styles and sid not in self.styles:
                    self.styles[sid] = self.styles[cur]

    def label(self, p):
        num_id, ilvl = None, 0
        ppr = p.find(W + "pPr")
        if ppr is not None:
            ps = ppr.find(W + "pStyle")
            if ps is not None and ps.get(W + "val") in self.styles:
                num_id, ilvl = self.styles[ps.get(W + "val")]
            np_ = ppr.find(W + "numPr")
            if np_ is not None:
                ni = np_.find(W + "numId")
                il = np_.find(W + "ilvl")
                if ni is not None:
                    num_id = ni.get(W + "val")
                if il is not None:
                    ilvl = int(il.get(W + "val", "0"))
        if not num_id or num_id == "0" or num_id not in self.nums:
            return ""
        abs_id, surcharges = self.nums[num_id]
        niveaux = self.abstraits.get(abs_id, {})
        if ilvl not in niveaux:
            return ""
        # Compteurs par liste abstraite : les listes qui partagent une définition continuent la même suite.
        cpt = self.compteurs.setdefault(abs_id, {})
        depart = surcharges.get(ilvl, niveaux[ilvl][0])
        cpt[ilvl] = cpt.get(ilvl, depart - 1) + 1
        for k in list(cpt):
            if k > ilvl:
                del cpt[k]
        start, fmt, texte = niveaux[ilvl]
        if _format_num(1, fmt) is None:
            return ""

        def remplace(m):
            k = int(m.group(1)) - 1
            if k not in niveaux:
                return ""
            v = cpt.get(k, surcharges.get(k, niveaux[k][0]))
            f = _format_num(v, niveaux[k][1])
            return f if f is not None else ""
        return re.sub(r"%(\d)", remplace, texte).strip()


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
            numerotation = Numerotation(z, noms) if libelle == "corps" else None
            for p in racine.iter(W + "p"):
                label = numerotation.label(p) if numerotation else ""
                texte = _texte_paragraphe(p)
                if not texte.strip():
                    continue
                numero += 1
                affiche = (label + " " + texte).strip() if label else texte
                if libelle == "corps" and _est_titre(p, affiche):
                    section = re.sub(r"\s+", " ", affiche.strip())[:70]
                blocs.append(Bloc(libelle, numero, section, texte, label, _style(p)))

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
            if regle:
                # Règle de computation par défaut présente : délai couvert, qualification recommandée (décision de Yoann du 05/11/2026).
                gravite = "a_verifier"
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
                                    "Écrire le délai qualifié en minuscules (« dix jours ouvrés »), ou, dans un gros acte au standard M&A, ajouter la définition à l'article Définitions."))


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


# --------------------------------------------------------------------------
# Module F — Structure : numérotation, renvois internes, termes définis
# --------------------------------------------------------------------------

RE_TOC = re.compile(r"(?:\t|[.…]{4,})\s*\d+\s*$")
RE_ART_MOT = re.compile(r"^\s*\[?\s*(?:ARTICLE|Article)\s+(\d+)(?:\.(\d+(?:\.\d+)*))?\b")
RE_NUM_DEBUT = re.compile(r"^\s*(\d+)(?:\.(\d+(?:\.\d+)*))?\s*[.):\-–]?\s")


def _niveau_titre(style):
    m = re.match(r"^(?:Titre|Heading|titre|heading)\s?(\d)$", style or "")
    return int(m.group(1)) if m else 0


def _est_toc(b):
    st = (b.style or "").upper()
    return st.startswith("TM") or st.startswith("TOC") or bool(RE_TOC.search(b.texte))


def structure_articles(blocs):
    """Liste ordonnée des articles et sous-articles du corps : [(numéro tuple, bloc)]."""
    res = []
    for b in blocs:
        if b.partie != "corps" or _est_toc(b):
            continue
        aff = b.affiche()
        m = RE_ART_MOT.match(aff)
        niveau = _niveau_titre(b.style)
        if m and len(aff) < 200:
            num = (int(m.group(1)),) + tuple(int(x) for x in (m.group(2) or "").split(".") if x)
            res.append((num, b))
            continue
        if niveau in (1, 2, 3) and len(aff) < 200:
            m2 = RE_NUM_DEBUT.match(aff + " ")
            if m2:
                num = (int(m2.group(1)),) + tuple(int(x) for x in (m2.group(2) or "").split(".") if x)
                res.append((num, b))
                continue
        # Sous-article numéroté « 3.2 » en tête de paragraphe court (titre non stylé)
        m3 = re.match(r"^\s*(\d{1,2})\.(\d{1,2}(?:\.\d{1,2})*)\.?\s+[A-ZÉÈÀ]", aff)
        if m3 and len(aff) < 160:
            res.append(((int(m3.group(1)),) + tuple(int(x) for x in m3.group(2).split(".")), b))
    return res


RE_RENVOI = re.compile(
    r"\b(?:l['’]\s*)?(?:articles?|art\.)\s+(\d+(?:\.\d+)*)(?!\.?\d)(?:\s*(?:,|et|à)\s*(\d+(?:\.\d+)*)(?!\.?\d))?"
    r"(?=\s*(?:ci-dessus|ci-dessous|ci-apr[èe]s|ci-avant|des\s+pr[ée]sentes|du\s+pr[ée]sent|de\s+la\s+pr[ée]sente|[,;.)]|\s+(?:et|ou|pour|qui|sera|seront|ne|de\s+l|en)\b|$))",
    re.IGNORECASE)
RE_RENVOI_EXTERNE = re.compile(r"^\s*(?:des\s+[Ss]tatuts|du\s+[Pp]acte|du\s+[Cc]ode|de\s+la\s+[Cc]onvention|du\s+[Rr][èe]glement|de\s+l['’](?:[Aa]ccord|[Aa]cte\s+de)|du\s+[Cc]ontrat\s+de|du\s+[Tt]rait[ée]|de\s+la\s+loi|du\s+d[ée]cret|du\s+CGI|du\s+LPF)")


def module_f(blocs, constats, inventaire):
    corps = [b for b in blocs if b.partie == "corps"]
    arts = structure_articles(corps)
    principaux = [(n, b) for n, b in arts if len(n) == 1]
    numeros = [n[0] for n, _ in principaux]
    existants = set(n for n, _ in arts)
    confiance = False
    # F1 — Numérotation des articles
    if len(numeros) >= 3:
        attendu = numeros[0]
        anomalie = False
        for (n, b) in principaux:
            if n[0] != attendu:
                anomalie = True
                grav = "bloquant" if not b.label else "a_verifier"
                if n[0] < attendu:
                    objet = "Numéro d'article en double ou en arrière : %d après %d" % (n[0], attendu - 1)
                else:
                    objet = "Numérotation discontinue : article %d attendu, article %d trouvé" % (attendu, n[0])
                constats.append(Constat("F", grav, b.lieu(), objet, _court(b.affiche(), 120)))
            attendu = n[0] + 1
        confiance = not anomalie
        # Sous-articles : continuité sous chaque article
        par_parent = {}
        for n, b in arts:
            if len(n) == 2:
                par_parent.setdefault(n[0], []).append((n[1], b))
        for parent, liste in par_parent.items():
            att = liste[0][0]
            for k, b in liste:
                if k != att:
                    constats.append(Constat("F", "a_verifier", b.lieu(),
                                            "Sous-numérotation discontinue sous l'article %d : %d.%d attendu, %d.%d trouvé" % (parent, parent, att, parent, k),
                                            _court(b.affiche(), 120)))
                att = k + 1
            if parent not in numeros:
                constats.append(Constat("F", "a_verifier", liste[0][1].lieu(),
                                        "Sous-article %d.%d rattaché à un article %d introuvable" % (parent, liste[0][0], parent),
                                        _court(liste[0][1].affiche(), 120)))
    # F2 — Renvois internes
    if len(numeros) >= 3:
        for b in corps:
            if _est_toc(b):
                continue
            t = b.texte
            for m in RE_RENVOI.finditer(t):
                suite = t[m.end():m.end() + 40]
                if RE_RENVOI_EXTERNE.match(suite):
                    continue
                avant = t[max(0, m.start() - 60):m.start()]
                if re.search(r"\b(?:son|sa|ses|leur|leurs|dudit|de\s+ladite|dudit\s+acte)\s*$", avant, re.IGNORECASE):
                    continue  # article d'un autre acte (« à son article 11 »)
                if re.search(SOURCES_LEGALES, suite[:30], re.IGNORECASE) or re.search(r"\b(?:CGI|LPF|code|C\.\s?civ|C\.\s?com)\b[^.]{0,20}$", avant, re.IGNORECASE):
                    continue
                for g in (m.group(1), m.group(2)):
                    if not g:
                        continue
                    num = tuple(int(x) for x in g.split("."))
                    if num[0] > 99:
                        continue  # numéro d'article de code
                    subs = sorted(n[1] for n in existants if len(n) == 2 and n[0] == num[0])
                    subs_fiables = bool(subs) and subs == list(range(1, len(subs) + 1))
                    cible_ok = num in existants or (len(num) > 1 and num[:1] in existants and not subs_fiables) \
                        or (len(num) > 2 and num[:2] in existants)
                    if not cible_ok:
                        if len(num) == 1 and num[0] not in numeros:
                            grav = "bloquant" if confiance and num[0] > max(numeros) else "a_verifier"
                        else:
                            grav = "a_verifier"
                        constats.append(Constat("F", grav, b.lieu(),
                                                "Renvoi interne vers l'article %s, introuvable dans le document" % g,
                                                "Articles repérés : %s. %s" % (_plage(numeros), _extrait(t, m.start(), m.end()))))
    elif len(numeros) < 3 and any(i["type"] == "renvoi interne" for i in inventaire):
        constats.append(Constat("F", "information", "Document",
                                "Structure en articles non reconnue : renvois internes non contrôlés",
                                "Le document ne comporte pas au moins trois articles identifiables (mot « Article », titre numéroté)."))
    # F3 — Termes définis
    termes = {}
    for b in corps:
        aff = b.affiche()
        for m in re.finditer(r"^\s*(?:[-–•]\s*)?[«\"“]\s*([^»\"”]{2,60}?)\s*[»\"”]\s*(?:,|:|–|—|-|d[ée]signe|signifie|s['’]entend|a\s+le\s+sens|d[ée]signent|signifient)", aff):
            termes.setdefault(m.group(1).strip(), []).append(("liste", b))
        for m in re.finditer(r"\((?:ci-?apr[èe]s|ensemble|ci-dessous|individuellement|chacun)?[^()]{0,50}?[«\"“]\s*([^»\"”]{2,60}?)\s*[»\"”][^()]{0,40}\)", aff):
            termes.setdefault(m.group(1).strip(), []).append(("incise", b))
        if not RE_ART_MOT.match(aff) and not _niveau_titre(b.style):
            m = re.match(r"^\s*(?:[-–•]\s*)?([A-ZÉÈÀ][\wÀ-ÿ'’\-]*(?:\s+(?:de|du|des|d['’]|de\s+la|à|en|et)?\s*[A-ZÉÈÀ][\wÀ-ÿ'’\-]*){0,4})\s*:\s", aff)
            if m and len(aff) > len(m.group(0)) + 25 and "finition" in (b.section or ""):
                termes.setdefault(m.group(1).strip(), []).append(("liste", b))
    nets = {}
    for k, v in termes.items():
        k2 = re.sub(r"^(?:Les|Le|La|L['’])\s*", "", k).replace("(s)", "").strip()
        if " et le verbe " in k2 or not k2[:1].isupper() or len(k2) > 60:
            continue
        nets.setdefault(k2, []).extend(v)
    termes = nets
    texte_corps = [(b, b.texte) for b in corps if not _est_toc(b)]
    def _motif_terme(terme):
        mots = terme.split()
        corps = r"\s+".join(re.escape(m) + r"(?:s|x)?" for m in mots)
        return re.compile(r"(?<![%s])%s(?![%s])" % (LETTRE, corps, LETTRE))

    def _forme(x):
        return " ".join(re.sub(r"[sx]$", "", w) for w in _sans_accent(x.lower()).split())

    for terme, defs in termes.items():
        motif = _motif_terme(terme)
        paragraphes_def = set(id(b) for _, b in defs)
        usages = sum(len(motif.findall(t)) for b, t in texte_corps if id(b) not in paragraphes_def)
        listes = [b for k, b in defs if k == "liste"]
        if usages == 0:
            constats.append(Constat("F", "a_verifier", defs[0][1].lieu(),
                                    "Terme défini « %s » jamais utilisé ensuite" % terme,
                                    "Supprimer la définition ou vérifier que le terme est employé sous la même forme."))
        if len(listes) > 1 and len(set(_court(b.texte, 300) for b in listes)) > 1:
            constats.append(Constat("F", "a_verifier", listes[1].lieu(),
                                    "Terme « %s » défini plusieurs fois" % terme,
                                    "Premières définitions : %s | %s" % (_court(listes[0].texte, 90), _court(listes[1].texte, 90))))
    if len(termes) >= 5:
        connus = set(termes)
        connus_bas = set(_forme(x) for x in connus)
        tout_texte = "\n".join(t for _, t in texte_corps)
        candidats = {}
        motif_cand = re.compile(r"(?<=[a-zà-ÿ,;:)»] )([A-ZÉÈÀ][a-zà-ÿ'’\-]+(?:\s+(?:de\s+la|de|du|des|d['’]|à|en|et|aux?)?\s*[A-ZÉÈÀ][a-zà-ÿ'’\-]+){1,3})")
        for b, t in texte_corps:
            for m in motif_cand.finditer(t):
                cand = m.group(1)
                candidats.setdefault(cand, []).append(b)
        exclus = re.compile(r"^(?:Messieurs|Mesdames|Monsieur|Madame|Mademoiselle|Avocat|Notaire|Expert|Ma[îi]tre|Me|Docteur|Dr|Tribunal|Cour|Conseil|Code|Registre|Greffe|R[ée]publique|Banque|Caisse|Cr[ée]dit|Soci[ée]t[ée]\s+G[ée]n[ée]rale|Union|[ÉE]tat|Direction|Minist[èe]re|Journal|Bulletin|Chambre|Ordre|Conseil|Centre|Institut|Agence|Service)\b")
        retenus = []
        for cand, bs in candidats.items():
            if len(bs) < 3 or exclus.match(cand) or re.search(r"\b(?:Monsieur|Madame|Mme|M)$", cand) \
                    or re.match(r"^(?:Route|Rue|Avenue|Boulevard|Chemin|Place|All[ée]e|Impasse|Quai|Parc|Zone|ZAC|ZI)\b", cand) \
                    or re.search(r"(?:Monsieur|Madame|Mademoiselle|Messieurs|M\.|Mme|Me|Ma[îi]tre|Docteur|[Rr]ue|[Aa]venue|[Bb]oulevard|[Pp]lace|[Cc]hemin|[Qq]uai)\s+(?:du\s+|de\s+la\s+|des\s+)?" + re.escape(cand), tout_texte) \
                    or _forme(cand) in connus_bas:
                continue
            if any(_forme(cand).startswith(_forme(k)) or _forme(k).startswith(_forme(cand)) for k in connus):
                continue
            retenus.append((len(bs), cand, bs[0]))
        retenus.sort(reverse=True)
        for nb, cand, b in retenus[:10]:
            constats.append(Constat("F", "a_verifier", b.lieu(),
                                    "Expression en majuscules « %s » employée %d fois sans définition repérée" % (cand, nb),
                                    "Terme défini manquant, ou majuscule à supprimer (nom propre : ignorer)."))
        if len(retenus) > 10:
            constats.append(Constat("F", "information", "Document",
                                    "%d autres expressions en majuscules sans définition, non détaillées" % (len(retenus) - 10), ""))


def _plage(numeros):
    if not numeros:
        return "aucun"
    return "%d à %d (%d)" % (min(numeros), max(numeros), len(numeros))


# --------------------------------------------------------------------------
# Module G — Fidélité au modèle (PV, procurations, actes de la vie sociale)
# --------------------------------------------------------------------------

import difflib

RE_JETON = re.compile(r"[«»\"“”()\[\]]|(?:[dlnmstjcDLNMSTJC]|qu|Qu)['’]|[\wÀ-ÿ\-./●]+")


MOIS = {"janvier", "février", "fevrier", "mars", "avril", "mai", "juin", "juillet", "août", "aout",
        "septembre", "octobre", "novembre", "décembre", "decembre"}
MOTS_OUTILS = {"de", "du", "des", "d", "d'", "d’", "la", "le", "les", "l", "l'", "l’", "qu'", "qu’", "à", "a", "au", "aux",
               "et", "en", "sur", "sous", "chez", "rue", "avenue", "boulevard", "place", "chemin", "route", "impasse", "allée"}


def _norm_mot(t):
    """Forme comparable d'un mot : minuscules, sans accent, sans marque du féminin ni du pluriel."""
    t = _sans_accent(t.lower())
    if len(t) > 3:
        t = re.sub(r"s$", "", t)
    if len(t) > 1:
        t = t.rstrip("e")
    return t


def _est_donnee(tok, premier=False):
    if re.search(r"\d|●|\[|\]", tok):
        return True
    if tok.lower() in MOIS:
        return True
    lettres = re.sub(r"[^A-Za-zÀ-ÿ]", "", tok)
    if not lettres:
        return True  # ponctuation
    if len(lettres) >= 2 and lettres.isupper():
        return True
    if lettres[0].isupper() and not premier:
        return True
    return False


def _squelette(texte):
    toks = RE_JETON.findall(texte)
    return " ".join(_norm_mot(t) for i, t in enumerate(toks)
                    if not _est_donnee(t, i == 0) and t.lower() not in MOTS_OUTILS)


def lire_blocs_corps(chemin):
    ext = os.path.splitext(chemin)[1].lower()
    blocs = lire_docx(chemin)[0] if ext == ".docx" else lire_texte(chemin)[0]
    return [b for b in blocs if b.partie in ("corps", "texte") and b.texte.strip()]


def module_g(blocs, constats, chemin_modele, config):
    modele = lire_blocs_corps(chemin_modele)
    livrable = [b for b in blocs if b.partie in ("corps", "texte") and b.texte.strip()]
    sq_m = [_squelette(b.affiche()) for b in modele]
    sq_l = [_squelette(b.affiche()) for b in livrable]
    sm = difflib.SequenceMatcher(None, sq_m, sq_l, autojunk=False)
    nb_donnees, nb_redac = 0, 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                if modele[i1 + k].affiche() != livrable[j1 + k].affiche():
                    nb_donnees += 1
            continue
        restants_l = list(range(j1, j2))
        for i in range(i1, i2):
            meilleur, score = None, 0.0
            for j in restants_l:
                r = difflib.SequenceMatcher(None, sq_m[i].split(), sq_l[j].split(), autojunk=False).ratio()
                if r > score:
                    meilleur, score = j, r
            if meilleur is not None and score >= 0.5:
                restants_l.remove(meilleur)
                ecart = _diff_mots(modele[i].affiche(), livrable[meilleur].affiche())
                if not ecart:
                    nb_donnees += 1
                    continue
                nb_redac += 1
                constats.append(Constat("G", "a_verifier", livrable[meilleur].lieu(),
                                        "Rédaction différente du modèle (§ %d du modèle) : écart voulu à justifier, ou à corriger" % modele[i].numero,
                                        ecart))
            else:
                constats.append(Constat("G", "a_verifier", "Modèle, § %d" % modele[i].numero,
                                        "Paragraphe du modèle absent du livrable",
                                        _court(modele[i].affiche(), 160)))
        for j in restants_l:
            constats.append(Constat("G", "a_verifier", livrable[j].lieu(),
                                    "Paragraphe ajouté, absent du modèle",
                                    _court(livrable[j].affiche(), 160)))
    # Données du précédent restées dans le livrable
    cabinet = set(x.lower() for x in config.get("donnees_cabinet", []))
    communs = set(x.lower() for x in config.get("mots_capitales_courants", []))
    texte_l = "\n".join(b.affiche() for b in livrable)
    vues = set()
    for b in modele:
        for m in re.finditer(r"\b\d{3}\s?\d{3}\s?\d{3}\b|\b\d{1,3}(?:[  ]\d{3})+\b|[«“]\s*([^»”]{2,40}?)\s*[»”]|\b[A-ZÉÈÀ][A-ZÉÈÀ'’\-]{3,}\b", b.texte):
            val = (m.group(1) or m.group(0)).strip()
            cle = val.lower()
            if cle in vues or cle in cabinet or cle in communs or len(val) < 3:
                continue
            vues.add(cle)
            if re.search(r"(?<![\wÀ-ÿ])%s(?![\wÀ-ÿ])" % re.escape(val), texte_l):
                constats.append(Constat("G", "a_verifier", "Document",
                                        "Donnée du modèle reprise telle quelle : « %s »" % _court(val, 50),
                                        "Présente dans le modèle (§ %d) et dans le livrable : vérifier qu'il s'agit bien d'une donnée du dossier et non d'un reliquat du précédent." % b.numero))
    constats.append(Constat("G", "information", "Document",
                            "Comparaison au modèle « %s » : %d paragraphe(s) aux données remplacées, %d rédaction(s) modifiée(s)"
                            % (os.path.basename(chemin_modele), nb_donnees, nb_redac), ""))


def _diff_mots(a, b):
    """Écarts de rédaction entre deux paragraphes, hors données du dossier ; chaîne vide s'il n'y en a pas."""
    ta, tb = RE_JETON.findall(a), RE_JETON.findall(b)
    na, nb = [_norm_mot(t) for t in ta], [_norm_mot(t) for t in tb]
    sm = difflib.SequenceMatcher(None, na, nb, autojunk=False)
    morceaux = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        sup = [t for t in ta[i1:i2]]
        aj = [t for t in tb[j1:j2]]
        tous = sup + aj
        if all(_est_donnee(t) for t in tous):
            continue
        # Petits mots qui changent avec une donnée (« de la Vieille Ville » → « des Exemples »)
        if any(_est_donnee(t) for t in tous) and all(_est_donnee(t) or t.lower() in MOTS_OUTILS for t in tous):
            continue
        if sup:
            morceaux.append("− « %s »" % _court(" ".join(sup), 70))
        if aj:
            morceaux.append("+ « %s »" % _court(" ".join(aj), 70))
    return " ; ".join(morceaux[:6])


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
    "F": "F. Structure : numérotation, renvois internes, termes définis",
    "G": "G. Fidélité au modèle",
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
    for mod in "ACDEFGB":
        liste = [c for c in constats if c.module == mod]
        if mod == "G" and not liste:
            continue
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
        l.append("## Renvois internes repérés (%d)" % len(internes))
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


def controler(chemin, config, modele=None):
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
    module_f(blocs, constats, inventaire)
    if modele:
        module_g(blocs, constats, modele, config)
    return constats, inventaire, len(blocs), meta


def main():
    ap = argparse.ArgumentParser(description="Contrôleur de livrable ECA EXPERTISE (modules A à G).")
    ap.add_argument("livrable")
    ap.add_argument("--config")
    ap.add_argument("--rapport", help="Chemin du rapport Markdown (sinon affiché)")
    ap.add_argument("--json", help="Chemin d'un export JSON des constats et de l'inventaire")
    ap.add_argument("--modele", help="Modèle du dépôt dont le livrable doit reprendre le texte (module G : PV, procurations)")
    args = ap.parse_args()
    try:
        config = charger_config(args.config)
        constats, inventaire, nb, meta = controler(args.livrable, config, args.modele)
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
