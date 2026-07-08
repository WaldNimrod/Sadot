> **Provenance:** harvested verbatim from `IsraelMicrogreens-BlenderV2-Project` `scripts/drawing/README.md` on 2026-07-08 — Sadot `design/` pipeline bootstrap (WP: `SDT-S001-P001-WP001`). Canon link and P-101 pilot commands below still reference the origin repo's paths/model — see `../ARCHITECTURAL_DRAWING_CANON/06_STANDARDS_PROJECT.md` for Sadot's own (TBD) equivalents.

# scripts/drawing — model-native drawing pipeline

**Canon (terminology, workflow, replication):** [`docs/ARCHITECTURAL_DRAWING_CANON/00_ENTRY_POINT.md`](../../docs/ARCHITECTURAL_DRAWING_CANON/00_ENTRY_POINT.md)

| Script | Role |
|--------|------|
| `check_section_toolbox.py` | Verify Section Toolbox addon |
| `export_sheet_views.py` | Mesh ortho edge extract → `_extracts/` SVG |
| `compose_sheet.py` | Compose extracts + measurements → PDF |
| `mesh_ortho_export.py` | Core projection library (used by export) |
| `install_section_toolbox.md` | Addon install guide |

## P-101 pilot

```bash
# 1 Extract views from _022
/Applications/Blender.app/Contents/MacOS/Blender --background \
  blender/IsraelMicrogreens_022.blend \
  --python scripts/drawing/export_sheet_views.py -- --preset P-101_reservoir

# 2 Measurements
/Applications/Blender.app/Contents/MacOS/Blender --background \
  blender/IsraelMicrogreens_022.blend \
  --python scripts/inspect/measure_sheet.py -- --sheet P101

# 3 Compose PDF
python3 scripts/drawing/compose_sheet.py --sheet P101 --preset P-101_reservoir

# 4 QA
cd _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS
python3 lib/sheet_qa_checklist.py drawings/P_reservoir drawings/_extracts/P101
python3 lib/sheet_model_parity.py P101 drawings/P_reservoir/P-101_reservoir.svg
```

Standard: `MODEL_NATIVE_DRAWING_STANDARD.md`
