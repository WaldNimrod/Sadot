# Plant Selection — Starter Shortlist (Climate-Fit Only)

## ⚠ Scope disclaimer — read before using this list

This is a **general climate-fit shortlist**, not a plot-specific planting plan.

- **No site survey exists yet** for the Niv Sadot property (soil test, drainage, sun/shade
  map, existing structures, irrigation infrastructure, microclimate pockets, neighbor
  shading, wind exposure) — all of that is **design-team work**, not this document's job.
- Every species below is included **only** because it generally suits the **regional
  climate** — Israeli coastal plain, Pardes Hanna area, Köppen **Csa** (hot-summer
  Mediterranean: mild wet winters, hot dry summers, effectively frost-free or near-frost-free).
- Final species selection, quantities, and placement must come from the actual site
  design process (`design/` dossier) — this list is an input to that process, not a
  substitute for it.
- "Maps to" citations below are **conceptual** — they say which part of the harvested
  crop-book schema/sources (see `SCHEMA_REFERENCE.md` and `sources/INDEX.md` in this
  directory) a future structured lookup for that species would use. They are not
  claims that the species is already a populated row in any database — Sadot has no
  database.

## The shortlist (13 species)

### 1. Olive — Olea europaea (זית)
Mediterranean-native evergreen fruit/ornamental tree; extremely drought-tolerant once
established, thrives in the region's hot dry summer and mild winter, minimal frost risk
at coastal-plain elevations. Long-lived, low-maintenance backbone tree for a Mediterranean
garden design.
- **Maps to:** would query crop_book with `category='fruit_trees'`, `growth_cycle='perennial'`;
  frost/cold-resistance + region fit would be cross-referenced against the L02 variety
  encyclopedia concept (`sources/INDEX.md`).

### 2. Pomegranate — Punica granatum (רימון)
Deciduous fruit shrub/small tree, well-adapted to the region's summer heat and winter
chill hours; ornamental value from flower + fruit display. Common in Israeli home
gardens region-wide.
- **Maps to:** `category='fruit_trees'`, `growth_cycle='perennial'`; `first_fruit_year`
  field relevant (young pomegranates fruit within a few years).

### 3. Fig — Ficus carica (תאנה)
Deciduous fruit tree, deep native-Mediterranean fit, very drought-tolerant, tolerates
poor soils. Classic Israeli garden/orchard tree.
- **Maps to:** `category='fruit_trees'`, `growth_cycle='perennial'`; `crop_planting_calendar`
  concept with `region='IL_center'` or `'MED_general'` for seasonal care timing.

### 4. Citrus (lemon / orange) — Citrus limon / Citrus sinensis (לימון / תפוז)
Evergreen fruit trees, a coastal-plain staple — the region's mild winters and irrigation
availability suit citrus well, though citrus is more frost-sensitive than olive/fig/
pomegranate (a genuine constraint, hence still "generally suited," not risk-free).
- **Maps to:** `category='fruit_trees'`, `growth_cycle='perennial'`, `is_grafted='true'`
  + `rootstock_variety` (citrus nursery stock is almost always grafted) — this is exactly
  the fruit-tree-specific column pair the schema already carries.

### 5. Loquat — Eriobotrya japonica (שסק)
Evergreen fruit tree, common in Israeli gardens, tolerant of the coastal-plain climate,
attractive broad-leaf form doubles as a shade/ornamental tree.
- **Maps to:** `category='fruit_trees'`, `growth_cycle='perennial'`.

### 6. Persimmon — Diospyros kaki (אפרסמון)
Deciduous fruit tree with strong regional commercial + garden presence in Israel;
handles the coastal plain's winter chill and summer heat, showy autumn fruit/foliage.
- **Maps to:** `category='fruit_trees'`, `growth_cycle='perennial'`.

### 7. Grapevine — Vitis vinifera (גפן)
Deciduous fruiting vine, deeply Mediterranean-adapted, useful for pergola/shade-structure
integration in a garden design (dual function: fruit + built-structure shading).
- **Maps to:** `category='fruits'` or `fruit_trees'` depending on schema convention
  chosen, `growth_cycle='perennial'`; companion-planting concept
  (`crop_companion_matrix`) relevant if placed near vegetable/herb beds.

### 8. Carob — Ceratonia siliqua (חרוב)
Native Mediterranean evergreen tree, exceptionally drought-tolerant, low water need
once established — a strong xeriscape/low-irrigation anchor tree option.
- **Maps to:** `category='fruit_trees'`, `growth_cycle='perennial'`; cover-crop/soil
  concept not applicable, but the L02 encyclopedia's `עמידות` (resistance) + `אזורים
  בארץ` (regions in Israel) fields are exactly the ones a carob lookup would want.

### 9. Bougainvillea — Bougainvillea spp. (בוגונוויליה)
Evergreen/semi-evergreen flowering vine/shrub, extremely common ornamental in Israeli
coastal gardens, thrives on heat and tolerates drought once established — classic
climbing-wall or pergola-cover choice.
- **Maps to:** `category` would need an ornamental category not currently in the
  crop_book enum (`vegetables/herbs/baby/legumes/fruits/fruit_trees/grains/cover_crops`)
  — flagged here as a gap: the harvested schema is vegetable/orchard-oriented and does
  not have a pure-ornamental category. This is a candidate for the domain-rules /
  governance-change conversation about extending or forking the category enum for
  Sadot's ornamental-garden use case, rather than something to solve in this document.

### 10. Oleander — Nerium oleander (הרדוף)
Evergreen flowering shrub, extremely drought- and heat-tolerant, ubiquitous in Israeli
public and private landscaping (note: toxic if ingested — a design/safety consideration,
not a climate-fit one).
- **Maps to:** same ornamental-category gap as Bougainvillea above.

### 11. Rosemary — Rosmarinus officinalis (רוזמרין)
Evergreen Mediterranean-native herb/shrub, doubles as ground cover, low hedge, or
culinary herb bed; thrives in the region's dry summer with minimal irrigation.
- **Maps to:** `category='herbs'`, `growth_cycle='perennial'` — this one fits the
  existing enum cleanly since `herbs` is already a category.

### 12. Lavender — Lavandula spp. (לבנדר)
Evergreen Mediterranean-native flowering herb/shrub, similar climate profile to
rosemary; ornamental + pollinator-attracting value.
- **Maps to:** `category='herbs'`, `growth_cycle='perennial'`; companion-planting
  concept (`crop_companion_matrix`) relevant as a pollinator-attractant near fruiting
  trees.

### 13. Jacaranda — Jacaranda mimosifolia (ג'קרנדה)
Deciduous flowering shade tree, widely planted as an ornamental street/garden tree
across Israel's coastal plain; strong seasonal (spring) purple-bloom display value for
a garden-design centerpiece.
- **Maps to:** same ornamental-category gap as Bougainvillea/Oleander above — a pure
  shade/ornamental tree, not a fruit tree, so it falls outside every current crop_book
  category.

## Observation for the domain-rules conversation

Items 9, 10, and 13 above expose the same gap: the harvested crop_book schema's
`category` enum (`vegetables, herbs, baby, legumes, fruits, fruit_trees, grains,
cover_crops`) has **no pure-ornamental bucket** — everything in it assumes an edible or
soil-amendment purpose. Sadot's garden-design domain will want ornamentals
(flowering shrubs, shade trees, vines chosen for bloom/form rather than yield) as a
first-class category, not a workaround. This is worth raising as part of the
domain-rules canon proposal (see `_COMMUNICATION/team_100/` GCR queue) rather than
silently forking the enum in this reference document.
