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

### 1. Repo brief

State:
- what the repository appears to do
- the likely target users
- the likely business or product value
- what level of certainty you have

### 2. Product and scenario context

Explain:
- who this project seems built for
- what user problem it solves
- in what scenarios it is used
- what success might look like for the product

If not explicit, mark this as inference.

### 3. Architecture and module map

Show:
- top-level architecture shape
- major modules and their responsibilities
- important dependencies or services
- boundaries between frontend, backend, data, infra, or agent layers when relevant

Use Mermaid only if the system boundaries are clear enough.

### 4. Request flow or core workflow

Describe the most important path through the system:
- user action
- entrypoint
- key modules crossed
- output or side effect

This helps users move from file-level understanding to system-level understanding.

### 5. Reading order

Give a practical reading path:
- where to start
- what to read second
- what to defer
- what to ignore on first pass

The goal is to reduce overwhelm.

### 6. Concepts and glossary

List the domain terms, patterns, and abstractions a learner must understand.

Examples:
- framework concepts
- domain entities
- internal service names
- agent/tool vocabulary

### 7. Pitfalls and checkpoint questions

Call out the likely confusion points:
- hidden coupling
- naming traps
- config gotchas
- misleading architecture assumptions

Add 3-5 checkpoint questions to verify understanding before the user moves to interview prep.

### 8. Practice tasks

Provide tasks in increasing difficulty:
- trace a flow
- change a small behavior
- extend a module
- explain a tradeoff

## Writing Rules

- Write like onboarding documentation for a developer joining the project.
- Prefer clear headings and compact explanations.
- Avoid hype, fluff, and motivational filler.
- Separate facts from inference.
- Keep the first-pass document scannable.
