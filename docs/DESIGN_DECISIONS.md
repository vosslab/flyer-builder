# Design decisions

<!-- VENDORED HEADER: START -->
Record each durable decision about how this code and repository are shaped, once it is settled, with
the reasoning a later reader needs. Guidance Neil Voss states belongs in
[HUMAN_GUIDANCE.md](HUMAN_GUIDANCE.md), dated history in `docs/CHANGELOG.md`, open discussion in
`docs/active_plans/decisions/`. [PROPAGATED HEADER - ENTRIES BELOW ARE YOURS]
<!-- VENDORED HEADER: END -->

Write each decision as a level-three heading with these four fields. `Owner` names the
authoritative code or contract document, rather than a person.

```markdown
### <decision title>

**Decision.** <the durable direction>

**Why.** <the reason it was chosen>

**Consequence.** <the constraint a future change preserves>

**Owner.** <the authoritative code or contract doc>
```

### Coordinate-free flyer YAML

**Decision.** Flyers use nested YAML rows and columns with measured ReportLab flowables.

**Why.** Flyer authors need to express visual groups without maintaining page coordinates.

**Consequence.** The renderer owns geometry and reports single-page overflow instead of clipping.

**Owner.** `flyerlib/render.py` and `docs/USAGE.md`.

### Source-resolution raster embedding

**Decision.** Decode raster inputs with Pillow and embed their original pixel dimensions without
new JPEG PDF image streams.

**Why.** Print fidelity depends on the raster source and its authored display size, while vectors
should remain resolution independent.

**Consequence.** A PNG conversion avoids another lossy JPEG encoding step but cannot recover detail
lost by an earlier JPEG source.

**Owner.** `flyerlib/render.py` and `docs/FILE_FORMATS.md`.

### PDF is the print deliverable

**Decision.** The builder produces only PDF from YAML and local assets. Full-page raster captures
are separate, optional documentation and visual-test artifacts.

**Why.** Flyers are printed directly from PDFs, preserving vector artwork and source raster pixels.

**Consequence.** Preview generation stays outside the production build and print path.

**Owner.** [../build_flyer.py](../build_flyer.py) and [USAGE.md](USAGE.md).

### Fixed printer-safe Letter frame

**Decision.** Every flyer uses a fixed 43.2-point (0.6-inch) margin on all Letter-page edges.
The root column distributes spare height between its top-level items.

**Why.** Consumer printers need a reliable no-ink boundary, while a balanced page uses the
remaining printable height without authored coordinates.

**Consequence.** Other `page.margin` values fail during build; nested rows use real gutter columns
and images cap to their allocated width, while QR blocks must fit their authored columns.

**Owner.** `flyerlib/render.py` and `docs/YAML_FILE_FORMAT.md`.

### GitHub section colors

**Decision.** Repository names share the color of their section divider; category headings stay navy.
Teaching uses green, course materials sky blue, documents purple, molecular/lab teal, academic
publishing navy blue, audio/video magenta, LEGO light orange, and Mac utilities dark orange.

**Why.** Color reinforces grouping instead of adding unrelated variation.

**Consequence.** Use the explicit colors from [COLOR_PALETTE.md](COLOR_PALETTE.md) consistently.

**Owner.** [../flyers/github/github.yaml](../flyers/github/github.yaml).

### Balanced GitHub composition

**Decision.** Give the portrait and title stronger presence beside the large QR, expand the calendar
to the content width, and connect it directly to the two-column category listings. Shorten copy and
remove the redundant project-list title before reducing description type.

**Why.** The supplied visual critique identifies header imbalance, a narrow calendar, and disconnected
sections in the denser design.

**Consequence.** Review the entire printed-page composition alongside content fit; retaining every
project is useful only while hierarchy and readability remain clear.

**Owner.** [../flyers/github/github.yaml](../flyers/github/github.yaml).
