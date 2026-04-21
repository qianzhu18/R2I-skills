# Interview Engine

This file defines how to generate role-aware interview prep, predicted questions, and spoken mocks.

## Core Rule

The interview layer should test whether the user's repository story is:
- technically correct
- role appropriate
- defensible under follow-up
- concise enough to say aloud

## Question Categories

Always prioritize project-connected questions from these buckets:
- repository understanding
- architecture and module boundaries
- implementation detail
- tradeoffs and alternatives
- debugging and failure modes
- ownership and contribution framing
- impact and honesty checks

## Role Tailoring

### Frontend engineer

Emphasize:
- rendering flow
- component boundaries
- state management
- performance
- accessibility
- browser behavior
- API integration

### Backend engineer

Emphasize:
- API contracts
- data modeling
- concurrency
- consistency
- performance and scaling
- observability
- reliability
- security

### Full-stack engineer

Emphasize:
- end-to-end request flow
- backend/frontend boundaries
- auth and data flow
- integration tradeoffs
- delivery pragmatism

### AI / agent engineer

Emphasize:
- prompt and tool orchestration
- retrieval or context strategy
- evals and failure detection
- latency and cost tradeoffs
- hallucination control
- safety and trust

### Infrastructure / platform engineer

Emphasize:
- deployment
- CI/CD
- resilience
- observability
- environment management
- scaling and rollback

If the role is unclear, default to general software engineer framing and say so.

## Question Tiers

For `prediction-pack` or `interview` mode, organize questions into:

### 1. Must-answer

Questions the interviewer is very likely to ask and the user must handle cleanly.

### 2. Likely follow-up

Questions triggered by strong claims, especially around:
- architecture choices
- ownership
- performance
- impact

### 3. Killer questions

Questions that expose shallow understanding:
- "Why did this design choice matter?"
- "What tradeoff did you consciously accept?"
- "How do you know this bullet is true?"
- "What would break if this module failed?"

## Predicted Key Blockers

Every interview-heavy output should include a `predicted key blockers` section.

This should identify:
- the 3-5 most likely places the user gets stuck
- why an interviewer will push there
- how to patch the gap before the interview

Common blocker patterns:
- can describe implementation, but not tradeoffs
- can describe architecture, but not user value
- can describe repo, but not own contribution boundary
- has strong bullet wording, but weak evidence
- can answer broad questions, but freezes on specifics

## Spoken Mock Mode

`spoken-mock` is a voice-friendly mode, not a true audio system.

Use it when the user wants oral practice.

Behavior:
- ask exactly one spoken-style question at a time
- keep the question short enough to answer aloud in 1-3 minutes
- do not dump the answer key first
- wait for the user's answer or transcript
- then score the answer across:
  - clarity
  - technical depth
  - evidence
  - tradeoff awareness
  - role fit
- give one concrete improvement tip before the next question

If the host tool does not support microphone or native voice conversation, this is still useful because the user can answer aloud and then type a summary or transcript.

## Prediction Pack

`prediction-pack` is the "押题" mode.

It should include:
- high-frequency questions for the role
- repo-specific project questions
- likely follow-up questions for risky claims
- red-flag questions the user is currently underprepared for
- a short "fix first" study checklist

Prefer 12 sharp questions over 40 generic ones.

## Scoring Rubric

When evaluating answers in `mock` or `spoken-mock`, use a 5-point rubric:
- `5`: clear, accurate, evidence-backed, role-appropriate
- `4`: strong but missing one dimension
- `3`: understandable but shallow or vague
- `2`: weak, confused, or overclaiming
- `1`: incorrect, undefendable, or off-target

Use the score to coach, not to shame.
