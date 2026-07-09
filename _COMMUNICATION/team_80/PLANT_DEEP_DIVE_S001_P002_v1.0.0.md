---
id: PLANT_DEEP_DIVE_S001_P002_v1.0.0
type: team_80 research finding (ADR044 Track 4 — advisory, not part of the gate process)
from: team_80 (Research) under team_110 direction
to: team_110 (Domain Architect) / team_00 (Principal) / team_70 (client-brief owner)
project: sadot
date: 2026-07-10
deepens: SDT-S001-P002-WP001 (climate/soil), SDT-S001-P002-WP002 (plant shortlist)
relates_to: design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md §1, §4, §5, §8
status: DRAFT — general species-level research; still gated on the same open plot-specific data as WP004 (soil lab test, sun/shade/wind survey) — see §5
---

# Plant-selection deep dive — Pardes Hanna residential garden (Niv Sadot)

## 0. Scope + relationship to existing KB (read first)

This memo **adds depth**, it does not restate:

- `knowledge/climate/ISRAELI_CLIMATE_SOIL_PARDES_HANNA.md` — regional Csa climate + hamra/kurkar soil profile (cited here, not reproduced).
- `knowledge/crops/PLANT_SELECTION_STARTER.md` — the existing 13-species general shortlist (olive, pomegranate, fig, citrus, loquat, persimmon, grapevine, carob, bougainvillea, oleander, rosemary, lavender, jacaranda). Where a species below overlaps that list (carob, bougainvillea, oleander, rosemary, lavender, grapevine), this memo only adds the maintenance-tier judgment and any new caveat — full descriptions are not repeated.
- `design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md` — client requirements. §1 (low-maintenance = hard constraint, "irrigation system took over everything" bad-experience story), §4 (banana circle, herb/tea, small organized veg bed), §5 (5 requested fruit trees), §8 (west-neighbor Tasi: tall/2nd-floor screening, climbing plant requested, not wall/fence).

**Non-fabrication discipline:** everything below is species-level horticultural knowledge (how the plant behaves in this climate/soil family in general), not plot-specific fact. It does NOT require the pending soil lab test or sun/shade/wind survey to state — but wherever this plot's actual microclimate (wind exposure, drainage, shade) would change a recommendation, that is flagged explicitly rather than assumed. See §5 for what remains genuinely open.

**Maintenance-tier convention used throughout:** relative to *this* climate (rainless May–Oct, mild wet Nov–Apr) —
- **Water — Low:** negligible irrigation once established (2–3 yr) beyond an occasional deep soak. **Medium:** benefits from periodic deep watering through the dry season to look good/fruit well. **High:** needs regular/frequent irrigation through the full dry season.
- **Pruning — Low:** shape once, then leave alone. **Medium:** annual/biennial shaping or deadwood removal. **High:** frequent structural work, size control, or (bananas) routine hands-on management.

---

## 1. The five client-requested trees — deep dive

### 1.1 Avocado (*Persea americana*, אבוקדו)

