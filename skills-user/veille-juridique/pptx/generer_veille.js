#!/usr/bin/env node
/*
 * Générateur du diaporama de la veille juridique et fiscale ECA EXPERTISE.
 * Charte : courrier en-tête ECA (logo, ardoise #495864, rouge #E63427, Raleway).
 * Aucune limite de slides : le contenu est paginé automatiquement.
 *
 * Usage : node generer_veille.js veille.json sortie.pptx
 * Dépendance : pptxgenjs (npm). Le logo logo-eca.png doit être dans le même dossier.
 *
 * Le script refuse de produire un fichier si un champ dépasse son budget de
 * caractères (le texte déborderait de son cadre) : il liste les champs à
 * raccourcir et sort avec le code 2. Raccourcir, puis relancer.
 */
"use strict";
const fs = require("fs");
const path = require("path");
let pptxgen;
try { pptxgen = require("pptxgenjs"); }
catch (e) { console.error("pptxgenjs manquant : npm install pptxgenjs"); process.exit(1); }

const [, , IN, OUT] = process.argv;
if (!IN || !OUT) { console.error("Usage : node generer_veille.js veille.json sortie.pptx"); process.exit(1); }
const data = JSON.parse(fs.readFileSync(IN, "utf8"));
const LOGO = path.join(__dirname, "logo-eca.png");
if (!fs.existsSync(LOGO)) { console.error("logo-eca.png introuvable à côté du script"); process.exit(1); }

/* ---------- Charte ---------- */
const COL = {
  ardoise: "495864",   // bleu-gris ECA (adresses, logo)
  ardoiseFonce: "2E3A44",
  rouge: "E63427",     // rouge du logo ECA
  texte: "1F2A33",
  gris: "6B7680",
  grisClair: "D5DADF",
  fond: "F2F4F6",
  teinte: "E9EDF0",
  blanc: "FFFFFF",
};
const FONT = "Raleway";
const W = 13.333, H = 7.5, MX = 0.6;

/* ---------- Budgets de caractères (au-delà, le texte déborde) ---------- */
const BUDGET = {
  titre: 100, reference: 200, avant: 340, apres: 340, concernes: 200,
  incertitudes: 200, action: 330, date_effet: 40, resume_texte: 230,
  action_ligne: 170, echeance: 40, ecarte_titre: 110, ecarte_motif: 120,
  source_libelle: 130,
};
const erreurs = [];
function check(val, key, where) {
  if (val == null) return "";
  const s = String(val).trim();
  if (s.length > BUDGET[key]) erreurs.push(`${where} › ${key} : ${s.length} caractères (max ${BUDGET[key]})`);
  return s;
}
const req = (v, where) => { if (v == null || String(v).trim() === "") erreurs.push(`${where} : champ obligatoire manquant`); return v; };

/* ---------- Validation des données ---------- */
req(data.semaine, "semaine");
const elements = (data.elements || []).map((e, i) => {
  const w = `elements[${i}]`;
  return {
    domaine: req(e.domaine, `${w} › domaine`) || "Autres",
    nature: req(e.nature, `${w} › nature`) || "",
    titre: check(req(e.titre, `${w} › titre`), "titre", w),
    reference: check(req(e.reference, `${w} › reference`), "reference", w),
    lien: e.lien || "",
    date_effet: check(e.date_effet, "date_effet", w),
    avant_label: e.avant_label || "Avant",
    apres_label: e.apres_label || "Après",
    avant: check(e.avant, "avant", w),
    apres: check(e.apres, "apres", w),
    concernes: check(e.concernes, "concernes", w),
    incertitudes: check(e.incertitudes, "incertitudes", w),
    action: check(req(e.action, `${w} › action`), "action", w),
    priorite: (e.priorite || "moyenne").toLowerCase(),
  };
});
const resume = (data.resume || []).map((r, i) => ({ domaine: r.domaine || "", texte: check(req(r.texte, `resume[${i}] › texte`), "resume_texte", `resume[${i}]`) }));
const actions = (data.actions || []).map((a, i) => ({
  action: check(req(a.action, `actions[${i}] › action`), "action_ligne", `actions[${i}]`),
  echeance: check(a.echeance || "", "echeance", `actions[${i}]`),
  priorite: (a.priorite || "moyenne").toLowerCase(),
  renvoi: a.renvoi || "",
}));
const ecartes = (data.ecartes || []).map((x, i) => ({ titre: check(x.titre, "ecarte_titre", `ecartes[${i}]`), motif: check(x.motif, "ecarte_motif", `ecartes[${i}]`) }));
const sources = (data.sources || []).map((s, i) => ({ libelle: check(req(s.libelle, `sources[${i}] › libelle`), "source_libelle", `sources[${i}]`), lien: s.lien || "" }));
if (!elements.length) erreurs.push("elements : aucun élément retenu (prévoir au moins une slide « Rien de significatif cette semaine » via un élément explicite)");

