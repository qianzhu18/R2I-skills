# Key Flows

## Most Important Workflow: PDF To PPT

The best learning flow in this repo is the `sci-ppt` pipeline.

1. user provides a paper PDF
2. the workflow extracts text and figures
3. the system generates an editable markdown outline
4. the user revises the outline
5. the revised outline is converted into PPT input
6. the final `.pptx` is generated

## Why This Flow Matters

This shows the repository is not chasing blind end-to-end automation. It keeps a human editing checkpoint in the middle, which is a meaningful product and engineering decision.

## Secondary Flow: Literature Search

`sci-search` combines:
- arXiv
- PubMed
- Web of Science when configured
- local journal metric normalization

That makes it more than a simple paper search wrapper.

## If You Want To Drill Down

- for workflow orchestration: read `paper_workflow.py`
- for packaging and invocation: read the corresponding `skills/sci-ppt/SKILL.md`
- for search-system talking points: read `sci_search.py`
