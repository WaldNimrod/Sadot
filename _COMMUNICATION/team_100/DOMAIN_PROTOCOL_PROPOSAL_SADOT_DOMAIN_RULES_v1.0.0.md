---
id: DOMAIN_PROTOCOL_PROPOSAL_SADOT_DOMAIN_RULES_v1.0.0
type: DOMAIN_PROTOCOL_PROPOSAL
from: Team 110 (Domain Architect, ADR045 full execution authority)
to: Team 100 (Chief System Architect)
cc: Team 00 (Principal), Team 120 (Ambassador)
date: 2026-07-08
version: v1.0.0
urgency: LOW
target_file: "lean-kit/modules/project-governance/SADOT_DOMAIN_RULES_CANON_v1.0.0.md (new, hub)"
project: "Sadot — Landscape Architecture (sadot)"
---

# Domain Protocol Proposal: SADOT_DOMAIN_RULES_CANON

## 1. Requesting Team

- **Team ID:** 110
- **Role:** Domain Architect (landscape architecture, IR#14-specialized)
- **Project:** Sadot (sadot)
- **Engine:** claude-code (this session)

## 2. Proposed Change

Register a new domain rules canon for the Sadot domain, following the pattern already established by the real
`TT_DOMAIN_RULES_CANON_v1.0.0.md` (TikTrack) — i.e. authored/committed at the hub path
`lean-kit/modules/project-governance/SADOT_DOMAIN_RULES_CANON_v1.0.0.md`, then propagated to Sadot's
`_aos/lean-kit/` cache like every other domain rules canon. Content proposed below, using
`lean-kit/modules/standards-conventions/templates/DOMAIN_RULES_TEMPLATE.md` as the structural base.

### Proposed content (draft — team_100 to ratify/adjust wording before committing)

```markdown
---
id: SADOT_DOMAIN_RULES_CANON
type: DOMAIN_RULES_REFERENCE
domain: sadot
authority: Team 00 + Team 100 (hub)
date: 2026-07-08
version: 1.0.0
status: ACTIVE
---

# Sadot domain rules (SDT-DOM) — canonical reference

**Read this file only when operating on Sadot product work** (landscape design, dossier, KB, hub, or Blender work in
the Sadot repo). Hub-only or non-Sadot spokes: skip.

**Hub path:** `lean-kit/modules/project-governance/SADOT_DOMAIN_RULES_CANON_v1.0.0.md`
**Spoke path (physical copy):** `_aos/lean-kit/modules/project-governance/SADOT_DOMAIN_RULES_CANON_v1.0.0.md`

---

## SDT-DOM-1 — AOS Environment is Out of Scope

Do NOT audit, modify, document, or produce artifacts that govern the AOS environment (`agents-os/`). The AOS
platform is a general multi-project environment with its own governance authority separate from Sadot.

Sadot domain work covers:
- Design-dossier standards (`design/`)
- Knowledge-base content (`knowledge/`)
- Client-hub content (`hub/`)
- 3D model / Blender pipeline conventions (`blender/`)
- Project work-environment conventions specific to Sadot

Violations: any artifact that purports to govern, override, or document AOS-layer behavior without Team 00 + Team 100
authorization is invalid and must be retracted.

## SDT-DOM-2 — AOS Layer Extensions Require Dual Authorization

Sadot MAY extend the AOS layer (add capabilities on top of AOS defaults for Sadot's benefit). Any extension that
overrides an AOS default — rather than purely adding to it — requires BOTH Team 00 written approval AND AOS
authorization (confirmation the AOS layer permits the override). An extension lacking both approvals is invalid.

## SDT-DOM-3 — Harvest Provenance is Mandatory

Sadot's environment was built by harvesting reusable infrastructure from four sibling domains (microgreens
architectural-drawing canon + geo/Blender pipeline, SmallFarmsAgents crop/climate KB, EyalAmit client-hub pattern,
nimrod-book/bio permaculture credentials). Every harvested file MUST carry a one-line provenance header (source
repo, harvest date, WP). Content authored from scratch (e.g. `knowledge/permaculture/`) MUST NOT claim harvested
provenance it doesn't have — cite real sources only.

## SDT-DOM-4 — raw-materials / knowledge / design Boundary

`raw-materials/` is the un-curated, git-ignored pile of client exchange (see `_aos/context/RAW_MATERIALS.md`).
`knowledge/` and `design/` are the tracked, curated canon outputs. Never treat `raw-materials/` content as
citable/final until it has been explicitly curated into `knowledge/` or `design/`. Never fabricate plot-specific
facts (site survey, soil test, sun/shade map) in `knowledge/` or `design/` while `raw-materials/from-client/` lacks
the corresponding real source — mark the gap BLOCKED instead.

## SDT-DOM-5 — Client-Hub Data Privacy

When Sadot's `hub/` pattern is cloned from or compared against another client's hub (e.g. EyalAmit), never copy
another client's real data/content (decisions, testimonials, meeting notes) into Sadot's `hub/data/`. Only
structural/code patterns may be reused; each client's real content stays in that client's own repo.
```

## 3. Rationale

The IR#14 sanction mechanism (`AOS_CONCEPT_AND_PRINCIPLES.md` rule #8) requires domain rule extensions to route
through Team 100 conflict-check + Team 00 sign-off before becoming canon. Sadot currently has no domain rules canon
at all — this proposal fills that gap using the same pattern already proven for TikTrack (`TT_DOMAIN_RULES_CANON`),
plus 3 Sadot-specific rules (SDT-DOM-3/4/5) surfaced directly from this build-out's real risk points: harvest
provenance, the raw-materials/knowledge boundary, and cross-client data privacy when reusing the EyalAmit hub
pattern.

## 4. Precise Prompt for Team 100

Review the draft content in §2. If acceptable as-is or with minor wording changes: commit it to
`lean-kit/modules/project-governance/SADOT_DOMAIN_RULES_CANON_v1.0.0.md` (hub), following the same commit pattern
used for `TT_DOMAIN_RULES_CANON_v1.0.0.md`, then run governance propagation so it lands in Sadot's
`_aos/lean-kit/modules/project-governance/` cache. If changes are needed, respond with a redline and Team 110 will
resubmit.

## 5. Impact Assessment

- **Affects other teams:** NO — Sadot-scoped only (per SDT-DOM-1, explicitly out-of-scope for AOS-layer/other-domain
  work).
- **Requires context refresh broadcast:** NO.
- **Backward compatible:** YES — net-new file, no existing canon changes.

## 6. Approval

- [ ] Team 100 reviewed
- [ ] Team 00 approved
- [ ] Change executed in `lean-kit/modules/project-governance/`
- [ ] Propagated to Sadot's `_aos/lean-kit/` cache
- [ ] Requesting team (team_110) notified

---

*Domain Protocol Proposal | AOS system*
