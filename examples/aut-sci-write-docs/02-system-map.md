# System Map

## Skill Layer

- `skills/sci-search`
- `skills/sci-extract`
- `skills/sci-figure`
- `skills/sci-review`
- `skills/sci-zotero`
- `skills/sci-ppt`

Each skill uses `SKILL.md` as its activation and workflow contract.

## Implementation Layer

Important Python entrypoints:

- `scripts/extract_core_insights.py`
- `skills/sci-search/sci_search.py`
- `skills/sci-ppt/src/aut_sci_ppt/run.py`
- `skills/sci-ppt/src/aut_sci_ppt/paper_workflow.py`

## Packaging Layer

- `.claude-plugin/marketplace.json` aggregates the skills into one plugin
- `skills-cli.js` provides local discovery for installed skills

## Repo Structure Lens

- `skills/`: declarative entrypoints and workflow contracts
- `scripts/`: shared executable helpers
- `.claude-plugin/`: plugin packaging and discovery metadata
- `examples/` and output folders: demonstration or generated material
- `docs/`: supporting explanation, not always the core runtime path

## Most Important Engineering Boundary

The strongest boundary is between:
- the declarative workflow contract in `SKILL.md`
- the executable logic in Python scripts and packages

## Best Drill-Down Candidates

- `skills/sci-ppt/src/aut_sci_ppt/paper_workflow.py`: richest end-to-end workflow
- `skills/sci-search/sci_search.py`: multi-source retrieval and normalization
- `scripts/extract_core_insights.py`: script-level evidence extraction plus testable behavior
