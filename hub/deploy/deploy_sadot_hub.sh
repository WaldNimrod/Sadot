#!/usr/bin/env bash
# Build + deploy the Sadot client hub to sadot.nimrod.bio (waldhomeserver, public, no auth).
#
# One-time server setup (do ONCE, not part of this repeatable script):
#   1. ssh nimrodw@waldhomeserver 'sudo mkdir -p /var/www/sadot-hub && sudo chown nimrodw /var/www/sadot-hub'
#   2. Copy hub/deploy/nginx.sadot-hub.conf -> waldhomeserver:/etc/nginx/sites-available/sadot-hub
#      then: sudo ln -s /etc/nginx/sites-available/sadot-hub /etc/nginx/sites-enabled/
#            sudo nginx -t && sudo systemctl reload nginx
#   3. Append hub/deploy/cloudflared.ingress.snippet to /etc/cloudflared/config.yml (above the 404 catch-all),
#      then: cloudflared tunnel route dns 12429a3a-e597-4841-bffb-96d539dadbc9 sadot.nimrod.bio
#            sudo systemctl restart cloudflared
#   4. Register the port-registry.yaml entry (see _COMMUNICATION/team_100/PORT_REGISTRATION_PROPOSAL_SADOT_HUB_v1.0.0.md)
#      and flip its status: RESERVED -> ACTIVE once step 1-3 are live.
#
# Usage (repeatable, from repo root):
#   bash hub/deploy/deploy_sadot_hub.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
REMOTE_HOST="waldhomeserver"
REMOTE_USER="nimrodw"
REMOTE_PATH="/var/www/sadot-hub"

echo "[1/4] Building hub..."
python3 "$REPO_ROOT/scripts/build_sadot_client_hub.py"

echo "[2/4] Resolving host (LAN then Tailscale)..."
if nc -z -G 2 10.100.102.2 22 2>/dev/null; then
  HOST_ADDR="10.100.102.2"
else
  HOST_ADDR="100.125.98.56"
fi
echo "    using $HOST_ADDR"

echo "[3/4] Syncing hub/dist/ -> $REMOTE_USER@$HOST_ADDR:$REMOTE_PATH ..."
rsync -az --delete "$REPO_ROOT/hub/dist/" "$REMOTE_USER@$HOST_ADDR:$REMOTE_PATH/"

echo "[4/4] Verifying (local md5 == remote md5 for index.html)..."
LOCAL_MD5="$(md5 -q "$REPO_ROOT/hub/dist/index.html" 2>/dev/null || md5sum "$REPO_ROOT/hub/dist/index.html" | cut -d' ' -f1)"
REMOTE_MD5="$(ssh "$REMOTE_USER@$HOST_ADDR" "md5sum $REMOTE_PATH/index.html | cut -d' ' -f1")"
if [ "$LOCAL_MD5" = "$REMOTE_MD5" ]; then
  echo "[OK] Deployed. https://sadot.nimrod.bio should now reflect this build."
else
  echo "[WARN] md5 mismatch — local=$LOCAL_MD5 remote=$REMOTE_MD5. Re-check rsync output above."
fi
