# Crop/Plant Knowledge — Schema Reference

**Status: REFERENCE ONLY.** Sadot is profile **L0** — there is no running application, no
database, and no ORM in this repo. This document describes a **reusable data model**
harvested from the sibling domain `SmallFarmsAgents` (the "ספר גידולים" / crop-book
subsystem of `organic_market_agent`), so that **if/when** Sadot ever needs a structured
plant database (e.g. to back a plant-selection tool or a planting-schedule generator for
the Niv Sadot garden), the shape does not need to be reinvented from scratch.

Nothing in `SmallFarmsAgents` was modified to produce this document — it is a read-only
citation of that repo's schema, reproduced here for Sadot's own use.

## Why this schema fits Sadot without changes

Sadot's garden is dominated by **perennial fruit trees / ornamentals**, not annual market
vegetables — the domain SmallFarmsAgents was built for. The good news: **the schema
already supports this** with no modification required:

- `crops.category` check constraint already includes `'fruit_trees'` (alongside
  `vegetables`, `herbs`, `baby`, `legumes`, `fruits`, `grains`, `cover_crops`).
- `crops.growth_cycle` check constraint already includes `'perennial'` (alongside
  `annual`, `biennial`).
- `crops.first_fruit_year` (Integer, nullable) exists specifically for perennials — years
  to first fruiting, meaningless for annual vegetables, directly relevant for an orchard.
- `crop_varieties.is_grafted` / `rootstock_variety` exist specifically for fruit-tree
  nursery stock (grafted citrus, stone fruit, etc.) — a concept market-vegetable growers
  rarely need but a garden/orchard designer needs constantly.

So a future Sadot plant table can literally be `category='fruit_trees'`,
`growth_cycle='perennial'` rows in the same shape below — no schema fork needed.

## Source provenance (exact file paths, SmallFarmsAgents repo)

All paths relative to `/Users/nimrod/Documents/AOS_V5/SmallFarmsAgents/`:

| File | What it defines |
|---|---|
| `organic_market_agent/crop_book/models.py` | ORM: `CropFamily`, `Crop`, `CropVariety`, `CropVarietySourceValue`, `CropConversionGroup`, `CropUnitConversion` |
| `organic_market_agent/crop_book/planting_calendar.py` | ORM: `CropPlantingCalendar` (table `crop_planting_calendar`) |
| `organic_market_agent/crop_book/companion_matrix.py` | ORM: `CropCompanionMatrix` (table `crop_companion_matrix`) |
| `organic_market_agent/crop_book/cover_crops.py` | ORM: `CropCoverCrop` (table `crop_cover_crops`) |
| `organic_market_agent/db/versions/035_crop_book_families.py` | Migration: creates `crop_families` |
| `organic_market_agent/db/versions/036_crop_book_crops.py` | Migration: creates `crops` (category/growth_cycle/harvest_unit_default check constraints) |
| `organic_market_agent/db/versions/037_crop_book_varieties.py` | Migration: creates `crop_varieties` (original full agronomic-column shape) |
| `organic_market_agent/db/versions/038_crop_book_source_values.py` | Migration: creates `crop_variety_source_values` (per-source raw measurement rows) |
| `organic_market_agent/db/versions/039_crop_book_conversion_groups.py` | Migration: creates `crop_conversion_groups` + deferred FK from `crops` |
| `organic_market_agent/db/versions/040_crop_book_unit_conversions.py` | Migration: creates `crop_unit_conversions` |
| `organic_market_agent/db/versions/049…`, `050…`, `051…` (numbering per in-file docstrings) | Migrations creating `crop_planting_calendar` (049), `crop_cover_crops` (050), `crop_companion_matrix` (051) — table bodies confirmed directly from the ORM files above; migration file bodies not separately re-read for this reference (out of the explicitly requested 035–040 range) |

Note on drift: `crop_varieties` as originally migrated (037, full column list below) is
**not identical** to the current ORM (`CropVariety` in `models.py`), which per its own
docstring was pared down by a later migration (058, WP-CB-MIG, "team_00-authorized") to
identity + seeder-ops columns only — the dropped agronomic facts (days-to-maturity,
spacing, yield, etc.) were moved into the generic `crop_variety_source_values` /
attribute-enrichment system so that every fact carries its own source + trust tier. Both
shapes are documented below since either is a legitimate reference depending on whether
Sadot wants "one row = one flattened fact set" (037 shape) or "one row = identity, facts
sourced separately" (current ORM shape).

## Table: `crop_families`

Botanical family lookup. Purpose: group crops for rotation/companion logic (e.g. don't
plant two Solanaceae in sequence).

| Column | Type | Notes |
|---|---|---|
| `id` | BigInt PK | |
| `scientific_name` | VARCHAR(200), unique, not null | e.g. `Rosaceae` |
| `name_he` | VARCHAR(200), nullable | Hebrew family name |

## Table: `crops`

