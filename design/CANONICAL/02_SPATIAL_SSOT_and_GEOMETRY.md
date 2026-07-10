# 02 · SPATIAL SSOT & GEOMETRY
### Sadot · Landscape Architecture · Team 110 · v0.4.0 · 2026-07-10 · **owns: Geometry** · status: **PARTIAL — plot boundary + elevations confirmed by licensed survey; soil + qualitative sun/shade received 2026-07-10; hardscape layout + rigorous sun-path model still pending S002/S003**

> Harvested/adapted from `IsraelMicrogreens-BlenderV2-Project/CANONICAL/02_SPATIAL_SSOT_and_GEOMETRY.md`, 2026-07-08, per `HANDOFF_TO_NEXT_team_110_SADOT_BUILDOUT_2026-07-08_v1.0.0.md` §C.2. Updated 2026-07-08 with real client survey data; updated 2026-07-10 with real soil/grade + qualitative sun-shade information.

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
not affect the orientation finding above, which is independent of that specific field). Since both the survey's ITM
grid and the IFC's own declared true-north are independently self-consistent, only a **translation** (not rotation)
is needed — resolved via a 2-corner tie-measurement plan: 2 real house corners identified directly from IFC geometry
(`blender/data/site/SITE_GEO.yaml` → `house_reference_corners`), 4 real-world distance measurements needed to fix
the offset. Full plan + build sequence: `design/CANONICAL/BLENDER_SHELL_BUILD_PLAN_v1.0.0.md` §3. A parallel channel
(asking architect Michal directly for the equivalent Revit measurements) is also in flight — see
`_COMMUNICATION/team_70/DRAFT_MESSAGE_TO_MICHAL_SITE_PLAN_v1.0.0.md`. Neither has returned results yet.

## Shell & structure (site layout)
**TBD for hardscape** — no zoning/paths/hardscape layout recorded yet; awaits S002 concept design. Real INPUT exists
though: the client's own hand-sketched concept diagram. Full confidence-tiered analysis (not restated here — do not
duplicate): `design/CANONICAL/CONCEPT_SKETCH_REFERENCE.md`.

## ⚠ Survey validity scope (team_00, 2026-07-09)

The survey PDF (`10111TD122`) is authoritative **only for the plot boundary and elevation/topography** below — the
ground doesn't change. It is **NOT** authoritative for any building/structure it depicts (house outline, pergola,
storage shed, etc.) — those show the **OLD, previously-existing house**, since replaced. The current house
(including its real deck) now stands roughly where the survey's old storage shed was shown, and is represented
**only** in the architectural IFC model (`NSB02.ifc`), not in this survey. Never cite a survey-PDF structure label
as evidence of the current house layout — use `HOUSE_IFC_REFERENCE.md` for that. (Tree data below is NOT known to
be affected by this — trees generally aren't removed just because a house was rebuilt — but treat with the same
general caution until confirmed.)

## Existing conditions (as of 2026-07-08, soil/sun-shade added 2026-07-10)
- **13 existing trees** per the survey's tree schedule (12 generic + 1 olive, olive at 6.00m height/0.35m diameter;
  item #11 does not appear in the printed schedule — numbering skips #10→#12) — full per-tree table in
  `blender/data/site/SITE_GEO.yaml`. Preservation/removal decisions deferred to S002.
- **Soil + current grade (team_00, 2026-07-10, qualitative — not a lab test):** hamra mixed with construction
  debris essentially everywhere; most of the yard sits below final target grade (hamra fill planned); the
  narrow east-side path (house-to-long-fence) is already at good grade but equally debris-laden. Real
  engineering implication for any excavation (pool, banana circle, footings) — expect rubble, not clean soil.
- **Sun/shade (team_00, 2026-07-10, qualitative):** near-full sun most of the day across almost the whole
  garden; west neighbor (Tasi) casts some afternoon shade; the western fence line (house-adjacent) shades
  mainly in winter; the north/back yard is shaded most of the day. A rigorous multi-date/multi-hour sun-path
  model is still needed and is flagged **critical for S002** — sequenced after the real geographic position
  (tie-measurement) resolves. Full detail, not restated here: `blender/data/site/SITE_GEO.yaml` →
  `soil_and_grade` / `sun_and_shade` / `sun_shade_modeling_still_needed`.
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

## Model state (current — provisional v1, not yet site-anchored)
- File: `blender/sadot_v1_initial.blend` — a deliberately provisional "show what we understood" pass (real IFC
  house geometry + real surveyed boundary), NOT the site-anchored S003 deliverable. Full state, caveats, and
  the 4-pass rotation-resolution history: `blender/CURRENT_MODEL.md` (not restated here).
- Audit: TBD — no export/inventory artifacts exist yet (pattern to follow: microgreens `exports/ai_bridge/*_inventory.json`).
- Built & SSOT-matched: rotation confirmed (0°); X/Y position and exact Z remain open approximations.

---
*02 · Spatial SSOT & Geometry · v0.4.0 · 2026-07-10 · Team 110. Geometric tiebreaker = the current Sadot .blend, see `blender/CURRENT_MODEL.md` (provisional v1 exists, not yet site-anchored). Plot boundary/elevations/tree count/orientation confirmed by survey; soil + qualitative sun/shade received; house reference corners identified pending tie-measurement; hardscape layout + rigorous sun-path model still pending.*
