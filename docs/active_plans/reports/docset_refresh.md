# Documentation refresh report

This refresh documents the current YAML-to-PDF implementation and its two production examples.

## Owners and artifacts

- README owner refreshes the landing page, verifies build commands, and reserves the screenshot block.
- Screenshot owner rebuilds both examples, renders their PDF pages, and publishes quality-90 WebP
  captures with a repeatable maintainer harness in `devel/capture_flyer_screenshots.sh`.
- Architecture owner creates code and file maps; installation/usage owner refreshes both workflows.
- Remaining-docs audit adds YAML and file-format references, troubleshooting, and development steps.
- Related-project owner verifies companion workflows and an alternative through primary sources.
- Agent-guidance audit keeps the already concise operational pointer file unchanged.

## Evidence and checks

- Local Markdown links, README opening paragraph, and flyer contract: 43 checks pass.
- Both examples rebuild from their local YAML and assets; final screenshots are visually reviewed.
- Central AUTHORS, Markdown, Python, and repository style files match the tracked baseline unchanged.
- The inherited Graphify map is identified as stale template evidence; no new graph is fabricated.

## Landing-page review

- README review score improves from 1/5 to 5/5: the former page supplied identity and licensing;
  the refreshed page adds current visual proof, a verified quick start, examples, and doc routes.
- Screenshot assets are 1309 by 1694 pixels, under 200 KB each, encoded as quality-90 WebP.

## Skipped artifacts

- Release history and news: no published release evidence; the current version file alone does not
  establish a release. No release is created by this refresh.
- Roadmap, TODO, cookbook, and FAQ: no distinct, evidence-backed material beyond existing guides.
- No contribution/security/community policy files or issue/PR templates require relocation.

## Known gaps

- Verify installation on a clean Debian environment.
- Verify physical printer output and phone scanning before distributing printed flyers.
- Regenerate the Graphify snapshot before using it as application architecture evidence.
