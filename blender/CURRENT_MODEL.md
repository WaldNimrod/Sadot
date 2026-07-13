# CURRENT MODEL — pointer (single source of truth for "which .blend")

**LIVE = `blender/sadot_v3_site_tie_2026-07-13.blend`** · *(2026-07-13 — a new copy made from
`sadot_v1_initial.blend` per team_00's explicit instruction to work only on a new copy. NOT a site-anchored,
concept-approved model — see caveats below before treating anything in it as final.)*

**Note on `sadot_v2_initial.blend`:** this file exists on disk (created 2026-07-10 00:45, after v1's last save)
but was **never documented or adopted as LIVE** — inspecting it (2026-07-13) found it contains an *earlier*
snapshot than v1's final state (still has the retracted `ORIGIN_fence_SW_corner` Empty, none of v1's renamed/
flagged objects). Most likely an intermediate Save-As checkpoint from the same session that got superseded
before it was ever pointed to here. Left in place (not deleted — this project's convention is to preserve, not
silently erase), but **not the lineage this file continues from** — v3 branches from v1, not v2.

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
6. **Fifth pass (2026-07-13) — real Z anchor from Michal's new site-tied sheet, PLUS a discovered-and-fixed
   placement bug.** New materials arrived from Michal (`raw-materials/from-client/שטח ובית.pdf` +
   `NSB02_v2_2026-07-13.ifc`). Full analysis: `design/CANONICAL/SITE_HOUSE_TIE_ANALYSIS_2026-07-13_v1.0.0.md`.
   Two changes made, on a new copy (`sadot_v3_site_tie_2026-07-13.blend`, branched from v1):
   - **Z re-anchored:** the deck (`IfcSlab #51836`) is labeled on Michal's sheet as "מרפסת, מפלס יח' הורים" with
     a real absolute elevation **+55.97m** — verified as genuine embedded PDF text, not a visual read, on a
     sheet independently confirmed (3 edge-length matches) to share the survey's real coordinate system. This
     replaces the earlier rougher relative estimate as the primary Z anchor.
   - **Bug found and fixed while verifying the above:** applying the new Z value initially made the house
     appear to float ~55m above the terrain. Root cause: the terrain uses a **local vertical datum**
     (confirmed empirically: `local_Z + 54.76 = real absolute elevation`, exact and consistent across all 6
     boundary points) — the new real elevation had to be converted into that same local datum
     (`55.97 − 54.76 = 1.21`) before applying it, not used as a raw world-Z value directly.
   - **Separately, verification also caught that the house's X/Y placement (inherited unchanged from v1) put
     it entirely outside the terrain's footprint** — the deck's X-range didn't overlap the plot's X-range at
     all (off by ~50m). This was a real pre-existing bug in v1, not something this pass introduced or a
     consequence of the Z fix. Corrected by rigidly shifting the whole house-shell so the deck's center lands
     at the terrain's bounding-box center — a rough re-centering, **not** a precise tie (no new X/Y number
     arrived this round; see `translation_still_open` in `SITE_GEO.yaml`). Verified visually (top-down
     viewport) after the fix: house sits within the plot outline, roughly south-central, matching the
     originally-intended qualitative description.
   - Also added to the scene: small labeled markers at all 6 real boundary corners (`BOUNDARY_1G`...`BOUNDARY_6G`,
     matching `boundary_itm`), and updated in-scene flag text (`Z_ANCHOR_DECK_5597m_design_not_asbuilt`,
     `XY_POSITION_STILL_OPEN`) replacing the old `Z_HEIGHT_NOT_VERIFIED` object.
   - IFC comparison (old `NSB02.ifc` vs new `NSB02_v2_2026-07-13.ifc`, via `ifcopenshell`): building envelope,
     deck, and site placement/rotation are **byte-identical** — the rotation=0° finding and the existing
     `house_reference_corners`/deck identification are unaffected by the new IFC export.
