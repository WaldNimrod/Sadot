---
id: PLAN_SADOT_BUILDOUT_ROADMAP_RESEARCH_ENV_v1.0.0
type: execution plan (approved 2026-07-08, executed same session — persisted here so it is a real repo
  artifact, not only a local Claude Code plan-mode file)
from: team_110
to: team_00 / team_100 (repo-visible reference for any future session, including a team_100 parallel channel)
date: 2026-07-08 (authored) / 2026-07-10 (persisted to repo)
note: This is a verbatim persistence of the plan team_00 approved via Claude Code's plan-mode UI. It
  originally existed only as a local Claude Code artifact at `~/.claude/plans/team-110-curried-book.md`
  on this Mac — NOT git-tracked, NOT part of `_COMMUNICATION/` or `_aos/`, and therefore invisible to any
  other session (including a team_100 session) unless persisted here. Saved verbatim, no content changes.
---

# PLAN — team_110 Sadot build-out: roadmap + research + environment/KB completion

## Context

team_120 finished Phase 1 (L0 scaffold, Model-B governance cache, `validate_aos.sh` 46 PASS/0 FAIL) and Phase 2 infra
staging, then handed off full execution authority (ADR045) to **team_110** — this session — via
[HANDOFF_TO_NEXT_team_110...md](file:///Users/nimrod/Documents/AOS_V5/Sadot/_COMMUNICATION/team_110/HANDOFF_TO_NEXT_team_110_SADOT_BUILDOUT_2026-07-08_v1.0.0.md).
The prior team_00-approved design ([shimmying-jumping-mango.md](file:///Users/nimrod/.claude/plans/shimmying-jumping-mango.md))
already fixed the *intent*: Sadot is the exemplar for a new "Specialization phase" in AOS project creation. My job now is
to **execute** that intent as team_110 (Domain Architect, full execution authority): turn `_aos/roadmap.yaml` into a real
WP structure, drive the RESEARCH track, and finish harvesting/building the environment + knowledge base team_120 started.

**Two hard constraints discovered during exploration that shape the plan:**
1. `raw-materials/from-client/` is **empty** — Niv Sadot has not yet sent a plot survey. Anything requiring real
   plot-specific data (topography, soil test, sun/shade) is genuinely **BLOCKED**, not just deprioritized.
2. There is **no existing mechanism for archetype inheritance** anywhere in AOS — `LANDSCAPE_DESIGN inherits
   3D_CREATIVE` is a brand-new hub-layer concept I'm introducing, not a template I'm filling in. It must be **proposed**
   to team_100 (who authors hub canon per Iron Rule #11), not built unilaterally.

Everything below reflects direct exploration of the Sadot repo + the 6 harvest sources, plus two independent design
passes (WP/roadmap structure; archetype-inheritance mechanism). Baseline: `validate_aos.sh` currently reports
**46 PASS / 30 SKIP / 0 FAIL** — the target after this work is still 0 FAIL.

---

## Decision log (architect-level calls made during planning, not re-litigated with team_00)

- **S001 is broadened, not replaced with a new S000.** The current `MILESTONE_MAP.md` S001 row ("Initial domain research
  and environment bootstrap") has **zero WPs ever registered against it** (`_aos/work_packages/` doesn't exist yet), so
  redefining its description costs nothing and avoids inventing a non-canonical S000. New S001 description: *"Environment
  completion, domain research, and site analysis + client brief."*
- **WP `id:` fields get an `SDT-` prefix** (e.g. `SDT-S001-P001-WP001`) because `work_packages.id` is a **global** primary
  key in the hub DB — plain `S001-P001-WP001` triples have already collided across other spokes (see
  `agents-os/_COMMUNICATION/team_100/RISK_SUMMARY_DUAL_SPOKE_WP_ID_COLLISIONS_v1.0.3.md`). Directories under
  `_aos/work_packages/` and all internal cross-refs stay unprefixed (`S001-P001-WP001/`) — only the hub-synced `id:`
  field carries the prefix. Documented inline in `roadmap.yaml`.
- **Track classification per WP** (not a native roadmap.yaml field yet — tagged via `notes:` until team_100 canonizes
  one): **RESEARCH** (team_80, ADR044 Track 4 — advisory, no gate, no LOD chain) vs **CONTENT** (team_70 Librarian,
  light LOD100/400/500) vs **3D_CREATIVE** (team_10 Blender build, full Stage 0-7 gate chain). Builder/validator engines
  per `_aos/team_assignments.yaml`: team_10/sadot_build = cursor-composer, team_90/sadot_val = openai, team_70 = codex —
  cross-engine (Iron Rule #1) satisfied at every gated WP.
- **The archetype-inheritance ask is filed as ONE bundled `GOVERNANCE_CHANGE_REQUEST`**, not a lighter
  `DOMAIN_PROTOCOL_PROPOSAL` — because it changes the hub-canon PLA *schema* itself (a new `inherits_from` field +
  composition rule), which is hub-authored territory for every future project, not a Sadot-local override. The
  `lifecycle_archetype: 3D_CREATIVE → LANDSCAPE_DESIGN` flip itself is a separate, later, pure structured-data mutation
  (Iron Rule #7) — not part of the GCR.
- **The permaculture KB (`knowledge/permaculture/`) is authored from scratch**, not harvested — confirmed no
  zones/sectors/guilds/swales structure exists in `nimrod-book` or `nimrod-bio` (both are biographical/marketing
  content, not a technical corpus). I will author it using standard, publicly-established permaculture design
  methodology (Mollison/Holmgren zone-and-sector analysis, guilds, swales), anchored to Nimrod's real credentials (PDC
  2014 @ Solar Garden Binyamina, Havat Adam ecological-agriculture study, the biochar project) cited as authority, not
  claimed as extracted proprietary content.
- **Hub-cloning rule:** when cloning `EyalAmit.co.il-2026/hub/` into Sadot's `hub/`, copy the **code/template/build-script
  structure only** (data schema shape, CSS/JS, the 6 relevant views: decisions/tasks, roadmap, updates, meeting-brief,
  what-we-need, materials-intake). **Never copy Eyal Amit's actual client data/content** (his `decisions.json` entries,
  testimonials, meeting notes) — Sadot's data files start empty/fresh for Niv Sadot. Skip the WordPress-migration-only
  views (site-tree, media-intake, content-proposals, legacy-unmapped, testimonials, analytics-config) — not relevant to
  a garden-design engagement.
- **`SADOT_DOMAIN_RULES_CANON` ultimately lives at the hub path** `lean-kit/modules/project-governance/
  SADOT_DOMAIN_RULES_CANON_v1.0.0.md` (mirroring the real TT_DOMAIN_RULES_CANON precedent), even though I (team_110)
  author the draft content — same source→snapshot flow (IR#11) as the archetype PLA: I propose, team_100 commits to hub,
  it propagates back to Sadot's `_aos/lean-kit/` cache.

---

## Stream 1 — Roadmap (`_aos/roadmap.yaml` + `MILESTONE_MAP.md` + `_aos/work_packages/`)

### Milestones

| Stage | Description | Status |
|---|---|---|
| S001 | Environment completion, domain research, and site analysis + client brief | ACTIVE |
| S002 | Concept design (narrative + schematic massing) | PLANNED |
| S003 | Detailed design — planting plan, finish materials, site-anchored 3D model | PLANNED |
| S004 | Design dossier, BOQ, client submissions | PLANNED |

### S001 — 3 programs, register all WPs now (per WP_ID_STANDARD best practice: register at first identification)

**P001 — Environment/KB completion** (all NOW, this session):
1. Harvest drawing-canon + geo/Blender-MCP pipeline → `design/ARCHITECTURAL_DRAWING_CANON/`, `design/scripts/drawing/`,
   `design/lib/` (8 generic modules only — skip `rear_site_projection.py`, `boq_*`, tank-vendor files), `blender/lib/geo_itm.py`,
   `blender/scripts/site/` (`site_geo_anchor.py`, `phase4_site_exterior_pass.py`, `measure_site_path.py`),
   `blender/CURRENT_MODEL.md`, `blender/scripts/inspect/session_mcp_verify.py` (re-parameterized for Sadot's model name).
2. Harvest `design/CANONICAL/` 10-doc SSOT skeleton, renamed for landscape (e.g. `08_AGRICULTURAL_PLAN.md` →
   `08_LANDSCAPE_PLANTING_PLAN.md`); preserve the conflict law ("the register drives the model, never the reverse").
3. Harvest crop/climate KB substrate → `knowledge/crops/` (adapt `planting_calendar.py`/`companion_matrix.py`/
   `cover_crops.py` models + the `035-040` schema, which already supports `category='fruit_trees'`/`growth_cycle='perennial'`
   — no migration needed for basic reuse).
4. Clone client-hub skeleton → `hub/` (`eyal-*`→`sadot-*`, `D-EYAL-`→`D-SADOT-`, `EA-`→`NS-`, per the hard rule above).
5. Author `knowledge/permaculture/` KB from scratch (zones/sectors/guilds/swales) per the decision log above.
6. Build `knowledge/context/INDEX.md` (4-part pattern: reading-order-by-task table, files-in-folder table, "what is NOT
   here" pointers, key-facts quick-ref — mirrors `microgreens/data/context/INDEX.md`), `_aos/teams.yaml` (nimrod-book
   pattern: per-team engine override + write_paths + ≤7 iron_rules + mandatory_reads ≤4 + `validator_override` block),
   plus the 3 missing `_aos/context/ACTIVATION_{ARCH,BUILDER,VALIDATOR}.md` files (currently absent despite being listed
   as "Mandatory (all profiles)" in `_aos/README.md` — a real gap, fixed here).
7. Draft `SADOT_DOMAIN_RULES_CANON` + file the `DOMAIN_PROTOCOL_PROPOSAL` to `_COMMUNICATION/team_100/`; draft the
   `PLA_LANDSCAPE_DESIGN` archetype-inheritance content + file the bundled `GOVERNANCE_CHANGE_REQUEST` (see Stream 3).
   Emit `_aos/context/TRAINING_PLAN.md` (6-artifact composition per the approved vNext design).

**P002 — Research** (team_80, ADR044 Track 4 — advisory, no gate):
1. Israeli climate/soil — general (non-plot) research → `knowledge/`. **NOW.**
2. Plant-selection candidate list from the harvested crop/climate KB (general fit). **NOW.**
3. Permaculture/ecological design principles + precedents research (feeds item 5 above). **NOW.**
4. Plot-specific site analysis (topography, sun/shade, drainage, soil test, existing vegetation). **BLOCKED** — needs
   `raw-materials/from-client/` survey.

**P003 — Site analysis + client brief authoring** (team_70):
1. Client brief intake questionnaire/template. **NOW.**
2. Site-analysis dossier + formal client brief (synthesizes P002-WP004). **BLOCKED** — depends on P002-WP004.

### S002-S004 — register as PLANNED with `spec_ref: TBD`, not executed this pass (all BLOCKED on S001 output)

- **S002-P001:** concept narrative + precedent board (team_70); concept massing/site diagram, non-delegatable team_00
  concept sign-off (team_10 + team_90).
- **S003-P001..P003:** planting plan (team_70); finish-materials/hardscape spec (team_70); site-anchored 3D model —
  asset spec + build → render validation (mandatory team_00 visual sign-off, non-delegatable) → export → documentation/
  archive (team_10/team_90, full 3D_CREATIVE Stage 0-7 chain).
- **S004-P001:** design dossier compilation, BOQ, client submission package + hub delivery to `raw-materials/to-client/`
  (team_70/team_90).

### First documents to author

- `_aos/work_packages/S001/LOD300_milestone.md` — full S001 scope across all 3 programs, 1-line AC per WP, explicit
  dependency graph flagging the 2 BLOCKED WPs, the harvest map as a table, the RESEARCH-exemption note, pointer to the
  archetype-inheritance GCR in flight.
- Per-WP `LOD100_scope.md` for every S001 WP: problem/need, why-now-or-blocked, team assignment, `spec_ref: TBD` or the
  stage LOD300 pointer.

---

## Stream 2 — Research (team_80 track)

Executed directly in this session under the team_80 hat (informal, advisory, no gate — per its own governance contract:
"Activation requires explicit Team 00 instruction... deliver findings to architecture team, not implementation").
Findings land in `_COMMUNICATION/team_80/` and get folded into `knowledge/`:
- Israeli climate zones + soil types relevant to Pardes Hanna generally (coastal plain, Mediterranean climate, typical
  soil profile) — general, not plot-specific.
- Candidate plant/species shortlist pulled from the harvested SMA crop/climate KB, filtered for ornamental + food-garden
  fit in that climate band (the schema's `category='fruit_trees'`/`perennial` support makes this a real query, not a
  rebuild).
- Permaculture/ecological design principles + 2-3 relevant precedents (small private-garden scale, Israeli or
  Mediterranean-climate examples) — feeds the `knowledge/permaculture/` KB structure.
- Plot-specific analysis (topography/sun-shade/drainage/soil-test/existing vegetation) is explicitly logged as
  **BLOCKED pending client survey** — not attempted with placeholder data.

---

## Stream 3 — Environment + knowledge-base completion

### Harvest map (source → Sadot destination)

| # | Source | Destination |
|---|---|---|
| 1 | `IsraelMicrogreens-BlenderV2-Project/docs/ARCHITECTURAL_DRAWING_CANON/` (11 files, own `08_REPLICATION_GUIDE.md`) | `design/ARCHITECTURAL_DRAWING_CANON/` |
| 2 | `.../scripts/drawing/` (export_sheet_views→measure_sheet→compose_sheet pipeline) | `design/scripts/drawing/` |
| 3 | `.../_communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/` (8 generic modules) | `design/lib/` |
| 4 | `.../CANONICAL/` (10-doc SSOT skeleton + conflict law) | `design/CANONICAL/` (renamed for landscape) |
| 5 | `.../lib/geo_itm.py` (WGS84↔Israeli-TM EPSG:2039) | `blender/lib/geo_itm.py` |
| 6 | `.../scripts/assembly/site_geo_anchor.py`, `phase4_site_exterior_pass.py`, `scripts/inspect/measure_site_path.py` | `blender/scripts/site/` |
| 7 | `.../blender/CURRENT_MODEL.md` pointer convention | `blender/CURRENT_MODEL.md` |
| 8 | `.../scripts/inspect/session_mcp_verify.py` (MCP port 9876 check) | `blender/scripts/inspect/session_mcp_verify.py` |
| 9 | `.../data/context/INDEX.md` (pattern only) | `knowledge/context/INDEX.md` (new content, same 4-part structure) |
| 10 | `SmallFarmsAgents/organic_market_agent/crop_book/` (`planting_calendar.py`, `companion_matrix.py`, `cover_crops.py`, `035-040` schema) | `knowledge/crops/` |
| 11 | `SmallFarmsAgents/data/external_sources/` (Israeli planting calendars, variety encyclopedia) | `knowledge/crops/sources/` (citations, not the raw 40MB binaries) |
| 12 | `SmallFarmsAgents/docs/CLIENT_HUB_STANDARD_v1.md` §7 replication checklist | followed exactly for `hub/` |
| 13 | `EyalAmit.co.il-2026/hub/` (structure + build script only, per hard rule) | `hub/` (`sadot-*`) |
| 14 | `nimrod-book/chapters/11_ERA_GARDEN_2013_2023.md` + `nimrod-bio` (credentials/authority, not structure) | cited in `knowledge/permaculture/` |

### Governance/config artifacts to produce

- `knowledge/INDEX.md` — top-level KB index (links `context/`, `crops/`, `permaculture/`).
- `_aos/teams.yaml` — Sadot team specialization (pattern: `nimrod-book/_aos/teams.yaml`).
- `_aos/context/ACTIVATION_ARCH.md`, `ACTIVATION_BUILDER.md`, `ACTIVATION_VALIDATOR.md` — currently missing, filled in now.
- `_aos/context/TRAINING_PLAN.md` — the 6-artifact composition (identity onboarding + mandatory_reads≤4 + activation
  prompts + IR#14 domain-specialization docs + the KB + startup/gate discipline).
- `_COMMUNICATION/team_100/DOMAIN_PROTOCOL_PROPOSAL_SADOT_DOMAIN_RULES_v1.0.0.md` — proposes `SADOT_DOMAIN_RULES_CANON`
  content (SDT-DOM-1, SDT-DOM-2 scaffold per `DOMAIN_RULES_TEMPLATE.md`, plus domain-specific rules: harvest-provenance
  citation requirement, raw-materials/knowledge/design boundary, client-hub data-privacy rule from the decision log).
- `_COMMUNICATION/team_100/GOVERNANCE_CHANGE_REQUEST_LANDSCAPE_DESIGN_ARCHETYPE_INHERITANCE_v1.0.0.md` (using
  `_aos/lean-kit/modules/project-governance/config_templates/GOVERNANCE_CHANGE_REQUEST.md.template`) — bundles:
  - **The inheritance mechanism** (new): frontmatter fields `inherits_from` / `inherits_version`; per-section composition
    rule (§1/2/4/5/7/9 restate-in-full-with-lineage-marker; §3 gate-spine verbatim + LOD tables additive; §6/8
    additive-only — a child can never drop a parent's L-GATE_VALIDATE AC).
  - **The `PLA_LANDSCAPE_DESIGN.md` draft**: inherits `3D_CREATIVE`; adds Stage 0 (Site & Agronomic Survey) before
    Concept and a parallel Stage 3P (Planting Plan) alongside 3D Modeling; 6 new AC-LD-01..06 (climate-suitability
    traceability, BOQ plant completeness, planting/hardscape spatial consistency, survey-data actually used, irrigation
    zoning, maintenance-schedule documentation); team_80 gets its first formal stage-table checkpoint role (Stage 0
    findings → Team 100 spec conversion, since team_80 is advisory-only and cannot itself validate a gate).
  - Explicit flag: this is the **first-ever** use of `inherits_from` in AOS — the hub README needs a matching update,
    not just a new PLA file.
- Sequencing: file the GCR now → team_100 conflict-check → team_00 sign-off → team_100 authors the real hub files +
  propagates → **only then** flip `lifecycle_archetype: 3D_CREATIVE → LANDSCAPE_DESIGN` in both
  `agents-os/_aos/projects.yaml` and Sadot's own `roadmap.yaml` (a separate, later, pure Iron-Rule-#7 data mutation).

---

## Execution order (this session, after plan approval)

1. Harvest streams 1-9 of the map above (mechanical copy/adapt work — parallelizable, well-specified from exploration;
   suited to fanned-out execution since each source is independent).
2. Build `knowledge/permaculture/` (authored, not harvested) + `knowledge/crops/` adaptation + `knowledge/INDEX.md`.
3. Clone + prune `hub/` (harvest map #12-13, hard rule enforced).
4. Write `_aos/roadmap.yaml` (full S001-S004 WP registration, `SDT-` prefixed ids), `_aos/MILESTONE_MAP.md`, `_aos/work_packages/S001/LOD300_milestone.md` + per-WP LOD100s.
5. Write `_aos/teams.yaml`, the 3 missing `ACTIVATION_*.md` files, `_aos/context/TRAINING_PLAN.md`.
6. Run the team_80 research stream (Stream 2) → fold findings into `knowledge/`.
7. Draft + file the `DOMAIN_PROTOCOL_PROPOSAL` (domain rules) and the `GOVERNANCE_CHANGE_REQUEST` (archetype
   inheritance) in `_COMMUNICATION/team_100/`.
8. Run `bash _aos/lean-kit/modules/validation-quality/scripts/validate_aos.sh .` — must stay at 0 FAIL.
9. Commit (git-tracked paths only — `raw-materials/` stays git-ignored throughout).
10. File `_COMMUNICATION/team_110/{WP_ID}/COMPLETION_REPORT_v1.0.0.md` → team_00 + team_120, including the vNext-process
    findings below.

## Findings to flag to team_120 (vNext procedure improvements)

- `_aos/context/ACTIVATION_{ARCH,BUILDER,VALIDATOR}.md` were never scaffolded despite `_aos/README.md` listing them as
  mandatory for all profiles — the vNext scaffold step should generate these at project creation, not leave them for
  the domain team to discover missing.
- `MILESTONE_MAP.md`'s placeholder S001 label didn't match the eventual real milestone — either leave placeholder rows
  fully blank/`TBD`, or explicitly comment them as "placeholder, first domain team session should redefine."
  - **WP-ID global-uniqueness collision risk** (hub DB `work_packages.id` PK) isn't mentioned anywhere in the scaffold
  or `WP_ID_STANDARD.md`'s main body (only in a team_100 risk-summary doc) — the vNext procedure should canonize a
  per-project ID-prefix convention (e.g. `SDT-`) as a day-one scaffold step for every new L0 spoke.
- No archetype fit existed for Sadot's domain and no inheritance mechanism existed to compose one — the Specialization
  phase should include an explicit early checkpoint: "does an existing archetype cleanly fit? If not, flag
  archetype-design-needed at Phase 0, not leave it fully to the domain team to discover and design mid-stream."

---

## Verification

- `bash _aos/lean-kit/modules/validation-quality/scripts/validate_aos.sh .` → 0 FAIL (baseline today: 46 PASS/30 SKIP/0 FAIL).
- `knowledge/context/INDEX.md` resolves and follows the 4-part pattern; every file it points to exists.
- `_aos/teams.yaml` — every team's `mandatory_reads` ≤4 and resolves to real files.
- `hub/` builds/renders locally (static-site build script run) with zero `eyal`/`EA-`/`D-EYAL-` strings remaining
  (`grep -ri eyal hub/` → no hits).
- `_aos/roadmap.yaml` — every WP has a valid `SDT-S00N-P00N-WP00N` id, resolvable `spec_ref` (or `TBD`), and a
  builder/validator pair satisfying cross-engine at gated WPs.
- `git status` — confirm nothing under `raw-materials/` was staged.

---

## Execution status (as of 2026-07-10, when this plan was persisted to the repo)

Substantially executed across this session and the follow-on session summarized in
[HANDOFF_TO_team_100_SADOT_PARALLEL_CHANNEL_v1.0.0.md](file:///Users/nimrod/Documents/AOS_V5/Sadot/_COMMUNICATION/team_100/HANDOFF_TO_team_100_SADOT_PARALLEL_CHANNEL_v1.0.0.md)
and [INFRA_AUDIT_and_RESPONSE_v1.0.0.md](file:///Users/nimrod/Documents/AOS_V5/Sadot/_COMMUNICATION/team_110/INFRA_AUDIT_and_RESPONSE_v1.0.0.md)
— see those files for the current per-item status (17 DONE / 5 PARTIAL / 2 NOT_DONE out of 24 audited items). This
file is preserved as the original plan record, not updated in place, per this project's norm of never silently
overwriting a prior decision record.
