#!/usr/bin/env python3
"""Outil de l'index des références des skills ECA (utilisé par maintenance-skills).

  python3 refs.py extract   <dossier_skills> <sortie.json>
  python3 refs.py reconcile <references-index.json> <extraction.json> [AAAA-MM-JJ]
  python3 refs.py render    <references-index.json> <references-index.md>

extract   : relève les références d'articles citées dans tous les SKILL.md
            (dossier contenant un sous-dossier par skill, ou des fichiers .md).
reconcile : ajoute à l'index les références nouvelles (statut « a_verifier »),
            retire celles qui ne sont plus citées, rafraîchit les occurrences ;
            affiche le bilan. Ne touche ni aux BOFiP, ni à la jurisprudence,
            ni aux textes, pièges et échéances (tenus à la main).
render    : régénère la vue lisible .md à partir du .json.
L'extraction est heuristique : son résultat se relit (les faux positifs se
corrigent dans REMAP / DROP ci-dessous, jamais en silence).
"""
import json, re, os, sys, collections, datetime
CGI = 'code-general-des-impots'
CODES = [
    (r'\bCGI\b|code général des impôts', CGI),
    (r'\bC\. ?com\.|code de commerce', 'code-de-commerce'),
    (r'\bC\. ?civ\.|code civil', 'code-civil'),
    (r'\bC\. ?trav\.|code du travail', 'code-du-travail'),
    (r'\bC\. ?mon\. ?fin\.|\bCMF\b', 'code-monetaire-et-financier'),
    (r'\bLPF\b', 'livre-des-procedures-fiscales'),
    (r'\bCSS\b|sécurité sociale', 'code-de-la-securite-sociale'),
    (r'\bC\. ?prop\. ?intell\.|\bCPI\b', 'code-de-la-propriete-intellectuelle'),
    (r'\bC\. ?conso\.', 'code-de-la-consommation'),
    (r'\bC\. ?assur\.', 'code-des-assurances'),
    (r'\bCIBS\b', 'code-des-impositions-sur-les-biens-et-services'),
]
ART = re.compile(r"(?<![\w/-])(?:(?:art\.|Art\.|articles?|Article)\s*)?((?:[LRD]\.?\s?\*?\s?)?\d{1,4}(?:-\d{1,3}){0,3}(?:\s(?:A|B|C|D|E|F|G|H|bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|duodecies|quindecies)\b(?:\s(?:A|B|C|D|E|F|G|H|bis|ter|quater))?)?)(?=[\s,.;:)»|\]\"]|$)")
REMAP = {('code-civil', 'L. 221-14'): ('code-de-commerce', 'L. 221-14'),
         ('code-de-la-securite-sociale', '223 sexies'): (CGI, '223 sexies'),
         ('code-de-la-securite-sociale', '224'): (CGI, '224'),
         (CGI, 'L. 80 A'): ('livre-des-procedures-fiscales', 'L. 80 A'),
         (CGI, 'L. 132-12'): ('code-des-assurances', 'L. 132-12'),
         (CGI, '1075'): ('code-civil', '1075'),
         ('code-civil', '3'): ('code-civil', '1137'),
         (CGI, '2 ter'): (CGI, '200 A'),
         ('code-du-travail', 'L. 141-23'): ('code-de-commerce', 'L. 141-23')}
DROP = {('code-de-commerce', '2026-403'), ('code-de-commerce', '22'),
        ('code-de-la-securite-sociale', '2026-534'),
        ('livre-des-procedures-fiscales', '2026-692'), (CGI, '2')}
INEXISTANTS = {(CGI, '150-0 F ter')}

def _code_for(line, a_start, a_end, art):
    """Code applicable, par ordre de priorité : marqueur collé après l'article
    (« Art. 1218 C. civ. »), marqueur le plus proche avant l'article (90
    caractères), marqueur peu après (« l'article 39, 1-5° du CGI »), repli par
    préfixe."""
    best, bd = None, (9, 999)
    for rx, slug in CODES:
        for m in re.finditer(rx, line):
            gap = m.start() - a_end
            if -1 <= gap <= 2:
                d = (0, gap)
            elif m.end() <= a_start and a_start - m.end() <= 90:
                d = (1, a_start - m.end())
            elif 0 <= gap <= 15:
                d = (2, gap)
            else:
                continue
            if d < bd:
                bd, best = d, slug
    if best:
        return best
    a = art.replace(' ', '').replace('.', '').replace('*', '')
    m = re.match(r'([LRD])\*?(\d+)', a)
    if m:
        p, n = m.group(1), int(m.group(2))
        if a.startswith(('L1224', 'L2312', 'L2314')): return 'code-du-travail'
        if a.startswith(('L561', 'R561', 'L151-3', 'L211-1')): return 'code-monetaire-et-financier'
        if a.startswith('L711'): return 'code-de-la-propriete-intellectuelle'
        if a.startswith(('L64', 'L57', 'L10', 'L169', 'L176', 'L190', 'L59', 'R196', 'R57', 'R59', 'R199', 'L80')): return 'livre-des-procedures-fiscales'
        if a.startswith(('L136-', 'L244-3')): return 'code-de-la-securite-sociale'
        if p in 'LR' and (100 <= n <= 950 or a.startswith('L23-10')): return 'code-de-commerce'
    return None

