> **Provenance:** ADAPTED from `IsraelMicrogreens-BlenderV2-Project` `docs/ARCHITECTURAL_DRAWING_CANON/06_STANDARDS_PROJECT.md` on 2026-07-08 — Sadot `design/` canon bootstrap (WP: `SDT-S001-P001-WP001`, architectural-drawing-canon + Blender/geo pipeline harvest). Per `08_REPLICATION_GUIDE.md` §"What to author per project", this file's **paths were rewritten** to reference Sadot's own `design/CANONICAL/` and `blender/` tree instead of the microgreens repo's `_communication/team_100_engineering/…` / `IsraelMicrogreens_0NN.blend` layout. Documents marked **TBD** below do not exist yet in Sadot — author them when the corresponding WP (drawing production, first 3D model) is reached; do not invent content now.

# 06 — Project binding standards (Sadot)

This spoke's **authoritative** drawing docs. When canon and a Sadot-specific doc conflict, the most recently Nimrod-approved doc wins.

## Primary (read for every sheet) — TBD, author when Sadot enters drawing production

Sadot has no drawing-production WP open yet (current work is `S001` KB/domain-setup and `S002` concept). These documents do not exist yet — create them under `design/CANONICAL/` (or a sibling `design/drawings/` tree, to be decided when the WP opens) once Sadot reaches its own Phase-5-equivalent stage:

| Document | Path (to author) | Role |
|----------|-------------------|------|
| **Model-native standard** | `design/MODEL_NATIVE_DRAWING_STANDARD.md` | Iron rules, LOD targets, frozen paths |
| **Field execution mandate** | `design/FIELD_EXECUTION_MANDATE.md` | Contractor-grade requirement |
| **Drawing delivery standard** | `design/DRAWING_DELIVERY_STANDARD.md` | Delivery rules |
| **Sheet index** | `design/DRAWING_SHEET_INDEX.yaml` | NCS IDs, subsystems, production order |
| **Approval log** | `design/APPROVAL_LOG.md` | Nimrod gate — verbatim quotes |
| **Measurement schema** | `exports/ai_bridge/SHEET_MEASUREMENTS_SCHEMA.md` | JSON contract |

## Design dossier SSOT (this spoke's `CANONICAL/`)

Sadot's 10-doc design-dossier skeleton (harvested/authored under a sibling WP, `SDT-S001-P001-WP002`) lives at `design/CANONICAL/` and plays the role the microgreens repo's top-level `CANONICAL/` folder plays there:

| Document | Path | Role |
|----------|------|------|
| Master index / canon map | `design/CANONICAL/00_MASTER_INDEX_and_CANON_MAP.md` | Entry point to project decisions |
| Decision register + rationale | `design/CANONICAL/01_DECISION_REGISTER_and_RATIONALE.md` | Why, not just what |
| Spatial SSOT + geometry | `design/CANONICAL/02_SPATIAL_SSOT_and_GEOMETRY.md` | Site geometry source of truth |
| Master parts register | `design/CANONICAL/03_MASTER_PARTS_REGISTER.md` | Plants/hardscape/materials register |
| Systems design spec | `design/CANONICAL/04_SYSTEMS_DESIGN_SPEC.md` | Irrigation/drainage/electrical systems |
| BOQ, procurement + cost | `design/CANONICAL/05_BOQ_PROCUREMENT_and_COST.md` | Bill of quantities |
| Contractor package + open rounds | `design/CANONICAL/06_CONTRACTOR_PACKAGE_and_OPEN_ROUNDS.md` | Field-execution package + open questions |
| Drawing set + render manifest | `design/CANONICAL/07_DRAWING_SET_and_RENDER_MANIFEST.md` | Sheet/render inventory — **binds to this canon's sheet pipeline** |
| Landscape planting plan | `design/CANONICAL/08_LANDSCAPE_PLANTING_PLAN.md` | Planting plan, species, schedule |
| Construction timeline | `design/CANONICAL/09_CONSTRUCTION_TIMELINE.md` | Build sequencing |

**Note:** exact `design/CANONICAL/` filenames above mirror the harvested skeleton (`SDT-S001-P001-WP002`); confirm against the actual files in that folder if it has since diverged.

## 3D model (upstream of drawings)

| Document | Path | Role |
|----------|------|------|
| Representational LOD + datum | `blender/BUILD_DATA/01_CONVENTIONS_LOD_and_DATUM.md` (**TBD** — author at first-model WP) | **BLENDER:REP-LOD** — not `BIM-LOD___` |
| Port conventions | `blender/BUILD_DATA/02_PORT_CONVENTIONS.md` (**TBD** — only if Sadot has socketed/modular hardscape systems) | Socket alignment |
| Current model pointer | `blender/CURRENT_MODEL.md` | Live blend filename — **exists now**, states no LIVE model yet (see file) |
| Geo anchoring (WGS84 ↔ Israeli TM) | `blender/lib/geo_itm.py` | Pure-Python EPSG:2039 converter — **harvested, reusable as-is** |
| Site geo/exterior assembly scripts | `blender/scripts/site/site_geo_anchor.py`, `phase4_site_exterior_pass.py`, `measure_site_path.py` | **Harvested** — adapt object-name prefixes (`SHELL.`, `SITE_path_`, etc.) to Sadot's own model once it exists |
| MCP session connectivity check | `blender/scripts/inspect/session_mcp_verify.py` | **Adapted** — `EXPECTED_MODEL_NAME_FRAGMENT` constant must be set once Sadot's first `.blend` exists (currently `"sadot"`) |

## Vendor / shop (`BIM-LOD400` supplement)

No vendor/shop package exists yet for Sadot (no tanks/prefab hardware analogous to the microgreens reservoir). Author per-vendor specs under `design/CANONICAL/06_CONTRACTOR_PACKAGE_and_OPEN_ROUNDS.md` or a dedicated `design/VENDOR_SPECS/` folder when a first shop package is needed. Do not reuse the microgreens `TANK_PRODUCT_SPECS.md` — it is explicitly excluded (vendor-specific, per `08_REPLICATION_GUIDE.md`).

## Legacy (reference only — origin repo, not this spoke)

The microgreens legacy references (`WATER_SYSTEM_BOQ/`, `make_C4_reservoir.py`, `WP_PHASE4_RENDER/`) do not apply to Sadot at all — they were project-specific to the origin repo and were never copied here. Listed for context only; do not create equivalents unless Sadot independently needs them.

## Open questions

| Pattern | Path |
|---------|------|
| Per-sheet blockers | `design/OPEN_QUESTIONS_<sheet>.md` (**TBD** — author per sheet once drawing production opens) |
| Project tracker | `_aos/roadmap.yaml` (Sadot uses the standard AOS roadmap, not a separate `PROJECT_TRACKER.yaml`) |

## Iron rules (summary — unchanged from origin canon)

1. Primary geometry = **model extract** (not hand SVG)
2. Every dimension → JSON, vendor spec, or Nimrod quote
3. Not measurable → STOP + open question
4. Builder ≠ validator (cross-engine QA)
5. Context render = inset only

Full text: `design/MODEL_NATIVE_DRAWING_STANDARD.md` (**TBD** — author when drawing production opens; until then this canon's `03_PROCESS_WORKFLOW.md` + `05_STANDARDS_EXTERNAL.md` are binding).
