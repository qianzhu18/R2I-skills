# Score Report

Use this file when generating `score-report` output after `mock` or `spoken-mock`.

## Goal

A score report should help the user improve their next answer, not just tell them they were bad.

## Score Dimensions

Evaluate each answer across these dimensions:
- clarity
- technical correctness
- system understanding
- evidence and honesty
- tradeoff awareness
- role fit
- communication confidence

If a dimension cannot be judged from the answer, say so briefly rather than pretending certainty.

## Report Structure

### 1. Score summary

Provide:
- overall score out of 5
- dimension scores
- one-line interpretation

### 2. Strongest part

State what the user did well:
- clear explanation
- good structure
- strong evidence
- concise tradeoff framing

### 3. Weakest part

State what weakened the answer:
- too vague
- overclaiming
- missing business value
- weak tradeoff explanation
- poor ownership framing

### 4. Likely interviewer concerns

Predict what the interviewer would worry about next.

Examples:
- "This sounds memorized, not understood."
- "You said the architecture was better, but you did not explain the tradeoff."
- "You claim impact, but I still do not know the evidence."

### 5. Upgrade version

Give the user a tighter version of the answer or a better answer structure.

Do not write a totally different personality. Keep it close enough to learn from.

### 6. Patch plan

End with:
- 3 things to improve
- next 3 highest-value questions to practice
- one suggested next mode: `prediction-pack`, `mock`, `spoken-mock`, or `resume`

## Scoring Tone

- Be direct, but not discouraging.
- Treat the score as a coaching tool.
- Focus on actionable improvement.
