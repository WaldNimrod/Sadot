---
id: HANDOFF_TO_team_100_SADOT_PARALLEL_CHANNEL_v1.0.0
type: HANDOFF (aos_handoff, full context) — opens an ongoing parallel channel, not tied to one WP
from: team_110 (Sadot Domain Architect + design lead — IR#14-specialized for landscape architecture)
to: team_100 (Chief Architect)
cc: [team_00]
date: 2026-07-09
domain: sadot (landscape_architecture)
project_path: /Users/nimrod/Documents/AOS_V5/Sadot
note: "Generated via /AOS_handoff → /AOS_mail handoff. Live DB/API capture was attempted first (per ADR043 §15.4/§16)
  — health check OK (200, DB online) but the authenticated messaging call returned 401 INVALID_ACTOR_KEY for
  team_110 (this session's actor key is not provisioned/valid for team_110-scoped messaging actions). Falling back
  to the documented legacy file transport (AC10) — this file IS the handoff artifact. team_00: if you want the live
  DB channel working too, team_110 needs a key provisioned via agents-os/scripts/provision_actor_key.sh, run from a
  team_00/team_99 issuer session."
---

# HANDOFF → team_100 — Sadot: full project context, opening an ongoing parallel channel

**Why this exists:** team_00 asked to open a parallel channel to team_100 for the Sadot project — not a one-time
WP handoff, but ongoing visibility so team_100 can track this domain, respond to the 2 governance items already
filed (§C below), and be a standing point of contact as the project continues across many future sessions.

## A. What Sadot is

A real, live **landscape-architecture / garden-design engagement**: a private house in Pardes Hanna, Israel,
client **Niv Sadot**. Domain team_110 (this team) holds **full execution authority (ADR045)** for the domain —
spawning team_10 (Blender/3D build), team_70 (Librarian/design dossier), team_80 (research), team_90 (cross-engine
validate) as needed. Deliverables: a site-anchored 3D garden model (Blender), a contractor-grade design dossier
(site plan, planting plan, hardscape sections, BOQ), a plant-selection + planting schedule tuned to the local
Israeli climate, and a client hub. `lifecycle_archetype` is currently `3D_CREATIVE` (base) — see §C.2.

## B. Current status (as of 2026-07-09) — one paragraph per real workstream

- **Roadmap:** S001 (environment/research/site-analysis+brief) is substantially executed; S002 (concept design)
  and S003 (detailed design + 3D model) are `PLANNED`, not yet started for real. Full state:
  `_aos/roadmap.yaml` (the SSOT — do not trust any WP-count number quoted elsewhere, including in older files in
  this repo; some drifted and were corrected, `roadmap.yaml` itself is current).
- **Client materials received & curated:** licensed plot survey (boundary/elevation/orientation — real, confirmed
  by direct computation from the survey's own ITM coordinates), the architect's IFC house model (real
  ifcopenshell extraction: storeys, windows, walls, doors, materials — `design/CANONICAL/HOUSE_IFC_REFERENCE.md`),
  4 voice-note recordings synthesized into `design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md` (a living document, several
  ASR-transcription corrections already made and tracked), and the client's own hand-drawn concept sketch
  (confidence-tiered analysis: `design/CANONICAL/CONCEPT_SKETCH_REFERENCE.md`).
- **Documentation/SSOT discipline:** a full audit pass was run recently (Workflow, 6 parallel domain audits) after
  team_00 asked for one explicitly, given this is a multi-session project where drift is costly. ~35 duplication/
  contradiction findings were fixed across 26 files (details in
  `_COMMUNICATION/team_110/COMPLETION_REPORT_SKETCH_ANALYSIS_and_SSOT_AUDIT_v1.0.0.md`). `design/CANONICAL/
  00_MASTER_INDEX_and_CANON_MAP.md` is the front door and should now be current.
- **3D model:** a first, deliberately-provisional `.blend` exists (`blender/sadot_v1_initial.blend`, pointer:
  `blender/CURRENT_MODEL.md`) — real IFC-extracted house geometry + the real surveyed plot boundary, but the
  **site-anchoring (how the house sits on the real plot, both position/rotation AND elevation) is explicitly NOT
  yet resolved** — an initial heuristic hypothesis (matching a wall to a survey edge) was tried and then
  **contradicted** by the client's own direct statement about which way the house faces, so it's currently back to
  an open investigation (a Workflow is resolving this rigorously via the IFC's own placement-matrix data as this
  handoff is being written). Do not treat the current model's positioning as final for anything downstream.
- **Governance filings (§C) — still awaiting team_100 action**, filed 2026-07-08, no response yet as of this
  writing.

## C. Action needed from team_100

1. **`_COMMUNICATION/team_100/DOMAIN_PROTOCOL_PROPOSAL_SADOT_DOMAIN_RULES_v1.0.0.md`** — proposes
   `SADOT_DOMAIN_RULES_CANON` content (domain-specific rules, harvest-provenance citation requirement,
   raw-materials/knowledge/design boundary, client-hub data-privacy rule). Awaiting conflict-check + sanction path
   (team_100 → team_00 sign-off per IR#14).
2. **`_COMMUNICATION/team_100/GOVERNANCE_CHANGE_REQUEST_LANDSCAPE_DESIGN_ARCHETYPE_INHERITANCE_v1.0.0.md`** —
   proposes a **new mechanism**: `inherits_from`/`inherits_version` frontmatter fields + a composition rule for
   lifecycle-archetype PLA files, used to define `LANDSCAPE_DESIGN` as inheriting `3D_CREATIVE`. This is the
   **first-ever use of `inherits_from` in AOS** — flagged in the GCR itself as needing a matching hub README
   update, not just a new PLA file. `roadmap.yaml`'s `lifecycle_archetype` stays `3D_CREATIVE` until this is
   ratified — do not treat `LANDSCAPE_DESIGN` as active in the meantime (a stale claim to that effect was found
   and fixed in `_aos/context/PROJECT_CONTEXT.md` during the SSOT audit — flagging here so team_100 doesn't
   independently discover the same drift).

Both are unanswered — team_100, please pick these up or tell team_00/team_110 what's blocking a response.

## D. Open items / genuinely unresolved (so team_100 has real context, not just a status label)

- Site-anchoring (position + rotation + elevation of the house within the real surveyed plot) — actively being
  re-resolved as this is written; see `design/CANONICAL/BLENDER_SHELL_BUILD_PLAN_v1.0.0.md` §3/§3b and
  `blender/CURRENT_MODEL.md` for the live state once that finishes.
- Several client-brief items still need direct confirmation from Niv (ornamental-pond decision, one neighbor-name
  ASR ambiguity, reference photos) — tracked in `design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md` §9, the single
  authoritative open-items list for the brief (do not let a second one grow elsewhere).
- Formal soil lab test and a real sun/shade seasonal study are still genuinely un-received (not fabricatable) —
  tracked in `_aos/roadmap.yaml` (WP `SDT-S001-P002-WP004`, status `IN_PROGRESS`, not `COMPLETE`).

## E. Constraints (unchanged, restated for a clean handoff)

Cross-engine validation at the decisive gate (IR#1); `validate_aos.sh` kept at 0 FAIL after every change (last
confirmed run: 46 PASS / 30 SKIP / 0 FAIL). IR#11 respected — `_aos/{governance,methodology,lean-kit}` never
hand-edited. Domain work lives in `design/`, `knowledge/`, `hub/`, `blender/`, `_COMMUNICATION/team_*/`, and the
tracked `_aos/` project files.

## F. What "parallel channel" means going forward

This isn't a one-time hand-off of a finished WP — team_00 wants team_100 to have standing visibility into Sadot as
it continues across sessions. Suggested light-touch cadence: team_100 checks in on the two pending governance
items above when able; team_110 will keep filing dated completion reports to `_COMMUNICATION/team_110/` as
milestones land (searchable there by date) rather than pushing every update to team_100 individually.

— aos_handoff issued by team_110 under team_00 · 2026-07-09 · opens an ongoing parallel channel, not a single-WP
return · legacy file transport (live DB channel not provisioned for team_110 this session — see note above)
