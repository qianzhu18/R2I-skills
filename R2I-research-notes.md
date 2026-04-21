# R2I Research Notes

Date: 2026-04-21  
Purpose: Validate the production direction of `R2I Skill` before rewriting the draft PRD.

## 1. Key findings

### 1.1 Skill ecosystems are real, but maturity differs by host

What the draft got right:
- Skills are now a meaningful distribution format for coding agents.

What needed correction:
- "Perfect support" across all target tools is too strong.

Current snapshot:
- Claude Code officially documents skills as following the Agent Skills open standard and supports personal and project skill directories.
- OpenAI Codex officially positions skills as a core part of the product across app, CLI, and IDE surfaces.
- Windsurf officially documents skills, including `.windsurf/skills/` and cross-agent discovery from `.agents/skills/`.
- Cursor officially discusses both Rules and Skills, but its blog notes Agent Skills are currently only available in the nightly release channel.

Implication for PRD:
- Launch with a platform priority order, not a blanket compatibility claim.

### 1.2 The market is already split across adjacent categories

Repo understanding:
- DeepWiki focuses on docs, diagrams, and codebase Q&A.
- DeepRepo focuses on architecture visualization, AI chat, and repo analysis.

Resume generation:
- CodeToResume turns GitHub projects into bullet points.
- SideprojectAI turns repositories into resume sections.
- GitResume focuses on turning commits and PRs into evidence-backed bullet points.

Interview preparation:
- AskResume generates interview questions and answers from resume input.

Implication for PRD:
- It is no longer credible to say "there is no competition".
- The stronger claim is: no obvious direct competitor was found in this quick scan that combines repo understanding, learning order, interview rehearsal, and evidence-backed resume bullets as a reusable skill artifact.

### 1.3 The best wedge is not "more features"

The draft overloaded the MVP with:
- always-on seven-module output
- quiz
- certificate
- enhanced diagrams

This is risky because:
- first responses become long and shallow
- users often want only one mode at a time
- trust matters more than novelty in career-facing output

Implication for PRD:
- use mode-based output instead of one mandatory giant answer
- keep "evidence and honesty" as the core differentiator

## 2. PRD-level changes recommended

1. Reframe the product around three anchors:
- user
- scenario
- pain

2. Change positioning from:
- "no competitors"

to:
- "adjacent tools exist, but the closed loop is still underserved"

3. Change the MVP from:
- "always output everything"

to:
- "infer the right mode and keep first response compact"

4. Add trust guardrails:
- fact vs inference
- evidence notes
- `metric to verify`

5. Expand supported input beyond GitHub URL:
- local repo path
- current workspace

## 3. Sources reviewed

Platform / ecosystem:
- Claude Code skills docs: [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)
- Agent Skills quickstart: [agentskills.io/skill-creation/quickstart](https://agentskills.io/skill-creation/quickstart)
- Codex product page: [openai.com/codex](https://openai.com/codex/)
- Codex app launch post: [openai.com/index/introducing-the-codex-app](https://openai.com/index/introducing-the-codex-app/)
- Codex help center overview: [help.openai.com/en/articles/11369540-codex-in-chatgpt](https://help.openai.com/en/articles/11369540-codex-in-chatgpt)
- Cursor best practices blog: [cursor.com/blog/agent-best-practices](https://cursor.com/blog/agent-best-practices)
- Cursor rules docs search result: [docs.cursor.com/context/rules-for-ai](https://docs.cursor.com/context/rules-for-ai)
- Windsurf skills docs: [docs.windsurf.com/windsurf/cascade/skills](https://docs.windsurf.com/windsurf/cascade/skills)
- Windsurf memories/rules docs: [docs.windsurf.com/windsurf/cascade/memories](https://docs.windsurf.com/windsurf/cascade/memories)

Adjacent products:
- DeepWiki docs: [docs.devin.ai/work-with-devin/deepwiki](https://docs.devin.ai/work-with-devin/deepwiki)
- DeepRepo: [deeprepo.dev](https://deeprepo.dev/)
- CodeToResume: [codetoresume.com](https://codetoresume.com/)
- SideprojectAI: [usesideprojectai.com](https://usesideprojectai.com/)
- GitResume: [gitresume.ai](https://gitresume.ai/)
- AskResume repo: [github.com/ask-resume/ask-resume-front](https://github.com/ask-resume/ask-resume-front)

## 4. Bottom line

The product direction is worth pursuing, but the winning version is narrower and sharper than the original draft:

- not "all-in-one content blast"
- not "another repo explainer"
- not "another resume rewriter"

It should be:

"an evidence-backed repo-to-interview skill that helps users learn, explain, and write about real projects without bluffing."
