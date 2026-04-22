# Architecture

This page explains how the repository is organized and which files act as the source of truth.

## Main Layers

### Product Layer

Top-level product and research docs:

- `README.md`
- `PRD-r2i-skill-production.md`
- `R2I-research-notes.md`
- `R2Iprd.md`

These explain positioning, product intent, and the evolving documentation strategy.

### Skill Layer

Canonical skill entrypoint:

- `.agents/skills/r2i-skill/SKILL.md`

Compatibility wrapper:

- `.claude/skills/r2i-skill/SKILL.md`

The Codex-side skill is the main source of truth. The Claude Code skill is wrapper glue that points back to the shared files.

### Reference Layer

Reference files under `.agents/skills/r2i-skill/references/` hold the reusable logic and guardrails:

- user and candidate adaptation
- study-doc production rules
- interview shaping
- honesty and evidence guardrails
- preview workflow
- scoring behavior

This keeps `SKILL.md` focused on orchestration instead of dumping every template into one file.

### Script Layer

Current scripts:

- `serve_study_doc.py`: builds and serves a local preview for a study-doc markdown file or docs bundle
- `repo_doc_verify.py`: checks whether a generated study-doc bundle meets the baseline production contract

### Example Layer

Examples under `examples/` are for:

- regression checks
- preview testing
- showing what "good" looks like

They are not the main source of truth for the skill rules.

## Core Flow

The repository is designed around this flow:

1. analyze repository evidence
2. shape a `study-doc`
3. move into `prediction-pack`
4. run `mock` or `spoken-mock`
5. produce a `score-report`
6. translate only defended material into `resume` output

## Source Of Truth Rules

Treat these as the main edit targets:

- `.agents/skills/r2i-skill/SKILL.md`
- `.agents/skills/r2i-skill/references/*`
- `.agents/skills/r2i-skill/scripts/*`

Treat these as secondary or derived:

- `.r2i-preview/`
- generated example previews
- any rendered HTML output

## Why This Split Matters

The skill should stay portable across hosts.

That means:

- orchestration lives in `SKILL.md`
- durable behavior rules live in `references/`
- executable preview and validation live in `scripts/`
- regression samples live in `examples/`
