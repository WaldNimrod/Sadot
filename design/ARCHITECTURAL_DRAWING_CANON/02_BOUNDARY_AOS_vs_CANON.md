> **Provenance:** harvested verbatim from `IsraelMicrogreens-BlenderV2-Project` on 2026-07-08 — Sadot `design/` canon bootstrap (WP: `SDT-S001-P001-WP001`, architectural-drawing-canon + Blender/geo pipeline harvest).

# 02 — Boundary: AOS hub vs drawing production canon

## Two parallel universes in every AOS spoke

```text
┌─────────────────────────────────────┐     ┌──────────────────────────────────────┐
│  AOS HUB (agents-os)                │     │  SPOKE DOMAIN (this repo)             │
│  ─────────────────                  │     │  ────────────────────                 │
│  Governance, teams, Iron Rules      │     │  Blender model, BUILD_DATA, drawings  │
│  WP specs: LOD300/LOD400 (software) │     │  BIM-LOD300/350/400 (2D contractor)   │
│  Propagated → spoke/_aos/ READ-ONLY │     │  docs/ARCHITECTURAL_DRAWING_CANON/    │
└─────────────────────────────────────┘     └──────────────────────────────────────┘
         ▲ aos_sync only                           ▲ spoke teams edit freely
         │ NEVER edit _aos/ for drawing rules      │ NEVER push drawing canon to hub
```

## What lives where

| Content | Location | Editable by spoke? |
|---------|----------|-------------------|
| Iron Rules, team governance | `_aos/governance/` | **No** — GCR to hub |
| Roadmap, hub WPs | `_aos/roadmap.yaml`, hub only | **No** |
| AOS session/validation commands | `.claude/commands/AOS_*.md` | Hub-managed |
| **Drawing production canon** | `docs/ARCHITECTURAL_DRAWING_CANON/` | **Yes** |
| 3D modeling BUILD_DATA | `_communication/team_110/BLENDER_BUILD_DATA/` | **Yes** (team_110) |
| Phase 5 execution docs | `_communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/` | **Yes** (team_100) |
| Project decisions | `CANONICAL/` | **Yes** (with procedure) |
| Blender model | `blender/*.blend` | **Yes** (team_110) |

## Sync discipline

- `bash _aos/.../aos_sync_all.sh` **overwrites** `_aos/`. Anything drawing-related placed there **will be lost**.
- Drawing canon **must not** be symlinked into `_aos/`.
- Cross-spoke handoff of drawing canon: copy `docs/ARCHITECTURAL_DRAWING_CANON/` folder or use hub **artifact route** (`~/Documents/_agent_comm/outbox/`) — not reverse sync from `_aos/`.

## Agent startup (drawing tasks)

1. Read `_aos/roadmap.yaml` — **AOS position only**
2. Read `docs/ARCHITECTURAL_DRAWING_CANON/00_ENTRY_POINT.md` — **drawing production**
3. Do **not** conflate AOS WP `LOD400_spec.md` with `BIM-LOD400` shop drawings

## Requesting hub changes

If AOS hub terminology causes repeated confusion (e.g. overloading "LOD400"):

1. File `GOVERNANCE_CHANGE_REQUEST` in `_COMMUNICATION/team_XX/` → team_100
2. Do **not** patch `_aos/` locally
3. Meanwhile enforce qualified names from [01_TERMINOLOGY.md](01_TERMINOLOGY.md) in this spoke
