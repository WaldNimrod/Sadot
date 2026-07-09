# 00 · MASTER INDEX & CANON MAP — Sadot (Landscape Architecture · Pardes Hanna)
### The single internal front door. Read this first. · Team 110 · v0.3.0 · 2026-07-09 · **PARTIAL**

> Harvested/adapted from `IsraelMicrogreens-BlenderV2-Project/CANONICAL/00_MASTER_INDEX_and_CANON_MAP.md`, 2026-07-08, per `HANDOFF_TO_NEXT_team_110_SADOT_BUILDOUT_2026-07-08_v1.0.0.md` §C.2 (design-dossier SSOT skeleton harvest). Refreshed 2026-07-09 — the previous pass (v0.1.0) was never updated when real geometry/brief/sketch content landed the same day it was written; this pass reconciles the header/status framing with the canon-map table below, which was already current.

This package (`design/CANONICAL/`) is the **one front door** over the project's living SSOTs. It does **not** replace them — it declares **which document owns which decision**, records the **supersession ledger**, and lists the **open items**. The living SSOTs stay where they are (bound by relative paths + git + BlenderMCP, once authored); `CANONICAL/` *points* to them.

**Status: PARTIAL.** Site geometry (plot boundary, elevation, orientation, existing trees) is confirmed via licensed
survey — see 02. The current house structure (storeys/windows/walls/doors/deck) is extracted from the architect's IFC
— see HOUSE_IFC_REFERENCE. The client's voice-note brief is drafted and largely reconciled — see CLIENT_BRIEF. A
client-confirmation sketch exists — see 07. Hardscape layout, parts register, systems specs, BOQ, and construction
drawings remain **TBD**, pending S002 (concept)/S003 (detailed design). Do not treat any TBD placeholder below as a
decision.

## The living SSOTs (authoritative detail lives here — once authored)
| SSOT | Path | Owns |
|---|---|---|
| **Engineering / systems** | TBD — no systems SSOT authored yet; will land under `_COMMUNICATION/team_110/` or a future `design/SYSTEMS/` once S003 opens | hardscape · irrigation · drainage · electrical/lighting · contractor package · BOQ |
| **Site datum (boundary/elevation/orientation)** | `blender/data/site/SITE_GEO.yaml` — **PARTIAL, confirmed by licensed survey** | plot boundary · elevation · orientation · existing-tree inventory · house reference corners |
| **Hardscape / planting beds / parts kit** | TBD — awaits S003 detailed design (no BUILD_DATA-equivalent exists yet) | hardscape layout · planting beds · the parts (plants + materials) kit |
| **Client requirements (interim, pre-S002)** | `design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md` | privacy/neighbors · plants · pool · storage · low-maintenance · materials · safety; §9 is the single open-items checklist gating S002 |
| **Live 3D model** | `blender/CURRENT_MODEL.md` (pointer convention harvested; no `.blend` authored yet — see `blender/` once seeded) | the geometry; driven up to the register, never the reverse |
| **Client hub (external face)** | `hub/` (sadot-* clone of the CLIENT_HUB_STANDARD, per team_120 harvest) | client-facing status; a derived VIEW over this canon |

## The worlds → owning document (CANON MAP)
| World | Owner doc | Source SSOT distilled |
|---|---|---|
| Navigation / "which doc?" | **00** (this) | — |
| Decisions & rationale | **01_DECISION_REGISTER** | TBD — no decisions recorded yet; first entries expected from S002 client-brief reconciliation |
| Client requirements / voice-note brief | **design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md** | Privacy/neighbors, plants, pool, storage, low-maintenance, materials, safety — the interim input SSOT until 01/08 are populated at S002/S003 |
| Spatial / geometry | **02_SPATIAL_SSOT** | PARTIAL — plot boundary/elevation/orientation confirmed (survey) + house structure/windows/materials confirmed (IFC, see **HOUSE_IFC_REFERENCE**); hardscape layout awaits S002 concept |
| House model ground truth | **HOUSE_IFC_REFERENCE** | Real ifcopenshell extraction of the architect's IFC — storeys, windows, walls, doors, stairs, materials; flags a coordinate-reconciliation gap vs. the real ITM survey; site-anchoring/tie-measurement plan: **BLENDER_SHELL_BUILD_PLAN** |
| Blender shell-build method | **BLENDER_SHELL_BUILD_PLAN** | House-shell construction plan derived from the IFC extraction; the 2 real reference corners used for site tie-measurement (exact coordinates owned by `SITE_GEO.yaml`) |
| Client concept sketch interpretation | **CONCEPT_SKETCH_REFERENCE** | Analysis of the client's own hand-drawn garden sketch — confidence-tiered, cross-verified by 2 independent reads |
| Domain knowledge (climate/soil/permaculture/crops) | **knowledge/context/INDEX.md** (routing only) + the specific `knowledge/<folder>` file it names | General regional/methodology knowledge only — never restate site-status or client-brief facts; those are owned by 02/CLIENT_BRIEF respectively |
| Parts (plants + materials) | **03_MASTER_PARTS_REGISTER** | TBD — awaits S003 detailed design |
| Systems design (specs) | **04_SYSTEMS_DESIGN_SPEC** | TBD — awaits S003 (irrigation / hardscape / lighting specs) |
| Procurement / cost | **05_BOQ_PROCUREMENT_and_COST** | TBD — awaits S004 (design dossier + BOQ + client submissions) |
| Contractor / open rounds | **06_CONTRACTOR_PACKAGE_and_OPEN_ROUNDS** | TBD — awaits S004 |
| Drawings / renders | **07_DRAWING_SET_and_RENDER_MANIFEST** | PARTIAL — client-confirmation sketch exists (`SITE_UNDERSTANDING_SKETCH_v1.0.0.svg`, `CONCEPT_SKETCH_INTERPRETATION_v1.0.0.svg`); construction drawing set still awaits S003 |
| Landscape / planting | **08_LANDSCAPE_PLANTING_PLAN** | PARTIAL — client plant preferences + existing-tree inventory received; plant-selection engine (`knowledge/`) + full S003 layout still TBD |
| Schedule | **09_CONSTRUCTION_TIMELINE** | TBD — no committed dates yet; real dates only, no invented placeholders (per portal "no invented dates" convention) |

