# Code architecture

## Overview

This repository compiles a coordinate-free YAML flyer into a one-page US Letter PDF. Authors
describe nested rows, columns, content blocks, styles, and local artwork; the renderer derives
positions while measuring the content.

## Major components

- [../build_flyer.py](../build_flyer.py) is the CLI entry point. It parses input and optional output
  paths, then calls the renderer.
- [../flyerlib/render.py](../flyerlib/render.py) parses YAML, registers bundled fonts, compiles
  blocks into ReportLab flowables, and writes the PDF only after a successful build.
- [../flyers/](../flyers/) holds canonical editable flyer sources and their local artwork.
- [../assets/fonts/](../assets/fonts/) supplies the bundled Atkinson Hyperlegible Next faces used by
  all rendered text.
- [../tests/test_flyer_render.py](../tests/test_flyer_render.py) protects the printable StVC example,
  its one-page constraint, and selected PDF link destinations.

The renderer uses PyYAML for source input, ReportLab for layout and PDF output, `qrcode` for vector
QR modules, and `svglib` for SVG artwork. These packages are declared in
[../pip_requirements.txt](../pip_requirements.txt).

## Data flow

```text
flyers/<name>/<name>.yaml + flyers/<name>/assets/
  -> build_flyer.py
  -> flyerlib.render.build()
  -> ReportLab flowables and vector QR/SVG drawing
  -> output/pdf/<name>.pdf
```

`row` containers allocate width by declared weights. `col` containers arrange measured children in
order. Text uses ReportLab paragraphs, local images retain their aspect ratio, and QR blocks add
clickable PDF links. A ReportLab layout failure raises `FlyerError` and leaves an existing output PDF
in place.

## Testing and verification

- Run the focused contract check with `source source_me.sh && python3 -m pytest
  tests/test_flyer_render.py -q`.
- Run the repository suite with `source source_me.sh && python3 -m pytest tests/`.
- Render PDFs with Poppler during visual review; output directories are ignored by Git.

## Extension points

- Add a flyer under [../flyers/](../flyers/) with one YAML source and a local `assets/` directory.
- Add renderer behavior in [../flyerlib/render.py](../flyerlib/render.py) only when it is shared by
  more than one flyer.
- Add durable behavior tests in [../tests/](../tests/); use `tests/_temp/` for one-time work.

## Known gaps

- Verify physical printer and phone-scanning performance for each flyer before distribution.
- Decide whether authored unknown YAML fields should become validation errors.
- Check an oversized image against its allocated row width before adding automatic image-width limits.
