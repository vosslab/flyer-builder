# Install

Installing this repository makes the `build_flyer.py` command able to render the included
coordinate-free YAML flyers to PDFs.

## Requirements

- Python 3.12 on macOS, run through `source source_me.sh && python3`.
- The packages listed in [../pip_requirements.txt](../pip_requirements.txt).
- Poppler is optional for rendered-PDF visual review with `pdftoppm`.

## Install steps

```bash
source source_me.sh && python3 -m pip install -r pip_requirements.txt
```

On macOS, [../Brewfile](../Brewfile) supplies the repository's Python runtime:

```bash
brew bundle
```

## Verify install

Build the small, self-contained GitHub flyer:

```bash
source source_me.sh && python3 build_flyer.py -i flyers/github/github.yaml
```

The command prints `output/pdf/github.pdf` after it creates the one-page PDF.

## Known gaps

- Verify a clean Debian installation when that platform becomes a supported release target.
