# File structure

## Top-level layout

```text
assets/             Shared bundled fonts and font licenses
build_flyer.py      CLI for building one YAML flyer
docs/               Project and workflow documentation
flyerlib/           YAML-to-PDF rendering library
flyers/             Editable flyer YAML and local artwork
output/             Ignored generated PDFs and previews
tests/              Flyer contract and repository hygiene tests
tools/              Repository tooling notes
```

## Key subtrees

- [../flyerlib/](../flyerlib/) contains the renderer package. `render.py` owns YAML parsing,
  ReportLab layout, SVG drawing, QR generation, and PDF output handling.
- [../flyers/stvc/](../flyers/stvc/) contains the podcast and biology-game example flyer.
- [../flyers/github/](../flyers/github/) contains the Voss Lab GitHub overview flyer, profile image,
  contribution graph, and Octocat mark.
- [../assets/fonts/](../assets/fonts/) contains the regular and bold bundled text fonts. Their
  license lives under `assets/fonts/licenses/`.
- [../tests/](../tests/) contains the focused flyer test plus propagated hygiene tests.

## Generated artifacts

- `output/pdf/` receives built PDFs and review images. The root `.gitignore` excludes `output*/`.
- `tmp/` and `tests/_temp/` are ignored temporary workspaces.
- Flyer source YAML and `flyers/<name>/assets/` are authored inputs and remain tracked.

## Documentation map

- [INSTALL.md](INSTALL.md) covers requirements and setup.
- [USAGE.md](USAGE.md) documents the CLI and coordinate-free source format.
- [CODE_ARCHITECTURE.md](CODE_ARCHITECTURE.md) describes the rendering flow.
- [FILE_STRUCTURE.md](FILE_STRUCTURE.md) maps repository paths.
- [COLOR_PALETTE.md](COLOR_PALETTE.md) supplies the standard accent colors for authored flyers.

## Where to add work

- Add a new flyer in `flyers/<name>/` with `<name>.yaml` and `assets/`.
- Add renderer behavior in `flyerlib/render.py` only when it is shared by more than one flyer.
- Add durable behavior tests in `tests/test_*.py`; use `tests/_temp/` for one-time investigation.
- Add user-facing workflow documentation under `docs/` and keep generated previews out of Git.
