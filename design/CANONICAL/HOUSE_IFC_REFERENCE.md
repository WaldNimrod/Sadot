# HOUSE IFC REFERENCE — extracted from the architect's model
### Sadot · Landscape Architecture · Team 110 · v1.1.0 · 2026-07-09 · **owns: house-model ground truth for landscape design** · status: **REAL DATA, with flagged reconciliation gaps — read the caveats before using positions**

> **v1.1.0 update (2026-07-09):** team_00 supplied real ground truth that corrected two v1.0.0 hypotheses — the
> real deck is at the front, extends from the kitchen, with a round end toward the garden; the "window not to
> block" belongs to one of two children (Yinon/Shani), each with their own room+pergola at the back, not the
> "parents' unit" wing. A targeted re-investigation (§4, §2) revised both findings below — the old §4 candidate
> (`IfcSpace #808`) is now **ruled out**, and the window hypothesis is downgraded to an unproven pattern, not
> retracted outright (see §2).

> Source: `raw-materials/from-client/NSB02.ifc` (Autodesk Revit 2023 export, IFC2X3, author "Michal", exported
> 2026-07-06). Extracted using `ifcopenshell` (a real IFC-parsing library, not text/regex guessing) — see
> `blender/scripts/site/extract_ifc_house_data.py`, reproducible. Cross-validated: the storey/window/stair
> numbers below were independently produced 3 times (2 parallel extraction agents + a direct re-run) with
> identical results.

## 0. Read this first — data-quality issues that affect how you use everything below

1. **Coordinate-system mismatch (important, unresolved).** This IFC file's own coordinates do NOT reliably align
   with the real ITM survey grid in `blender/data/site/SITE_GEO.yaml`. Evidence: `IfcSite.RefLatitude/RefLongitude`
   decode to ~32.045°N/34.769°E, which is NOT Pardes Hanna (~32.46°N/34.96°E — a ~50km discrepancy); the file's
   internal XY coordinates are large arbitrary negative numbers (~-411,000, -270,500) consistent with an
   uncalibrated Revit "Survey Point" offset, not real ITM easting/northing (which would be positive, ~100,000-280,000
   / ~350,000-1,250,000). **Do not assume this file's absolute X/Y/Z can be directly overlaid on the real site
   survey without reconciliation** — ask the architect (Michal) for the Revit "Shared Coordinates" / true
   Survey Point setup, or plan to manually re-anchor the house model once imported, using the real front-door
   position relative to the surveyed boundary as the anchor.
2. **`IsExternal` property is unreliable.** Every one of the 111 walls reads `IsExternal=True` (should be
   impossible for a real house — interior partitions exist). Do not use this flag to separate exterior envelope
   from interior walls. On `IfcWindow`/`IfcDoor`, the same flag is inconsistent even between two windows in the
   *same* wall — also not trustworthy per-element.
3. **Window/door type names are generic and don't match actual dimensions.** E.g. many windows share the type
   name "70X190" (70×190cm) but their real per-instance `OverallWidth`/`OverallHeight` range from 1.00×0.50m up
   to 2.76×1.50m. Always use the per-instance dimension (table below), never the type-name-implied size.
4. **The one deck/terrace-NAMED element in the file (`IfcSpace #808`) is confirmed NOT the real deck** — no
   curved geometry at all, and its position offset was independently re-derived by hand (not a tool bug) — it
   really is orphaned in the model. The real deck candidate found instead (`IfcSlab #51836`, no name tag) is
   documented in §4.
5. **Length unit is centimeters** (confirmed via `IfcUnitAssignment` + cross-checked against real dimensions —
   e.g. wall/floor layer thicknesses only make sense as cm). All values below are already converted to meters.

## 1. Building storeys (5)

