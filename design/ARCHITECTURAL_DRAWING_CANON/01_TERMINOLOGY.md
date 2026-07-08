> **Provenance:** harvested verbatim from `IsraelMicrogreens-BlenderV2-Project` on 2026-07-08 — Sadot `design/` canon bootstrap (WP: `SDT-S001-P001-WP001`, architectural-drawing-canon + Blender/geo pipeline harvest). Per `08_REPLICATION_GUIDE.md` §"Terminology in new spoke": ship unchanged unless hub renames AOS WP LOD files.

# 01 — Terminology (mandatory disambiguation)

**Problem:** The word **LOD**, **LOD400**, **field execution**, and **canon** mean different things in AOS, in this repo's Blender BUILD_DATA, and in international architectural/BIM practice. Using the wrong definition causes drift and wrong deliverables.

**Rule for agents and humans:** Before any drawing task, identify **which column** of the table below applies. If unsure -> read this file -> ask Nimrod.

**Default LOD rule:** In this repo, bare `LOD`, `LOD300`, `LOD400`, or `LOD500` means **AOS work-package LOD** by default. Any architectural/BIM reference must use the exact token pattern **`BIM-LOD___`** (`BIM-LOD300`, `BIM-LOD350`, `BIM-LOD400`, etc.).

**Adopted industry standard:** For `BIM-LOD___` definitions, this project adopts **BIMForum LOD Specification 2025** as the reference standard. Do not invent local BIM level definitions.

---

## Master disambiguation table

| Term | Meaning in **AOS hub** | Meaning in **Team 110 BUILD_DATA** (3D model) | Meaning in **architectural/BIM practice** (2D drawings) | This project's **binding choice** |
|------|------------------------|-----------------------------------------------|--------------------------------------------------------|-----------------------------------|
| **LOD** | Often shorthand for a **work-package implementation spec** filename (`LOD300_spec.md`, `LOD400_spec.md`) | **Level of Detail** for 3D proxies — "reads clearly, not engineering" | **Level of Development** (BIMForum/AIA) — reliability of model element for a milestone | **Bare `LOD` = AOS work-package LOD (default).** Every BIM reference must be an explicit `BIM-LOD___` token; every 3D-model reference is `BLENDER:REP-LOD`. |
| **LOD300** (AOS) | Design-phase **software/UI spec** (e.g. client portal mockups, AC matrix) | — | BIM **construction document** design intent | **Different domains.** AOS `LOD300_spec.md` != `BIM-LOD300` |
| **LOD400** (AOS) | **Implementation-ready software spec** for a WP (portal, `_aos/` bootstrap) — "builder can implement without guessing" | — | BIM **shop-drawing / fabrication** element fidelity | **Different domains.** AOS `LOD400_spec.md` != `BIM-LOD400` |
| **BIM-LOD300** | — | — | 2D/3D **design intent** measurable for construction documents | **Target for plans/sections** (IFC sheets) |
| **BIM-LOD350** | — | — | **MEP coordination** — interfaces, penetrations | **Target for MEP overlay sheets** |
| **BIM-LOD400** | — | — | **Fabrication** — spools, shop submittals | **Only** vendor/shop packages (Z-series) |
| **Representational LOD** | — | Correct bbox, ports, &lt;200 tris; no threads/fillets | — | **3D model rule** in `BUILD_DATA/01` |
| **LOD 400** (data/context legacy) | — | — | — | **Deprecated phrasing** in `data/context/01` ("4 decimal places") — means **metric precision**, not `BIM-LOD___`. Do not use for drawings |
| **Field execution** | Sometimes any **deliverable** at gate | — | Drawing set a **contractor builds from** | Phase 5 sheets + specs; not screenshots |
| **Canon** | Hub governance snapshots in `_aos/` | `CANONICAL/` project decisions | — | **`docs/ARCHITECTURAL_DRAWING_CANON/`** for drawing production; `_aos/` is hub mirror only |
| **matrix_basis** | — | Blender object transform for measurement | — | **Mandatory** for all sheet dimensions (not `matrix_world`) |
| **Model-native** | — | — | Geometry from **model extract**, not hand SVG | Binding pipeline per `MODEL_NATIVE_DRAWING_STANDARD.md` |

---

## Approved vocabulary (use in titles, commits, chat)

