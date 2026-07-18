---
id: ACK_MANDATE-HUB-20260715-SADOT-PUBLISH-LEAN-BLEND
type: ACK (spoke → hub team_100)
for_hub: true
from: sadot domain session (team_100 / team_110 — Blender owner)
to: team_100 (hub — Chief System Architect)
date: 2026-07-15
re: MANDATE-HUB-20260715-SADOT-PUBLISH-LEAN-BLEND
status: DONE — publish-lean ACHIEVED
origin_repo: /Users/nimrod/Documents/AOS_V5/Sadot
---

# ACK — publish-lean feasibility PROVED

## Canon proof (the number you asked for)

| Metric | Value |
|--------|-------|
| **ACHIEVED lean file size** | **504 234 bytes ≈ 492 KB** |
| Path | `/Users/nimrod/Documents/AOS_V5/Sadot/blender/milestones/sadot_current.blend` |
| vs GitHub 100 MB limit | **~0.48% of limit** |
| vs prior baked working file | 554 MB → 492 KB (**~1128× smaller**) |
| Method | Removed baked BlenderKit appends; **57 collection instances LINKED** from `blender/assets/models/*.blend`; unpack textures; purge; Save As compressed |

**Verdict:** publish-lean is **feasible for Sadot**. Team-00 versioning canon is ratified by this pilot.

## Git / sync

```
commit: c460106 feat(sadot): publish-lean milestone .blend (linked assets, <100MB) — Team-00 versioning canon
origin/main...HEAD → 0  0
.gitignore: *.blend + !blender/milestones/*.blend
pre-push: tracked *.blend >95 MB now FAILs (GH001 guard)
```

`blender/CURRENT_MODEL.md` now points TRACKED SSoT → milestones; heavy `sadot_v25_…2026-07-15.blend` stays local/off-git.

## Off-machine backup

| Layer | Result |
|-------|--------|
| Local `_BACKUPS_OFFGIT/sadot-blend-latest/` | DONE (~4.5 GB) |
| Local dated snapshot + git bundle (~3.0 GB) | DONE (`--bundle`) |
| `rsync` → `nimrod@100.125.98.56:~/Backups/` | **SKIPPED** — agent sandbox still blocks SSH to Tailscale host (`Operation not permitted` on port 22) |

Operator one-liner when Tailscale/SSH is available from a normal Terminal:

```bash
bash /Users/nimrod/Documents/AOS_V5/Sadot/scripts/backup_blender_binaries.sh --remote --bundle
```

## Viewport check

After linking: house, deck, pool, stones, table/chairs, tree labels present; 17 library links loaded; authored mesh verts ~9k local.

— sadot domain session · 2026-07-15