| Storey | Elevation (m, local) |
|---|---|
| `0- קומת כניסה` (entrance floor) | 55.99 |
| `יח' הורים` (parents' unit) | 59.09 |
| `גג שכן` (neighbor's roof — likely a roof-datum level, not habitable) | 60.35 |
| `גג 6` (roof 6 — likely a roof-datum level) | 61.89 |
| `גג ניב` (Niv's roof — likely a roof-datum level, name probably coincidental, not a distinct family floor) | 62.95 |

Real structure: 2 occupied levels (entrance floor + a raised "parents' unit" ~3.1m above it) + 3 roof-datum
levels used to host different roof-pitch geometry.

## 2. Windows (13 total) — precise per-instance data

| Tag | W×H (m) | Storey | Exterior? |
|---|---|---|---|
| 5709118 | 1.00×0.50 | entrance | yes (flag inconsistent — see §0.2) |
| 5774586 | 1.00×0.50 | entrance | — |
| 5782595 | 1.40×1.20 | entrance | — |
| **5792190** | **2.76×1.50 (largest)** | **parents' unit** | — |
| 5792970 | 1.00×0.50 | parents' unit | — |
| 5793211 | 1.00×1.00 (round) | parents' unit | yes |
| 5793427 | 1.50×0.70 | parents' unit | — |
| 5794246 | 2.08×1.14 (mamad door-window, no host wall) | entrance | yes |
| 5795233 | 1.00×0.50 | entrance | — |
| 5829225 | 1.50×0.70 | parents' unit | — |
| 5834063 | 1.40×1.20 | entrance | — |
| 5977949 / 5977979 | 0.50×0.50 (mamad vent pipes ×2) | entrance | yes |

**Correction (v1.1.0):** the v1.0.0 table above has 8 entrance-floor rows and 5 parents'-unit rows (13 total) —
the v1.0.0 prose said "6 of 13 in the parents' unit," which was a miscount; it's actually **5**. Corrected here.

**Client-brief cross-reference — REVISED.** Team_00 clarified the two names in the voice brief (ASR: "עינון"/
"שני") are really **Yinon and Shani, the children**, each with their own room+pergola+one window, at the BACK of
the house — NOT the "יח' הורים" (parents' unit) wing as v1.0.0 guessed. The IFC file carries **no occupant names
anywhere** (confirmed exhaustively — Revit exports essentially never carry this), so this can't be settled from
the BIM data alone. A re-investigation found a **plausible but unproven pattern**: of the 8 entrance-floor
windows, two (tags **5834063** and **5795233**, ~5.75m apart) flank a cluster containing a door + 2 ventilation
pipes (a bathroom/hall signature) — architecturally consistent with "two bedrooms flanking a shared bath," which
would fit two children's rooms. One small slab (`Floor:ר3:5618668:2`, #2592, ~9m², entrance-floor level) sits
right at window 5795233's position — a plausible small-balcony/pergola pad — but no matching second slab was
found near window 5834063, so the "two matching balconies" reading is only half-supported. **This is a
hypothesis to confirm with the client, not a settled fact** — added to the WhatsApp draft. The two `ממד`
(mamad/safe-room) openings and the parents'-unit windows are lower-probability candidates now, not excluded
entirely.

## 3. Building envelope (footprint)

Best estimate: **~54m × ~26.5m × ~9.5m** (X×Y×Z bounding box), BUT this likely still includes some boundary/
retaining garden walls (several walls are named `קיר בלוק קיים` — "existing block wall," a plausible property-
boundary designation, not house shell) — **verify visually against the architect's 2D plan before treating this
as the true roofline**, especially since this footprint (~1,430 m²) is implausibly larger than the entire 752 sqm
registered plot, confirming it over-captures something beyond the house itself.

- **111 walls** (96 `IfcWallStandardCase`), **16 doors** (3 flagged exterior: two single-leaf 80cm doors + one
  combined 90+40cm door — these three are the real physical entrance-to-garden connection points),
  **6 roofs** (one, `Basic Roof:10`, sits ~133m from the rest of the model — a stray/context fragment, excluded).
- **2 stairs, 0 ramps, 0 exterior stairs.** Stair 1: 19 risers × 18 treads, riser height 16.3cm, tread 29.4cm.
  Stair 2 (short entry run): 4 risers × 3 treads, riser height 17.5cm, tread 27.0cm. **The house model does not
  define an exterior stair or ramp at all — the entrance-to-garden level transition is a landscape-design
  decision, not something inherited from the house model.** This directly matters for the client's "homogeneous
  level continuity" request.

## 4. Deck / terrace — REVISED (v1.1.0): real candidate found, name-tagged element ruled out

**v1.0.0 candidate `IfcSpace #808` ("מרפסת") is now definitively ruled out** — re-verified 2026-07-09 by 3
independent methods (ifcopenshell's own world-coords API, a from-scratch hand-composed placement-chain matrix,
and a local-to-world cross-check): its ~90-115m offset from the rest of the house is real, not an extraction bug.
Its own boundary was also walked recursively for curved geometry: **zero curves** — a plain straight polygon. The
client's ground truth (front, kitchen-adjacent, ROUND end toward the garden) rules this element out on both
counts (wrong place, wrong shape).

**New best candidate: `IfcSlab #51836` ("Floor:ר4:5739839"), entrance-floor storey, no deck-indicating name.**
Found by searching the *entire* file for any element with a genuinely large curved boundary segment (excluding
mm-scale furniture fillets) — this slab is the only structural/architectural element with a real multi-arc round
edge (5 distinct arc radii, 1.68m to 7.92m — a compound sweeping curve, not a single filleted corner). Supporting
evidence, all independently corroborating:
- **Protrudes ~2.2m past the building's own wall envelope** on the true-north side (Y+ = true north, confirmed
  via the IFC's own `TrueNorth` declaration) — i.e. it's an exterior projection off the house, not an interior room.
- **Directly adjacent** (overlapping footprint) to `IfcBuildingElementProxy "UK_Gas Hob - 4 Burner"` — a kitchen
  appliance sitting right on/against this slab.
- **2.6m from a 4.20m-wide double-leaf glass door** (`דלת זכוכית דו כנפית 400/240`, tag 5935521) hosted in the
  bordering wall — a door this wide reads as a kitchen-to-deck opening, not an interior doorway.
- Surrounded by ~22 small wall segments named `עץ` (**wood** — Hebrew) plus an outdoor sofa (`M_Sofa-Pensi`,
  found via the same curve-search since its cushions also register small arcs) sitting immediately adjacent —
  consistent with wood decking/railing + deck furniture.
- Corroborating detail: `#808`'s (wrong) base elevation (57.6947m) is within 2cm of this slab's top elevation
  (57.6747m) — suggesting #808's Revit room-tag inherited the right *floor level* while its *horizontal* position
  drifted/corrupted during design iteration — a plausible root cause for the original stale tag, and further
  evidence the real design intent for "deck at this level" lives at this slab's location.

No room in the file is explicitly tagged "מטבח" (kitchen) anywhere — Revit exports frequently omit this label;
the hob+door+slab spatial cluster is the evidence, not a name match.

**Status: high-confidence candidate, not yet visually confirmed against the architect's 2D plan.** Recommend
confirming with Niv/the architect before finalizing (question added to the WhatsApp draft) — but this is now the
working assumption for S003 3D-modeling purposes rather than an open unknown.

## 5. Materials (63 total) — relevant to landscape hardscape matching

Exterior wall structure is plain masonry/concrete (בלוק=concrete block 10-30cm, בטון=concrete 15-30cm), no
cladding layer in the exported layer sets. Two screening-panel wall types use a **מַשׁרַאבִּיָה (mashrabiya lattice
screen)** — one with a "mesh" material, one with gray sheet metal — worth knowing if the landscape design should
echo or contrast this screening language.

**Exterior-paving-relevant floor build-ups** (most directly useful — these are real Revit floor types, likely
including the actual exterior paved areas):
- `Floor:Generic 300mm kayam` — 3cm Porcelain over 7cm sand over 20cm new concrete (classic tile-on-sand-bed).
- `Floor:ר1` / `ר1 4` — 10cm Porcelain over 8-10cm sand over 20cm concrete.
- `Floor:ר7` — 3cm "אבן חומה" (facade/wall stone, likely local sandstone/limestone).

Roof: tile roof (`רעפים`, 5cm clay tile over 15cm wood strips, ~100m² + ~62m² across 2 roofs) plus a flat
low-slope concrete roof variant (15cm concrete, ~26m²+~22m²).

No fire/thermal/acoustic property data exists anywhere in the file (checked exhaustively — 0 matches across all
1,442 property values) — not a gap in extraction, the model genuinely doesn't carry this data.

## 6. Site (IfcSite)

`RefElevation = 1.7047m` (project length units) — note this does NOT directly match the storey elevations
(55.99-62.95m), meaning storey elevation is referenced to an internal Revit project-base-point datum, not
`RefElevation` directly. Only one property set (`Category: Topography`) — no soil/terrain/vegetation data.
`TrueNorth` direction = `(~0, 1)` — confirms the project's own Y-axis is declared as true north, consistent with
the independently-computed boundary-edge bearings in `blender/data/site/SITE_GEO.yaml`.

## 7. What this means for the Blender/S003 pipeline

- Import via Bonsai (once installed — see open item) will bring in real geometry, but the model will need to be
  **manually re-anchored** to the real ITM survey coordinates (§0.1) — do not trust the file's native XY/Z for
  site placement.
- The 3 real exterior doors + the stair data (§3) plus the newly-identified deck slab (§4, `IfcSlab #51836`) are
  the actual house-to-garden connection points to design the level-continuity/hardscape transition around.
- Confirm the §4 deck candidate and the §2 children's-window hypothesis directly with Niv before finalizing
  either in the landscape model — both are strong leads, not settled facts.
