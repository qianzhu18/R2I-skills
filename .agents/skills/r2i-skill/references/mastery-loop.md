# Mastery Loop

This skill should not stop at "repo summary".

Its job is to help the user move through this loop:

`understand -> practice -> defend -> write`

## 1. Understand

Build a compact mental model of the repository:
- what problem the repo solves
- who it appears to serve
- what the main modules or flows are
- what technical decisions are visible from the codebase

This is the foundation. If this step is weak, every later step becomes vague.

## 2. Practice

Give the user a path to learn actively, not passively.

Good practice prompts:
- read these files in this order
- trace this request path end to end
- modify this feature safely
- implement this small extension
- explain why this module exists

Practice tasks should become slightly harder over time:
- level 1: reading and tracing
- level 2: modify behavior
- level 3: extend architecture or explain tradeoffs

## 3. Defend

Use the interviewer role here.

The interviewer should:
- ask the most likely follow-up question after each strong claim
- challenge vague ownership or business-value language
- expose where the user is relying on inference instead of proof
- force tradeoff explanations, not just feature descriptions

Examples:
- "Why did this architecture choice matter?"
- "How would you defend this bullet if I asked for evidence?"
- "What would break if this module were removed?"
- "What part of this impact is verified versus inferred?"

The goal is not to intimidate the user. The goal is to harden the story before it reaches the resume.

## 4. Write

Only after the story survives interviewer pressure should it become:
- a short project summary
- a 1-minute speaking script
- a bilingual STAR-style resume bullet

Each strong bullet should ideally map back to:
- repository evidence
- a plausible user or business value statement
- one likely interviewer challenge question

## Rule of Thumb

If the user cannot likely answer the interviewer follow-up, the bullet is not ready yet.
