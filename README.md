# R2I Skill

R2I = `Repo to Interview`.

This repository hosts an agent skill that helps users turn a GitHub repo or local project into a reusable mastery loop:

`understand the project -> learn it actively -> survive interviewer follow-ups -> write honest resume bullets`

## What This Skill Does

R2I is not just a repo summary prompt.

It is designed to help a user:
- read and understand an unfamiliar repository
- build a practical learning path
- tailor preparation to a target role and candidate profile
- get challenged by an interviewer-style lens
- get a role-specific prediction pack with likely blockers
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
- `.agents/skills/r2i-skill/references/mastery-loop.md`
- `.agents/skills/r2i-skill/references/interview-engine.md`
- `.agents/skills/r2i-skill/references/user-scenarios.md`
- `.agents/skills/r2i-skill/references/evidence-and-honesty.md`
- `.agents/skills/r2i-skill/references/output-modes.md`

Product docs:
- `PRD-r2i-skill-production.md`
- `R2I-research-notes.md`
- `R2Iprd.md`

## Output Modes

- `quick-scan`: first-pass repo understanding
- `learn`: learning order, concepts, tasks, and checkpoint questions
- `interview`: project explanation, Q&A, and interviewer follow-ups
- `prediction-pack`: role-specific likely questions, blockers, and patch list
- `mock`: interactive text interview, one question at a time
- `spoken-mock`: oral-practice mode, one question at a time
- `resume`: bilingual STAR bullets with evidence notes
- `full-loop`: compact version of the whole path

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
Mode: prediction-pack
```

## Example Prompts

- `Use $r2i-skill to analyze this repository and give me a full-loop output.`
- `Use $r2i-skill to help me learn this repo step by step, then ask me interviewer-style follow-up questions.`
- `Use $r2i-skill to generate a prediction-pack for a backend engineer interview based on this repo.`
- `Use $r2i-skill to run a spoken-mock for a junior full-stack role and ask one question at a time.`
- `Use $r2i-skill to turn this project into bilingual resume bullets, and tell me which claims are still weak.`
- `Use $r2i-skill to act like an interviewer and pressure-test my explanation of this repo.`

## Design Principles

- Evidence before expression
- Honest framing over hype
- Learning before resume writing
- Interviewer pressure before final bullets
- Role-aware prep over generic question dumps

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