7. **Sixth pass (same day, 2026-07-13) — team_00 caught that pass 5's fix was NOT actually correct, on sight.**
   A screenshot showed the house clearly sitting beside/outside the terrain, contradicting pass 5's own
   numeric claims. Re-investigated properly this time (multiple independent checks, not a repeat of the same
   shortcut) and found **two real, distinct bugs**, plus one pre-existing data anomaly surfaced along the way:
   - **Bug 1 — a renamed object was silently excluded from every rigid shift.** The house-shift code filtered
     objects by name prefix (`walls_`/`doors_`/`windows_`/contains `deck51836`). One object — the south-facing
     glass door, renamed earlier this project to `דלת_זכוכית_2_8m_faces_SSE_~south_door7639` — no longer
     matched any of those patterns, so it silently sat at its original v1 location while the other 140 objects
     moved. Found by cross-referencing every object's **mesh-data name** (which survives renames) against v1's
     full object list — the one true way to reliably enumerate "every house object" regardless of what a
     human renamed it to later. Fixed by applying the same cumulative delta the other 140 already had.
   - **Bug 2 — pass 5 matched bounding-box *centers*, not true polygon containment.** The plot is a narrow,
     rotated hexagon (its own bounding box is much bigger than its real area — normal for any non-axis-aligned
     shape). Matching bbox centers can land a point inside the bbox but outside the actual polygon. Redone
     properly with a real point-in-polygon test (ray-casting against the actual 6-point boundary) and the
     polygon's true area-weighted centroid (`shoelace` formula) instead of its bbox center — confirmed by the
     test, not assumed.
   - **Data anomaly found (not a bug in this session's work — pre-existing in the IFC-derived export):** one
     door, `doors_112958` (already flagged earlier as "faces ENE, not the south one"), sits **~59.6m below**
     every other house object in Z, while every other object clusters tightly. This is not a real position —
     it's an export anomaly for this one element. Hidden from viewport/render and renamed to
     `BROKEN_EXPORT_doors_112958_glass_400x240_faces_ENE_not_south_Z_ANOMALY` so it can't be mistaken for a
     real feature; not guessed at or repositioned, since there's no real basis for a corrected value yet.
   - **Also clarified, not a bug:** computing a robust median-based "core" cluster found 121 of 141 house
     objects sit in a tight, plausible ~23×15×6.6m group (matches a real house), while 20 do not — these 20
     are existing/new block-walls named consistently with garden/boundary walls, sitting 15-32m from the core.
     This matches the *already-documented* limitation ("the wall export includes oversized boundary/retaining
     wall elements, not an exterior-only shell") — now visually distinguishable as a separate cluster in the
     viewport rather than blended confusingly into one mass. Not pruned this pass (no instruction to do so);
     just no longer silently contributing to a misleading "where is the house" read.
   - Re-centered using the **121-object core's own centroid** (not the full 141, which the 20 outliers would
     skew) onto the terrain's **true polygon centroid** (`(-56.79, -26.75)`, shoelace-computed) — verified with
     the point-in-polygon test this time, and visually confirmed from a fresh top-down screenshot: the house
     footprint (round deck included) now sits inside the plot outline, matching Michal's site sheet's general
     shape.
   - **North arrow added** (explicit team_00 request): a clear labeled arrow object east of the plot, pointing
     +Y — confirmed true/grid north per the already-established 0° rotation finding (terrain was built
     directly from real ITM Easting=X/Northing=Y with no rotation applied).
   - **Process lesson, stated plainly:** pass 5's verification (checking axis-aligned bounding-box overlap
     only) was not actually sufficient evidence of correct placement, and was reported with more confidence
     than it deserved. Any future repositioning against this non-rectangular plot **must** use a real
     point-in-polygon check (or equivalent) against the 6-point boundary, not a bounding-box comparison.
