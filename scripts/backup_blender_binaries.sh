#!/usr/bin/env bash
# backup_blender_binaries.sh — off-git backup of Blender working binaries (Team-00 policy 2026-07-15)
#
# Why: *.blend are gitignored (GH001 / not LFS). This script is the durability path.
# Usage:
#   bash scripts/backup_blender_binaries.sh              # local _BACKUPS_OFFGIT only
#   bash scripts/backup_blender_binaries.sh --remote      # also rsync to waldhomeserver if reachable
#   bash scripts/backup_blender_binaries.sh --bundle      # also refresh git bundle of backup branch
#
# Ports: none. Env:
#   SADOT_BLEND_BACKUP_DIR  override local backup root (default: <repo>/_BACKUPS_OFFGIT)
#   SADOT_BLEND_REMOTE      override SSH target (default: nimrod@100.125.98.56)

set -euo pipefail

REPO_ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel 2>/dev/null || true)"
REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
cd "$REPO_ROOT"

DO_REMOTE=0
DO_BUNDLE=0
for arg in "$@"; do
  case "$arg" in
    --remote) DO_REMOTE=1 ;;
    --bundle) DO_BUNDLE=1 ;;
    -h|--help)
      sed -n '2,14p' "$0"
      exit 0
      ;;
  esac
done

BACKUP_ROOT="${SADOT_BLEND_BACKUP_DIR:-$REPO_ROOT/_BACKUPS_OFFGIT}"
LATEST_DIR="$BACKUP_ROOT/sadot-blend-latest"
REMOTE="${SADOT_BLEND_REMOTE:-nimrod@100.125.98.56}"
STAMP="$(date +%Y-%m-%d)"

mkdir -p "$LATEST_DIR"

shopt -s nullglob
BLENDS=(blender/*.blend)
if [ ${#BLENDS[@]} -eq 0 ]; then
  echo "[blend-backup] no blender/*.blend found — nothing to copy" >&2
  exit 0
fi

echo "[blend-backup] copying ${#BLENDS[@]} file(s) → $LATEST_DIR"
cp -f "${BLENDS[@]}" "$LATEST_DIR/"
du -sh "$LATEST_DIR" | awk '{print "[blend-backup] local latest:", $0}'

# Dated snapshot folder (keeps prior checkpoints; cheap hardlink where possible)
SNAP="$BACKUP_ROOT/snapshots/$STAMP"
mkdir -p "$SNAP"
if cp -al "$LATEST_DIR"/. "$SNAP/" 2>/dev/null; then
  echo "[blend-backup] hardlink snapshot → $SNAP"
else
  cp -f "$LATEST_DIR"/*.blend "$SNAP/" 2>/dev/null || true
  echo "[blend-backup] copy snapshot → $SNAP"
fi

if [ "$DO_BUNDLE" = "1" ]; then
  if git show-ref --verify --quiet refs/heads/backup/main-with-blender-pre-gh001; then
    BUNDLE="$BACKUP_ROOT/sadot-blender-history-$STAMP.bundle"
    git bundle create "$BUNDLE" backup/main-with-blender-pre-gh001
    ls -lh "$BUNDLE" | awk '{print "[blend-backup] bundle:", $0}'
  else
    echo "[blend-backup] WARN: branch backup/main-with-blender-pre-gh001 missing — skip --bundle" >&2
  fi
fi

if [ "$DO_REMOTE" = "1" ]; then
  if ssh -o BatchMode=yes -o ConnectTimeout=8 "$REMOTE" "mkdir -p ~/Backups/sadot-blend-latest && echo OK"; then
    rsync -a "$LATEST_DIR/" "$REMOTE:~/Backups/sadot-blend-latest/"
    if [ "$DO_BUNDLE" = "1" ] && [ -n "${BUNDLE:-}" ] && [ -f "${BUNDLE:-}" ]; then
      rsync -a "$BUNDLE" "$REMOTE:~/Backups/"
    fi
    echo "[blend-backup] remote rsync OK → $REMOTE:~/Backups/sadot-blend-latest/"
  else
    echo "[blend-backup] WARN: remote unreachable ($REMOTE) — local backup only" >&2
    exit 2
  fi
fi

echo "[blend-backup] done"
