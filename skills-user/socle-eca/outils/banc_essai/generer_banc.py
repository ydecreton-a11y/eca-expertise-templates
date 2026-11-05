#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Banc d'essai du contrôleur de livrable : génère des documents FICTIFS
(noms inventés) avec des erreurs insérées et connues, plus leur version
propre, puis vérifie que le contrôleur trouve chaque erreur et rien de plus
sur les versions propres.

Usage : python3 generer_banc.py   (nécessite python-docx, pour le banc seul)
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

from docx import Document

ICI = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(os.path.dirname(ICI), "controle_livrable.py")


def doc_protocole(errone):
    d = Document()
    d.core_properties.author = "Me Violaine Schmidt" if errone else "Yoann Decreton"
    d.core_properties.last_modified_by = "Yoann Decreton"
    d.add_heading("PROTOCOLE DE CESSION DE TITRES", 0)
    d.add_paragraph("ENTRE LES SOUSSIGNÉS : M. Jean EXEMPLE, ci-après le « Cédant », et la société HORIZON BOIS SAS, ci-après le « Cessionnaire ».")
    d.add_heading("Article 1 — Définitions et interprétation", 1)
    if not errone:
        d.add_paragraph("« Jours Ouvrés » désigne les jours de la semaine à l'exception du samedi, du dimanche et des jours fériés légaux en France.")
    d.add_paragraph("« Titres » désigne les mille (1 000) actions composant le capital social de la Société.")
    d.add_heading("Article 2 — Prix", 1)
    if errone:
        d.add_paragraph("Le prix de cession est fixé à 250 000 € (deux cent mille euros), payable comptant à la Date de Réalisation.")   # E1
        d.add_paragraph("Le Cédant cède cinq cents (5 000) actions au titre de la première tranche.")                                    # E2
    else:
        d.add_paragraph("Le prix de cession est fixé à 250 000 € (deux cent cinquante mille euros), payable comptant à la Date de Réalisation.")
        d.add_paragraph("Le Cédant cède cinq cents (500) actions au titre de la première tranche.")
    d.add_heading("Article 3 — Conditions suspensives", 1)
    if errone:
        d.add_paragraph("Les conditions suspensives devront être levées dans un délai de quinze (15) jours à compter de la signature.")    # A1
        d.add_paragraph("Le Cessionnaire notifiera sa décision dans les 10 Jours Ouvrés suivant la réception.")                           # A2 (terme non défini)
        d.add_paragraph("L'agrément est réputé acquis à défaut de réponse dans les 30 jours de la notification.")                          # A3
    else:
        d.add_paragraph("Les conditions suspensives devront être levées dans un délai de quinze (15) jours calendaires à compter de la signature.")
        d.add_paragraph("Le Cessionnaire notifiera sa décision dans les 10 Jours Ouvrés suivant la réception.")
        d.add_paragraph("L'agrément est réputé acquis à défaut de réponse dans les 30 jours ouvrables de la notification.")
    d.add_heading("Article 4 — Expertise", 1)
    d.add_paragraph("À défaut d'accord, le prix est fixé par un expert désigné conformément à l'article 1843-4 du Code civil, "
                    "dans les conditions précisées par Cass. com., 12 février 2025, n° 23-11.410.")
    d.add_paragraph("Le régime de l'article 150-0 B ter du CGI et la doctrine BOI-RPPM-PVBMI-30-10-60 sont réservés ; voir également l'article 3 des présentes.")
    d.add_heading("Article 5 — Notifications", 1)
    if errone:
        d.add_paragraph("Adresse du Cessionnaire : [●], ou toute autre adresse à compléter.")                                              # D1, D2
        d.add_paragraph("Clause rédigée d'après le modèle de pacte de Violaine Schmidt.")                                                    # C1 (x2) + modèle
    else:
        d.add_paragraph("Adresse du Cessionnaire : 12 rue des Exemples, 59000 Lille.")
    d.add_paragraph("Les Titres sont cédés libres de tout nantissement.")
    d.add_paragraph("Fait à Cambrai, le 5 novembre 2026, en deux exemplaires originaux.")
    return d