Core crop/plant entity — one row per species/crop concept (not per variety).

| Column | Type | Notes |
|---|---|---|
| `id` | BigInt PK | |
| `name_he` | VARCHAR(200), unique, not null | Hebrew name — primary display key in source app |
| `name_en` | VARCHAR(200), nullable | |
| `scientific_name` | VARCHAR(200), nullable | |
| `family_id` | FK → `crop_families.id`, not null | |
| `category` | VARCHAR(50), not null, CHECK IN | `'vegetables','herbs','baby','legumes','fruits','fruit_trees','grains','cover_crops'` — **`fruit_trees` already present** |
| `growth_cycle` | VARCHAR(30), nullable, CHECK IN | `'annual','biennial','perennial'` — **`perennial` already present** |
| `harvest_unit_default` | VARCHAR(20), nullable, CHECK IN | `'kg','bunch','head','case','unit','seedling'` |
| `first_fruit_year` | Integer, nullable | Years to first fruiting — perennial/orchard-specific |
| `conversion_group_id` | FK → `crop_conversion_groups.id`, nullable, `ON DELETE SET NULL` | Links crop to a shared unit-conversion group |
| `description` | Text, nullable | |
| `oma_product_id` | VARCHAR(20), nullable | Link back to source app's product catalog — not relevant to Sadot |
| `icon_url` | VARCHAR(255), nullable | Optional illustration; UI falls back to SVG sprite if null |

Indexes: `family_id`, `category`.

## Table: `crop_varieties` (as originally migrated — migration 037)

Variety-level agronomic parameters, one row per cultivar of a crop.

| Column | Type | Notes |
|---|---|---|
| `id` | BigInt PK | |
| `crop_id` | FK → `crops.id`, not null | |
| `name_en` / `name_he` | VARCHAR(200), nullable | |
| `is_default` | Boolean, default false | Flags the "typical" variety for a crop |
| `is_grafted` | Boolean, default false | **Fruit-tree/orchard-relevant** |
| `rootstock_variety` | VARCHAR(200), nullable | **Fruit-tree/orchard-relevant** |
| `planting_method` | VARCHAR(30), nullable, CHECK IN | `'direct_sow','transplant','greenhouse_transplant','cutting','purchase'` — `cutting`/`purchase` map to nursery-stock perennials |
| `days_to_maturity` | Integer, nullable | |
| `harvest_window_min_days` / `_max_days` | Integer, nullable | |
| `in_row_spacing_cm` | Numeric(6,2), nullable | |
| `rows_per_bed` | Integer, nullable | |
| `planting_season` | VARCHAR(100), nullable | |
| `succession_interval_weeks` | Integer, nullable | |
| `harvest_unit` | VARCHAR(20), nullable, CHECK IN | same values as `crops.harvest_unit_default` |
| `avg_yield_per_bed_m` | Numeric(10,4), nullable | |
| `yield_source` | VARCHAR(200), nullable | |
| `documented_price` / `_unit` / `_source` | Numeric/VARCHAR, nullable | Market-price fields — not relevant to a private garden |
| `pricebook_product_id` | VARCHAR(100), nullable | Not relevant to Sadot |
| `avg_revenue_per_bed_m` | Numeric(10,2), nullable | Not relevant to Sadot |
| `days_to_germinate_gh` | Integer, nullable | Later renamed `nursery_days_to_germinate` in the current ORM |
| `days_in_gh_total` | Integer, nullable | |
| `seeder`, `seeder_front_gear`, `seeder_rear_gear`, `seeder_roller_plate` | VARCHAR, nullable | Market-garden seeding-tractor settings — not relevant to Sadot |
| `harvest_stage` | VARCHAR(30), nullable, CHECK IN | `'full_size','baby_leaf','head','plant_sale','seed'` |
| `notes` | Text, nullable | |

Unique constraint: `(crop_id, name_en)`. Indexes: `crop_id`, `(crop_id, is_default)`.

### `crop_varieties` — current ORM shape (post-migration-058 trim)

Per `models.py`, the live ORM keeps only identity + seeder-ops columns
(`is_default`, `is_grafted`, `rootstock_variety`, `nursery_days_to_germinate`, the four
`seeder_*` columns, `harvest_stage`, `seeder_settings`, `notes`) and moves every other
agronomic fact (days-to-maturity, spacing, yield, etc.) out to
`crop_variety_source_values` / a separate attribute-enrichment model
(`enrichment_models.py`, `attribute_models.py` — not read for this reference, out of
requested scope) so that each fact is individually sourced and trust-weighted.

## Table: `crop_variety_source_values`

Per-source raw measurement rows — the mechanism that lets multiple sources disagree
about e.g. "days to maturity" for the same variety without overwriting each other.

