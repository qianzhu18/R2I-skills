---
name: r2i-skill
description: Analyze a GitHub repository URL, local repo path, or current codebase and turn it into a development-doc-style learning pack, role-tailored interview prep pack, predicted interviewer questions, mock interview flow, score report, and resume-ready project story. Use when the user wants to understand an unfamiliar repo, prepare for interviews for a specific role, pressure-test project claims, extract defensible STAR bullets from code, convert repository work into honest resume language, or asks for "R2I", "repo to interview", "仓库吃透", "项目上简历", "押题", "模拟面试", "学习文档", or similar outcomes.
---

This is the Claude Code entrypoint for the shared R2I skill.

Use the repository-backed skill instructions and references below as the source of truth:
- `../../../.agents/skills/r2i-skill/SKILL.md`
- `../../../.agents/skills/r2i-skill/references/candidate-profile.md`
- `../../../.agents/skills/r2i-skill/references/learning-doc-playbook.md`
- `../../../.agents/skills/r2i-skill/references/user-scenarios.md`
- `../../../.agents/skills/r2i-skill/references/interview-engine.md`
- `../../../.agents/skills/r2i-skill/references/evidence-and-honesty.md`
- `../../../.agents/skills/r2i-skill/references/mastery-loop.md`
- `../../../.agents/skills/r2i-skill/references/output-modes.md`
- `../../../.agents/skills/r2i-skill/references/preview-workflow.md`
- `../../../.agents/skills/r2i-skill/references/score-report.md`

When invoked in Claude Code:
1. Read the shared files above first.
2. Follow the shared `.agents/skills/r2i-skill/SKILL.md` instructions.
3. Treat this wrapper as compatibility glue only.
