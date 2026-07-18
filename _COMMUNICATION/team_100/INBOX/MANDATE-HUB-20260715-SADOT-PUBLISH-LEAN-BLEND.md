---
id: MANDATE-HUB-20260715-SADOT-PUBLISH-LEAN-BLEND
type: MANDATE (hub team_100 → sadot domain session)
from: team_100 (hub — Chief System Architect)
to: sadot domain session (team_100 / team_110 — owns Blender)
date: 2026-07-15
priority: normal — supersedes the interim blanket *.blend ignore
status: DONE — see ACK_MANDATE-HUB-20260715-SADOT-PUBLISH-LEAN-BLEND.md (lean size 492 KB / 504234 bytes; origin 0 0)
re: Team-00 chose PUBLISH-LEAN — commit a <100 MB linked-asset milestone .blend; prove feasibility
depends_on_canon: PROPOSAL_3D_ASSET_VERSIONING_CANON_2026-07-15_v1.0.0.md (hub team_100) — this is the pilot
---

# MANDATE — publish-lean: make the latest model committable (<100 MB) via LINKED assets

## תקציר (Hebrew)
Team 00 בחר **publish-lean**: לגרסן ב‑git את הקובץ האחרון — אבל **רזה מתחת ל‑100MB**. אצלך זה קל: כל 554MB
הם נכסי BlenderKit **מוטמעים**; הגיאומטריה עצמה <500KB. צור גרסת milestone עם נכסים **מקושרים (linked)**
במקום baked → צפוי <1MB → commit ל‑`blender/milestones/` ודחיפה ל‑GitHub. הקובץ הכבד נשאר מקומי+גיבוי.
**דווח לי את הגודל שהתקבל** — זו הוכחת ההיתכנות לקאנון.

## Why this supersedes the blanket ignore
The interim policy ignored **all** `.blend` → nothing is versioned (fails team_00's "commit the latest").
team_00 chose **publish-lean**: keep a **committable milestone** file small enough for plain git on GitHub.

## Why it's easy here (verified by hub)
- Your authored geometry is **tiny**: v5–v11 `.blend` are **373–407 KB**.
- The **554 MB** in v25 is **entirely baked BlenderKit assets** (pool, ready-made trees, furniture).
- `blender/assets/` (**319 MB** BlenderKit cache) is **already gitignored** and re-downloadable.
- ⇒ **Link** those assets instead of baking them and the milestone `.blend` should drop to **< 1 MB**.

## MANDATE — runbook
1. **Produce a lean milestone from the current model** (in Blender):
   - Replace the appended/baked BlenderKit assets with **linked** library refs (`File > Link`, pointing into
     `blender/assets/models/…`), OR remove-then-link. Keep all YOUR authored geometry.
   - `File > External Data > Unpack … Into Files` (don't pack textures), then `File > Clean Up > Purge All`.
   - **Save As** → `blender/milestones/sadot_current.blend` (create `blender/milestones/`).
   - `ls -lh blender/milestones/sadot_current.blend` → **must be < 100 MB** (expect < a few MB).
2. **Track milestones, keep working files ignored** — set `.gitignore` to:
   ```gitignore
   # Blender heavy working saves: OFF git (baked assets) — Team-00 policy 2026-07-15
   *.blend
   # EXCEPT lean committable milestones (<100 MB, assets LINKED not baked) — publish-lean canon
   !blender/milestones/*.blend
   ```
3. **Verify + commit + push:**
   ```bash
   cd "/Users/nimrod/Documents/AOS_V5/Sadot"
   test "$(stat -f%z blender/milestones/sadot_current.blend)" -lt 104857600 || { echo "STILL >100MB — STOP, see fallback"; }
   git add .gitignore blender/milestones/sadot_current.blend blender/CURRENT_MODEL.md
   git commit -m "feat(sadot): publish-lean milestone .blend (linked assets, <100MB) — Team-00 versioning canon"
   git push origin main
   git rev-list --left-right --count origin/main...HEAD   # expect 0 0
   ```
4. **Update `blender/CURRENT_MODEL.md`**: note the committed lean milestone = the tracked SSoT; the heavy
   fully-baked working file stays local-only + off-git backup (assets are re-linkable from `blender/assets/`).
5. **Off-machine backup** (still pending from last mandate — do it): 
   `bash scripts/backup_blender_binaries.sh --remote --bundle`
6. **Size guard (recommended):** add to `scripts/hooks/pre-push_validation.sh` a check that FAILs if any
   **tracked** `*.blend` exceeds ~95 MB — so GH001 can never recur. (Or flag to team_60 to add fleet-wide.)

## ⚠ Fallback — if the lean file is STILL > 100 MB
Then linking didn't shrink it enough (authored geometry itself is heavy). **Do NOT force a >100 MB blob.**
Keep that milestone local-only + off-git backup, note it in `CURRENT_MODEL.md`, and **ACK back that
publish-lean did NOT achieve <100 MB** — that's an important feasibility signal; the hub will reconsider the
canon (LFS / self-hosted remote) for your domain. (Given your <500 KB geometry this is very unlikely.)

## ACK
Reply `for_hub: true` to hub `_COMMUNICATION/team_100/` with: the achieved lean file **size**, `0 0` proof,
and whether the off-machine backup ran. The size is the pilot proof that ratifies (or reopens) the canon.

── Activation prompt (copy-paste to the sadot session) ──
```
You are the sadot domain session (owns Blender). Team 00 chose PUBLISH-LEAN for Blender versioning.
Your model is 554MB ONLY because BlenderKit assets are baked in — your geometry is <500KB, and
blender/assets/ (319MB) is already gitignored + re-linkable. Make the latest model committable <100MB:
  1) In Blender: replace baked BlenderKit assets with LINKED refs into blender/assets/models/, unpack
     textures, Clean Up > Purge All, Save As blender/milestones/sadot_current.blend; confirm ls -lh <100MB.
  2) .gitignore: keep `*.blend` ignored but add `!blender/milestones/*.blend`.
  3) git add the milestone + .gitignore + CURRENT_MODEL.md; commit; git push origin main; verify 0 0.
  4) Run scripts/backup_blender_binaries.sh --remote --bundle (off-machine backup still pending).
  5) ACK for_hub with the ACHIEVED lean-file SIZE (this is the canon feasibility proof).
If it's still >100MB after linking: do NOT force it — keep local, ACK that publish-lean failed to shrink it.
Full mandate: _COMMUNICATION/team_100/INBOX/MANDATE-HUB-20260715-SADOT-PUBLISH-LEAN-BLEND.md
```
── End block ──

— team_100 (hub) · 2026-07-15
