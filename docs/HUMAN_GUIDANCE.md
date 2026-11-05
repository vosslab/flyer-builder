# Human guidance

<!-- VENDORED HEADER: START -->
Record the durable guidance Neil Voss states, or approves for preservation here, in his own words:
first person or close paraphrase, one to three lines per bullet. Material he supplies as a source
may inform [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md) once it is settled, and an entry of uncertain
origin belongs there too. Rules: [REPO_STYLE.md](REPO_STYLE.md).
[PROPAGATED HEADER - ENTRIES BELOW ARE YOURS]
<!-- VENDORED HEADER: END -->

## Flyer authoring (2026-11-04)

- Flyer source should use rows and columns and avoid authored coordinates.
- Build the StVC migration as a redesign while preserving its final content and print brief.
- Make a one-page Voss Lab GitHub overview for students, instructors, and curious makers. It should
  feature one prominent profile QR code and concrete project categories without stale project counts.
- Make the GitHub flyer visually grounded with the profile photo, contribution graph, and current
  pinned projects: biology-problems, vosslab-skills, concept-map-maker, qti-package-maker-rs,
  vossvolvox-pages, and bad-cell-day.
- Use a harmonious wider accent palette across GitHub flyer sections and projects while keeping a
  white page, navy body text, and the contribution graph's native greens.
- Expand the GitHub flyer beyond pinned repositories with the teaching workflow
  `markdown-to-tutorial` plus `djot-slide-builder` and `brick-inventory-label-maker`; skip the
  similar biology-problems website.
- Use a direct, light-mode GitHub contribution capture rather than a supplied graph screenshot;
  keep it as a local quality-95 WebP asset so normal flyer builds remain offline.
- Use quality-95 WebP for refreshed review screenshots and contribution captures; preserve raster
  source dimensions in the PDF and avoid new JPEG image encoding.
- Use the approved square pastel-white 2026 profile portrait from the branding library for the
  GitHub flyer rather than a dark GitHub avatar.


- Match the GitHub QR center Octocat color to the QR modules.

- Make category headings visibly distinct from repository subheadings so flyer organization is clear.

- The production flyer pipeline is YAML -> PDF -> print. Full-page WebP output is optional for
  testing and review, not a required deliverable or print intermediate.

- Give each repository its own entry, including markdown-to-tutorial and djot-slide-builder; use
  lower-page space for additional Maker tools instead of combining distinct repositories.
- Enforce a 0.6-inch margin on every flyer edge for printer safety. Use spare vertical space to
  balance the page rather than leaving a large white area below the final content.
- The GitHub QR already gives the profile destination; remove the redundant lower-page caption.

- Use meaningful project categories rather than a catch-all such as Research, games, and AI.
- Use this 26-repository GitHub flyer shortlist: markdown-to-tutorial, flyer-builder,
  djot-slide-builder, exam-formatting-tools, biology-problems, qti-package-maker-rs, nilbc-web,
  screenshot-ai-renamer-macos, book-to-markdown, peptidyle-learning-engine, movie-slide-maker,
  syllabus, curriculum-vitae, ferrum-chemical-forge, vossvolvox-pages,
  virtual-lab-protocol-simulation, course-finder-grid, vosslab-daily-blog, protein-image-grader,
  track-runner-virtual-dolly-cam, brick-collection, concept-map-maker,
  brick-inventory-label-maker, emwy-video-editor, automated-radio-disc-jockey, and
  py-movie-media-manager. Keep each as a separate concise entry; ferrum-chemical-forge is pre-alpha.
- Favor a genuinely larger 140-point profile QR code over further squeezing project descriptions.

- Color-code GitHub repositories by section rather than assigning unrelated colors within a section.
