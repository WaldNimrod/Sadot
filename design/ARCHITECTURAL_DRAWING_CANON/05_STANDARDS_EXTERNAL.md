> **Provenance:** harvested verbatim from `IsraelMicrogreens-BlenderV2-Project` on 2026-07-08 — Sadot `design/` canon bootstrap (WP: `SDT-S001-P001-WP001`, architectural-drawing-canon + Blender/geo pipeline harvest).

# 05 — External architectural standards

References are **industry authority** — not AOS hub docs. Use for sheet content, title blocks, and LOD targets.

## Adopted BIM Level of Development standard

**Adopted standard:** [BIMForum LOD Specification 2025](https://bimforum.org/wp-content/uploads/2026/01/LOD-Spec-2025-Part-I-Official.pdf), which expands the AIA LOD schema and is used here as the project reference vocabulary for BIM Level of Development.

**Important:** BIMForum is a reference language for element reliability. It does not decide this project's phase targets by itself. This project assigns targets below.

| Token | Source | Use in this project | Minimum evidence before using token |
|-------|--------|---------------------|-------------------------------------|
| `BIM-LOD100` | BIMForum/AIA | Concept, symbol, zone, or derived information only | Explicitly marked approximate; no contractor dimensions |
| `BIM-LOD200` | BIMForum/AIA | Generic recognizable placeholder | Approximate size/location/orientation only; not field-execution |
| `BIM-LOD300` | BIMForum/AIA | Field plans/sections; design intent measurable | Model-native extract + `matrix_basis` JSON or approved vendor spec |
| `BIM-LOD350` | BIMForum/AIA | MEP coordination sheets | `BIM-LOD300` base plus penetrations, clearances, interfaces, and clash/coordination evidence |
| `BIM-LOD400` | BIMForum/AIA | Shop/fabrication submittals only (Z-series) | Vendor/shop/fabrication source, spool/assembly details, or fabrication-ready model |
| `BIM-LOD500` | BIMForum/AIA | Field-verified as-built/existing condition | Installed condition verified in the field; not a pre-install design target |

**Nimrod-approved target:** `BIM-LOD350` MEP coordination + `BIM-LOD300` field-execution sheets. `BIM-LOD400` is reserved for shop-fabricated/vendor packages.

## How to build a sheet to a BIM-LOD target

1. Pick the target token before production: `BIM-LOD300`, `BIM-LOD350`, or `BIM-LOD400`.
2. Identify the element list and source of truth: live `_022` model, `matrix_basis` JSON, vendor spec, or Nimrod-approved record.
3. Extract geometry from the model; do not draw primary geometry by hand.
4. Add only dimensions that trace to JSON, vendor spec, or approval log.
5. For `BIM-LOD350`, add interfaces: penetrations, clearances, access/service zones, and connection points.
6. For `BIM-LOD400`, add fabrication/shop evidence: spool lengths, vendor install detail, cut/reinforcement detail, or approved shop package.
7. Run sheet QA, model parity, and visual PDF review before any gate.

## Drawing presentation

| Standard | Applies to |
|----------|------------|
| [ISO 128-3:2022](https://www.iso.org/standard/83356.html) | Views, sections, cuts |
| [ISO 5457](https://www.iso.org/standard/29017.html) | Sheet sizes (A3/A2/A1) |
| [ISO 7200](https://www.iso.org/standard/35450.html) | Title block fields |
| [NCS v6 UDS](https://nationalcadstandard.org/ncs6/pdfs/ncs6_uds1.pdf) | Sheet numbering `P-101`, `A-301` |
| [AIA CAD Layer Guidelines](https://nationalcadstandard.org/ncs6/pdfs/ncs6_clg_lnf.pdf) | DXF layers if CAD export |

## Sheet sizes (container project)

| Size | Typical sheets |
|------|----------------|
| A2 | Container floor plans, MEP overlays |
| A3 | Sections, single-system, details |
| A1 | Site/reservoir context |

## Minimum content per sheet type (NCS type digit)

| Type | Digit | Minimum |
|------|-------|---------|
| Plan | 1 | Footprint, tags, cut marks, dims |
| Section | 3 | Cutting plane, levels, systems in cut |
| Detail | 5 | Connection geometry, materials, dims ≥1:10 |
| Schedule | 6 | Equipment table keyed to plan |

## Units

- **Millimetres** on all execution sheets
- **English** labels (contractor-facing Phase 5)

## What external standards do NOT cover

- Blender `matrix_basis` convention → `BUILD_DATA/01`
- AOS agent workflow → `_aos/` (separate universe)
- Software WP specs → hub `LOD300_spec.md` / `LOD400_spec.md` (AOS default, not `BIM-LOD___`)