if (erreurs.length) {
  console.error("GÉNÉRATION REFUSÉE — à corriger dans le JSON :\n- " + erreurs.join("\n- "));
  process.exit(2);
}

/* ---------- Présentation ---------- */
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "ECA EXPERTISE";
pres.company = "ECA EXPERTISE";
pres.title = `Veille juridique et fiscale – semaine ${data.semaine}`;
pres.theme = { headFontFace: FONT, bodyFontFace: FONT };

const FOOTER_TXT = "ECA EXPERTISE  ·  Veille juridique et fiscale  ·  Usage interne";
pres.defineSlideMaster({
  title: "ECA_CONTENU",
  background: { color: COL.blanc },
  objects: [
    { image: { path: LOGO, x: W - MX - 1.65, y: 0.38, w: 1.65, h: 0.6 } },
    { text: { text: FOOTER_TXT, options: { x: MX, y: H - 0.5, w: 8, h: 0.3, fontFace: FONT, fontSize: 9, color: COL.gris, margin: 0 } } },
    { placeholder: { options: { name: "titre", type: "title", x: MX, y: 0.4, w: W - 2 * MX - 2.0, h: 0.95, fontFace: FONT, fontSize: 26, bold: true, color: COL.ardoise, valign: "top", align: "left", margin: 0 }, text: "" } },
  ],
  slideNumber: { x: W - MX - 0.6, y: H - 0.5, w: 0.6, h: 0.3, fontFace: FONT, fontSize: 9, color: COL.gris, align: "right" },
});
pres.defineSlideMaster({
  title: "ECA_SECTION",
  background: { color: COL.ardoise },
  objects: [
    { text: { text: FOOTER_TXT, options: { x: MX, y: H - 0.5, w: 8, h: 0.3, fontFace: FONT, fontSize: 9, color: COL.grisClair, margin: 0 } } },
    { placeholder: { options: { name: "titre", type: "title", x: MX, y: 0.9, w: 7.0, h: 2.0, fontFace: FONT, fontSize: 40, bold: true, color: COL.blanc, valign: "bottom", align: "left", margin: 0 }, text: "" } },
  ],
  slideNumber: { x: W - MX - 0.6, y: H - 0.5, w: 0.6, h: 0.3, fontFace: FONT, fontSize: 9, color: COL.grisClair, align: "right" },
});

const T = (slide, text, o) => slide.addText(text, Object.assign({ fontFace: FONT, color: COL.texte, margin: 0, isTextBox: true, valign: "top" }, o));
const box = (slide, o) => slide.addShape(pres.shapes.ROUNDED_RECTANGLE, Object.assign({ rectRadius: 0.08, line: { type: "none" } }, o));
const chunk = (arr, n) => { const out = []; for (let i = 0; i < arr.length; i += n) out.push(arr.slice(i, i + n)); return out; };

const NATURE = {
  loi: "Loi", ordonnance: "Ordonnance", decret: "Décret", "décret": "Décret", arrete: "Arrêté", "arrêté": "Arrêté",
  doctrine: "Doctrine BOFiP", bofip: "Doctrine BOFiP", jurisprudence: "Jurisprudence", ue: "Droit de l'Union", autre: "Autre",
};
const natureLabel = (n) => NATURE[String(n).toLowerCase()] || n;
const PRIO = { haute: { t: "Priorité haute", c: COL.rouge }, moyenne: { t: "Priorité moyenne", c: COL.ardoise }, basse: { t: "Priorité basse", c: COL.gris } };
const prio = (p) => PRIO[p] || PRIO.moyenne;

function chip(slide, x, y, text, fill, color) {
  const w = Math.max(1.0, 0.16 + text.length * 0.085);
  box(slide, { x, y, w, h: 0.34, fill: { color: fill }, rectRadius: 0.17 });
  T(slide, text, { x, y, w, h: 0.34, fontSize: 11, bold: true, color, align: "center", valign: "middle" });
  return x + w + 0.15;
}

