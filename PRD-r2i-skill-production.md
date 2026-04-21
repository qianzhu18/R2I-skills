# R2I Skill Production PRD

Version: 0.9  
Updated: 2026-04-21  
Status: Draft for build  
Related files:
- Original draft: `R2Iprd.md`
- Research snapshot: `R2I-research-notes.md`
- Skill artifact: `.agents/skills/r2i-skill/`

## 1. Summary

R2I Skill is a repo-to-career-story agent skill. It turns a GitHub repository URL, local codebase, or current workspace into an evidence-backed learning path, interviewer-tested project narrative, interview prep pack, and resume-ready project story.

The product is not a web app. It is a portable agent skill designed to live inside skill-capable coding agents so users can reuse it across repeated repo analysis workflows with minimal setup.

## 2. Contacts

| Role | Name | Notes |
| --- | --- | --- |
| Product owner | Qian_zhu | Product direction and launch decision maker |
| PRD revision | Codex | Consolidated user/scenario/pain analysis and production framing |
| Primary users | Developers, students, job seekers | Initial launch audience |

## 3. Background

The draft PRD correctly identified a strong intuition: developers do not just want to "read a repo". They want to understand it well enough to learn from it, explain it in an interview, and convert it into resume value.

What the draft did not yet do well enough:
- It listed features before clarifying user segments and their top jobs-to-be-done.
- It treated all outputs as mandatory, which risks bloated answers and weak usability.
- It assumed broad platform support without differentiating maturity by host tool.
- It framed the market as if there were no adjacent competitors, which is no longer accurate.

Research completed on 2026-04-21 suggests the opportunity is real, but narrower and more specific than the draft implied:
- Repo-understanding tools exist, such as DeepWiki and DeepRepo.
- GitHub-to-resume tools exist, such as CodeToResume, SideprojectAI, and GitResume.
- Resume-to-interview Q&A tools exist, such as AskResume.
- Skills ecosystems now exist across Claude Code, Codex, Windsurf, and Cursor, but maturity differs by platform.

Therefore the production opportunity is not "another repo explainer" and not "another resume rewriter". It is an evidence-backed closed loop:

`repo understanding -> learning order -> interviewer challenge -> honest resume bullets`

## 4. Objective

### Product objective

Reduce the time between "I have a repository" and "I can explain this project confidently, survive follow-up questions, and write it up honestly" from hours to minutes.

### Why this matters

For users:
- They stop bouncing between code explanation tools, interview prep prompts, and resume rewriting tools.
- They get a reusable workflow instead of starting from scratch each time.
- They avoid fake-sounding bullet points that collapse under follow-up questioning.

For the product:
- A good skill is faster to ship, easier to share, and easier to iterate than a standalone app.
- A portable skill can ride the growth of agent ecosystems instead of competing as a separate SaaS from day one.

### Key results

The first public version should target:
- 70% of test users can get a usable first-pass repo brief within 3 minutes of invocation.
- 60% of test users say the generated interview script is usable after light edits.
- 50% of test users reuse at least one generated resume bullet after manual review.
- 0 fabricated quantitative impact claims in default output.
- First response stays compact enough to scan, even in `full-loop` mode.

## 5. Market Segments

### Primary segment

Job-seeking developers, students, and career switchers who want to convert side projects, internship work, or open-source repos into defensible interview and resume material.

### Secondary segments

Working developers preparing for interviews, promotion packets, or internal transfers.

Developers onboarding to unfamiliar open-source or team repositories and wanting a guided path to understanding.

### User / Scenario / Pain table

| User | Core scenario | Current pain | Why current alternatives fail |
| --- | --- | --- | --- |
| Job seeker / student | "I built or studied this repo, now I need to explain it in interviews." | Can talk about files, but not architecture, tradeoffs, or ownership. | Repo explainer tools rarely convert code context into interview language. |
| Job seeker / student | "I need bullet points for my resume." | Existing AI bullets sound inflated or generic. | Resume tools often overfit to writing polish and underfit to repo evidence. |
| Working developer | "I need to recover what matters from repos I touched months ago." | Remembers doing the work, but not the strongest proof or framing. | Git-history and resume tools help with recall, but not with codebase understanding. |
| New repo learner | "I want to actually understand this codebase." | Does not know where to start or which modules matter most. | Repo-summary products help with navigation, but not with deliberate practice or career framing. |

### Jobs-to-be-done

- When I find a promising repo, I want a fast map of how it works, so I can decide what to study.
- When I prepare for an interview, I want repo-specific questions and realistic follow-up pressure, so I can sound concrete.
- When I write my resume, I want evidence-backed bullet points, so I can stay honest and still sound strong.

## 6. Value Propositions

### Core value proposition

R2I Skill helps developers turn code repositories into defensible project stories they can learn, explain, and reuse.

### What is different

1. Closed-loop output

Most adjacent products specialize in one stage:
- understand the repo
- write resume bullets
- generate interview questions

R2I connects all three stages inside one reusable skill, with an interviewer lens acting as the bridge between learning and resume writing.

2. Evidence-first career translation

The system should not only sound smart. It should separate:
- facts supported by repo evidence
- reasonable inferences
- suggested framing
- metrics the user must verify

3. Mode-based usability

The original draft required every run to generate every section. Production behavior should be mode-based:
- quick scan
- learn
- interview
- resume
- full loop

This keeps first responses useful and avoids prompt bloat.

4. Skill-native distribution

The product can be shipped as a repository-native artifact with low ops cost and high shareability.

### Competitive positioning

R2I should position itself as:

"The evidence-backed repo-to-interview workflow for developers who want to understand a project deeply enough to talk about it and write it honestly."

