#!/usr/bin/env bash
# Render the bundled flyers for the README screenshot block.
set -euo pipefail

source source_me.sh
python3 build_flyer.py -i flyers/stvc/stvc.yaml
python3 build_flyer.py -i flyers/github/github.yaml

mkdir -p docs/screenshots
pdftoppm -f 1 -singlefile -r 154 -png output/pdf/stvc.pdf /tmp/stvc_flyer
pdftoppm -f 1 -singlefile -r 154 -png output/pdf/github.pdf /tmp/github_flyer
cwebp -quiet -q 90 /tmp/stvc_flyer.png -o /tmp/stvc_flyer.webp
cwebp -quiet -q 90 /tmp/github_flyer.png -o /tmp/github_flyer.webp
cp /tmp/stvc_flyer.webp docs/screenshots/stvc_flyer.webp
cp /tmp/github_flyer.webp docs/screenshots/github_flyer.webp
rm /tmp/stvc_flyer.png /tmp/github_flyer.png /tmp/stvc_flyer.webp /tmp/github_flyer.webp
