> **Provenance:** harvested verbatim from `IsraelMicrogreens-BlenderV2-Project` on 2026-07-08 — Sadot `design/` canon bootstrap (WP: `SDT-S001-P001-WP001`, architectural-drawing-canon + Blender/geo pipeline harvest). Per `08_REPLICATION_GUIDE.md`, only `CANON_VERSION.yaml` and `06_STANDARDS_PROJECT.md` were adapted for this spoke; this file is unmodified content.

# Architectural Drawing Production Canon — ENTRY POINT

**Read this file first.** This folder is the **single front door** for producing contractor-grade architectural/MEP drawings from a Blender model inside an AOS spoke.

---

## What this canon is

A **project-portable, spoke-local** standard for:

- Terminology (disambiguated from AOS hub vocabulary)
- Workflow (model → extract → measure → compose → QA → gate)
- Tools and scripts
- External architectural standards (`BIM-LOD___`, ISO, NCS)
- File layout and replication to other domains

**First implementation:** `IsraelMicrogreens-BlenderV2-Project` (microgreens container farm).  
**Next expected consumer:** another spoke with Blender-based field-execution drawings.

---

## What this canon is NOT

| Do not confuse with | Location | Why different |
|---------------------|----------|---------------|
| **AOS hub governance** | `_aos/` in each spoke | READ-ONLY snapshot from hub; `aos_sync` overwrites edits |
| **AOS LOD300 / LOD400 WP specs** | Hub work packages, client portal specs | Software/governance **implementation** fidelity — not BIM drawing LOD |
| **AOS Iron Rules / teams** | `_aos/governance/` | Org-wide agent rules — not drawing production |
| **Phase 4 beauty renders** | `WP_PHASE4_RENDER/` | Client marketing — not contractor plans |
| **Legacy schematic SVG** | `WATER_SYSTEM_BOQ/…/make_contractor_drawings.py` `plx()` | Pre-model schematic coords — **retired pattern** |

**Rule:** Never edit `_aos/` to store drawing canon. Never store drawing canon in the hub. Canon lives in **`docs/ARCHITECTURAL_DRAWING_CANON/`** (or equivalent path in other spokes).

---

## Document map (read order)

| # | File | Purpose |
|---|------|---------|
| **01** | [01_TERMINOLOGY.md](01_TERMINOLOGY.md) | **Mandatory** — same words, different meanings |
| **02** | [02_BOUNDARY_AOS_vs_CANON.md](02_BOUNDARY_AOS_vs_CANON.md) | Isolation from hub sync |
| **03** | [03_PROCESS_WORKFLOW.md](03_PROCESS_WORKFLOW.md) | Six-stage pipeline |
| **04** | [04_TOOLS_AND_SCRIPTS.md](04_TOOLS_AND_SCRIPTS.md) | Commands and paths |
| **05** | [05_STANDARDS_EXTERNAL.md](05_STANDARDS_EXTERNAL.md) | BIMForum, ISO, NCS |
| **06** | [06_STANDARDS_PROJECT.md](06_STANDARDS_PROJECT.md) | This spoke's binding docs |
| **07** | [07_ARTIFACT_LAYOUT.md](07_ARTIFACT_LAYOUT.md) | Where files live |
| **08** | [08_REPLICATION_GUIDE.md](08_REPLICATION_GUIDE.md) | Copy to a new spoke |
| — | [CANON_VERSION.yaml](CANON_VERSION.yaml) | Version stamp |
| — | [INDEX.yaml](INDEX.yaml) | Machine-readable index |

---

## Quick start (this repo)

```bash
# 1. Extract views from live blend
/Applications/Blender.app/Contents/MacOS/Blender --background \
  blender/IsraelMicrogreens_022.blend \
  --python scripts/drawing/export_sheet_views.py -- --preset P-101_reservoir

# 2. Measurements
/Applications/Blender.app/Contents/MacOS/Blender --background \
  blender/IsraelMicrogreens_022.blend \
  --python scripts/inspect/measure_sheet.py -- --sheet P101

# 3. Compose PDF
python3 scripts/drawing/compose_sheet.py --sheet P101 --preset P-101_reservoir

# 4. QA
cd _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS
python3 lib/sheet_qa_checklist.py drawings/P_reservoir drawings/_extracts/P101
python3 lib/sheet_model_parity.py P101 drawings/P_reservoir/P-101_reservoir.svg
```

**Live model pointer:** `blender/CURRENT_MODEL.md`  
**Process diagram (Nimrod gate):** `_communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/drawings/process/MODEL_NATIVE_PROCESS.pdf`

---

## Governance

| Role | Authority |
|------|-----------|
| Canon content | team_110 (modeling) + team_100 (engineering docs) |
| Sheet approval | team_00 (Nimrod) — `APPROVAL_LOG.md` |
| Cross-engine QA | team_190 (Iron Rule #1) |
| Hub `_aos/` changes | team_00 / team_100 via GCR only |

**Revision:** Update `CANON_VERSION.yaml` when canon structure or terminology changes.
