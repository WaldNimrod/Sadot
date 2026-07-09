# BLENDER HOUSE-SHELL BUILD PLAN
### Sadot · Landscape Architecture · Team 110 · v1.3.0 · 2026-07-09 · **owns: house-shell construction approach for S003** · status: **v1 MODEL BUILT — a strong candidate site-anchor now exists (§3b), not yet an independently-confirmed one**

> **v1.3.0 (2026-07-09):** a candidate site-anchor was found by a DIFFERENT method than §3's tie-measurement plan
> — team_00 identified a mashrabiya wall in the live model as the real south fence; the exact rotation+translation
> that aligns it with survey edge 3G→4G was computed (not eyeballed) and matches within centimeters at the far
> end. See new §3b. This doesn't replace §3's plan (still the more rigorous path once real measurements exist) but
> is now the model's actual working transform. Full derivation: `blender/data/site/SITE_GEO.yaml` →
> `fence_edge_candidate_transform`; full status: `blender/CURRENT_MODEL.md`.

> **v1.2.0 (2026-07-09):** first Sadot `.blend` built — `blender/sadot_v1_initial.blend` (see
> `blender/CURRENT_MODEL.md` for the full pointer + caveats). This executed §2/§4 below with one simplification
> (all 111 walls exported, not just the exterior perimeter — see §2) and one open item unchanged (§3's
> tie-measurement still hasn't happened, so placement in §4 step 5 is a flagged approximation, not a site anchor).

> **v1.1.0 (2026-07-09):** dedupe pass — coordinate tables (reference corners, boundary points) now point to
> `blender/data/site/SITE_GEO.yaml` instead of duplicating the numbers; deck status corrected from "CONFIRMED" to
> "high-confidence candidate" to match `HOUSE_IFC_REFERENCE.md` §4's own status; balcony finding consolidated into
> `HOUSE_IFC_REFERENCE.md` §4b; noted the parallel Michal-inquiry channel in §3/§5.

## 1. Scope

Build the house as an **exterior envelope/shell ONLY** in Blender — no interior partitions, no interior
furniture/fixtures, no MEP (electrical/plumbing). Included:
- Exterior walls (silhouette/footprint), extruded to real per-storey height.
- Roof (real geometry from the 6 `IfcRoof` entities, excluding the 1 stray fragment already identified).
- All 13 windows, as openings cut into the shell at their exact real positions/dimensions (simple glazing plane,
  not full frame/hardware detail — this is a landscape-context model, not a construction submittal).
- Exterior doors (16 total, all included as openings; the 4.2m double-leaf glass door near the deck is the most
  visually important one).
- All balcony/deck/terrace elements ("מרפסות"), per current confidence:
  - **Front deck — HIGH-CONFIDENCE CANDIDATE, ready to model pending visual sign-off:** `IfcSlab #51836`, genuine
    multi-arc round edge, real geometry already extracted (see `HOUSE_IFC_REFERENCE.md` §4). Not yet visually
    confirmed against the architect's 2D plan — build it, but don't treat it as immune to correction.
  - **Parents' 2nd-floor balcony + children's balconies (back)** — geometric search results (protruding-slab
    method): see `HOUSE_IFC_REFERENCE.md` §4b (canonical location for this finding; not restated here).

## 2. Method — extract-and-rebuild via ifcopenshell, not a full Bonsai import

**Recommendation: do NOT do a full Bonsai IFC import as the primary path**, even once Bonsai is installed. A full
import brings in everything (202 electrical fixtures, all 111 walls including interior partitions, furniture,
etc.) which then needs manual deletion to reach a "shell only" result — slow and error-prone.

**Preferred approach:** a standalone Python script (outside Blender, using the already-installed
`ifcopenshell` at `/Library/Developer/CommandLineTools/usr/bin/python3`) that:
1. Extracts the exterior wall **axis lines** (not the unreliable `IsExternal` flag) for the walls forming the
   building's outer perimeter — chained corner-to-corner via wall-axis + bearing continuity (the same technique
   that found the two reference corners in §3 below), not by trusting any per-wall exterior/interior tag.
2. Extrudes that perimeter polygon to each storey's real height (entrance floor + parents' unit level).
3. Cuts window and door openings at their exact extracted positions/dimensions (boolean subtraction, or simply
   leaving gaps in the wall mesh at the right spots — simpler and sufficient at this level of detail).
4. Adds the roof geometry (from the real `IfcRoof` entities).
5. Adds the deck slab (`#51836`) and any confirmed balcony slabs as separate mesh pieces at their real elevations.
6. Exports everything as a single OBJ (Blender's native importer handles this with no addon needed).

This keeps `design/lib/`'s existing drawing-canon tooling and the terrain-TIN script (`generate_terrain_tin.py`)
in the same "extract real data → generate clean geometry → import to Blender" family — one consistent pipeline,
not a mix of manual Bonsai cleanup and scripted terrain.

**Bonsai's role, reconsidered:** useful later as a *cross-check/reference* (visually compare the extracted shell
against a full import) or if a future need arises for LOD/detail beyond what this shell requires — not blocking
the shell-only goal.

