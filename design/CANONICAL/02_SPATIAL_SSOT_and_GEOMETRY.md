# 02 · SPATIAL SSOT & GEOMETRY
### Sadot · Landscape Architecture · Team 110 · v0.2.0 · 2026-07-08 · **owns: Geometry** · status: **PARTIAL — plot boundary + elevations confirmed by licensed survey; hardscape layout still pending S002/S003**

> Harvested/adapted from `IsraelMicrogreens-BlenderV2-Project/CANONICAL/02_SPATIAL_SSOT_and_GEOMETRY.md`, 2026-07-08, per `HANDOFF_TO_NEXT_team_110_SADOT_BUILDOUT_2026-07-08_v1.0.0.md` §C.2. Updated 2026-07-08 with real client survey data.

Conflict law: **geometry → this doc wins**, and **the current Sadot .blend is the geometric tiebreaker** — see `blender/CURRENT_MODEL.md` for the version pointer, once a model is authored. Authoritative detail lives in `blender/data/site/SITE_GEO.yaml` (the licensed-survey extraction) until a BUILD_DATA-equivalent is created under S003 (detailed design). This doc is the locked geometric frame, once locked.

## Datum (world origin)
**Plot boundary + registry confirmed** (licensed survey `10111TD122`, מודדי עירון, signed 2023-08-22): Gush 10111,
Helka 122, Pardes Hanna, 752 sqm, 6-point ITM-compatible boundary polygon + ~40 spot elevations (visible range
54.47-57.59m). Full data: `blender/data/site/SITE_GEO.yaml`. **Still TBD:** true-north bearing (survey shows a north
arrow but no digitized bearing was extracted from the raster scan — needs a DWG/DXF version or manual measurement
before S003 set-out), and the Blender world-origin anchor object (created when the first `.blend` exists).
Reconciliation needed: the architectural IFC model (`raw-materials/from-client/NSB02.ifc`) carries its own
Revit-authored site lat/long that does not match the client-supplied WGS84 pin — flagged, not yet resolved.

## Shell & structure (site layout)
**TBD for hardscape** — no zoning/paths/hardscape layout recorded yet; awaits S002 concept design. However, real
INPUT now exists: the client's own hand-sketched concept diagrams (2 versions,
`raw-materials/from-client/WhatsApp Image 2026-07-0{6,8}*.jpeg`) show a curved pool/water feature, a winding pebble
path, a circular pergola/gazebo structure, and a lattice/planter feature. See `design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md`
for the full synthesized brief these sketches accompany.

## Existing conditions (as of 2026-07-08)
- **24 existing trees** per the survey's tree schedule (23 generic + 1 olive, olive at 6.00m height/0.35m diameter)
  — preservation/removal decisions deferred to S002, but the inventory itself is real, not placeholder.
- **House/architectural reference:** `raw-materials/from-client/NSB02.ifc` (Autodesk Revit 2023 export, IFC2X3,
  project name decodes to "ניב שדות") — the house-model basis for the site-anchored Blender build in S003.

## Model state (current — none yet)
- File: **none authored yet.** Pointer convention harvested to `blender/CURRENT_MODEL.md`; will name the live `.blend` once the site-anchored model exists (S003).
- Audit: TBD — no export/inventory artifacts exist yet (pattern to follow: microgreens `exports/ai_bridge/*_inventory.json`).
- Built & SSOT-matched: nothing yet.

---
*02 · Spatial SSOT & Geometry · v0.1.0 · 2026-07-08 · Team 110. Geometric tiebreaker = the current Sadot .blend, see `blender/CURRENT_MODEL.md` (no model authored yet). Skeleton only.*
