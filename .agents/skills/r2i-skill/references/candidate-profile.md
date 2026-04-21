# Candidate Profile

Interview output gets much better when the skill first builds a compact profile of the candidate.

## Preferred Inputs

If the user provides them, capture these fields:
- `target role`
- `target level`
- `candidate background`
- `repo relationship`
- `target company style`
- `weak spots`
- `language`
- `time available`

## Default Assumptions

If the user gives no profile information:
- assume a general software engineer interview
- assume mid-level difficulty
- assume the user wants Chinese output unless otherwise stated
- assume the repository is something they want to discuss honestly, not claim ownership of blindly

State these assumptions briefly when the output is interview-heavy.

## Why These Fields Matter

### Target role

This is the highest-signal input. The same repository should produce different questions for:
- frontend
- backend
- full-stack
- AI / agent
- infrastructure

### Target level

Level changes question depth:
- intern / junior: understanding, implementation details, debugging, learning ability
- mid: tradeoffs, ownership, cross-module reasoning
- senior+: architecture, prioritization, failure handling, mentoring, business framing

### Candidate background

The user may be:
- a student using the repo as a learning artifact
- a contributor with partial ownership
- the original builder
- someone preparing from an open-source repo

Do not force the same ownership language on all of them.

### Repo relationship

This field is critical for honesty.

Examples:
- `built it`: stronger ownership framing is possible
- `contributed to it`: be precise about module or feature responsibility
- `studied it`: frame around understanding, reverse engineering, and proposed improvements

### Weak spots

Use weak spots to concentrate the pressure test.

Examples:
- "I panic when asked tradeoffs"
- "I can explain code but not business value"
- "I don't know how to describe my contribution honestly"
- "I struggle with system design follow-ups"

## Output Behavior

For interview-oriented outputs, surface the profile in a compact line:
- role
- level
- repo relationship
- language
- explicit assumptions if any

Do not turn the profile section into a long questionnaire unless the user asks for that.
