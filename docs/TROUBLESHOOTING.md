# Troubleshooting

Use this guide when a flyer build does not produce the expected PDF.

## Python cannot import a package

Run the repository bootstrap and install the declared dependencies:

```bash
source source_me.sh && python3 -m pip install -r pip_requirements.txt
```

Run all repository Python commands through the same bootstrap so the intended Python environment is
used.

## The build names a missing asset

Asset paths are relative to the YAML flyer file, not the repository root. Confirm the path exists
below the flyer's `assets/` directory and use its exact case.

## The build names an unknown style

Add the style under the source file's top-level `styles` mapping, or change the text block to use an
existing style. `body` is always available.

## Text or artwork looks wrong

Rebuild the flyer, then render and inspect the PDF at print scale. Check that images have an authored
`height`, SVG files have a usable view box, and a row gives each visual enough width.

```bash
pdftoppm -png output/pdf/github.pdf /tmp/github
```

Use a different output prefix when reviewing another flyer. The PNGs are temporary review files.

## The flyer uses more than one page

The renderer does not resize content to force it onto one page. Reduce copy, image height, text size,
or gaps in the YAML, then rebuild. Verify the page count with `pdfinfo` or `pypdf` before printing.

## A QR code will not scan

Keep its quiet zone unobstructed. Increase its authored `size`, simplify or remove the center icon,
and render at 200 and 300 dpi for decoding checks. A generated PDF is not proof that a code scans
from a physical print.
