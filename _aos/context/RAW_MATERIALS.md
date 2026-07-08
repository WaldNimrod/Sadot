# RAW MATERIALS — Sadot (tracked canon reference to the git-ignored `raw-materials/` folder)

Every AOS project keeps a **`raw-materials/`** folder at the repo root for un-curated source material and client
exchange. This tracked file documents it; the folder itself is **git-ignored** (it can balloon — photos, drone
imagery, CAD/DWG, PDFs, surveys) and is intended to be **auto-synced against a Google Drive folder**.

## Structure (uniform)
| Path | Purpose (he) | Contents |
|------|--------------|----------|
| `raw-materials/from-client/` | קבלת חומרים מהלקוח | materials RECEIVED from Niv Sadot — plot survey, photos, references, permits, prior plans |
| `raw-materials/to-client/`   | הגשות ללקוח | submissions/deliverables TO the client — rendered plans, planting lists, BOQ, decks (versioned) |
| `raw-materials/working/`     | — | scratch / unsorted raw material |

## Rules
- **Never git-add** anything under `raw-materials/` — it is git-ignored by design (`.gitignore` → `/raw-materials/`).
- **Drive sync:** point Google Drive Desktop (or `rclone`) at `raw-materials/` so the source pile + client exchange
  live off-git in one synced place. (Sync setup is the operator's Drive config; the folder + ignore is the AOS infra.)
- **Curation flow:** raw source lands in `from-client/` → the domain teams curate the relevant subset INTO the tracked
  `knowledge/` KB + `design/` dossier. `raw-materials/` = the un-curated pile; `knowledge/`+`design/` = the canon outputs.
- Registered in `_aos/project_identity.yaml` `allowed_write_roots`.

> **Canon status:** implemented here for Sadot (the vNext exemplar). A fleet-wide standard — every project gets this
> folder via the create-project scaffold + `.gitignore` template — is proposed to team_100 for later canonization.
