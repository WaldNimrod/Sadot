---
id: REPORT_TO_team_120_PORT_CANON_PROCESS_GAP_v1.0.0
type: process-gap report (team_00 instruction 2026-07-10: mandatory report to team_120 on the port-canon
  situation)
from: team_110
to: team_120
date: 2026-07-10
project: sadot
note: Sent via live API first (POST /api/messaging/v2/send) -- returned 401 INVALID_ACTOR_KEY (team_110's
  actor key is not valid for messaging on this host, consistent with earlier failures this session). Degraded
  to this file-transport artifact + _COMMUNICATION/_log/messages.log entry, per the AOS_mail skill's
  documented non-blocking degrade path.
---

# Port-Canon Process Gap — sadot-hub Live, Registry Commit Structurally Blocked

## What happened (2026-07-10)

team_00 approved standing up the Sadot client hub at a public, no-auth address
(`sadot.nimrod.bio`), mirroring the `il-mg.nimrod.bio` precedent. Following the staged plan in
`hub/deploy/README.md`, this session (team_110) executed, directly on **waldhomeserver**, with team_00's
explicit per-host/per-change confirmation:

1. Created `/var/www/sadot-hub`.
2. Installed + enabled the nginx vhost (port 8094, loopback-only, no auth by design).
3. Added the `sadot.nimrod.bio → 127.0.0.1:8094` ingress rule to the shared cloudflared tunnel
   (`12429a3a-e597-4841-bffb-96d539dadbc9`, same tunnel as tt/agros/cm/il-mg), routed DNS, restarted the
   service. Backed up `config.yml` first; diff-verified only the intended 2 lines were added.
4. Ran the first content deploy (`hub/deploy/deploy_sadot_hub.sh`) and verified live:
   `https://sadot.nimrod.bio` → **200**, `x-robots-tag: noindex, nofollow`, no auth prompt, correct title.

**The site is live right now.** What did NOT happen, and structurally cannot happen from this session:
committing the corresponding entry to the hub's own
`agents-os/lean-kit/modules/12-home-server-infrastructure/deployment/port-registry.yaml` (Iron Rule #8 SSOT,
Team 60 ownership). The fully-drafted, reviewed entry sits at
`_COMMUNICATION/team_100/PORT_REGISTRATION_PROPOSAL_SADOT_HUB_v1.0.0.md` (`status: RESERVED`), port 8094,
verified free both in canon and via live `ss -tln` on waldhomeserver before use. **This repo's own
CLAUDE.md carries a hard-stop rule: no session rooted in a spoke may Write/Edit anything under
`agents-os/`, regardless of how ready or reviewed the content is** — so the registry commit needs a
hub-rooted session (team_100 / team_60 / team_00) to apply it and flip `RESERVED → ACTIVE`.

## Why this is a process gap, not a one-off

This is the **second consecutive** real-world instance of the same structural gap:

- `il-mg.nimrod.bio` (port 8087) is live and real (confirmed via `sites-enabled/il-mg` on waldhomeserver)
  but was **never registered in `port-registry.yaml` at all** — it doesn't appear anywhere in the file.
  Discovered incidentally while preparing the sadot-hub proposal (2026-07-10); out of scope to fix from
  here, flagged for the IsraelMicrogreens project's own team.
- `sadot-hub` (port 8094) is now live too, and — unlike il-mg — DID go through the proper proposal step
  first, but is now stuck exactly at the hub-write boundary: a spoke session can prepare a perfect,
  verified proposal and even stand up the actual service, but can never be the one to close the loop on
  the canonical bookkeeping. Nothing structurally forces that last step to happen; it just depends on
  someone noticing and doing it from the hub side.

Two-for-two suggests the current process has no real enforcement mechanism for port-registry completeness
— it relies on someone remembering, from the hub side, to go apply a spoke's proposal. Worth vNext-process
attention: e.g. a lightweight registration-request queue/API a spoke session CAN call (rather than needing
a raw file write), or a standing sweep responsibility assigned to a specific team to periodically reconcile
live `sites-enabled/*` + `ss -tln` reality against the canonical registry across all spokes.

## What's needed to close this specific instance

1. A hub-rooted session (team_100 / team_60 / team_00) applies the entry from
   `_COMMUNICATION/team_100/PORT_REGISTRATION_PROPOSAL_SADOT_HUB_v1.0.0.md` to the live
   `port-registry.yaml`, then flips `status: RESERVED` → `ACTIVE` (server-side reality already matches
   `ACTIVE` — this is now a pure bookkeeping catch-up, not a design decision).
2. Optionally, while in there: register `il-mg.nimrod.bio` too, since it's live and unregistered.
3. Separately, team_120 (or whoever owns vNext scaffold/process design) decides whether/how to close the
   general gap above so a third instance doesn't happen on the next spoke.

## Cross-references

- `_COMMUNICATION/team_100/PORT_REGISTRATION_PROPOSAL_SADOT_HUB_v1.0.0.md` — the drafted registry entry
- `hub/deploy/README.md`, `hub/deploy/nginx.sadot-hub.conf`, `hub/deploy/cloudflared.ingress.snippet` — what
  was actually applied
- `_COMMUNICATION/team_110/PLAN_SADOT_BUILDOUT_ROADMAP_RESEARCH_ENV_v1.0.0.md` § "Findings to flag to
  team_120 (vNext procedure improvements)" — this is a 4th finding in the same spirit as the 3 already
  logged there (ACTIVATION_* scaffolding, MILESTONE_MAP placeholder drift, WP-ID collision risk)
