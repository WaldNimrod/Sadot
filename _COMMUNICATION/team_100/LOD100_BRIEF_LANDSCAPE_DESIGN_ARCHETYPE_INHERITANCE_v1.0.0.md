---
type: LOD100_BRIEF
proposed_track: STANDARD
proposed_wp: methodology/lifecycle-archetypes — introduce archetype inheritance (`inherits_from`) + register LANDSCAPE_DESIGN
origin: GOVERNANCE_CHANGE_REQUEST_LANDSCAPE_DESIGN_ARCHETYPE_INHERITANCE_v1.0.0.md (Sadot, team_110, 2026-07-08)
triage: _COMMUNICATION/team_100/TRIAGE_GCR_LANDSCAPE_DESIGN_ARCHETYPE_INHERITANCE_2026-07-10_v1.0.0.md (Sadot repo)
author: team_100
date: 2026-07-10
status: AWAITING_TEAM_00_ROADMAP_PLACEMENT
---

# LOD100 Brief — Archetype inheritance (`inherits_from`) + `PLA_LANDSCAPE_DESIGN`

## Problem / need

Sadot (landscape architecture) needs a lifecycle archetype that is *almost* `3D_CREATIVE` but with a
living-plant/horticulture track bolted on (site survey, planting plan, BOQ, irrigation). Today AOS's
`methodology/lifecycle-archetypes/README.md` only supports adding a **sibling** PLA — flat, orthogonal
to the 4 existing ones — with no way to say "this archetype is `3D_CREATIVE` plus these deltas."
Building `LANDSCAPE_DESIGN` as a full sibling would mean re-authoring 3D_CREATIVE's entire gate
spine, stage table, and validation criteria by hand and hoping it never drifts from the parent it's
conceptually derived from. Team 110's GCR proposes fixing this properly: a first-ever `inherits_from`
mechanism, then `LANDSCAPE_DESIGN` as its first real user.

## Proposed outcome (LOD400 deliverable)

Two hub files, both authored by Team 100 per Iron Rule #11 (Team 110's GCR content is a proposal, not
final text):

1. **`methodology/lifecycle-archetypes/README.md`** — new "Archetype Inheritance" section +
   "Adding an Inherited Archetype" procedure, alongside the existing sibling-archetype procedure.
   New PLA frontmatter fields: `inherits_from` (parent archetype id, null for a base archetype — v1
   is single-level only, no inheritance chains) and `inherits_version` (parent version pinned at
   authoring time, parent must be `status: ACTIVE`). A fixed per-section composition rule for all 10
   PLA sections (full text proposed in the GCR §2A) — restate-vs-additive-vs-verbatim rules per
   section, so a future second inheriting PLA has a predictable contract instead of bespoke merge
   logic each time.

2. **`methodology/lifecycle-archetypes/PLA_LANDSCAPE_DESIGN.md`** (new) — inherits `3D_CREATIVE`
   v1.0.0. Adds Stage 0 (Site & Agronomic Survey) and a parallel Stage 3P (Planting Plan, using the
   compound-stage pattern `3D_CREATIVE` already licenses), 6 new acceptance criteria (AC-LD-01..06:
   climate/soil suitability, BOQ completeness, spatial consistency, site-survey-as-input, irrigation
   zoning, maintenance schedule), and team_80's first formal stage-table checkpoint role (Stage 0,
   advisory posture unchanged — Team 100 remains the validating checkpoint since team_80's own
   contract makes it non-gating). Full draft content in the GCR §2B — usable as the authoring
   starting point.

Sadot's `lifecycle_archetype` stays `3D_CREATIVE` until this WP closes and a *separate* Iron-Rule-#7
data mutation flips it — not part of this WP's scope.

## Open design questions to resolve at SPEC gate (this is why it's a WP, not IMPLEMENT-NOW)

1. **Gate-spine consistency.** The GCR says the 4-gate spine is "inherited verbatim, never
   overridden" — does that hold up against `GATE_REGISTRY.md`'s existing gate-ownership assignments,
   or does team_90/team_100's own gate-mapping table need a companion update?
2. **Composition-rule enforceability.** The rules are process discipline only at L0 (no new tooling,
   per the GCR's own "sync discipline" note) — is that acceptable long-term, or should `validate_aos.sh`
   eventually gain a check that a child PLA's inherited sections actually match its parent verbatim
   where required?
3. **team_80 checkpoint role.** Stage 0 gives team_80 its first formal stage-table placement
   ("validated by Team 100"). Confirm this is actually consistent with team_80's own governance
   contract as currently written (not just compatible in spirit) before it's canon.
4. **Backward-compatibility check.** The GCR asserts `inherits_from: null`/absent is a no-op for the
   3 other existing PLAs — verify by actually re-reading each, not just asserting it.

## Scope / size

- STANDARD track (LOD_CHECK → SPEC → BUILD → VALIDATE → CLOSE) — the SPEC gate is where the 4
  questions above get resolved before BUILD authors the final files. Hub-canon scope: affects all
  future projects, not Sadot-local (per the GCR's own impact assessment — requires a context-refresh
  broadcast on close).
- ~2 hub files (README.md section + new PLA), plus the `_aos/methodology/` propagation to every
  spoke's snapshot including Sadot's.
- **Dependency:** none blocking — Sadot's own roadmap (S002/S003) proceeds under `3D_CREATIVE` in the
  meantime and is not blocked waiting on this WP.

## Recommendation to Team 00

Place on the hub roadmap as a STANDARD-track WP. The destination (`LANDSCAPE_DESIGN` inheriting
`3D_CREATIVE`) is sound and already has team_00's in-principle backing — this WP is about giving it a
properly spec'd, precedent-setting mechanism rather than a same-session rubber stamp, since every
future inheriting PLA will follow whatever pattern gets set here.

*team_100 | LOD100 brief | 2026-07-10*
