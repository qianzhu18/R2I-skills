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

## Most Important Engineering Boundary

The strongest boundary is between:
- the declarative workflow contract in `SKILL.md`
- the executable logic in Python scripts and packages