| Column | Type | Notes |
|---|---|---|
| `id` | BigInt PK | |
| `variety_id` | FK → `crop_varieties.id`, not null, `ON DELETE CASCADE` | |
| `field_name` | VARCHAR(100), not null | English DB column name this row supplies a value for, e.g. `'days_to_maturity'` |
| `source` | VARCHAR(100), not null | Citation key for where the value came from |
| `value_text` | Text, nullable | |
| `value_numeric` | Numeric(14,6), nullable | |
| `unit` | VARCHAR(50), nullable | |
| `note` | Text, nullable | |
| `trust_tier` | VARCHAR(20), nullable | Added later (migration 042) |
| `confidence_weight` | Numeric(5,4), nullable | Added later (migration 042) |
| `is_outlier_rejected` | Boolean, default false | Added later (migration 042) |

Unique constraint: `(variety_id, field_name, source)` — enables idempotent upserts.
Indexes: `variety_id`, `(variety_id, field_name)`.

## Tables: `crop_conversion_groups` + `crop_unit_conversions`

Unit-conversion infrastructure (e.g. bunches → kg, heads → kg) — pivots every unit
through grams. `crop_unit_conversions` rows attach to **either** a shared
`conversion_group_id` **or** a specific `crop_id` (mutually exclusive, enforced by a
`CHECK` constraint), letting many crops share one conversion table while allowing
per-crop overrides. Likely low-relevance to Sadot (a private garden doesn't sell
produce by weight), but documented for completeness since it's part of the same schema
family.

## Table: `crop_planting_calendar` (source: `planting_calendar.py`)

Monthly planting matrix — one row per `(crop, source, activity_type)` combination, with
one boolean column per month.

| Column | Type | Notes |
|---|---|---|
| `id` | BigInt PK | |
| `crop_id` | FK → `crops.id`, not null, `ON DELETE CASCADE` | |
| `source` | VARCHAR(50), not null | Citation key |
| `trust_tier` | VARCHAR(20), not null | |
| `region` | VARCHAR(40), nullable, free-text | Conventions per source docstring: `IL_general` (default Israel), `IL_north`/`IL_center`/`IL_south` (zone overlays), `MED_general` (Mediterranean reference) — **the `MED_general` / `IL_center` conventions map directly onto Pardes Hanna's Csa climate** |
| `activity_type` | VARCHAR(20), not null, CHECK IN | `'seed','transplant','both'` |
| `season` | VARCHAR(20), nullable, CHECK IN | `'spring','summer','fall','winter','all'` |
| `month_jan` … `month_dec` | Boolean, default false | 12 columns, one per calendar month |
| `notes` | Text, nullable | |

Unique constraint: `(crop_id, source, activity_type)`.

## Table: `crop_cover_crops` (source: `cover_crops.py`)

Standalone reference chart for cover crops (green manures) — separate from the
market-vegetable `crops` table (no FK to `crops`).

| Column | Type | Notes |
|---|---|---|
| `id` | BigInt PK | |
| `name_en` / `name_he` | VARCHAR(60) | |
| `category` | VARCHAR(40), not null, CHECK IN | `'legume','cereal','brassica','other'` |
| `source` | VARCHAR(50), not null | |
| `trust_tier` | VARCHAR(20), not null | |
| `total_days_garden` | Integer, nullable | |
| `germination_temp_c_min` | Numeric(4,1), nullable | |
| `hardiness_zone` | Integer, nullable | USDA zone |
| `sow_window` | Text, nullable | |
| `inoculum` | VARCHAR(80), nullable | Rhizobium inoculant type, for legume cover crops |
| `survives_winter` | Boolean, nullable | |
| `notes` | Text, nullable | |

Unique constraint: `(name_en, source)`.

## Table: `crop_companion_matrix` (source: `companion_matrix.py`)

Companion-planting pairwise relationships — directly useful for Sadot's garden-bed
layout logic (which perennials/ornamentals can share a planting zone).

| Column | Type | Notes |
|---|---|---|
| `id` | BigInt PK | |
| `crop_a_id` / `crop_b_id` | FK → `crops.id`, not null, `ON DELETE CASCADE` | `CHECK (crop_a_id != crop_b_id)` |
| `compatibility` | VARCHAR(20), not null, CHECK IN | `'beneficial','neutral','antagonistic'` |
| `source` | VARCHAR(50), not null | |
| `trust_tier` | VARCHAR(20), not null | |
| `evidence_strength` | VARCHAR(20), nullable, values `'strong','weak','anecdotal'` | |
| `notes` | Text, nullable | |

Unique constraint: `(crop_a_id, crop_b_id, source)`.

## Shared conventions across all crop-book tables

- **`source`** — every fact-bearing table carries its own citation key, never a single
  global "source of truth" — multiple disagreeing sources coexist by design.
- **`trust_tier`** — a source-quality ranking (see `sources/INDEX.md` in this directory
  for the SmallFarmsAgents source hierarchy this ranking is drawn from).
- **Free-text `region`/`notes` columns** are deliberately unconstrained (per the
  `planting_calendar.py` docstring) rather than enum-locked, so regional nuance can be
  added without a migration.
