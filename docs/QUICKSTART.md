# Quickstart

This repository ships an `r2i-skill` that works in both Codex and Claude Code.

Use this page when you want the fastest path from clone to first successful `study-doc` preview.

## 30-Second Path

1. Clone the repo.
2. Open it in Codex app or Claude Code.
3. Invoke the skill on a repository.
4. If you want a browser preview, generate a `study-doc` and run the local preview script.

## Install Shape

This repository already contains both entrypoints:

- Codex entrypoint: `.agents/skills/r2i-skill/`
- Claude Code entrypoint: `.claude/skills/r2i-skill/`

Use the repo directly if you are developing the skill itself.

If you want to install it into another environment later, copy the matching skill folder into that tool's skills directory.

## First Invocation

Example prompt:

```text
Use $r2i-skill on this repo.
Target role: backend engineer
Level: junior
Repo relationship: I studied this repo deeply
Mode: study-doc
```

## Local Preview

Build and serve the docs-bundle preview:

```bash
python3 .agents/skills/r2i-skill/scripts/serve_study_doc.py \
  --input examples/aut-sci-write-docs \
  --port 4173
```

Then open:

```text
http://127.0.0.1:4173
```

## Success Signals

A healthy first run should give you:

- a repo brief
- a docs-bundle style `study-doc`
- stable pages such as `00-overview` and `01-quick-start`
- a local preview that loads in the browser

## Validation

Validate the skill package:

```bash
python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  .agents/skills/r2i-skill
```

Validate a generated study-doc bundle:

```bash
python3 .agents/skills/r2i-skill/scripts/repo_doc_verify.py \
  --input examples/aut-sci-write-docs
```

## Next Reads

- [Architecture](./ARCHITECTURE.md)
- [Contributing](./CONTRIBUTING.md)
- [Examples](./EXAMPLES.md)