| Trait | Finding |
|---|---|
| Mature size (unpruned) | 10–15m tall, canopy nearly as wide; dense evergreen. Commercial/home-garden practice keeps it pruned to 4–6m — **size control requires active, recurring pruning**, not a one-time job. |
| Climate fit | **Good, well-precedented.** Israel's actual commercial avocado belt (coastal plain, Sharon, Western Galilee) is this exact climate zone — Pardes Hanna sits inside it, not at its margin. Mature Israeli-grown cultivars (Hass, Ettinger, Fuerte, Pinkerton) tolerate brief light frost (~ -1 to -2°C); young trees are more sensitive (~0°C). Frost risk at this latitude/elevation is low, consistent with `ISRAELI_CLIMATE_SOIL_PARDES_HANNA.md` §1. |
| Water | **Medium–High** — shallow-rooted, genuinely thirsty relative to olive/carob/fig; wants consistent moisture through the dry summer, not a "plant and forget" species. |
| Disease | **Phytophthora cinnamomi (root rot) is the single biggest risk** — triggered by poor drainage/waterlogging, not drought. This is a real open question until the soil-drainage picture is confirmed (hamra is "moderately well-drained," not free-draining — see §5). Also: persea mite, avocado lace bug, occasional Mediterranean fruit fly on ripening fruit. |
| Wind | Shallow roots + brittle wood + top-heavy canopy → real wind-damage/limb-breakage risk; benefits from a sheltered siting. |
| Pruning/staking | Young trees typically need a stake 1–2 years. Size-control pruning is an ongoing (not one-off) task if kept small. Heavy leaf litter/turnover year-round despite being evergreen. |
| Verdict | **Genuine tension with the low-maintenance hard constraint.** Climate-suitable and low frost risk, but it is the most water- and drainage-demanding of the five, and size control is recurring work, not "plant once." |

### 1.2 Mango (*Mangifera indica*, מנגו)

| Trait | Finding |
|---|---|
| Mature size (unpruned) | 10–20m+ in favorable conditions; Israeli home-garden/orchard practice keeps it 5–8m via pruning. Slower growing than avocado. |
| Climate fit | **More marginal than avocado — flag clearly.** Mango is grown commercially in Israel (Jordan Valley, western Negev, some coastal-plain plantings) but is more frost-sensitive than avocado — young trees can suffer leaf/branch damage near 0°C, severe cold can kill a young tree outright. Separately, mango flower induction wants a pronounced dry/cool period; the coastal plain's humid, wet Mediterranean winter is **less ideal for reliable flowering/fruit-set** than the hotter, drier inland growing regions — this affects fruit reliability, not survivability. Realistic framing: mango will grow and can fruit at Pardes Hanna (it's a common dooryard tree across central Israel), but fruiting is more variable than avocado, and an unusually cold winter is a real risk to a young tree in a way it isn't for avocado. |
| Water | **Low–Medium** — somewhat more drought-tolerant than avocado once established (deeper-rooted), a genuine point in its favor. |
| Disease | **Anthracnose (*Colletotrichum*)** is the standout home-garden problem in Israel's humid coastal air, especially at flowering/fruit-set — causes flower/fruit drop and blemished fruit; humidity-driven, not really preventable by garden care alone. Also mango scale, mealybugs, and Mediterranean fruit fly on fruit. |
| Pruning/staking | Minimal routine pruning needed beyond shape/deadwood/size control (does not need the heavy annual structural work a stone fruit needs) — young grafted trees benefit from staking the first 1–2 years, same as avocado. |
| Verdict | **Doable but the most climate-marginal of the five for reliable fruiting** (not for bare survival). Lower water demand than avocado is a genuine low-maintenance point in its favor. |

### 1.3 Pecan (*Carya illinoinensis*, פקאן)

| Trait | Finding |
|---|---|
| Mature size | **By far the largest of the five, and the outlier on this whole property.** A forest tree by nature — mature specimens commonly reach 20–30m+ with an equally wide canopy; even a modest 30–40-year-old specimen is realistically 15–25m tall/wide. This is multiples larger than avocado/mango/carob and needs to be sited with that end-state in mind, not the nursery-pot size. |
| Root system | Deep taproot when young, but mature laterals spread very widely — **a real caution near hardscape, the planned pool, and buried utilities**, directly relevant given this design's hardscape/pool/deck program. |
| Climate fit | Warm summers suit it fine, but pecan is a historically river-bottomland species — it wants deep, consistently moist, well-drained soil. **It is the least drought-tolerant of the five requested trees and one of the highest water-demand trees in this entire memo** — a direct, structural conflict with the client's #1 stated priority, independent of pest/disease considerations. |
| Pollination | Wind-pollinated with dichogamy (male/female flower timing offset within one tree) — a single tree can still produce, but **two different cultivars are typically recommended for reliable, fuller nut set.** |
| Pruning/safety | Needs early formative pruning for a strong central leader (nut trees are prone to structural weakness if untrained young); **mature specimens are known for dropping large limbs** — an ongoing safety consideration near a house, pool, or seating area, not just an aesthetic one. Messy leaf and husk/shell litter at harvest. |
| Disease | Pecan scab (fungal) is more of a concern in humid regions and could be a moderate risk in humid coastal Israel, but this is secondary to the space/water/structural issues above. |
| Verdict | **Honestly, the poorest fit against the low-maintenance hard constraint of all five requested trees** — highest water demand, largest ultimate footprint (decades-scale, not years), and an ongoing limb-drop safety consideration near planned hardscape. Client asked for it explicitly (not conditionally, unlike carob), so this should be surfaced to the client/design team as a real trade-off decision — e.g., siting it as far as possible from the pool/deck/seating and treating it explicitly as a multi-generational tree, rather than treated as a routine "one more fruit tree" choice. |

