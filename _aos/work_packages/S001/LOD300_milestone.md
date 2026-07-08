---
id: S001-LOD300-milestone
type: LOD300_milestone
stage: S001
authored_by: team_110 (Domain Architect, ADR045 full execution authority)
date: 2026-07-08
status: ACTIVE
---

# S001 — Milestone Scope: Environment completion, domain research, site analysis + client brief

## 1. Scope statement

S001 is the foundation stage of the Sadot landscape-architecture project (client Niv Sadot, private house, Pardes
Hanna). It covers three parallel programs: (P001) finishing the environment/knowledge-base infrastructure team_120
started staging, (P002) the RESEARCH track (team_80, advisory, no gate), and (P003) authoring the site-analysis
dossier + formal client brief that S002 (Concept Design) depends on. This broadens the milestone description
team_120 originally wrote ("Initial domain research and environment bootstrap") — no WP was ever registered against
that label, so the broadening carries no migration cost.

**Hard constraint:** `raw-materials/from-client/` is empty — no plot survey has been received from Niv Sadot. Two WPs
below are genuinely BLOCKED, not just deprioritized, until that arrives.

## 2. Work Packages in this stage

### P001 — Environment / Knowledge-Base completion (team_110 executing directly, all NOW)

| WP | Label | Acceptance criterion (1-line) |
|---|---|---|
| SDT-S001-P001-WP001 | Harvest drawing-canon + Blender/geo pipeline → `design/`, `blender/` | All listed files present at target paths with provenance headers; source repo unmodified |
| SDT-S001-P001-WP002 | Harvest `design/CANONICAL/` 10-doc SSOT skeleton | 10 renamed/adapted docs present; conflict law preserved verbatim |
| SDT-S001-P001-WP003 | Harvest crop/climate KB → `knowledge/crops/` | Schema reference + citation index + starter plant shortlist present, no raw binaries duplicated |
| SDT-S001-P001-WP004 | Clone + prune client hub → `hub/` | 6 core views present, `sadot-*` renamed, zero `eyal`/`EA-`/`D-EYAL-` strings, no real Eyal client data copied |
| SDT-S001-P001-WP005 | Author `knowledge/permaculture/` KB from scratch | 5 files present, credential citations verified against source, no fabricated facts |
| SDT-S001-P001-WP006 | `knowledge/INDEX.md` + `_aos/teams.yaml` + missing `ACTIVATION_*.md` | INDEX resolves; every team's `mandatory_reads` ≤4 and resolves; 3 ACTIVATION files exist |
| SDT-S001-P001-WP007 | `SADOT_DOMAIN_RULES_CANON` draft + `DOMAIN_PROTOCOL_PROPOSAL` filed | Proposal artifact filed at `_COMMUNICATION/team_100/`, addressed correctly, actionable per IR#14 |
| SDT-S001-P001-WP008 | `LANDSCAPE_DESIGN` archetype-inheritance mechanism + PLA draft + GCR filed | GCR artifact filed at `_COMMUNICATION/team_100/` using the canonical template, bundles mechanism + PLA content |
| SDT-S001-P001-WP009 | `_aos/context/TRAINING_PLAN.md` (6-artifact composition) | All 6 artifacts named + resolvable, references WP006-008 outputs |

### P002 — Research (team_80, ADR044 Track 4 — advisory, NOT part of the gate process)

| WP | Label | Acceptance criterion | Status |
|---|---|---|---|
| SDT-S001-P002-WP001 | Israeli climate/soil general research | Findings artifact in `_COMMUNICATION/team_80/`, folded into `knowledge/` | NOW |
| SDT-S001-P002-WP002 | Plant-selection candidate shortlist | Shortlist cites harvested crop-KB schema, general-fit only | NOW |
| SDT-S001-P002-WP003 | Permaculture principles + precedents research | Feeds WP005's KB structure | NOW |
| SDT-S001-P002-WP004 | Plot-specific site analysis | Real topography/sun-shade/drainage/soil-test data | **IN_PROGRESS** — unblocked 2026-07-08 (survey PDF + IFC received); soil test/sun-shade study still open |

### P003 — Site analysis + client brief authoring (team_70 / sadot_doc)

| WP | Label | Acceptance criterion | Status |
|---|---|---|---|
| SDT-S001-P003-WP001 | Client brief intake questionnaire/template | Template ready to send to Niv Sadot | **COMPLETE** (superseded — real brief arrived first) |
| SDT-S001-P003-WP002 | Site-analysis dossier + formal client brief | Synthesizes P002-WP004 | **IN_PROGRESS** — drafted 2026-07-08, pending client confirmation of open items |
| SDT-S001-P003-WP003 | Transcribe + curate client voice-note recordings | 4 recordings transcribed + synthesized | **COMPLETE** 2026-07-08 |