8. **Overall status: rotation = CONFIRMED (0°, rigorous, independent of any survey/client input, re-confirmed
   unchanged against the new IFC export). Z = materially improved (real absolute design elevation, +55.97m at
   the deck, from a same-datum site-tied sheet) — still a design value, not an as-built field measurement.
   Position (X/Y) = still an open approximation for the precise tie, but now verified (point-in-polygon, not
   just bbox) to sit within the real plot boundary, roughly at its centroid — closing the precise tie needs
   Michal's DWG/DXF or her stated offset (see the updated draft to her,
   `_COMMUNICATION/team_70/DRAFT_MESSAGE_TO_MICHAL_SITE_PLAN_v1.0.0.md`).** Do not present the rotation as
   still-uncertain to Niv — that part is settled. Do present the exact X/Y position as still pending; Z can be
   presented as "a real design elevation, pending as-built confirmation," a meaningfully stronger claim than
   before. One door object (`doors_112958`) is hidden pending investigation of its anomalous export data.

8. **Seventh/eighth pass (2026-07-14) — team_00 took over positioning directly, and was right to.** After the
   repeated placement issues in pass 6/7, team_00 joined the house into one object in their own live session,
   found the join left the object's origin ~492,219m from its own geometry (fixed by re-origining to the SW
   corner, 4G), then manually rotated + positioned the house and **confirmed visually correct**: the house's
   long axis now runs along the plot's long axis, matching Michal's site plan's real shape — something this
   session's own repeated computational attempts never achieved.
   - **Rotation correction: NOT 0°.** The rigorous "0°" finding (3 independent IFC placement-hierarchy methods,
     pass 3) was real but answered a narrower question than assumed: it confirmed the IFC's own internal
     consistency relative to its OWN declared TrueNorth, not that IFC-native Y actually equals real ITM
     Northing. That specific mapping was never independently checked against a trusted external reference
     until team_00's own direct verification. Actual rotation is ~-105.5°, team_00-confirmed by inspection —
     notably close to the pass-2 hypothesis (105.28°) that was retracted for a different reason (a bad
     wall-to-edge correspondence) — the ROTATION VALUE from that early attempt may have been closer to right
     all along; what was wrong was the justification, not necessarily the number.
   - **Z anchor set precisely** (team_00 instruction): deck reference point (round front deck, structural/
     pre-decking level) = **55.97m real** exactly; south-boundary-edge design reference = **54.5m real**
     exactly; difference = **1.47m exact** (verified to float precision). Finished deck surface (after +15cm
     decking) = 56.12m. **Iron rule: finished ground must never exceed 55.97m real anywhere on the property.**
   - **Grading calculation (front section, deck to south boundary):** real distance 9.00m, rise 1.47m →
     **16.3% average slope (1 in 6.1)** — steep for a uniform graded surface (comfortable walking grade is
     ~5%, ADA-ramp-equivalent 8.3%). Directly supports the already-planned kurkar/basalt terracing + rockery
     approach rather than one continuous slope. Full numbers: `blender/data/site/SITE_GEO.yaml` →
     `z_anchor_precise_2026-07-14`.
9. **Overall status (2026-07-14): rotation + X/Y position = team_00-verified correct by direct inspection
   against the real site plan (not yet independently re-derived computationally — that would be the next
   rigor step if time allows, matching this project's own "cross-check at least 2 ways" standard). Z = fully
   precise (55.97/54.5/1.47 exact). Front-section grading is now a real, numbered design input, not an open
   question.**

## Role table

| Role | File | Notes |
|---|---|---|
| **LIVE** | `blender/sadot_v3_site_tie_2026-07-13.blend` | Real Z anchor (deck +55.97m) + X/Y placement bug fix — see pass 6 above. Still not site-anchored/concept-approved. |
| previous LIVE | `blender/sadot_v1_initial.blend` | Superseded 2026-07-13 — kept, not deleted. |
| undocumented, not adopted | `blender/sadot_v2_initial.blend` | Stray intermediate snapshot, older than v1's final state — see note above. Not part of the lineage. |
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
