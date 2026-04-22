# Aut_Sci_Write Study Doc

## Repo Brief

`Aut_Sci_Write` is a modular academic-skill suite rather than a single web product. Its repository packages six Claude Code research skills that cover literature search, PDF insight extraction, figure extraction, review writing, Zotero integration, and PPT generation.

The strongest engineering shape in this repo is "skill layer + Python implementation layer + workflow glue", especially for the `sci-ppt` path from paper PDF to editable outline to final presentation.

## Product And User Context

Primary users appear to be:
- graduate students
- researchers preparing literature reviews or rebuttals
- users who want to execute academic workflows inside Claude Code

Likely user value:
- reduce context-switching across search, reading, figure extraction, and presentation tasks
- standardize academic output quality
- make multi-step research workflows reusable as installable skills

## Architecture And Module Map

- `skills/sci-search`: paper search plus journal metrics
- `skills/sci-extract`: PDF insight extraction and Heilmeier-style analysis
- `skills/sci-figure`: figure and subfigure extraction from PDF
- `skills/sci-review`: literature review and rebuttal writing
- `skills/sci-zotero`: Zotero sync and citation workflows
- `skills/sci-ppt`: PDF or structured input to academic PPT generation

Implementation layers:
- Python scripts for the core extraction / search logic
- `SKILL.md` files as activation and workflow contracts
- a lightweight Node CLI for local skill discovery

## Core Workflow

The most instructive end-to-end path is `sci-ppt`:

1. read a paper PDF
2. extract text and figures
3. generate an editable markdown outline
4. let the user revise the outline
5. convert the revised outline into PPT input
6. generate a final `.pptx`

This is a human-in-the-loop workflow, not blind one-shot automation.

## File Reading Order

Read in this order:

1. `README.md`
2. `.claude-plugin/marketplace.json`
3. `skills-cli.js`
4. `skills/sci-ppt/SKILL.md`
5. `skills/sci-ppt/src/aut_sci_ppt/run.py`
6. `skills/sci-ppt/src/aut_sci_ppt/paper_workflow.py`
7. `scripts/extract_core_insights.py`
8. `skills/sci-search/sci_search.py`
9. `tests/test_extract_core_insights.py`
10. `tests/test_sci_search.py`

## Key Concepts Glossary

- `skill suite`: a package of multiple installable research skills
- `marketplace.json`: plugin aggregation entrypoint
- `human-in-the-loop`: user revises the generated outline before final PPT creation
- `journal metrics normalization`: converts multiple journal DB shapes into one consistent schema
- `lazy dependency loading`: avoids loading heavy PDF dependencies when only CLI help is needed

## Common Pitfalls

- Do not describe this repo as a monolithic research platform.
- Do not claim every workflow is fully autonomous; the PPT flow deliberately includes a manual edit step.
- The strongest engineering story is workflow modularization, not UI polish.

## Checkpoint Questions

- Why is this repository better described as a skill suite than an app?
- Why does the PPT workflow insert a markdown outline editing step?
- What engineering tradeoff is solved by local journal metric normalization?
- Which part of the repo feels most production-minded, and why?

## Practice Tasks

- Trace the `sci-ppt` workflow from PDF input to `.pptx` output.
- Explain how `sci-search` handles journal metrics and source aggregation.
- Summarize what the tests prove about the repository's reliability.
- Give a 1-minute project explanation for an AI tooling interview.
