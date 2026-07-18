---
id: MANDATE-HUB-20260715-SADOT-BLENDER-BINARY-POLICY
type: MANDATE (hub team_100 → sadot domain session)
from: team_100 (hub — Chief System Architect)
to: sadot domain session (team_100 / team_110 / team_60 — whoever owns git)
date: 2026-07-15
priority: normal — do at your next safe Blender checkpoint (NOT urgent; merge-guard already durable)
status: DONE — see ACK_MANDATE-HUB-20260715-SADOT-BLENDER-BINARY-POLICY.md (origin/main == local main == 0 0)
re: Team-00 ratified binary policy — keep large .blend OFF GitHub; reunify main to the blob-free lineage
supersedes_partial: ACK_MANDATE-HUB-20260715-MERGE-GUARD-GITHUB-DURABILITY.md (this closes the "Ask for hub/Team 00")
---

# MANDATE — keep Blender binaries off GitHub + reunify `main` (Team-00 decision)

## תקציר (Hebrew)
Team 00 החליט: **קבצי .blend הכבדים לא עולים ל‑GitHub.** ה‑merge-guard כבר durable על origin (`871f080`).
מה שנשאר: (1) לגבות את ה‑.blend הכבדים החוצה, (2) להחזיר את local `main` ל‑origin (שכבר נקי מ‑blobs),
(3) gitignore ל‑`*.blend`, (4) לדחוף → 0/0. **זהירות: `reset --hard` ימחק את v18–v25 מהדיסק — לגבות קודם!**

## Decision (ratified 2026-07-15, Team 00 / Principal)
Chosen path: **keep large Blender binaries out of plain git** (NOT Git LFS). Rationale: GitHub is the
governance/text SSoT, not a large-binary store; AOS already backs large binaries to disk/zip (dup-dir
migration precedent); LFS adds recurring quota cost + history-rewrite risk + heavy clones for private
working binaries. Full Blender checkpoint history is preserved locally (backup branch + off-git backup).

## Current facts (verified by hub)
- `origin/main` = `871f080` is **already blob-free** — it contains only the small `sadot_v1..v17*.blend`
  (<1 MB each) + the merge-guard. Merge-guard durability: **DONE**, nothing more needed there.
- The 8 oversized commits (v18–v25 `.blend`, 459–543 MB — BlenderKit assets baked in) exist ONLY on
  local `main` (`f5b9e2d`) and on `backup/main-with-blender-pre-gh001`. They are the GH001 blockers.
- `.gitignore` already ignores `*.blend1/2` + `/blender/assets/` (BlenderKit cache) but NOT `*.blend`.

## MANDATE — runbook (do at a safe checkpoint; read the ⚠ before running anything)
> ⚠ **DATA-LOSS WARNING:** `git reset --hard origin/main` will **delete v18–v25 `.blend` from your working
> tree** (they don't exist at `871f080`). Your **latest model is v25 (543 MB)** — back it up OFF the repo
> FIRST. Also stash/commit any live WIP first.

```bash
cd "/Users/nimrod/Documents/AOS_V5/Sadot"

# 0. Preserve live WIP
git stash push -u -m "pre-binary-policy WIP"        # or commit it

# 1. Back up ALL Blender history + the latest working models OFF the repo (belt + suspenders)
git bundle create ~/Backups/sadot-blender-history-2026-07-15.bundle backup/main-with-blender-pre-gh001
mkdir -p ~/Backups/sadot-blend-latest
cp blender/sadot_v1[89]*.blend blender/sadot_v2*.blend ~/Backups/sadot-blend-latest/   # v18..v25
#   (recommended: also rsync ~/Backups/sadot-blend-latest to waldhomeserver)

# 2. Reunify main to the blob-free lineage (origin) — deletes v18..v25 from the tree (backed up in step 1)
git checkout main
git reset --hard origin/main        # main == 871f080

# 3. Keep .blend off git going forward + drop the small tracked ones so main is fully .blend-free
printf '\n# ── Blender working binaries: kept OFF git (Team-00 policy 2026-07-15) ──\n*.blend\n' >> .gitignore
git rm --cached --quiet blender/*.blend 2>/dev/null || true
git add .gitignore
git commit -m "chore(sadot): keep Blender .blend binaries off git (Team-00 policy 2026-07-15) — back up off-repo"

# 4. Restore the latest working model for continued work (now untracked/gitignored)
cp ~/Backups/sadot-blend-latest/sadot_v25_contour_lines_2026-07-14.blend blender/   # + any others you need

# 5. Push — clean, no blobs
git push origin main
git rev-list --left-right --count origin/main...HEAD   # expect: 0  0

# 6. Re-apply your WIP
git stash pop        # resolve any conflicts; .blend now untracked so they won't re-enter git
```

## After this
- `origin/main` == local `main` == `0  0`; **future `aos_sync` propagations push cleanly** (no recurring
  GH001/divergence). Merge-guard stays durable.
- Blender history lives in: `backup/main-with-blender-pre-gh001` (local) + the `.bundle` + the off-git
  `.blend` copies. Establish a routine backup of `blender/*.blend` (periodic zip/rsync to disk or
  waldhomeserver) since they're no longer versioned in git.
- If you deliberately want the small early `v1..v17.blend` kept on GitHub as lightweight design history,
  skip the `git rm --cached` in step 3 and narrow the ignore to the heavy ones — your call.

## ACK
Reply with an ACK (`for_hub: true`) to hub `_COMMUNICATION/team_100/` confirming `0  0` + the backup
location, so the hub marks sadot fully closed.

── Activation prompt (copy-paste to the sadot session) ──
```
You are the sadot domain session. Team 00 ratified: keep large Blender .blend OFF GitHub (NOT LFS).
merge-guard is already durable on origin (871f080). Now reunify main + set the binary policy.
Full runbook (READ the DATA-LOSS warning — reset --hard deletes v18–v25 from disk; back them up first):
_COMMUNICATION/team_100/INBOX/MANDATE-HUB-20260715-SADOT-BLENDER-BINARY-POLICY.md
Steps: (0) stash WIP; (1) git bundle the backup branch + copy v18–v25 .blend off-repo (ideally rsync to
waldhomeserver); (2) git reset --hard origin/main; (3) add `*.blend` to .gitignore + git rm --cached
blender/*.blend + commit; (4) restore latest .blend (v25) as untracked; (5) git push → verify 0 0;
(6) git stash pop. Then set a routine off-git backup of blender/*.blend and ACK for_hub to the hub.
```
── End block ──

— team_100 (hub) · 2026-07-15
