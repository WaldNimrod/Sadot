---
id: RESEARCH_FINDINGS_S001_P002_v1.0.0
type: team_80 research findings (ADR044 Track 4 — advisory, not part of the gate process)
from: team_80 (Research) under team_110 direction
to: team_110 (Domain Architect) / team_00 (Principal)
date: 2026-07-08
project: sadot
---

# S001-P002 Research Findings — Sadot

## WP001 — Israeli climate/soil, general (non-plot)

Delivered: `knowledge/climate/ISRAELI_CLIMATE_SOIL_PARDES_HANNA.md`. Summary: Pardes Hanna sits in Israel's Sharon
coastal plain, Köppen Csa (hot-summer Mediterranean) climate — hot dry summers (~May-Oct), mild wet winters carrying
essentially all of the region's ~500-650mm/year rainfall. Regional soil is typically "hamra" (reddish sandy clay
loam over kurkar sandstone), moderately well-drained, historically favored for citrus/orchard agriculture in this
belt. **Caveat, stated explicitly in the artifact:** this is regional-prior knowledge, not a lab soil test or a
plot-specific sun/shade/drainage survey — those require the client survey (see WP004 below).

## WP002 — Plant-selection candidate shortlist

Delivered: `knowledge/crops/PLANT_SELECTION_STARTER.md` (produced alongside the crop-KB harvest, since both draw on
the same source schema). 10-15 species generally suited to a private Mediterranean-climate coastal-plain garden,
each tagged with which harvested crop-KB concept it maps to (e.g. `category='fruit_trees'`). Explicitly marked
NOT plot-final.

## WP003 — Permaculture/ecological design principles + precedents

Delivered as `knowledge/permaculture/` (5 files: `00_INDEX.md`, `01_ZONES_AND_SECTORS.md`,
`02_GUILDS_AND_PLANTING_STRATEGY.md`, `03_WATER_AND_SWALES.md`, `04_CREDENTIALS_AND_PRECEDENT.md`). Standard
Mollison/Holmgren zone-and-sector, guild, and water-harvesting/swale methodology, adapted for small-residential-plot
scale, anchored to Nimrod's cited real credentials (PDC 2014 @ Solar Garden Binyamina, Havat Adam ecological-
agriculture study, biochar project) per `nimrod-book/chapters/11_ERA_GARDEN_2013_2023.md`.

## WP004 — Plot-specific site analysis

**BLOCKED.** `raw-materials/from-client/` is empty — no plot survey (topography, sun/shade, drainage, soil test,
existing vegetation) has been received from Niv Sadot. No placeholder/fabricated plot data was produced. Unblock
condition: client delivers survey materials to `raw-materials/from-client/`; this WP and its downstream dependent
(`SDT-S001-P003-WP002`, the formal site-analysis dossier + client brief) then become actionable.

## Routing

Per team_80's own governance contract (advisory, ADR044 Track 4, not part of the gate process): these findings are
delivered to the architecture layer (team_110) for use in `knowledge/` and future S002/S003 spec work. No gate
verdict is issued or required for this artifact.
