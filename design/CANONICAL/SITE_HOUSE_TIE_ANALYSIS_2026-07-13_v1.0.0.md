---
id: SITE_HOUSE_TIE_ANALYSIS_2026-07-13_v1.0.0
type: technical analysis (team_00 instruction 2026-07-13: examine new materials from Michal in depth, document
  well, position the house precisely, mark heights/boundaries clearly)
from: team_110
to: team_00
date: 2026-07-13
project: sadot
inputs:
  - raw-materials/from-client/שטח ובית.pdf (A0 sheet, combined entrance-floor plan + site-siting plan; PDF
    metadata: authored by Michal, exported from "NSB02.pdf", created 2026-07-12 18:35 IDT)
  - raw-materials/from-client/NSB02_v2_2026-07-13.ifc (new IFC export, re-exported 2026-07-12, alongside the
    original raw-materials/from-client/NSB02.ifc, re-exported 2026-07-06 — both kept, not overwritten)
---

# Site + House Tie Analysis — New Materials from Michal (2026-07-13)

## 0. What this answers, and the honesty bar it's held to

team_00 asked us to (1) copy the new materials into sources, (2) examine them in depth, (3) note that they
contain the connection between the model and the ground, (4) document well, examine in Blender, position the
house precisely against geographic direction/topography/boundaries, mark heights/boundaries clearly, and (5)
work only on a new copy of the model file. This document is deliverable (3)+(4). Per this project's established
rule (see the retracted 105.28° rotation episode in `blender/CURRENT_MODEL.md` §0.1): **no number below is
reported as precise unless it was verified two independent ways.** Where that bar isn't met, it's stated
plainly, not rounded up to sound more certain than it is.

## 1. שטח ובית.pdf — what it actually is

A single A0 sheet (2384×3370pt) combining two drawings Michal already had: the entrance-floor plan
("קומת כניסה", revision-tagged 21.08.25 → 23.12.25), and — new, and the reason this file matters — a **site
plan showing the real house footprint plotted directly on the licensed-survey boundary**, corner IDs and all.

**Confirmed same real coordinate system as the licensed survey (`10111TD122`), independently, three ways:**
- Boundary corners **4G** and **5G** are labeled explicitly on this sheet, in the same positions/shape as
  `blender/data/site/SITE_GEO.yaml` → `boundary_itm`.
- Boundary edge lengths printed on the sheet match the survey's own computed edge lengths: **52.80** m (survey:
  edge 2G→3G = 52.800 m), **10.10** m (survey: edge 3G→4G = 10.099 m), **15.25** m (survey: edge 5G→6G =
  15.249 m). Three independent edge matches, not one — this is the same plot, same datum, not a redrawn/approximate
  copy.
- A north arrow is drawn on the sheet, pointing consistent with the plot's long axis running near N–S — a
  qualitative sanity check only (a hand-drawn arrow's exact angle isn't reliable to the degree, per the same
  lesson as the retracted rotation), but it does not contradict the already-rigorously-confirmed 0° rotation
  finding.

### 1a. Real elevation anchors — a genuine upgrade over the previous approximation