def _norm(code, a):
    a = a.strip()
    if code in ('code-civil', 'code-de-commerce', 'code-de-la-consommation', 'code-du-travail', 'code-de-la-propriete-intellectuelle') and a.endswith(' C'):
        a = a[:-2]
    a = re.sub(r'^([LRD])\.?\s?(\*?)\s?(\d)', lambda m: m.group(1) + (m.group(2) if m.group(2) else '. ') + m.group(3), a)
    return re.sub(r'\s+', ' ', a)

def _files(d):
    """Un sous-dossier par skill (SKILL.md) ; à défaut, fichiers .md à plat."""
    skills = [(os.path.basename(r), os.path.join(r, 'SKILL.md')) for r, _, fs in sorted(os.walk(d)) if 'SKILL.md' in fs]
    if skills:
        yield from skills
        return
    for f in sorted(os.listdir(d)):
        if f.endswith('.md'):
            yield f[:-3], os.path.join(d, f)

def extract(d):
    refs = collections.OrderedDict()
    def add(c, a, occ):
        refs.setdefault((c, a), []).append(occ)
    for skill, path in _files(d):
        txt = open(path, encoding='utf-8').read()
        hdr = 'vérifié' in txt and re.search(r'« vérifié \d{2}/\d{2}/\d{4} »', txt)
        hdr_date = None
        if hdr:
            hdr_date = re.search(r'« vérifié (\d{2}/\d{2}/\d{4}) »', txt).group(1)
        for i, line in enumerate(txt.split('\n'), 1):
            if re.match(r'^\s*(name|description):', line):
                continue
            for m in ART.finditer(line):
                art = m.group(1).strip()
                pre = line[max(0, m.start() - 15):m.start() + 1]
                if re.fullmatch(r'\d{1,2}', art) and not re.search(r'(art\.|Art\.|article)\s*$', line[max(0, m.start() - 12):m.start() + len(m.group(0)) - len(art)]):
                    continue
                if re.fullmatch(r'\d{4}', art) and art.startswith(('19', '20')) and not re.search(r'(art\.|Art\.|C\. ?civ\.)', pre + m.group(0)):
                    continue
                code = _code_for(line, m.start(1), m.end(1), art)
                if not code:
                    continue
                a = _norm(code, art)
                if (code, a) in DROP:
                    continue
                code, a = REMAP.get((code, a), (code, a))
                v = re.search(r'vérifiée?s?\s*(?:le\s*)?\(?(\d{2}/\d{2}/\d{4})', line)
                vd = v.group(1) if v else (hdr_date if hdr_date and re.search(r'vérifiée?s?\b', line) else None)
                occ = {'skill': skill, 'ligne': i, 'verifie': vd, 'extrait': line.strip()[:160]}
                if code == CGI and a == '990' and line[m.end():m.end() + 2] == ' I':
                    a = '990 I'
                if code == CGI and a == '150':
                    for x in (['150 U', '150 VH'] if '150 U' in line else ['150 VB']):
                        add(code, x, dict(occ))
                    continue
                add(code, a, occ)
    return refs

def lj_key(art):
    return re.sub(r'\s+', '-', art.lower().replace('. ', '').replace('.', '').replace('*', '').strip())

def cmd_extract(d, out):
    refs = extract(d)
    data = [{'code': c, 'article': a, 'occurrences': o} for (c, a), o in refs.items()]
    json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(data), 'références extraites')

def _iso(d):
    return datetime.datetime.strptime(d, '%d/%m/%Y').date().isoformat()