It should not position itself as:
- a generic documentation generator
- an ATS keyword spinner
- a standalone SaaS dashboard in the first release

## 7. Solution

### 7.1 Product principles

1. Evidence before expression

Never let polished language outrun repository evidence.

2. User-intent before feature completeness

Generate only what the user needs in the current moment.

3. Interviewer pressure before final writing

Strong claims should be challenged before they become bullets.

4. Progressive depth

Large repos should first yield a high-level map, then deeper drill-downs.

5. Honest framing over hype

If the repo is small, incomplete, or tutorial-like, say so and frame it appropriately.

6. Portable by default

The skill should be packaged in an open, reusable format rather than locked to a web product.

### 7.2 User flow

1. User provides a repo URL, local path, or current repo context.
2. User intent is inferred or explicitly requested:
   - learn
   - interview
   - resume
   - full-loop
3. Skill reads top-level repository evidence and builds a first-pass repo brief.
4. Skill runs a compact mastery loop:
   - understand
   - learn
   - interviewer challenge
   - resume conversion
5. Skill generates mode-specific output.
6. User optionally drills into one module, one interview theme, or one resume variant.

### 7.3 Functional requirements

#### Input requirements

Must support:
- public GitHub repository URL
- local repository path
- current working repository

Should support:
- optional target role
- optional job description
- optional seniority level
- optional language preference

#### Output mode requirements

`quick-scan`
- Repo brief
- key modules or architecture shape
- standout files or folders
- likely interview-worthy highlights
- top uncertainties

`learn`
- Repo brief
- reading order
- key concepts or subsystems
- 3-5 practice tasks
- interviewer checkpoint questions
- what to ignore on first pass

`interview`
- Repo brief
- 10-15 repo-specific questions
- reference answers
- likely interviewer follow-up questions
- 1-minute and 3-minute explanation scripts

`resume`
- Repo brief
- 3-5 bilingual STAR-style bullets
- evidence note for each bullet when possible
- likely interviewer challenge for the strongest bullets
- suggested metrics marked as `metric to verify`
- anti-overclaim warning when evidence is thin

`full-loop`
- Repo brief
- compact learning path
- compact interview pack
- 3-5 bilingual resume bullets
- interviewer challenge checkpoints
- recommended next drill-down

#### Output format requirements

- Chinese first by default
- Resume bullets in Chinese and English
- Clear section headers
- High signal, low filler
- Mermaid diagram only when architecture is clear enough to justify it

#### Large-repo handling

When the repo is too large, too noisy, or too ambiguous for reliable deep analysis in one pass:
- produce a high-level architecture and priority map first
- identify the most promising modules to inspect next
- avoid pretending to have full certainty

#### Evidence and trust requirements

The skill must:
- distinguish fact from inference
- avoid fabricated business impact
- avoid fabricated team scope
- avoid fabricated performance or revenue metrics
- keep resume output interview-defensible

### 7.4 Technology and packaging

#### Canonical packaging

Ship the skill as a repository-native skill folder with supporting references.

Initial canonical path in this project:
- `.agents/skills/r2i-skill/`

Why:
- aligns with the open agent skill ecosystem
- works well for portable, versioned distribution
- is already discoverable by some tools directly and adaptable to others

#### Platform strategy

Launch priority:
1. Claude Code
2. OpenAI Codex
3. Windsurf
4. Cursor nightly / experimental

Reason:
- Skill support exists across these tools, but maturity and discovery behavior are not identical.
- Cursor skill support currently appears less mature than rules and is documented as nightly-only in the official blog post reviewed on 2026-04-21.

### 7.5 Non-functional requirements

- Low maintenance: no backend required for MVP
- Shareable: all core behavior lives in `SKILL.md` plus a small set of references
- Inspectable: users can audit the instructions
- Honest by design: no default fake metrics
- Compatible with iterative extension: later add job-description tailoring, commit-history ingestion, and export helpers

### 7.6 Assumptions

- The user has access to the repository they want analyzed.
- The host agent can read files in the repo and, when needed, browse public URLs.
- Users prefer a reusable skill workflow over repeated custom prompting.
- A strong MVP does not require quiz certificates or a web UI.

### 7.7 Risks and mitigations

| Risk | Why it matters | Mitigation |
| --- | --- | --- |
| Host tool fragmentation | Skills are supported differently across tools. | Publish a primary support matrix and avoid overclaiming "perfect compatibility". |
| Hallucinated resume impact | This destroys user trust immediately. | Enforce evidence labels and `metric to verify`. |
| Large repo overload | Full-loop output becomes shallow or noisy. | Use progressive disclosure and `full-loop-lite` behavior first. |
| Users want job-specific tailoring | Generic bullets may feel too broad. | Support optional job description in v1.1. |
| Private repo sensitivity | Some users will not want cloud analysis. | Keep the skill usable on local repos inside local agents. |

## 8. Release

### MVP scope

Include in MVP:
- repo brief
- learn mode
- interview mode
- resume mode
- full-loop mode
- evidence and honesty rules
- bilingual resume bullets
- local repo plus GitHub URL support

Do not include in MVP:
- standalone web app
- certificate generation
- multi-repo batch analysis
- automatic LinkedIn or DOCX export
- voice mock interview

### Post-MVP

Phase 2:
- job-description alignment
- commit and PR evidence support
- stronger architecture-diagram generation
- platform-specific packaging guides

Phase 3:
- mock interview workflow
- export templates
- repo comparison mode

### Release recommendation

Ship a narrow, credible first version built around the following promise:

"Drop in a repo and get a trustworthy path to learn it, explain it, and write it up."

That promise is clearer, more defensible, and more buildable than the original "everything in one pass" framing.
