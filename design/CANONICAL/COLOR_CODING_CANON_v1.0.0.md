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
| House (NEW, in-scope) | Gray — concrete | `#737373` (matte, non-emissive) | The current/new house — the actual design scope. 268-piece cluster of the `walls_119777_Basic_Wall...` family. |
| **House (OLD, reference only)** | Dark gray, fully transparent | `#383838` @ 25% alpha | **CORRECTION (2026-07-14): this is NOT a fence/screen — it is the OLD, pre-existing house, shown only for reference/context.** Not part of the design scope. 29-piece cluster, spatially separate from the new house. First misidentified as "walls/fences" — corrected same day team_00 flagged it. |

| Terrain / original ground | Light brown, 50% transparent | `#C29A6B` @ 50% alpha | The surveyed 6-point terrain polygon (`terrain` object). |
| Ground fill (solid) | Solid opaque brown — deliberately distinct (opaque, not transparent) from the survey-reference terrain above, since this represents real fill/build-up soil, not the abstract survey polygon | `#4D2E17`, 100% opaque | New 2026-07-14 (team_00 instruction): "יש 'למלא' אדמה ולהשלים את שכבת הterrain עד לחומה שיצרנו ממזרח... זה הקרקע שלהם הבסיסית" (need to fill soil and complete the terrain layer to the east wall — this is their base ground). First use: `GROUND_FILL_east_tree03_area`, connecting the real surveyed boundary edge (2G-3G) to the new east wall's outer face, flat at real 54.91m (team_00-stated current ground level in that area). `MAT_ground_fill_solid_brown`. |
| Roof — **REMOVED 2026-07-14, open problem** | n/a — no roof geometry currently exists in the model | `#59544D` (was) | Tried twice (pass 11: flat per-storey; pass 12: real gabled slopes fit from the IFC's own roof elements, plus a deck roof) — team_00 rejected both, the second time explicitly asking for a different approach rather than another iteration of the same method ("נצטרך למצוא דרך אחרת"). Both attempts deleted. Full history (kept for whatever the next approach draws on, but none of it reflects the current scene): `blender/CURRENT_MODEL.md` passes 11-13. |
| Decking (wood) | Warm wood brown | `#734A26` | `DECKING_wood_front_porch` — 15cm layer on the concrete front deck (2026-07-14, team_00 instruction), real elevation 55.97m (concrete) to 56.12m (finished decking surface). |
| Planting / existing trees | Natural: trunk warm brown, canopy matte green (not the abstract label/structure palette — trees read better in natural tones) | Trunk `#4D3320`, canopy `#356929` | New category, defined 2026-07-14 (first planting object: `TREE_06_existing_neem_trunk`/`_canopy`, real position/height/canopy-diameter from team_00's on-site observation — see `SITE_GEO.yaml` `tree_6_update_2026-07-14`). Applies to all existing/preserved site trees modeled going forward; new-design planting may warrant its own sub-convention later (not yet needed). |

## Still open (not yet defined — ask before assuming)

- Boundary-corner markers (the `BOUNDARY_*` empties themselves, as opposed to their text labels)
- North arrow geometry (as opposed to its label, already covered above)
- Future modeled elements: tire fence, rockery/terracing, pool
- New-design planting (as opposed to existing/preserved trees, now covered above) — may need its own palette once S002/S003 planting plan exists

## Applying this in Blender

Each category = one shared Blender material (not per-object duplicates), so a future palette change is a
one-line edit propagating everywhere. Material names follow `MAT_<category-slug>` (e.g. `MAT_house_concrete`,
`MAT_walls_fences_light_gray`, `MAT_labels_glow_yellow`) for easy lookup.

## Cross-references

- `blender/CURRENT_MODEL.md` — which object groups currently map to which category (may shift as the model
  is refined — check there for the current live object-name mapping, not just this canon's category list)
- `design/CANONICAL/07_DRAWING_SET_and_RENDER_MANIFEST.md` — render/drawing conventions this feeds into
- `design/CANONICAL/BLENDER_MODELING_TEAM_CHARTER_v1.0.0.md` — general modeling discipline