## Conflict law (when documents disagree)
- **Parts** → **03** wins. **Decisions** → **01** wins. **Geometry** → **02** wins (the model is the geometric tiebreaker). **"Which doc?"** → **00** wins.
- **Domain knowledge** (climate/soil/permaculture/crops) is never itself a tiebreaker for a live project fact — `knowledge/` may state general/regional knowledge, but site-status, survey, and client-brief facts always defer to 02 / CLIENT_BRIEF respectively; `knowledge/` should point, not restate.
- **Recency rule:** the most-current dated decision supersedes older ones, regardless of which file it sits in. Supersessions are logged below.
- **The register drives the model, never the reverse.**

## Status legend
`LOCKED` decided, build as-is · `WORKING` current best, may refine · `PROVISIONAL` depends on an open input · `EXISTING` already on site / in model — match. **None of these apply yet** — every entry in this skeleton is `TBD` until S002/S003 populate it.

## SUPERSESSION LEDGER
*(empty — no decisions have been superseded yet; this table activates the first time a dated decision in `01_DECISION_REGISTER` is revised)*

| # | Topic | SUPERSEDED | CURRENT TRUTH | Where written back |
|---|---|---|---|---|
| — | — | — | — | — |

## OPEN ITEMS REGISTER (consolidated — gates the work)
- **Site survey / client brief** — RECEIVED 2026-07-08 (survey PDF + IFC + hand sketches + voice notes), curated into
  02 + `CLIENT_BRIEF_NIV_SADOT_v1.0.0.md`. Remaining sub-items tracked in CLIENT_BRIEF §9 (Adas identity, ornamental-pond
  decision, boundary targeting, reference photos, sketch confirmation) — not a project-level blocker anymore.
- **Concept design (S002)** — first real decisions land in 01; first geometry in 02.
- **Detailed design (S003)** — planting plan (08), hardscape + systems specs (04), parts register (03), site-anchored 3D model (02 / `blender/`).
- **Design dossier + BOQ + client submissions (S004)** — populates 05/06/07.
- **`LANDSCAPE_DESIGN` archetype** — proposed to team_100 (inherits `3D_CREATIVE`); `roadmap.yaml` still carries `3D_CREATIVE` as base until sanctioned.
- **Outbound drafts awaiting send** — `_COMMUNICATION/team_70/DRAFT_WHATSAPP_TO_NIV_CLARIFICATIONS_v1.0.0.md` (to Niv,
  internal revision 1.2 per its own frontmatter) and `DRAFT_MESSAGE_TO_MICHAL_SITE_PLAN_v1.0.0.md` (to architect
  Michal, internal revision 1.1) — reviewed, not yet sent.
- **Governance proposals awaiting team_100/team_00 action** —
  `_COMMUNICATION/team_100/DOMAIN_PROTOCOL_PROPOSAL_SADOT_DOMAIN_RULES_v1.0.0.md` and
  `GOVERNANCE_CHANGE_REQUEST_LANDSCAPE_DESIGN_ARCHETYPE_INHERITANCE_v1.0.0.md`.
- **On-site tie-measurement** — 4 distances needed to reconcile the IFC house model against the real ITM survey grid
  (`BLENDER_SHELL_BUILD_PLAN_v1.0.0.md` §3); a parallel ask to architect Michal is also in flight (see drafts above).

---
*00 · Master Index & Canon Map · v0.3.0 · 2026-07-09 · Team 110. Front door over the living SSOTs; conflict law governs; site geometry + client brief + house-IFC extraction are real and PARTIAL, everything else remains TBD until S002/S003.*