/* ---------- 1. Couverture ---------- */
{
  const s = pres.addSlide();
  s.background = { color: COL.blanc };
  s.addImage({ path: LOGO, x: MX, y: 0.6, w: 3.3, h: 1.2 });
  box(s, { x: MX, y: 2.45, w: W - 2 * MX, h: 3.2, fill: { color: COL.ardoise } });
  T(s, "Veille juridique et fiscale", { x: MX + 0.6, y: 2.85, w: 10, h: 1.0, fontSize: 44, bold: true, color: COL.blanc });
  T(s, `Semaine ${data.semaine}`, { x: MX + 0.6, y: 3.95, w: 10, h: 0.6, fontSize: 24, color: COL.blanc });
  const n = elements.length;
  T(s, `${n} élément${n > 1 ? "s" : ""} retenu${n > 1 ? "s" : ""}${data.date_edition ? "  ·  édition du " + data.date_edition : ""}`,
    { x: MX + 0.6, y: 4.75, w: 10, h: 0.45, fontSize: 16, color: COL.grisClair });
  T(s, "Usage interne  ·  Droit des sociétés  ·  Fiscalité  ·  Transmission  ·  Contentieux fiscal",
    { x: MX, y: 6.05, w: W - 2 * MX, h: 0.35, fontSize: 12, color: COL.gris });
  T(s, "Cambrai  ·  Arras  ·  Valenciennes", { x: MX, y: 6.45, w: W - 2 * MX, h: 0.35, fontSize: 12, bold: true, color: COL.rouge });
}

/* ---------- 2. Résumé exécutif (paginé, 5 par slide) ---------- */
const resumePages = chunk(resume.length ? resume : elements.map((e) => ({ domaine: e.domaine, texte: e.titre })), 5);
resumePages.forEach((page, pi) => {
  const s = pres.addSlide({ masterName: "ECA_CONTENU" });
  s.addText(resumePages.length > 1 ? `Résumé exécutif (${pi + 1}/${resumePages.length})` : "Résumé exécutif", { placeholder: "titre" });
  page.forEach((r, i) => {
    const y = 1.55 + i * 1.05, num = pi * 5 + i + 1;
    box(s, { x: MX, y, w: W - 2 * MX, h: 0.9, fill: { color: i % 2 ? COL.blanc : COL.fond } });
    s.addShape(pres.shapes.OVAL, { x: MX + 0.2, y: y + 0.17, w: 0.56, h: 0.56, fill: { color: COL.ardoise }, line: { type: "none" } });
    T(s, String(num), { x: MX + 0.2, y: y + 0.17, w: 0.56, h: 0.56, fontSize: 16, bold: true, color: COL.blanc, align: "center", valign: "middle" });
    T(s, r.domaine ? r.domaine.toUpperCase() : "", { x: MX + 1.0, y: y + 0.1, w: 3.0, h: 0.7, fontSize: 11, bold: true, color: COL.rouge, valign: "middle" });
    T(s, r.texte, { x: MX + 4.1, y: y + 0.08, w: W - 2 * MX - 4.3, h: 0.74, fontSize: 14, valign: "middle" });
  });
});

/* ---------- 3. Éléments, groupés par domaine ---------- */
const domaines = [];
elements.forEach((e) => { if (!domaines.includes(e.domaine)) domaines.push(e.domaine); });
const avecSections = domaines.length > 1;

