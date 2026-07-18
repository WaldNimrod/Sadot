---
id: ACK_MANDATE-HUB-20260715-MERGE-GUARD-GITHUB-DURABILITY
type: ACK (spoke → hub team_100)
for_hub: true
from: sadot domain session (team_100 / team_110)
to: team_100 (hub — Chief System Architect)
date: 2026-07-15
re: MANDATE-HUB-20260715-MERGE-GUARD-GITHUB-DURABILITY
status: PARTIAL — merge-guard durable on GitHub; Blender history blocked by GH001
origin_repo: /Users/nimrod/Documents/AOS_V5/Sadot
---

# ACK — merge-guard on GitHub; Blender FF blocked by GitHub 100 MB limit

## Mandate outcome

| Goal | Result |
|------|--------|
| Merge-guard (`gh_merge_guard.sh` + `.claude/settings.json` PreToolUse wiring) on `origin/main` | **DONE** |
| Pre-push `validate_aos.sh` / Check 77 | **PASS** (46 PASS / 0 FAIL on push) |
| Full FF of all 23 local commits → `0  0` | **BLOCKED** (GH001) |
| 19 Blender `feat(sadot)` commits on GitHub | **BLOCKED** (files 459–543 MB > 100 MB) |

## What landed on GitHub

1. **Fast-forward chunk 1** (no large blobs): `fa84aa2..42a161f` — 11 Blender/site commits through `style(sadot): darken ground fill material`.
2. **Next FF of `978bc43` rejected** by GitHub pre-receive:
   ```
   GH001: Large files detected
   File blender/sadot_v18_planting_pool_staging_2026-07-14.blend is 459.37 MB;
   this exceeds GitHub's file size limit of 100.00 MB
   ```
   (Earlier single-pack push of all 23 also failed: `pack exceeds maximum allowed size (2.00 GiB)`.)
3. **Merge-guard durability workaround** (no rebase of local Blender history): cherry-picked the 4 `gov(aos-sync)` commits (`6cb0ff6`…`f5b9e2d`) onto `origin/main` @ `42a161f` in a disposable worktree, then pushed from the main worktree so pre-push validate could run:
   - `origin/main` tip: **`871f080`** — `gov(aos-sync): propagate hub e728664 → tracked set (Model B / ADR054)`
   - Confirmed on origin: `scripts/hooks/gh_merge_guard.sh` (mode 100755) + `.claude/settings.json` wires `Bash(gh pr merge:*)` → `gh_merge_guard.sh`

## Current sync state (not `0  0`)

```
git rev-list --left-right --count origin/main...HEAD
4	12
```

- **merge-base:** `42a161f` (darken ground fill)
- **origin/main:** `871f080` (cherry-picked gov tip — merge-guard present)
- **local `main`:** `f5b9e2d` (original linear history: 8 large Blender commits + original 4 gov SHAs)
- **safety ref:** `backup/main-with-blender-pre-gh001` → `f5b9e2d`

Local and origin have **diverged** solely because GitHub cannot accept the ~460–570 MB `.blend` blobs that sit between `42a161f` and the original gov tip. Content of merge-guard on origin matches the propagation; commit SHAs for the 4 gov commits differ from local.

## Ask for hub / Team 00

To reunify and get Blender durability on GitHub without leaving large binaries in plain git:

1. **Approve Git LFS** for `*.blend` (and likely `blender/assets/**`), then `git lfs migrate import` + coordinated force-with-lease of `main` (history rewrite — needs explicit Team 00 OK), **or**
2. Keep Blender binaries out of GitHub (external backup / LFS later) and leave origin at gov tip `871f080` while local retains full model history.

Until then: merge-guard is live locally **and** durable on GitHub for fresh clones of `main`. Blender checkpoint history remains Mac-local only for the 8 oversized commits.

## Mandate file

Spoke inbox: `/Users/nimrod/Documents/AOS_V5/Sadot/_COMMUNICATION/team_100/INBOX/MANDATE-HUB-20260715-MERGE-GUARD-GITHUB-DURABILITY.md` — treat operational status as **PARTIAL** per this ACK.

— sadot domain session · 2026-07-15
