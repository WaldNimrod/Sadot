---
id: HANDOFF_TO_team_110_S002_P007_INGEST_2026-07-28_v1.0.0
type: HANDOFF
from: team_100
to: team_110
cc: [team_00, team_10]
date: 2026-07-28
domain: sadot
wp_id: SDT-S002-P007-WP001
parallel_to: SDT-S002-P001-WP001
engine: Cursor Composer / Auto
---

# HANDOFF → team_110 — S002-P007 Revit→Blender ingest (parallel)

## FIRST ACTION

1. Read `design/CANONICAL/REVIT_BLENDER_INGEST_LOD200_v1.0.0.md`
2. Run **comprehensive web research** on Revit→Blender paths (IFC / DWG / FBX / glTF / Bonsai)
3. File findings memo under `_COMMUNICATION/team_110/` (or team_80 if research-only)
4. Choose primary path → update LOD200 §3
5. Build `blender/scripts/ingest/` (+ README)
6. Run **smoke trials** (use existing Sadot IFC under `raw-materials/` / prior extracts if no new file)
7. Write readiness paragraph: can we accept Michal’s mid-design temp file yet?

Do **not** message Michal. Do **not** block on P001.

## Identity

```bash
export AOS_SESSION_TEAM_ID=110 AOS_PROJECT_ID=sadot
cd /Users/nimrod/Documents/AOS_V5/Sadot
```

| | |
|--|--|
| WP | `SDT-S002-P007-WP001` **IN_PROGRESS** |
| Spec | `design/CANONICAL/REVIT_BLENDER_INGEST_LOD200_v1.0.0.md` |
| Builder | `sadot_build` (spawn team_10 for Blender MCP trials as needed) |

## Done when

LOD200 §1 checklist all checked; smoke trial logged; readiness yes/no recorded.

## Options after

- **[A]** Continue trials / harden scripts
- **[B]** Declare ingest-ready → wait for Michal file → S003
- **[C]** Escalate format choice to team_00
