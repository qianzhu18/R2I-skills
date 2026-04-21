---
name: r2i-skill
description: Analyze a GitHub repository URL, local repo path, or current codebase and turn it into an evidence-backed learning plan, role-tailored interview prep pack, predicted interviewer questions, and resume-ready project story. Use when the user wants to understand an unfamiliar repo, prepare for interviews for a specific role, pressure-test project claims, extract defensible STAR bullets from code, convert repository work into honest resume language, or asks for "R2I", "repo to interview", "仓库吃透", "项目上简历", "押题", "模拟面试", or similar outcomes.
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
- Optional job description, target role, seniority, candidate background, or interview context

For interview-quality output, strongly prefer these optional user inputs:
- `target role`: frontend engineer, backend engineer, full-stack engineer, AI engineer, agent engineer, infra engineer, etc.
- `target level`: intern, junior, mid, senior, staff
- `candidate background`: years of experience, education, prior work, strongest stack
- `repo relationship`: built it, contributed to it, studied it, cloned it for learning
- `target company style`: startup, big tech, outsourcing, product company, research team
- `weak spots`: system design, performance, tradeoffs, project depth, collaboration, metrics
- `language`: Chinese, English, or bilingual

If these are missing, infer a reasonable default and state the assumptions in interview-oriented output.

If the user does not specify a mode, infer it from intent and continue without asking unless the ambiguity would materially change the output.

Mode cues:
- "吃透", "学习", "看懂", "onboard" -> `learn`
- "面试", "怎么讲", "mock", "Q&A" -> `interview`
- "模拟面试", "口语面试", "一问一答", "spoken mock" -> `spoken-mock`
- "押题", "高频题", "关键卡点", "prediction" -> `prediction-pack`
- "简历", "bullet", "STAR", "项目经历" -> `resume`
- "分析这个仓库", "R2I", "full loop" -> `full-loop`

Before writing the answer, read:
- `references/candidate-profile.md`
- `references/user-scenarios.md`
- `references/interview-engine.md`
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

Use `references/candidate-profile.md` to build a lightweight candidate profile before producing interview or resume output.

Use `references/user-scenarios.md` to adjust the output for:
- job seekers who need resume and interview language
- students or junior developers who need learning order and concepts
- working developers who need architecture, ownership, and tradeoff language

Do not give every user the same output depth or tone.

### 4. Tailor the interview layer

Use `references/interview-engine.md`.

Questions must be tailored to:
- target role
- target level
- repository shape
- candidate background
- likely interviewer style

Always produce a "predicted key blockers" view for interview-oriented work:
- what the interviewer is most likely to press on
- what the user can probably answer
- what claims are still weak or risky

### 5. Run the mastery loop

Use `references/mastery-loop.md`.

The default loop is:
1. Map the repository
2. Choose what to learn first
3. Let an interviewer challenge the user's understanding
4. Convert the strongest defensible material into resume language

If the user asks only for resume output, still run a compressed version of steps 1 and 3 internally before drafting bullets.

### 6. Start with a repo brief

Every mode starts with a compact repo brief covering:
- what the repository appears to be
- primary user or business value, if knowable
- architecture shape or key modules
- interview-worthy highlights
- uncertainty or missing context

If the repo is large or unclear, return a high-level map first and recommend the next drill-down paths instead of pretending full certainty.

### 7. Generate only the needed outputs

Use `references/output-modes.md` to select the correct deliverables.

Default behavior:
- `quick-scan`: repo brief plus risks, standout files, and next questions
- `learn`: repo brief plus learning path, file reading order, practice tasks, and interviewer checkpoints
- `interview`: repo brief plus role-aware interview Q&A, interviewer follow-ups, and speaking scripts
- `prediction-pack`: role-aware predicted questions, key blockers, must-know topics, and red flags
- `mock`: interactive one-question-at-a-time interview with feedback after each answer
- `spoken-mock`: oral-style mock interview optimized for speaking practice, not long text dumps
- `resume`: repo brief plus bilingual STAR bullets, evidence notes, and interviewer challenge questions
- `full-loop`: compact versions of learn, interview, and resume outputs connected by the mastery loop

Prefer concise, directly usable outputs over long narrative dumps.

For `mock` and `spoken-mock`:
- ask one question at a time
- wait for the user's answer before continuing
- do not dump the entire answer key first
- after each answer, score the response and then ask the next question
- if the user only wants the question list, switch to `prediction-pack`

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
- Prioritize the most likely interview traps over sheer question quantity.
- Tailor question difficulty to the target level; do not ask staff-level architecture questions to an intern by default.
- If true voice interaction is unavailable in the host tool, run `spoken-mock` as a text-guided oral practice mode.

## Response Pattern

Use this response order unless the user asks for a different structure:
1. Repo brief
2. Mode-specific deliverables
3. Confidence markers or uncertainties
4. Recommended next action

When `resume` or `full-loop` mode is selected, include at least one "likely interviewer challenge" for the strongest bullet.

When `mock` or `spoken-mock` mode is selected:
1. State the inferred or provided candidate profile
2. Ask exactly one question
3. Wait

When `prediction-pack` mode is selected, include:
1. likely high-frequency questions
2. predicted key blockers
3. red-flag follow-ups
4. topics to patch before the interview

## What Good Looks Like

Strong output:
- connects code evidence to user value
- translates technical work into interview language without hype
- uses interviewer pressure to expose weak claims before they reach the resume
- adapts the question set to the target role and candidate reality
- identifies the likely choke points before the interviewer does
- gives the user something they can reuse immediately

Weak output:
- restates folder names without interpretation
- sounds impressive but cannot be defended from the repo
- asks generic LeetCode-style questions disconnected from the project and role
- forces all sections even when the user only asked for one
