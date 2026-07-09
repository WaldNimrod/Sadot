# CONCEPT SKETCH REFERENCE — Niv's Hand-Drawn Garden Concept
### Sadot · Landscape Architecture · Team 110 · v1.0.0 · 2026-07-09 · **owns: interpretation of the client's own hand sketch** · status: **WORKING — cross-verified by 2 independent reads, several elements genuinely ambiguous, pending client confirmation**

> This is the single canonical analysis of the client's hand-drawn concept sketch. `design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md`
> (cross-references section) and `design/CANONICAL/02_SPATIAL_SSOT_and_GEOMETRY.md` (Shell & structure section) point here
> rather than re-describing the sketch — do not restate this document's content elsewhere; add a one-line pointer instead.

## 0. Source & method

**Source:** 2 phone photos of the same single hand-drawn sketch (ballpoint pen on graph-paper), sent by Niv:
`raw-materials/from-client/WhatsApp Image 2026-07-06 at 07.15.24.jpeg` and
`WhatsApp Image 2026-07-08 at 12.40.10.jpeg`. Both show the identical drawing from slightly different angles/lighting —
not two different concepts.

**Method:** the second photo (07-08, clearer, less rotated, 1080×1920px) was cropped and upscaled region-by-region
(Python PIL, `Image.MAX_IMAGE_PIXELS = None`, LANCZOS resampling at 4-16×) — the same close-zoom discipline used for
the surveyor's PDF. The first photo (07-06) was viewed directly and is visually consistent with the second wherever
compared; it was not used for detailed cropping because of a macOS file-access-control attribute on that specific file
that blocks shell-level tools (Bash/`cp`/`xattr`) from opening it, even though the Read tool can display it directly —
a local tooling quirk, not a data problem.

**Verification:** every finding below was independently cross-checked by a second, fresh-eyes read of the same photo
(an agent given no prior hypotheses, only the already-confirmed client requirements as background) before being written
up here. Where the two reads agree, confidence is marked accordingly. **Where they genuinely disagree, both readings
are shown — do not treat either as settled.** This sketch is a rough concept doodle, not a scaled or oriented plan —
**no compass direction or real-world scale is asserted anywhere in this document.**

---

## 1. High-confidence findings (match the client's independently-confirmed voice-note requirements)

| Sketch element | Location in sketch | Matches | Confidence |
|---|---|---|---|
| Large curved shape, top of the page, against the house wall, filled with horizontal line-hatching | Top-center, spanning most of the page width | The **confirmed planned dug swimming pool** (`design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md` §4) — hatching reads as water | **High** |
| Two long parallel curved lines filled with oval "pebble" stippling, sweeping from near the pool down through the middle of the garden | Runs diagonally through the whole lower two-thirds of the page | The **confirmed winding pebble/stone path** (§4, §6 kurkar-stone preference) | **High** |

---

## 2. Medium-confidence findings (plausible, not yet client-confirmed)

| Sketch element | Location | Best-guess identification | Confidence | Open question |
|---|---|---|---|---|
| Rectangle filled with a diagonal cross-hatch (lattice/grid) pattern, labeled with a solid heavily-inked mark at its top edge that may be the digit "2" or may just be a doodle | Left side, adjacent to the house wall | A trellis/lattice privacy-screen panel — position (immediately beside the house, on the side opposite the pebble path/pool) is consistent with the west-side screening Tasi requires (§8) | Medium | A height figure is written along its bottom-left inside edge — **two independent reads disagree: "1.30" vs "1.50" vs "1.80" are all plausible readings of the same handwritten digits, genuinely ambiguous.** Needs direct client confirmation, not a guess. |
| Small scalloped "cloud/flower" outlines (distinct in style from the smooth oval pebble-stipple), scattered near the path edges and the two circular features below | Several locations, mostly center and lower-right | Individual plant/shrub markers | Medium | **Deliberately not counted or tallied** — this project has previously fabricated a tree count from ambiguous source material; any plant count must come from the client directly, not from doodle-density inference. |
| Vertical column of overlapping ovals along the right edge of the page, larger/denser than the path's pebble stipple | Right border, running most of the page height | Either a hedge/shrub row along that boundary, or simply a continuation of the path's stone edging | Medium | Which of the two — boundary planting or path edge — is genuinely unclear from the drawing alone. |

---

## 3. Low-confidence / open hypotheses (flagged, not asserted — need direct client confirmation)

Two or three roughly-circular, fully-enclosed shapes appear in the lower half of the sketch, plus one adjacent
organic (non-circular) blob shape between them. **Exactly how many distinct features these represent, and what each
one is, could not be determined with confidence from either read of the photo:**

- **A dense scribbled/tangled circle**, center of the garden area, ringed by several small plant-marker doodles —
  read most plausibly as a **large shrub or tree canopy** (the scribble density suggesting foliage), but one of the
  two independent reads also counted this as one of the "circular enclosed shapes," so it's ambiguous whether it's
  meant as a distinct built feature at all.
- **An organic (non-circular) blob shape** immediately beside/below the tangle above, containing a few short cursive
  marks that are not confidently legible as Hebrew text, a number, or anything specific — read as a **possible
  labeled planting bed**, but the label itself could not be transcribed.
