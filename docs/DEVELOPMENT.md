# Development

This repository uses small Python modules and YAML examples. The application does not require a
package build step.

## Local workflow

Install runtime dependencies and build both shipped flyers:

```bash
source source_me.sh && python3 -m pip install -r pip_requirements.txt
source source_me.sh && python3 build_flyer.py -i flyers/stvc/stvc.yaml
source source_me.sh && python3 build_flyer.py -i flyers/github/github.yaml
```

Generated PDFs go to `output/pdf/` and are ignored by Git.

## Verification

Run the focused rendering contract while changing the renderer or shipped flyer sources:

```bash
source source_me.sh && python3 -m pytest tests/test_flyer_render.py -q
```

Run the complete repository checks before handoff:

```bash
source source_me.sh && python3 -m pytest tests/
```

The focused test verifies the StVC flyer remains one page and keeps its important PDF destinations.
PDF rendering and QR decoding at print resolutions remain implementation-time visual checks.

## Optional visual review

The production builder outputs only PDF. Render pages separately when visual inspection or
documentation needs a full-page image; do not route print output through a WebP preview.

```bash
bash devel/capture_flyer_screenshots.sh
```

This optional command rebuilds both PDFs and refreshes the quality-95 WebP documentation captures.

## GitHub graph refresh

Refresh the GitHub contribution asset only when a new live capture is wanted. Install development
requirements first; the script uses Playwright to capture GitHub's loaded light-mode calendar, then
writes the quality-95 local WebP used by offline flyer builds.

```bash
source source_me.sh && python3 -m pip install -r pip_requirements-dev.txt
source source_me.sh && python3 devel/refresh_github_contributions.py
```

## Adding a flyer

1. Create `flyers/<name>/<name>.yaml` and `flyers/<name>/assets/`.
2. Use [YAML_FILE_FORMAT.md](YAML_FILE_FORMAT.md) to compose rows, columns, copy, artwork, and QR
   codes without coordinates.
3. Build the new source with [build_flyer.py](../build_flyer.py) and inspect the PDF.
4. Add a permanent test only when the new behavior is a stable, meaningful shared contract.
