# Reading Path

## Recommended Order

1. `README.md`
2. `.claude-plugin/marketplace.json`
3. `skills/sci-ppt/SKILL.md`
4. `skills/sci-ppt/src/aut_sci_ppt/run.py`
5. `skills/sci-ppt/src/aut_sci_ppt/paper_workflow.py`
6. `scripts/extract_core_insights.py`
7. `skills/sci-search/sci_search.py`
8. tests

## Why This Order

- start from the product promise
- then understand how multiple skills are aggregated
- then study the richest workflow
- then inspect lower-level scripts
- finally verify engineering maturity through tests

## Ignore On First Pass

- `docs/` visual assets
- example output binaries
- historical figure output directories

## Three Useful Lanes

### Learner Lane

Use this if your goal is repo comprehension:

1. `README.md`
2. `.claude-plugin/marketplace.json`
3. `skills/sci-ppt/SKILL.md`
4. `paper_workflow.py`

### Contributor Lane

Use this if your goal is safe local edits:

1. `README.md`
2. tests
3. `extract_core_insights.py`
4. one target skill implementation file

### Interviewer Lane

Use this if your goal is explanation and defense:

1. `README.md`
2. `skills/sci-ppt/SKILL.md`
3. `paper_workflow.py`
4. `sci_search.py`
5. tests as proof points
