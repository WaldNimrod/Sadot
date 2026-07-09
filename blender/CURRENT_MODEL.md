# CURRENT MODEL — pointer (single source of truth for "which .blend")

**LIVE = `blender/sadot_v1_initial.blend`** · *(2026-07-09 — first Sadot `.blend`, created ahead of the formal
`SDT-S003-P003-WP001` WP as an early "show what we understood" initial pass, per team_00's request. NOT a
site-anchored, concept-approved model — see caveats below before treating anything in it as final.)*

**What's in it:** real IFC-extracted house geometry (111 walls + 13 windows + 16 doors + the deck slab #51836,
via `blender/scripts/site/export_house_shell_obj.py` — collection `HouseShell_v1_PROVISIONAL`) and the real
6-point surveyed plot boundary/terrain (collection `Terrain_RealSurvey`, from `blender/data/site/terrain.obj`).
**Known limitations (read before using):**
- The house's placement within the plot now uses a **mathematically-derived candidate transform** (rotation +
  translation, see "Origin convention" below) rather than the earlier translation-only guess — but it still rests
  on an **unconfirmed hypothesis** (that a specific wall really is the real south fence). Not the same as a
  surveyed tie-measurement. See `design/CANONICAL/BLENDER_SHELL_BUILD_PLAN_v1.0.0.md` §3-5.
- The wall export includes ALL 111 IFC walls (interior partitions + some oversized boundary/retaining-wall
  elements), not an exterior-only shell — visible in the model as wall geometry extending beyond the compact,
  recognizable house core. Pruning to true exterior-only is a later refinement.
- Roofs are NOT included — the 6 `IfcRoof` entities have no geometric `Representation` in this IFC export at all
  (a real data gap, confirmed, not a script bug).
- Per-corner terrain elevations are approximate (read from the nearest visually-adjacent spot-height label on the
  survey, not the surveyor's own formal point-elevation list — see `SITE_GEO.yaml` `approximate_corner_elevations_v1`).

**Next real model deliverable:** the site-anchored, concept-approved model is still `SDT-S003-P003-WP001` in
`_aos/roadmap.yaml` (currently `PLANNED`, blocked on `S002` concept approval + the real tie-measurement) — this
v1 file is a precursor/sanity-check, not that deliverable.

**Origin convention (updated 2026-07-09, three passes):**
1. **First pass:** team_00 identified `walls_119777_Basic_Wall:משראביה:6071941` (a mashrabiya lattice-screen wall
   near the deck) in the live scene as "the south fence." The whole scene (house + terrain) was re-anchored so
   this wall's south end, outer face, ground-level corner sits at local `(0,0,0)` — marked by an Empty named
   `ORIGIN_fence_SW_corner`. This exact corner choice was a first guess (the wall isn't axis-aligned, so
   "southwest corner" didn't pick out one unambiguous vertex).
2. **Second pass — precise math, not eyeballing:** team_00 manually rotated the `terrain` object in the live
   scene to roughly align it with the house; this was then **replaced with an exact computed transform**, not
   left as the manual eyeball: the fence wall's own fixed direction (north-end→south-end) was compared against
   the terrain's own local direction for real survey edge 3G→4G. Result: **rotation θ = 105.28° (CCW about Z)**,
   applied to the `terrain` object (not the house, which stays fixed), plus a translation placing the terrain's
   own 4G point exactly at the wall's south end `(0,0,0)`. Team_00's manual eyeball rotation (~103.6°) was only
   ~1.7° off the computed value — strong independent corroboration this is the right general alignment.
   **Cross-check:** after applying this transform, the terrain's own 3G point lands within **3-9cm** of the
   fence wall's *other* (north) end — an extremely tight match if this is coincidence, and strong (though still
   not independently confirmed) support that `walls_119777` really is the physical fence at real edge 3G→4G.
   Full numeric derivation: `blender/data/site/SITE_GEO.yaml` → `fence_edge_candidate_transform`.
3. **Status: strong candidate, not a confirmed site anchor.** It depends entirely on the wall-is-that-real-edge
   hypothesis, which hasn't been checked against the architect's plan or the client's own knowledge of the site.
   Treat as the current best working transform, supersedable the moment the real tie-measurement (or Michal's
   coordinates) arrives — do not present this rotation to Niv as a settled fact.

## Role table

| Role | File | Notes |
|---|---|---|
| **LIVE** | `blender/sadot_v1_initial.blend` | Initial/provisional — see caveats above. |
| previous LIVE | *(none — this is the first model)* | — |
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