def cmd_reconcile(idx_path, ext_path, today=None):
    idx = json.load(open(idx_path, encoding='utf-8'))
    ext = json.load(open(ext_path, encoding='utf-8'))
    cur = {(r['code'], r['article']): r for r in idx['references']}
    seen, new = set(), []
    for e in ext:
        k = (e['code'], e['article']); seen.add(k)
        occ = [{kk: vv for kk, vv in o.items() if kk != 'verifie'} for o in e['occurrences']]
        dates = [_iso(o['verifie']) for o in e['occurrences'] if o.get('verifie')]
        if k in cur:
            r = cur[k]; r['occurrences'] = occ
            if dates and (not r.get('derniere_verification') or max(dates) > r['derniere_verification']) and r['statut_verification'] != 'verifie':
                r['derniere_verification'] = max(dates); r['statut_verification'] = 'verifie'
        else:
            r = {'id': f'{k[0]}:{k[1]}', 'type': 'mention_inexistante' if k in INEXISTANTS else 'article', 'code': k[0], 'article': k[1],
                 'cle_librejustice': lj_key(k[1]), 'statut_verification': 'a_verifier', 'derniere_verification': None,
                 'etat_source': None, 'occurrences': occ}
            idx['references'].append(r); new.append(k)
    gone = [k for k in cur if k not in seen and not any(o.get('ligne') is None for o in cur[k]['occurrences'])]
    idx['references'] = [r for r in idx['references'] if (r['code'], r['article']) not in set(gone)]
    json.dump(idx, open(idx_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('Nouvelles références :', len(new)); [print('  +', c, a) for c, a in new]
    print('Références plus citées (retirées) :', len(gone)); [print('  -', c, a) for c, a in gone]

def cmd_render(idx_path, md_path):
    idx = json.load(open(idx_path, encoding='utf-8'))
    out = idx['references']
    L = ['# Index des références citées dans les skills ECA', '',
         f"Créé le {idx['date_creation']} — dernière maintenance : {idx.get('derniere_maintenance') or 'aucune'}. Tenu par `maintenance-skills` ; source de vérité : `references-index.json` (ce fichier en est la vue lisible, régénérée par `refs.py render`).", '',
         idx['regle'], '']
    nv = sum(1 for r in out if r['statut_verification'] == 'verifie')
    L += [f"**{len(out)} articles** ({nv} vérifiés, {len(out) - nv} à vérifier) · {len(idx['bofip'])} BOFiP · {len(idx['jurisprudence'])} décisions · {len(idx['textes'])} textes · {len(idx['pieges_dates_socle'])} pièges datés · {len(idx['echeances'])} échéances", '']
    L += ['## Échéances annoncées', '', '| Date | Objet | Action | Skills |', '|---|---|---|---|']
    L += [f"| {e['date']} | {e['objet']} | {e['action']} | {', '.join(e['skills'])} |" for e in idx['echeances']] + ['']
    L += ['## Articles', '', '| Code | Article | Dernière vérification | État connu | Skills |', '|---|---|---|---|---|']
    for r in sorted(out, key=lambda r: (r['code'], r['article'])):
        es = ''
        if r.get('etat_source'):
            s = r['etat_source']; es = s.get('statut', '') + (f" jusqu'au {s['version_jusqu_a']}" if s.get('version_jusqu_a') else '')
            if s.get('versions_futures'): es += ' ; version future au ' + ', '.join(v['depuis'] for v in s['versions_futures'])
        if r['type'] == 'mention_inexistante': es = 'cité comme inexistant'
        L.append(f"| {r['code']} | {r['article']} | {r.get('derniere_verification') or 'à vérifier'} | {es} | {', '.join(sorted(set(o['skill'] for o in r['occurrences'])))} |")
    L += ['', '## BOFiP', '', '| Identifiant | Skills | Dernière vérification | Note |', '|---|---|---|---|']
    L += [f"| {b['id']} | {', '.join(b['skills'])} | {b.get('derniere_verification') or 'à vérifier'} | {b.get('note', '')} |" for b in idx['bofip']]
    L += ['', '## Jurisprudence', '', '| Décision | Skills | Portée retenue | Dernière vérification | Note |', '|---|---|---|---|---|']
    L += [f"| {j['id']} | {', '.join(j['skills'])} | {j['portee_retenue']} | {j.get('derniere_verification') or 'à vérifier'} | {j.get('note', '')} |" for j in idx['jurisprudence']]
    L += ['', '## Textes', '', '| Texte | Objet | Skills | Dernière vérification |', '|---|---|---|---|']
    L += [f"| {t['id']} | {t['objet']} | {', '.join(t['skills'])} | {t.get('derniere_verification') or 'à vérifier'} |" for t in idx['textes']]
    L += ['', '## Pièges datés du socle (§ 5)', '', '| Piège | Vérifié | Sources |', '|---|---|---|']
    L += [f"| {p['piege']} | {p['verifie']} | {p['sources']} |" for p in idx['pieges_dates_socle']]
    open(md_path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('Vue régénérée :', md_path)

if __name__ == '__main__':
    c = sys.argv[1] if len(sys.argv) > 1 else ''
    if c == 'extract': cmd_extract(sys.argv[2], sys.argv[3])
    elif c == 'reconcile': cmd_reconcile(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)
    elif c == 'render': cmd_render(sys.argv[2], sys.argv[3])
    else: print(__doc__)
