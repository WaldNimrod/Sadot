# BLENDER HOUSE-SHELL BUILD PLAN
### Sadot · Landscape Architecture · Team 110 · v1.0.0 · 2026-07-09 · **owns: house-shell construction approach for S003** · status: **PLAN — not yet executed, blocked on 3 items (see §5)**

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
  - **Front deck — CONFIRMED, ready to model:** `IfcSlab #51836`, genuine multi-arc round edge, real geometry
    already extracted (see `HOUSE_IFC_REFERENCE.md` §4).
  - **Parents' 2nd-floor balcony — NOT YET FOUND.** A dedicated geometric search (protruding-slab pattern, same
    method that found the front deck) on the `יח' הורים` storey returned **no matching element** — no slab/space
    there protrudes past the wall envelope the way the front deck does. This may mean it isn't modeled as a
    distinct element in this IFC export at all. **Open item** — either dig further (check for a recessed/inset
    balcony that wouldn't show as "protruding"), or treat it as a landscape-team addition based on the client's
    stated need rather than an as-designed architectural element.
  - **Children's balconies (back) — PARTIALLY FOUND.** One plausible small slab (`Floor:ר3:5618668:2`, #2592,
    ~9m²) sits near window tag 5795233; no matching second slab was found near window tag 5834063. Treat as a
    working hypothesis for one balcony, open for the other.

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

| Corner | Where | IFC-native world coords (m) |
|---|---|---|
| **Front** | Outside corner ~2m from the kitchen/deck door, on the straight part of the wall right where the deck's straight edge meets the house (not the round arc) | X=-411197.429, Y=-270528.236, Z≈57.68 |
| **Back** | Outside corner of the children's bedroom wing (window tag 5834063's room), where the back wall turns into a ~22m-long exterior wall run — a genuine major footprint corner | X=-411206.746, Y=-270527.663, Z≈57.69 |

Distance between them (internal check): ≈9.33m. Both are on the same storey (entrance floor, real elevation
~57.69m in the IFC's own world coordinates).

**Why 2 corners, not 1:** the IFC's `TrueNorth` declaration and the survey's own ITM grid both claim true-north
alignment independently — meaning the *rotation* between the two coordinate systems is very likely already
zero. That leaves only a *translation* (X/Y offset) to solve — which 2 independent distance measurements
(triangulation) can fully determine, without needing any compass/angle measurement on site.

**What's needed from you:** measure the real-world straight-line distance from **2 of the 6 real survey boundary
points** (table below, from `blender/data/site/SITE_GEO.yaml` — these were the surveyor's own coordinates,
confirmed accurate) to **each** of the 2 house corners above. A laser distance meter is ideal if there's line of
sight; a long tape measure works otherwise (in short chained segments if needed).

| Survey point | Easting (ITM) | Northing (ITM) |
|---|---|---|
| 1G | 196695.299 | 707864.034 |
| 2G | 196701.014 | 707864.620 |
| 3G | 196694.530 | 707812.220 |
| 4G | 196684.489 | 707813.303 |
| 5G | 196680.410 | 707860.480 |
| 6G | 196695.580 | 707862.030 |

Pick whichever 2 of these 6 points are physically locatable on the ground (survey pins/monuments, or ask מודדי
עירון to help relocate them) and reasonably reachable from the house. Report back 4 numbers: distance from point
A to the front corner, point A to the back corner, point B to the front corner, point B to the back corner
(2 points × 2 corners = 4 measurements — this over-determines the solution slightly, which lets us catch
measurement errors rather than just accept whatever comes out).

Once these 4 distances are in, the transform (translation + confirmation of zero rotation) can be computed
directly — no further survey work needed.

## 4. Build sequence (once unblocked)

1. Get the 4 tie-measurements (§3) → compute the IFC→ITM transform.
2. Run the shell-extraction script (§2) → `house_shell.obj`.
3. Run `generate_terrain_tin.py` on real elevation data (needs the surveyor's digital point list — separate open
   item, not blocking the house shell) → `terrain.obj`.
4. Open a **dedicated Sadot Blender file** (see §5 — currently blocked) → import both OBJs, apply the computed
   transform to `house_shell.obj` so it sits correctly on the real, precisely-plotted boundary.
5. Add the plot boundary itself as a reference curve/plane (from `SITE_GEO.yaml`'s 6 real points).
6. Screenshot + compare against the client's hand sketches and `SITE_UNDERSTANDING_SKETCH_v1.0.0.svg` for a
   sanity check before proceeding to S002 concept work on top of this base.

## 5. Blockers (unchanged from earlier — restated for this plan's completeness)

- **Dedicated Blender session** — the currently MCP-connected Blender instance has unsaved microgreens work
  (`is_dirty: True` on `IsraelMicrogreens_026.blend`) — must not be touched. Needs either that session
  saved/closed, or a second Blender instance opened by the user.
- **Bonsai install** — not required for the primary plan (§2), only for optional later cross-checking; still
  blocked on explicit "online access" approval if pursued.
- **Parents' balcony + one children's balcony** — not geometrically confirmed in the IFC (§1) — needs either more
  investigation or a client-informed design decision.

## References
- `design/CANONICAL/HOUSE_IFC_REFERENCE.md` — full house data (storeys, windows, walls, doors, stairs, materials).
- `blender/data/site/SITE_GEO.yaml` — real plot boundary, elevation, orientation.
- `blender/scripts/site/generate_terrain_tin.py` — terrain/contour tool (tested, needs real elevation point data).
- `blender/scripts/site/extract_ifc_house_data.py` — house-data extraction tool (extend for §2's shell script).
