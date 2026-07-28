---
id: REVIT_BLENDER_INGEST_LOD200
version: 1.0.0
type: LOD200 tooling / ingest readiness
wp_id: SDT-S002-P007-WP001
date: 2026-07-28
status: READY — mid-design IFC accept; production lock = S003
authority: team_00 parallel track 2026-07-28
---

# Revit → Blender ingest — LOD200 (internal)

## 0. Intent

Prepare **our** pipeline to receive a **mid-design temporary** model from Michal (Revit) into Blender.  
**We send Michal nothing.** No export checklist to her. When ingest is proven, she can drop a working file; then S003 does production convert+lock.

Constraint: minimum future friction for her (whatever she already exports easily) — we adapt.

## 1. LOD200 checklist

- [x] Web research: viable Revit→Blender paths (IFC, DWG/DXF, FBX, glTF, direct add-ons)
- [x] Primary path chosen + reject list with evidence
- [x] Units / Z-up / scale / georef notes for Sadot
- [x] Repo infra: scripts and/or documented Blender steps under `blender/`
- [x] At least one **smoke trial** on a fixture (synthetic or prior IFC in `raw-materials/`)
- [x] Readiness note: “can accept Michal mid-design file” yes/no + what’s missing
- [x] Explicit handoff boundary to S003 (production lock)

Research memo: `_COMMUNICATION/team_110/RESEARCH_REVIT_BLENDER_INGEST_2026-07-28_v1.0.0.md`  
Smoke log: `_COMMUNICATION/team_110/SMOKE_TRIAL_INGEST_IFC_2026-07-28_v1.0.0.md`

## 2. Research scope (web — comprehensive)

Document in `_COMMUNICATION/team_110/` or `team_80/` memo, then fold summary into this file §3:

| Topic | Questions |
|-------|-----------|
| IFC from Revit | Which IFC versions; ifcopenshell vs BlenderBIM/Bonsai; site/terrain/levels fidelity |
| CAD DWG/DXF | Useful for 2D levels/paths only? Scale pitfalls |
| Mesh FBX/OBJ/glTF | When acceptable for temp working model |
| Collections / naming | How to map Revit categories → our Blender collections (House/Ground/…) |
| Levels / storeys | Preserve absolute elevations (deck 55.97 context) |
| Failure modes | Empty roofs, huge wall sets, coordinate origin — already seen in Sadot IFC |

Cite sources with dates. Prefer paths already used in this repo (`ifcopenshell`, existing IFC extracts).

## 3. Decision record

| Field | Value |
|-------|--------|
| Primary ingest format | **IFC** (prefer IFC2X3 CV 2.0 — Michal’s existing exports; IFC4 / 4.3 acceptable) |
| Secondary / fallback | **FBX or glTF** mesh quick-look only (no BIM semantics) |
| Toolchain | `ifcopenshell` CLI → `blender/scripts/ingest/verify_ifc.py` + `export_shell_obj.py` → Blender OBJ import; **Bonsai = optional visual QA**, not primary dump |
| Why not others | `.rvt` — no Revit here; DWG/DXF — 2D overlay only; full Bonsai import — interior clutter (see `BLENDER_SHELL_BUILD_PLAN` §2); native Revit FBX-as-sole — materials/scale fragile |

### 3.1 Units / Z-up / scale / georef (Sadot)

| Topic | Note |
|-------|------|
| Scene units | Blender meters, **Z-up** |
| IFC length | NSB02 family uses **centimeters** → `unit_scale_to_m = 0.01` via `ifcopenshell.util.unit` |
| Storeys | Preserve `IfcBuildingStorey.Elevation` (converted to m); use for relative levels |
| Absolute ASL (deck ~55.97) | Requires survey / ITM tie — **not** claimed from IFC alone |
| XY georef | Rotation ≈ 0° confirmed; **translation still open** (`HOUSE_IFC_REFERENCE` §0). Mid-design ingest keeps IFC-native world coords |
| Collections | Map walls/doors/windows/roofs/house slabs → `House`; deck/site slabs + terrain → `Ground` (see research memo §4) |

### 3.2 Readiness (mid-design)

**YES — we can accept Michal’s mid-design temporary file if it is IFC** (same family as `/Users/nimrod/Documents/AOS_V5/Sadot/raw-materials/from-client/NSB02*.ifc`). Pipeline verifies schema/units/storeys/counts and exports a Blender-importable OBJ shell. FBX/glTF also acceptable as visual-only secondary. **Missing for production:** ITM translation lock, roof strategy, full collection dress, convert+lock — that is **S003**, not P007. Do not message Michal.

### 3.3 Handoff boundary → S003

P007 ends when ingest scripts + smoke + readiness are recorded.  
**S003** owns: final Michal file → production convert, site lock against survey, replace provisional house shell, then S004 dress Layer-2 systems onto the locked base.

## 4. Infrastructure

| Path | Purpose |
|------|---------|
| `blender/scripts/ingest/` | `verify_ifc.py`, `export_shell_obj.py` |
| `blender/scripts/ingest/README.md` | Operator steps for a trial |
| `blender/data/ingest/fixtures/` | Pointers to existing IFC — no huge binaries committed |
| `design/CANONICAL/REVIT_BLENDER_INGEST_LOD200_v1.0.0.md` | This SSOT |

Smoke trial must log: file type, Blender version, object counts, scale check (known length if available), pass/fail.

## 5. Relation to other WPs

| WP | Relation |
|----|----------|
| P001–P006 Layer-2 | Parallel — does not block; do not wait |
| S003 convert+lock | Consumes this pipeline when Michal file arrives |
| Old DRAFT_MESSAGE_TO_MICHAL | **Do not send** |

## 6. Acceptance (WP complete)

1. Research memo + §3 decision filled.
2. Ingest script/docs in repo.
3. ≥1 successful smoke trial recorded (path + date + result).
4. One-paragraph readiness: what Michal can drop next and what we still cannot ingest.

## 7. Out of scope

- Asking Michal to change her workflow beyond “send file of type X if easy”
- Final site lock / dress (S003/S004)
- Layer-2 system design (P001–P005)
