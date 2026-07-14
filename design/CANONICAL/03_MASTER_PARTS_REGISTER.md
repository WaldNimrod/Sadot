# 03 · MASTER PARTS REGISTER
### Sadot · Landscape Architecture · Team 110 · v0.2.1 · 2026-07-10 · **owns: Parts** · status: **PARTIAL — S001-stage candidate list, NOT the final S003-locked register**

> Harvested/adapted from `IsraelMicrogreens-BlenderV2-Project/CANONICAL/03_MASTER_PARTS_REGISTER.md`, 2026-07-08,
> per `HANDOFF_TO_NEXT_team_110_SADOT_BUILDOUT_2026-07-08_v1.0.0.md` §C.2. Populated 2026-07-10 with a
> candidate parts/asset list (team_00's request, ahead of the formal S003 gate) — synthesized from 4 team_80
> research memos (tire fencing, rockery/kurkar, plant palette, dug pool) plus a direct read of the client brief,
> sketch analysis, and existing plant KB. **This is preparatory — final siting, exact heights/materials, and
> species locks still belong to S002 (concept) and S003 (detailed design); do not treat any P1 item here as
> already built or placed.**

Conflict law: **parts → this register wins.** This is the single parts SSOT — do not restate this content
elsewhere; point here.

## How to read this register

Every part is tagged on three axes:
- **Build Method** — `SCRATCH-PROCEDURAL` (simple parametric geometry — fast, fine at landscape-model fidelity) ·
  `SCRATCH-CUSTOM` (bespoke one-off shape, no off-the-shelf equivalent) · `SOURCED-CANDIDATE` (good fit for this
  project's PolyHaven/Sketchfab/Hyper3D asset-search integrations in Blender — noted for later use, not queried
  yet) · `HYBRID` (scratch base + sourced dressing).
- **Complexity** — rough Blender modeling effort at *landscape-model* fidelity (a site/garden model, not an
  engineered-shell or hero-asset render) — Low / Medium / High.
- **Priority** — **P1** client-confirmed must-have · **P2** design-team-recommended solution to a confirmed
  requirement (not literally named by the client, but the identified correct answer) · **P3** representative
  placeholder (one-per-role filler, swap-ready) · **P4** open/contingent, pending a client decision — do NOT
  build until confirmed · **EXIST** — existing site condition (survey-confirmed), not a new design element.

Cross-cutting constraints shaping *how* several parts get built, not separate parts: the low-maintenance hard
constraint (`CLIENT_BRIEF` §1) caps lawn/planting density; the snake/wildlife concern (§7) means the rockery/path
stone kit needs two deployment variants (void-rich naturalistic vs. void-free/gravel-choked near circulation);
the kurkar/basalt, no-"moon rock" material preference (§6) governs every stone-finish choice.

## A. Boundary & Screening Hardscape — Tire Fence

| Part | Description | Build Method | Complexity | Priority | Notes / Source |
|---|---|---|---|---|---|
| Tire-core wall unit (rammed-earth-filled tire) | Structural "brick" — tire packed ~95% with compacted soil, stacked in running bond, battered courses. Target height 1.8–2.2m. | SCRATCH-PROCEDURAL (stacked torus/cylinder array, per-course batter offset) | Medium | P1 | `RESEARCH_FINDINGS_TIRE_FENCE_CONSTRUCTION_v1.0.0.md` §1–2. Mostly hidden geometry once finished — don't over-invest in tread detail. |
| Render/stucco finish coat over tire face | Full plaster/stucco squaring off the round tire geometry — standard finish + UV-protection layer. | SCRATCH-PROCEDURAL (shrinkwrap/solidify shell) | Low | P1 | Same memo §3 — this is what makes the wall read as stone, not tire. |
| Stone veneer/cladding over rendered wall (kurkar or basalt) | Thin adhered natural-stone veneer — the visible finish; ties to the rockery kurkar/basalt units in §B. | SCRATCH-PROCEDURAL (planar tile array) or HYBRID with sourced stone texture | Low–Medium | P1 | Reconciles tire-fence memo §3 with `CLIENT_BRIEF` §6. |
| Loose used-tire mesh (only if raw tire is ever visually exposed) | Generic worn tire model. | SOURCED-CANDIDATE (Sketchfab) | Low | P3 | Only needed for a construction-progress/budget-alt view — the recommended build hides it entirely. |
| Footing / batter profile (freestanding, non-bermed) | Shallow strip footing + stepped-back coursing. | SCRATCH-PROCEDURAL | Low | P2 | Memo §1–2 — cheap to model, reads correctly either way. |

## B. Rockery / Terrace Stone System — multi-scale kit

**"Varying stone size" = at least 3 distinct mesh scales used together, not one asset repeated.** Two deployment
variants of the same kit: naturalistic/void-rich (beds, set back from circulation) vs. void-free/gravel-choked
(path/seating perimeters) — same parts, different placement density per the snake-safety zoning synthesis.

| Part | Description | Build Method | Complexity | Priority | Notes / Source |
|---|---|---|---|---|---|
| Boulder / anchor stone (>250mm) | Large structural/anchor stones, angular/tabular (NOT rounded) for load-bearing courses. | SOURCED-CANDIDATE (PolyHaven rock scans) | Low (per-instance) | P1 | `RESEARCH_FINDINGS_ROCKERY_HARDSCAPE_KURKAR_v1.0.0.md` §1–2. Explicitly NOT "moon rock" — angular/tabular only for structural courses. |
| Cobble fill stone (~64–250mm) | Mid-size gap-filling stone between anchor boulders. | SOURCED-CANDIDATE or SCRATCH-PROCEDURAL (displaced icosphere) | Low | P1 | Same memo §2 — large-to-small build sequence. |
| Gravel/scree surface dressing (<64mm) | Fine material — path infill, surface dressing. Rounded stone is fine/expected here. | SCRATCH-PROCEDURAL (geo-node scatter) or tileable SOURCED material | Low | P1 | Memo §2 — resolves "no rounded stone" without banning it at the fine end. |
| Dressed kurkar unit (cladding/facing/upper courses) | Cut/shaped kurkar block — porous, soft, native-geology; facing, not heavy structural load. | SCRATCH-PROCEDURAL (beveled slab) + kurkar-toned SOURCED material | Low | P1 | Memo §3 — kurkar as facing, not primary structural stone. |
| Dressed basalt unit (structural/lower courses, coping) | Denser/harder stone for load-bearing courses + higher-abrasion/wet zones (feeds Pool coping, §C). | SCRATCH-PROCEDURAL (beveled slab) + basalt-toned SOURCED material | Low | P1 | Memo §3 + Pool memo §2 — "harder stone lower, softer stone upper." |
| Retaining/terrace course (stepped wall run) | Batter-faced dry-stone course forming one terrace step; several stacked at different heights = "play of heights." | SCRATCH-PROCEDURAL (parametric wall generator) | Medium | P1 | Memo §1 — stepped-terrace-over-one-tall-wall is the standard technique. |
| Drainage backfill zone (crushed rock + geotextile) | Functional layer behind retaining courses — mostly invisible once backfilled/planted. | SCRATCH-PROCEDURAL (simple wedge volume) | Low | P2 | Memo §1 — relevant given Nov–Mar-concentrated rainfall. |
| Void-free path/seating-perimeter treatment | Same stone kit, gravel-choked joints, no open voids — the snake-safety variant. | SCRATCH-PROCEDURAL (denser, no gap) | Low | P1 | Memo §4 zoning synthesis — apply near every path/seating edge. |

## C. Dug Swimming Pool (landscape-level model only)

A site/landscape model, **not** an engineered pool shell — a simple excavated freeform shape + water-surface
material is sufficient; shell engineering is out of scope for this list.

| Part | Description | Build Method | Complexity | Priority | Notes / Source |
|---|---|---|---|---|---|
| Pool excavation shell (freeform curved shape) | Simple dug-out volume matching the kidney-like curve in the client's hand sketch. | SCRATCH-CUSTOM (sculpted/curve-boolean freeform) | Medium | P1 | `RESEARCH_FINDINGS_POOL_CONSTRUCTION_v1.0.0.md` §1 + `CONCEPT_SKETCH_REFERENCE.md` §1 (high-confidence match). |
| Water surface | Flat/near-flat plane with a water shader. | SCRATCH-PROCEDURAL | Low | P1 | Pool memo §1 — no need to model real hydraulics for a landscape render. |
| Pool coping/waterline edge (basalt or travertine) | Tight-fitting, non-porous, non-slip coping — deliberately NOT kurkar here, NOT loose boulders. | SCRATCH-PROCEDURAL (profile-swept slab) + SOURCED material | Low–Medium | P1 | Pool memo §2 — explicit kurkar-vs-basalt-at-waterline caveat. |
| Stepped kurkar/basalt retaining terraces around the pool | Reuses the terrace-course kit from §B around the pool zone. | Cross-ref §B | — | P1 | Pool memo §2 — height variation without a boulder pile at the water's edge. |
| Pool cover (evaporation/algae/debris lever) | Optional flat cover geometry, retracted or deployed. | SCRATCH-PROCEDURAL | Low | P3 | Pool memo §4 — a genuine option, not yet decided. |

## D. Circulation — Paths & Surfaces

| Part | Description | Build Method | Complexity | Priority | Notes / Source |
|---|---|---|---|---|---|
| Winding pebble/stone path | The two parallel curved, oval-pebble-stippled lines sweeping from the pool through the garden. | SCRATCH-PROCEDURAL (curve-driven ribbon + §B edge treatment) + SOURCED pebble scatter material | Medium | P1 | `CONCEPT_SKETCH_REFERENCE.md` §1 — high-confidence sketch match. |
| Path-edge void-free stone treatment | Gravel-choked, tightly-jointed edge along the path's full length. | Cross-ref §B void-free variant | — | P1 | Snake-safety zoning applies to every path edge, not just the pool. |

## E. Confirmed Fruit Trees — client-named, individual species (highest planting priority)

| Part | Description | Build Method | Complexity | Priority | Notes / Source |
|---|---|---|---|---|---|
| Avocado — *Persea americana* (אבוקדו) | Dense evergreen, pruned to 4–6m in practice. | SOURCED-CANDIDATE | Medium | P1 | `PLANT_DEEP_DIVE_S001_P002_v1.0.0.md` §1.1 — climate-safe, water/drainage-demanding; site away from pool drainage. |
| Mango — *Mangifera indica* (מנגו) | Kept 5–8m via pruning; more climate-marginal for fruiting than survival. | SOURCED-CANDIDATE | Medium | P1 | Plant memo §1.2. |
| Pecan — *Carya illinoinensis* (פקאן) | Largest of the five — 15–25m+ mature footprint; wide lateral root spread. | SOURCED-CANDIDATE | Medium–High | P1 | Plant memo §1.3 — flagged as the poorest low-maintenance fit of the five but explicitly requested; site far from pool/deck/hardscape. |
| Carob — *Ceratonia siliqua* (חרוב) | Broad, dense, rounded canopy, 8–12m, often wider than tall. | SOURCED-CANDIDATE | Medium | P1 | Plant memo §1.4 — best low-maintenance fit of all five; the client's own "if feasible" hedge is unwarranted. |
| Banana — *Musa* spp., dwarf Cavendish recommended (בננה) | Giant perennial herb, not a tree — 1.5–2.5m dwarf form; needs wind-sheltered siting. | SOURCED-CANDIDATE | Low–Medium | P1 | Plant memo §1.5 — ties to the banana-circle earthwork, §I below. |

## F. Representative Plant Palette — one-per-role placeholders (lower priority than E, swap-ready)

| Part | Description | Build Method | Complexity | Priority | Notes / Source |
|---|---|---|---|---|---|
| Shade tree — Tabor/Palestine oak, *Quercus ithaburensis*/*calliprinos* (אלון) | Deep-rooted native evergreen, safest long-term hardscape-adjacent shade tree. | SOURCED-CANDIDATE | Medium | P3 | Plant memo §2a. Alt: Mediterranean hackberry (*Celtis australis*). |
| Flowering shrub — Plumbago, *Plumbago auriculata* | Long-blooming pale blue, drought-tolerant, minimal pruning. | SOURCED-CANDIDATE | Low | P3 | Plant memo §2b. Alt: rockrose (*Cistus*) or Cape honeysuckle. |
| Ground cover / lawn-alternative — Silver carpet, *Dymondia margaretae* | Very low-growing, no-mow, drought-tolerant. | SOURCED-CANDIDATE (or tileable material at wide shot) | Low | P3 | Plant memo §2c. **Open design fork:** whether a lawn is wanted at all is unconfirmed — do not model turf grass by default. |
| Screening backbone — Italian cypress, *Cupressus sempervirens* (ברוש מצוי) | Tall columnar evergreen — the real structural answer to the Tasi (west) 2nd-floor screening requirement. | SOURCED-CANDIDATE | Medium | **P2** | Plant memo §2d — "a vine alone reaching genuine 2nd-floor screening is optimistic without a tall support/backbone." |
| Climbing screen vine — Bougainvillea, *Bougainvillea* spp. | Confirmed strong regional fit; thorny (walkway-proximity note). | SOURCED-CANDIDATE | Low–Medium | **P2** | `CLIENT_BRIEF` §8 explicitly asked for "a climbing plant, not a wall or fence" — pairs with the cypress backbone, not a substitute. Alt: pink trumpet vine (*Podranea*). |
| Trellis/support frame for the climbing vine | Simple post-and-wire or lattice frame. | SCRATCH-PROCEDURAL | Low | P2 | Needed regardless of which vine is chosen. |
| Herb/tea bed cluster — za'atar, sage, thyme, lemongrass, lemon verbena | Grouped low planting bed — single "herb bed kit" rather than 5 separate hero models. | SOURCED-CANDIDATE (small-plant packs) | Low | P3 | Plant memo §2e — za'atar flagged as single best-fit herb overall. Mint explicitly EXCLUDED from open-bed planting (container-only if used) — parallels the client's own overgrowth fear. |
| Other KB starter-list species (olive, pomegranate, fig, citrus, loquat, persimmon, jacaranda) | Existing climate-fit shortlist, not client-requested — backup/filler planting. | SOURCED-CANDIDATE, as needed | Low–Medium | P4 (backlog) | `knowledge/crops/PLANT_SELECTION_STARTER.md` — do not model until S002/S003 calls for filler variety. |

## G. Existing Site Trees — survey-confirmed (existing condition, not new design)

| Part | Description | Build Method | Complexity | Priority | Notes / Source |
|---|---|---|---|---|---|
| Generic existing tree (×11) | Unidentified species ("עץ" in survey), heights 2.5–6.5m, diam 0.11–0.34m — real per-tree data available. | SOURCED-CANDIDATE (generic proxy driven by real height/diameter) or SCRATCH-PROCEDURAL | Low | EXIST | `blender/data/site/SITE_GEO.yaml` — species ID needs an arborist visit; preserve-vs-remove per tree deferred to S002. (Was ×12 — tree #6 split out below, 2026-07-14.) |
| Existing olive tree (×1) | 6.00m height, 0.35m diameter, species-identified in survey. | SOURCED-CANDIDATE (olive-specific canopy) | Low–Medium | EXIST | Same source — the one species-confirmed existing tree. |
| Existing tree #6 — Neem, working ID (×1) | Survey: 5.00m height, 0.20m trunk diameter. team_00 direct observation 2026-07-14: mature Neem (עץ ניר הודי, *Azadirachta indica* — working ID, not confirmed), 4.00m height (as-observed, height discrepancy vs. survey flagged not resolved), 2.00m canopy diameter. | SCRATCH-PROCEDURAL (trunk cylinder + canopy icosphere, real dimensions/position) — built 2026-07-14 | Low | EXIST | `blender/data/site/SITE_GEO.yaml` → `existing_trees.table` `tree_6_update_2026-07-14`. Position extracted from the survey PDF via 3-point affine fit (0.000m residual). Objects: `TREE_06_existing_neem_trunk`/`_canopy`. Neem is a new species for this project — not yet in `knowledge/`; add a crop-book-style entry there if/when it recurs. |

## H. Structures — Shed, Pergolas, Deck, Seating

| Part | Description | Build Method | Complexity | Priority | Notes / Source |
|---|---|---|---|---|---|
| Storage shed/structure (hoses + garden equipment) | Simple shed box; must not block Yinon's-window view. | SCRATCH-CUSTOM (simple gable/shed-roof volume) | Medium | P1 | `CLIENT_BRIEF` §2, §2a. |
| Shed shelving/framing sub-component | Possible match to the sketch's mini cabinetry-style dimension callouts. | SCRATCH-PROCEDURAL | Low | P2 (medium-confidence) | `CONCEPT_SKETCH_REFERENCE.md` §4 — not confirmed as garden-related; build only after client confirmation. |
| Work-surface area | Adjacent to the shed; must also not block Yinon's-window sightline. | SCRATCH-PROCEDURAL (counter/bench volume) | Low | P1 | `CLIENT_BRIEF` §2, §2a. |
| Yinon's pergola / Shani's pergola (2 structures) | Existing house-attached features, each child's own room + pergola, back of house. | **Check `HOUSE_IFC_REFERENCE.md` first** — SCRATCH-PROCEDURAL only if not already in the IFC extraction | Medium | P2 | `CLIENT_BRIEF` §2a — do not duplicate if the IFC model already contains these. |
| Planted buffer between the two pergolas | Partial-privacy planting (block one side, keep light on the other) — reuses §F hedge/vine parts. | Cross-ref §F | — | P1 | `CLIENT_BRIEF` §2a — explicit requirement, vegetation not solid structure. |
| Circular gathering pergola/gazebo (possible 3rd structure) | Most structurally elaborate sketch shape — may be a genuine 3rd structure or a misread of the two pergolas above. | SCRATCH-CUSTOM if built | Medium–High | **P4 — open hypothesis, do not build until client-confirmed** | `CONCEPT_SKETCH_REFERENCE.md` §3. |
| Round paved seating area / fire pit (bottom-left sketch shape) | Ambiguous — seating, fire pit, or a tree/planter. | SOURCED-CANDIDATE (fire pit) / SCRATCH-PROCEDURAL (paving) | Low–Medium | **P4 — open hypothesis** | `CONCEPT_SKETCH_REFERENCE.md` §3 — poor match for the storage/work-surface need. |
| Front deck, round-ended (kitchen-adjacent) | The real client-confirmed deck — `IfcSlab #51836` in the architect's IFC. | **Verify against `HOUSE_IFC_REFERENCE.md` first — already sourced from the house-IFC extraction, do not model from scratch** | — | P1 (existence) / verify-before-build | `CLIENT_BRIEF` §9 (resolved). |
| Lattice/mashrabiya privacy-screen panel | Diagonal cross-hatch grid panel beside the house — height ambiguous (1.30/1.50/1.80m, unconfirmed). | SCRATCH-PROCEDURAL (array-modifier lattice grid) | Low–Medium | P2 (medium-confidence) | `CONCEPT_SKETCH_REFERENCE.md` §2 — build parametrically so height can be locked once confirmed. |
| Existing gate + fence gap (east side) | Maintains easy east-side access per the client's earlier sketch annotation. | SCRATCH-PROCEDURAL | Low | P2 | `CLIENT_BRIEF` §8. |
| Parents' 2nd-floor balcony planting | Planter boxes on the existing balcony — smaller, distinct scope from the ground-floor garden. | SCRATCH-PROCEDURAL (planter boxes) + SOURCED small potted plants | Low | P2 | `CLIENT_BRIEF` §2a. |

## I. Garden Features — Beds & Earthworks

| Part | Description | Build Method | Complexity | Priority | Notes / Source |
|---|---|---|---|---|---|
| Vegetable bed (small, organized) | Raised/defined bed, planned not sprawling. | SCRATCH-PROCEDURAL (bed frame + soil material) | Low | P1 | `CLIENT_BRIEF` §4. |
| Banana circle earthwork | Sunken compost-filled pit + surrounding berm, greywater-fed, ringed by banana plants (§E). | SCRATCH-PROCEDURAL (boolean terrain depression + berm) | Low–Medium | P1 | `CLIENT_BRIEF` §4; plant memo §1.5 confirms this is the correct mitigation for banana's high water need. |
| Homogeneous entrance-to-terrace level connection | No-step grade transition so the garage/car-door area and terrace read as one continuous space. | SCRATCH-PROCEDURAL (terrain grading) | Low | P1 | `CLIENT_BRIEF` §3 — a grading note more than a discrete part; flag for the terrain mesh pass. |

## J. Open / Contingent Items — pending client decision (do not build without confirmation)

| Part | Description | Build Method (if adopted) | Complexity | Priority | Notes / Source |
|---|---|---|---|---|---|
| Separate ornamental/fish pond | Small decorative pond, distinct from the swim pool. | SCRATCH-PROCEDURAL shell + SOURCED aquatic plants + water material | Low–Medium | **P4** | `CLIENT_BRIEF` §4/§9 + Pool memo §3 — genuinely undecided; mutually exclusive with the option below, do not build both. |
| Combined swim-pond hybrid (biological filtration, planted regeneration zone) | Alternative — single system serving both swim + ornamental-pond curiosity, larger footprint, greener water. | SCRATCH-PROCEDURAL gravel-bed zone + SOURCED marginal/aquatic plants | Medium | **P4** | Pool memo §3 — real trade-off (footprint, clarity, wildlife-attraction tension with §7) not yet put to the client. |
| Rising/cascading water feature to an upper level | ASR-uncertain — not confirmed as a real request. | N/A | — | **P4 — do not build** | `CLIENT_BRIEF` §4, §9. |
| Dense "tangle" canopy shape / organic "blob" bed (sketch, center) | Possibly a large shrub/tree canopy + adjacent labeled bed — could overlap with the pergola-buffer hypothesis in §H. | N/A until clarified | — | **P4** | `CONCEPT_SKETCH_REFERENCE.md` §3 — deliberately not asset-ized; routed to the live client-question doc. |

## K. Terrain & Site Base (already exists — cross-reference only, not new parts)

| Part | Status | Source |
|---|---|---|
| Terrain mesh | Already generated | `blender/data/site/terrain.obj` |
| House shell | Already exported from IFC | `blender/data/site/house_shell_v1.obj` |
| Site boundary/orientation datum | Survey-confirmed | `blender/data/site/SITE_GEO.yaml` |

Any grading changes implied by §I (level-continuity, banana-circle earthwork) modify this existing terrain
mesh — they are not separate new geometry files.

**Fill + soil note (team_00, 2026-07-10):** most of the yard currently sits below final target grade — hamra
fill is planned to bring it up. Fill (and existing ground generally) is debris-laden (construction rubble)
essentially everywhere except the already-good-grade east path — a real cost/method factor for every
excavation-touching part above (pool shell §C, banana circle + vegetable bed §I, retaining-course footings
§B). See `blender/data/site/SITE_GEO.yaml` → `soil_and_grade` for full detail; not a substitute for a formal
geotechnical test.

## Reconciliations applied this pass

Populated from a TBD skeleton (2026-07-08) using 4 team_80 research memos (tire fencing, rockery/kurkar, plant
palette, dug pool — all `_COMMUNICATION/team_80/`) plus a direct read of `CLIENT_BRIEF_NIV_SADOT_v1.0.0.md`,
`CONCEPT_SKETCH_REFERENCE.md`, `08_LANDSCAPE_PLANTING_PLAN.md`, and `knowledge/crops/PLANT_SELECTION_STARTER.md`.

## Open items feeding back into other canon docs

- §H's IFC-verification flags (pergolas, deck) should be checked against `HOUSE_IFC_REFERENCE.md` before any new
  geometry is built, to avoid duplicating what the house-IFC extraction already contains.
- §H/§J ambiguous sketch items (gazebo, seating/fire-pit circle, tangle/blob) should stay unbuilt until
  `_COMMUNICATION/team_70/DRAFT_WHATSAPP_TO_NIV_CLARIFICATIONS_v1.0.0.md` gets client answers.
- This register is downstream of S002 (concept design) siting decisions — heights, exact placements, and final
  species/material choices are not yet locked; parts here are asset-scoped, not placed.

## OPEN-PN register (parts needing a final part number / SKU)

TBD — SKU assignment awaits S003 procurement (`05_BOQ_PROCUREMENT_and_COST.md`); this pass is asset/modeling
scope only, not a bill of materials.

---
*03 · Master Parts Register · v0.2.0 · 2026-07-10 · Team 110. S001-stage candidate list — asset-scoped, not
placed/locked; final register still awaits S003.*