### 1.4 Carob (*Ceratonia siliqua*, חרוב) — deepening the existing 1-paragraph KB entry

| Trait | Finding |
|---|---|
| Mature size | 8–12m tall, broad dense rounded canopy often **as wide or wider than tall** (10–15m spread on old specimens) at full maturity — a genuine shade tree, but slow: can take 15–25 years to reach that size. |
| Pollination | **Mostly dioecious** (separate male/female trees) — a fruiting garden specimen needs a female tree (or a hermaphrodite cultivar) plus a male nearby, or a self-fertile named cultivar. Israeli nurseries typically sell grafted, known-female commercial cultivars (e.g. varieties bred from the 'Bnei Darom'-type Israeli carob breeding line) — **worth confirming at point of purchase** if pod production (not just shade/form) matters, since a seedling-grown tree's sex isn't knowable until it flowers years later. |
| Water/soil | **Best low-maintenance fit of all five requested trees.** Some of the best drought tolerance of any Mediterranean tree once established (deep taproot); **actively prefers/tolerates alkaline, rocky, limestone-derived soils** — a strong match to hamra-over-kurkar, better than any of the other four requested trees. |
| Disease/pests | Minimal pest/disease pressure in Israel — occasional scale insects, nothing chronic. |
| Pruning | Minimal beyond early formative shaping; no staking needed beyond nursery establishment. |
| Roots vs. hardscape | Deep, non-aggressive relative to surface hardscape — no notable root-invasiveness concern (contrast with several ornamentals flagged in §4). |
| Caveats | Slow growth = years before it delivers real shade (patience, not effort, is the cost). Mature pods drop and are sticky/messy at harvest — some clients find this a litter nuisance, though given the client's demonstrated compost/permaculture instinct (banana circle) this is arguably a feature, not a bug. |
| Verdict | The client's own "if feasible" hedge on carob is unwarranted — **it fits this climate/soil/maintenance profile better than any of the other four requested trees.** Main real caveat is confirming female/grafted nursery stock if fruiting matters, and managing expectations on how many years until it's a real shade presence. |

### 1.5 Banana (*Musa* spp., בננה)

