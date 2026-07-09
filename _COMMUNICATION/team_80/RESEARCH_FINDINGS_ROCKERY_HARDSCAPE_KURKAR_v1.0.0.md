---
id: RESEARCH_FINDINGS_ROCKERY_HARDSCAPE_KURKAR_v1.0.0
type: team_80 research findings (ADR044 Track 4 — advisory, not part of the gate process)
from: team_80 (Research) under team_110 direction
to: team_110 (Domain Architect) / team_00 (Principal)
date: 2026-07-10
project: sadot
mandate: ad hoc — direct research request (not yet tied to a numbered roadmap WP); method used was
  unsupervised web research (WebSearch/WebFetch), not a formal ADR046 §2.6 team_00-approved engine plan —
  flagging this gap explicitly per governance contract Rule 3, in case a retroactive pre-approval record is
  required for this task.
feeds: design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md §6 (materials/hardscape preference) + §7 (safety/snake
  consideration); intended input to future S002 concept design hardscape spec and
  design/CANONICAL/08_LANDSCAPE_PLANTING_PLAN.
---

# Rockery / Dry-Stone Terracing Technique Research — Kurkar + Basalt, Snake-Safety Zoning

## 0. Scope and honesty framing (read this first)

This memo mixes three tiers of evidence quality — flagged inline throughout, not just here:

1. **Well-established general landscape-construction engineering knowledge** — dry-stone retaining wall
   mechanics, rockery gradation, drainage backfill. Sourced from a US federal highway engineering guideline
   (FHWA) and professional dry-stone-wall trade bodies. This is real, load-bearing-relevant engineering
   knowledge, though written for a broader range of wall heights than a typical residential terrace — treat
   the specific numbers as upper-bound/conservative, not as a substitute for a site-specific mason's judgment
   on a private garden of this scale.
2. **Moderately-sourced Israeli-market practice** — kurkar/basalt material combination as an actual current
   trend in Israeli residential landscaping. Sourced from Israeli gardening-industry and consumer-facing
   sites (not engineering literature), so treat as *practice confirmation*, not an engineering spec.
3. **Adapted general guidance, not rockery-specific** — the snake/wildlife-hiding-spot material (§4) comes
   from general snake-deterrence and pest-management landscaping sources (mostly US extension services and
   pest-control industry), **not** rockery-engineering literature and **not** Israel/Sharon-plain-specific.
   The reconciliation with the "play of heights" aesthetic in §4 is team_80's own design synthesis, not a
   single sourced technique — flagged explicitly where it appears.

No source found addresses "kurkar + basalt rockery terracing with snake-safe zoning" as one integrated
technique — that combination is this memo's own synthesis across three separate literatures.

---

## 1. Dry-stone / rockery terracing techniques for grade changes

**Well-established** (FHWA rockery design guidelines; The Stone Trust dry-stone-wall specifications) — see
Sources.

