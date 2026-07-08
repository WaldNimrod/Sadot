# TRAINING_PLAN.md — Sadot Domain Team Onboarding

**Authored by:** team_110 (Domain Architect, ADR045 full execution authority) · **Date:** 2026-07-08
**Pattern:** the fixed 6-artifact composition approved in `~/.claude/plans/shimmying-jumping-mango.md` §C.

Every agent activating on Sadot — any engine, any team — completes this composition before touching a WP. It
supersedes generic per-role checklists with Sadot-specific pointers.

## 1. Identity onboarding (mandatory first-session read, once per agent)

- `/Users/nimrod/Documents/AOS_V5/agents-os/methodology/AOS_IDENTITY_ONBOARDING_v1.0.0.md` — what AOS is, hub vs
  spoke, the boundary rule, authority hierarchy, how to file a `GOVERNANCE_CHANGE_REQUEST`.
- Sadot-specific addendum: this repo's `_aos/` is a read-only Model-B governance snapshot (`_aos/governance/`,
  `_aos/methodology/`, `_aos/lean-kit/` — never hand-edited, refreshed by hub sync per `_aos/AOS_GOVERNANCE_VERSION.yaml`).
  Domain work lives in `design/`, `knowledge/`, `hub/`, `blender/`, `_COMMUNICATION/team_*/`, and the tracked `_aos/`
  project files (roadmap, teams.yaml, context/).

## 2. Per-team mandatory_reads (≤4 each — see `_aos/teams.yaml`)

| Team | Mandatory reads |
|---|---|
| team_10 (Blender/drawing builder) | `knowledge/context/INDEX.md`, `design/ARCHITECTURAL_DRAWING_CANON/00_ENTRY_POINT.md`, `blender/CURRENT_MODEL.md` |
| team_70 / `sadot_doc` (content/dossier author) | `knowledge/context/INDEX.md`, `design/CANONICAL/00_MASTER_INDEX_and_CANON_MAP.md`, `knowledge/permaculture/00_INDEX.md` |
| team_80 (research) | `knowledge/context/INDEX.md` |
| team_00 (Principal) | none required — reads on demand |

## 3. Per-role activation prompts

- `_aos/context/ACTIVATION_ARCH.md` (sadot_arch — architecture_agent)
- `_aos/context/ACTIVATION_BUILDER.md` (sadot_build — builder_agent, team_10)
- `_aos/context/ACTIVATION_VALIDATOR.md` (sadot_val — validator_agent, team_90)
- `/AOS_onboard` (hub skill) generates a fresh onboarding block per team on request — run it if any of the above
  feels stale.

## 4. IR#14 domain-specialization docs (in flight — not yet ratified)

- `_COMMUNICATION/team_100/DOMAIN_PROTOCOL_PROPOSAL_SADOT_DOMAIN_RULES_v1.0.0.md` — proposes
  `SADOT_DOMAIN_RULES_CANON` (SDT-DOM-1..N). Awaiting team_100 conflict-check + team_00 sign-off.
- `_COMMUNICATION/team_100/GOVERNANCE_CHANGE_REQUEST_LANDSCAPE_DESIGN_ARCHETYPE_INHERITANCE_v1.0.0.md` — proposes the
  `inherits_from` PLA mechanism + `PLA_LANDSCAPE_DESIGN.md` content. Awaiting team_100 conflict-check + team_00
  sign-off. `lifecycle_archetype` stays `3D_CREATIVE` until this resolves — do not treat LANDSCAPE_DESIGN as active.
- Once ratified: read the hub-authored `PLA_LANDSCAPE_DESIGN.md` and the `SADOT_DOMAIN_RULES_CANON` from
  `_aos/lean-kit/modules/project-governance/` (propagated snapshot) instead of these proposal drafts.

## 5. The knowledge base

- `knowledge/INDEX.md` — top-level KB index.
- `knowledge/context/INDEX.md` — reading-order-by-task table (4-part pattern, mirrors
  `IsraelMicrogreens-BlenderV2-Project/data/context/INDEX.md`).
- `knowledge/crops/` — plant-selection/climate data substrate (harvested from SmallFarmsAgents).
- `knowledge/permaculture/` — zones/sectors/guilds/swales design methodology + Nimrod's cited credentials (authored
  from scratch — no prior structured source existed).
- Optional NotebookLM packaging (`AOS_NOTEBOOKLM_PACKAGE_PROCEDURE_v1.0.0.md`) — deferred; revisit once the KB has
  enough real (non-placeholder) content to be worth consolidating.

## 6. Startup + gate discipline

Every session, in this order:
1. `_aos/context/PROJECT_CONTEXT.md` — project background.
2. `_aos/roadmap.yaml` — current WP + gate position (SSOT for WP state).
3. `_aos/project_identity.yaml` — write-root boundaries.
4. Your role's `_aos/context/ACTIVATION_*.md` — identity + responsibilities.
5. `knowledge/context/INDEX.md` — domain orientation.
6. `bash _aos/lean-kit/modules/validation-quality/scripts/validate_aos.sh .` — must show 0 FAIL before any gate
   advancement.

**Gate model:** Track A (4-gate): L-GATE_ELIGIBILITY → L-GATE_SPEC → L-GATE_BUILD → L-GATE_VALIDATE. RESEARCH-classified
WPs (team_80, ADR044 Track 4) are exempt — advisory only, no LOD chain. team_90 owns the governance facet of
L-GATE_VALIDATE in this project (the historical "team_190" name is collapsed into team_90 — cite team_90, not team_190).
