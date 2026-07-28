# Sadot — Revit → Blender ingest scripts

WP: `SDT-S002-P007-WP001`  
SSOT: `design/CANONICAL/REVIT_BLENDER_INGEST_LOD200_v1.0.0.md`  
Research: `_COMMUNICATION/team_110/RESEARCH_REVIT_BLENDER_INGEST_2026-07-28_v1.0.0.md`

## Primary path

**Michal IFC → ifcopenshell verify → OBJ shell → Blender import**

Bonsai (fka BlenderBIM) is optional visual QA only — do not use a full Bonsai dump as the working landscape base.

## Prerequisites

- Python with `ifcopenshell` (this Mac: `/Library/Developer/CommandLineTools/usr/bin/python3`)
- Fixture IFC under `raw-materials/from-client/` (gitignored) — see `blender/data/ingest/fixtures/README.md`
- Blender for the final OBJ import step (MCP or GUI)

## Operator steps (smoke trial)

From repo root `/Users/nimrod/Documents/AOS_V5/Sadot`:

```bash
export PY=/Library/Developer/CommandLineTools/usr/bin/python3

# 1) Verify IFC (schema, units, storeys, counts, bbox)
$PY blender/scripts/ingest/verify_ifc.py \
  raw-materials/from-client/NSB02_v2_2026-07-13.ifc \
  -o blender/data/ingest/last_verify.json

# 2) Export shell OBJ (walls/windows/doors/roofs/deck)
$PY blender/scripts/ingest/export_shell_obj.py \
  raw-materials/from-client/NSB02_v2_2026-07-13.ifc \
  -o blender/data/ingest/house_shell_smoke.obj

# 3) Blender — File → Import → Wavefront (.obj)
#    Prefer meters / Z-up. Place imported objects into collection House
#    (see CURRENT_MODEL.md pass 18). Screenshot viewport for smoke log.
```

Fallback IFC if v2 missing: `raw-materials/from-client/NSB02.ifc`.

## What to log (smoke)

| Field | Example |
|-------|---------|
| File type / path | IFC2X3, `NSB02_v2_…ifc` |
| ifcopenshell version | from verify output |
| Blender version | if import step run |
| Counts | walls / windows / doors / roofs / slabs |
| Unit scale | `0.01` (cm→m) expected for NSB02 |
| Scale check | storey elevation delta or XY bbox span vs `HOUSE_IFC_REFERENCE` |
| Result | PASS / FAIL |

Template log path: `_COMMUNICATION/team_110/SMOKE_TRIAL_INGEST_IFC_YYYY-MM-DD_v1.0.0.md`

## Secondary path (mesh only)

If Michal drops FBX/glTF instead of IFC: import via Blender native importers, check scale (mm→m often `0.001`), treat as **visual-only** — no storey/BIM semantics. Prefer asking for IFC when convenient (we do **not** send her a checklist unprompted).

## S003 boundary

These scripts prove we can **receive and inspect** a mid-design temp file.  
Production convert + ITM site lock + dress = **S003**, not this folder.