def doc_procuration(errone):
    d = Document()
    d.core_properties.author = "Yoann Decreton"
    d.add_heading("POUVOIR", 0)
    d.add_paragraph("Je soussigné, M. Paul FICTIF, gérant de la SARL ATELIER FICTIF, donne pouvoir à ECA EXPERTISE afin d'accomplir les formalités "
                    "consécutives aux décisions du 3 novembre 2026.")
    if errone:
        d.add_paragraph("Le présent pouvoir est consenti à la société CELEFI pour une durée de huit jours.")                                # C2 + A4
        d.add_paragraph("Capital social : 7 500 euros (sept mille cinq cents euros). Siège : {{ADRESSE_SIEGE}}.")                          # D3
    else:
        d.add_paragraph("Le présent pouvoir est consenti pour une durée de huit jours calendaires.")
        d.add_paragraph("Capital social : 7 500 euros (sept mille cinq cents euros). Siège : 3 place du Marché, 59400 Cambrai.")
    d.add_paragraph("Fait à Cambrai, le 5 novembre 2026.")
    return d


def doc_pacte(errone):
    d = Document()
    d.core_properties.author = "Yoann Decreton"
    d.add_heading("PACTE D'ASSOCIÉS", 0)
    d.add_heading("Article 6 — Droit de préemption", 1)
    if errone:
        d.add_paragraph("Le bénéficiaire dispose de trente jours pour exercer son droit, au prix de 1 200 000 € (un million deux cent mille euros).")  # A5
        d.add_paragraph("Le prix est minoré de 10 % (dix pour cent) en cas de faute ; [PERSONNE_1] en est informé.")                               # D4
    else:
        d.add_paragraph("Le bénéficiaire dispose de trente jours calendaires pour exercer son droit, au prix de 1 200 000 € (un million deux cent mille euros).")
        d.add_paragraph("Le prix est minoré de 10 % (dix pour cent) en cas de faute ; l'associé concerné en est informé.")
    d.add_paragraph("Les associés conviennent que l'abattement prévu à l'article 150-0 D du CGI s'applique au taux de 50 % dans les conditions légales.")
    return d


def doc_structure(errone):
    d = Document()
    d.core_properties.author = "Yoann Decreton"
    d.add_heading("ACTE DE CESSION", 0)
    d.add_paragraph("ENTRE M. Jean EXEMPLE (ci-après le « Cédant ») ET la société HORIZON BOIS (ci-après le « Cessionnaire »).")
    d.add_heading("ARTICLE 1 : DÉFINITIONS", 1)
    d.add_paragraph("« Actions » désigne les actions cédées.")
    d.add_paragraph("« Prix » désigne le prix de cession des Actions.")
    d.add_paragraph("« Date de Réalisation » désigne la date de transfert des Actions." if not errone else "« Comptes de Référence » désigne les comptes du dernier exercice.")
    d.add_paragraph("« Garantie » désigne la garantie d'actif et de passif consentie par le Cédant.")
    if errone:
        d.add_paragraph("« Prix » désigne le prix ajusté selon l'article 2.")              # F : défini deux fois
    d.add_heading("ARTICLE 2 : PRIX", 1)
    d.add_heading("2.1 Montant", 2)
    d.add_paragraph("Le Prix est payé par le Cessionnaire au Cédant à la Date de Réalisation.")
    d.add_heading("2.3 Paiement" if errone else "2.2 Paiement", 2)            # F : 2.2 manquant
    d.add_paragraph("Le paiement intervient à la Date de Réalisation, sur les Comptes de Référence." if errone
                    else "Le paiement intervient à la Date de Réalisation par virement.")
    d.add_heading("ARTICLE 3 : GARANTIE", 1)
    d.add_paragraph("Le Cédant consent la Garantie au Cessionnaire." if not errone else "Le Cédant consent une garantie au Cessionnaire.")  # F : Garantie inutilisée
    d.add_heading("ARTICLE 5 : NOTIFICATIONS" if errone else "ARTICLE 4 : NOTIFICATIONS", 1)   # F : article 4 manquant
    d.add_paragraph("Les notifications prévues à l'article 7 des présentes sont faites par lettre recommandée." if errone   # F : renvoi vers 7
                    else "Les notifications prévues à l'article 2.2 ci-dessus sont faites par lettre recommandée.")
    d.add_paragraph("Le Cédant remet les registres à la Date de Réalisation.")
    d.add_paragraph("Fait à Cambrai, le 5 novembre 2026.")
    return d


