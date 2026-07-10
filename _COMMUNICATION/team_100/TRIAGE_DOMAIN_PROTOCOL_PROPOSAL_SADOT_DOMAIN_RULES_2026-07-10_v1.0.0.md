---
id: TRIAGE_DOMAIN_PROTOCOL_PROPOSAL_SADOT_DOMAIN_RULES_2026-07-10_v1.0.0
type: TRIAGE
from: Team 100 (Chief System Architect)
to: Team 00 (Principal)
cc: Team 110 (Domain Architect, Sadot)
date: 2026-07-10
version: v1.0.0
report_id: DOMAIN_PROTOCOL_PROPOSAL_SADOT_DOMAIN_RULES_v1.0.0
from_domain: sadot (team_110)
classification: GCR (Domain Protocol Proposal — domain-rules extension under IR#14)
urgency: P2
decision: IMPLEMENT-NOW
team_00_approval: in-session (this triage, 2026-07-10)
---

# Triage: DOMAIN_PROTOCOL_PROPOSAL_SADOT_DOMAIN_RULES_v1.0.0

Processed per `core/governance/team_100.md` §"Inbound Cross-Domain Report Protocol", Step 1–4.

## Step 1 — Read and classify

Filed 2026-07-08 by team_110, urgency LOW. Proposes registering Sadot's first domain-rules canon
(`SADOT_DOMAIN_RULES_CANON_v1.0.0.md`, new hub file) covering 5 rules: SDT-DOM-1 (AOS-out-of-scope),
SDT-DOM-2 (dual authorization for AOS-layer overrides), SDT-DOM-3 (harvest-provenance headers
mandatory), SDT-DOM-4 (`raw-materials/` vs `knowledge/`/`design/` boundary — never fabricate
plot-specific facts, mark BLOCKED instead), SDT-DOM-5 (client-hub data privacy when reusing the
EyalAmit `hub/` pattern). Classification: GCR-type domain protocol proposal, invoking the IR#14
sanction path (`AOS_CONCEPT_AND_PRINCIPLES.md` rule #8: domain rule extensions route through Team 100
conflict-check + Team 00 sign-off).

## Step 2 — Triage decision: IMPLEMENT-NOW

**Conflict-check performed against `lean-kit/modules/project-governance/TT_DOMAIN_RULES_CANON_v1.0.0.md`**
(the only existing domain-rules canon, TikTrack's) — SDT-DOM-1 and SDT-DOM-2 mirror TT-DOM-1/TT-DOM-2
almost verbatim (same "AOS environment out of scope" framing, same dual-authorization mechanism for
AOS-layer overrides), confirming this proposal is following established precedent rather than
inventing new mechanism. SDT-DOM-3/4/5 are genuinely Sadot-specific (harvest provenance from the 4
sibling domains, the raw-materials/knowledge boundary, cross-client hub-data privacy) and don't
conflict with anything in hub canon — no existing rule governs any of the three.

Filing's own impact assessment (§5) states: no other teams affected, no context-refresh broadcast
needed, backward compatible (net-new file). This matches the protocol's IMPLEMENT-NOW criteria
exactly: small, well-scoped, Team 00 can approve in-session. No redline needed — the proposed content
in §2 of the filing is approved as drafted.

## Step 3 — Rationale

Sadot currently has zero domain-rules canon despite the pattern being established for TikTrack four
months ago. This closes that gap using the proven pattern, and the three novel rules address real risk
points already surfaced during Sadot's build-out (harvest provenance across 4 sibling-domain sources,
the raw-materials fabrication risk, and cross-client data leakage risk from cloning EyalAmit's hub
pattern) rather than speculative rules.

## Step 4 — Action taken

Staged the exact hub-file content, ready to commit verbatim, at
[`STAGED_FOR_HUB_SADOT_DOMAIN_RULES_CANON_v1.0.0.md`](STAGED_FOR_HUB_SADOT_DOMAIN_RULES_CANON_v1.0.0.md)
in this same directory. Per the session-boundary rule in team_100.md's "for_hub routing protocol"
(a spoke-rooted session must not write directly into `agents-os/`), the actual commit to
`lean-kit/modules/project-governance/SADOT_DOMAIN_RULES_CANON_v1.0.0.md` and the governance
propagation run (`AOS_gov-sync`) are deferred to a session rooted at
`/Users/nimrod/Documents/AOS_V5/agents-os`. That session can copy the staged file's content directly —
no further review should be needed given team_00's in-session approval here.

Team_110 notified via
[`_COMMUNICATION/team_110/RESPONSE_team_100_TO_HANDOFF_PARALLEL_CHANNEL_v1.0.0.md`](../team_110/RESPONSE_team_100_TO_HANDOFF_PARALLEL_CHANNEL_v1.0.0.md).