## 3. Site anchoring — the tie-measurement

Two real, precise exterior corners were identified directly from the IFC model's own geometry (not estimated):

| Corner | Where |
|---|---|
| **Front** | Outside corner ~2m from the kitchen/deck door, on the straight part of the wall right where the deck's straight edge meets the house (not the round arc) |
| **Back** | Outside corner of the children's bedroom wing (window tag 5834063's room), where the back wall turns into a ~22m-long exterior wall run — a genuine major footprint corner |

Exact coordinates (both on the entrance-floor storey, ≈9.33m apart): see `blender/data/site/SITE_GEO.yaml` →
`house_reference_corners` — that file is the numeric SSOT; do not copy the coordinates here where they could drift
out of sync if a survey correction ever revises them.

**Why 2 corners, not 1:** the IFC's `TrueNorth` declaration and the survey's own ITM grid both claim true-north
alignment independently — meaning the *rotation* between the two coordinate systems is very likely already
zero. That leaves only a *translation* (X/Y offset) to solve — which 2 independent distance measurements
(triangulation) can fully determine, without needing any compass/angle measurement on site.

**What's needed from you:** measure the real-world straight-line distance from **2 of the 6 real survey boundary
points** (exact coordinates: `blender/data/site/SITE_GEO.yaml` → `boundary_itm.points` — the surveyor's own
coordinates, confirmed accurate; not reproduced here to avoid a second copy drifting out of sync) to **each** of
the 2 house corners above. A laser distance meter is ideal if there's line of sight; a long tape measure works
otherwise (in short chained segments if needed).

Pick whichever 2 of the 6 boundary points (1G-6G) are physically locatable on the ground (survey pins/monuments, or
ask מודדי עירון to help relocate them) and reasonably reachable from the house. Report back 4 numbers: distance
from point A to the front corner, point A to the back corner, point B to the front corner, point B to the back
corner (2 points × 2 corners = 4 measurements — this over-determines the solution slightly, which lets us catch
measurement errors rather than just accept whatever comes out).

**A parallel channel was opened 2026-07-09:** asking architect Michal directly for a site-plan export or
Revit-measured distances to the same 2 corners, as an alternative to the on-site tie-measurement above — see
`_COMMUNICATION/team_70/DRAFT_MESSAGE_TO_MICHAL_SITE_PLAN_v1.0.0.md` (not yet sent). The on-site plan above remains
the fallback if that doesn't return results.

Once these 4 distances are in, the transform (translation + confirmation of zero rotation) can be computed
directly — no further survey work needed.

**Note (2026-07-09): the "confirmation of zero rotation" assumption above did not hold** — see §3b.

## 3b. A candidate transform found by a different method (2026-07-09) — not a replacement for the above

While working in the live Blender model, team_00 identified `walls_119777` (a mashrabiya lattice-screen wall near
the deck) as the real south-boundary fence. Rather than the 2-corner tie-measurement in §3, this gives a
**1-edge correspondence**: the wall's own fixed direction should match real survey edge 3G→4G's direction.

**What was computed (exactly, not eyeballed):** the rotation θ that aligns the wall's north→south direction with
the terrain's own local 3G→4G direction: **θ = 105.28° (CCW about Z)** — i.e. **rotation is NOT ≈0° as §3
assumed**; a real ~105° rotation exists between the IFC world-coordinate export and the real ITM grid. Plus a
translation placing the terrain's own 4G point at the wall's south end. Full numbers:
`blender/data/site/SITE_GEO.yaml` → `fence_edge_candidate_transform`.

