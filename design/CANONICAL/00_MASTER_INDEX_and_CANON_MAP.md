# 00 · MASTER INDEX & CANON MAP — Sadot (Landscape Architecture · Pardes Hanna)
### The single internal front door. Read this first. · Team 110 · v0.1.0 · 2026-07-08 · **SKELETON**

> Harvested/adapted from `IsraelMicrogreens-BlenderV2-Project/CANONICAL/00_MASTER_INDEX_and_CANON_MAP.md`, 2026-07-08, per `HANDOFF_TO_NEXT_team_110_SADOT_BUILDOUT_2026-07-08_v1.0.0.md` §C.2 (design-dossier SSOT skeleton harvest).

This package (`design/CANONICAL/`) is the **one front door** over the project's living SSOTs. It does **not** replace them — it declares **which document owns which decision**, records the **supersession ledger**, and lists the **open items**. The living SSOTs stay where they are (bound by relative paths + git + BlenderMCP, once authored); `CANONICAL/` *points* to them.

**Status: SKELETON.** Sadot has no real design decisions, geometry, or parts recorded yet — this pass exists to lay the SSOT structure the domain teams (team_110 design lead, team_10 Blender/3D, team_70 Librarian, team_80 research, team_90 validation) will fill starting at **S002** (concept design) and **S003** (detailed design: planting plan + hardscape + site-anchored 3D model). Do not treat any placeholder below as a decision.

## The living SSOTs (authoritative detail lives here — once authored)
| SSOT | Path | Owns |
|---|---|---|
| **Engineering / systems** | TBD — no systems SSOT authored yet; will land under `_COMMUNICATION/team_110/` or a future `design/SYSTEMS/` once S003 opens | hardscape · irrigation · drainage · electrical/lighting · contractor package · BOQ |
| **Spatial / Parts (plants + hardscape)** | TBD — awaits S003 detailed design (no BUILD_DATA-equivalent exists yet) | site datum · hardscape · planting beds · the parts (plants + materials) kit |
| **Live 3D model** | `blender/CURRENT_MODEL.md` (pointer convention harvested; no `.blend` authored yet — see `blender/` once seeded) | the geometry; driven up to the register, never the reverse |
| **Client hub (external face)** | `hub/` (sadot-* clone of the CLIENT_HUB_STANDARD, per team_120 harvest) | client-facing status; a derived VIEW over this canon |

## The worlds → owning document (CANON MAP)
| World | Owner doc | Source SSOT distilled |
|---|---|---|
| Navigation / "which doc?" | **00** (this) | — |
| Decisions & rationale | **01_DECISION_REGISTER** | TBD — no decisions recorded yet; first entries expected from S002 client-brief reconciliation |
| Spatial / geometry | **02_SPATIAL_SSOT** | TBD — awaits site survey (`raw-materials/from-client/`) + S002 concept |
| Parts (plants + materials) | **03_MASTER_PARTS_REGISTER** | TBD — awaits S003 detailed design |
| Systems design (specs) | **04_SYSTEMS_DESIGN_SPEC** | TBD — awaits S003 (irrigation / hardscape / lighting specs) |
| Procurement / cost | **05_BOQ_PROCUREMENT_and_COST** | TBD — awaits S004 (design dossier + BOQ + client submissions) |
| Contractor / open rounds | **06_CONTRACTOR_PACKAGE_and_OPEN_ROUNDS** | TBD — awaits S004 |
| Drawings / renders | **07_DRAWING_SET_and_RENDER_MANIFEST** | TBD — awaits the site-anchored 3D model (S003) |
| Landscape / planting | **08_LANDSCAPE_PLANTING_PLAN** | TBD — awaits plant-selection engine (`knowledge/`) + S003 |
| Schedule | **09_CONSTRUCTION_TIMELINE** | TBD — no committed dates yet; real dates only, no invented placeholders (per portal "no invented dates" convention) |

## Conflict law (when documents disagree)
- **Parts** → **03** wins. **Decisions** → **01** wins. **Geometry** → **02** wins (the model is the geometric tiebreaker). **"Which doc?"** → **00** wins.
- **Recency rule:** the most-current dated decision supersedes older ones, regardless of which file it sits in. Supersessions are logged below.
- **The register drives the model, never the reverse.**

## Status legend
`LOCKED` decided, build as-is · `WORKING` current best, may refine · `PROVISIONAL` depends on an open input · `EXISTING` already on site / in model — match. **None of these apply yet** — every entry in this skeleton is `TBD` until S002/S003 populate it.

## SUPERSESSION LEDGER
*(empty — no decisions have been superseded yet; this table activates the first time a dated decision in `01_DECISION_REGISTER` is revised)*

| # | Topic | SUPERSEDED | CURRENT TRUTH | Where written back |
|---|---|---|---|---|
| — | — | — | — | — |

## OPEN ITEMS REGISTER (consolidated — gates the work)
- **Site survey / client brief** — awaits materials in `raw-materials/from-client/` (Niv Sadot's plot, Pardes Hanna). Populates 02 (geometry) + 01 (decisions).
- **Concept design (S002)** — first real decisions land in 01; first geometry in 02.
- **Detailed design (S003)** — planting plan (08), hardscape + systems specs (04), parts register (03), site-anchored 3D model (02 / `blender/`).
- **Design dossier + BOQ + client submissions (S004)** — populates 05/06/07.
- **`LANDSCAPE_DESIGN` archetype** — proposed to team_100 (inherits `3D_CREATIVE`); `roadmap.yaml` still carries `3D_CREATIVE` as base until sanctioned.

---
*00 · Master Index & Canon Map · v0.1.0 · 2026-07-08 · Team 110. Front door over the (not-yet-authored) living SSOTs; conflict law governs; skeleton only — no supersessions recorded.*
