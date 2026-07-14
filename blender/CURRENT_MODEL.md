# CURRENT MODEL — pointer (single source of truth for "which .blend")

**LIVE = `blender/sadot_v8_tree06_east_wall_2026-07-14.blend`** · *(2026-07-14, same session — pass 15: first
planting object (existing tree #6, real position/height/canopy from team_00's on-site observation) + the
manually-built east boundary wall's peak height corrected to real 55.83m. Save-As'd from
`sadot_v7_origin_at_sw_corner_2026-07-14.blend` (pass 14: world origin reset to the plot's SW corner
(`BOUNDARY_4G`), team_00 direct instruction). Every object
rigidly shifted by the same vector — verified zero relative drift. See pass 14 below.)*

**Roof status: NONE.** All roof geometry was built twice (flat per-storey, then real gabled/sloped) and both
attempts were rejected and deleted (pass 11-13) — team_00 asked for a different approach, not tried yet. Do
not add a roof without new direction.

*(Fuller lineage, condensed — full detail in the numbered passes below: `sadot_v6_roof_removed` (pass 13,
roof deleted) ← `sadot_v5_roof_slopes` (pass 12, roof rejected) ← `sadot_v4_roof_precision` (pass 11, roof
rejected) ← `sadot_v3_site_tie_2026-07-14` (passes 7-10: team_00's manual rotation/position correction, the
precise Z anchor, old-house reference material, wall-height fixes) ← `sadot_v3_site_tie_2026-07-13` ←
`sadot_v1_initial`. NOT a site-anchored, concept-approved model — see caveats below. Rotation/X/Y position are
LOCKED (see pass 11) but that is a different claim from "concept-approved" — S002 concept sign-off is still a
separate, not-yet-reached gate.)*

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
- **Rotation is NOT 0° — see "Origin convention" pass 8 below.** The 2026-07-09 "0°, rigorously confirmed"
  finding was real but answered a narrower question (IFC-internal placement consistency) than assumed; actual
  rotation is **exactly -105.500031°** (read directly from `rotation_euler.z` on all 268 new-house wall objects
  in the live scene, 2026-07-14 — uniform to full float precision, confirming team_00's manual value was a
  clean -105.5° input). **LOCKED 2026-07-14 (explicit team_00 instruction): rotation and X/Y position are
  correct and final — do not move, re-derive, or re-verify them further.** This is not a reversal of the
  "not yet independently re-derived" caveat that stood after pass 9 — it is team_00 closing that question
  directly. Incidentally, unrelated verification work the same day (fitting an IFC-native-to-Blender-world
  transform in order to correctly place newly-extracted IFC geometry, for the roof rebuild below) matched
  268+29=297 walls' combined point-cloud shape to the source IFC's wall geometry to sub-centimeter accuracy,
  and separately landed the independently-trusted deck-slab reference within ~25cm — a real, if incidental,
  geometric cross-check via a third method (point-cloud registration, distinct from both the original
  IFC-placement-hierarchy walk and team_00's own visual inspection) that happens to support the locked value.
  This was not requested and should not be read as "the position was re-litigated" — it is offered only as
  corroborating context. **Z is fully precise**, not approximate: deck reference = 55.97m real, south-edge
  reference = 54.5m real, difference = 1.47m exact (pass 6/10). See
  `design/CANONICAL/BLENDER_SHELL_BUILD_PLAN_v1.0.0.md` §3/§3b for the pre-pass-7 method detail (historical;
  superseded by the lock above).
- The wall export includes ALL 111 IFC walls (interior partitions + some oversized boundary/retaining-wall
  elements), not an exterior-only shell — visible in the model as wall geometry extending beyond the compact,
  recognizable house core. Pruning to true exterior-only is a later refinement.
- **ROOF: REMOVED 2026-07-14 (pass 13) — the model currently has no roof geometry at all.** Two rebuild
  attempts (pass 11: flat per-storey; pass 12: real gabled slopes + deck roof) were both tried and both
  rejected by team_00 as not working, the second time with "we'll need to find a different way" — i.e. not
  "iterate again the same way," a real open problem. The history below (real per-storey grouping, real
  IFC-derived slope magnitudes, the deck-footprint approach, the no-double-coverage logic) is kept for the
  record — some of it may still be useful raw material for whatever the different approach turns out to be —
  but none of it is currently in the scene and none of it should be presented as settled. See pass 13.
  Roofs are NOT in the source IFC — the 6 `IfcRoof` entities have no geometric `Representation` in that export
  at all (a real data gap, confirmed, not a script bug). A separate lead — 8 `IfcSlab` entities tagged
  `PredefinedType=ROOF` that DO carry geometry (a common Revit/IFC export pattern) — was checked and rejected
  2026-07-14: cross-validated against the trusted deck-slab reference, that geometry sits 10+ meters from the
  real walls (one entity is 130m away, clearly a stray/neighbor-context object); the draft-sounding family
  names ("Generic -15new 2") are consistent with unfinished/mispositioned Revit placeholders, not the
  architect's real roof design. Not used.
  **Roof rebuilt 2026-07-14 (pass 11, superseding pass 10's synthetic hull-based pieces):** real per-storey
  construction, not guessed clustering. Each new-house wall (268 objects) was matched to its true IFC
  `IfcBuildingStorey` (ground floor "0- קומת כניסה" / upper floor "יח' הורים" / "גג 6") via nearest-neighbor
  point matching against the IFC source (using the validated IFC→Blender transform above) — 268/268 matched,
  median offset 0.48m. Each storey's roof footprint is a real filled union of that storey's own wall
  footprints (grid-rasterized at 10cm + flood-filled from outside so walls act as barriers and enclosed
  room interiors become solid — NOT a convex hull, and NOT just a hollow trace of the wall lines), at that
  storey's own max wall-top height + 5cm clearance. The ground-floor piece has the upper-floor and "roof 6"
  footprints subtracted so it doesn't wrongly cap the double-height sections. Result: `ROOF_ground_floor`
  (z=5.56-5.76m), `ROOF_upper_floor` (z=8.28-8.48m), `ROOF_roof6_0`/`ROOF_roof6_1` (z=8.28-8.48m) — visually
  confirmed (front-orthographic screenshot) as two distinct height bands, and top-down confirmed to precisely
  trace real room notches/jogs rather than a smoothed outline. Replaces the old `ROOF_section_<id>` objects
  (deleted). See `COLOR_CODING_CANON_v1.0.0.md`. Color is still a placeholder, not client-confirmed. Known
  simplification: height is per-storey (matching real architectural levels), not per-room within a storey —
  interior partition walls that sit below their storey's own roof height is normal (real ceilings are flat
  per level) and not a defect.
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
   against the real site plan. LOCKED same day (see pass 11) — not open for further re-derivation.** Z = fully
   precise (55.97/54.5/1.47 exact). Front-section grading is now a real, numbered design input, not an open
   question.

10. **2026-07-14, later same day — two wall-height precision fixes (team_00 direct instruction):**
    - `walls_119777_Basic_Wall:משראביה:6071941` (south-edge wall): shifted rigidly so its bottom sits at
      EXACTLY real 54.50m (was 54.56m) — matches the `SOUTH_EDGE_REF_54_5m` anchor precisely, top moved by
      the same amount (56.06m → 56.00m), preserving the wall's own height.
    - `walls_119777_Basic_Wall:משראביה:6071941.089` (west-side wall): bottom vertices extended down to follow
      the real, interpolated ground height along the wall's length (linearly interpolated between the real
      4G elevation, 54.76m, and 5G elevation, 55.80m, by each vertex's own Y position) — bottom now varies
      54.76m→55.03m along the wall's run instead of sitting flat at 55.99m. Top vertices left completely
      unchanged (57.49m real), per instruction ("שיא הגובה של הקיר ללא שינוי").

11. **2026-07-14, next session (team_00 instructions, picking up the handoff) — rotation/position LOCKED,
    roof rebuilt for real precision, north arrow fixed:**
    - **Rotation/X/Y position explicitly LOCKED by team_00** — "הבית כבר ממוקם על המגרש נכון - זה נעול - נא
      לעדכן ולא יזוז" (the house is already correctly positioned on the plot — this is locked — update the
      docs and it must not move). Read the exact live value (-105.500031°, see the "Known limitations" bullet
      above) but did not move anything. No further re-derivation is open work.
    - **Roof rebuilt (pass 10's synthetic hull-based pieces replaced) — see the "Known limitations" roof
      bullet above for the full method.** Summary: real per-IFC-storey grouping (not guessed clustering) +
      grid-rasterized filled footprint (not a convex hull, not a hollow wall-trace) + per-storey real height,
      with the ground floor cut back where the upper floor/roof-6 continue above it. Verified both numerically
      (storey Z values) and visually (top-down: precise room-notch tracing; front-ortho: two distinct height
      bands as separate horizontal lines).
    - **North arrow: two real bugs found and fixed, both flagged by team_00 as imprecise/missing:**
      (1) the arrowhead cone's `rotation_euler.x` was `+90°`, pointing the apex south (toward the shaft)
      instead of north — sign-flipped to `-90°`, verified by transforming the apex vertex to world space
      (now north of the base, as it should be). (2) the whole containing collection (`Collection` — also
      holds the 6 `BOUNDARY_*G` markers/labels and the undocumented `AXISCHECK_*` objects) had its viewport
      visibility toggled off at the collection level, independent of any object's own hide flag — this is
      almost certainly why it read as "missing" even though the objects existed. Unhidden. Visually confirmed
      after both fixes: a clean triangle pointing at the "N" label.
    - Not investigated this pass: the 4 `AXISCHECK_house_*`/`AXISCHECK_terrain_*` objects (also in the
      now-unhidden `Collection`) — undocumented anywhere in this file, purpose unknown, left as-is.

12. **2026-07-14, same session — team_00 rejected pass 11's roof as "ממש ממש ממש לא בכיוון" (really,
    really, really off), with 4 specific gaps. Rebuilt again, this time with real slope + deck coverage:**
    - **team_00's 4 points, and what changed:**
      1. *"Every space/part needs its own roof surface"* — kept the real per-storey/per-group construction
         from pass 11 (not one blob), and added the new deck roof (below) as its own explicit piece.
      2. *"The round front deck has no roof"* — added `ROOF_deck_porch`: a new roof piece over the deck's
         own real footprint (from `DECKING_wood_front_porch`), flat, at deck-top + 2.4m — a placeholder
         pergola clearance, **not client-confirmed**, chosen only to sit clearly below the main roofline and
         above head height. No real source data pins this height or confirms it should be flat rather than
         sloped; flagged, not asserted as final.
      3. *"Not all roofs are level — some have real slope. Model accordingly"* — `ROOF_ground_floor` and
         `ROOF_upper_floor` rebuilt as real symmetric gables (ridge along each footprint's own PCA long axis,
         15° each side), replacing the flat pass-11 slabs. `ROOF_roof6_0`/`_1` rebuilt as 8° gables. Both
         angles are real, not guessed: fit (least-squares plane per element) directly from the IFC's own 8
         roof-type `IfcSlab` entities (the same ones rejected in pass 11 for being 10+ meters out of
         position) — their *absolute placement* is untrustworthy draft data, but their *local shape*
         (translation-independent) isn't, and each named roof design turned out to be a real symmetric
         paired-face gable (matching slope magnitude, opposite sign) rather than a single mispositioned
         blob. 15° matched the two `רעפים חדש2` ("tiles") elements (~62m²+~108m², real tile-roof data per
         `HOUSE_IFC_REFERENCE.md` §5: "רעפים, 5cm clay tile... ~100m²+~62m²"); 8° matched `Generic -15new 2`,
         which is independently storey-confirmed as belonging to the same `גג 6` storey as the `roof6_0`/`_1`
         walls (unlike the other roof elements, which sit in storeys with zero real walls to cross-check
         against). One tiny 7th piece (`Basic Roof:10:5857893`, ~1.5m², 29° — the non-outlier twin of the
         130m stray) wasn't matched to anything and isn't represented.
      4. *"Second floor still has no roof; no double-coverage — one roof per XY point, whichever contour it's
         inside"* — rebuilt the whole set as one unified pass instead of pairwise subtraction: explicit
         priority `roof6_0/roof6_1 > upper_floor > {ground_floor, deck_porch}`, each lower piece's mask has
         every higher piece's mask subtracted before meshing. Verified numerically: zero pairwise-overlapping
         grid cells across all 5 final masks (was 94 cells of `upper` vs `roof6` before this fix — `roof6_0`
         turned out to sit entirely inside `upper`'s raw footprint). Total roofed area 154.5m².
    - **`HOUSE_IFC_REFERENCE.md` cross-check surfaced one bug in my own earlier analysis, not in the model:**
      I had misread `IfcBuildingStorey.Elevation` as millimeters (÷1000); the file's real unit is centimeters
      (÷100 — confirmed in that doc's §0.5 and cross-checked against its own storey table). This only ever
      affected my own commentary about whether "יח' הורים" was a real second story (it is — 3.1m above the
      entrance floor, not 0.31m) — it was never used in any geometry calculation, which always used real
      measured wall/mesh Z, not the raw `Elevation` attribute.
    - Not attempted: precisely relocating each real roof element's own footprint onto its correct storey
      area (only its slope magnitude was reused) — that needs a second independent anchor for roof-to-wall
      correspondence this session didn't find; the PCA-ridge placement is a reasonable, defensible
      approximation, not a rederivation of the architect's exact design.
    - Verified visually (angled material-shaded screenshot): real ridge lines with two sloping faces on both
      gables, distinct deck cap, ground/upper/roof6/deck all visually distinguishable.

13. **2026-07-14, same session — team_00 rejected pass 12 too: "תמחקו את הגג זה לא עובד. נצטרך למצוא דרך
    אחרת" (delete the roof, it's not working. We'll need to find a different way).** All 5 pass-12 roof
    objects deleted. No diagnosis was given beyond "not working" — do not guess or invent a specific reason
    (proportions, style, a rendering issue, something about the underlying wall data, etc.) without asking;
    none of the possibilities has evidence over any other. **Current state: no roof geometry in the model at
    all.** This is now open, unsolved work, explicitly flagged by team_00 as needing a different approach
    before trying again — not a cue to immediately attempt a pass 14 with more of the same method. Two
    approaches (flat per-storey; real-slope gabled) are now ruled out. Everything else in the model (walls,
    terrain, deck, boundary markers, north arrow, the locked rotation/position) is untouched by this pass.

14. **2026-07-14, same session — world origin reset to the plot's SW corner (team_00 direct instruction):**
    "נא לאפס את מערכת הצירים הכללית כך שתהיה בדיוק בפינת המגרש - דרום מערב. שם גם צריכה להיות ה 00 של המודל
    כולו וגם של הבית" (reset the general axis system so it's exactly at the plot's corner — southwest. That's
    also where the 00 of the whole model, and of the house, needs to be).
    - **SW corner = `BOUNDARY_4G`**, per this project's own already-established convention (charter §2 point
      6: team_00 previously stated "use the SW corner as the anchor point and rotation axis"; pass 7 already
      re-origined the joined house to this same corner once). Not re-derived from the boundary coordinates —
      reused the existing, already-marked reference point.
    - **Method:** confirmed zero parented objects across the whole scene (326 total) — this makes a rigid
      whole-scene shift exact and safe: subtracting `BOUNDARY_4G`'s own location from every object's
      `location` translates each object's world position by the identical vector regardless of that object's
      own rotation (translation and rotation compose independently in the transform matrix), so no relative
      position, rotation, or shape can be altered by construction. Applied to all 326 objects.
    - **Verified three ways:** (1) `BOUNDARY_4G` now reads exactly `(0.0, 0.0, 0.0)`. (2) The distance between
      two unrelated objects (`BOUNDARY_1G` and a house wall) is bit-identical before and after
      (36.122586m both times). (3) Visually — top-down screenshot shows the world grid's origin (red/green
      axis crossing) landing exactly on the plot's SW corner point.
    - **Z is included, not just X/Y:** `BOUNDARY_4G`'s Z was already `0.0` in the pre-shift local-Z convention
      (`local_Z + 54.76 = real elevation` — see `rotation_resolution`/`deck_absolute_elevation_2026-07-13` in
      `SITE_GEO.yaml`), which independently cross-checks against 4G's own real surveyed elevation, 54.76m —
      exact match. So Z=0 at the new origin is that corner's own real ground height, not an arbitrary datum;
      the shift moved X/Y only in practice (4G's Z was already 0).
    - **One shared origin for site and house, not two** — satisfies the "also of the house" half of the
      instruction: there is no separate house-local origin to set, since every house wall object was included
      in the same uniform shift into this one coordinate system.
    - Full technical record: `blender/data/site/SITE_GEO.yaml` → `blender_datum` (updated from its prior TBD
      placeholder, which had speculated 1G or plot-centroid — superseded by this direct instruction for 4G).

15. **2026-07-14, same session — first planting object: existing tree #6 (team_00 on-site species/size
    observation, relayed via `_COMMUNICATION/team_110/MSG_team_120_TO_team_110_TREE6_SPECIES_ID_2026-07-14_v1.0.0.md`).**
    Working species ID: Neem (*Azadirachta indica*), not yet confirmed — a new species for this project. Real
    data: height 4.00m (team_00 fresh observation; survey recorded 5.00m in 2023 — height discrepancy flagged
    and kept on record, not resolved), canopy diameter 2.00m (new measurement axis; the survey's existing
    0.20m `diameter_m` is trunk diameter, not a conflict). Position extracted from the same source survey PDF
    (`raw-materials/from-client/10111TD122 (1).pdf`) that supplies `boundary_itm`: located tree #6's symbol on
    the site plan, fit a 3-point (1G/4G/3G) 2D affine transform from PDF-pixel to current Blender-world
    coordinates — **exact fit, 0.000m residual on all 3 calibration points**, independently cross-checked
    against the known 3G-4G survey edge length (fit implied 10.098m vs. surveyed 10.099m — matches). First
    fit attempt (pure rotation+uniform-scale, no reflection) failed badly (up to 10m residual) — a rendered
    top-down map requires a reflection relative to world XY (image-row-down ≠ a proper rotation of
    world-north-up), not a bug in the pixel readings; switching to a general affine model (allows reflection)
    fixed it immediately. Real base elevation (54.93m) interpolated from the terrain's own triangulated survey
    mesh at that XY (not assumed flat — found which of the terrain's 5 real triangles contains the point,
    barycentric-interpolated its Z). Built as two objects, `TREE_06_existing_neem_trunk` (0.20m diameter
    cylinder, matching the tree's own surveyed trunk diameter) + `TREE_06_existing_neem_canopy` (2.00m diameter
    icosphere, top reaching exactly 4.00m above the real base) — a new "planting" color category defined for
    this in `COLOR_CODING_CANON_v1.0.0.md` (natural trunk-brown/canopy-green, not the abstract scheme palette).
    Verified visually: sits in front of the house near the deck, matching the survey sheet's depiction.
    `SITE_GEO.yaml` `existing_trees.table` and `03_MASTER_PARTS_REGISTER.md` §G updated (tree #6 split out of
    the ×12 generic bucket, following the existing olive-tree row as template).

