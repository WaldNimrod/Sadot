---
id: ACK_MANDATE-HUB-20260715-SADOT-BLENDER-BINARY-POLICY
type: ACK (spoke → hub team_100)
for_hub: true
from: sadot domain session (team_100 / team_110)
to: team_100 (hub — Chief System Architect)
date: 2026-07-15
re: MANDATE-HUB-20260715-SADOT-BLENDER-BINARY-POLICY
status: DONE
origin_repo: /Users/nimrod/Documents/AOS_V5/Sadot
---

# ACK — Blender binaries off GitHub; `main` reunified (`0  0`)

## Outcome

| Step | Result |
|------|--------|
| 0. Stash WIP | DONE (`pre-binary-policy WIP`) |
| 1. Off-repo backup of v18–v25 + git bundle | DONE (see paths below) |
| 2. `git reset --hard origin/main` → `871f080` | DONE |
| 3. `*.blend` gitignored + `git rm --cached` + commit | DONE → `f52642d` |
| 4. Restore latest working `.blend` (untracked) | DONE — `sadot_v25_contour_lines_2026-07-15.blend` (554 MB) |
| 5. `git push` + verify | DONE — **`0  0`** |
| 6. Stash pop / WIP restore | DONE (comms artifacts restored; v25 already on disk) |
| Routine off-git backup | DONE — `scripts/backup_blender_binaries.sh` pushed |

## Sync proof

```
origin/main...HEAD → 0  0
origin/main tip: (policy + backup-script commits on top of merge-guard 871f080)
tracked blender/*.blend count: 0
Check 77: still PASS on pre-push
```

## Backup locations

Primary (this Mac; session sandbox blocked `~/Backups` + SSH to waldhomeserver):

- Bundle: `/Users/nimrod/Documents/AOS_V5/Sadot/_BACKUPS_OFFGIT/sadot-blender-history-2026-07-15.bundle` (~3.0 GB, from `backup/main-with-blender-pre-gh001`)
- Flat copies v18–v25 (incl. both v25 dates): `/Users/nimrod/Documents/AOS_V5/Sadot/_BACKUPS_OFFGIT/sadot-blend-latest/` (~4.5 GB)
- Dir is gitignored via `/_BACKUPS_OFFGIT/`

Local history branch retained: `backup/main-with-blender-pre-gh001` → `f5b9e2d`

**Remote rsync to waldhomeserver:** SKIPPED this session (SSH `100.125.98.56:22` not permitted from the agent sandbox). Operator can run:

```bash
bash /Users/nimrod/Documents/AOS_V5/Sadot/scripts/backup_blender_binaries.sh --remote --bundle
```

## Policy on `main`

- `.gitignore`: `*.blend` + `/_BACKUPS_OFFGIT/`
- All previously tracked `blender/*.blend` removed from the index (files may remain on disk as ignored working copies)
- Routine backup entrypoint: `/Users/nimrod/Documents/AOS_V5/Sadot/scripts/backup_blender_binaries.sh`

Sadot merge-guard + binary-policy loop: **closed from the spoke side**.

— sadot domain session · 2026-07-15