**2026-07-08 update:** first client materials batch received in `raw-materials/from-client/` — licensed survey
(`10111TD122 (1).pdf`, plot boundary + 24-tree inventory + elevations), architectural IFC model (`NSB02.ifc`), 2
hand-sketched concept diagrams, and 4 voice-note recordings (transcribed + synthesized into
`design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md`). Curated into `blender/data/site/SITE_GEO.yaml` and
`design/CANONICAL/02_SPATIAL_SSOT_and_GEOMETRY.md` / `08_LANDSCAPE_PLANTING_PLAN.md`. This substantially advances
P002-WP004 and P003-WP002 — see roadmap.yaml notes on each for exactly what remains open.

## 3. Dependency graph

```
P001 (harvest + governance, WP001-009) ──┬──> P002-WP001/002/003 (general research) ──> P001-WP005 (permaculture KB)
                                          │
                                          └──> P002-WP002 depends on P001-WP003 (crop KB harvest)

raw-materials/from-client/ survey (EXTERNAL, from Niv Sadot)
        │
        ├──> P002-WP004 (plot-specific site analysis)  [BLOCKED until survey arrives]
        │           │
        │           └──> P003-WP002 (site-analysis dossier + client brief)  [BLOCKED]
        │                       │
        │                       └──> S002 (Concept Design) — cannot start without the formal client brief
```

## 4. Harvest map (source → Sadot destination)

| # | Source | Destination | WP |
|---|---|---|---|
| 1 | `IsraelMicrogreens-BlenderV2-Project/docs/ARCHITECTURAL_DRAWING_CANON/` | `design/ARCHITECTURAL_DRAWING_CANON/` | WP001 |
| 2 | `.../scripts/drawing/` | `design/scripts/drawing/` | WP001 |
| 3 | `.../WP_PHASE5_TECHNICAL_DOCS/lib/` (8 generic modules) | `design/lib/` | WP001 |
| 4 | `.../lib/geo_itm.py` | `blender/lib/geo_itm.py` | WP001 |
| 5 | `.../scripts/assembly/site_geo_anchor.py` + 2 others | `blender/scripts/site/` | WP001 |
| 6 | `.../blender/CURRENT_MODEL.md` (pattern only) | `blender/CURRENT_MODEL.md` | WP001 |
| 7 | `.../scripts/inspect/session_mcp_verify.py` | `blender/scripts/inspect/` | WP001 |
| 8 | `.../CANONICAL/` (10-doc skeleton) | `design/CANONICAL/` | WP002 |
| 9 | `SmallFarmsAgents/organic_market_agent/crop_book/` | `knowledge/crops/` | WP003 |
| 10 | `SmallFarmsAgents/data/external_sources/` (cited, not copied) | `knowledge/crops/sources/` | WP003 |
| 11 | `EyalAmit.co.il-2026/hub/` (structure only) | `hub/` | WP004 |
| 12 | `nimrod-book/chapters/11_ERA_GARDEN_2013_2023.md` + `nimrod-bio` (authority, not structure) | cited in `knowledge/permaculture/` | WP005 |

## 5. RESEARCH-exemption note

P002 WPs run under team_80's own governance contract: "External research team... Advisory — delivers research
artifacts to architecture teams via Team 00 routing. Not part of the gate process." No LOD100-500 chain is required;
`current_lean_gate`/`lod_status` fields in `roadmap.yaml` carry schema-required nominal values only, per ADR044 Track 4.

## 6. In-flight governance proposals

- `_COMMUNICATION/team_100/DOMAIN_PROTOCOL_PROPOSAL_SADOT_DOMAIN_RULES_v1.0.0.md` (WP007) — awaiting team_100
  conflict-check + team_00 sign-off.
- `_COMMUNICATION/team_100/GOVERNANCE_CHANGE_REQUEST_LANDSCAPE_DESIGN_ARCHETYPE_INHERITANCE_v1.0.0.md` (WP008) —
  awaiting team_100 conflict-check + team_00 sign-off. `lifecycle_archetype` stays `3D_CREATIVE` until this resolves.

## 7. Team assignment

Per `_aos/team_assignments.yaml`: `sadot_build` (cursor-composer) builds harvested/technical artifacts, `sadot_doc`
(codex — IR#14 specialization of team_70 the Librarian) authors content/governance drafts, `sadot_val` (openai)
validates. Cross-engine (Iron Rule #1) satisfied at every gated WP.
