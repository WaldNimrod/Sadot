# Sadot Client Hub

Static client-facing status hub for **Niv Sadot (ניב שדות)** — landscape-architecture /
garden-design project for a private house in Pardes Hanna.

## What this is

A view-and-coordination layer (not a replacement for formal deliverables) that shows the
client, in one place: roadmap status, open tasks, open decisions requiring input, a
meeting brief, and a prioritized "what we need from you" list. Client decision answers
can be exported as JSON from the browser (no server round-trip) for later ingestion into
`hub/ssot/`.

Most `hub/data/*.json` files are still empty scaffolding (schema-valid, no content yet) —
`decisions.json`, `tasks.json`, `updates.json`, `roadmap.json`, `meeting-brief.json`,
`what-we-need.json` will populate once the landscape-design engagement enters its
content/decisions phase. **Exception:** `materials-needed.json` is already populated —
the first real client materials batch (survey, IFC model, sketches, voice brief) arrived
2026-07-08 and is tracked there.

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
| `index.html` | `updates.json`, `roadmap.json`, `tasks.json`, `decisions.json`, `questions.json` | Landing page, stats, recent updates teaser |
| `questions-decisions.html` | `questions.json` + `established-guidance.json` | Numbered open questions (each tagged who it's waiting on) + a plain-language summary of Niv's own established guidance so far |
| `tasks.html` | `tasks.json` + `decisions.json` | Merged view: formal decisions accordion (with JSON export) + task list — distinct from `questions-decisions.html`: this page is for structured decisions with an exportable answer, not the running list of open clarifying questions |
| `roadmap.html` | `roadmap.json` | Milestones table + current focus |
| `updates.html` | `updates.json` | Full, dated changelog — every hub-facing update gets an entry here (see "Keeping this hub current" below) |
| `meeting.html` | `meeting-brief.json` | Meeting prep/agenda |
| `what-we-need.html` | `what-we-need.json` | Prioritized client-input list |
| `materials-needed.html` | `materials-needed.json` | Materials/photos/approvals tracker |

## Keeping this hub current

Every hub-facing change (a new question, an answered one, a new milestone, a corrected fact) should:

1. Update the owning data file first (`questions.json`, `established-guidance.json`, `roadmap.json`, etc.) —
   never hand-edit anything under `dist/`.
2. Add a new entry to `updates.json` (newest on top: `id`, `date`, `titleHe`, `bodyHe`) — one line, written for
   Niv, describing what changed and when. This is what `updates.html` and the index teaser render.
3. Rebuild (`python3 scripts/build_sadot_client_hub.py`) and redeploy (see Deployment below).

This mirrors the update discipline used on the `IsraelMicrogreens` project's client hub
(`CLIENT_HUB_UPDATE_PROCEDURE.md`), simplified for Sadot's single-script build (no separate SoT/template
layer to keep in sync).

## Nav

All 8 pages share one nav bar, defined in exactly one place: `HUB_NAV_ITEMS` +
the `nav()` function in `scripts/build_sadot_client_hub.py`. Adding a page = adding one tuple to that list —
never hand-write a `<nav>` block in a page function.

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
