# Output Modes

Use this file to decide what to generate after the repo brief.

## Shared Rules

All modes should:
- start with a repo brief
- stay compact on first pass
- separate facts from inference
- offer a next action or follow-up path
- adapt to target role and candidate profile when interview stakes are involved

Default training order:
1. `study-doc`
2. `prediction-pack`
3. `mock` or `spoken-mock`
4. `score-report`
5. `resume`

## quick-scan

Use when the user wants a first-pass analysis.

Minimum deliverables:
- repo brief
- architecture shape or major modules
- standout files or folders
- likely interview-worthy strengths
- top uncertainties or risks

## learn

Use when the user wants to understand the repository deeply.

Minimum deliverables:
- repo brief
- recommended reading order
- 3-5 core concepts or subsystems
- 3 practice tasks or modifications
- 3-5 interviewer checkpoint questions to verify understanding
- what to ignore on first pass

`learn` should be compact. If the user explicitly wants a full developer-handbook style output, switch to `study-doc`.

## study-doc

Use when the user wants the repository converted into a development learning document, onboarding guide, or structured study manual.

Minimum deliverables:
- repo brief
- product / user / business context
- architecture and module map
- request flow or core workflow
- file reading order
- key concepts glossary
- common pitfalls
- 3-5 checkpoint questions
- practice tasks

When the output is meant to be reused or previewed locally:
- prefer the canonical seven-page docs bundle
- follow `study-doc-production.md`

## interview

Use when the user wants speaking material or interview prep.

Minimum deliverables:
- repo brief
- 10-15 repo-specific questions across basic, intermediate, and advanced
- concise reference answers
- common traps or interviewer follow-up questions
- 1-minute and 3-minute project explanation scripts

## prediction-pack

Use when the user wants "押题", "高频题", "关键卡点", or a concentrated pre-interview pack.

Minimum deliverables:
- repo brief
- target role and assumption line
- 10-15 likely high-frequency questions
- predicted key blockers
- red-flag follow-up questions
- fastest study patch list

## mock

Use when the user wants an interactive simulation.

Minimum deliverables:
- candidate profile line
- exactly one question at a time
- answer evaluation rubric
- one improvement tip per turn

Do not dump the full script unless explicitly asked.

## spoken-mock

Use when the user wants oral practice.

Minimum deliverables:
- candidate profile line
- one spoken-style question at a time
- guidance to answer aloud in 1-3 minutes
- response scoring after each answer
- next question only after the user responds

## score-report

Use when the user wants a scoring summary, practice review, or interview debrief.

Minimum deliverables:
- score summary
- dimension scores
- strongest answer point
- weakest dimensions
- likely interviewer concerns
- patch plan
- next 3 questions to practice

## resume

Use when the user wants career-facing output.

Minimum deliverables:
- repo brief
- 3-5 bilingual STAR-style bullets
- evidence note for each bullet when possible
- likely interviewer challenge for the top 1-3 bullets
- `metric to verify` suggestions
- "do not overclaim" note if the repo evidence is thin

## full-loop

Use when the user asks for R2I, a full analysis, or does not specify a mode.

Minimum deliverables:
- repo brief
- compact `study-doc`
- compact `prediction-pack`
- 1 starter mock question
- starter `score-report` rubric
- 3-5 bilingual resume bullets
- next step for deeper drill-down

## interview-journey

Use when the user wants a staged workflow instead of one isolated output.

Minimum deliverables:
- stage 1: `study-doc`
- stage 2: `prediction-pack`
- stage 3: `mock` or `spoken-mock` kickoff
- stage 4: `score-report` plan
- optional stage 5: `resume`

For very large repositories:
- return a `full-loop-lite` first
- summarize the system at a high level
- recommend 2-4 modules for deeper follow-up
