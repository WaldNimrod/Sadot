# HOUSE IFC REFERENCE — extracted from the architect's model
### Sadot · Landscape Architecture · Team 110 · v1.0.0 · 2026-07-08 · **owns: house-model ground truth for landscape design** · status: **REAL DATA, with flagged reconciliation gaps — read the caveats before using positions**

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
4. **The one deck/terrace-named element found does not spatially match the house.** See §4 — flagged, not used
   for design yet.
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

**Client-brief cross-reference:** the client's voice-note brief (`CLIENT_BRIEF_NIV_SADOT_v1.0.0.md` §2/§2a)
mentions not blocking the view/light from a specific family member's window. **6 of the 13 windows are in the
"יח' הורים" (parents' unit) wing** — including the largest window in the house (2.76×1.50m, tag 5792190) and a
round window (tag 5793211). This is the strongest lead for which physical window the client meant — worth
confirming directly (added to the WhatsApp draft). The two `ממד` (mamad/safe-room) openings are NOT a person's
window — exclude those from the privacy/view discussion.

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

## 4. Deck / terrace — found, but flagged, do not use yet

Only one element in the entire file carries a deck/terrace/balcony name in any language (searched Hebrew: דק,
מרפסת, טרסה, פטיו, ורנדה; English: deck, terrace, patio, balcony, veranda — across all slabs, coverings, proxies,
roofs, spaces): **`IfcSpace #808`, `LongName="מרפסת"` ("balcony/terrace")**, an L-shaped ~31.6 m² room/volume,
base elevation 57.69m, on the entrance-floor storey.

**Problem: its footprint sits ~90-115m away from every wall/window/door in the rest of the model** (real, checked
geometrically, not a units artifact). Two explanations, both plausible, neither confirmed:
(a) it's a legitimately detached garden terrace, separate from the house structure, consistent with the client
describing the deck-to-yard connection as something to unify — but 90m+ is very large for a 752 sqm plot;
(b) it's a stale/orphaned Space tag left over from an earlier design iteration in Revit, whose schedule data
(name, area) is real but whose 3D position was never updated.

**Do not use these coordinates for landscape design until confirmed with the architect.** No `IfcSlab` or
`IfcCovering` (the usual "solid deck" element types) carries any deck-indicating name anywhere in the file — the
physical deck, if modeled at all, exists without a name tag, or isn't a distinct object in this export.

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
- The 3 real exterior doors + the stair data (§3) are the actual house-to-garden connection points to design
  the level-continuity/hardscape transition around — more reliable than the flagged deck space (§4).
- Confirm the deck/terrace question directly with the architect or Niv before committing to any specific deck
  geometry in the landscape model.