function slideElement(e, idx) {
  const s = pres.addSlide({ masterName: "ECA_CONTENU", sectionTitle: avecSections ? e.domaine : undefined });
  s.addText(e.titre, { placeholder: "titre" });
  let cx = MX;
  cx = chip(s, cx, 1.5, natureLabel(e.nature), COL.rouge, COL.blanc);
  cx = chip(s, cx, 1.5, e.domaine, COL.teinte, COL.ardoise);
  if (e.date_effet) cx = chip(s, cx, 1.5, "Effet : " + e.date_effet, COL.teinte, COL.ardoise);
  const p = prio(e.priorite);
  chip(s, cx, 1.5, p.t, COL.blanc, p.c);

  const top = 2.05, colW = 3.75, gap = 0.2;
  // Avant / Après
  [[e.avant_label, e.avant, COL.fond], [e.apres_label, e.apres, COL.teinte]].forEach(([lab, txt, fill], k) => {
    const x = MX + k * (colW + gap);
    box(s, { x, y: top, w: colW, h: 2.65, fill: { color: fill } });
    T(s, lab.toUpperCase(), { x: x + 0.2, y: top + 0.15, w: colW - 0.4, h: 0.3, fontSize: 11, bold: true, color: k ? COL.rouge : COL.ardoise });
    T(s, txt || "—", { x: x + 0.2, y: top + 0.5, w: colW - 0.4, h: 2.05, fontSize: 13 });
  });
  // Concernés / incertitudes
  const y2 = top + 2.85, wl = 2 * colW + gap;
  T(s, [
    { text: "Qui est concerné  ", options: { bold: true, color: COL.ardoise } },
    { text: e.concernes || "—", options: { breakLine: true } },
    { text: " ", options: { fontSize: 6, breakLine: true } },
    { text: "Zones d'incertitude  ", options: { bold: true, color: COL.ardoise } },
    { text: e.incertitudes || "Aucune identifiée." },
  ], { x: MX, y: y2, w: wl, h: 1.6, fontSize: 13 });

  // Colonne droite : action cabinet + référence
  const xr = MX + wl + 0.35, wr = W - MX - xr;
  box(s, { x: xr, y: top, w: wr, h: 2.65, fill: { color: COL.ardoise } });
  T(s, "ACTION CABINET", { x: xr + 0.2, y: top + 0.15, w: wr - 0.4, h: 0.3, fontSize: 11, bold: true, color: COL.blanc });
  T(s, e.action, { x: xr + 0.2, y: top + 0.5, w: wr - 0.4, h: 2.05, fontSize: 13, color: COL.blanc });
  box(s, { x: xr, y: y2, w: wr, h: 1.6, fill: { color: COL.blanc }, line: { color: COL.grisClair, width: 1 } });
  T(s, "RÉFÉRENCE", { x: xr + 0.2, y: y2 + 0.12, w: wr - 0.4, h: 0.3, fontSize: 11, bold: true, color: COL.ardoise });
  T(s, e.lien ? [{ text: e.reference, options: { hyperlink: { url: e.lien, tooltip: "Ouvrir la source officielle" }, color: COL.ardoise, underline: { style: "sng" } } }] : e.reference,
    { x: xr + 0.2, y: y2 + 0.45, w: wr - 0.4, h: 1.05, fontSize: 11 });
  s.addNotes(`${natureLabel(e.nature)} — ${e.reference}${e.lien ? "\n" + e.lien : ""}`);
}

let idx = 0;
domaines.forEach((d) => {
  const items = elements.filter((e) => e.domaine === d);
  if (avecSections) {
    pres.addSection({ title: d });
    const s = pres.addSlide({ masterName: "ECA_SECTION", sectionTitle: d });
    s.addText(d, { placeholder: "titre" });
    T(s, `${items.length} élément${items.length > 1 ? "s" : ""}`, { x: MX, y: 3.05, w: 7, h: 0.5, fontSize: 18, color: COL.grisClair });
    const liste = items.slice(0, 7).map((e, i, a) => ({ text: e.titre, options: { bullet: true, breakLine: i < a.length - 1, paraSpaceAfter: 6 } }));
    if (items.length > 7) liste.push({ text: `… et ${items.length - 7} autre(s)`, options: { bullet: true } });
    const ph = Math.min(5.4, 0.5 + liste.length * 0.78);
    box(s, { x: 8.2, y: 1.2, w: W - 8.2 - MX, h: ph, fill: { color: COL.ardoiseFonce } });
    T(s, liste, { x: 8.45, y: 1.45, w: W - 8.2 - MX - 0.5, h: ph - 0.5, fontSize: 13, color: COL.blanc });
  }
  items.forEach((e) => slideElement(e, idx++));
});