- **A clean circle in the bottom-left corner**, with a small dark rectangle (post or paving block) attached at its
  rim, and faint illegible marks inside — could be a round paved seating area, a fire pit, or a tree/planter; the
  shape is a poor match for the client's stated storage/work-surface need (§2a), which is usually drawn as a
  rectangle, not a circle.
- **A larger circle at mid-right**, part of its rim traced over in darker ink, with a fainter concentric inner
  circle, adjacent to an "A-frame"/crossing-brace mark, a vertical ladder-like tick-mark run, and a small
  vertical-bar panel — the most structurally elaborate of the shapes, and the best candidate for the **"circular
  gathering structure (pergola/gazebo)"** already noted at a high level in `CLIENT_BRIEF_NIV_SADOT_v1.0.0.md`'s
  cross-references section.

**A tempting but unconfirmed reading:** given the client's separately-stated requirement for **two children's own
pergolas (Yinon's and Shani's) with a planted buffer between them** (§2a), it is plausible that 2 of these round
shapes represent the two pergolas and the organic blob between them represents the buffer planting. **This is a
hypothesis, not a finding** — the sketch does not clearly support "exactly 2 similar circular structures" over
"3 different unrelated features" or some other reading, and neither independent read of the photo was confident
enough to assert it. Treat as a question to put to Niv directly (see §6), not as established layout.

---

## 4. Separate mini-sketch at the top of the page (likely unrelated to the garden layout)

Above the main garden square, the same page carries a smaller, differently-styled drawing: three box/module outlines
with width labels reading approximately **"605"**, **"528"**, and a third (read as "549" or "544", ambiguous last
digit), plus three sub-dimension call-outs between paired arrows, reading approximately **"24C"**, then either
**"2×4"** (a lumber/timber dimension) or a cursive Hebrew fragment (genuinely ambiguous), then **"33"**.

This is drawn in an architectural-dimension style (straight rectangles, paired arrow call-outs) completely unlike
the freehand garden sketch below it — both independent reads agree it looks like a **cabinetry/shelving or
framing/lumber detail**, not a plan or elevation of the garden. **Best guess (medium confidence): a rough sketch of
the storage shed/shelving unit mentioned in the voice brief** (`CLIENT_BRIEF_NIV_SADOT_v1.0.0.md` §2a — storage for
hoses/garden equipment + a work surface), possibly with the "2×4" reading indicating its framing lumber. **Not
confirmed** — this could equally be an unrelated household sketch that happened to share the page.

---

## 5. Illegible / unresolved marks (documented for completeness, not interpreted)

- The heavily-inked mark at the top of the lattice panel (§2) — could be the digit "2" over-inked into illegibility,
  or a doodle; genuinely 50/50 between the two independent reads.
- The cursive marks inside the bottom-left circle (§3) and inside the organic blob (§3) — neither read could
  transcribe these with any real confidence; they may be Hebrew shorthand, a plant name, or non-alphabetic scribble.
- A few short diagonal pen strokes near the pool's top-left corner — could be a decorative flourish or an
  unintentional mark; not read as a meaningful arrow or label by either pass.

---

## 6. Open items — route through the existing client-question channel

Per the project's documentation discipline (one list of "things to ask Niv," not several competing ones), the
specific new questions this analysis raises have been **added to the existing draft**,
`_COMMUNICATION/team_70/DRAFT_WHATSAPP_TO_NIV_CLARIFICATIONS_v1.0.0.md` (see that file for the actual question
wording) — covering: the lattice-panel height figure, whether the round shapes represent the two children's
pergolas or something else, and the purpose of the top-of-page mini-sketch. Do not maintain a second open-items list
here; if a new sketch-related question arises later, add it to that file, not this one.

---

## 7. Diagram

`design/CONCEPT_SKETCH_INTERPRETATION_v1.0.0.svg` — a clean, redrawn, color-coded (confidence-tiered) rendering of
this document's §1-§3 findings, laid out to match the sketch's own relative positions. **Topological only — no real
scale or compass orientation is claimed**, exactly matching this document's own caveats.

---

## Cross-references

- `design/CLIENT_BRIEF_NIV_SADOT_v1.0.0.md` — the synthesized voice-note brief this sketch accompanies; §1's
  high-confidence findings and §3's pergola/buffer hypothesis both connect directly to requirements documented there
  (§2a, §4, §8).
- `design/CANONICAL/02_SPATIAL_SSOT_and_GEOMETRY.md` — real, surveyed plot geometry (this sketch carries none of its
  own — it is a concept doodle, not a scaled site plan).
- `_COMMUNICATION/team_70/DRAFT_WHATSAPP_TO_NIV_CLARIFICATIONS_v1.0.0.md` — the live, single list of questions
  awaiting the client's answer, including the ones this analysis raised.

---
*CONCEPT_SKETCH_REFERENCE · v1.0.0 · 2026-07-09 · Team 110. Cross-verified by 2 independent reads of the source photo;
several elements remain genuinely ambiguous by design — see §3/§5. Do not restate this content elsewhere; point here.*
