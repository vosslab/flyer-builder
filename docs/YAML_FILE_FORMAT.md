# YAML file format

Each flyer is one YAML file beneath [flyers/](../flyers/). The renderer resolves every asset path
relative to that file. Authors describe visual groups with rows and columns; they never supply page
coordinates.

## Document shape

The top level requires `layout`. `title` is accepted as flyer metadata but is not written into the
PDF. `page.margin` is optional only for brevity: the renderer always uses a 43.2-point (0.6-inch)
margin on every Letter-page edge and rejects any other value.

```yaml
title: Example
page: {margin: 43.2}
styles:
  title: {size: 42, leading: 44, bold: true, color: "#142535"}
layout:
  col:
    gap: 12
    items:
      - text: {value: "A coordinate-free flyer", style: title}
      - rule: {color: "#00775F"}
```

## Containers

`col` stacks its `items` from top to bottom. `row` places its `items` from left to right. Both
accept `gap` in points and require a non-empty `items` list.

Each item in a row may use this wrapper:

```yaml
- weight: 3
  block: {text: {value: "Wide column"}}
```

Weights divide the remaining width after real gutter columns. Omit a weight for `1`. A row also
accepts `valign` with ReportLab values such as `TOP`, `MIDDLE`, or `BOTTOM`. Use nesting to make
groups; `row` and `col` do not accept `x`, `y`, widths, or heights. The root `col` distributes
unused vertical space between its top-level items, keeping the first and last content at the
printer-safe bounds.

## Content blocks

Every content item is a mapping with exactly one block type.

| Block | Required fields | Optional fields |
| --- | --- | --- |
| `text` | `value` | `style`, `size`, `leading`, `color`, `align`, `bold`, `url` |
| `image` | `path`, `height` | none |
| `qr` | `url` | `size`, `color`, `icon`, `label` |
| `rule` | none | `color`, `thickness` |
| `row` | `items` | `gap`, `valign` |
| `col` | `items` | `gap` |

`image.path` and `qr.icon` name local files relative to the YAML file. Images preserve their natural
aspect ratio and use the authored height in points, capped to the available column width without
raster resampling. SVG images remain vector artwork in the PDF.

QR codes use high error correction, a four-module quiet zone, and a deterministic mask. `size`
defaults to 76 points. An icon is centered on a white patch; use it only when rendered scanning has
been checked. A `label` appears below the QR code.

Text style names refer to entries in `styles`. A style may set `size`, `leading`, `bold`, `color`,
and `align`; text blocks can override each property. Text uses `Atkinson` or `Atkinson-Bold` from
[assets/fonts/](../assets/fonts/). Newlines in `value` become line breaks. Text becomes ReportLab
paragraph markup, so escape literal markup-sensitive characters such as `&` as `&amp;`.

## Build and fit

Build a source file with [build_flyer.py](../build_flyer.py):

```bash
source source_me.sh && python3 build_flyer.py -i flyers/github/github.yaml
```

The default output is `output/pdf/<yaml-stem>.pdf`. Missing assets, unknown styles, empty containers,
and malformed block mappings stop the build. The build writes to a temporary PDF before replacing an
existing result.

The renderer measures wrapped text and rejects a layout that exceeds one Letter page. Check the
emitted PDF page count after changing copy, artwork, sizes, or gaps.

## Authoring limits

- Use only the listed block types and documented fields. The current parser does not reject every
  unknown inner field, so spelling mistakes can be ignored silently.
- Keep graphic dimensions and gaps proportional to their row. Images cap to their available width;
  QR codes must fit their authored column width and fail clearly when they do not.
- Inspect final PDFs at print scale. A successful build alone does not establish readable text,
  unclipped artwork, or scannable QR codes.