**Cross-check (the strongest evidence this isn't a coincidence):** after applying this transform, the terrain's
own 3G point lands within **3-9cm** of the wall's *other* (north) end — a very tight match for two independently
derived points to land on. Team_00's own manual eyeball rotation (~103.6°) was also only ~1.7° off the computed
105.28° — a second independent corroboration.

**Status: strong candidate, NOT an independently confirmed site anchor.** It depends entirely on the hypothesis
that `walls_119777` really is the physical structure at real edge 3G→4G — this has not been checked against the
architect's own plan or the client's knowledge of the site. The §3 tie-measurement plan (or Michal's coordinates)
remains the more rigorous confirmation path and should still be pursued — this candidate transform should be
treated as the model's current best-working placement, not presented to Niv as a settled fact. If §3's real
measurements arrive and disagree with this ~105° rotation by more than a few degrees, trust the real
measurement and treat this whole finding as likely a false match.

## 4. Build sequence

1. Get the 4 tie-measurements (§3) → compute the IFC→ITM transform. **Still open — not yet done.**
2. ~~Run the shell-extraction script (§2)~~ **DONE (2026-07-09, v1):** `blender/scripts/site/export_house_shell_obj.py`
   (a new, simpler script than the wall-axis-chaining approach originally described in §2 — it exports ALL walls
   via `ifcopenshell.geom` real mesh geometry directly, interior partitions included, rather than reconstructing
   just the exterior perimeter; a later pass can prune to exterior-only) → `blender/data/site/house_shell_v1.obj`
   (111 walls + 13 windows + 16 doors + the deck slab #51836 = 141 elements; roofs excluded — the 6 `IfcRoof`
   entities have no geometric `Representation` at all in this export, a real data gap, not a script bug).
3. ~~Run `generate_terrain_tin.py` on real elevation data~~ **DONE (2026-07-09, v1):**
   `blender/data/site/boundary_points_v1.csv` (6 real ITM boundary points + per-corner elevations read directly
   from the nearest visually-adjacent spot-height on the 600 DPI survey re-scan — see `SITE_GEO.yaml`
   `approximate_corner_elevations_v1`, explicitly flagged as indicative, not the surveyor's own formal point-list)
   → `blender/data/site/terrain.obj`.
4. ~~Open a dedicated Sadot Blender file~~ **DONE (2026-07-09):** `blender/sadot_v1_initial.blend` — imported both
   OBJs via `wm.obj_import(forward_axis='Y', up_axis='Z')` (the non-default axis setting matters — Blender's OBJ
   importer default assumes OBJ is Y-up and remaps Y↔Z on import, which would have scrambled our own
   easting/northing/elevation axes; both files use X=easting-like, Y=northing-like, Z=real elevation already).
5. ~~Position `house_shell_v1.obj`~~ **SUPERSEDED TWICE (2026-07-09):** first a translation-only approximation
   (south-central part of the plot, per Niv's own description); then replaced by §3b's candidate transform — the
   `terrain` object (not the house, which stays fixed as the datum) is now rotated 105.28° and translated so its
   own 3G/4G points align with the mashrabiya-wall fence candidate. **Still not a confirmed site-anchored fact —
   see §3b's status paragraph before treating this placement as final.** Visual result: the compact, recognizable
   house core (deck + windows + doors) sits right at the plot's south-east corner, matching where the candidate
   fence sits; some of the 111 walls (the oversized boundary/retaining-wall elements flagged in step 2) visibly
   extend beyond the plot on the other sides — expected (§2's known limitation), not a placement bug.
6. ~~Add the plot boundary itself as a reference curve/plane~~ **DONE** — `terrain.obj` imported as its own
   collection (`Terrain_RealSurvey`).
7. Screenshot + compare against `design/CANONICAL/CONCEPT_SKETCH_REFERENCE.md` (the client's hand sketch analysis)
   and `SITE_UNDERSTANDING_SKETCH_v1.0.0.svg` for a sanity check before proceeding to S002 concept work on top of
   this base.

**Survey re-scan finding (2026-07-09):** re-examined the full parcel 122 in the survey PDF after Michal told
team_00 it also marks the new house's position (southern part of the plot). Found no house-footprint outline —
only the already-known small outbuildings and 3 "קו בניין X מ'" building/setback-line annotations (4m/5m/7m from
different edges), which define a *permitted building envelope*, not a drawn house shape. Flagged back to team_00;
not used as a precision anchor. Full note: `blender/data/site/SITE_GEO.yaml` (comment above `house_reference_corners`).

## 5. Blockers

- ~~Dedicated Blender session~~ **RESOLVED (2026-07-09):** user opened a fresh Blender instance (MCP on port 9876,
  clean default scene) — the earlier blocker (a different, MCP-connected instance had unsaved microgreens work)
  no longer applies. `blender/sadot_v1_initial.blend` was built in this session.
- **Bonsai install** — not required for the primary plan (§2), only for optional later cross-checking; still
  blocked on explicit "online access" approval if pursued.
- **Parents' balcony + one children's balcony** — not geometrically confirmed in the IFC (`HOUSE_IFC_REFERENCE.md`
  §4b) — needs either more investigation or a client-informed design decision.
- **Tie-measurement numbers** — neither the on-site measurement (§3) nor the parallel Michal-inquiry channel
  (`_COMMUNICATION/team_70/DRAFT_MESSAGE_TO_MICHAL_SITE_PLAN_v1.0.0.md`, not yet sent) has returned results yet.

## References
- `design/CANONICAL/HOUSE_IFC_REFERENCE.md` — full house data (storeys, windows, walls, doors, stairs, materials).
- `blender/data/site/SITE_GEO.yaml` — real plot boundary, elevation, orientation.
- `blender/scripts/site/generate_terrain_tin.py` — terrain/contour tool (tested, needs real elevation point data).
- `blender/scripts/site/extract_ifc_house_data.py` — house-data extraction tool (extend for §2's shell script).
