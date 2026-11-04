# Repository map

Graphify is an optional maintainer tool for exploring source relationships. The inherited graph
snapshot describes the starter repository, not the flyer renderer; it is not current architecture
evidence. Use [CODE_ARCHITECTURE.md](CODE_ARCHITECTURE.md) and
[FILE_STRUCTURE.md](FILE_STRUCTURE.md) for the current application map.

## Refresh the source map

- Run the mapping wrapper from the repository root after installing development dependencies.
- Keep generated Graphify data under the ignored root directory `graphify-out/`.
- Inspect the resulting map before publishing a replacement illustration.

```bash
source source_me.sh && python3 devel/graphify_map_repo.py --help
```

The inherited [GRAPHIFY_map.svg](GRAPHIFY_map.svg) remains a starter-template artifact. Regenerate it
before using it to explain this repository.
