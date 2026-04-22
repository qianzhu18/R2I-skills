# R2I Skill

R2I = `Repo to Interview`.

This repository hosts an agent skill that helps users turn a GitHub repo or local project into a reusable interview-training loop:

`study the repo like a dev doc -> get a prediction pack -> run mock answers -> receive a score report -> write honest resume bullets`

## What This Skill Does

R2I is not just a repo summary prompt.

It is designed to help a user:
- read and understand an unfamiliar repository
- turn the repository into a developer-learning document
- tailor preparation to a target role and candidate profile
- get challenged by an interviewer-style lens
- get a role-specific prediction pack with likely blockers
- practice one-question-at-a-time mock answers
- receive a score report with patch actions
- extract evidence-backed project stories and resume bullets

## Core Idea

Most tools stop at one step:
- repo understanding
- interview prep
- resume rewriting

R2I tries to connect them into one loop so the user does not end up with polished but undefendable bullets.

## Skill Structure

Main skill:
- `.agents/skills/r2i-skill/SKILL.md`
- `.claude/skills/r2i-skill/SKILL.md`

Supporting references:
- `.agents/skills/r2i-skill/references/candidate-profile.md`
- `.agents/skills/r2i-skill/references/learning-doc-playbook.md`
- `.agents/skills/r2i-skill/references/mastery-loop.md`
- `.agents/skills/r2i-skill/references/interview-engine.md`
- `.agents/skills/r2i-skill/references/user-scenarios.md`
- `.agents/skills/r2i-skill/references/evidence-and-honesty.md`
- `.agents/skills/r2i-skill/references/output-modes.md`
- `.agents/skills/r2i-skill/references/preview-workflow.md`
- `.agents/skills/r2i-skill/references/score-report.md`

Preview script:
- `.agents/skills/r2i-skill/scripts/serve_study_doc.py`

Product docs:
- `PRD-r2i-skill-production.md`
- `R2I-research-notes.md`
- `R2Iprd.md`

## Output Modes

- `quick-scan`: first-pass repo understanding
- `study-doc`: development-doc-style learning manual
- `learn`: compact learning mode
- `interview`: project explanation, Q&A, and interviewer follow-ups
- `prediction-pack`: role-specific likely questions, blockers, and patch list
- `mock`: interactive text interview, one question at a time
- `spoken-mock`: oral-practice mode, one question at a time
- `score-report`: scoring summary and patch plan
- `resume`: bilingual STAR bullets with evidence notes
- `interview-journey`: staged workflow across study, prediction, mock, and scoring
- `full-loop`: compact version of the whole path

## Local Preview

`study-doc` can now be previewed on a localhost port inside Codex app or Claude Code workflows.

The preferred preview format is a docs bundle, not one giant markdown page. The current learning-doc shape is:

- `00-overview.md`
- `01-quick-start.md`
- `02-system-map.md`
- `03-key-flows.md`
- `04-reading-path.md`
- `05-checklist.md`
- `06-pitfalls-and-faq.md`

Example:

```bash
python3 .agents/skills/r2i-skill/scripts/serve_study_doc.py \
  --input examples/aut-sci-write-docs \
  --port 4173
```

Then open:

```text
http://127.0.0.1:4173
```

The preview script accepts either:
- a directory of markdown pages
- a single markdown file

This is the intended bridge between "the model generated a learning document" and "the user can actually read it like a local doc site".

## Candidate Inputs

The skill works best when the user provides:
- target role
- target level
- candidate background
- repo relationship
- target company style
- weak spots
- interview language

Example:

```text
Use $r2i-skill on this repo.
Target role: AI engineer
Level: junior
Background: 1 internship, mostly Python
Repo relationship: I built this with a teammate
Weak spots: system design and tradeoff questions
Mode: study-doc
```

## Example Prompts

- `Use $r2i-skill to convert this repository into a development learning doc for a junior backend engineer interview.`
- `Use $r2i-skill to give me the full interview-journey for this repo.`
- `Use $r2i-skill to generate a prediction-pack for a backend engineer interview based on this repo.`
- `Use $r2i-skill to run a spoken-mock for a junior full-stack role and ask one question at a time.`
- `Use $r2i-skill to generate a score-report for my last three answers in this thread.`
- `Use $r2i-skill to turn this project into bilingual resume bullets, and tell me which claims are still weak.`
- `Use $r2i-skill to act like an interviewer and pressure-test my explanation of this repo.`

## Design Principles

- Evidence before expression
- Honest framing over hype
- Learning before resume writing
- Interviewer pressure before final bullets
- Role-aware prep over generic question dumps
- Stage-based training over disconnected modes

## Current Positioning

R2I is best understood as:

`an evidence-backed repo-to-interview skill for people who want to learn, explain, and write about projects without bluffing`

## Compatibility

This repository includes two entrypoints so the skill can be used in both major workflows:
- `Codex`: repository skill under `.agents/skills/r2i-skill/`
- `Claude Code`: project skill under `.claude/skills/r2i-skill/`

## Voice Note

This repository does not implement native microphone-based interviewing by itself.

What it does support today:
- `spoken-mock`: a voice-friendly oral practice mode where the skill asks one question at a time and evaluates the user's spoken answer after the user types a transcript or summary

What would be needed for true voice interviewing:
- a separate voice wrapper built with a realtime voice stack, not just a repo skill
