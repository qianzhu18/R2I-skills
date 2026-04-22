# Quick Start

## First Read

Start with:

1. `README.md`
2. `.claude-plugin/marketplace.json`
3. `skills-cli.js`

This gives you:
- the skill inventory
- the installation model
- the plugin aggregation shape

## Prerequisites

- Python 3 available locally
- enough environment setup to run repo tests
- optional API credentials only if you want to exercise live external integrations

## Fast Verification

The repo includes lightweight tests for two important implementation areas:

```bash
python3 -m unittest tests/test_extract_core_insights.py tests/test_sci_search.py
```

In local testing, these six tests passed.

## Success Signals

You know the first-pass environment is healthy if:

- the unit tests pass
- you can explain what `.claude-plugin/marketplace.json` is doing
- you can point to one executable script and one `SKILL.md` contract without confusion

## Generated And Secondary Outputs

Do not treat every folder as equal source of truth on first pass.

- `skills/` is the skill contract layer
- Python files under `scripts/` or skill subfolders are execution logic
- output examples and generated artifacts are supporting evidence, not the best first edit target

## What To Verify Next

- Can you explain why this is a skill suite instead of one app?
- Can you point to the script that powers journal metric normalization?
- Can you trace the PDF-to-PPT flow?