This is the single most useful new fact on the sheet. The round deck/porch (already identified as `IfcSlab
#51836`, "מרפסת קדמית") is explicitly labeled here **"מרפסת, מפלס יח' הורים"** (deck, parents'-unit level) with
an absolute elevation callout:

> **+55.97 m**, with a **"-0.02"** notation directly beneath it.

This was verified against the PDF's actual embedded text layer (not just a visual read) — most of this sheet's
dimensions and labels are vector *outlines*, not real text (confirmed: searching the PDF's text layer for
boundary IDs and most dimension numbers returns nothing, because they're drawn as curves), but **"+55.97 m" and
"-0.02" are real, extractable PDF text objects**, at PDF coordinates (853–890, 2586–2596). That means this
number is not a transcription risk the way a visually-read dimension is — it's literally embedded as text in
the file.

**Why this matters:** the previous Z-anchor (`SITE_GEO.yaml` → `client_confirmed_height_facts`) was a rough
verbal relative statement ("floor is ~0.30–0.40m above the north/east ground"). This is a real, plotted,
same-datum absolute elevation for a specific, already-identified point on the house, on the same sheet that
independently checks out against the survey's own boundary geometry. It directly supersedes the old
`front_corner z: 57.68` (IFC-internal, never tied to the real datum) as the better real-world Z reference.

Three more real elevation ties, from utility inspection chambers ("תא", top-level/invert-level) along the
north/entrance walkway, at plotted positions near the pergola:
| Chamber | T.L. (top level) | I.L. (invert level) |
|---|---|---|
| near entrance pergola (west) | 55.70 | 54.70 |
| middle (near garden strip) | ~55.3x (partially obscured in the scan) | ~54.x (obscured) |
| east, near "גינון" | 55.53 | 54.89 |

These sit inside the survey's known elevation scatter (54.47–57.59), consistent, not contradictory.

### 1b. Building lines (קווי בניין) — now shown relative to the actual house, not just abstractly

The 2026-07-09 re-scan of the original survey found three building-line (setback) annotations — 4m, 5m, 7m —
but couldn't relate them to the house because the survey doesn't show the current house at all. **This sheet
does:** the 5m line runs near the 5G/north end, and the 7m line runs near the 4G/south end, both now drawn
directly against the real house footprint and boundary. This is real, useful siting context even though (see
§1c) it doesn't by itself resolve a precise numeric translation.

### 1c. What was attempted for a precise X/Y translation, and why it's not reported as solved

Two independent extraction approaches were tried, in the same spirit as the rigorous rotation resolution
(placement-hierarchy walk, 3 methods) that this project already trusts more than one-off visual matches:

1. **Raster pixel-georeferencing:** rendered the sheet at 200 DPI, pixel-located the 4G and 5G corner markers
   precisely via a labeled-grid crop technique, intending to compute a pixel→real-ITM affine transform from
   those two known control points and apply it to a pixel-located house corner.
2. **Vector PDF extraction:** re-approached via the PDF's own vector data (PyMuPDF) to avoid raster/pixel
   estimation error entirely — confirmed the boundary line is drawn in a distinct color `(0,0,0.496)` as ~45
   dashed-line path fragments, and confirmed real embedded text exists for some labels (see §1a) but not for
   the boundary corner IDs or most dimension numbers (drawn as outlined curves, not text — not searchable).

**Result:** both approaches are directionally sound, but neither reached the same bar of confidence as the
rotation finding. The raster approach carries real pixel-picking uncertainty (sub-meter, not survey-grade); the
vector approach found the right boundary path but resolving it into clean corner vertices (vs. dash-segment
endpoints) and then finding the *house's own* corresponding vector path needs more dedicated work than is wise
to rush here — this project already has one retracted, overconfident geometric claim on record
(`blender/CURRENT_MODEL.md` §0.1), and a second one isn't worth the risk of a rushed pixel-guess dressed up as
precise. **Translation (X/Y) is therefore still logged as open**, but materially better-constrained than
before (real building-line proximities, confirmed same-plot siting, confirmed side of plot) — not the same as
"no real basis" it was at before this file arrived.

**Recommended concrete next step (cheapest real fix):** ask Michal directly for either the underlying DWG/DXF
(which carries exact numeric coordinates, no visual extraction needed at all), or simply the specific
offset/coordinates she used when siting the house on this sheet — she has this number in her own CAD software
already. This is a small addition to the existing ask in
`_COMMUNICATION/team_70/DRAFT_MESSAGE_TO_MICHAL_SITE_PLAN_v1.0.0.md` (not yet sent) — worth adding before
sending, since this new sheet actually answers that draft's "Option A" almost exactly and she may be able to
give the last-mile number in one line.

## 2. NSB02_v2_2026-07-13.ifc — what actually changed vs. the original

Compared programmatically (`ifcopenshell`, both files), not by filename/date assumption:

- **File-level:** identical entity-type histogram (same count of every IFC entity type), identical total line
  count (141,818 lines each) — this is a re-export of the same model, not a structurally different one.
- **Site/placement/georeferencing: byte-identical.** `IfcSite` RefLatitude/RefLongitude/RefElevation, the full
  `IfcLocalPlacement` chain (Project→Site→Building→all 5 storeys), and the `TrueNorth` declaration are
  unchanged between the two files. **The existing rigorous rotation=0° finding therefore still applies to this
  new file unchanged** — no need to redo that 3-method analysis.
  - Reconfirmed in passing: `IfcSite`'s own RefLatitude/RefLongitude (32°2'42.72"N, 34°46'10.92"E) still does
    **not** match the real Pardes Hanna location or the client-supplied WGS84 pin — this was already flagged as
    unreliable Revit-template data, not a new problem.
- **Building envelope: byte-identical.** All 111 `IfcWall` entities' world-coordinate geometry (1,740 vertices)
  match exactly between old and new — same bounding box, same deck slab centroid and Z-range to the 4th decimal.
  **The two existing `house_reference_corners` and the deck identification are unaffected by this update.**
- **What did change (2,008 of 26,281 IfcCartesianPoint entities, traced to their owning elements):** small,
  scattered interior edits — a sliding door, some furniture (desk, chair), two interior walls, one room's floor,
  an A/C socket, a 3D electrical socket. Normal iterative-design churn between a 2026-07-06 and 2026-07-12
  export, unrelated to siting. Not catalogued exhaustively here since it's design detail, not a geometry-anchor
  question — flagged only so nobody assumes "identical entity count" means "nothing changed at all."

**Bottom line: this IFC revision does not itself carry new site-tie information — the PDF does (§1).** The IFC
update is a normal design-progress re-export; the meaningful new material this round is the site plan.

## 3. Net effect on the open items

| Item | Before this round | After this round |
|---|---|---|
| Rotation | Confirmed 0°, 3 independent methods | **Unchanged, now also cross-checked against a byte-identical placement hierarchy in the new IFC export** |
| Z (elevation) | Rough verbal relative statement, no real datum tie | **Real plotted absolute elevation (+55.97m) at an already-identified house point, same sheet that verifies against the real boundary — materially stronger anchor** |
| X/Y (translation) | Provisional placeholder, "no real basis" | **Still open, but now bounded by real building-line proximities and confirmed same-plot siting — not the same as before; closing it precisely needs Michal's DWG or her stated offset** |
| Building lines (4/5/7m) | Found in the abstract (re-scan), not tied to the house | **Now shown directly against the real house footprint** |
| Tree count/positions | 13 trees (survey) | **Consistent** — tree numbers 1,3,4,6,7,8,9,12,13,14 seen on this sheet match the survey's own numbering (which skips #11); no discrepancy found |

## 4. Applying this to the model — a new copy, plus a bug found along the way

Per instruction, all of this was applied to a **new copy** (`blender/sadot_v3_site_tie_2026-07-13.blend`,
branched from `sadot_v1_initial.blend` — `sadot_v1_initial.blend` is untouched):

1. Re-anchored the house's Z using the deck's real +55.97m elevation (§1a).
2. **While verifying that change, found the house floating ~55m above the terrain.** Root cause: the terrain
   uses a *local* vertical datum (empirically confirmed: `local_Z + 54.76 = real absolute elevation`, exact
   across all 6 boundary corners) — the new real elevation needed converting into that local datum
   (`55.97 − 54.76 = 1.21`) before use, not applied as a raw absolute value. Fixed.
3. **Separately, also found the house's X/Y position (inherited unchanged from v1) sat entirely outside the
   plot's footprint** — a real pre-existing bug, not introduced by this pass or a side-effect of the Z fix.
   Corrected by rigidly re-centering the whole house-shell on the terrain's bounding-box center — this is a
   rough fix to a broken state, **not** a new precise X/Y tie (that's still open, per §1c). Verified visually
   (top-down viewport screenshot): house now sits within the plot outline, roughly matching the originally-
   intended "south-central" description.
4. Added small labeled markers at all 6 real boundary corners (1G–6G) directly in the scene, and updated the
   in-scene flag text to reflect the new, more accurate status.

**Correction (same day):** team_00 caught, on sight, that the above placement was actually wrong despite being
reported as verified — the house appeared clearly outside the plot in a screenshot. Re-investigation found two
real bugs (a renamed object silently excluded from the shift; bounding-box-center matching used instead of a
true point-in-polygon test against the real non-rectangular plot) plus one pre-existing data anomaly (one door
object with an export-corrupted Z, now hidden and flagged, not guessed at). All fixed and re-verified with a
proper point-in-polygon test this time, plus a north arrow added. Full narrative, numbers, and the process
lesson: `blender/CURRENT_MODEL.md` pass 7 ("sixth pass").

## Cross-references

- `blender/data/site/SITE_GEO.yaml` — technical SSOT, updated alongside this document with the new elevation
  anchors and building-line notes
- `blender/CURRENT_MODEL.md` — full placement history; this round appended, not rewritten over prior passes
- `design/CANONICAL/HOUSE_IFC_REFERENCE.md` — deck/corner identification (unaffected, see §2)
- `_COMMUNICATION/team_70/DRAFT_MESSAGE_TO_MICHAL_SITE_PLAN_v1.0.0.md` — recommend adding the DWG/offset ask
  before sending (still not sent as of this writing)
