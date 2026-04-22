# Pitfalls And FAQ

## Common Misread

### "This is a full scientific platform."

Not really. The repository is better understood as a bundle of installable skills plus Python workflows.

### "Everything is fully autonomous."

Also not true. The PPT path intentionally keeps a manual editing step.

### "The main value is UI polish."

No. The strongest story is workflow modularization and task packaging.

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
