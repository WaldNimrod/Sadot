# Guilds and Planting Strategy

**Status:** methodology (standard permaculture design theory, authored here — see `00_INDEX.md`). Species-level
choices are deferred to `knowledge/crops/` (in progress) and the real site survey — this file defines the
*framework* for guild design, not a final planting list.

## 1. What a guild is

A **guild** is a group of plants (and sometimes animals/fungi) deliberately placed together because their
functions support each other — the assemblage as a whole is more productive, resilient, and self-maintaining than
any one species grown alone. The concept comes from observing how plants cluster and cooperate in mature natural
ecosystems, then deliberately designing analogous multi-species groupings for cultivated ground (Mollison;
Holmgren; popularized further by Dave Jacke & Eric Toensmeier, *Edible Forest Gardens*, 2005).

A guild is not just "plants that grow well next to each other" (companion planting) — it specifically means
plants assigned **functional roles** that together meet the needs of a central "guild member" (often a fruit or
nut tree) that would otherwise need external inputs (fertilizer, pest control, mulch, irrigation labor).

## 2. Functional roles in a guild

| Role | Function | Classic examples |
|---|---|---|
| **Central element** | The plant the guild is built around | Fruit/nut tree, or a key perennial |
| **Nitrogen-fixers** | Fix atmospheric N via root-nodule bacteria (legume family, and some non-legumes e.g. Elaeagnus) into soil-available form | Clover, vetch, beans, lupine, Elaeagnus, Casuarina |
| **Dynamic accumulators / mulch plants** | Deep-rooted plants that draw minerals up from subsoil; cut-and-drop as mulch | Comfrey, yarrow, dandelion |
| **Pest-confusers / pollinator attractors** | Aromatic or flowering plants that disrupt pest-insect targeting by scent, or draw in beneficial/pollinating insects | Alliums (garlic, chives), aromatic herbs (rosemary, lavender, mint family), flowering umbellifers (dill, fennel, yarrow) |
| **Groundcover / living mulch** | Low, spreading plants that shade the soil surface, suppress weeds, retain moisture | Strawberry, clover, nasturtium, sweet potato |
| **Climbers / vertical layer** | Use vertical space without competing for ground footprint | Beans, peas, grape, passionfruit (support-dependent) |
| **Root layer** | Occupies a different soil depth/niche than the central element's roots | Alliums, root vegetables with shallow-to-medium root zones |
| **Barrier/support species (situational)** | Windbreak, trellis-host, or structural support for climbers | Sturdy shrub or small tree used as a living trellis |

### The classic example — apple-tree guild

The most commonly taught guild (Jacke & Toensmeier and others): an apple tree as the central element, underplanted
with **comfrey** (dynamic accumulator, chop-and-drop mulch), **daffodils or alliums** (pest-confusion — bulbs also
deter burrowing rodents from the root zone), **clover or vetch** (nitrogen fixation + living mulch), and
**yarrow/dill/fennel** (attract predatory and pollinating insects). This single example demonstrates every role
in the table above and is a useful mental template even where the actual central tree differs (citrus, stone
fruit, olive — all common in this climate).

## 3. Guild design principles worth carrying into this project

1. **Stack vertically as well as horizontally.** A guild ideally occupies canopy, understory/shrub, herbaceous,
   groundcover, and root layers simultaneously — this is what makes a guild more productive per square meter than
   a monoculture bed, which matters directly on a small residential plot (see `01_ZONES_AND_SECTORS.md` §2 on
   compressed zones).
2. **Every guild member should earn its place with ≥1 function**, not just occupy space decoratively. On a small
   plot this discipline matters more, not less — there's no spare ground for purely ornamental filler once
   productive/functional needs are met, though ornamental value is a legitimate function too (this is a *garden*,
   not a farm plot — the client-facing aesthetic matters as much as yield).
3. **Match guild composition to the central element's actual needs**, not the textbook example verbatim — a
   nitrogen-hungry stone fruit needs different N-fixer density than an olive, which tolerates poor soil and
   actively dislikes excess summer moisture around its base.
4. **Guilds are not static** — they are established with nurse/pioneer species (fast nitrogen-fixers, quick
   groundcover) that may be thinned out or replaced as the central element matures and the guild's needs shift
   from establishment (weed suppression, N-loading) to maintenance (pollinator support, pest confusion).

## 4. Interface contract with `knowledge/crops/`

This file defines **roles**; it does not assign final species. Actual species selection is the job of the
crop/climate knowledge base at `knowledge/crops/` (harvested separately from the SMA sibling domain — as of this
writing, that folder exists but is still being populated; see `_aos/context/PROJECT_CONTEXT.md` "Current focus").
The intended division of labor:

- **This file (`02_GUILDS_AND_PLANTING_STRATEGY.md`)** owns: the guild concept, the functional-role taxonomy above,
  and design principles for composing a guild.
- **`knowledge/crops/`** owns: which specific species are viable for this climate/soil (Israeli Mediterranean,
  Pardes Hanna coastal-plain conditions), their water/light/soil requirements, and harvest data.
- **The join, once both sides are populated:** each `knowledge/crops/` species entry should be tagged with which
  guild role(s) it can serve (central element / N-fixer / dynamic accumulator / pest-confuser / groundcover /
  climber / root layer), so a guild can be assembled by cross-referencing "what's viable here" (crops KB) against
  "what role does this guild still need filled" (this file). Until `knowledge/crops/` is populated with that
  tagging, no specific guild composition for this project's actual plot can be finalized — only the generic
  apple-guild-style template above is available as a placeholder pattern.
- Final guild placement is additionally gated on the sector/zone data in `01_ZONES_AND_SECTORS.md` (sun/wind/water
  determine which central elements are viable where) and the site survey referenced there.
