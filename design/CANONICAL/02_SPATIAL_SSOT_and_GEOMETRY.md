# 02 · SPATIAL SSOT & GEOMETRY
### Sadot · Landscape Architecture · Team 110 · v0.2.0 · 2026-07-08 · **owns: Geometry** · status: **PARTIAL — plot boundary + elevations confirmed by licensed survey; hardscape layout still pending S002/S003**

> Harvested/adapted from `IsraelMicrogreens-BlenderV2-Project/CANONICAL/02_SPATIAL_SSOT_and_GEOMETRY.md`, 2026-07-08, per `HANDOFF_TO_NEXT_team_110_SADOT_BUILDOUT_2026-07-08_v1.0.0.md` §C.2. Updated 2026-07-08 with real client survey data.

Conflict law: **geometry → this doc wins**, and **the current Sadot .blend is the geometric tiebreaker** — see `blender/CURRENT_MODEL.md` for the version pointer, once a model is authored. Authoritative detail lives in `blender/data/site/SITE_GEO.yaml` (the licensed-survey extraction) until a BUILD_DATA-equivalent is created under S003 (detailed design). This doc is the locked geometric frame, once locked.

## Datum (world origin)
**Plot boundary + registry + orientation confirmed** (licensed survey `10111TD122`, מודדי עירון, signed 2023-08-22):
Gush 10111, Helka 122, Pardes Hanna, 752 sqm, 6-point ITM-compatible boundary polygon (shoelace area 751.42 sqm,
0.08% from registered — confirms coordinates read correctly) + ~40 spot elevations (visible range 54.47-57.59m).
**True-north bearing resolved 2026-07-08** — computed directly from the ITM boundary coordinates (ITM northing =
grid north by construction, convergence negligible at this scale), no manual north-arrow measurement needed: short
"width" edges run ~84°/264° (near E-W), long "depth" edges run ~353-355° (near N-S, one edge kinked ~187° — see
`blender/data/site/SITE_GEO.yaml` `orientation` for all 6 edge bearings). Cross-checked against the architectural
IFC model, which declares its own project Y-axis = true north. Full data: `blender/data/site/SITE_GEO.yaml`.
**Still TBD:** the Blender world-origin anchor object (created when the first `.blend` exists, S003) — pick a
`plus_x_bearing` for the model's local axes at that point.
**Open reconciliation:** the architectural IFC model (`raw-materials/from-client/NSB02.ifc`) carries its own
Revit-authored site lat/long that does not match the client-supplied WGS84 pin — flagged, not yet resolved (does
not affect the orientation finding above, which is independent of that specific field).

## Shell & structure (site layout)
**TBD for hardscape** — no zoning/paths/hardscape layout recorded yet; awaits S002 concept design. However, real
INPUT now exists: the client's own hand-sketched concept diagrams (2 versions,
`raw-materials/from-client/WhatsApp Image 2026-07-0{6,8}*.jpeg`) show a curved pool/water feature, a winding pebble
path, a circular pergola/gazebo structure, and a lattice/planter feature. See `design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md`
for the full synthesized brief these sketches accompany.

## ⚠ Survey validity scope (team_00, 2026-07-09)

The survey PDF (`10111TD122`) is authoritative **only for the plot boundary and elevation/topography** below — the
ground doesn't change. It is **NOT** authoritative for any building/structure it depicts (house outline, pergola,
storage shed, etc.) — those show the **OLD, previously-existing house**, since replaced. The current house
(including its real deck) now stands roughly where the survey's old storage shed was shown, and is represented
**only** in the architectural IFC model (`NSB02.ifc`), not in this survey. Never cite a survey-PDF structure label
as evidence of the current house layout — use `HOUSE_IFC_REFERENCE.md` for that. (Tree data below is NOT known to
be affected by this — trees generally aren't removed just because a house was rebuilt — but treat with the same
general caution until confirmed.)

## Existing conditions (as of 2026-07-08)
- **13 existing trees** per the survey's tree schedule (12 generic + 1 olive, olive at 6.00m height/0.35m diameter;
  item #11 does not appear in the printed schedule — numbering skips #10→#12) — full per-tree table in
  `blender/data/site/SITE_GEO.yaml`. Preservation/removal decisions deferred to S002.
- **House/architectural reference:** `raw-materials/from-client/NSB02.ifc` (Autodesk Revit 2023 export, IFC2X3,
  project name decodes to "ניב שדות") — the house-model basis for the site-anchored Blender build in S003, and
  the ONLY reliable source for the current house's layout (see scope note above — the survey PDF's building
  labels are obsolete).
  **Full extraction (real, via ifcopenshell, not text-guessing):** `design/CANONICAL/HOUSE_IFC_REFERENCE.md` — 5
  storeys, 13 windows (precise dimensions), 111 walls, 16 doors, 2 stairs (0 exterior stairs/ramps — the
  entrance-to-garden level transition is NOT in the house model, it's a landscape-design decision), 63
  materials, and a high-confidence deck candidate (IfcSlab #51836). **Critical flag: this IFC file's own
  coordinates do NOT reliably align with the real ITM survey grid** — needs an updated/as-built survey or
  specific reference measurements from the architect/client to reconcile precisely (see that doc §0.1); the old
  survey's structure positions can no longer be used as an anchoring shortcut (see scope note above).

## Model state (current — none yet)
- File: **none authored yet.** Pointer convention harvested to `blender/CURRENT_MODEL.md`; will name the live `.blend` once the site-anchored model exists (S003).
- Audit: TBD — no export/inventory artifacts exist yet (pattern to follow: microgreens `exports/ai_bridge/*_inventory.json`).
- Built & SSOT-matched: nothing yet.

---
*02 · Spatial SSOT & Geometry · v0.2.0 · 2026-07-08 · Team 110. Geometric tiebreaker = the current Sadot .blend, see `blender/CURRENT_MODEL.md` (no model authored yet). Plot boundary/elevations/tree count confirmed by survey; hardscape layout still pending.*
