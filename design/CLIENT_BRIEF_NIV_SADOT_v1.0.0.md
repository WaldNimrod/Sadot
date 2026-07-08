---
id: CLIENT_BRIEF_NIV_SADOT
version: 1.2.0
status: DRAFT — synthesized from client voice notes via automated (Whisper/Hebrew) transcription; Yinon/Shani identity + deck location confirmed by team_00 2026-07-09; remaining items in §9 still need direct client confirmation
date: 2026-07-08 (updated 2026-07-09)
owns: client requirements input to 01_DECISION_REGISTER + 08_LANDSCAPE_PLANTING_PLAN
---

# Client Brief — Niv Sadot (Pardes Hanna)

**Source:** 4 WhatsApp voice notes received 2026-07-06 and 2026-07-08 (`raw-materials/from-client/`), transcribed
locally (Whisper, Hebrew, `small` model — imperfect ASR, gist-level accuracy). Raw transcripts kept in
`raw-materials/working/transcripts/` (git-ignored). **This document is the curated synthesis — verify against the
original audio before treating any single requirement as final,** especially names/directions which are the parts
most likely to be ASR errors.

## 1. Top priority: low maintenance

Stated explicitly and repeatedly, in both the 07-06 and 07-08 recordings: the garden must be **easy and simple to
maintain**. Client referenced a past bad experience where an irrigation/sprinkler system became overgrown and took
over ("took control of everything") and he doesn't want to repeat it. This should be treated as a hard constraint
on plant density, lawn area, and irrigation complexity — not just a preference.

## 2. View & sightlines

- Do NOT block the view line from upstairs / the upper porch, or from **Yinon's window** (one of Niv's children —
  name confirmed by team_00 2026-07-09; ASR originally rendered this as "עינון"). No tall trees/dense vegetation
  directly in that sightline.
- A planned storage/work-surface area should NOT block the view from that same window.

## 2a. Storage + work surface + pergola privacy/light balance (recording 14:25:23 — previously omitted, added on audit)

**Correction (2026-07-09):** this section is about Niv's OWN family — his children **Yinon and Shani**, each with
their own room + pergola at the back of the house — NOT a neighbor. Keep this separate from §8 (actual neighbor
privacy, different names/directions).

- Wants help with some kind of storage shed/area — to store hoses and similar garden equipment — plus a work
  surface area.
- That work surface should NOT block the view from **Yinon's window**.
- Separately, wants a **planted buffer between his own pergola and the children's pergolas (Yinon's and Shani's)**
  using vegetation, not a solid structure — explicitly wants PARTIAL privacy: block enough for privacy on one side,
  but do NOT fully block light/view on the other side. Client specifically notes the pergola in question has only
  one window, and enough light should still reach it.
