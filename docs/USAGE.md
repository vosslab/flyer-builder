# Usage

Build a flyer from YAML:

```bash
source source_me.sh && python3 build_flyer.py -i flyers/stvc/stvc.yaml
```

The default result is `output/pdf/stvc.pdf`. Use `-o` to choose another PDF path.

## Layout language

Flyers use nested `row` and `col` blocks. Rows divide the available width by `weight`; columns
stack children in order. The renderer computes all positions, wrapping, and row heights.

Supported content blocks are `text`, `image`, `qr`, and `rule`. A text block can select a named
style and override its size, leading, color, alignment, or bold weight. Images name a local path
and height. QR blocks carry a URL, size, optional foreground color, optional label, and optional
local SVG icon.

Use `gap` for space between group children. Keep source SVG artwork in the flyer asset directory;
the ReportLab SVG renderer preserves it as vector PDF artwork. The renderer reports rather than clips
content that cannot fit on one Letter page.
