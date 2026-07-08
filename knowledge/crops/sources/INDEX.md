# Crop/Plant Source Index — Citation Only

This is a **citation index**, not a data mirror. The underlying binaries (~40 MB of
XLSX/DOCX/PDF/JPG) live in the `SmallFarmsAgents` repo and are **not copied here** —
Sadot references them read-only, in place, when a specific variety/climate lookup is
needed.

**Full path to the source directory:**
`/Users/nimrod/Documents/AOS_V5/SmallFarmsAgents/data/external_sources/`

**Full index of everything in that directory (74 files, all tiers, quality-scored):**
`/Users/nimrod/Documents/AOS_V5/SmallFarmsAgents/data/external_sources/INDEX.md`

Below are only the sources most relevant to Sadot's garden-design use case (Israeli
planting calendars, a variety encyclopedia with frost/cold-resistance data, and the
cover-crop chart). For anything else, open the full index above.

## Trust-tier context (from `SmallFarmsAgents/organic_market_agent/crop_book/source_registry.py`)

SmallFarmsAgents ranks sources on an 8-class taxonomy (highest trust first): `EX`
(team_00 expert override) → `NI` (Nimrod-Input, i.e. files/links Nimrod supplied
directly — most of the sources below are `NI`-tier) → `PR` (prescriptive / university
extension) → `WR` (AI-synthesized web research) → `OP` (operational farm records) → `MK`
(market index) → `WB` (external web databases) → `UC` (user-community). When
cross-referencing a source below, its tier indicates how much independent verification
it has already had.

## Israeli planting calendars

| Code | Path (relative to `data/external_sources/`) | What it has | Tier |
|---|---|---|---|
| **L01** | `israeli/L01_GROWORGANIC_sowing_dates_base.xlsx` | Sowing/planting per crop × season (Spring/Summer/Fall/Winter), Hebrew, 86 rows × 26 cols. Markers `S=שתילים` (transplant), `X=זרעים` (seed) | NI |
| **L03** | `israeli/L03_IDAN_winter_planning.xlsx` | Per crop/variety: planting date, germination date, harvest start/end, area, bed spacing, plants/m², total yield — winter crops, 203 rows × 19 cols, Hebrew | NI |
| **L04** | `israeli/L04_IDAN_summer_planning.xlsx` | Same structure as L03, summer crops, 150 rows × 17 cols, Hebrew | NI |
| **L36** | `israeli/L36_BUSTAN_sowing_calendar.pdf` | 1-page Israeli edible-garden calendar (גינת בוסתן) — crop × **calendar month** grid, legend `ז=זריעה` (sow), `ש=שתילה` (transplant), `ש/ז=either` | NI |

These four are the closest analogue to a "when to plant what in Israel" reference.
L36 in particular is calendar-month granularity (not season-bucket), which is the
easiest shape to translate into a garden-planning calendar for a specific site.

Companion raw-text extracts (already OCR'd/extracted, safe to read directly without
opening the binary): `data/external_sources/raw_text/israeli__L36_BUSTAN_sowing_calendar.txt`,
`data/external_sources/sample_extracts/israeli__L01_GROWORGANIC_sowing_dates_base.txt`,
`data/external_sources/sample_extracts/israeli__L03_IDAN_winter_planning.txt`,
`data/external_sources/sample_extracts/israeli__L04_IDAN_summer_planning.txt`.

## Variety encyclopedia (frost/cold-resistance, regions, flowering)

| Code | Path | What it has | Tier |
|---|---|---|---|
| **L02** | `israeli/L02_AOSNOT_variety_info.docx` | 1.3 MB Hebrew **per-crop encyclopedia**. Each entry: כללי (general), שתילה (planting), גיזום (pruning), תנאי השקיה (irrigation needs), תנאי אור (light needs), תאריך שתילה (planting date), מזיקים (pests), קצב צימוח (growth rate), **עמידות** (frost/cold resistance), **אזורים בארץ** (regions in Israel), **תאריך פריחה** (flowering date), תאריך תנובה (yield date), האבקה (pollination), שם לטיני (Latin name) | NI |

This is the single richest source for exactly the questions a perennial/fruit-tree
garden design needs answered per species: does it tolerate the local winter, does it
suit this region of Israel, and when does it flower (relevant for both aesthetics and
pollination-timing / companion placement). Raw-text extract already available at
`data/external_sources/raw_text/israeli__L02_AOSNOT_variety_info.txt` — read that
before opening the DOCX.

## Cover-crop chart

| Code | Path | What it has | Tier |
|---|---|---|---|
| **L12** | `jmf_extension/L12_cover_crop_chart.pdf` | 1-page JMF chart: **germination temperature (°F+°C), USDA hardiness zone, sowing window, inoculum, winter survival** for Clover (Crimson/Red), Common Vetch, Field Peas, Hairy Vetch, Melilot, Barley, Buckwheat, Fall Rye, Oat, Spring/Winter Wheat | PR |
| **L13** | `jmf_extension/L13_cover_crops_guide.pdf` | 7-page narrative companion to L12 — 4 main functions of cover cropping + planting periods | PR |

Relevant to Sadot for soil-building beds / green-manure strips within the garden design,
even though the primary planting palette is ornamental/fruit-tree rather than
market-vegetable. Raw-text extracts:
`data/external_sources/raw_text/jmf_extension__L12_cover_crop_chart.txt`,
`data/external_sources/raw_text/jmf_extension__L13_cover_crops_guide.txt`.

## How to consult these from Sadot

These files are **not** duplicated into this repo (by design — read-only cross-reference,
~40 MB of binaries, not Sadot's to own or version). When a specific lookup is needed:

1. Prefer the pre-extracted plain-text versions under
   `SmallFarmsAgents/data/external_sources/raw_text/` or `sample_extracts/` — no binary
   parsing required.
2. Fall back to the original binary (XLSX/DOCX/PDF) under `data/external_sources/israeli/`
   or `data/external_sources/jmf_extension/` only if the raw-text extract is insufficient.
3. Treat `SmallFarmsAgents` as **read-only** at all times — Sadot has no write mandate
   there.
4. For anything beyond the four topics above (e.g. Tend multi-year farm records, Curtis
   Stone urban-farmer charts, hydroponic guides), see the full source index:
   `/Users/nimrod/Documents/AOS_V5/SmallFarmsAgents/data/external_sources/INDEX.md`.
