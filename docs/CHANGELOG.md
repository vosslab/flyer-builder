## 2026-11-04

### Additions and New Features

- Rebalance the GitHub flyer header with a larger portrait/title, a nearly full-width contribution
  graph, stronger repository names, and shorter copy. Remove the redundant project-list title;
  retain all 26 projects and the printer-safe margins.

- Color-code GitHub repository names and divider rules consistently by section using the standard
  text palette; preserve navy category headings.

- Replace the GitHub flyer project list with 26 separately named favorites in balanced teaching,
  publishing, science, media, and maker categories; enlarge the profile QR code to 140 points.

- Replace the catch-all GitHub project category with Molecular structure, Biology games, and AI
  development tools; rebalance the project columns within the fixed print margins.

- Separate the two teaching-workflow repository entries and add hilbert-curve-brick and
  color-by-number-tool to the GitHub flyer Maker tools section.

- Clarify the production flyer pipeline as YAML -> PDF -> print; full-page WebP captures remain
  optional documentation and visual-test artifacts, outside the print workflow.

- Clarify GitHub flyer hierarchy with larger navy category headings, accent rules, and grouped project columns.

- Match the GitHub flyer Octocat graphic to the QR code navy (`#182B49`) and refresh previews.

- Refresh the README with reproducible previews of both flyers, installation and authoring routes,
  architecture and file maps, YAML and output references, troubleshooting, development guidance,
  and related-project evidence. Mark the inherited Graphify snapshot as starter-template material.
- Add coordinate-free YAML flyer rendering and migrate the redesigned StVC flyer with bundled
  fonts, editable SVG artwork, local QR generation, and one-page PDF output.
- Add a print-ready GitHub profile flyer with one profile QR code and verified representative work
  across education, interactive biology, protein geometry, and practical AI workflows.
- Refresh the GitHub flyer with the supplied contribution graph, live GitHub profile photo, official
  Octocat mark, and the six current pinned-project summaries.
- Add the teaching workflow and LEGO label maker to the GitHub flyer and correct Bad Cell Day's
  across-organs cooperative-game description.
- Replace the supplied contribution screenshot with a refreshable direct light-mode GitHub capture
  stored as a local quality-90 WebP flyer asset.
- Preserve decoded raster source dimensions in PDF image streams, replace the StVC JPEG asset with
  a same-size PNG, and raise refreshed WebP review assets to quality 95.

### Developer Tests and Notes

- Enforce a fixed 43.2-point printer-safe margin on all flyer edges, use real row gutters and
  balanced root-column spacing, and verify the rendered QR-link bounds reach only those safe edges.

- Rebuild both examples for quality-90 WebP documentation screenshots. Verify local Markdown links,
  the README opening paragraph, and the focused flyer rendering contract (43 checks pass).
- Verify the StVC PDF is one Letter page, includes clickable destinations, renders all artwork,
  and has a saved WebP review image.
