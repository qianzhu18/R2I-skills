# Contributing

Use this page when changing the skill itself rather than using the skill on another repository.

## Contribution Principles

- Keep Codex and Claude Code behavior aligned.
- Prefer small, auditable reference files over bloated top-level instructions.
- Do not weaken evidence and honesty constraints to make output sound more impressive.
- Favor reusable docs-bundle patterns over one-off custom page structures.

## Safe Change Order

If you are making a change for the first time, follow this order:

1. update the smallest relevant reference file
2. update `SKILL.md` only if orchestration needs to change
3. update examples if the expected study-doc shape changes
4. run validation
5. preview the result locally

## Before You Open A PR

Run:

```bash
python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  .agents/skills/r2i-skill
```

```bash
python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  .claude/skills/r2i-skill
```

```bash
python3 .agents/skills/r2i-skill/scripts/repo_doc_verify.py \
  --input examples/aut-sci-write-docs
```

If the study-doc structure changed, also rebuild or preview locally:

```bash
python3 .agents/skills/r2i-skill/scripts/serve_study_doc.py \
  --input examples/aut-sci-write-docs \
  --build-only
```

## Good Contributions

- stronger study-doc production constraints
- better repo-type coverage in examples
- tighter evidence rules
- clearer interview trap prediction
- improved preview and validation tooling

## Contributions To Avoid

- adding hype without stronger evidence handling
- duplicating guidance across many files when one reference file can own it
- making the preview prettier while weakening the content contract
- editing generated preview output instead of the markdown source
