---
id: TREE_KEY_LEGEND_v1.0.0
type: canonical reference (team_00 instruction, 2026-07-14: "לכל עץ להוסיף מספר שיופיע בתעוד וגם במודל
  בצבע + לייצר רשימת מפתח עצים - כל מספר איזה עץ זה בדיוק" — add a number to every tree that appears in
  the documentation and in the model in color, and produce a tree key list — which number is exactly
  which tree)
from: team_110
to: whoever works on the Sadot Blender model, planting plan, or reads a tree number in a render/drawing
date: 2026-07-14
status: DRAFT — 2 trees modeled so far. Add a row here BEFORE modeling any future tree, matching the
  discipline already used for the boundary/geometry canon.
---

# Tree Key / Legend — Sadot

**Read this before trusting any bare "tree N" reference anywhere in this project — spoken, written, or in a
future PDF/render.** There are **two separate, non-interchangeable tree-numbering schemes** in play. The same
number ("3", for instance) means a completely different tree depending on which scheme it's from. This file
is the single place that disambiguates both.

## ⚠ The two schemes

| Scheme | Source | Where recorded | Used for |
|---|---|---|---|
| **Survey schedule** | The 2023 licensed survey's own לוח עצים (tree schedule) table, `raw-materials/from-client/10111TD122 (1).pdf` | `blender/data/site/SITE_GEO.yaml` → `existing_trees.table`, numbered 1–14 (skips 11) | Tree **#6** (Neem) below |
| **Site-plan sheet** | Michal's combined site-siting sheet's own tree symbols, `raw-materials/from-client/שטח ובית.pdf` | `blender/data/site/SITE_GEO.yaml` → `siteplan_trees` (separate section) | Tree **#3** (olive) below |

These were confirmed genuinely distinct on 2026-07-14: the survey schedule's own entry #3 is a generic
"עץ" at 3.00m — not the 2m olive team_00 identified as "tree 3" on the site plan. Don't assume a bare number
matches one scheme just because it matches the other project's convention elsewhere.

## Modeled trees (as of 2026-07-14)

| In-model number label | Scheme | Species | Real data source | Blender object(s) | Notes |
|---|---|---|---|---|---|
| **6** | Survey schedule | Neem (עץ ניר הודי, *Azadirachta indica*) — **working ID, not confirmed** | team_00 direct observation, relayed via `_COMMUNICATION/team_110/MSG_team_120_TO_team_110_TREE6_SPECIES_ID_2026-07-14_v1.0.0.md`. Height 4.00m as-observed (survey recorded 5.00m in 2023 — discrepancy on record, not resolved). Canopy 2.00m diameter. | `TREE_06_existing_neem_trunk` (canopy object no longer exists as of this writing — see caveat below) | **Geometry currently incomplete/uncertain**: the canopy object was deleted and the trunk repositioned/rescaled during live-session editing after this tree was first built; not yet reconciled. The number label position is a best-effort placement above whatever the trunk object's current top is — do not treat tree #6's current on-screen shape as confirmed-correct the way tree #3's is. |
| **3** | Site-plan sheet | Olive (זית) | team_00 direct observation, 2026-07-14. Height 2.00m. Canopy/trunk diameter not given — Blender object uses assumed placeholder proportions, flagged as such (not surveyed). | `TREE_siteplan03_existing_olive_canopy` (trunk+canopy joined into one object by team_00, 2026-07-14 — the name is a holdover from before the join, not a claim that it's canopy-only) | Position set precisely twice: first via PDF-pixel 3-point affine extraction (0.000m residual), then manually refined and locked in by team_00 directly in the live session — **the current position is team_00's own placement, treat as correct.** |

## Not yet modeled

The survey schedule has 12 more trees (1–5, 7–10, 12–14) with real height/diameter data but no species ID
and no position extracted yet — see `SITE_GEO.yaml` → `existing_trees.table`. Any additional trees the
site-plan sheet shows are also not yet inventoried here. Do not assume "only 2 trees exist on site" — only 2
are modeled so far.

## Convention for adding the next tree

1. Determine which scheme the number belongs to (ask if team_00 doesn't say explicitly — this file exists
   because that ambiguity already caused one real mix-up).
2. Add a row to this table before or immediately after modeling it.
3. In Blender: a `MAT_labels_glow_yellow` FONT object, `size=0.6`, centered above the tree's own top,
   containing only the bare number (matches the boundary-corner label style) — named `TREE_<id>_number_label`,
   placed in the `Trees` collection alongside the tree's own mesh object(s).
4. Update the corresponding `SITE_GEO.yaml` section (`existing_trees.table` for survey-scheme trees,
   `siteplan_trees` for site-plan-scheme trees — do not merge the two sections).

## Cross-references

- `blender/data/site/SITE_GEO.yaml` — full technical data for both schemes
- `blender/CURRENT_MODEL.md` — passes 15/16 (tree #6, tree #3 build history)
- `design/CANONICAL/03_MASTER_PARTS_REGISTER.md` §G — parts-register rows for both trees
- `design/CANONICAL/COLOR_CODING_CANON_v1.0.0.md` — planting material/color convention
