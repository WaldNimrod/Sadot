# CURRENT MODEL — pointer (single source of truth for "which .blend")

**LIVE = `blender/sadot_v1_initial.blend`** · *(2026-07-09 — first Sadot `.blend`, created ahead of the formal
`SDT-S003-P003-WP001` WP as an early "show what we understood" initial pass, per team_00's request. NOT a
site-anchored, concept-approved model — see caveats below before treating anything in it as final.)*

**What's in it:** real IFC-extracted house geometry (111 walls + 13 windows + 16 doors + the deck slab #51836,
via `blender/scripts/site/export_house_shell_obj.py` — collection `HouseShell_v1_PROVISIONAL`) and the real
6-point surveyed plot boundary/terrain (collection `Terrain_RealSurvey`, from `blender/data/site/terrain.obj`).
**Known limitations (read before using):**
- **Rotation is now RESOLVED (0°, rigorously confirmed 2026-07-09 — see "Origin convention" below); position
  (X/Y translation) is still an open, flagged approximation**, and Z is still approximate too (though now
  grounded in a real client-stated fact). Not the same as a surveyed tie-measurement. See
  `design/CANONICAL/BLENDER_SHELL_BUILD_PLAN_v1.0.0.md` §3/§3b.
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

**Origin convention (updated 2026-07-09, FOUR passes — read to the end, earlier passes were wrong):**
1. **First pass:** team_00 identified `walls_119777_Basic_Wall:משראביה:6071941` (a mashrabiya wall near the deck)
   in the live scene as "the south fence" and the scene was re-anchored to its corner.
2. **Second pass:** an exact rotation (θ=105.28°, computed from matching that wall to survey edge 3G→4G) was
   applied to the `terrain` object, with a tight-looking 3-9cm cross-check at the wall's other end.
3. **Third pass — CONTRADICTION found, then RESOLVED rigorously:** the client stated directly that the deck +
   glass door face roughly south. Checking pass 2's rotation against that statement showed the deck would face
   ESE (~107°) under it — not south. Rather than trust either heuristic, the question was settled by walking the
   IFC's own `IfcLocalPlacement` hierarchy directly (Project→Site→Building→all 5 storeys), via 3 independent
   methods (raw STEP data, composed-matrix decomposition, and independent PCA on the actual geometry). **Every
   containment level carries an identity rotation, to full float precision — rotation = 0.000000°.** Pass 2's
   105.28° was a bad wall-to-edge correspondence (the file has 2 distinct wall-orientation families 90° apart;
   the wrong one got matched). **The scene has been reverted to 0° rotation, translation-only** — see
   `design/CANONICAL/BLENDER_SHELL_BUILD_PLAN_v1.0.0.md` §3b and `blender/data/site/SITE_GEO.yaml` →
   `rotation_resolution` for the full derivation (`fence_edge_candidate_transform_RETRACTED` preserves pass 2 for
   the record).
   - **Bonus finding from the same investigation:** the deck sits near TWO glass doors (2.95m and 3.49m away).
     The one originally assumed to be "the" deck door (#112958, 4.2m wide) actually faces ENE — not south. A
     different, narrower door (#7639, 2.8m, on wall #2391) faces SSE (159.26°, ~21° off true south) — a much
     better match for "roughly south." Both doors/objects have been relabeled in the live scene accordingly.
   - **Remaining honest caveat:** this all rests on the IFC's declared `TrueNorth` (exactly local +Y) really
     being true geographic north — and its suspicious exactness looks like an untouched Revit default, not a
     deliberately-surveyed value. The door-#7639-faces-~south finding is the best available support that it's
     directionally correct anyway, but it's still an assumption, not an independent confirmation.
4. **Fourth pass (current) — position (X/Y), translation-only, unchanged reasoning:** with rotation confirmed at
   0°, the `terrain` object was translated (no rotation) back to a south-central placement matching Niv's own
   description, using the same logic as the original pre-heuristic v1 placement (front/back reference-corner
   midpoint at local x=-5, y=-28 relative to point 1G). **This exact position is still just a flagged
   approximation** — only the rotation is confirmed, not the position. It will move once the real
   tie-measurement (§3) or Michal's coordinates arrive.
5. **Z (vertical) — now grounded in a real fact, still approximate.** The client separately stated (2026-07-09):
   real ground on the house's north/east sides currently sits ~0.30-0.40m below the entrance floor; the south
   side is currently very low and will need fill (a design decision, not a discoverable fact — no number
   assigned). The model now places the terrain's average boundary-corner elevation ~0.35m below the entrance
   floor, rather than the earlier arbitrary equate-two-unrelated-numbers choice — still not a survey-grade tie,
   and the client separately warned the whole site was regraded since the 2023 survey, so even the boundary
   corners' old elevations may not reflect current real conditions. See `SITE_GEO.yaml` →
   `client_confirmed_height_facts`.
6. **Overall status: rotation = CONFIRMED (0°, rigorous, independent of any survey/client input). Position (X/Y)
   = still an open approximation. Z = still an open approximation, now better-grounded.** Do not present the
   rotation as still-uncertain to Niv — that part is settled. Do present the position and exact height as still
   pending.

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
