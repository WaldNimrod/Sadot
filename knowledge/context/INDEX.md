# knowledge/context/INDEX.md — Sadot Domain Knowledge Orientation

**Authority:** team_110 (Domain Architect) · **Created:** 2026-07-08 · **Status:** ACTIVE
**Pattern:** mirrors `IsraelMicrogreens-BlenderV2-Project/data/context/INDEX.md` (reading-order-by-task +
files-in-folder + what-is-NOT-here + key-facts quick-ref).

## Reading Order by Task Type

| Task type | Read first | Read next |
|---|---|---|
| Onboarding (any new agent/team) | This file | `_aos/context/PROJECT_CONTEXT.md`, `_aos/context/TRAINING_PLAN.md` |
| Plant selection / planting plan | `knowledge/crops/PLANT_SELECTION_STARTER.md` | `knowledge/crops/SCHEMA_REFERENCE.md`, `knowledge/climate/ISRAELI_CLIMATE_SOIL_PARDES_HANNA.md` |
| Permaculture / ecological design | `knowledge/permaculture/00_INDEX.md` | `01_ZONES_AND_SECTORS.md` → `02_GUILDS_AND_PLANTING_STRATEGY.md` → `03_WATER_AND_SWALES.md` |
| Climate/soil context | `knowledge/climate/ISRAELI_CLIMATE_SOIL_PARDES_HANNA.md` | `knowledge/permaculture/03_WATER_AND_SWALES.md` (irrigation/dry-summer design) |
| Architectural drawing production | `design/ARCHITECTURAL_DRAWING_CANON/00_ENTRY_POINT.md` | `design/CANONICAL/00_MASTER_INDEX_and_CANON_MAP.md` |
| 3D model / Blender pipeline | `blender/CURRENT_MODEL.md` | `blender/lib/geo_itm.py`, `blender/scripts/site/`, `design/CANONICAL/HOUSE_IFC_REFERENCE.md` |
| Client-hub work | `hub/README.md` | `hub/data/*.json` |
| Domain authority / credentials | `knowledge/permaculture/04_CREDENTIALS_AND_PRECEDENT.md` | `nimrod-book/chapters/11_ERA_GARDEN_2013_2023.md` (source repo, read-only) |

## Files in This Folder (and siblings under `knowledge/`)

| File | Content | Size |
|---|---|---|
| `context/INDEX.md` | This file | ~2KB |
| `climate/ISRAELI_CLIMATE_SOIL_PARDES_HANNA.md` | Regional (non-plot) climate + soil research | ~4KB |
| `crops/SCHEMA_REFERENCE.md` | Harvested crop/climate KB schema reference | — |
| `crops/PLANT_SELECTION_STARTER.md` | 10-15 species general climate-fit shortlist | — |
| `crops/sources/INDEX.md` | Citation index into SmallFarmsAgents `data/external_sources/` (not copied) | ~6KB |
| `permaculture/00_INDEX.md` | Permaculture subfolder index | — |
| `permaculture/01_ZONES_AND_SECTORS.md` | Zone/sector design theory + small-plot adaptation | — |
| `permaculture/02_GUILDS_AND_PLANTING_STRATEGY.md` | Guild concept + crop-KB interface | — |
| `permaculture/03_WATER_AND_SWALES.md` | Water-harvesting/swale basics for dry-summer Israeli gardens | — |
| `permaculture/04_CREDENTIALS_AND_PRECEDENT.md` | Nimrod's cited real credentials (PDC 2014, Havat Adam, biochar) | — |

## What Is NOT Here (by design)

| Topic | Where it actually lives |
|---|---|
| Plot-specific site survey (topography, sun/shade, drainage, soil test) | `raw-materials/from-client/` — **received 2026-07-08** (boundary, elevations, 13-tree inventory); soil test + true-north bearing still pending, curated into `blender/data/site/SITE_GEO.yaml` |
| Design decisions, spatial SSOT, BOQ, contractor package | `design/CANONICAL/` (the dossier front door — "register drives the model") |
| Architectural drawing production standards | `design/ARCHITECTURAL_DRAWING_CANON/` |
| 3D model file + geo-anchoring scripts | `blender/` |
| Client-facing hub content | `hub/` |
| Raw (un-curated) client exchange | `raw-materials/` (git-ignored — see `_aos/context/RAW_MATERIALS.md`) |
| WP/roadmap state | `_aos/roadmap.yaml`, `_aos/work_packages/S001/LOD300_milestone.md` |
| Team specialization / activation | `_aos/teams.yaml`, `_aos/context/ACTIVATION_*.md` |
| The raw ~40MB Israeli planting-calendar/variety-encyclopedia source binaries | `SmallFarmsAgents/data/external_sources/` (cited in `crops/sources/INDEX.md`, not duplicated here) |

## Key Facts (Quick Reference)

```
Client:            Niv Sadot — private house, Pardes Hanna
Domain:            landscape_architecture (lifecycle_archetype: 3D_CREATIVE → LANDSCAPE_DESIGN pending GCR)
Climate:           Köppen Csa (hot-summer Mediterranean); ~500-650mm/yr rain, Oct-Apr; dry rainless summer
Regional soil:     "Hamra" — reddish sandy clay loam over kurkar sandstone (regional prior, NOT plot-confirmed)
Plot survey:       RECEIVED 2026-07-08 (licensed survey + IFC model + sketches + voice brief) — see
                   blender/data/site/SITE_GEO.yaml + design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md.
                   Still open: formal soil lab test, digitized true-north bearing.
Harvest sources:   IsraelMicrogreens-BlenderV2-Project (drawing canon+geo+Blender), SmallFarmsAgents (crop KB),
                   EyalAmit.co.il-2026 (hub pattern), nimrod-book (permaculture credentials)
Permaculture KB:   authored from scratch 2026-07-08 — no prior structured source existed
```