def _remplacer(doc, remplacements, supprimer=(), ajouter_apres=None):
    for p in list(doc.paragraphs):
        t = p.text
        if any(x in t for x in supprimer):
            p._element.getparent().remove(p._element)
            continue
        n = t
        for a, b in remplacements:
            n = n.replace(a, b)
        if n != t and p.runs:
            p.runs[0].text = n
            for r in p.runs[1:]:
                r.text = ""
        if ajouter_apres and ajouter_apres[0] in n:
            nouveau = doc.add_paragraph(ajouter_apres[1])
            p._element.addnext(nouveau._element)


DONNEES_FICTIVES = [
    ("Madame Céline, Annick LEGRAND", "Monsieur Paul, Henri FICTIF"), ("Je soussignée", "Je soussigné"),
    ("16 décembre 1983 à ARRAS (62)", "3 mars 1979 à DOUAI (59)"), ("Née le", "Né le"),
    ("5, rue de la Vieille Ville à SIMENCOURT (62123)", "12, rue des Exemples à LILLE (59000)"),
    ("Agissant en qualité de Présidente", "Agissant en qualité de Président"),
    ("« CeLeFi »", "« ATELIER FICTIF »"), ("20 000 euros", "7 500 euros"),
    ("951 054 154 R.C.S. ARRAS", "912 345 678 R.C.S. LILLE MÉTROPOLE"),
    ("Centre Commercial LECLERC – 95, avenue LOBBEDEZ – 62000 ARRAS", "3 place du Marché – 59400 CAMBRAI"),
    ("par suppression du nom d’usage « FICHEUX » à la suite du jugement de divorce du Tribunal judiciaire d’ARRAS du 11 juin 2024",
     "par suppression du nom d’usage « DURAND » à la suite du jugement de divorce du Tribunal judiciaire de LILLE du 3 février 2025"),
]


def docs_modele(dossier):
    import glob
    racine = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
    trouves = [f for f in glob.glob(os.path.join(racine, "**", "*.docx"), recursive=True)
               if "celefi" in os.path.basename(f).lower() and "pouvoir" in os.path.basename(f).lower()]
    if not trouves:
        print("Modèle CELEFI introuvable dans le dépôt : banc G ignoré")
        return None
    modele = trouves[0]
    shutil.copy(modele, os.path.join(dossier, "modele_procuration.docx"))
    fid = Document(modele)
    _remplacer(fid, DONNEES_FICTIVES)
    fid.save(os.path.join(dossier, "g_fidele.docx"))
    par = Document(modele)
    _remplacer(par, DONNEES_FICTIVES + [("L’exécution de ce mandat vaudra décharge au mandataire.",
                                          "Le mandataire sera valablement déchargé par l’accomplissement de sa mission."),
                                         ("produire toutes pièces justificatives", "fournir les pièces qui seraient utiles")],
               supprimer=("de la modification de mon adresse personnelle",),
               ajouter_apres=("de la mise à jour des informations relatives aux bénéficiaires effectifs.",
                              "de la nomination d’un directeur général délégué ;"))
    par.save(os.path.join(dossier, "g_reformule.docx"))
    rel = Document(modele)
    _remplacer(rel, [x for x in DONNEES_FICTIVES if not x[0].startswith("951")])
    rel.save(os.path.join(dossier, "g_reliquat.docx"))
    return os.path.join(dossier, "modele_procuration.docx")


