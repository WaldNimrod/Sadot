# Sadot Client Hub

Static client-facing status hub for **Niv Sadot (ניב שדות)** — landscape-architecture /
garden-design project for a private house in Pardes Hanna.

## What this is

A view-and-coordination layer (not a replacement for formal deliverables) that shows the
client, in one place: roadmap status, open tasks, open decisions requiring input, a
meeting brief, and a prioritized "what we need from you" list. Client decision answers
can be exported as JSON from the browser (no server round-trip) for later ingestion into
`hub/ssot/`.

Content is currently **empty scaffolding** — every `hub/data/*.json` file is schema-valid
but has no real project content yet. It will be populated once the landscape-design
engagement enters its content/decisions phase.

## Structure

```
hub/
  data/     — JSON source of truth (edit these, then rebuild)
  src/      — CSS/JS assets (hub-base.css is the shared, unmodified standard base;
              sadot.css is the thin project-layer override; feedback.js /
              hub-form-exports.js are generic, parameterized export scripts)
  ssot/     — validated feedback exports after ingestion (manifest.json + responses/)
  dist/     — build output (git-ignored, regenerated — do not edit by hand)
```

## Build locally

From the repo root:

```bash
python3 scripts/build_sadot_client_hub.py
python3 -m http.server 8000 --directory hub/dist
# open http://localhost:8000/
```

`--out <dir>` overrides the output directory (default `hub/dist`).

## Pages

| Page | Data source | Notes |
|------|-------------|-------|
| `index.html` | `updates.json`, `roadmap.json`, `tasks.json`, `decisions.json` | Landing page, stats, recent updates log |
| `roadmap.html` | `roadmap.json` | Milestones table + current focus |
| `tasks.html` | `tasks.json` + `decisions.json` | Merged view: decisions accordion (with JSON export) + task list |
| `meeting.html` | `meeting-brief.json` | Meeting prep/agenda |
| `what-we-need.html` | `what-we-need.json` | Prioritized client-input list |
| `materials-needed.html` | `materials-needed.json` | Materials/photos/approvals tracker |

## What's deliberately not here

Per `CLIENT_HUB_STANDARD_v1.md` §7 replication checklist, this hub was pruned down from
the EyalAmit.co.il-2026 pattern to only the pages relevant to a landscape-architecture
engagement. **Not included** (all were WordPress-migration-specific views on the source
hub, not applicable here): site-tree, media-intake, content-proposals, content-intake,
legacy-unmapped, testimonials-curation, analytics-config, page-review.

## Deployment

**Not yet configured.** The hosting target for this project is TBD, so there is no
`deploy_sadot_client_hub.py` / `ftp_publish_*` script yet. Per the standard (§9), the Hub
is platform-agnostic — once a hosting target is chosen (VPS, cloud storage, uPress, CI/CD,
etc.), add a project-specific deploy script following the pattern documented there. For
now, use `python3 -m http.server` against `hub/dist/` for local preview only.

Feedback **ingestion** (`ingest_sadot_feedback_json.py`, validating exported JSON against
`decisions.json` IDs and writing to `hub/ssot/`) is also not yet built — add it when the
first real decision-answer export needs to be ingested.

## Provenance

Adapted from:

- `EyalAmit.co.il-2026/hub/` (structure, build-script architecture, CSS/JS foundation) —
  **read-only reference**, no client content or real data was copied; only the generic
  code/template/schema shape.
- `SmallFarmsAgents` — [`CLIENT_HUB_STANDARD_v1.md`](../../SmallFarmsAgents/docs/CLIENT_HUB_STANDARD_v1.md)
  (canonical schema definitions, replication checklist, branding/CSS standard) and its
  `hub/data/decisions.json` + `tasks.json` (clean standard shape, used as the reference
  for Sadot's own decisions/tasks schema instead of EyalAmit's more embellished variant).

Renamed constants relative to `build_eyal_client_hub.py` (see
`scripts/build_sadot_client_hub.py` header comment for the full list):
`EXPORT_TYPE` → `sadot-feedback`, `DEFAULT_RESPONDENT` → `Niv Sadot`, `PROJECT_META` →
`Sadot2026`, decision-ID prefix `D-EYAL-` → `D-SADOT-`, page-ref prefix `EA-` → `NS-`
(reserved; unused until/unless a site-tree page is added).