| Trait | Finding |
|---|---|
| Botanical note | Not a tree — a giant perennial herb (pseudostem of tightly wrapped leaf sheaths, no wood). This changes the maintenance *type*, not just degree, versus the other four. |
| Mature size | Variety-dependent: common Israeli dessert types (Cavendish-group 'Grand Naine', 'Williams') reach 2.5–4m; dwarf Cavendish forms stay 1.5–2.5m and are generally the better residential/wind-exposed choice. |
| Climate fit | **The least cold-hardy of the five requested plants** — leaves damage below ~5°C, the growing point/pseudostem can be killed by frost at or below 0°C (though the underground rhizome often survives light frost and resprouts). There IS a real coastal-plain commercial banana belt in Israel (Sharon/coastal strip, Jordan Valley, Bet She'an, Arava), so growing bananas here is well-precedented — but bananas are also **the single most wind-sensitive plant in this whole memo**: large soft leaves shred badly in wind and strong wind can topple or snap the pseudostem outright. **A banana planting needs a wind-sheltered microclimate — this is squarely a sun/shade/wind-survey question, still pending (see §5).** |
| Water | **High** — shallow-rooted, genuinely thirsty, not drought-tolerant in the way the other four (once established) are. This is the sharpest tension with the low-maintenance hard constraint on paper — **except:** |
| The client's own mitigation is correct | The requested **banana circle** (sunken compost-filled pit ringed by bananas, fed by household greywater) is specifically the standard permaculture answer to exactly this water/nutrient demand — it turns a "waste" stream into the irrigation/fertility source instead of dedicated potable water + fertilizer. **This is worth stating plainly: the client's own proposed technique is the right low-maintenance-compatible solution to banana's high water need**, not an extra complication layered on top of it. |
| Pruning/ongoing care | Needs routine **sucker management** — a banana mat continuously throws new pseudostems from the underground rhizome; standard practice keeps 1 mother + 1–2 follow-on daughters per mat and removes the rest, and each pseudostem is cut down after it fruits once (it doesn't regrow). This is genuinely more frequent hands-on attention than any other of the five trees, but each instance is simple, low-skill, no-ladder work — **"low effort per session, higher frequency," not "occasional big job."** |
| Pests/disease | Banana weevil borer (present but less severe than in wetter tropical regions), Fusarium wilt/Panama disease risk is soil-borne and cultivar-dependent (mainstream Cavendish-type stock sold in Israel is broadly resistant to the historic Race-1 strain; the newer Tropical-Race-4 strain is a serious global concern but is not a mainstream risk in Israeli home-garden banana stock at time of writing — worth a one-line check with the nursery on cultivar disease history, not a high-alarm item). |
| Verdict | High water/attention input in isolation, but the client's own requested banana-circle design is specifically the correct mitigation — the real open item is **siting for wind shelter**, which needs the still-pending site survey, not a plant-selection decision. |

---

## 2. Representative shortlist by garden role

Not exhaustive — genuinely representative coverage of the roles a home garden needs beyond the five requested fruit trees. Each species tagged with maintenance tier (see §3 consolidated table) and, where relevant, a caution.

### (a) Shade tree, distinct from the fruit trees above

| Species | Note |
|---|---|
| **Tabor oak / Palestine oak** — *Quercus ithaburensis* / *Quercus calliprinos* (אלון התבור / אלון מצוי) | Native evergreen oaks, deep-rooted, tolerate alkaline soil well, drought-tolerant once established, non-aggressive roots. Slow-growing — same patience trade-off as carob. Genuinely one of the safest long-term shade-tree choices for this soil/climate/hardscape combination. |
| **Mediterranean hackberry** — *Celtis australis* (מיש דרומי) | Deciduous, tough, well-behaved roots, alkaline-soil tolerant, moderate growth rate (faster payoff than oak), widely used as an Israeli street/garden tree with a good low-maintenance track record. |
| *Caution, not recommended near hardscape* — **ficus (*Ficus microcarpa*/*religiosa*/*benjamina*), Schinus molle (pepper tree)** | Both extremely common in Israeli landscaping and both have well-documented aggressive surface-root systems that heave pavement and invade pipes — see §4. Given this design includes a pool/deck, these are a poor fit here even though they're frequently the default "shade tree" suggestion regionally. |

### (b) Flowering ornamental shrub

| Species | Note |
|---|---|
| **Plumbago** — *Plumbago auriculata* | Long-blooming (pale blue), drought-tolerant once established, minimal pruning, non-invasive — a strong low-maintenance default. |
| **Cape honeysuckle** — *Tecomaria capensis* | Drought/heat-tolerant, long-blooming, can be kept as loose shrub or trained on a support; low-medium water. |
| **Rockrose** — *Cistus × purpureus* | Native-Mediterranean-adjacent, some of the best drought tolerance of any flowering shrub in this climate; caveat — relatively short-lived (~10–15 yrs), so treat as a fill/accent, not a permanent structural planting. |
| *Caution — higher-maintenance than the hard constraint favors* — **roses, Hibiscus rosa-sinensis** | Both are commonly requested "flowering shrub" defaults but both want more water and more routine pest/disease management (aphids, black spot, mildew) than fits a genuine low-maintenance brief — flag if either comes up in client photo references. |

### (c) Ground cover / lawn alternative — **and a genuine question: does he want a lawn at all?**

Given §1 of the client brief is an explicit, repeated, hard low-maintenance constraint with a specific bad-experience story about an irrigation system "taking over everything," **a conventional lawn is arguably the single highest-maintenance, highest-water element the design could include** in this climate — weekly mowing plus irrigation through a 5–6 month rainless summer, ongoing fertilization. Nothing in the client brief as currently synthesized (`design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md`) explicitly requests a lawn. **This is worth a direct question back to the client** (parallel to the other open §9 items already tracked in that document) rather than assumed either way — this memo is not the place to decide it, only to flag that it's a live design fork directly relevant to his stated #1 priority.

| Option | Note |
|---|---|
| **Silver carpet** — *Dymondia margaretae* | Very low-growing, drought-tolerant once established, takes light foot traffic, no mowing — a common genuine "lawn alternative" in Mediterranean-style design. |
| **Creeping myoporum** — *Myoporum parvifolium* | Fast-spreading, evergreen, drought-tolerant, minimal care; common in Israeli xeriscaping. |
| **Gazania** — *Gazania rigens* | Flowering, very drought-tolerant, low maintenance, widely used in Israeli public/private landscaping. |
| *If a true lawn area is still wanted* (e.g., a small kids'-play patch) | Warm-season grasses — **Cynodon dactylon** (Bermuda) or **Zoysia** — are the lower-water/lower-maintenance choice for this climate versus cool-season fescue/ryegrass, but even so remain the highest-maintenance planting choice in the whole palette. Recommend minimizing lawn footprint to only where functionally needed, not decorative fill, if any is kept at all. |

### (d) Hedge/privacy shrubs + climbing/vine screening — directly relevant to the west (Tasi) boundary requirement

The brief is explicit that Tasi's boundary needs **tall, second-floor-height** separation and that a **low ground-level screen or climbing plant alone would not be sufficient** (`CLIENT_BRIEF` §8). That constraint should shape this shortlist directly.

**Hedge/screening shrubs and small trees:**

| Species | Note |
|---|---|
| **Italian cypress** — *Cupressus sempervirens* (ברוש מצוי) | The strongest single candidate for genuine 2nd-floor-height screening: classic Mediterranean columnar form, extremely drought-tolerant once established, tolerates alkaline soil very well, minimal maintenance, can reach 15–20m if grown as a tall column. This is likely the right structural backbone for the Tasi boundary, with a vine (below) as accent/infill rather than the sole screening element. |
| **Myrtle** — *Myrtus communis* (הדס) | Native Mediterranean evergreen shrub, drought-tolerant, alkaline-tolerant, 2–5m — good mid-height layering alongside the cypress. |
| **Weeping bottlebrush** — *Callistemon viminalis* | Evergreen, drought-tolerant, reaches a useful 4–6m, flowering bonus. |
| *Caution* — **Photinia, Ligustrum (privet), Podocarpus** | All commonly recommended hedge defaults elsewhere, but all want noticeably more water than fits this brief's hard constraint — flag as a poor fit here specifically. |

**Climbing/vine species for a trellis or lattice-style screen:**

| Species | Note |
|---|---|
| **Bougainvillea** *(already in `PLANT_SELECTION_STARTER.md`)* | Confirmed strong fit — extremely common, heat/drought-tolerant once established. Note for this specific use: thorny (a walkway-proximity safety note if sited near a path). |
| **Pink trumpet vine** — *Podranea ricasoliana* | Vigorous, drought-tolerant once established, evergreen-ish, fast coverage, fewer thorns than bougainvillea — a strong second option for a lattice/mashrabiya-style trellis screen. |
| **Grapevine** *(already in starter list)* | Deciduous — loses screening density in winter, which matters less for a summer-privacy/shade use case than for a year-round sightline block; dual-purpose edible fit matches the client's stated edible-over-ornamental preference. |
| *Medium-water option, not top-tier drought* — **Star jasmine**, *Trachelospermum jasminoides* | Denser, more fragrant screen than the above, but wants noticeably more water — usable if the client values density/fragrance over minimal irrigation, not a default low-maintenance pick. |
| *Caution — do not run on the house/boundary wall itself* — **Creeping fig**, *Ficus pumila* | Commonly used in Israel for wall coverage, but its holdfast roots damage masonry/stucco and can invade mortar joints — fine on a freestanding trellis, a poor fit if the intent is to grow it directly on a rendered wall surface. |

**Honest design-realism flag:** a vine alone reaching genuine, opaque *second-floor* height screening within a reasonable timeframe is optimistic without a tall support structure (trellis/pergola frame) to climb — the professional read is that the Tasi boundary likely needs the cypress (or comparable tall evergreen) as the actual height-and-opacity solution, with the client's requested "climbing plant, not a wall or fence" serving as the lower-to-mid-height layer and softening/aesthetic element rather than the sole solution. Worth surfacing to the client directly rather than silently substituting.

### (e) Herb/tea plants

Existing KB already covers rosemary and lavender (both confirmed good fits, maintenance-tiered in §3). Adding:

| Species | Note |
|---|---|
| **Za'atar** — *Origanum syriacum* (זעתר) | Regionally native/naturalized Levantine herb, extremely low water once established, minimal care, culturally resonant (za'atar is a staple of Israeli home herb gardens) — arguably the single best-fit herb for this specific brief. |
| **Sage** — *Salvia officinalis* | Mediterranean native, very drought-tolerant, low maintenance, culinary + tea use. |
| **Thyme** — *Thymus vulgaris* | Drought-tolerant, low maintenance; creeping forms double as ground cover (overlaps §2c) — wants very well-drained soil specifically. |
| **Lemongrass** — *Cymbopogon citratus* | Good tea plant, drought-tolerant once established, **clumping (not spreading/invasive)** — dies back in a cold snap but resprouts from the base in a mild winter like Pardes Hanna's. |
| **Lemon verbena** — *Aloysia citrodora* | Popular Israeli tea plant, deciduous in cold, moderate water/moderate maintenance — a genuine tea-purpose pick, not just culinary. |
| *Caution — genuinely risks recreating the client's own overgrowth fear* — **Mint**, *Mentha* spp. | An excellent, very popular tea plant, but notoriously invasive via spreading rhizomes if planted directly in a bed — this is precisely the kind of "took over everything" outcome the client explicitly said he wants to avoid. **Recommend containment (pot, or a buried root barrier) if mint is wanted at all, not open-bed planting.** |
| *Note — wants more water/part shade than the rest of this list* — **Lemon balm**, *Melissa officinalis* | Popular tea herb but can scorch in full, baking summer sun without decent moisture — site in partial shade with the other low-water herbs, or accept it as a medium-water outlier in this bed. |

---

## 3. Consolidated maintenance-tier table

Covers every species named in §1–§2 (KB-existing species included for completeness/screening purposes, not re-described).

| Species | Role | Water | Pruning | Other maintenance note |
|---|---|---|---|---|
| Avocado | Requested fruit tree | Medium–High | High (ongoing size control) | Drainage/root-rot risk; wind shelter helps |
| Mango | Requested fruit tree | Low–Medium | Medium | Humidity-driven anthracnose not preventable by care alone |
| Pecan | Requested fruit tree | **High** | **High** | Largest ultimate footprint of all; limb-drop safety near hardscape |
| Carob | Requested fruit tree | **Low** | Low | Confirm grafted female stock if fruiting wanted; slow to size |
| Banana | Requested (banana circle) | High (mitigated by circle) | High-frequency but low-skill | Wind shelter is the open siting question |
| Olive, Pomegranate, Fig, Carob (dup.), Rosemary, Lavender | *(existing starter list — see that doc)* | Generally Low | Generally Low–Medium | — |
| Citrus | *(existing starter list)* | Medium | Medium | More frost-sensitive than olive/fig per that doc |
| Grapevine | Vine / trellis role (d) | Low–Medium | Medium (annual dormant prune improves fruiting, optional otherwise) | Deciduous — seasonal screening only |
| Bougainvillea | Vine / trellis role (d) | Low | Low–Medium (to control spread) | Thorny — walkway placement note |
| Oleander | Ornamental shrub / hedge | Low | Low | Toxic if ingested — safety note, not climate note |
| Tabor/Palestine oak | Shade tree (a) | Low | Low | Slow-growing |
| Mediterranean hackberry | Shade tree (a) | Low–Medium | Low | Faster payoff than oak |
| Plumbago | Flowering shrub (b) | Low | Low | — |
| Cape honeysuckle | Flowering shrub (b) | Low–Medium | Low–Medium | — |
| Rockrose (Cistus) | Flowering shrub (b) | Low | Low | Short-lived (~10–15 yrs) |
| Roses, Hibiscus | Flowering shrub (b), caution | High | High | Pest/disease-prone — poor fit for hard constraint |
| Dymondia, Myoporum, Gazania | Ground cover (c) | Low | None (no mowing) | — |
| Bermuda/Zoysia turf | Lawn, if wanted (c) | Medium–High | High (mowing) | Highest-maintenance option in whole palette |
| Italian cypress | Hedge/screen (d) | Low | Low | Best tall-screen candidate for Tasi boundary |
| Myrtle | Hedge/screen (d) | Low | Low–Medium | — |
| Weeping bottlebrush | Hedge/screen (d) | Low–Medium | Low | — |
| Photinia, Ligustrum, Podocarpus | Hedge, caution | High | Medium–High | Poor fit vs. hard constraint |
| Podranea (pink trumpet vine) | Vine / screen (d) | Low | Low–Medium | — |
| Star jasmine | Vine / screen (d) | Medium | Low–Medium | Denser/fragrant but thirstier |
| Creeping fig | Vine, caution | Medium | Medium | Damages masonry — trellis only, not house wall |
| Za'atar (*Origanum syriacum*) | Herb/tea (e) | **Low** | Low | Best-fit herb overall |
| Sage | Herb/tea (e) | Low | Low | — |
| Thyme | Herb/tea (e) | Low | Low | Wants very well-drained soil |
| Lemongrass | Herb/tea (e) | Low | Low | Clumping, not invasive |
| Lemon verbena | Herb/tea (e) | Medium | Low–Medium | Deciduous in cold |
| Mint | Herb/tea, caution | Medium | **High (containment)** | Invasive spreading — direct overgrowth-risk parallel |
| Lemon balm | Herb/tea, caution | Medium–High | Low | Wants partial shade here |

---

## 4. Explicit poor-fit flags (commonly recommended elsewhere, wrong for THIS site)

1. **Acid-soil-requiring ornamentals — azalea, rhododendron, camellia; and acid-soil edibles like blueberry (*Vaccinium*).** These typically want pH ~4.5–6. Even the existing KB's own hedge on hamra ("mildly acidic to near-neutral") is nowhere near acidic enough for genuine acid-lovers, and where kurkar (a calcareous/limestone-derived sandstone) is shallow or exposed, local pH tends to trend neutral-to-mildly-alkaline, not acidic. **Do not plant these directly in native soil here** regardless of exactly where this parcel's still-untested soil lands on that spectrum — they would need heavy, ongoing soil amendment or container culture, which itself conflicts with the low-maintenance constraint.
2. **Ficus species used as shade/screen trees (*Ficus microcarpa*, *F. religiosa*, *F. benjamina*) and creeping fig (*F. pumila*) grown on masonry.** Extremely common in Israeli landscaping, but well-documented for aggressive, invasive root systems that heave pavement, invade pipes, and (for the creeping form) damage wall surfaces. A poor fit given this design's planned pool/deck/hardscape.
3. **California pepper tree (*Schinus molle*).** Common, graceful, drought-tolerant — but known for aggressive surface roots that heave pavement; same caution as the ficus family.
4. **Running bamboo (e.g. *Phyllostachys* spp.).** Not requested, but bamboo is one of the most common "fast privacy screen" suggestions a designer or nursery might independently propose for the Tasi boundary. **Flagging preemptively:** running bamboo spreads aggressively via rhizomes and is one of the closest real-world matches to the client's own explicitly-stated fear ("took over everything") — recommend excluding it from consideration entirely rather than requiring a containment system to manage.
5. **Mint (*Mentha* spp.) in open beds.** See §2e/§3 — good tea plant, genuinely invasive habit, direct parallel to the client's stated bad experience; use only in containers or with a buried barrier.
6. **Cool-season turf lawn (fescue/ryegrass) and, to a lesser extent, any large lawn area at all.** See §2c — the highest water + mowing burden in the entire plant palette, in direct tension with the #1 stated priority; worth a direct client question rather than a default inclusion.
7. **Pecan, among the client's own requested trees**, deserves a repeat flag here even though it was explicitly requested (see §1.3 verdict) — it is the one requested species that is structurally hard to reconcile with "low maintenance" (highest water demand of the five, largest ultimate size/root spread, ongoing limb-drop safety consideration near planned hardscape). Not a "wrong plant," but the trade-off should be made explicit to the client rather than absorbed silently into the plant list.

---

## 5. What remains genuinely open (do not treat this memo as resolving these)

- **Soil lab test** — still pending per `SDT-S001-P002-WP004` / `ISRAELI_CLIMATE_SOIL_PARDES_HANNA.md` §4. Nothing above depends on the exact pH number, but final drainage-sensitive placement (avocado especially) and any acid-soil-adjacent decision should be re-checked once it arrives.
- **Sun/shade/wind survey** — still pending, same WP. Two direct dependencies from this memo: (1) **banana siting needs a wind-sheltered spot** — cannot be identified without the wind-exposure picture; (2) the **Tasi (west) boundary screening design** (cypress + vine combination proposed in §2d) should be checked against actual sun exposure on that boundary once available.
- **Which boundary the "climbing plant, not wall/fence" request actually targets** (Tasi/west vs. Pierre/back) is still an open client-confirmation item per `CLIENT_BRIEF` §9 — this memo's §2d assumes the west/Tasi reading already used in that document's §8, consistent with team_00's 2026-07-09 resolution of Tasi=west/tall-2nd-floor, but the specific "climbing plant" line itself is still flagged unconfirmed there.
- **Whether a lawn area is wanted at all** (§2c) is not currently a confirmed client requirement either way — recommend adding it to the same client-confirmation queue as the other open `CLIENT_BRIEF` §9 items, rather than assuming a decision here.

## Routing

Per team_80's governance contract (advisory, ADR044 Track 4, not part of the gate process): delivered to team_110 (architecture layer, for `knowledge/` and downstream S002/S003 spec work) and team_70 (client-brief owner, for the open-items queue in `design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md` §9). No gate verdict is issued or required for this artifact.
