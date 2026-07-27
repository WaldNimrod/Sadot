---
id: PROCESS_WP_DEPENDENCY_MAP_2026-07-28_v1.0.0
type: PROCESS_MAP / WP dependency mockup
from: team_100
to: [team_00, team_110, team_70, team_80, team_10]
date: 2026-07-28
domain: sadot
status: ACTIVE
version_note: "v1.1 same day — LOD200 push: P006 fish pond dual-level, P007 irrigation, P004 zones upgraded"
narrative_ref: _COMMUNICATION/team_100/NARRATIVE_LAYER2_PIVOT_2026-07-28_v1.0.0.md
roadmap_ref: _aos/roadmap.yaml
canvas: /Users/nimrod/.cursor/projects/Users-nimrod-Documents-AOS-V5-Sadot/canvases/sadot-layer2-process-mockup.canvas.tsx
---

# Sadot — Process + WP dependency map (Layer-2 + LOD200 push)

## 1. End-to-end flow

```
S001 (closing)
    │
    ▼
S002 ── PARALLEL FORK (LOD200 — push hard before Michal) ──────┐
    │  P001 Export contract           (pri 1)                    │
    │  P002 Swim-pool technical       (pri 2)                    │
    │  P006 Fish pond dual-level      (pri 3) ── hydroponic → deck planters
    │       *** ZERO link to swim pool P002 ***
    │  P007 Garden irrigation+cabinets (pri 4) ◄──► P004 zones (NOT deck planters)
    │  P004 Vegetation zones LOD200   (pri 5)                    │
    │  P003 Terrace details           (pri 6)                    │
    │  P005 Remaining §9              (pri 7)                    │
    │                                                            │
    │              EXTERNAL GATE                                 │
    │         Michal final Revit (Layer-1)                       │
    │              │                                             │
    │              ▼                                             │
    │         ★ STOP ★                                           │
    ▼              ▼                                             │
S003 Convert+lock ◄── P001                                       │
    ▼                                                            │
S004 Dress ◄── merge P002+P003+P004+P006+P007 ───────────────────┘
    │  + renders + team_00 sign-off
    ▼
S005 Delivery — plans · BOQ (mandatory) · presentation · procurement+minimal hub
```

## 2. Stage → what is executed

| Stage | Status | Executes | Output |
|-------|--------|----------|--------|
| **S001** | Closing | Foundation (existing) | KB, research, brief |
| **S002** | **ACTIVE — LOD200 push** | P001–P007 (see §3) | Layer-2 specs ready to dress |
| **GATE** | External | Michal final Revit per P001 | Layer-1 geometry |
| **S003** | BLOCKED | Convert+lock; archive conceptual | Locked `CURRENT_MODEL` |
| **S004** | After S003 | Dress all S002; renders; sign-off | Complete model + visuals |
| **S005** | After S004 | Plans; BOQ; presentation; procurement+hub | Delivery package |

## 3. S002 fork — LOD200 packages

| WP ID | Pri | Depends | Michal blocks? | Produces |
|-------|-----|---------|----------------|----------|
| `SDT-S002-P001-WP001` | 1 | research | No (enables S003) | Export checklist |
| `SDT-S002-P002-WP001` | 2 | team_00 dims | No (location later) | Swim-pool LOD200 |
| `SDT-S002-P006-WP001` | 3 | team_00 intent | No (envelope later) | Dual-level fish/plant + **hydroponic** deck planters — **no link to swim pool** |
| `SDT-S002-P007-WP001` | 4 | P004 zone ids (soft) | No | Garden irrigation + cabinets LOD200 (excludes P006 hydro loop) |
| `SDT-S002-P004-WP001` | 5 | soft P005 | No (XY later) | Vegetation zones + plant allocation LOD200 |
| `SDT-S002-P003-WP001` | 6 | team_80 | No | Terrace details |
| `SDT-S002-P005-WP001` | 7 | Niv | No | Remaining §9 (fish pond = decided intent) |

## 4. Fish pond intent (critical — team_00 clarified)

- Swim pool (`P002`) and fish/plant system (`P006`) are **unrelated** — separate water systems entirely.
- Two levels: **vegetation above / fish below**.
- Concrete planters on the **deck** are irrigated **hydroponically from the fish pond** (not from garden irrigation, not from swim pool).
- Location from Michal; hydraulics + hydroponic loop = Sadot LOD200 now.

## 5. Post-gate hard chain

| From | To |
|------|-----|
| Michal + P001 | S003 convert |
| S003 + P002/P003/P004/P006/P007 | S004 dress |
| S004 dress | S004 renders → S005 presentation |
| S004 dress | S005 plans + BOQ → procurement+hub |

## 6. Visual mockup

Open: [sadot-layer2-process-mockup.canvas.tsx](/Users/nimrod/.cursor/projects/Users-nimrod-Documents-AOS-V5-Sadot/canvases/sadot-layer2-process-mockup.canvas.tsx)
