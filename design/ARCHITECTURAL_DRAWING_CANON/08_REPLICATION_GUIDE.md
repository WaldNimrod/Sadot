> **Provenance:** harvested verbatim from `IsraelMicrogreens-BlenderV2-Project` on 2026-07-08 — Sadot `design/` canon bootstrap (WP: `SDT-S001-P001-WP001`, architectural-drawing-canon + Blender/geo pipeline harvest). This file is the procedure this Sadot copy was made under; its own content is unmodified.

# 08 — Replication guide (new AOS spoke)

Use when a **second domain** needs the same model-native drawing pipeline (e.g. another Blender-based facility).

## What to copy (minimum)

```text
docs/ARCHITECTURAL_DRAWING_CANON/     # entire folder — update CANON_VERSION.yaml
scripts/drawing/                      # export + compose pipeline
scripts/inspect/measure_sheet.py      # extend sheet lists per project
_communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/
  drawing_kit.py
  sheet_layout.py
  sheet_export.py
  sheet_qa_checklist.py
  sheet_model_parity.py
  sheet_gate.py
  measure_model.py
```

## What to author per project

| Item | Action |
|------|--------|
| `06_STANDARDS_PROJECT.md` | Replace paths and doc list |
| `DRAWING_SHEET_INDEX.yaml` | New sheet IDs + subsystems |
| `view_presets/*.yaml` | Per-building crops and collections |
| `measure_sheet.py` `SHEET_OBJECTS` | Object names from inventory |
| `BUILD_DATA/01` | 3D representational LOD (may differ) |
| `MODEL_NATIVE_DRAWING_STANDARD.md` | Copy + adjust `BIM-LOD400` shop list |

## What NOT to copy blindly

| Item | Reason |
|------|--------|
| `IsraelMicrogreens_*.blend` | Project-specific geometry |
| `rear_site_projection.py` | Rear-yard coords unique to this site |
| `TANK_PRODUCT_SPECS.md` | Vendor-specific |
| `WATER_SYSTEM_BOQ/` | Legacy schematic set |
| `_aos/` | Hub sync — each spoke gets its own snapshot |

## Terminology in new spoke

1. Ship `01_TERMINOLOGY.md` unchanged unless hub renames AOS WP LOD files.
2. Train agents: **read `00_ENTRY_POINT.md` before any drawing task**.
3. Add Cursor rule pointing to canon entry (optional):

```markdown
# Architectural drawings
Before Phase 5 / sheet work: read docs/ARCHITECTURAL_DRAWING_CANON/00_ENTRY_POINT.md
Do not confuse AOS LOD400 WP specs with `BIM-LOD400` shop drawings.
```

## Versioning

1. Bump `CANON_VERSION.yaml` `version` on structural changes.
2. Record origin in `origin_spoke` when forked.
3. Prefer **merge upstream** canon improvements back to Israel Microgreens when generic.

## Checklist (new spoke bootstrap)

- [ ] Copy canon folder + `scripts/drawing/`
- [ ] Update `06_STANDARDS_PROJECT.md`
- [ ] Create `DRAWING_SHEET_INDEX.yaml`
- [ ] Pin Blender version in `install_section_toolbox.md`
- [ ] Run pilot sheet end-to-end
- [ ] Cross-engine QA (Iron Rule #1)
- [ ] Nimrod gate on process PDF + first sheet

## Hub integration (optional future)

If multiple spokes adopt this canon, hub may host a **template spoke** or `lean-kit` module — that is a **GCR to team_100**, not a local `_aos/` edit. Until then, **`docs/ARCHITECTURAL_DRAWING_CANON/` in each spoke is SSOT**.
