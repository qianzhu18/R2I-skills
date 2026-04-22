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

## Fast Verification

The repo includes lightweight tests for two important implementation areas:

```bash
python3 -m unittest tests/test_extract_core_insights.py tests/test_sci_search.py
```

In local testing, these six tests passed.

## What To Verify Next

- Can you explain why this is a skill suite instead of one app?
- Can you point to the script that powers journal metric normalization?
- Can you trace the PDF-to-PPT flow?
