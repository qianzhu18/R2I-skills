# Learning Doc Playbook

Use this file when generating `study-doc` output or when `learn` should behave like structured onboarding.

## Goal

The learning phase should feel like an internal developer handbook for this repository.

Do not just summarize code. Turn the repository into a study document that helps the user:
- understand what the project is
- understand who it serves
- understand how the system is organized
- know what to read first
- know what to practice next

## Preferred Structure

Research note:
- current onboarding-style skills and repo wiki generators tend to use a small set of operational pages rather than one long essay
- common patterns are overview, quick start, system map, key flows, reading path, checklist, and pitfalls

Prefer a docs bundle with these pages:

### 00-overview.md

State:
- what the repository appears to do
- who it serves
- why it matters
- confidence level and major unknowns

### 01-quick-start.md

State:
- how to run or verify the project quickly
- what prerequisites exist
- what commands matter first
- how a learner knows the environment is working

Keep setup executable and time-bounded.

### 02-system-map.md

Show:
- top-level architecture shape
- major modules and responsibilities
- important dependencies or services
- a file map for the most important areas

Use Mermaid only if the system boundaries are clear enough.

### 03-key-flows.md

Describe the most important request, data, or user workflow:
- user action
- entrypoint
- key modules crossed
- output or side effect

This helps users move from file-level understanding to system-level understanding.

### 04-reading-path.md

Give a practical reading path:
- where to start
- what to read second
- what to defer
- what to ignore on first pass

The goal is to reduce overwhelm.

### 05-checklist.md

Include:
- key concepts glossary
- verification questions
- hands-on exercises
- "I understand this if..." checks

### 06-pitfalls-and-faq.md

Call out likely confusion points:
- hidden coupling
- naming traps
- config gotchas
- misleading architecture assumptions
- common wrong explanations

If the user does not ask for a multi-page docs bundle, you may compress these pages into one concise markdown document while preserving the same order.

## Writing Rules

- Write like onboarding documentation for a developer joining the project.
- Prefer clear headings and compact explanations.
- Avoid hype, fluff, and motivational filler.
- Separate facts from inference.
- Keep the first-pass document scannable.
- Prefer docs-bundle navigation over giant single-page dumps when preview is requested.