- **Batter (backward lean of the wall face):** dry-stone retaining structures are never built plumb; the
  face leans back into the slope. Trade guidance for smaller fieldstone garden walls: roughly **1–3 inches
  of setback per vertical foot** (fieldstone tends toward the higher end, more structured cut stone toward
  the lower end). The FHWA rockery-specific guideline (aimed at larger engineered rockeries, e.g. highway
  embankments) specifies a face batter of **4V:1H to 6V:1H** and requires base-course rocks sloped back at
  least 5% toward the hill — directionally the same principle (lean back, don't go vertical), but that
  guideline's numeric detail is calibrated for taller, engineered structures than a residential terrace and
  should not be applied literally without a mason's judgment on wall height here.
- **Base/foundation course:** a leveling/founding course of coarse, angular, crushed drain rock beneath the
  first course of facing stone — FHWA specifies **≥300 mm (12 in)** of 100–150 mm crushed angular rock; for
  a sloping "toe" (the ground in front of the wall also slopes away, relevant on a multi-level terraced
  garden) it calls for substantially more horizontal soil buffer in front of the wall for stability. This is
  the kind of detail worth raising with whoever builds the walls if any single terrace step exceeds roughly
  waist height.
- **Drainage backfill:** a persistent theme across every source — a dry-stacked stone retaining
  structure **must** have a free-draining zone behind it, not native soil packed directly against the
  stone. Standard practice: clean angular crushed stone (roughly ¾"–1½", i.e. ~20–40 mm) backfilled directly
  behind the wall, often with a perforated drain pipe at the base, separated from surrounding native soil by
  non-woven geotextile fabric (to stop fines migrating in and clogging the drainage zone over time). This
  matters even in a low-winter-rainfall climate like Pardes Hanna's, because the region's ~500–650 mm/year
  falls almost entirely Nov–Mar (per `knowledge/climate/ISRAELI_CLIMATE_SOIL_PARDES_HANNA.md`) — concentrated
  wet-season loading behind a retaining structure is exactly the failure mode drainage backfill exists to
  prevent, even without a genuine frost/freeze-thaw risk (which this climate does not have).
- **Rock selection for structural courses:** rockery/dry-stone-wall literature consistently specifies
  **angular, tabular, or roughly rectangular stone with the long dimension set into the wall (perpendicular
  to the face)** for load-bearing courses — rounded boulders/cobbles are explicitly discouraged as
  *structural* facing stone because they don't interlock; rounded stone is instead recommended for
  decorative/non-structural uses (dry creek beds, surface texture, borders). This is a genuinely useful
  distinction for this project — see §2.
- **Capping:** the top course uses smaller, flatter cap stones, still substantial (FHWA: ≥90 kg/200 lb for
  its engineered scale — again, a conservative upper-bound number, not a residential-scale requirement).
- **Stepped terraces on a slope:** the general technique for "play of heights" on a sloped residential lot is
  a series of these retaining courses at different heights creating level planting/circulation shelves,
  rather than one tall wall — smaller individual retaining heights are both more stable for dry-stack
  construction (lower overturning force per wall) and read visually as more varied/staggered terrain, which
  maps directly onto the client's stated preference against one flat/uniform surface.

## 2. How "varying stone size" is actually achieved in a real rockery

**Well-established**, and directly useful for answering the client's own phrase ("מסלעה לטרסות בגודל אבנים
משתנה"):

- Industry rock-size classification (roughly): **boulder** (>250 mm / 10 in), **cobble** (~64–250 mm /
  2.5–10 in), **gravel/pebble** (~4–64 mm), **fines/scree** (<4 mm). A rockery that reads as "natural" almost
  always uses **at least three of these size classes together in the same bed**, not one — this is the
  literal opposite of the uniform "moon rock" look the client dislikes (which is usually a single size class
  of one rounded, uniformly-colored stone repeated across the whole bed).
- Standard build sequence, consistent across every source checked: **place the largest boulders first** as
  the structural/anchor stones (partially buried, following the way they'd naturally sit — one flatter face
  down, mimicking a rock outcrop rather than stones dropped on top of soil), **then work down in size** —
  medium cobbles fill gaps and transition zones between the big anchor stones, and fine gravel/decomposed
  stone is the last layer, used as surface dressing, path infill, and the visual "connective tissue" between
  the larger stones and the planting beds.
- The natural-terrain effect the client is describing is essentially a **scree/talus gradation** — coarse,
  large material at the base/structural points, progressively finer material as fill and surface finish. A
  single-size bed (all boulders, or all cobbles) reads as artificial/manufactured precisely because real
  weathered slopes never sort that cleanly.
- **Where rounded stone still belongs:** rockery literature discourages rounded stone specifically for
  *load-bearing structural facing* — but rounded cobbles remain a legitimate and even desirable choice for
  the *fine/surface* end of a graduated bed (dry-creek-style texture, path edging, decorative infill). This
  means the client's two stated preferences aren't actually in tension: reject the *uniform, all-one-size,
  all-rounded* "moon rock" aesthetic as the *entire* material palette, while still allowing some rounded
  material at the small end of a properly graduated, angular-anchored bed. Worth flagging explicitly to the
  client/mason so "no rounded stone at all" isn't over-applied as a rule.
- Israeli residential-garden industry sources (מסלעה guides) independently confirm this is standard local
  practice, not just a foreign-guide construct: local **מסלעה** ("rockery/stone-terrace") construction
  commonly names **layered/large "sela shekhavot" (bedding-plane) stones or boulders** as the structural base,
  combined with basalt, dolomite, and "ג'מעין" (pale flat local stone), and describes the rockery's explicit
  function as overcoming a sloped/graded site and creating natural-looking terraces for planting — matching
  this project's brief almost exactly.

## 3. Kurkar specifically

**Well-established (geology/material science):**

- Kurkar is an **aeolian (wind-blown) quartz sandstone with carbonate cement** — a lithified ancient coastal
  dune, technically a calcarenite/eolianite, found along the Levantine coastal plain including the Sharon
  region (consistent with `knowledge/climate/ISRAELI_CLIMATE_SOIL_PARDES_HANNA.md` §2's "hamra soil over
  kurkar sandstone" regional profile).
- It is **porous**: reported water absorption in the range of roughly **3.4–8.6% by weight**, with a
  "saturation coefficient" around 0.3–0.6 in one materials-science analysis — indicating moderate resistance
  to some weathering modes but real vulnerability to erosion via capillary water absorption. It is
  consistently described as **soft and easy to quarry/shape** relative to basalt or granite, which is exactly
  why it's traditionally used for cladding and lighter masonry rather than as a primary structural/load-bearing
  stone in tall walls.
- **Documented weathering risk is specifically salt/sea-spray weathering**, not general outdoor exposure —
  studies of historic kurkar sea walls (e.g. Ottoman/Napoleonic-era fortifications at Akko) found significant
  strength loss in weathered material (roughly 16–23% compressive-strength loss, 18–35% modulus-of-rupture
  loss vs. fresh stone) attributable to direct marine salt exposure, and note that kurkar coastal cliffs
  generally are actively eroding/crumbling today.
- **Freeze-thaw is a non-issue here**, consistent with this climate's Csa (hot-summer Mediterranean)
  classification and effectively no winter freezing at Pardes Hanna's elevation/latitude — this is the one
  major durability risk factor that does NOT apply to this material in this location, even though it's
  usually the first thing raised about porous sedimentary stone in colder climates.

**Team_80 inference, not directly sourced (flagged as such):** Pardes Hanna-Karkur sits roughly 8–10 km
inland from the coast (nearest coastal town, Caesarea, is ~8 km away) — it is **not** a direct sea-spray
environment the way the historic seawalls in the weathering studies were. The specific salt-weathering
failure mode documented in the literature is plausibly of **much lower relevance** at this inland site than
at an immediate seafront location. This is a reasonable extrapolation from the material science, but it has
not been separately tested/confirmed for this specific inland exposure — worth a direct question to a local
mason (see Open Questions) rather than treating as settled.

- **General moisture note (not kurkar-specific, general principle for soft porous carbonate stone):** expect
  some surface staining/efflorescence over years of wet-season exposure (Nov–Mar rains per the climate KB),
  and expect kurkar to be **the softer, weaker partner** in any kurkar+basalt combination — consistent with
  the rockery-engineering guidance in §1 that structural/load-bearing courses want harder, more durable
  stone. Practical implication: kurkar reads well as the visually dominant/warm-toned material and as facing,
  capping, or upper/lighter-load courses, while basalt (denser, harder, darker) is the natural choice for any
  course under greater structural load or higher abrasion/foot-traffic exposure — this is a general
  stone-selection principle, not a citation specific to this pairing.

**Moderately-sourced (Israeli market/practice):**

- Combining **kurkar (or other pale local stone) with basalt** for visual contrast is confirmed as a real,
  current, popular technique in Israeli residential landscaping — multiple Israeli gardening/hardscape
  industry sources describe basalt's dark, dense, angular character as a deliberate contrast material against
  paler local stone (kurkar, dolomite, "ג'מעין"), commonly used for edging/borders/accent lines against a
  lighter field, and describe a general trend toward "layered materials" (a practical drainage/stability base
  layer, an aesthetic surface layer, precise edging between them to stop stone migration) as increasingly
  standard practice. This directly supports treating the client's own "kurkar + possibly basalt, mixed" idea
  as a genuinely conventional, buildable local design, not a novel ask.

## 4. Snake/wildlife-hiding-spot safety (client brief §7) vs. the "play of heights" aesthetic

**Explicitly flagged: this section is adapted general guidance, not rockery-engineering literature and not
Israel-specific.** Sources are US extension services and pest-control industry pages discussing snakes in
residential landscaping generally. No source specifically addresses rockery/mesola construction technique
for snake safety, and none is calibrated to Israeli/Sharon-plain snake species. Treat this section as a
reasonable starting framework to validate with a local pest-control or landscape professional, not as settled
guidance.

**What the general sources agree on:**

- The actual risk factor is **voids/gaps large enough to shelter an animal**, not stone size or "rockery"
  as a category per se. Large gaps between stacked stones are repeatedly named as the primary hiding
  mechanism.
- Mitigation is achieved by **closing gaps at ground level with smaller compacted material** — crushed rock
  or compacted gravel used as choking/infill between larger stones removes the void without removing the
  larger stones themselves.
- **Interfaces between rockery and hard structures are a specifically named risk** — joints/seams where a
  rock feature meets a patio, step, or wall edge are called out as common refuge/overwintering points, and
  the general recommendation is to seal or tightly grout those specific contact joints.
- Keeping **ground-level vegetation trimmed back** at the base of any stone feature near circulation areas is
  named as compounding mitigation — tall grass or dense low ground cover against a rock face defeats gap-
  closing efforts by re-creating concealment at the surface even if the stone joints are void-free.
- One source (lower confidence, single citation) claims **sharp/angular surface stone somewhat discourages
  basking** near structures compared to smooth stone — noted here as a minor point, not something to design
  around on its own.

**Team_80 design synthesis (not a sourced technique — flagged as our own reconciliation, for the
architect/mason to validate):** the client's dislike of flat/uniform terrain and this safety concern are not
actually in conflict if handled by **zoning**, which is consistent with the client's own "play of heights,
play of zones" framing:

- In beds and slopes **set back from paths, seating, and thresholds**, build the naturalistic, graduated,
  intentionally void-rich rockery described in §1–2 — large anchor boulders, open structural gaps, loose
  cobble/scree texture. This is also where the height/terrain drama is most visible anyway (background/mid-
  ground planting beds, not the immediate walking surface).
- In the **immediate perimeter of paths and seating** (a buffer distance the client and mason should agree
  on directly — general snake-deterrence sources don't give one specific number, this is a judgment call, not
  sourced), use the same kurkar/basalt material palette but with a **void-free treatment**: gravel-choked
  joints, mortared/grouted contact points, or a compacted decomposed-stone surface rather than loosely stacked
  large stone — and continue the height variation through grade changes/steps rather than through open rock
  voids at exactly the points where people walk and sit.
- Continue trimming ground cover back from all stone edges near circulation, per the general guidance above,
  regardless of zone.

This zoning approach lets the same stone palette and the same "varied heights" concept run through the whole
garden, while concentrating the genuinely loose/void-rich rockery expression away from where people are.

---

## Open questions for a real contractor/mason (not resolved by desk research)

1. **Inland salt-weathering relevance:** does kurkar's documented salt/sea-spray weathering risk meaningfully
   apply ~8–10 km inland at Pardes Hanna, or is that specifically a direct-seafront phenomenon that doesn't
   transfer here? (Team_80 inference above says "probably low relevance," but this needs a real answer from
   someone who's built with kurkar away from the coast.)
2. **Sourcing:** is genuine quarried kurkar (vs. a manufactured/concrete "kurkar-look" product, which at least
   one Israeli source mentions as a cheaper alternative) actually available and cost-appropriate for this
   project at the volumes needed, and from where?
3. **Load-bearing course design:** for whatever the tallest single terrace retaining height ends up being in
   the final grading plan, is dry-stack (no mortar) appropriate at that height, or does the design need
   mortared/reinforced courses at the base with dry-stack only above a certain height — and does that change
   the kurkar-vs-basalt allocation (harder stone lower, softer stone upper)?
4. **Snake-safety buffer distance:** what void-free perimeter distance around paths/seating does a local
   pest-control or landscape professional actually recommend for the species present in this specific region
   — the general sources reviewed here don't give a number, and Israeli-specific/species-specific guidance
   was not found in this pass.
5. **Maintenance implication:** given the client's #1 stated priority is low maintenance (brief §1), does a
   graduated multi-size rockery (more surface area, more joints, more places for weeds/leaf litter to
   accumulate) create a maintenance burden that conflicts with that priority, and if so, what construction
   choices (geotextile under gravel infill, joint sealing, plant selection at the rockery edge) reduce that
   burden without losing the aesthetic?
6. **Drainage sizing:** what climate KB in this repo gives as regional rainfall (~500–650 mm/yr, concentrated
   Nov–Mar) is a desk figure — does the mason want a real winter-storm-intensity number (mm/hr peak) to size
   backfill drainage/pipe capacity behind any retaining courses, rather than relying on the annual total?

---

## Sources

- [SECTION 04600 Dry Stone Wall Retaining System — The Stone Trust](https://thestonetrust.org/wp-content/uploads/2013/12/Design-Specifications-For-Dry-Stonewall-Retaining-Systems.pdf)
- [Build a Dry-Stacked Stone Retaining Wall — Fine Gardening](https://www.finegardening.com/article/build-a-dry-stacked-stone-retaining-wall)
- [Dry Stacked Stone Walls — ASLA](https://www.asla.org/news-insights/the-field/dry-stacked-stone-walls)
- [Retaining Wall Challenges — The Stone Trust](https://thestonetrust.org/retaining-wall-challenges/)
- [ROCKERY DESIGN AND CONSTRUCTION GUIDELINES, FHWA-CFL/TD-06-006 — US Federal Highway Administration](https://www.fhwa.dot.gov/clas/ctip/rockery_design_construction_guidelines/ch_5_guidelines.aspx)
- [Rockery Rocks: Sizes, Types & How to Choose — Harbor Soils](https://blog.harborsoils.com/rockery-rock-guide/)
- [A Step-By-Step DIY Guide on How to Build Rockery Gardens — Outdoor Aggregates](https://outdooraggregates.com/diy/aesthetic-features/how-to-build-rockery/)
- [Rock Size Chart for Landscaping and Construction Projects — Hello Gravel](https://hellogravel.com/guides/rock-size-chart-for-landscaping-and-construction-projects/)
- [Kurkar — Wikipedia](https://en.wikipedia.org/wiki/Kurkar)
- [A Dune Disguised as Stone: How Soft Sand Became the Walls that Stopped Napoleon — Nir Topper](https://www.nirtopper.com/post/kurkar)
- [Deterioration of Sandstone in Historical and Contemporary Sea Walls — MDPI Applied Sciences](https://www.mdpi.com/2076-3417/11/15/6892)
- [Stones Park — Kurkar Stone (product/material page)](https://www.stones-park.com/en/Kurkar+Stone)
- [אבנים לעיצוב גינה — Gan Even](https://gan-even.com/%D7%9E%D7%91%D7%95%D7%90-%D7%9C%D7%A2%D7%99%D7%A6%D7%95%D7%91-%D7%92%D7%99%D7%A0%D7%95%D7%AA-%D7%90%D7%91%D7%A0%D7%99%D7%9D-%D7%A1%D7%95%D7%92%D7%99%D7%9D-%D7%A9%D7%99%D7%9E%D7%95%D7%A9%D7%99%D7%9D/)
- [ריצוף אבני בזלת — Avney Yesod](https://www.avneyesod.com/%D7%A8%D7%99%D7%A6%D7%95%D7%A3-%D7%A2%D7%9D-%D7%90%D7%91%D7%A0%D7%99-%D7%91%D7%96%D7%9C%D7%AA/)
- [גינת פרא: טרנד ריצוף הבזלת כובש את החצרות בארץ — Mako](https://www.mako.co.il/living-garden-and-porch/Article-c5c023ea4f99881026.htm)
- [כמו אבן שואבת: מסלעה בגינה פרטית — Pro.co.il](https://www.pro.co.il/gardners/guide/center-of-attraction-rockery-in-the-private-yard)
- [עיצוב מסלעה בגינה — Midrag](https://www.midrag.co.il/Content/Tip/10712)
- [How to Keep Snakes Away from Your Landscaping Stones — Rock Stone and Pebble](https://rockstoneandpebble.com/how-can-i-deter-snakes-from-the-stones-in-my-landscape/)
- [Deterring unwanted snakes — Minnesota DNR](https://www.dnr.state.mn.us/livingwith_wildlife/snakes/deterring.html)
- [How to Discourage Snakes from Living in Your Yard — University of Illinois Extension](https://extension.illinois.edu/blogs/good-growing/2026-05-29-how-discourage-snakes-living-your-yard)
- [12 Ways to Stop Snakes From Slithering Into Your Yard — Utah State University Extension](https://extension.usu.edu/news_sections/gardening/12-ways-to-stop-snakes-from-slithering-into-yards)

## Routing

Per team_80's own governance contract (advisory, ADR044 Track 4, not part of the gate process): these findings
are delivered to the architecture layer (team_110) for use in future S002 concept-design hardscape work and
`design/CANONICAL/08_LANDSCAPE_PLANTING_PLAN`, and cross-referenced against
`design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md` §6/§7. No gate verdict is issued or required for this artifact.
