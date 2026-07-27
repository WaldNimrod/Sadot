---
id: NOTE_AOS_VERSION_REVIEW_SIDE_TRACK_2026-07-28_v1.0.0
type: NOTE / side-track separation
from: team_100
to: [team_00, team_120, team_110]
date: 2026-07-28
domain: sadot
status: OPEN — separate from Layer-2 domain work
---

# Side track — AOS new-version review (not Layer-2)

## Separation rule

team_00 (2026-07-28): a newer AOS version has been rolled out. Reviewing it against Sadot domain
documentation and coordinating with **team_120** is a **separate narrative**. It must **not** block or
interleave with Layer-2 domain milestones S002–S005.

Domain narrative SSOT: `_COMMUNICATION/team_100/NARRATIVE_LAYER2_PIVOT_2026-07-28_v1.0.0.md`.

## What this side track may cover (when scheduled)

- Diff new AOS governance/lean-kit expectations vs current Sadot spoke docs (`PROJECT_CONTEXT`, activation,
  domain proposals already filed under `_COMMUNICATION/team_100/`)
- Coordinate findings with team_120 (Ambassador / propagation)
- Any follow-up GCRs stay on the normal IR#12 path (team_100 / team_00) — never edit `_aos/governance/`
  or lean-kit cache by hand (Iron Rule #11)

## What this side track must NOT do

- Change S002 priority order or delay P001–P005
- Reopen the full site-in-Blender precision track
- Mix AOS infra chores into garden/pool/planting WPs

## Next action (when team_00 opens this track)

File a dated mandate or kickoff under `_COMMUNICATION/team_120/` (or team_100) with explicit scope and
non-goals; keep Layer-2 WPs untouched.
