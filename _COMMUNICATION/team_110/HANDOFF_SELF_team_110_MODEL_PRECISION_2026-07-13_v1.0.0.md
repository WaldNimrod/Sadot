---
id: HANDOFF_SELF_team_110_MODEL_PRECISION_2026-07-13_v1.0.0
type: session handoff (team_00 instruction, 2026-07-14: "/AOS_handoff 110 full" — session-to-session
  continuation, same team/role, for whoever continues the Blender model-precision process)
from: team_110 (this session)
to: team_110 (next session)
date: 2026-07-14
note: The live hub API (GET /api/prompts/generate?mode=handoff) returned 200 but a generic, context-empty
  template (team/project details "unavailable", no governance file found for "110", assumed project
  "agents-os") — the hub's live generator has no registered Sadot-specific context for this team. This file
  is the REAL handoff content, authored directly, per team_00's explicit requirement to include references to
  the actual Blender precision work and role procedures — do not rely on the generic API template alone.
---

# Session Handoff — team_110, Sadot Blender Model-Precision Track

## 1. MANDATORY READS — in this order, before touching the model

1. **`design/CANONICAL/BLENDER_MODELING_TEAM_CHARTER_v1.0.0.md`** — the team mandate: why precision matters
   here (landscape-architecture ground truth, not decoration), the tools (Blender MCP is a LIVE GUI session
   team_00 may be watching in real time; ifcopenshell lives at
   `/Library/Developer/CommandLineTools/usr/bin/python3`, not the default `python3`), and 6 specific mistakes
   this project already made and fixed — read these before repeating any of them.
2. **`blender/CURRENT_MODEL.md`** — the full placement history, pass by pass, including two retracted findings
   kept on record (never silently overwritten): a false 105.28° rotation hypothesis (pass 2), and a
   subsequently-*also-wrong* "0°, rigorously confirmed" finding (pass 3) that was real but answered a
   narrower question than assumed (IFC-internal consistency, not IFC-to-real-ITM axis mapping). The ACTUAL
   rotation, team_00-verified by direct visual inspection against Michal's site plan, is ~-105.5° — notably
   close to the very first (retracted-for-a-different-reason) hypothesis.
3. **`design/CANONICAL/COLOR_CODING_CANON_v1.0.0.md`** — what every color in the scene means. Notably: the
   268-piece cluster (`MAT_house_concrete`) is the current/new house — in scope. The 29-piece cluster
   (`MAT_old_house_REFERENCE_ONLY`, dark gray, 25% transparent) is the OLD pre-existing house, reference only,
   NOT in scope — this was misidentified once already as "fences/walls," corrected same day.
4. **`blender/data/site/SITE_GEO.yaml`** — technical SSOT: real survey boundary (`boundary_itm`, 6 points),
   the precise Z anchor (`z_anchor_precise_2026-07-14`: deck=55.97m real, south-edge=54.5m real, diff=1.47m
   exact, iron rule: finished ground never exceeds 55.97m), the front-section grading calc (16.3% average
   slope — supports terracing, not a uniform grade), and the rotation reconsideration note.
5. **`design/CANONICAL/SITE_HOUSE_TIE_ANALYSIS_2026-07-13_v1.0.0.md`** — how the real terrain surface was
   extracted directly from the architect's IFC (`IfcSite` named "Surface:5849516", 116 real verts) and the
   PDF/IFC cross-analysis that led here.

## 2. LIVE file

**`blender/sadot_v3_site_tie_2026-07-14.blend`** — do not confuse with `sadot_v1_initial.blend` (superseded)
or `sadot_v2_initial.blend` (stray, never adopted — see `CURRENT_MODEL.md`). Work on a NEW copy for anything
exploratory, per the charter.

## 3. What this session accomplished (chronological, same day 2026-07-13→14)

- Received + examined new client materials (`שטח ובית.pdf`, updated IFC) — found the IFC's `IfcSite` carries
  a real modeled terrain surface, not just placement metadata.
- Attempted rigorous rotation re-derivation (multiple methods) — all inconclusive/contradictory on their own.
- team_00 manually positioned the house directly in Blender and **was right**: long axis now runs along the
  plot's long axis, matching the real site plan. This is now the trusted position — not yet independently
  re-derived computationally (see Open Items).
