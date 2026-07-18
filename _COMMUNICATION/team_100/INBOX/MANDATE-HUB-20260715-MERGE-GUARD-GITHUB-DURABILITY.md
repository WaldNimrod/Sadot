---
id: MANDATE-HUB-20260715-MERGE-GUARD-GITHUB-DURABILITY
type: MANDATE (hub team_100 → sadot domain session)
from: team_100 (hub — Chief System Architect)
to: sadot domain session (team_100 / team_110 / team_60 — whoever owns git push)
date: 2026-07-15
priority: normal — NON-URGENT, act when you reach a safe checkpoint
status: PARTIAL — see ACK_MANDATE-HUB-20260715-MERGE-GUARD-GITHUB-DURABILITY.md (merge-guard on origin/main @ 871f080; Blender FF blocked by GH001)
re: close the Autonomous-Merge-Policy fleet-propagation loop for sadot (GitHub durability)
---

# MANDATE — push the merge-guard propagation commit to GitHub (complete from your side)

## תקציר (Hebrew tl;dr)
מדיניות ה‑Autonomous Merge Policy כבר הופצה אליכם ונמצאת מקומית (הקומיט קיים, ה‑hook פעיל).
מה שחסר: דחיפה ל‑GitHub. אצלכם יש גם 19 קומיטים של עבודת Blender שלא נדחפו — דחיפה אחת (`git push origin main`)
מעלה גם את עבודת ה‑Blender שלכם וגם את קומיט ה‑merge‑guard יחד. Fast‑forward, בלי rebase. אין דחיפות.

## What happened
The hub rolled out the **Autonomous Merge Policy** (ADR052 addendum — a deterministic `gh pr merge`
guard hook + `.claude/settings.json` wiring + validate Check 77). `aos_sync_all.sh` propagated it to every
domain. On sadot the propagation commit landed **locally** and is already committed:

```
f5b9e2d gov(aos-sync): propagate hub e728664 → tracked set (Model B / ADR054)
```

The merge-guard is **already active in your local tree**. The only remaining gap is **GitHub durability** —
the commit was never pushed, because your Blender session was active with unpushed work when the fleet push
ran, so the hub did not push on your behalf.

## Your git state (as of 2026-07-15)
- `main` is **behind 0 / ahead 23** of `origin/main` → **NOT diverged**; a clean fast-forward push.
- The 23 unpushed commits are: **4 `gov(aos-sync)` governance commits** (incl. the merge-guard `f5b9e2d`)
  **+ 19 of your own `feat(sadot)` Blender commits** that were never pushed.
- Working tree has ~5 uncommitted files (your live Blender work) — `git push` ships committed history only.

## MANDATE (complete when convenient — NOT blocking your work)
1. At a natural checkpoint, run:
   ```bash
   git -C "/Users/nimrod/Documents/AOS_V5/Sadot" push origin main
   ```
   This publishes **your 19 Blender commits + the merge-guard commit together** to `origin/main`
   (this is expected and desirable — your Blender history has not been backed up to GitHub yet either).
2. Your **pre-push hook runs `validate_aos.sh`**. If it flags uncommitted WIP, commit or `git stash` first,
   then push. No rebase/merge needed (you are behind 0).
3. Confirm: `git -C … rev-list --left-right --count origin/main...HEAD` → expect `0  0`.
4. Reply / ack to hub `_COMMUNICATION/team_100/` so the hub can close the loop for sadot.

## Effect if you do nothing for now
Merge-guard is already live locally. Exposure: a **fresh clone** wouldn't have the hook, **and your 19
Blender commits remain un-backed-up on GitHub** until this push lands — so there is a mild data-durability
reason to push sooner here than on other domains.

## Reference
- Policy: hub `governance/directives/ADR052_ADDENDUM_AUTONOMOUS_MERGE_POLICY_v1.0.0.md`
- Content SHA note: the real propagated content is `hub e728664` (the PR #47 merge that contains the hook).

── Activation prompt (copy-paste to the sadot session) ──
```
You are the sadot domain session (team_100/team_110/team_60). Governance + backup task, non-urgent:
your main is behind 0 / ahead 23 (4 gov commits incl. the Autonomous-Merge-Policy propagation, plus 19 of
your own feat(sadot) Blender commits) — a clean fast-forward. When you reach a safe checkpoint:
  1) if uncommitted WIP would fail pre-push validate, commit or `git stash` it first;
  2) `git push origin main`  (ships your Blender history + the merge-guard commit; pre-push runs
     validate_aos.sh — expect PASS, Check 77 green);
  3) verify `git rev-list --left-right --count origin/main...HEAD` == `0  0`;
  4) ack back to hub team_100 to close the loop.
Do NOT rebase/merge (not diverged). Full mandate:
_COMMUNICATION/team_100/INBOX/MANDATE-HUB-20260715-MERGE-GUARD-GITHUB-DURABILITY.md
```
── End block ──

— team_100 (hub) · 2026-07-15
