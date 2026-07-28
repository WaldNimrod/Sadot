---
id: RESEARCH_REVIT_BLENDER_INGEST_2026-07-28_v1.0.0
type: RESEARCH
from: team_110
to: [team_00, team_100, team_10]
date: 2026-07-28
domain: sadot
wp_id: SDT-S002-P007-WP001
engine: Cursor Composer / Auto
status: COMPLETE
---

# Research — Revit → Blender ingest paths (Sadot P007)

## Verdict

**Primary path: IFC** (prefer IFC2X3 Coordination View 2.0 — already proven from Michal) via **`ifcopenshell` CLI → verify + OBJ shell → Blender import**.  
**Bonsai (fka BlenderBIM) = optional visual QA only**, not the production ingest dump.  
**Secondary:** FBX or glTF mesh for quick-look temp geometry.  
**Reject as primary:** `.rvt`, DWG/DXF-as-3D, native Revit FBX-as-sole path, full Bonsai import as the working base.

---

## 1. IFC from Revit

| Question | Finding |
|----------|---------|
| Versions | Michal’s existing files are **IFC2X3** (`NSB02.ifc`, `NSB02_v2_2026-07-13.ifc`). IFC2x3 CV 2.0 remains the widely certified coordination exchange; IFC4 Reference View is newer/stricter; IFC4 Design Transfer View is still experimental/unofficial in practice. IFC4.3 gains in Revit 2026 are real but not required for our mid-design temp drop. |
| ifcopenshell vs Bonsai | **ifcopenshell** (installed here: 0.8.4) = programmatic open/geom/unit/storey APIs — already used for `HOUSE_IFC_REFERENCE` + `export_house_shell_obj.py`. **Bonsai** = Blender-native IFC authoring/viewer (`File → Open IFC Project`); brings *everything* (interiors, fixtures) into the scene — slow to clean for landscape work. |
| Site / terrain / levels | Storeys (`IfcBuildingStorey.Elevation`) and element placements survive IFC well. Absolute site georef from Revit is often wrong or Survey-Point-offset (Sadot: large negative XY, RefLat/Lon ~50 km off Pardes Hanna). Terrain is usually *not* in the house IFC — keep survey TIN separate. |
| Fidelity for Layer-1 | Walls/slabs/doors/windows/roofs/storeys sufficient for mid-design reference. Materials/textures weak. `IsExternal` unreliable in our file. |

**Sources (accessed 2026-07-28):**

- Autodesk Revit IFC Manual / MVD notes — IFC2x3 CV2.0 vs IFC4 RV vs DTV: https://autodesk.ifc-manual.com/understanding-ifc/model-view-definitions-mvd
- Autodesk Revit IFC 2026 exporter app notes: https://up.autodesk.com/2026/RVT/ADSKIFCExporterHelp_26_1.htm
- AECO.digital — Revit 2026 IFC 4.3 practical caveats (2025/2026): https://aeco.digital/revit-2026-ifc-4-3/
- Bonsai docs — Open IFC Project / schema notes: https://docs.bonsaibim.org/quickstart/explore_model.html
- Bonsai Blender Extensions page (rename from BlenderBIM): https://extensions.blender.org/add-ons/bonsai/
- buildingSMART / GitHub discussions on IFC4 DTV unofficial status: https://forums.buildingsmart.org/t/ifc4-design-transfer-view-experiences/4362
- In-repo: `design/CANONICAL/HOUSE_IFC_REFERENCE.md`, `design/CANONICAL/BLENDER_SHELL_BUILD_PLAN_v1.0.0.md` §2

---

## 2. CAD DWG/DXF

| Use | Verdict |
|-----|---------|
| 2D levels, paths, outlines | Useful as **overlay reference** only |
| Primary 3D ingest | **Reject** — loses BIM semantics; scale/units pitfalls (mm vs m); 3D DWG from Revit is messy polymesh/ACIS |

Prefer PDF/DWG for plan overlays alongside IFC geometry, not instead of IFC.

