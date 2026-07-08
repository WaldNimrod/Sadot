> **Provenance:** harvested verbatim from `IsraelMicrogreens-BlenderV2-Project` on 2026-07-08 — Sadot `design/` canon bootstrap (WP: `SDT-S001-P001-WP001`, architectural-drawing-canon + Blender/geo pipeline harvest).

# 07 — Artifact layout

## Canon (portable)

```
docs/ARCHITECTURAL_DRAWING_CANON/
  00_ENTRY_POINT.md          ← start here
  01_TERMINOLOGY.md
  …
  CANON_VERSION.yaml
  INDEX.yaml
```

## Drawing production tree

```
drawings/
  view_presets/              # Stage 1 — YAML per sheet
    P-101_reservoir.yaml
  _extracts/                 # Stage 2 — model-native SVG
    P101/
      plan.svg
      section_aa.svg
      …
  P_reservoir/               # Stage 4 — composed outputs
    P-101_reservoir.pdf
    P-101_reservoir.svg
  process/
    MODEL_NATIVE_PROCESS.pdf # Nimrod process gate

exports/ai_bridge/
  sheet_measurements_P101.json   # Stage 3
  phase3_inventory.json          # Subsystem register
  SHEET_MEASUREMENTS_SCHEMA.md

scripts/drawing/
  export_sheet_views.py
  compose_sheet.py
  mesh_ortho_export.py
  README.md

_communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/
  MODEL_NATIVE_DRAWING_STANDARD.md
  DRAWING_SHEET_INDEX.yaml
  lib/                         # Composer + QA
  APPROVAL_LOG.md

blender/
  IsraelMicrogreens_022.blend  # Live model (see CURRENT_MODEL.md)
```

## Naming conventions

| Artifact | Pattern | Example |
|----------|---------|---------|
| Sheet ID | NCS `[Discipline]-[Type][Seq]` | `P-101` |
| Preset file | `<ID>_<topic>.yaml` | `P-101_reservoir.yaml` |
| Extract folder | Sheet ID without hyphen | `P101/` |
| Measurement JSON | `sheet_measurements_<ID>.json` | `sheet_measurements_P101.json` |
| Legacy C-series | Retired | `C4` → `P-101` |

## QA artifacts

| Artifact | Location |
|----------|----------|
| Viewport parity | `snapshots/` |
| Export log | `logs/drawing/export_sheet_views.json` |
| QA verdict | stdout from `sheet_qa_checklist.py` |

## What not to put in `_aos/`

Anything under `docs/ARCHITECTURAL_DRAWING_CANON/`, `drawings/`, `scripts/drawing/`, or Phase 5 `lib/`.