| Say this | Not this |
|----------|----------|
| **BIM-LOD300 sheet** | "LOD300 sheet" (defaults to AOS WP spec) |
| **BIM-LOD350 MEP coordination sheet** | "LOD350 sheet" |
| **BIM-LOD400 shop submittal** | "LOD400 drawing" |
| **AOS LOD400 implementation spec** | "LOD400 drawing" |
| **Representational 3D LOD** (BUILD_DATA) | "LOD 400 model" or "`BIM-LOD400` model" |
| **Model-native extract** | "render as plan" |
| **Drawing production canon** | "AOS canon" |
| **P-101** (NCS sheet ID) | "C4" (legacy ID — map via `DRAWING_SHEET_INDEX.yaml`) |

---

## Qualified name cheat sheet

```
LOD300 / AOS-LOD300   -> AOS work-package design spec (software/governance)
LOD400 / AOS-LOD400   -> AOS work-package implementation spec (software/governance)
BIM-LOD100            -> concept / symbol / space reservation; approximate only
BIM-LOD200            -> generic recognizable 3D placeholder; approximate only
BIM-LOD300            -> construction-document design intent; measurable element
BIM-LOD350            -> coordination model; interfaces/penetrations/clearances
BIM-LOD400            -> shop/fabrication submittal; vendor/spool/assembly detail
BIM-LOD500            -> field-verified as-built/existing condition
BLENDER:REP-LOD       -> 3D proxy fidelity (BUILD_DATA/01)
```

Agents **must** use `BIM-LOD___` for every BIM reference in governance, handoffs, sheet indexes, title blocks, and cross-domain chat. Unqualified `LOD___` remains AOS by default.

---

## BIM-LOD build examples (BIMForum-based)

| Target | Build this way | Not acceptable |
|--------|----------------|----------------|
| `BIM-LOD100` | Show an element exists by symbol, zone, or derived information only. Use for early planning or placeholder notes. | Contractor dimensions, installed location, or fabrication claims |
| `BIM-LOD200` | Model a generic but recognizable placeholder with approximate size, location, and orientation. | Calling it field-ready or using it for exact installation |
| `BIM-LOD300` | Model/extract a designed element whose quantity, size, shape, location, and orientation are measurable. For this repo: live `_022` extract + `matrix_basis` JSON + sheet dimensions. | Hand SVG geometry, screenshots as plans, or dimensions not traceable to JSON/vendor spec |
| `BIM-LOD350` | Start from `BIM-LOD300`, then add coordination interfaces: penetrations, access clearances, connection zones, sleeves, clashes, and MEP interaction points. | A plain plan with no interface/clearance evidence |
| `BIM-LOD400` | Use only for shop/fabrication packages: vendor tank install details, prefab spools, cut/reinforcement packages, or assembly instructions. Must cite vendor/shop source or fabrication-ready model. | General field plan labeled as shop/fabrication |
| `BIM-LOD500` | Use only after field verification/as-built survey. Record installed condition, not intended design. | Treating `BIM-LOD500` as "more detailed design" before installation |

---

## Examples from this repo (concrete)

| File | Actual meaning |
|------|----------------|
| `WP_S002…/LOD400_spec.md` | **AOS** — client portal implementation spec |
| `_aos/work_packages/S001/LOD400_spec.md` | **AOS** — spoke `_aos/` bootstrap WP |
| `BLENDER_BUILD_DATA/01_CONVENTIONS_LOD_and_DATUM.md` | **BLENDER:REP-LOD** — 3D modeling rules |
| `MODEL_NATIVE_DRAWING_STANDARD.md` | **BIM-LOD300/350/400** targets for 2D output |
| `DRAWING_SHEET_INDEX.yaml` `lod: BIM-LOD300` | **BIM-LOD300** — not AOS WP |

---

## Drift prevention rules

1. New docs **must** use qualified names from the cheat sheet.
2. Never add drawing rules to `_aos/` — file a GCR or update this canon folder.
3. Never cite `data/context/01` "LOD 400" for drawing fidelity — use the `BIM-LOD___` table.
4. Sheet title blocks say `BIM-LOD___` level or omit the BIM level field; never "AOS LOD400".
5. When replicating canon to a new spoke, copy `docs/ARCHITECTURAL_DRAWING_CANON/` verbatim first, then customize `06_STANDARDS_PROJECT.md` paths only.
