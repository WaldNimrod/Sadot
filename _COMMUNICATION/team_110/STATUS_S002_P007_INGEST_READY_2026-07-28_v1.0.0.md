---
id: STATUS_S002_P007_INGEST_READY_2026-07-28_v1.0.0
type: STATUS
from: team_110
to: [team_00, team_100]
date: 2026-07-28
domain: sadot
wp_id: SDT-S002-P007-WP001
engine: Cursor Composer / Auto
status: DONE — ingest-ready for mid-design IFC
recommended_option: B
---

# STATUS — S002-P007 Revit→Blender ingest readiness

## Done-when checklist

| Criterion | Evidence |
|-----------|----------|
| Research memo + §3 decision | `/Users/nimrod/Documents/AOS_V5/Sadot/_COMMUNICATION/team_110/RESEARCH_REVIT_BLENDER_INGEST_2026-07-28_v1.0.0.md` + LOD200 §3 filled |
| Ingest scripts/docs | `/Users/nimrod/Documents/AOS_V5/Sadot/blender/scripts/ingest/` |
| ≥1 smoke trial | `/Users/nimrod/Documents/AOS_V5/Sadot/_COMMUNICATION/team_110/SMOKE_TRIAL_INGEST_IFC_2026-07-28_v1.0.0.md` — **PASS** |
| Readiness yes/no | LOD200 §3.2 — **YES for IFC mid-design**; production lock = S003 |

## Recommendation: **[B]** Declare ingest-ready → wait for Michal file → S003

- Primary path locked: IFC → ifcopenshell → OBJ → Blender
- Proven on Michal’s `NSB02_v2_2026-07-13.ifc` (141 elements exported)
- Do **not** message Michal
- Optional **[A]** later: Blender MCP viewport import when addon is up; harden roof-null handling
- **[C]** not needed — format choice is clear

## Note

`validate_aos.sh` still reports Check 32 FAIL (`_aos/` uncommitted drift from Layer-2 pivot) — pre-existing; team_00/100 sync issue, not P007 scope.
