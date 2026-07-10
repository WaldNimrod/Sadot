---
id: FOR_HUB_REPO_BOUNDARY_ENFORCEMENT_GAP_2026-07-10_v1.0.0
type: FOR_HUB_REPORT
for_hub: true
from: team_100 (Chief Architect, acting in Sadot spoke session)
to: team_120 (Ambassador)
cc: [team_00]
urgency: P1 (Iron rule improvement candidate — no active exploit found, but zero technical enforcement confirmed fleet-wide)
date: 2026-07-10
origin_repo: /Users/nimrod/Documents/AOS_V5/Sadot
routing_note: >
  Staged here per team_100.md's own "for_hub routing protocol" — a spoke-rooted session must not write
  directly into agents-os. Team 00: please route this into a session rooted at
  /Users/nimrod/Documents/AOS_V5/agents-os for team_120 to pick up, per that same protocol.
---

# FOR_HUB report — the hub↔spoke repo-write boundary has zero technical enforcement anywhere in AOS

## Trigger

While processing Sadot's two pending governance filings in a session rooted at the Sadot spoke repo, I
(acting as team_100) found myself with an `AskUserQuestion` genuinely presenting "write the proposed
hub file directly into `agents-os` from this Sadot-rooted session" as a *viable option* — not
immediately rejected as an obvious violation. Team 00 flagged this hard: domain work must never enter
the hub repo, and the fact that it was ever framed as a live choice, rather than treated as
unthinkable, is itself the defect worth reporting. This report is the resulting root-cause
investigation, run at Team 00's direction.

## Root cause — three distinct findings, in order of how directly they explain what happened

**1. Harness-level: a global, cross-project `additionalDirectories` grant.**
`~/.claude/settings.json` (user-global, not AOS- or project-specific) lists `agents-os` alongside five
other unrelated project repos as `additionalDirectories`, with `"defaultMode": "acceptEdits"`. This
means *every* Claude Code session on this machine, regardless of which repo it's rooted in, has raw
filesystem read/write reach into the hub with edits auto-accepted — no permission prompt gates it.
This is orthogonal to AOS entirely; it predates and is unrelated to Sadot's creation. **Not something
team_120 or any AOS governance file can fix** — flagging for visibility only; Team 00 owns this one
directly (it's their own machine-level Claude Code config).

**2. AOS-level: the "spoke never writes to hub" rule is prose-only, fleet-wide, with zero technical
enforcement.** Confirmed by exhaustive search: `core/governance/team_100.md` lines 141-146 (the
"for_hub routing protocol"), `_aos/methodology/AOS_DIRECTORY_CANON_v1.0.0.md` line 36, and each
spoke's `project_identity.yaml.cross_project_routing` field state this rule in prose. Nothing enforces
it technically — no git hook, no pre-commit/pre-push check in either repo, no CI gate.
`validate_aos.sh` Check 14 checks the *opposite* direction (whether the hub's own settings reach into
spokes) and is advisory-WARN only. `AOS_project-init`'s own bootstrap procedure (step 5: "manually
edit the hub's `_aos/projects.yaml` to register the new spoke") never specifies which session type
(hub-rooted vs. spoke-rooted) should perform that edit — meaning the standard onboarding flow for
**every** new AOS project, not just Sadot, has always depended on unwritten practice rather than an
enforced boundary. This is a structural gap across the whole fleet, surfaced by Sadot only because
this session happened to test it out loud.

**3. Sadot-specific: `project_identity.yaml` is missing content other spokes have.** Sadot's
`_aos/project_identity.yaml` has `forbidden_patterns: []` (empty) and a `cross_project_routing` field
that omits the explicit "do NOT write to agents-os / AOS-Sandbox-Lean / AOS-Sandbox-Full /
smallfarmsagents" line that TikTrack's equivalent file *does* carry populated. This is a genuine,
Sadot-specific documentation-population gap in how Sadot's bootstrap ran — but note this file is
itself a protected `_aos/`-layer snapshot (per Sadot's own CLAUDE.md, team_110/team_100 sessions must
not edit it directly), so backfilling it correctly requires a hub-side fix + re-propagation, not a
local patch.

## Audit result — no actual violation occurred

Ran a full git-history + working-tree content audit of `agents-os` for any real Sadot content
(commits, `git grep`, uncommitted diffs). **Finding: no Sadot deliverable content (design files,
client data, 3D/KB content) has ever entered the hub, committed or uncommitted.** All "sadot" hits are
legitimate cross-project catalog metadata: the `_aos/projects.yaml` registry row (same shape as every
other spoke), a `msg_preflight.sh` routing-regex line, and a few completion-report mentions of Sadot's
*local file paths* as a cited exemplar for an unrelated raw-materials-folder canon proposal — never
Sadot content itself. Nothing from this session touched `agents-os` (confirmed via `git status` before
and after). Team_110's own prior work does not appear to have ever written into the hub either — the
only Sadot-registration commit (`da0bd64`, 2026-07-08) is exactly the kind of catalog-row registration
every spoke gets, authored under a team_100-labeled commit message.

One pattern worth your explicit read: `lean-kit/modules/project-governance/TT_DOMAIN_RULES_CANON_v1.0.0.md`
is an existing, 3-month-old (2026-04-16) precedent of a *domain-specific* rules canon living in the
hub, authored on a domain team's behalf. Sadot's pending `DOMAIN_PROTOCOL_PROPOSAL_SADOT_DOMAIN_RULES`
filing follows this exact same established pattern. If Team 00's new hard rule means even
governance-content-about-a-domain must never live in the hub (as distinct from a domain's actual
deliverable work, which correctly must never live there), that would mean revisiting the
TT_DOMAIN_RULES_CANON pattern itself, not just Sadot's proposal — flagging so this isn't decided
implicitly.

## Requested from team_120

Per your charter (governance propagation, GCR handling, drift-audit, DOC_CANON stewardship) this is
exactly the kind of fleet-wide drift your role is meant to catch. Requesting:

1. Triage this as an Iron-rule-improvement candidate (P1, per team_100.md's own classification table)
   — the fix likely needs `AOS_project-init`'s bootstrap procedure updated so every future new project
   gets `forbidden_patterns` + the explicit hub-write warning populated by default, not by convention.
2. Route the `project_identity.yaml` backfill for Sadot specifically (and audit whether any other
   existing spoke besides TikTrack has the same gap) through whatever hub-side regeneration +
   propagation path is correct for `_aos/`-layer snapshot content.
3. Confirm whether team_120's own scope extends to proposing a technical safeguard (even a lightweight
   one — a `validate_aos.sh` check hardened from advisory to blocking, or a pre-commit hook in
   `agents-os` that rejects commits whose diff didn't originate from a hub-rooted actor) or whether
   this needs a dedicated GCR to whichever team owns that layer.
4. Confirm receipt and triage decision back through this same channel — team_100 (this identity) is
   tracking it via the parallel channel already open with team_110/Sadot.

— team_100 · 2026-07-10 · filed from Sadot spoke session per for_hub routing protocol, awaiting Team 00
routing into a hub-rooted session
