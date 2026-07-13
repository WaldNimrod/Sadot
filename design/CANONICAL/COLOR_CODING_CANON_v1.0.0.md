---
id: COLOR_CODING_CANON_v1.0.0
type: canonical reference (team_00 instruction, 2026-07-14: "אנחנו נתחיל להגדיר מפתח צבעים לכלל המודל —
  יש לייצר קאנון לנושא" — start defining a color key for the whole model, create a canon for it)
from: team_110
to: whoever works on the Sadot Blender model / any exported drawings or renders
date: 2026-07-14
status: DRAFT — opened with 3 categories, meant to grow. Add new rows here as new categories are defined,
  don't let color decisions live only inside a Blender file.
---

# Color Coding Canon — Sadot 3D Model

Single source of truth for what color/material represents what, across the Blender model and any renders or
drawings derived from it. When a new object category needs a color, it gets defined here FIRST, then applied
in Blender — not the other way around, so the convention stays discoverable and consistent across sessions.

## Categories (as of 2026-07-14)

| Category | Color / material | Hex (approx) | Applies to |
|---|---|---|---|
| Labels & annotations | Glowing yellow (emissive) | `#FFD400` emission | All `FONT` text objects — boundary corner labels, height-reference labels, flag notes, north-arrow label. Emissive so they read clearly regardless of scene lighting/angle. |
| House | Gray — concrete | `#8C8C8C` (matte, non-emissive) | The main house structure (the compact cluster including the round front deck) — currently the majority-piece cluster of the joined `walls_119777_Basic_Wall...` object family. |
| Walls / fences (חומות) | Light gray | `#B8B8B8` (matte, non-emissive) | Property boundary walls / fences / screen elements — currently the smaller, spatially-separate cluster of the same object family (includes the mashrabiya screen run). Distinct from "House" — these are boundary/fence structures, not the building itself. |

| Terrain / original ground | Light brown, 50% transparent | `#C29A6B` @ 50% alpha | The surveyed 6-point terrain polygon (`terrain` object). |
| Roof (flat, placeholder) | Dark warm gray (PLACEHOLDER — not yet client-specified) | `#59544D` | `ROOF_flat_whole_house` — added 2026-07-14 to cover the IFC's missing roof data (real gap: no `IfcRoof` geometry exists in the source file). Color not yet confirmed with team_00 — ask before treating as final. |

## Still open (not yet defined — ask before assuming)

- Boundary-corner markers (the `BOUNDARY_*` empties themselves, as opposed to their text labels)
- North arrow geometry (as opposed to its label, already covered above)
- Future modeled elements: tire fence, rockery/terracing, pool, planting

## Applying this in Blender

Each category = one shared Blender material (not per-object duplicates), so a future palette change is a
one-line edit propagating everywhere. Material names follow `MAT_<category-slug>` (e.g. `MAT_house_concrete`,
`MAT_walls_fences_light_gray`, `MAT_labels_glow_yellow`) for easy lookup.

## Cross-references

- `blender/CURRENT_MODEL.md` — which object groups currently map to which category (may shift as the model
  is refined — check there for the current live object-name mapping, not just this canon's category list)
- `design/CANONICAL/07_DRAWING_SET_and_RENDER_MANIFEST.md` — render/drawing conventions this feeds into
- `design/CANONICAL/BLENDER_MODELING_TEAM_CHARTER_v1.0.0.md` — general modeling discipline