def ajouter_suivi_et_commentaire(chemin):
    """Insère une modification suivie, un commentaire et un texte masqué dans le XML."""
    tmp = chemin + ".tmp"
    with zipfile.ZipFile(chemin) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                x = data.decode("utf-8")
                ins = ('<w:p><w:ins w:id="901" w:author="Relecteur" w:date="2026-11-05T10:00:00Z"><w:r><w:t>Phrase insérée en suivi.</w:t></w:r></w:ins></w:p>'
                       '<w:p><w:r><w:rPr><w:vanish/></w:rPr><w:t>Note masquée : prix plancher du client 180 000 €.</w:t></w:r></w:p>'
                       '<w:p><w:r><w:rPr><w:highlight w:val="yellow"/></w:rPr><w:t>Point surligné à revoir.</w:t></w:r></w:p>')
                x = x.replace("<w:sectPr", ins + "<w:sectPr", 1)
                data = x.encode("utf-8")
            zout.writestr(item, data)
        if "word/comments.xml" not in zin.namelist():
            zout.writestr("word/comments.xml",
                          '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                          '<w:comments xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                          '<w:comment w:id="0" w:author="YD"><w:p><w:r><w:t>Vérifier avec le client.</w:t></w:r></w:p></w:comment>'
                          '</w:comments>')
    os.replace(tmp, chemin)


# Erreurs attendues sur les documents erronés : (module, gravité, fragment de l'objet)
ATTENDU = {
    "protocole_errone.docx": [
        ("E", "bloquant", "250 000"), ("E", "bloquant", "5 000"),
        ("A", "bloquant", "quinze (15) jours"), ("A", "bloquant", "Jours Ouvrés"), ("A", "bloquant", "30 jours"),
        ("D", "bloquant", "[●]"), ("D", "bloquant", "à compléter"),
        ("C", "bloquant", "Violaine Schmidt"), ("C", "bloquant", "Métadonnées"),
        ("D", "bloquant", "Suivi des modifications"), ("D", "bloquant", "commentaire"), ("D", "bloquant", "texte masqué"),
        ("D", "a_verifier", "surligné"),
        ("B", "a_verifier", "1843-4"), ("B", "a_verifier", "23-11.410"), ("B", "a_verifier", "BOI-RPPM-PVBMI-30-10-60"),
        ("B", "a_verifier", "150-0 B ter"),
    ],
    "procuration_erronee.docx": [
        ("C", "bloquant", "CELEFI"), ("A", "bloquant", "huit jours"), ("D", "bloquant", "{{ADRESSE_SIEGE}}"),
    ],
    "structure_erronee.docx": [
        ("F", "bloquant", "Numérotation discontinue"), ("F", "a_verifier", "2.2 attendu"),
        ("F", "a_verifier", "article 7"), ("F", "a_verifier", "« Garantie » jamais utilisé"),
        ("F", "a_verifier", "« Prix » défini plusieurs fois"), ("F", "a_verifier", "« Date de Réalisation »"),
    ],
    "pacte_errone.docx": [
        ("A", "bloquant", "trente jours"), ("D", "bloquant", "[PERSONNE_1]"),
        ("B", "a_verifier", "150-0 D"), ("B", "a_verifier", "50 %"),
    ],
}


ATTENDU_G = {
    "g_reformule.docx": [("G", "a_verifier", "Rédaction différente du modèle"), ("G", "a_verifier", "Paragraphe du modèle absent"),
                         ("G", "a_verifier", "Paragraphe ajouté")],
    "g_reliquat.docx": [("G", "a_verifier", "951 054 154")],
}