## Role table

| Role | File | Notes |
|---|---|---|
| **LIVE** | `blender/sadot_v8_tree06_east_wall_2026-07-14.blend` | First planting object (existing tree #6 — working-ID Neem, real position/height/canopy) + manually-built east boundary wall's peak height corrected to real 55.83m — see pass 15. World origin at the plot's SW corner (pass 14). Rotation -105.500031° (exact) + X/Y **LOCKED** by team_00. **Still no roof geometry** — see pass 13. Note: the wall object used for the new east wall (`walls_119777_Basic_Wall:...6071941`, no suffix) was previously the precisely-fixed south-edge wall — that position is no longer represented in the scene (flagged to team_00, not yet resolved). Still not site-anchored/concept-approved. |
| previous LIVE | `blender/sadot_v7_origin_at_sw_corner_2026-07-14.blend` | Superseded 2026-07-14 (same session — see pass 15). World origin reset to the plot's SW corner — see pass 14. Kept, not deleted. |
| previous LIVE | `blender/sadot_v6_roof_removed_2026-07-14.blend` | Superseded 2026-07-14 (same session — world origin reset, see pass 14). No roof geometry — team_00 rejected pass 12's roof, asked for a different approach (pass 13). Kept, not deleted. |
| previous LIVE | `blender/sadot_v5_roof_slopes_2026-07-14.blend` | Superseded 2026-07-14 (same session — team_00 rejected this pass's roof too, see pass 13). Had real gabled/sloped per-storey roof + deck roof — see pass 12. Kept, not deleted. |
| previous LIVE | `blender/sadot_v4_roof_precision_2026-07-14.blend` | Superseded 2026-07-14 (same session — team_00 rejected this pass's flat-only roof, see pass 12). Real per-storey filled roof but flat (no slope), deck excluded — see pass 11. Kept, not deleted. |
| previous LIVE | `blender/sadot_v3_site_tie_2026-07-14.blend` | Superseded 2026-07-14 (Save-As'd forward same session — same lineage, not a fork). Precise Z anchor (55.97/54.5/1.47), the now-superseded synthetic hull-based per-room roofs, old-house reference material, wall-height fixes — see passes 7-10 above. Kept, not deleted. |
| previous LIVE | `blender/sadot_v3_site_tie_2026-07-13.blend` | Superseded 2026-07-14 (Save-As'd forward once work crossed midnight — same lineage, not a fork). Real Z anchor (deck +55.97m) + X/Y placement bug fix — see pass 6 above. Kept, not deleted. |
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
