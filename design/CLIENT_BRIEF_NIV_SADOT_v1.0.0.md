---
id: CLIENT_BRIEF_NIV_SADOT
version: 1.0.0
status: DRAFT — synthesized from client voice notes via automated (Whisper/Hebrew) transcription; NOT yet reviewed/confirmed by Niv Sadot or team_00
date: 2026-07-08
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

- Do NOT block the view line from upstairs / the upper porch, or from a specific window (referenced by name in the
  recording — verify with client which room). No tall trees/dense vegetation directly in that sightline.
- A planned storage/work-surface area should NOT block the view from that same window.

## 2a. Storage + work surface + pergola privacy/light balance (recording 14:25:23 — previously omitted, added on audit)

- Wants help with some kind of storage shed/area — to store hoses and similar garden equipment — plus a work
  surface area.
- That work surface should NOT block the view from the window referenced as "עינון's" (same name as in §2 — verify
  spelling/identity with the client).
- Separately, wants a **planted buffer between two pergolas** (referenced as "עינון's pergola" and "שני's pergola" —
  both names need verification) using vegetation, not a solid structure — explicitly wants PARTIAL privacy: block
  enough for privacy on one side, but do NOT fully block light/view on the other side. Client specifically notes the
  pergola in question has only one window, and enough light should still reach it.
- This is additional detail on top of the general privacy/screening requirements in §8 — keep both in view together
  since they may refer to the same or adjacent boundary.

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

- One direction (ASR: near a name that sounds like "פייר טאסי" — verify): wants a **climbing plant**, not a wall or
  fence, to create separation from the neighbor.
- Another direction (ASR: near a name that sounds like "עדאס" — verify): wants a **tree** positioned to screen a
  neighbor's bedroom window and improve privacy — client explicit that this should be a real screening tree, not
  just planting for its own sake.
- Existing gate + fence gap on the east side (per the client's own earlier sketch annotation) — wants easy access
  maintained toward the east side.

## 9. Open items requiring direct client confirmation before S002 (concept design) proceeds

- [ ] Exact names/rooms referenced for the view-blocking constraint (§2) and the pergola-privacy passage (§2a) —
      "עינון" and "שני" need spelling/identity confirmation, and whether they're the same people/rooms referenced twice
- [ ] "ברכה צמחייה" — confirm intended meaning (§4)
- [ ] The rising water-feature mention (§4) — confirm this is a real request, not an ASR artifact
- [ ] The 5th fruit tree in §5 (ASR: "נוראים גליים") — **listen to the original recording directly**; do not guess a
      species name from the transcript alone
- [ ] Neighbor-direction names in §8 — confirm spelling/identity so the privacy-screening plan targets the right
      boundary lines
- [ ] Reference photos for preferred plants (client said he would send separately — check `raw-materials/from-client/`
      for updates)
- [ ] Cross-reference against the IFC house model (`design/CANONICAL/HOUSE_IFC_REFERENCE.md`): the "יח' הורים"
      (parents' unit) wing has 6 windows including the largest in the house — likely the window referenced in §2/§2a,
      needs client confirmation
- [ ] The "מרפסת" (deck/terrace) element found in the IFC model sits ~90m+ from the rest of the house geometrically
      — almost certainly a stale/orphaned Revit tag, not the real deck. Needs the client (or architect) to confirm
      where the actual exterior deck is before any level-continuity design proceeds

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