def lancer(chemin, modele=None):
    sortie = tempfile.mktemp(suffix=".json")
    cmd = [sys.executable, "-I", SCRIPT, chemin, "--json", sortie, "--rapport", os.devnull]
    if modele:
        cmd += ["--modele", modele]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode == 1:
        raise RuntimeError(r.stderr)
    import json
    with open(sortie, encoding="utf-8") as f:
        return json.load(f), r.returncode


def main():
    dossier = os.path.join(ICI, "documents")
    shutil.rmtree(dossier, ignore_errors=True)
    os.makedirs(dossier)
    for nom, fabrique in (("protocole", doc_protocole), ("procuration", doc_procuration), ("pacte", doc_pacte)):
        suff_err = "erronee" if nom == "procuration" else "errone"
        p_err = os.path.join(dossier, "%s_%s.docx" % (nom, suff_err))
        p_ok = os.path.join(dossier, "%s_propre.docx" % nom)
        fabrique(True).save(p_err)
        fabrique(False).save(p_ok)
        if nom == "protocole":
            ajouter_suivi_et_commentaire(p_err)
    doc_structure(True).save(os.path.join(dossier, "structure_erronee.docx"))
    doc_structure(False).save(os.path.join(dossier, "structure_propre.docx"))
    modele = docs_modele(dossier)

    total, trouves, faux = 0, 0, []
    for fichier in sorted(os.listdir(dossier)):
        if fichier.startswith(("g_", "modele_")):
            continue
        res, code = lancer(os.path.join(dossier, fichier))
        constats = res["constats"]
        if fichier in ATTENDU:
            for mod, grav, frag in ATTENDU[fichier]:
                total += 1
                ok = any(c["module"] == mod and c["gravite"] == grav and (frag in c["objet"] or frag in c["detail"] or frag in c["lieu"])
                         for c in constats)
                trouves += ok
                print("%s %-28s %s %-10s %s" % ("OK " if ok else "RATÉ", fichier, mod, grav, frag))
            print("    code de sortie : %d (attendu 2)" % code)
        else:
            bloquants = [c for c in constats if c["gravite"] == "bloquant"]
            averif = [c for c in constats if c["gravite"] == "a_verifier" and c["module"] != "B"]
            print("PROPRE %-24s bloquants : %d · à vérifier hors inventaire : %d · code %d"
                  % (fichier, len(bloquants), len(averif), code))
            for c in bloquants + averif:
                faux.append((fichier, c))
                print("    fausse alerte ? %s %s — %s" % (c["module"], c["gravite"], c["objet"]))
    if modele:
        for fichier in ("g_fidele.docx", "g_reformule.docx", "g_reliquat.docx"):
            res, code = lancer(os.path.join(dossier, fichier), modele)
            cg = [c for c in res["constats"] if c["module"] == "G"]
            if fichier in ATTENDU_G:
                for mod, grav, frag in ATTENDU_G[fichier]:
                    total += 1
                    ok = any(c["gravite"] == grav and (frag in c["objet"] or frag in c["detail"]) for c in cg)
                    trouves += ok
                    print("%s %-28s %s %-10s %s" % ("OK " if ok else "RATÉ", fichier, mod, grav, frag))
            else:
                alertes = [c for c in cg if c["gravite"] != "information"]
                print("PROPRE %-24s alertes G : %d" % (fichier, len(alertes)))
                for c in alertes:
                    faux.append((fichier, c))
                    print("    fausse alerte ? %s — %s | %s" % (c["gravite"], c["objet"], c["detail"][:120]))
            for c in cg:
                if c["gravite"] == "information":
                    print("    " + c["objet"])
    print("\nDétection : %d / %d erreurs insérées" % (trouves, total))
    print("Alertes sur les versions propres : %d" % len(faux))
    return 0 if trouves == total and not faux else 3


if __name__ == "__main__":
    sys.exit(main())
