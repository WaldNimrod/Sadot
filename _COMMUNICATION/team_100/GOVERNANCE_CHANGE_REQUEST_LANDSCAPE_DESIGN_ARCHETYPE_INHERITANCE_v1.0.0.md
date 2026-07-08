---
id: GOVERNANCE_CHANGE_REQUEST_LANDSCAPE_DESIGN_ARCHETYPE_INHERITANCE_v1.0.0
type: GOVERNANCE_CHANGE_REQUEST
from: Team 110 (Domain Architect, ADR045 full execution authority)
to: Team 100 (Chief System Architect)
cc: Team 00 (Principal), Team 120 (Ambassador)
date: 2026-07-08
version: v1.0.0
urgency: MEDIUM
target_file: "methodology/lifecycle-archetypes/README.md + methodology/lifecycle-archetypes/PLA_LANDSCAPE_DESIGN.md (new, hub)"
project: "Sadot — Landscape Architecture (sadot)"
---

# Governance Change Request: Introduce Archetype Inheritance (`inherits_from`) + Register `LANDSCAPE_DESIGN`

## 1. Requesting Team

- **Team ID:** 110
- **Role:** Domain Architect (landscape architecture, IR#14-specialized)
- **Project:** Sadot (sadot)
- **Engine:** claude-code (this session)

## 2. Proposed Change

Two coupled changes, bundled in one GCR because the second cannot be authored without the first existing:

**A. A new hub-layer mechanism:** archetype inheritance. No such mechanism exists anywhere in AOS today — confirmed
by exhaustive search: `methodology/lifecycle-archetypes/README.md` only documents adding a **sibling** archetype
(flat, orthogonal to the 4 existing PLAs), not inheriting from one. There is no `inherits_from` field anywhere in the
PLA schema. The only prior mention of this idea anywhere in the codebase is a forward-looking comment on Sadot's own
`projects.yaml` row. Sadot would be the first-ever use of this mechanism.

**B. The concrete `LANDSCAPE_DESIGN` archetype**, authored using that new mechanism, inheriting `3D_CREATIVE`.

Sadot's `lifecycle_archetype` stays `3D_CREATIVE` in the meantime and does NOT flip until team_100 completes both
changes and propagates them — the flip itself is a separate, later, pure Iron-Rule-#7 data mutation, not part of
this GCR.

### A. Inheritance mechanism (proposed schema)

New PLA frontmatter fields:
```yaml
inherits_from: 3D_CREATIVE   # null for a base archetype (v1: single-level inheritance only, no chains)
inherits_version: "1.0.0"    # parent version pinned at authoring time; parent must be status: ACTIVE
```

Fixed per-section composition rule (so future inheriting PLAs get a predictable contract, not bespoke merge logic
each time):

| PLA § | Composition rule |
|---|---|
| §1 What This Covers | Restate in full + mandatory lineage sentence ("Inherits gate spine from `<parent>`; extends with …") |
| §2 Stage Sequence | Restate in full (child renumbers 0..N) + mandatory "Lineage" column per row: verbatim / extended / NEW |
| §3 Gate Mapping | The 4 universal gates + `gate_spine` inherited **verbatim, never overridden**. Stage→gate table restated. LOD artifact table: **additive only** |
| §4 Deliverables/Stage | Restate in full; inherited-stage rows copied unchanged; new/extended stages get fresh rows |
| §5 Team Roles/Stage | Restate in full; inherited-stage role/validator pairs kept exactly (no silent reassignment); new stages need Team 100 conflict-check against each named team's own governance contract |
| §6 Validation Criteria | **Additive** — inherited-stage prose kept verbatim, new stages append clearly-marked new prose |
| §7 `stage_mapping` values | Restate in full (literal strings are necessarily child-specific once renumbered) |
| §8 L-GATE_VALIDATE ACs | **Additive only** — a child can never drop a parent AC (that requires a GCR against the parent itself) |
| §9 Compatibility Notes | Restate + required "Inherits from: X vY — Divergences from parent" bullet list |
| §10 Domain Interaction Protocols | Independent of inheritance — governed separately by IR#14 as today |

**Sync discipline:** no auto-propagation if the parent PLA later changes version — Team 100 (author of both) adds a
follow-up note to the child's §9 when it next changes the parent. Process discipline, not new tooling — consistent
with `stage_mapping`'s existing "informational, not machine-validated" status at L0.

### B. `PLA_LANDSCAPE_DESIGN.md` draft content

**Frontmatter:** `pla_id: LANDSCAPE_DESIGN`, `inherits_from: 3D_CREATIVE`, `inherits_version: "1.0.0"`,
`authority: Team 00`, `authored_by: Team 100`, `gate_spine:` unchanged, `proven_in: Sadot (S001, planned)`.

**§1 (restated):** Applies when the deliverable is an outdoor/garden design combining hardscape 3D modeling with a
living-plant system tuned to local (Israeli) climate/soil. Does NOT apply to pure interior/product 3D modeling with
no planting component (→ `3D_CREATIVE`), or a pure horticulture knowledge corpus with no spatial deliverable (→
`CONTENT_SUBSTRATE`/`DOMAIN_AGENT`).

**§2 (new stages inserted, parallel-track letter-suffix convention — same pattern 3D_CREATIVE already uses for
bolt-on compound stages):**

| Stage | Name | Lineage |
|---|---|---|
| 0 | Site & Agronomic Survey | **NEW** — soil test/type, sun-shade map, existing vegetation, water source, slope/drainage |
| 1 | Concept | parent Stage 0 (**extended** — site-survey findings + planting style now feed concept) |
| 2 | Asset Spec + Planting Spec | parent Stage 1 (**extended** — plant palette by microclimate zone + BOQ skeleton added) |
| 3 | 3D Modeling | parent Stage 2 (**verbatim**) |
| 3P | Planting Plan | **NEW, parallel to Stage 3**, same gate envelope — species-by-location layout, density, irrigation overlay, BOQ finalized |
| 4 | Iteration | parent Stage 3 (**extended** — planting plan refined in same review cycles) |
| 5 | Render Validation | parent Stage 4 (**extended** — Team 00 sign-off also confirms planting-plan/model consistency) |
| 6 | Export | parent Stage 5 (**verbatim**) |
| 7 | Documentation | parent Stage 6 (**extended** — planting plan, BOQ, irrigation/maintenance schedule added) |
| 8 | Archive | parent Stage 7 (**verbatim**) |

Rationale for the parallel "3P" slot rather than sequential: real landscape practice runs planting design
*concurrently* with hardscape modeling, not strictly after — forcing sequence would misrepresent the work. Compound
`stage_mapping` (already licensed by 3D_CREATIVE §2) covers WPs doing both: `"Stage 3 (3D Modeling) + Stage 3P
(Planting Plan)"`.

**§3:** Gate spine unchanged. Stage 0 → L-GATE_ELIGIBILITY (no concept proceeds without survey data). Stages 1-2 →
L-GATE_SPEC. Stages 3/3P/4/5/6 → L-GATE_BUILD. Stages 7-8 → L-GATE_VALIDATE. LOD tables extended (append) with
plant-list/BOQ/climate-suitability language.

**§4:** New rows — Stage 0 → `SITE_SURVEY.md` + soil test report; Stage 2 → `PLANTING_PALETTE.md`; Stage 3P →
`PLANTING_PLAN.md`, `BOQ_PLANTS.md`; Stage 7 → append planting plan + irrigation schedule. All other rows inherited
verbatim.

**§5 (team_80 gets its first formal stage-table checkpoint role):** Stage 0 = team_80 (Research) produces
soil/climate/plant-suitability findings + Team 100 drafts spec, **validated by Team 100** before Stage 1/2 opens —
team_80's own governance contract is explicit it is "advisory, not in gate process," so it cannot itself validate;
Team 100 is the mandatory checkpoint converting its findings into authorized spec input (same pattern as
CONTENT_SUBSTRATE Stage 4). Stage 3P = domain specialist (landscape/horticulture designer), validated by Team 100
(BOQ/spec completeness) with a non-blocking team_80 climate-suitability spot-check, before Stage 5's mandatory Team
00 visual gate. Every other stage inherits its role row verbatim (Stage 3 modeler→Team 100; Stage 5 render→**Team
00 mandatory**; Stage 6 export→team_90; Stage 7-8 → Team 100+Team 00 validated by team_90).

**§6:** New transition criteria — Stage 0→1: soil/sun/water/drainage documented, no "TBD" site facts. Stage 2→3/3P:
plant-palette climate-suitability pre-check complete. Stage 3P→4: every planted location maps to a palette species;
density matches irrigation-zone capacity. Stage 7→8: doc set covers planting plan + BOQ + maintenance schedule, in
addition to parent's object/driver coverage.

**§7:** New canonical strings for stages 0, 1, 2, 3P, 4, 5, 7 (extended/renamed); 3, 6, 8 keep parent's literal names.

**§8 (6 new AC-LD extensions, additive to parent's AC-3D-01..06 which apply in full):**
- **AC-LD-01:** Every plant species has a documented Israeli-climate/soil suitability check (zone, water need, sun
  exposure) traceable to Stage 0 or team_80 findings.
- **AC-LD-02:** BOQ includes complete plant quantities (species, pot size, count) — no plant line item may be "TBD".
- **AC-LD-03:** Planting-plan geometry is spatially consistent with the 3D hardscape model.
- **AC-LD-04:** Site survey data was actually used as input to Stage 1/2 (not just collected).
- **AC-LD-05:** Irrigation zoning documented and matches planting density/water needs.
- **AC-LD-06:** Documentation includes a maintenance/seasonal-care schedule usable without horticulture background.

**§9:** "Inherits from: 3D_CREATIVE v1.0.0. Divergences: +2 stage slots (Stage 0, Stage 3P), +6 ACs, +team_80
checkpoint role (first PLA to formally place team_80 inside a stage table)." **Flag: this is the first-ever use of
`inherits_from` — the README needs a matching update, not just a new PLA file.**

**§10:** Not needed now — deferred to a future spoke-local `DOMAIN_PROTOCOL_PROPOSAL` if a horticulture-specific
interaction protocol is wanted later.

## 3. Rationale

Sadot's design intent (team_00-approved 2026-07-08, per `~/.claude/plans/shimmying-jumping-mango.md` §E) is a
`LANDSCAPE_DESIGN` sub-archetype inheriting `3D_CREATIVE`. Exploration confirmed no archetype-inheritance mechanism
exists to build it — this GCR proposes both the mechanism and the concrete archetype together so the mechanism
isn't specified in the abstract without a worked example.

## 4. Precise Prompt for Team 100

1. Review §2A (the `inherits_from` mechanism + composition-rule table) — if acceptable, add it to
   `methodology/lifecycle-archetypes/README.md` (a new "Archetype Inheritance" section + an "Adding an Inherited
   Archetype" procedure alongside the existing sibling-archetype procedure).
2. Review §2B (the `PLA_LANDSCAPE_DESIGN.md` draft) — author the final hub file at
   `methodology/lifecycle-archetypes/PLA_LANDSCAPE_DESIGN.md` using the draft as a starting point (Team 100 retains
   full authorship per Iron Rule #11 — this is a proposal, not final text).
3. Bump lean-kit patch version; run governance propagation (`AOS_gov-sync`/`propagate_governance.sh`) so Sadot's
   `_aos/methodology/` snapshot picks up both files.
4. Notify Team 110 — Sadot will then flip `lifecycle_archetype: 3D_CREATIVE → LANDSCAPE_DESIGN` in both hub
   `agents-os/_aos/projects.yaml` (row `id: sadot`) and Sadot's own `_aos/roadmap.yaml` `project:` block, as a
   separate Iron-Rule-#7 structured-data mutation (API-only if DB online; direct file edit + commit under the
   L0/ADR034 offline carve-out otherwise) — NOT part of this GCR's scope.

## 5. Impact Assessment

- **Affects other teams:** YES — the `inherits_from` mechanism is hub-canon, available to all future archetypes/
  projects, not Sadot-local. team_80 gains its first formal stage-table role (Stage 0 checkpoint) — advisory
  posture unchanged, just formally documented for this one archetype.
- **Requires context refresh broadcast:** YES — any future project considering an inherited archetype should know
  this mechanism exists.
- **Backward compatible:** YES — `inherits_from: null`/absent is the default for all 4 existing PLAs; nothing about
  them changes.

## 6. Approval

- [ ] Team 100 reviewed
- [ ] Team 00 approved
- [ ] Change executed in `methodology/lifecycle-archetypes/`
- [ ] Propagated to Sadot's `_aos/methodology/` cache
- [ ] Requesting team (team_110) notified
- [ ] Sadot `lifecycle_archetype` flip executed as a separate follow-up step (not blocked on this checklist)

---

*Governance Change Request | AOS system*
