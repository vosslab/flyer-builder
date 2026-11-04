# File formats

Flyer Builder consumes coordinate-free YAML plus local visual assets and produces one or more PDF
files. This reference names the supported formats and where they belong.

## Inputs

- Flyer definitions use `.yaml` files under [flyers/](../flyers/). See
  [YAML_FILE_FORMAT.md](YAML_FILE_FORMAT.md) for their structure.
- Text blocks contain YAML strings and use a limited subset of ReportLab paragraph markup for links
  and line breaks.
- Raster artwork may be a format that ReportLab's `ImageReader` can read, including the PNG and JPEG
  assets in the shipped flyers.
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

## Asset ownership

Keep each flyer's source artwork below its own `flyers/<name>/assets/` directory. This keeps the
YAML file portable inside the repository and prevents it from relying on an external checkout.

The GitHub flyer includes a profile image, contribution graph, and Octocat mark from their stated
sources. Refresh external-profile visuals intentionally and review the page after doing so.