**Sources:** Autodesk IFC Manual (2D → DWG/PDF); CADInterop Revit format matrix: https://www.cadinterop.com/en/formats/cad-systems/revit.html (accessed 2026-07-28)

---

## 3. Mesh FBX / OBJ / glTF

| Format | When OK | Pitfalls |
|--------|---------|----------|
| **OBJ** | Our preferred *intermediate* after ifcopenshell.geom (already in repo) | No BIM props; good Z-up meters after we convert |
| **FBX** | Secondary “quick look” if Michal exports mesh easily | Native Revit FBX historically weak on materials; dense meshes; Y-up vs Z-up |
| **glTF/GLB** | Secondary for realtime/preview | Not BIM; scale must be checked |

OSArch consensus historically: IFC for structure+semantics, redo materials in Blender; Twinmotion plugin FBX better than stock Revit FBX if mesh-only needed.

**Sources:** OSArch “Revit to Blender — best format”: https://community.osarch.org/discussion/123/revit-to-blender-what-is-the-best-format (accessed 2026-07-28)

---

## 4. Collections / naming (Revit → Sadot Blender)

Map IFC types into the existing 6-collection scheme (`CURRENT_MODEL.md` pass 18):

| IFC / Revit category | Target Blender collection |
|----------------------|---------------------------|
| IfcWall, IfcDoor, IfcWindow, IfcRoof, house IfcSlab | `House` |
| Site slabs that are landscape-facing (deck candidate), terrain, boundary | `Ground` |
| Vegetation (none from Michal expected) | `Planting` / `Trees` |
| Paths, fences, retaining (when present) | `Hardscape` / fences collection as already named |
| PDF/plan overlays, empties, diagnostics | `Texts and refs` (or current English equivalent) |
| Obsolete survey house cluster | `Old House` (REFERENCE ONLY) |

Ingest scripts should **group OBJ objects by IFC type prefix** (`walls_*`, `windows_*`, …) so a Blender import pass can batch-move into collections. Do not trust `IsExternal` for exterior envelope filtering.

---

## 5. Levels / storeys / elevations

- Always convert with `ifcopenshell.util.unit.calculate_unit_scale` (Sadot NSB02: **cm → m**, scale `0.01`).
- Blender scene: **meters, Z-up** (project convention).
- Preserve relative storey elevations from IFC; absolute ITM Z for deck (~55.97 m ASL context) requires **survey tie**, not IFC RefElevation alone (`HOUSE_IFC_REFERENCE` §0 — translation still open).
- Mid-design ingest: accept IFC-native world coords + report storey table; do **not** claim site-locked until S003.

---

## 6. Failure modes (already seen on Sadot IFC)

Documented in `HOUSE_IFC_REFERENCE.md` §0 — pipeline must warn, not crash:

1. **Georef translation wrong** — large negative XY; RefLat/Lon not Pardes Hanna; rotation≈0° confirmed, translation open.
2. **`IsExternal` junk** — all walls True.
3. **Type names ≠ dimensions** — use instance OverallWidth/Height.
4. **Named deck space wrong** — real deck = unnamed slab candidate; stray roof ~133 m off.
5. **Empty / rejected roofs** — prior Blender roof passes deleted by team_00; ingest may still *export* roof geometry for later strategy.
6. **Huge wall sets** — full import includes interiors (~111+ walls); shell export keeps all walls unless axis-chaining filter added later.

---

## 7. Decision (feeds LOD200 §3)

| Field | Value |
|-------|--------|
| Primary ingest format | **IFC** (IFC2X3 preferred; IFC4/4.3 OK) |
| Secondary / fallback | **FBX or glTF** mesh quick-look |
| Toolchain | `ifcopenshell` → `blender/scripts/ingest/` verify + OBJ → Blender; Bonsai optional QA |
| Why not others | `.rvt` no Revit; DWG not 3D-primary; full Bonsai dump too heavy (shell plan §2); Revit FBX materials/scale fragile |

---

## 8. Readiness implication

We can already accept another Michal **IFC** drop of the same family as `NSB02*`. Production site lock remains **S003**. Do not message Michal.
