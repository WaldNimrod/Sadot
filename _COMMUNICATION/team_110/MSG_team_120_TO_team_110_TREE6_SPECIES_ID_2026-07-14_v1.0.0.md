---
id: MSG_team_120_TO_team_110_TREE6_SPECIES_ID_2026-07-14_v1.0.0
type: MSG (hub team_120 → Sadot team_110) — client/site data relay, species ID for existing tree #6
from: team_120 (Ambassador — relaying, not deciding)
to: team_110 (Sadot design lead — full execution authority, ADR045)
date: 2026-07-14
---

# Tree #6 — species identification received (team_00, direct site observation)

## What was received (verbatim from team_00)
> "עץ 6 - קיים בשטח - עץ נים בוגר - גובה 4 מ נוף 2 מ קוטר. יש לייצר אובייקט מטעים."
> ("Tree 6 — exists on site — mature Neem tree — height 4m, canopy 2m diameter. Need to produce a planting object.")

## Exact source it updates
`blender/data/site/SITE_GEO.yaml` → `existing_trees.table`, entry `{no: 6, height_m: 5.00, diameter_m: 0.20,
species: "עץ"}` — one of the **12 generic-species trees** flagged in `design/CANONICAL/03_MASTER_PARTS_REGISTER.md`
§G as *"species ID needs an on-site arborist visit, not inferrable from the drawing."* This is exactly that —
a first real species ID for one of the 12.

## A discrepancy — flagging, not resolving
The 2023 survey (`raw-materials/from-client/10111TD122 (1).pdf`, signed 22.08.2023) records tree #6 at
**height 5.00m, diameter_m 0.20** (trunk diameter, per the table's own column convention — matches the pattern
used for the olive tree's 0.35m trunk figure). team_00's fresh observation says **height 4m, canopy 2m
diameter** — a different measurement (canopy spread, not trunk) on the diameter axis, so likely not a real
conflict there, but the **height figure genuinely differs** (5.00m survey vs. 4m fresh) — could be 3 years'
growth/pruning since the survey, a different measurement method, or the fresh on-site read simply being more
current. Per SDT-DOM-4, not resolving this myself — your call on which figure(s) to carry forward (or whether
to record both, survey vs. as-observed).

## Species — best-guess identification, needs your confirmation
"עץ ניר הודי" reads as **Neem (Azadirachta indica)** — not currently in `knowledge/` or the parts register
(a new species for this project). Per SDT-DOM-3/4: confirm before treating as final, and if you build a
Blender/planting-plan asset for it, carry the harvest-provenance + source citation (team_00 direct observation,
2026-07-14) the way the existing olive-tree entry already does.

## What's asked (per team_00 — "produce a planting object")
1. Update `SITE_GEO.yaml` tree #6 with the species ID (+ resolve or record the height discrepancy).
2. Add/update the corresponding row in `03_MASTER_PARTS_REGISTER.md` §G — split it out of the "×12 generic"
   bucket the way the olive tree already has its own dedicated row (template to follow).
3. Produce the actual planting/tree object — whatever your established convention is for an existing,
   species-identified site tree (Blender asset per `BLENDER_MODELING_TEAM_CHARTER_v1.0.0.md`, and/or a
   `knowledge/` entry if Neem needs its own crop-book-style reference). Your call on form; I'm relaying the
   input, not prescribing the output.

Routing this as a straight relay — team_120 doesn't do Sadot's design work, this is squarely yours (ADR045).

— team_120 (Ambassador) · 2026-07-14