- IFC re-investigation (`HOUSE_IFC_REFERENCE.md` §2) found a plausible candidate pair of entrance-floor windows
  (tags 5834063 + 5795233) flanking what looks like a shared bathroom — consistent with two children's bedrooms —
  but this is unconfirmed, not the "יח' הורים" (parents' unit) wing originally guessed.

## 3. Level continuity for gatherings

Wants the yard's lower level near the entrance to connect **homogeneously** (same level, no awkward step) with the
outdoor terrace, so that opening the garage/car door creates one shared space usable for social gatherings.

## 4. Desired features

- Small, organized, planned **vegetable bed** ("ערוגה קטנה מסודרת ומתוכננת לירקות")
- **Fish pond**
- A planted/water feature pond (ASR: "ברכה צמחייה" — verify exact meaning, possibly a bog/planted pond)
- **Banana circle** (a permaculture greywater/compost technique — ties directly into `knowledge/permaculture/`)
- Possibly a water feature that rises/cascades to an upper level (ASR uncertain — verify)
- Storage shed/structure for garden tools
- Herb + tea plants

## 5. Preferred plants (client's own list, to send reference photos separately)

Fruit trees: **avocado, mango, pecan, and carob if feasible** (clearly legible in the transcript). Bananas. Plus
one more fruit tree the client named that the ASR rendered as "נוראים גליים" — **not a recognizable Hebrew word for
any fruit; do NOT treat this as "guava" (גויאבה) or any other specific species without listening to the original
audio directly.** Flagged in §9, not assumed. General preference for edible/useful species over purely ornamental
ones — consistent with the permaculture-guild approach in `knowledge/permaculture/02_GUILDS_AND_PLANTING_STRATEGY.md`.

## 6. Materials / hardscape preference

**Dislikes** the large white rounded decorative "moon rock" boulders common in Israeli landscaping. Prefers
**kurkar** stone (matches the region's native geology — see `knowledge/climate/ISRAELI_CLIMATE_SOIL_PARDES_HANNA.md`
§2) and possibly basalt, mixed to create varied terrain ("play of heights, play of zones") rather than a flat
uniform surface.

## 7. Safety consideration

Wants the design to avoid creating excessive hiding spots for snakes and similar wildlife — a practical constraint
on dense ground-cover/rock-pile placement near walkways and seating areas.

## 8. Privacy / neighbor boundary

**Names + directions confirmed by team_00 (2026-07-09):**
- **טאסי (Tasi)** — neighbor to the **west**, immediately adjacent house.
- **פייר (Pierre)** — neighbor at the **back**.
- The original transcript mentions both names together in the same breath ("מכיוון פייר טאסי") for the
  climbing-plant/no-wall-no-fence request — read as: that request applies to the shared boundary area near
  Tasi (west) and/or Pierre (back), most likely the closer west-adjacent house (Tasi) given "not a wall or fence"
  reads as a close-proximity ask. **Still worth a direct confirmation of which boundary this specifically targets.**
- **"עדאס" (Adas) — still UNCONFIRMED, a third/separate name, not resolved by the Tasi/Pierre clarification.**
  This is the one associated with the tree/bedroom-window-screening request below. Do not assume it equals
  Tasi or Pierre without asking.

- Climbing-plant request (Tasi/Pierre direction — see above): wants a **climbing plant**, not a wall or fence, to
  create separation from the neighbor.
- Adas direction (still unconfirmed): wants a **tree** positioned to screen a neighbor's bedroom window and
  improve privacy — client explicit that this should be a real screening tree, not just planting for its own sake.
- Existing gate + fence gap on the east side (per the client's own earlier sketch annotation) — wants easy access
  maintained toward the east side.
- Cross-reference: once the IFC-vs-ITM coordinate reconciliation (`HOUSE_IFC_REFERENCE.md` §0.1) resolves, these
  neighbor directions (west/back/east) can be tied to the real surveyed boundary edges in
  `blender/data/site/SITE_GEO.yaml` (6 boundary points, bearings already computed).

## 9. Open items requiring direct client confirmation before S002 (concept design) proceeds

- [ ] "ברכה צמחייה" — confirm intended meaning (§4)
- [ ] The rising water-feature mention (§4) — confirm this is a real request, not an ASR artifact
- [ ] The 5th fruit tree in §5 (ASR: "נוראים גליים") — **listen to the original recording directly**; do not guess a
      species name from the transcript alone
- [ ] "עדאס" (Adas) in §8 — still unconfirmed (Tasi=west, Pierre=back are now resolved, but Adas is a separate
      name/direction, associated with the bedroom-window screening-tree request)
- [ ] Confirm which boundary (Tasi/west vs. Pierre/back) the climbing-plant/no-fence request in §8 specifically
      targets — transcript mentions both names together
- [ ] Reference photos for preferred plants (client said he would send separately — check `raw-materials/from-client/`
      for updates)
- [x] **RESOLVED by team_00 (2026-07-09):** "עינון"/"שני" = **Yinon and Shani, the children** — each has their own
      room + pergola + one window, at the back of the house. IFC re-investigation found a plausible but unproven
      candidate pair (entrance-floor windows, tags 5834063 + 5795233, flanking what looks like a shared bath) —
      see `HOUSE_IFC_REFERENCE.md` §2. Still needs client confirmation before treating as final.
- [x] **RESOLVED by team_00 (2026-07-09):** Tasi (west, adjacent house) and Pierre (back) — see §8.
- [x] **RESOLVED by team_00 (2026-07-09):** the real deck is at the front, extends from the kitchen, round-ended
      toward the garden — NOT the "מרפסת" IFC element (confirmed ruled out: no curves, ~90m+ offset is real, not
      a bug). IFC re-investigation found a strong candidate instead: `IfcSlab #51836`, unnamed, with a genuine
      multi-arc round edge, adjacent to a gas hob and a 4.2m glass door — see `HOUSE_IFC_REFERENCE.md` §4. High
      confidence, not yet visually confirmed against the architect's 2D plan.

## 10. Audit note (2026-07-08)

This document was independently cross-checked against the raw transcripts after initial drafting. Two corrections
were made: (1) an unverified plant identification ("guava") was removed and re-flagged as uncertain — §5; (2) a
distinct requirement from recording `14.25.23` (storage/work-surface + pergola privacy-vs-light balance) that was
missing from the first draft was added — §2a. Treat this as a live document, not a one-shot final brief.

## Cross-references

- Hand-sketched concept diagrams (2 versions, `raw-materials/from-client/WhatsApp Image 2026-07-0{6,8}*.jpeg`) show
  a curved pool/water feature, a winding pebble path, a circular gathering structure (pergola/gazebo), and a
  lattice/planter feature — broadly consistent with §4 above. Digitize into `design/CANONICAL/02_SPATIAL_SSOT_and_GEOMETRY.md`
  once S002 concept work formally starts.
- Plot boundary, elevation range, orientation, and existing 13-tree inventory: `blender/data/site/SITE_GEO.yaml`,
  `design/CANONICAL/02_SPATIAL_SSOT_and_GEOMETRY.md`.
- Architectural house model (IFC, Revit-exported): `raw-materials/from-client/NSB02.ifc` — basis for the S003 3D
  build.
