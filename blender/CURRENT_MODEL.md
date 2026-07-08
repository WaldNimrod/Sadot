# CURRENT MODEL — pointer (single source of truth for "which .blend")

**LIVE = *(none yet)*** · *(2026-07-08 — no Sadot `.blend` exists. This file is a placeholder authored ahead of the first model so the convention is in place before Stage 2 (3D Modeling) starts.)*

**First model deliverable:** the first Sadot `.blend` is created during **Stage 1 (Asset Spec) + Stage 2 (3D Modeling)** of the detailed-design work package — `SDT-S003-P003-WP001` ("Site-anchored 3D model — asset spec + build") in `_aos/roadmap.yaml`. That WP is currently `PLANNED`, blocked on `S002` concept approval + real plot survey data.

**When the first model is created:** update this file's **LIVE = ** line with the real filename, fill in the role table below, and follow the harvested geo-anchoring pipeline (`blender/lib/geo_itm.py` — WGS84 ↔ Israeli TM/EPSG:2039 — and `blender/scripts/site/site_geo_anchor.py`, `phase4_site_exterior_pass.py`, `measure_site_path.py`) to true-scale-anchor the model to the real plot.

## Role table (fill in once a model exists)

| Role | File | Notes |
|---|---|---|
| **LIVE** | *(TBD)* | Set when the first Sadot `.blend` is saved. |
| previous LIVE | *(none yet)* | — |
| **Phase-render fork (frozen)** | *(TBD, if/when a render-only fork is needed)* | Follow the microgreens precedent: `Save As` a `_render` suffixed copy before any beauty-render batch; never edit the frozen fork after that. |

**Rule (once LIVE exists):** open LIVE, `Save As` before each milestone, bump the filename (e.g. `sadot_001.blend` → `sadot_002.blend`). Never edit a frozen render fork. Keep exactly one file pointed to by **LIVE =** above at all times — this file is the single source of truth for "which `.blend` is current," matching the convention harvested from `IsraelMicrogreens-BlenderV2-Project/blender/CURRENT_MODEL.md`.

## Related (already harvested, ready to use once a model exists)

| Path | Role |
|---|---|
| `blender/lib/geo_itm.py` | Pure-Python WGS84 ↔ Israeli TM (EPSG:2039) converter |
| `blender/scripts/site/site_geo_anchor.py` | Places/updates a `SITE.geo_anchor` Empty at the engineering datum + loads WGS84 from `data/site/SITE_GEO.yaml` (that YAML does not exist yet in Sadot — author it alongside the site-analysis WP, `SDT-S001-P002-WP004`) |
| `blender/scripts/site/phase4_site_exterior_pass.py` | Site-exterior render + path-audit pass (references sibling asset/material scripts not yet harvested — see file header) |
| `blender/scripts/site/measure_site_path.py` | Footprint/equipment AABB + paver-path measurement from `matrix_basis` (object-name prefixes are the origin model's convention — re-tune to Sadot's own naming once modeling starts) |
| `blender/scripts/inspect/session_mcp_verify.py` | Blender MCP (port 9876) connectivity + sanity check — `EXPECTED_MODEL_NAME_FRAGMENT` constant set to `"sadot"`, update once the first `.blend` exists |

## Provenance

This file is a **new** authoring (not copied) for the Sadot spoke on 2026-07-08 (WP: `SDT-S001-P001-WP001`), following the same convention as `IsraelMicrogreens-BlenderV2-Project/blender/CURRENT_MODEL.md` (bold `LIVE =` pointer + role table + Save-As-before-milestone rule), adapted to state there is no live model yet rather than inventing one.
