---
id: SMOKE_TRIAL_INGEST_IFC_2026-07-28_v1.0.0
type: SMOKE_TRIAL
from: team_110
to: [team_00, team_100, team_10]
date: 2026-07-28
domain: sadot
wp_id: SDT-S002-P007-WP001
engine: Cursor Composer / Auto
result: PASS
---

# Smoke trial — IFC ingest (P007)

## Result: **PASS** (CLI verify + OBJ export)

Blender GUI/MCP import was **not** available this session (`Could not connect to Blender`). Plan allows CLI smoke for LOD200; live viewport import is Option **[A]** harden follow-up.

## Inputs

| Field | Value |
|-------|--------|
| File | `/Users/nimrod/Documents/AOS_V5/Sadot/raw-materials/from-client/NSB02_v2_2026-07-13.ifc` |
| Type / schema | IFC2X3 |
| ifcopenshell | 0.8.4.post1 |
| Python | `/Library/Developer/CommandLineTools/usr/bin/python3` |
| Blender version | *not run* (MCP offline) |

## Commands

```bash
/Library/Developer/CommandLineTools/usr/bin/python3 blender/scripts/ingest/verify_ifc.py \
  raw-materials/from-client/NSB02_v2_2026-07-13.ifc \
  -o blender/data/ingest/last_verify.json

/Library/Developer/CommandLineTools/usr/bin/python3 blender/scripts/ingest/export_shell_obj.py \
  raw-materials/from-client/NSB02_v2_2026-07-13.ifc \
  -o blender/data/ingest/house_shell_smoke.obj
```

## Verify output (summary)

| Metric | Value |
|--------|-------|
| unit_scale_to_m | 0.01 |
| IfcWall / Window / Door / Roof / Slab | 111 / 13 / 16 / 6 / 45 |
| Storeys | 5 (entrance 55.99 m → parents 59.09 m) |
| Scale check storey[0]→[1] | **3.1 m** (within 2–5 m band) |
| Bbox sample XY×Z span | **35.34 × 22.46 × 9.33 m** |
| Warnings | `IsExternal=True` on all 111 walls (known) |
| Errors | none |

JSON: `/Users/nimrod/Documents/AOS_V5/Sadot/blender/data/ingest/last_verify.json`

## Export output

| Metric | Value |
|--------|-------|
| OBJ | `/Users/nimrod/Documents/AOS_V5/Sadot/blender/data/ingest/house_shell_smoke.obj` |
| Bytes | 613 341 |
| Elements exported | **141** (0 geom fail) |
| Roofs | 0/6 kept — all 6 `Representation is NULL` (Sadot known empty-roof mode) |
| Deck slab | **found** |

## Pass criteria

- [x] IFC opens and reports schema + units
- [x] Non-zero building geometry counts
- [x] Known length (storey delta) sane
- [x] OBJ written with substantial content
- [ ] Blender viewport confirm — deferred (MCP offline) → Option A

## Implication

Pipeline can accept another Michal **IFC** drop of this family. Empty roofs in export are expected for this file and do not block mid-design ingest readiness.
