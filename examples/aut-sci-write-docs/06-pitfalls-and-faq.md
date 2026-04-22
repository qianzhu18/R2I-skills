# Pitfalls And FAQ

## Common Misread

### "This is a full scientific platform."

Not really. The repository is better understood as a bundle of installable skills plus Python workflows.

### "Everything is fully autonomous."

Also not true. The PPT path intentionally keeps a manual editing step.

### "The main value is UI polish."

No. The strongest story is workflow modularization and task packaging.

### "Everything under examples or outputs is a good edit target."

Also no. Those directories are often artifacts, samples, or secondary material. Start with the workflow contract and implementation files first.

## Likely Interview Trap

If you oversell ownership or autonomy, an interviewer will quickly ask:

- Which part is prompt orchestration versus real executable logic?
- What happens when external APIs or PDF parsing fail?
- Why did the author choose a skill suite instead of one large tool?

## FAQ

### What is the best module to study first?

`sci-ppt`, because it shows the richest end-to-end workflow and the clearest human-in-the-loop design.

### What is the best script-level file to discuss?

Either:
- `paper_workflow.py` for workflow orchestration
- `sci_search.py` for multi-source search plus normalization

### What should I avoid editing first if I am still learning the repo?

Avoid starting with:

- generated outputs
- historical example artifacts
- cosmetic docs-only areas that do not reveal core workflow boundaries
