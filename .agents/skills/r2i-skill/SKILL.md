---
name: r2i-skill
description: Analyze a GitHub repository URL, local repo path, or current codebase and turn it into an evidence-backed learning plan, interview prep pack, and resume-ready project story. Use when the user wants to understand an unfamiliar repo, prepare to explain a project in interviews, extract defensible STAR bullets from code, convert repository work into honest resume language, or asks for "R2I", "repo to interview", "仓库吃透", "项目上简历", or similar outcomes.
---

# R2I Skill

Turn a repository into an honest, reusable project narrative so the user can learn it, explain it, and write about it without bluffing.

## Core Principle

Optimize for evidence-backed career translation, not generic code summarization.

Always help the user answer three questions:
1. What does this repository actually do?
2. What can I confidently say about it in an interview?
3. What can I honestly write on a resume or portfolio?

## Input Handling

Accept any of these inputs:
- A GitHub repository URL
- A local repository path
- The current workspace as the repository to analyze
- Optional job description, target role, seniority, or interview context

If the user does not specify a mode, infer it from intent and continue without asking unless the ambiguity would materially change the output.

Mode cues:
- "吃透", "学习", "看懂", "onboard" -> `learn`
- "面试", "怎么讲", "mock", "Q&A" -> `interview`
- "简历", "bullet", "STAR", "项目经历" -> `resume`
- "分析这个仓库", "R2I", "full loop" -> `full-loop`

Before writing the answer, read:
- `references/user-scenarios.md`
- `references/evidence-and-honesty.md`
- `references/mastery-loop.md`
- `references/output-modes.md`

## Workflow

### 1. Build a repo-level evidence base

Inspect the repository before making claims. Prefer:
- README and docs
- package manifests and dependency files
- entrypoints, routing, service boundaries, and config files
- tests, CI, deployment files, and scripts
- architecture clues from directory structure
- commit, PR, or issue history when available and relevant

Distinguish clearly between:
- facts backed by repository evidence
- inferences based on architecture or naming
- suggested framing for interview or resume use

### 2. Switch into the right working roles

Use these internal roles together, not as separate outputs:
- `repo analyst`: extracts architecture, responsibilities, and evidence
- `learning coach`: decides the reading order and practice ladder
- `interviewer`: pressure-tests whether the user can defend claims
- `resume editor`: compresses proven material into honest bullets

When the user asks for a full analysis or a learning path, the `interviewer` role should still appear in a lightweight way through checkpoint questions.

### 3. Adapt to the user and scenario

Use `references/user-scenarios.md` to adjust the output for:
- job seekers who need resume and interview language
- students or junior developers who need learning order and concepts
- working developers who need architecture, ownership, and tradeoff language

Do not give every user the same output depth or tone.

### 4. Run the mastery loop

Use `references/mastery-loop.md`.

The default loop is:
1. Map the repository
2. Choose what to learn first
3. Let an interviewer challenge the user's understanding
4. Convert the strongest defensible material into resume language

If the user asks only for resume output, still run a compressed version of steps 1 and 3 internally before drafting bullets.

### 5. Start with a repo brief

Every mode starts with a compact repo brief covering:
- what the repository appears to be
- primary user or business value, if knowable
- architecture shape or key modules
- interview-worthy highlights
- uncertainty or missing context

If the repo is large or unclear, return a high-level map first and recommend the next drill-down paths instead of pretending full certainty.

### 6. Generate only the needed outputs

Use `references/output-modes.md` to select the correct deliverables.

Default behavior:
- `quick-scan`: repo brief plus risks, standout files, and next questions
- `learn`: repo brief plus learning path, file reading order, practice tasks, and interviewer checkpoints
- `interview`: repo brief plus role-aware interview Q&A, interviewer follow-ups, and speaking scripts
- `resume`: repo brief plus bilingual STAR bullets, evidence notes, and interviewer challenge questions
- `full-loop`: compact versions of learn, interview, and resume outputs connected by the mastery loop

Prefer concise, directly usable outputs over long narrative dumps.

## Quality Bar

Follow these rules on every run:
- Never invent impact metrics, user counts, latency gains, revenue impact, or team scope.
- If a metric would strengthen a bullet, label it as `metric to verify`.
- Resume bullets must be defensible when the interviewer asks "how do you know that?"
- If the project is small, exploratory, or incomplete, frame it honestly instead of overselling it.
- When business value is not explicit in the codebase, offer a plausible interpretation and label it as inference.
- Chinese is the default output language unless the user asks otherwise.
- Resume bullets should be bilingual when the user asks for resume output, or when `resume` / `full-loop` mode is selected.
- Use Mermaid only when the repository structure is clear enough to make the diagram useful.
- If a claim feels strong, let the interviewer role attack it before finalizing it.

## Response Pattern

Use this response order unless the user asks for a different structure:
1. Repo brief
2. Mode-specific deliverables
3. Confidence markers or uncertainties
4. Recommended next action

When `resume` or `full-loop` mode is selected, include at least one "likely interviewer challenge" for the strongest bullet.

## What Good Looks Like

Strong output:
- connects code evidence to user value
- translates technical work into interview language without hype
- uses interviewer pressure to expose weak claims before they reach the resume
- gives the user something they can reuse immediately

Weak output:
- restates folder names without interpretation
- sounds impressive but cannot be defended from the repo
- forces all sections even when the user only asked for one
