---
id: PORT_REGISTRATION_PROPOSAL_SADOT_HUB_v1.0.0
type: infra registration proposal (port-registry.yaml addition — not a schema change, no GCR needed per
  Iron Rule #8 port canon; joint team_60 + team_100 authorship + team_00 sign-off required per the
  registry's own R4 before the live file is edited)
from: team_110
to: team_100 / team_60 (or team_00 directly, in-session)
date: 2026-07-10
project: sadot
---

# Port Registration Proposal — Sadot Client Hub (`sadot.nimrod.bio`)

## Context

team_00 asked (2026-07-10) to prepare public, no-authentication deployment infrastructure for the Sadot
client hub, matching the `il-mg.nimrod.bio` (IsraelMicrogreens) precedent on waldhomeserver — same nginx +
Cloudflare Tunnel pattern, minus the auth layer (deliberate, per explicit instruction).

Before proposing a port, checked the live registry
(`agents-os/lean-kit/modules/12-home-server-infrastructure/deployment/port-registry.yaml`, v2.6.1) and the
actual server state via SSH: `ss -tln` on waldhomeserver confirms **8090, 8092, 8099 are the only listeners
in the 8080-8104 range** (matches the registry's `agents-os` project entries) — **8094 is free**, both in
canon and in reality, as of 2026-07-10. `ls /etc/nginx/sites-enabled/` confirms no existing `sadot` site
(current sites: `aos-ecosystem`, `capra-mio`, `il-mg`, `tiktrack`).

**Note on precedent drift:** `il-mg.nimrod.bio` (port 8087) is live and real (confirmed via
`sites-enabled/il-mg`) but was **never actually registered** in `port-registry.yaml` — it doesn't appear as
a project entry anywhere in the file. Flagging this so it isn't repeated; not fixing it here (out of scope
for this proposal, belongs to the IsraelMicrogreens project's own team).

## Proposed entry

Single-environment static site (no dev/staging/production tiers needed — matches the `carpa-mio` pattern,
not the `TikTrack`/`agents-os` tiered pattern):

```yaml
  - id: sadot-hub
    name: "Sadot Client Hub (sadot.nimrod.bio)"
    ownership_team: "team_110 + team_100"
    canonical_port_decision: >-
      team_00 in-session decision 2026-07-10: public, no-authentication static client hub for
      Niv Sadot (landscape-architecture engagement). Port 8094 (next free slot in the 8080-8099
      dev-base sub-band; verified free via `ss -tln` on waldhomeserver 2026-07-10). No dev/staging/
      production tiers — single static deployment. Deliberately NO auth layer (unlike il-mg's
      Cloudflare-Access/basic-auth gate) per explicit team_00 instruction — this hub must stay
      freely reachable by the client without a login step.
    base_triplet:
      site: 8094
    reserved_offsets: [0]
    instances:
      - env: production
        host: waldhomeserver
        site: 8094
        runtime_note: >-
          nginx static site (hub/dist/ build output, python3 scripts/build_sadot_client_hub.py) at
          127.0.0.1:8094 (loopback-only — reachable via the Cloudflare Tunnel, not directly).
          Cloudflare Tunnel: sadot.nimrod.bio -> 127.0.0.1:8094 (shared tunnel
          12429a3a-e597-4841-bffb-96d539dadbc9, same one serving tt/agros/cm/il-mg). No auth (by
          design). X-Robots-Tag noindex + robots.txt disallow-all (not meant for search indexing,
          but openly link-accessible). Deploy: Sadot/hub/deploy/deploy_sadot_hub.sh.
        status: RESERVED    # -> ACTIVE once the one-time setup in hub/deploy/README.md is applied live
```

## What's needed to close this out

1. team_100 + team_60 (or team_00 directly) reviews + applies this entry to the live
   `port-registry.yaml`.
2. Someone with shell access to waldhomeserver runs the one-time setup in
   `Sadot/hub/deploy/README.md` (nginx vhost, cloudflared route, first deploy).
3. Flip `status: RESERVED` → `ACTIVE` once step 2 is confirmed live (`curl -sI https://sadot.nimrod.bio`
   returns 200 with no auth prompt).

Prepared but **not applied** — this session did not edit the live `port-registry.yaml`, nginx, or
cloudflared config, since those are shared infra touching other live projects on the same host.
