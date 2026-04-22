# Examples

This directory contains example outputs and regression fixtures for the `study-doc` workflow.

## Current Files

### `aut-sci-write-docs/`

Multi-page onboarding-style learning docs bundle.

Use it for:

- preview testing
- validator testing
- visual checks in Codex app

### `aut-sci-write-study-doc.md`

Single-file fallback sample.

Use it for:

- compact rendering tests
- compatibility checks when a multi-page bundle is not desired

## Recommended Usage

Preview:

```bash
python3 .agents/skills/r2i-skill/scripts/serve_study_doc.py \
  --input examples/aut-sci-write-docs \
  --port 4173
```

Validate:

```bash
python3 .agents/skills/r2i-skill/scripts/repo_doc_verify.py \
  --input examples/aut-sci-write-docs
```
