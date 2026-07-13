---
id: BLENDER_MODELING_TEAM_CHARTER_v1.0.0
type: team mandate (team_00 instruction, 2026-07-13: "לנעול את תפקידכם בזיכרות הפרויקט שלנו ולחייב דיוק
  אדריכלי ומרחבי מירבי" — lock this role into the project's memory, require maximum architectural/spatial
  precision)
from: team_110
to: whoever next opens blender/ for this project (team_10/sadot_build, or any future session)
date: 2026-07-13
status: MANDATORY READING before touching any placement, rotation, or elevation in the Sadot Blender model
---

# Blender Modeling Team Charter — Sadot

## 0. What this project's 3D model is actually for

This is **landscape architecture**, not generic visualization. The Blender model's entire purpose is to be
**true spatial ground truth**: where the house really sits on the real plot, which way it really faces, what
the real elevations are. Every downstream design decision — where the pool can go, setback compliance, sun/
shade studies, sightlines, planting placement, how much fill the terrain needs — is only as good as this
ground truth. A wrong house position or a 90°-off rotation doesn't just look bad in a render; it silently
poisons every design decision built on top of it. **Precision here is not cosmetic. Treat every placement
claim as a real engineering claim, not a modeling nicety.**

## 1. Tools actually available in this environment

- **Blender MCP** (`mcp__blender__execute_blender_code`, `get_viewport_screenshot`, `get_scene_info`,
  `get_object_info`) — talks to a **live GUI Blender session**, not headless. Team_00 is often watching the
  same window in real time. Changes you script are real changes to their session.
- **ifcopenshell** — installed under `/Library/Developer/CommandLineTools/usr/bin/python3`, NOT the default
  `python3` on PATH (that one lacks it; check with `python3 -c "import ifcopenshell"` first and fall back to
  the CommandLineTools path if it fails).
- **PyMuPDF (`fitz`) / pdfplumber** — for extracting real vector data (text positions, stroke paths/colors)
  directly from client PDFs, when raster/pixel reading isn't precise enough. `pdftoppm` (poppler) for
  high-DPI raster rendering when a visual read is all that's needed.
- **Raw materials**: `raw-materials/from-client/` (git-ignored, real client files) is the actual source of
  truth — the licensed survey PDF, the architect's IFC exports, site-siting sheets. Read these directly; don't
  work from summaries of them once the real files exist.

## 2. Hard-won precision lessons — read before repeating any of these mistakes

This project has made and caught the following errors, in this order, within real sessions. Each one looked
plausible at the time it was made.

1. **A visually-matched wall-to-boundary-edge rotation (105.28°) was wrong**, discovered only because the
   client stated a real-world fact ("the deck faces roughly south") that contradicted it. The rigorous fix was
   to walk the IFC's own `IfcLocalPlacement` hierarchy directly via **3 independent methods** (raw STEP
   `Axis`/`RefDirection`, composed 4×4 matrix decomposition, independent PCA on actual world-coordinate
   geometry) — not to eyeball a better-looking wall match. **Rule: never trust a single heuristic geometric
   match for anything that matters. Cross-check at least 2 independent ways.**
2. **A rigid-shift script that filters objects by name prefix (`walls_`/`doors_`/`windows_`) silently missed
   an object that had been renamed** to something else (a Hebrew descriptive name) earlier in the project.
   It sat un-shifted while 140 others moved. **Rule: to reliably enumerate "every object in a group,"
   filter by something that survives renames — mesh-data name (`obj.data.name`), not `obj.name`.**
3. **Matching axis-aligned bounding-box centers is not the same as being inside a real (non-rectangular)
   polygon.** This plot is a rotated, narrow hexagon; its bbox is much bigger than its true area (normal for
   any tilted shape). A bbox-center match can land a point inside the box but outside the actual plot.
   **Rule: use a real point-in-polygon test (ray-casting against the actual boundary vertices) for any
   "is this inside the plot" question. Never substitute a bounding-box check.**
4. **A distance-from-median clustering step mistook the far end of one real, genuinely elongated building
   for a separate structure**, then repositioned only the "near" part — which looks, and is, visibly broken.
   **Rule: before treating a spatially-distant group of objects as "a separate structure" (garden wall, shed,
   etc.), check it against the real reference document (the architect's site plan). A real house on a narrow
   50m+ lot can legitimately span most of that length — spatial distance alone does not mean "different
   structure."**
5. **A scripted change to a live GUI Blender session does not always visually refresh** on its own. If
   team_00 reports "I don't see a change" and your own data checks say otherwise, force it: `tag_redraw()` on
   every area in every screen, plus `bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)`, and
   explicitly reframe the specific viewport (`view3d.view_all()` via `temp_override`) — object positions
   changing does not move an already-framed camera to follow them.
6. **Client/architect-stated facts about real geometry outrank anything you derive computationally.** When
   team_00 gives a concrete anchor fact (e.g., "the south plot line and the south fence line sit exactly on
   top of each other," "use the SW corner as the anchor point and rotation axis," "the west wall runs almost
   parallel to the west boundary") — that is real, higher-confidence ground truth. Use it directly. Don't
   re-derive an equivalent-but-uncertain version from raw geometry when a direct stated fact is available.

Full narrative with numbers for all of the above: `blender/CURRENT_MODEL.md`, "Origin convention" section —
required reading before touching placement/rotation again, not just this summary.

## 3. Working method (apply every time, not just when something looks wrong)

1. State the specific geometric claim you're about to make (position, rotation, elevation) and what evidence
   it rests on, before writing it to the file.
2. Verify it at least 2 independent ways (a numeric check AND a visual screenshot at minimum; a true
   point-in-polygon test where boundary-containment is the question).
3. Take a real screenshot after every meaningful placement change — top orthographic (Numpad 7 equivalent,
   `view3d.view_axis(type='TOP')`) for boundary/position questions, since perspective distorts apparent
   angles, especially for thin/elongated shapes.
4. Work on a **new copy** of the model file for any exploratory or uncertain change — never overwrite the
   last-known-good file in place. Bump the filename (`sadot_vN_description_YYYY-MM-DD.blend`) and update
   `blender/CURRENT_MODEL.md`'s `LIVE =` pointer only once verified.
5. Document what was found wrong and how it was fixed, even (especially) when it was your own error — this
   project's established norm is to preserve the record of mistakes, not silently overwrite them (see the
   `_RETRACTED` sections already in `blender/data/site/SITE_GEO.yaml`).
6. When uncertain, say so plainly and stop rather than presenting a guess with more confidence than it earned.

## Cross-references

- `blender/CURRENT_MODEL.md` — the live pointer + full placement history (read this every session before
  touching the model)
- `blender/data/site/SITE_GEO.yaml` — technical SSOT for all site-geometry facts
- `design/CANONICAL/SITE_HOUSE_TIE_ANALYSIS_2026-07-13_v1.0.0.md` — the site-tie analysis this charter grew out of
- `design/CANONICAL/BLENDER_SHELL_BUILD_PLAN_v1.0.0.md` — the build-sequence plan
