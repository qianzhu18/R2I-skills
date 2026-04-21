# Evidence And Honesty Rules

This skill should help users sound strong without sounding fake.

## Evidence Tiers

Use these labels mentally when writing:

- `fact`: directly supported by repository artifacts
- `inference`: a reasonable conclusion from repository structure, naming, tests, or config
- `framing`: a suggested way to present the work in interviews or on a resume
- `metric to verify`: a useful number the user should confirm before using

Do not blur these categories together.

## Safe Evidence Sources

Prefer evidence from:
- README and project docs
- package manifests and dependency files
- configuration, deployment, and CI files
- module boundaries, routing, services, and tests
- commit or PR history if available
- issue descriptions or architecture notes if available

## Unsafe Claims

Do not state any of these as facts unless explicitly supported:
- number of users
- performance improvement percentages
- revenue impact
- conversion lift
- cost savings
- team size or leadership scope
- production incident ownership

If a stronger bullet would benefit from a number, provide:
- the bullet wording
- the missing number as `metric to verify`

## Resume Bullet Rules

Every resume-oriented bullet should be:
- specific about system, feature, or technical responsibility
- honest about certainty
- short enough to paste into a resume after light editing
- paired with a private evidence note when the repo supports it
- pressure-tested by at least one interviewer-style follow-up question when feasible

Example pattern:
- Bullet: Built a modular authentication flow for a TypeScript web app, separating route guards, token handling, and session state to improve maintainability and onboarding clarity.
- Evidence note: README auth section, `src/auth/*`, router middleware, session config
- Metric to verify: reduced auth-related bugs or onboarding time

## Interview Answer Rules

Good interview material should:
- connect implementation details to tradeoffs
- highlight why the design matters
- surface likely weaknesses or open questions
- challenge strong bullets with "how do you know?" and "why does this matter?"

Bad interview material:
- just paraphrases README text
- claims end-user impact without evidence
- avoids uncertainty by sounding generic

## Honesty Over Hype

If the repository looks unfinished, toy-sized, tutorial-like, or generated:
- say so tactfully
- shift the framing toward learning value, architectural clarity, or technical experimentation
- avoid pretending it was a large production system
