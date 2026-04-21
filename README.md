# R2I Skill

R2I = `Repo to Interview`.

This repository hosts an agent skill that helps users turn a GitHub repo or local project into a reusable mastery loop:

`understand the project -> learn it actively -> survive interviewer follow-ups -> write honest resume bullets`

## What This Skill Does

R2I is not just a repo summary prompt.

It is designed to help a user:
- read and understand an unfamiliar repository
- build a practical learning path
- get challenged by an interviewer-style lens
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

Supporting references:
- `.agents/skills/r2i-skill/references/mastery-loop.md`
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
- `resume`: bilingual STAR bullets with evidence notes
- `full-loop`: compact version of the whole path

## Example Prompts

- `Use $r2i-skill to analyze this repository and give me a full-loop output.`
- `Use $r2i-skill to help me learn this repo step by step, then ask me interviewer-style follow-up questions.`
- `Use $r2i-skill to turn this project into bilingual resume bullets, and tell me which claims are still weak.`
- `Use $r2i-skill to act like an interviewer and pressure-test my explanation of this repo.`

## Design Principles

- Evidence before expression
- Honest framing over hype
- Learning before resume writing
- Interviewer pressure before final bullets

## Current Positioning

R2I is best understood as:

`an evidence-backed repo-to-interview skill for people who want to learn, explain, and write about projects without bluffing`