/* ---------- 4. Synthèse des actions (paginé, 6 par slide) ---------- */
if (actions.length) {
  if (avecSections) pres.addSection({ title: "Synthèse" });
  const pages = chunk(actions, 6);
  pages.forEach((page, pi) => {
    const s = pres.addSlide({ masterName: "ECA_CONTENU", sectionTitle: avecSections ? "Synthèse" : undefined });
    s.addText(pages.length > 1 ? `Actions du cabinet (${pi + 1}/${pages.length})` : "Actions du cabinet", { placeholder: "titre" });
    const head = (t) => ({ text: t, options: { bold: true, color: COL.blanc, fill: { color: COL.ardoise }, fontSize: 12 } });
    const rows = [[head("Action"), head("Échéance"), head("Priorité"), head("Élément")]];
    page.forEach((a, i) => {
      const fill = { color: i % 2 ? COL.blanc : COL.fond }, p = prio(a.priorite);
      rows.push([
        { text: a.action, options: { fill } },
        { text: a.echeance || "—", options: { fill } },
        { text: p.t.replace("Priorité ", ""), options: { fill, bold: true, color: p.c } },
        { text: a.renvoi || "—", options: { fill, color: COL.gris } },
      ]);
    });
    s.addTable(rows, { x: MX, y: 1.55, w: W - 2 * MX, colW: [7.2, 1.9, 1.3, W - 2 * MX - 10.4], fontFace: FONT, fontSize: 12, color: COL.texte, valign: "middle", margin: [0.06, 0.12, 0.06, 0.12], border: { type: "none" }, rowH: 0.62 });
  });
}

/* ---------- 5. Éléments écartés (optionnel, 9 par slide) ---------- */
if (ecartes.length) {
  const pages = chunk(ecartes, 9);
  pages.forEach((page, pi) => {
    const s = pres.addSlide({ masterName: "ECA_CONTENU", sectionTitle: avecSections ? "Synthèse" : undefined });
    s.addText(pages.length > 1 ? `Écartés cette semaine (${pi + 1}/${pages.length})` : "Écartés cette semaine", { placeholder: "titre" });
    const rows = [[{ text: "Texte ou décision", options: { bold: true, color: COL.blanc, fill: { color: COL.ardoise } } }, { text: "Motif", options: { bold: true, color: COL.blanc, fill: { color: COL.ardoise } } }]];
    page.forEach((x, i) => { const fill = { color: i % 2 ? COL.blanc : COL.fond }; rows.push([{ text: x.titre, options: { fill } }, { text: x.motif, options: { fill, color: COL.gris } }]); });
    s.addTable(rows, { x: MX, y: 1.55, w: W - 2 * MX, colW: [6.6, W - 2 * MX - 6.6], fontFace: FONT, fontSize: 12, color: COL.texte, valign: "middle", margin: [0.05, 0.12, 0.05, 0.12], border: { type: "none" }, rowH: 0.5 });
  });
}

/* ---------- 6. Sources (paginé, 10 par slide) ---------- */
const srcs = sources.length ? sources : elements.map((e) => ({ libelle: e.reference, lien: e.lien }));
const srcPages = chunk(srcs, 10);
srcPages.forEach((page, pi) => {
  const s = pres.addSlide({ masterName: "ECA_CONTENU", sectionTitle: avecSections ? "Synthèse" : undefined });
  s.addText(srcPages.length > 1 ? `Sources officielles (${pi + 1}/${srcPages.length})` : "Sources officielles", { placeholder: "titre" });
  const runs = [];
  page.forEach((x, i) => {
    const n = pi * 10 + i + 1;
    runs.push({ text: `${n}.  `, options: { bold: true, color: COL.rouge } });
    runs.push(x.lien
      ? { text: x.libelle, options: { hyperlink: { url: x.lien }, color: COL.ardoise, underline: { style: "sng" }, breakLine: i < page.length - 1 } }
      : { text: x.libelle, options: { breakLine: i < page.length - 1 } });
  });
  T(s, runs, { x: MX, y: 1.55, w: W - 2 * MX, h: 5.2, fontSize: 13, paraSpaceAfter: 8 });
});

/* ---------- Écriture + thème ---------- */
(async () => {
  await pres.writeFile({ fileName: OUT });
  try {
    const skillTheme = process.env.PPTX_APPLY_THEME;
    if (skillTheme && fs.existsSync(skillTheme)) {
      const { applyTheme } = require(skillTheme);
      await applyTheme(OUT, {
        name: "ECA EXPERTISE", headFontFace: FONT, bodyFontFace: FONT,
        colors: { dk1: COL.texte, lt1: COL.blanc, dk2: COL.ardoise, lt2: COL.fond, accent1: COL.rouge, accent2: COL.ardoise,
          accent3: COL.gris, accent4: "C00000", accent5: COL.grisClair, accent6: COL.ardoiseFonce, hlink: COL.ardoise, folHlink: COL.gris },
      });
    }
  } catch (e) { console.error("Thème non appliqué (sans incidence sur le rendu) : " + e.message); }
  console.log(`OK : ${OUT} — ${pres.slides.length} slides (${elements.length} éléments)`);
})();
