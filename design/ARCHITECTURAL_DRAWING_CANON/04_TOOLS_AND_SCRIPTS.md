> **Provenance:** harvested verbatim from `IsraelMicrogreens-BlenderV2-Project` on 2026-07-08 — Sadot `design/` canon bootstrap (WP: `SDT-S001-P001-WP001`, architectural-drawing-canon + Blender/geo pipeline harvest).

# 04 — Tools and scripts

## Pipeline scripts (this repo)

| Script | Runs in | Purpose |
|--------|---------|---------|
| `scripts/drawing/export_sheet_views.py` | Blender background | Mesh ortho edge → SVG extracts |
| `scripts/drawing/mesh_ortho_export.py` | Blender (imported) | Projection library |
| `scripts/drawing/compose_sheet.py` | Python 3 | Assemble PDF from extracts + JSON |
| `scripts/drawing/check_section_toolbox.py` | Blender | Optional addon check |
| `scripts/inspect/measure_sheet.py` | Blender background | `matrix_basis` → JSON |
| `scripts/inspect/render_sheet_context.py` | Blender background | Context inset PNG only |

## Phase 5 libraries

Path: `_communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/`

| Module | Role |
|--------|------|
| `drawing_kit.py` | Title block, frame, SVG primitives |
| `sheet_layout.py` | Zones, legend, notes, scale bar |
| `sheet_export.py` | SVG → HTML → PDF (WeasyPrint) |
| `rear_site_projection.py` | Rear-yard dimension coords |
| `measure_model.py` | Load measurement JSON |
| `sheet_qa_checklist.py` | Pre-delivery QA |
| `sheet_model_parity.py` | Anti schematic-drift |
| `sheet_gate.py` | Approval order |
| `tank_specs.py` | Vendor `BIM-LOD400` supplement |

## Optional Blender extensions

| Tool | Doc | Status on Mac Blender 5.0.1 |
|------|-----|----------------------------|
| Section Toolbox | `scripts/drawing/install_section_toolbox.md` | Not installed — mesh fallback active |
| Section Pro | Blender Market (paid) | Not evaluated |

**Primary extract today:** mesh orthographic edge projection (model-native vectors).  
**Upgrade path:** Section Toolbox when installed — same preset YAML, swap extract backend.

## External tools

| Tool | Use |
|------|-----|
| WeasyPrint | PDF from composed SVG |
| PyYAML | Preset loading |
| ezdxf | DXF export (legacy water BOQ; extend for extracts later) |

## MCP / live Blender

- `user-blender` MCP: viewport screenshot, `execute_blender_code` — QA only for drawings
- Measurement authority: **background** `measure_sheet.py`, not live MCP `matrix_world`

## Logs

| Log | Content |
|-----|---------|
| `logs/drawing/export_sheet_views.json` | Extract run metadata |
| `logs/assembly/` | Model fix scripts (tanks, etc.) |
| `logs/post_task/` | Task completion snapshots |
