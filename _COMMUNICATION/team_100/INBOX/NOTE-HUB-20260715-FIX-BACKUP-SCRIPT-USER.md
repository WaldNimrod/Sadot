---
id: NOTE-HUB-20260715-FIX-BACKUP-SCRIPT-USER
type: NOTE (hub team_100 → sadot domain session)
from: team_100 (hub — Chief System Architect)
date: 2026-07-15
priority: normal
re: backup_blender_binaries.sh targets a non-existent SSH user → off-machine backup silently skipped
---

# Fix — `backup_blender_binaries.sh` default SSH user is wrong

team_99 (server-resident) verified on waldhomeserver: **the sadot off-machine backup NEVER landed** — zero
`.blend` / bundles on the server. Root cause: the script targets user **`nimrod`**, which **does not exist**
on the server (only **`nimrodw`**). The rsync is guarded by `if ssh BatchMode … then rsync`, so a bad user
makes the transfer **silently skip** — no error surfaced. So the ~7.5 GB of heavy `.blend` + the 3 GB history
bundle are still **only on this Mac** (a real single-point-of-failure for "very important" files).

## Update (2026-07-15, after re-runs)
Re-running with `nimrodw@` connected, but the transfer was **partial + silent**: the latest dir arrived only
partially and the **3 GB bundle never transferred** — with no error surfaced. NOT a disk-space issue
(server `/` has 67 GB free, `/data` 844 GB). Root causes = (a) wrong default user, (b) remote target
`~/Backups` is on the OS root volume (wrong place for large/growing binary backups — `/data` is the dedicated
volume, already home to `/data/backups` DB dumps), (c) no rsync error-check → silent partials.

## Fix (3 changes) — `scripts/backup_blender_binaries.sh`
- **user** — line 35: `…:-nimrod@100.125.98.56}` → `…:-nimrodw@100.125.98.56}` (+ line 12 doc).
- **target** — remote path `~/Backups/…` → **`/data/backups/sadot-blend/…`** (dedicated 844 GB volume; the
  home/root volume is the wrong place for multi-GB backups).
- **fail-loud** — check the `rsync` exit code when `--remote` was requested; **exit non-zero** on any failure
  or partial (do NOT fall through to a success echo). Optionally verify remote size ≈ local after transfer.

(Server host per the `/server` canon: LAN `10.100.102.2` at home, else Tailscale `100.125.98.56`, user `nimrodw`.)

## Then verify it actually lands
The **operator** runs the re-run from the Mac (rsync is a Mac→server push; agent SSH is classifier-blocked):
```bash
SADOT_BLEND_REMOTE=nimrodw@100.125.98.56 bash /Users/nimrod/Documents/AOS_V5/Sadot/scripts/backup_blender_binaries.sh --remote --bundle
```
Then confirm via team_99 on the server: `ls -lh ~/Backups/sadot-blend-latest/ && du -sh ~/Backups/sadot-blend-latest`.

## Optional hardening
Make the script **fail loud** if the remote `ssh` check fails while `--remote` was requested (exit non-zero
instead of silently skipping) — so a future wrong-user/unreachable case surfaces immediately.

— team_100 (hub) · 2026-07-15
