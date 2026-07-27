---
id: NARRATIVE_LAYER2_PIVOT_2026-07-28_v1.0.0
type: NARRATIVE / RACI / stage-skeleton
from: team_100 (Chief Architect)
to: [team_00, team_110, team_70, team_80, team_10]
cc: [team_120]
date: 2026-07-28
domain: sadot
status: ACTIVE — team_00 ratified in session 2026-07-28
supersedes: prior "full site design in Blender" precision track
---

# Sadot — Layer-2 Narrative Pivot (2026-07-28)

## 1. Why this pivot

Planning the **entire site** (levels, paths, retaining walls, pool siting) inside Blender proved too complex for the agent stack. That precision track is **stopped**.

New operating model: **Michal (Revit) owns Layer 1 (site)**. Sadot owns **Layer 2** (materials, pool technical design, planting, irrigation, execution package, BOQ, presentations).

## 2. RACI — Layer split

| Layer | Owner | Delivers |
|-------|--------|----------|
| **Layer 1 — Site** | Michal (Revit) | Full model: paths, elevations/levels, exact pool location + size, deck, stairs, main cast retaining walls, terrace locations + heights |
| **Layer 2 — Garden / details** | Sadot (this project) | Materials and construction details; technical design of pools; all planting / vegetation / irrigation; terrace build method + materials (not location/height); garden execution plans; **BOQ (mandatory)**; procurement lists (plants, equipment); presentations and renders |

**Existing Blender model** (`blender/milestones/sadot_current.blend`, history in `blender/CURRENT_MODEL.md`):

- Treat as **coarse reference + initial conceptual design** only.
- Direction is roughly correct; **not** final precision.
- Do **not** continue site-tie / roof precision / DWG ask as a critical path.

## 3. Gate flow

```
S002 Layer-2 Pre-Revit  →  Michal final Revit  →  STOP + convert to Blender
        →  dress all Layer-2 work onto locked base  →  S004 complete in situ
        →  S005 execution package (plans, BOQ, procurement, presentations)
```

1. **Now:** begin Layer-2 thinking and technical planning (not blocked on final Revit).
2. **On Michal final model:** stop placement work → convert into our Blender workspace → dress everything built so far onto the updated model → then free to finish the project.
3. **End deliverables:** garden execution plans + procurement lists + **BOQ required** + presentations/renders. Client hub for Niv stays **minimal**.

## 4. Milestone skeleton (post-pivot)

| Milestone | Role | Status intent |
|-----------|------|----------------|
| **S001** | Foundation: env / KB / research / brief | Wind-down → COMPLETE; §9 client items execute under S002-P005 |
| **S002** | Layer-2 Pre-Revit (active focus) | ACTIVE |
| **S003** | Revit → Blender conversion + lock site base | PLANNED / BLOCKED on Michal |
| **S004** | Dress Layer-2 onto locked model + in-situ completion + renders | PLANNED after S003 |
| **S005** | Delivery: execution plans, BOQ, procurement, presentations, minimal hub | PLANNED after S004 |

SSOT live state: `_aos/roadmap.yaml` + `_aos/MILESTONE_MAP.md`.

## 5. S002 priority order (team_00 — LOD200 push 2026-07-28)

1. **P001** — Revit export contract for Michal (one short page; minimum overhead).
2. **P002** — Swim-pool technical design **LOD200**.
3. **P006** — Dual-level fish/plant pond **LOD200** + **hydroponic** irrigation of deck planters from the fish pond. **Zero coupling** to the swim pool (`P002`).
4. **P007** — Garden irrigation system **LOD200** (zones, mains, cabinets) — does **not** feed the deck planters (P006 owns that).
5. **P004** — Vegetation zones + initial plant distribution **LOD200** (research + zone map).
6. **P003** — Terrace construction materials / details.
7. **P005** — Remaining client brief §9 (Adas, climbing, refs, sketch); fish-pond item treated as decided intent.

Push hard on P002/P006/P007/P004 before Michal arrives — do not wait idly for Layer-1.

## 6. Frozen / superseded as precision path

- Old S002 (narrative + schematic massing as hard gate) — **superseded as dependency**; concept = existing Blender + Michal Revit.
- “Build full site from scratch in Blender” (`SDT-S003-P003-WP001` old framing) — **replaced** by S003 Revit conversion.
- Roof precision / DWG site-tie as blockers — **frozen**.

## 7. Prep for Michal materials (P001 constraint)

Before receipt: research and define **exactly how Michal should export** (format, units, datum, required categories). One-shot checklist. **Do not create overhead for her.**

## 8. Out of scope of this narrative

AOS new-version review vs domain docs + coordination with team_120 is a **separate side track** — see sibling artifact `NOTE_AOS_VERSION_REVIEW_SIDE_TRACK_2026-07-28_v1.0.0.md`. It does not block S002–S005 domain work.

## 9. Authority

Ratified by team_00 in session 2026-07-28. team_100 authored this narrative and the matching roadmap / milestone / PROJECT_CONTEXT updates.
