# Usage

The production workflow is YAML -> PDF -> print. Build a one-page US Letter flyer from a YAML
source whose nested rows and columns determine layout.

## Quick start

Build the Stump the Vibe Coder flyer:

```bash
source source_me.sh && python3 build_flyer.py -i flyers/stvc/stvc.yaml
```

Build the Voss Lab GitHub flyer:

```bash
source source_me.sh && python3 build_flyer.py -i flyers/github/github.yaml
```

Each command writes a PDF under `output/pdf/`, named after its YAML file.
The GitHub graph is a checked-in local WebP asset, so ordinary flyer builds stay offline.

## Print the PDF

Open the generated PDF in your PDF viewer and print on US Letter paper at actual size (100%).
The builder produces only the PDF; a full-page raster image is not an intermediate print step.
Keep source artwork at its original resolution. Optional WebP renders are for review and testing.

## CLI

`build_flyer.py` accepts these options:

- `-i`, `--input`: required YAML flyer source.
- `-o`, `--output`: optional destination PDF path.

For example, create a separately named PDF:

```bash
source source_me.sh && python3 build_flyer.py \
  -i flyers/github/github.yaml \
  -o output/pdf/vosslab-github.pdf
```

## Layout language

The top-level `layout` is one `row` or `col` block. Rows split their available width by each
item's `weight`; columns stack items in source order. The renderer measures text and images, so
YAML never supplies page coordinates.

Supported blocks are:

- `text`: literal text, an optional named style, and an optional PDF link.
- `image`: a local raster image or SVG with an authored height.
- `qr`: a URL rendered as a linked vector QR code, with optional color, label, and SVG icon.
- `rule`: a horizontal divider.
- `row` and `col`: nested containers with `items` and an optional `gap`.

Use the existing [../flyers/stvc/stvc.yaml](../flyers/stvc/stvc.yaml) and
[../flyers/github/github.yaml](../flyers/github/github.yaml) as complete examples. Put a flyer's
local artwork beside its YAML file in an `assets/` directory.

## Outputs

- PDFs are generated under `output/pdf/` by default and ignored by Git.
- The source YAML and its local assets are the canonical editable flyer materials.
- The renderer rejects invalid blocks, missing assets, unknown styles, and content that does not
  fit a Letter page.

## Verification

Run the flyer contract check with:

```bash
source source_me.sh && python3 -m pytest tests/test_flyer_render.py -q
```

## Known gaps

- Verify each new flyer with an actual printed page and phone scan before distribution.
