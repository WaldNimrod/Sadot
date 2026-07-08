---
id: HANDOFF_TO_NEXT_team_110_SADOT_BUILDOUT_2026-07-08_v1.0.0
type: HANDOFF (aos_handoff) — domain build-out, FULL execution authority (ADR045)
from: team_120 (Ambassador — laid the infrastructure) under team_00
to: team_110 (Sadot Domain Architect + design lead — IR#14-specialized for landscape architecture)
cc: [team_00, team_100]
date: 2026-07-08
domain: sadot (landscape_architecture)
project_path: /Users/nimrod/Documents/AOS_V5/Sadot
---

# HANDOFF → team_110 (Sadot) — own the build-out: roadmap + research + complete the environment & knowledge bases

**team_120 laid the infrastructure; you execute the domain.** You have **full execution authority (ADR045)** for the
Sadot domain: spawn team_10 (Blender/3D build), team_70 (Librarian — the design dossier), team_80 (research), team_90
(cross-engine validate); refine + drive the roadmap; complete the environment. **Scope reminder:** team_120 does NOT do
the research or the design — you and your teams do.

## A. Current state (Phase 1 — DONE by team_120, verified)
- Sadot L0 project created, registered in the hub `_aos/projects.yaml`, Model-B applied, git-committed, **validate_aos
  → 46 PASS / 0 FAIL**. Design lead = **team_110** (you), IR#14-specialized for landscape architecture.
- **Archetype:** `LANDSCAPE_DESIGN` — a NEW sub-archetype that **inherits + extends `3D_CREATIVE`** (inherits its 3D-model
  + human-visual-approval-gate lifecycle; extends with a horticulture/soil/permaculture/planting knowledge domain).
  Currently the roadmap carries `3D_CREATIVE` as the base until the sub-archetype is registered (see C.5).
- **raw-materials/ ingest is LIVE** (git-ignored, Drive-syncable): `raw-materials/from-client/` (materials FROM Niv Sadot),
  `to-client/` (submissions), `working/`. Client materials land here; you curate the subset into `knowledge/`+`design/`.
  See `_aos/context/RAW_MATERIALS.md`. Read `_aos/context/PROJECT_CONTEXT.md` first.
- Full design + decisions: the team_00-approved plan (`~/.claude/plans/shimmying-jumping-mango.md`) — the "vNext
  new-project procedure + Specialization phase"; Sadot is its exemplar.

## B. Your mandate — three streams
### B.1 ROADMAP — precisely define + implement
Refine `_aos/roadmap.yaml` + `_aos/MILESTONE_MAP.md` into the real landscape-project WP structure, e.g.:
`S001` site analysis + client brief → `S002` concept design → `S003` detailed design (planting plan + hardscape +
site-anchored 3D model) → `S004` design dossier + BOQ + client submissions. Create the WPs (`_aos/work_packages/<WP-ID>/`).
Classify each: **RESEARCH** (investigations), **CONTENT/CONTENT_SUBSTRATE** (dossier/plans), 3D_CREATIVE (the model).

### B.2 RESEARCH — the domain investigation (RESEARCH track → team_80; team_00/you decide)
Site/plot analysis (Niv Sadot's plot in Pardes Hanna — from `raw-materials/from-client/` survey once populated),
Israeli climate + soil for the site, plant selection (drive from the SMA crop KB — see C.6), permaculture/ecological
design principles (build the structured KB — none exists yet, see C.7), precedents.

### B.3 COMPLETE THE ENVIRONMENT + KNOWLEDGE BASES (Phase 2 — Specialization)
Harvest the reusables below into Sadot, build the KB, specialize the teams, emit the training plan.

## C. Harvest map (exact paths — copy/adapt into Sadot; retain provenance headers)
1. **Architectural drawing canon + pipeline** (highest-fit) — from
   `/Users/nimrod/Documents/AOS_V5/IsraelMicrogreens-BlenderV2-Project/docs/ARCHITECTURAL_DRAWING_CANON/` (follow its own
   `08_REPLICATION_GUIDE.md`) + `scripts/drawing/` (model→ortho→SVG→dimensioned-PDF) + `WP_PHASE5_TECHNICAL_DOCS/lib/*`.
   → into Sadot `design/`. Adapt terminology to landscape (planting plan, hardscape sections).
2. **Design-dossier SSOT skeleton** — microgreens `CANONICAL/` 10-doc set (spatial-SSOT / parts(plants)-register / BOQ /
   contractor-package / drawing-set / agricultural(planting)-plan / timeline + conflict law "register drives model").
   → Sadot `design/CANONICAL/`.
3. **Israeli georeferencing + site scripts** — microgreens `lib/geo_itm.py` (WGS84→Israeli-TM EPSG:2039) + `site_geo_anchor.py`
   / `phase4_site_exterior_pass.py` / `measure_site_path.py`. → anchor Niv Sadot's real plot at true scale in Blender.
4. **Blender MCP loop + versioning** — `blender/CURRENT_MODEL.md` pointer convention, `scripts/inspect/session_mcp_verify.py`
   (port 9876), `mcp__blender__*` asset gen (PolyHaven/Sketchfab/Hyper3D) for plants/props/textures. → Sadot `blender/`.
5. **Client hub** — spec `SmallFarmsAgents/docs/CLIENT_HUB_STANDARD_v1.md` (+ replication checklist §7); clone
   `EyalAmit.co.il-2026/hub/` → Sadot `hub/`, rename `eyal-*`→`sadot-*`; wire decisions / meeting-brief / `what-we-need` /
   materials-intake for Niv Sadot.
6. **Crop/climate KB** — `SmallFarmsAgents/data/external_sources/` (Israeli planting calendars, variety encyclopedia w/
   frost/cold-resistance, spacing/yields) + `organic_market_agent/crop_book/` (`planting_calendar.py`, `companion_matrix.py`,
   `cover_crops.py`) + the `035–040_crop_book_*` schema (already supports perennials + fruit_trees). → Sadot plant-selection engine.
7. **Permaculture/ecological authority** — `nimrod-book/chapters/11_ERA_GARDEN_*` (PDC/Havat-Adam credentials, methodologies) +
   systems-design principles + `nimrod-bio` soil/garden/greenhouse. NOTE: **no structured zones/sectors/guilds/swales KB exists —
   you must BUILD it** (structure + author). This is a core research+authoring task.

## C-cont. Build these (Phase 2 deliverables)
- **`knowledge/` KB tree + `knowledge/INDEX.md`** on the microgreens `data/context/INDEX.md` pattern (reading-order-by-task
  table + "what is NOT here" pointers + key-facts quick-ref). Ingest seed materials from `raw-materials/from-client/`.
- **`_aos/teams.yaml`** — specialize team_110 (landscape design lead) + the Sadot roster: per-team `engine`, `write_paths`,
  `iron_rules`, and **`mandatory_reads` (≤4 per team, after PROJECT_CONTEXT)** pointing into `knowledge/`. Pattern: `nimrod-book/_aos/teams.yaml`.
- **`SADOT_DOMAIN_RULES_CANON`** — from `lean-kit/modules/standards-conventions/templates/DOMAIN_RULES_TEMPLATE.md` + the IR#14
  set (interaction protocol / glossary / stage model). Sanction path: **`DOMAIN_PROTOCOL_PROPOSAL` → `_COMMUNICATION/team_100/`
  → team_100 conflict-check → team_00 sign-off** (IR#14 / AOS_CONCEPT_AND_PRINCIPLES §Iron Rules #8).
- **`LANDSCAPE_DESIGN` archetype** — draft the `inherits: 3D_CREATIVE` + `extends:` (horticulture/soil/permaculture knowledge +
  any gate delta); route to team_100 to author the hub canon (`methodology/lifecycle-archetypes/`) — it is hub canon (IR#11),
  you PROPOSE, team_100 authors. Then flip Sadot's `roadmap.yaml` `lifecycle_archetype: 3D_CREATIVE` → `LANDSCAPE_DESIGN`.
- **Training/onboarding plan** — the 6-artifact composition (identity onboarding + mandatory_reads + `_aos/context/ACTIVATION_*` +
  the IR#14 specialization docs + the `knowledge/` KB + startup/gate discipline). Emit as `_aos/context/TRAINING_PLAN.md`.

## D. Constraints + return
- Cross-engine validation at the decisive gate (IR#1); keep `validate_aos.sh` at **0 FAIL** after each change.
- IR#11: never hand-edit the `_aos/{governance,methodology,lean-kit}` cache (hub-sync only); domain work lives in
  `design/`, `knowledge/`, `hub/`, `blender/`, `_COMMUNICATION/team_*/`, and the tracked `_aos/` project files.
- **Return:** a refined roadmap + created WPs + the completed environment (KB + teams.yaml + domain rules + training plan) +
  a COMPLETION/STATUS report → team_120 + team_00. Findings/gaps that improve the vNext procedure → flag to team_120 (they
  feed the L2 command-fix WP).

## Activation — ── Copy this block ──
```
אתה team_110 — האדריכל/מוביל התכנון של דומיין Sadot (אדריכלות נוף, לקוח ניב שדות, פרדס חנה). סמכות ביצוע מלאה (ADR045).
טען זהות: aos_actor team_110. עבוד בתוך /Users/nimrod/Documents/AOS_V5/Sadot. קרא קודם _aos/context/PROJECT_CONTEXT.md +
ההנדאוף המלא _COMMUNICATION/team_110/HANDOFF_TO_NEXT_team_110_SADOT_BUILDOUT_2026-07-08_v1.0.0.md.
מנדט (3 זרמים): (1) מפת דרכים — דייק ובנה את _aos/roadmap.yaml + MILESTONE_MAP ל-WPים אמיתיים (S001 ניתוח אתר+בריף →
S002 קונספט → S003 תכנון מפורט: תכנית נטיעה+חומרי גמר+מודל 3D → S004 תיק תכנון+כתב כמויות+הגשות ללקוח). (2) מחקר (מסלול
RESEARCH, team_80) — ניתוח מגרש, אקלים/קרקע ישראל, בחירת צמחייה (ממאגר SMA), עקרונות פרמקלצר. (3) השלמת הסביבה ובסיסי
הידע — קצור את 6 המקורות לפי מפת ה-harvest (microgreens drawing-canon+Blender+geo / SMA crop KB / clone hub של EyalAmit
→ sadot-* / nimrod-book+bio), בנה את knowledge/INDEX, הקם _aos/teams.yaml (התמחות + mandatory_reads≤4), נסח
SADOT_DOMAIN_RULES_CANON (DOMAIN_PROTOCOL_PROPOSAL→team_100→team_00), הצע ל-team_100 את ארכיטייפ LANDSCAPE_DESIGN
(יורש 3D_CREATIVE), והפק תכנית הכשרה. אילוצים: cross-engine בשער המכריע; validate_aos ב-0 FAIL; אל תיגע ב-cache של
_aos/{governance,methodology,lean-kit}. חומרי גלם נכנסים ב-raw-materials/from-client/. החזר COMPLETION + ממצאים
שמשפרים את נוהל ה-vNext → team_120. ספq/החלטות עקרוניות → team_00.
```
## ── סוף הבלוק ──

— aos_handoff issued by team_120 under team_00 · 2026-07-08 · full domain authority to team_110 · return → team_120 + team_00
