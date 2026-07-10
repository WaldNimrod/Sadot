# Deploying the Sadot hub — sadot.nimrod.bio (public, no auth)

Mirrors the `il-mg.nimrod.bio` deployment pattern (same waldhomeserver, same shared Cloudflare Tunnel,
same nginx-static-vhost approach) — **with one deliberate difference: no authentication layer.** This hub
is meant to be freely reachable by the client (Niv Sadot) via a direct link, no login step. Keep it that
way; don't add an auth gate without a fresh explicit ask.

## Status

**Prepared, not yet applied.** These files are ready to use; the live server (nginx site, cloudflared
route, port-registry entry) has not been touched yet. Applying them means editing shared infra on
waldhomeserver (which also serves tt/agros/cm/il-mg) — do that deliberately, not as a side effect of
routine hub content updates.

## Files here

| File | Purpose |
|---|---|
| `nginx.sadot-hub.conf` | Static vhost — port 8094 (loopback-only; reachable via the tunnel, not directly) |
| `cloudflared.ingress.snippet` | Hostname routing block + DNS-route + verify commands |
| `deploy_sadot_hub.sh` | Repeatable build + rsync + verify — run this for every future update |

The port-registry proposal (for `agents-os/lean-kit/modules/12-home-server-infrastructure/deployment/port-registry.yaml`)
is at `_COMMUNICATION/team_100/PORT_REGISTRATION_PROPOSAL_SADOT_HUB_v1.0.0.md`.

## One-time setup (do once, in order)

1. **Remote directory:**
   ```bash
   ssh nimrodw@waldhomeserver 'sudo mkdir -p /var/www/sadot-hub && sudo chown nimrodw /var/www/sadot-hub'
   ```
2. **nginx vhost:** copy `nginx.sadot-hub.conf` to the server, enable, reload:
   ```bash
   scp hub/deploy/nginx.sadot-hub.conf nimrodw@waldhomeserver:/tmp/sadot-hub
   ssh nimrodw@waldhomeserver 'sudo mv /tmp/sadot-hub /etc/nginx/sites-available/sadot-hub && \
     sudo ln -sf /etc/nginx/sites-available/sadot-hub /etc/nginx/sites-enabled/sadot-hub && \
     sudo nginx -t && sudo systemctl reload nginx'
   ```
3. **Cloudflare Tunnel:** append the block in `cloudflared.ingress.snippet` to
   `/etc/cloudflared/config.yml` (above the `http_status:404` catch-all, without touching the tt/agros/cm/
   il-mg entries already there), then:
   ```bash
   ssh nimrodw@waldhomeserver 'cloudflared tunnel route dns 12429a3a-e597-4841-bffb-96d539dadbc9 sadot.nimrod.bio && \
     sudo systemctl restart cloudflared'
   ```
4. **Port canon:** apply the proposed entry from `PORT_REGISTRATION_PROPOSAL_SADOT_HUB_v1.0.0.md` to the
   hub's `port-registry.yaml`, then flip its `status:` from `RESERVED` to `ACTIVE`.
5. **First deploy + verify:**
   ```bash
   bash hub/deploy/deploy_sadot_hub.sh
   curl -sI https://sadot.nimrod.bio | grep -i x-robots-tag   # expect: noindex, nofollow
   curl -s -o /dev/null -w '%{http_code}\n' https://sadot.nimrod.bio   # expect: 200, no auth prompt
   ```

## Every update after that

```bash
bash hub/deploy/deploy_sadot_hub.sh
```

Rebuilds from `hub/data/*.json`, rsyncs `hub/dist/` to the server, and verifies the deployed `index.html`
matches the local build via md5. Remember: per `hub/README.md` → "Keeping this hub current", add an
`updates.json` entry for the change *before* running this.