- Z anchored precisely: deck=55.97m, south-edge=54.5m, diff=1.47m exact, iron rule recorded.
- Grading calculated: 9.00m run, 16.3% average slope — flagged as too steep for a uniform grade, supports the
  planned kurkar/basalt terracing.
- Color-coding canon created and applied (house/old-house-reference/labels/terrain/roof/decking).
- Flat single roof was tried, **rejected by team_00 as lazy** — rebuilt as ~7 per-room/section roof pieces,
  each at its own contour and height (clustered by wall proximity + height similarity), open deck excluded.
- Wood decking added: 15cm layer on the concrete deck (55.97m → 56.12m finished surface).
- Two wall-height precision fixes: south-edge wall bottom set to exactly 54.50m; west-side wall bottom
  extended to follow real interpolated ground height along its length (top unchanged).
- All committed to git (`b491f7f`, `a737b5f`).

## 4. FIRST TASK — DONE, same session (team_00 instruction, 2026-07-14)

**UPDATE: this was completed in the handoff-writing session itself, not left for the next one.**
`REF_PDF_shetach_uvayit` exists in the scene (hidden, per instruction) — a textured plane built from the
200 DPI render of `שטח ובית.pdf`, registered via a 2-point similarity transform (4G/5G correspondences,
computed rotation 2.255°, scale 0.006341 world-units/pixel). Verified visually: the plot's blue boundary line
in the image tracks the terrain's own boundary outline closely. Small residual offset expected (only 2
control points, ordinary pixel-picking precision) — if a future session wants tighter registration, add a
3rd control point (e.g. 1G or 3G) and refit. To use it: `bpy.data.objects["REF_PDF_shetach_uvayit"].hide_set(False)`.

Original question, answered: **yes, it can, and now is.**

If yes: position it precisely so the **blue plot-boundary line drawn in the PDF** lands exactly on our own
plot boundary markers in the scene (`BOUNDARY_1G`...`BOUNDARY_6G`). Goal: once precisely registered in real
3D space, the PDF's other content (dimensions, tree positions, elevation call-outs, room labels) becomes a
reliable visual reference for extracting more precise points to complete other objects. **The PDF must stay
in the scene, hidden, for future use** — not deleted after use.

**What's already available to do this precisely, from this session's own work:**
- `blender/data/site/SITE_GEO.yaml` — real ITM coordinates for boundary corners 1G-6G, and the confirmed
  match between this PDF and the survey (3 independent edge-length matches: 52.80m/10.10m/15.25m).
- Precise pixel positions for corners 4G and 5G were already found in a 200-DPI render of this same PDF
  during this session's analysis (see `design/CANONICAL/SITE_HOUSE_TIE_ANALYSIS_2026-07-13_v1.0.0.md` §1) —
  reuse these rather than re-deriving from scratch: 4G ≈ pixel (975, 9130), 5G ≈ pixel (625, 1670) in a
  200 DPI render of the PDF's single A0 page. Real ITM: 4G=(196684.489, 707813.303), 5G=(196680.410,
  707860.480). These give 2 point-correspondences — enough for a similarity transform (rotation+scale+
  translation); remember the image Y-axis is inverted relative to world Y (north-up).
- The rendered PNG may already exist in a prior session's scratchpad — check before re-rendering the PDF.

## 5. Open items / not yet resolved

- **Rotation/position: team_00-verified by inspection, not yet independently re-derived computationally.**
  If time allows, this would meet the project's own "cross-check at least 2 ways" standard — but do NOT
  treat this as blocking; team_00's direct verification is real evidence.
- No formal soil lab test; no rigorous multi-date/multi-hour sun-path model (flagged critical for S002,
  blocked on this same position now being settled — may be unblocked, worth checking).
- Roof/decking/old-house colors are placeholders, not yet client-confirmed final.
- `_COMMUNICATION/team_100/PORT_REGISTRATION_PROPOSAL_SADOT_HUB_v1.0.0.md` and the team_120 port-canon
  process-gap report are still awaiting a hub-side response.
- Task #20 (Gantt/roadmap draft) from the earlier task list is still pending — not touched this session.

## 6. Role procedure reminder

Per `_aos/context/ACTIVATION_BUILDER.md` (now points to the charter above as required reading): cross-engine
rule, `validate_aos.sh` before declaring build-gate pass, never fabricate plot-specific geometry without real
source data, raise spec ambiguities rather than silently drifting.
