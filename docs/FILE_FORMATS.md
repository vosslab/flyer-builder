# File formats

Flyer Builder consumes coordinate-free YAML plus local visual assets and produces a PDF per build
for direct printing. This reference names the supported formats and where they belong.

## Inputs

- Flyer definitions use `.yaml` files under [flyers/](../flyers/). See
  [YAML_FILE_FORMAT.md](YAML_FILE_FORMAT.md) for their structure.
- Text blocks contain YAML strings and use a limited subset of ReportLab paragraph markup for links
  and line breaks.
- Raster artwork may be a format Pillow can decode, including the PNG and WebP assets in the shipped
  flyers. The renderer retains source pixel dimensions and losslessly embeds decoded raster pixels;
  it does not create JPEG-encoded PDF image streams.
- SVG artwork is read through `svglib` and placed as vector PDF artwork. Store it beside the flyer
  that uses it.
- Font files live under [assets/fonts/](../assets/fonts/) and currently provide the regular and bold
  Atkinson Hyperlegible Next faces.

## Outputs

- [build_flyer.py](../build_flyer.py) writes PDFs to `output/pdf/` by default. That directory is
  Git-ignored because PDFs are generated artifacts.
- The CLI prints the generated PDF path after a successful build.
- PDF links come from text URLs and QR-code destinations. They remain clickable in compatible PDF
  viewers.

The production pipeline is YAML -> PDF -> print. Optional full-page WebP captures support
documentation and visual testing; they are not required outputs or print intermediates. WebP
source artwork remains a valid input.

## Asset ownership

Keep each flyer's source artwork below its own `flyers/<name>/assets/` directory. This keeps the
YAML file portable inside the repository and prevents it from relying on an external checkout.

The GitHub flyer includes a profile image, contribution graph, and Octocat mark from their stated
sources. Refresh external-profile visuals intentionally and review the page after doing so.

## Print fidelity

SVG artwork, text, rules, and QR modules remain vector in the PDF, so they do not have one global
DPI value. Raster artwork keeps its source pixel dimensions; its effective print resolution depends
on the authored physical size. Converting a legacy JPEG source to PNG prevents another lossy JPEG
encoding step but cannot restore details already lost in the original JPEG.
