---
id: S002-LOD300-milestone
type: LOD300_milestone
stage: S002
authored_by: team_100 (Chief Architect)
date: 2026-07-28
status: ACTIVE
authority: team_00 Layer-2 pivot + LOD200 push 2026-07-28
narrative_ref: _COMMUNICATION/team_100/NARRATIVE_LAYER2_PIVOT_2026-07-28_v1.0.0.md
process_ref: _COMMUNICATION/team_100/PROCESS_WP_DEPENDENCY_MAP_2026-07-28_v1.0.0.md
---

# S002 — Milestone Scope: Layer-2 Pre-Revit (LOD200 push)

## 1. Scope statement

Advance **as much Layer-2 design as possible** before Michal’s final Revit. Target **LOD200** for
irrigation, vegetation zones, swim-pool tech, and the dual-level fish/plant pond system — not mere
mood/concept sketches.

**On Michal final Revit:** STOP placement → S003 convert → S004 dress all S002 outputs → S005 deliver.

## 2. Work packages (priority order)

| Priority | WP | Label | AC (1-line) | LOD |
|----------|-----|-------|-------------|-----|
| 1 | SDT-S002-P001-WP001 | Revit export contract | One short checklist for Michal; no overhead | 100 |
| 2 | SDT-S002-P002-WP001 | Swim-pool technical | LOD200 structure/materials/sections; dims from team_00 | 200 |
| 3 | SDT-S002-P006-WP001 | Dual-level fish/plant pond + hydroponic deck planters | LOD200: two levels (plants / fish); deck planters hydroponic from fish pond ONLY; **zero link to swim pool** | 200 |
| 4 | SDT-S002-P007-WP001 | Irrigation + cabinets | LOD200 zones, mains intent, cabinet/controller schedule; low-maintenance | 200 |
| 5 | SDT-S002-P004-WP001 | Vegetation zones + distribution | LOD200 zone map + initial plant allocation (research); not final bed XY | 200 |
| 6 | SDT-S002-P003-WP001 | Terrace details | Build method + materials | 200 |
| 7 | SDT-S002-P005-WP001 | Remaining §9 | Adas / climbing / refs / sketch; fish pond treated decided | 100 |

**Superseded:** `SDT-S002-P001-WP002` (old massing).

## 3. Dual-level fish pond — design intent (team_00, clarified)

- **Completely separate** from the swim pool (`P002`) — no shared water, filtration, or hydraulics.
- **Two levels:** upper = vegetation; lower = fish.
- **Deck planters:** concrete planters (perlite) on the deck, irrigated **hydroponically from the fish pond** (aquaponic/hydroponic loop).
- Garden irrigation (`P007`) does **not** feed those planters — P006 owns that loop alone.
- Location/envelope size from Michal (Layer-1); technical system = Sadot LOD200 now.

## 4. Dependency graph

```
P001 ──────────────────────────────► S003 convert (later)

P002 swim pool ────────────────────► S004 dress
P006 fish pond + deck planters ────► S004 dress
P007 irrigation ◄── zone ids ── P004 vegetation zones ──► S004
P003 terraces ─────────────────────► S004
P005 §9 (soft) ──► P004

Michal Revit (EXTERNAL) ──► S003 ──► S004 merge all above
```

**Fork rule:** P001–P007 may run in parallel after P001 is started; P006/P007/P004 are the LOD200 volume of work before Michal.

## 5. Explicit freezes

- Full site precision in Blender — STOPPED
- Roof / DWG site-tie as blockers — FROZEN
- Exact bed XY on final levels — waits for S003/S004 (LOD200 zones are allowed now)

## 6. Deliverable paths (target)

| WP | Suggested artifact |
|----|-------------------|
| P001 | `_COMMUNICATION/team_70/REVIT_EXPORT_CHECKLIST_FOR_MICHAL_v1.0.0.md` |
| P002 | `design/CANONICAL/POOL_SWIM_TECHNICAL_LOD200_v1.0.0.md` |
| P006 | `design/CANONICAL/FISH_POND_DUAL_LEVEL_HYDROPONIC_LOD200_v1.0.0.md` |
| P007 | `design/CANONICAL/IRRIGATION_SYSTEM_LOD200_v1.0.0.md` |
| P004 | `design/CANONICAL/VEGETATION_ZONES_LOD200_v1.0.0.md` |
| P003 | `design/CANONICAL/TERRACE_DETAILS_LOD200_v1.0.0.md` |
