R2I AI Agent Skill 开发 PRD（产品需求文档）版本：1.0
作者：Qian_zhu（产品提出人）
日期：2026年4月21日
状态：已完成（可直接交给开发/自己开发）
文档目的：明确把 R2I 做成一个 AI Agent Skill（而非 Web App）的完整需求，把 Skill 本身作为最终「作品」交付。Skill 发布后就是一个 GitHub 仓库，用户一键加载即可永久使用，实现「仓库 → 学习闭环 + 面试题 + 简历」全流程。1. 产品概述产品名称：R2I Skill（全称：Repo to Interview & Resume Skill）
中文名称：仓库吃透机 Skill / 项目上简历 Skill  一句话愿景：
做一个极简、可一键加载的 AI Agent Skill，用户在 Claude Code / Cursor 等工具里输入一行命令就能永久激活。之后只要丢一个 GitHub 仓库 URL，AI 自动输出完整学习闭环素材（教程 + 练习 + 面试题 + STAR 简历 bullet points），学完即可直接写进简历。核心价值：  比现有 Skill（DeepWiki、yupi-skill 等）更完整：一次性覆盖「学 + 练 + 说 + 简历」闭环。  
开发成本极低：只需一个 GitHub 仓库 + SKILL.md 文件即可上线。  
传播快：符合 2026 年 AI Skill 生态，可直接上 awesome-agent-skills 列表。

交付物（最终作品形式）：
一个公开 GitHub 仓库，包含：  SKILL.md（核心文件）  
README.md（使用说明）  
可选：prompts/ 文件夹（存放多 Agent Prompt 模板）  
examples/ 文件夹（示例输出）

2. 问题与机会用户痛点：  现有 Skill 只能生成文档或简历优化，无法一次性把 GitHub 仓库变成「可上简历」的完整项目经验。  
开发者想快速“吃透”一个仓库却不知道怎么讲、怎么写 bullet points。

市场机会：  目前没有 Skill 能完整实现 R2I 闭环（调研确认）。  
目标用户：每天使用 Claude/Cursor 的开发者、应届生、面试准备者（中文社区尤其欢迎）。

3. 目标用户 & 使用场景Primary User：Claude Code / Cursor 重度用户，想快速把开源/内部仓库转化为简历项目。
场景：  「用 R2I Skill 分析 https://github.com/vercel/next.js」  
AI 立即输出学习路径 + 面试题 + 简历 bullet points。

4. 产品目标Skill 加载后，100% 自动进入 R2I 模式。  
单次分析输出控制在 2000-4000 字以内，结构清晰。  
作为「作品」本身可写入简历：「开发 R2I AI Agent Skill，已帮助 X 名开发者把 GitHub 项目写进简历」。

5. 核心功能需求（Skill 行为规范）Skill 必须严格遵循以下规则，一旦触发立即执行：5.1 触发机制用户输入 GitHub 仓库 URL，或说出「用 R2I Skill 分析」「R2I 这个仓库」等关键词时激活。

5.2 核心输出模块（必须全部生成，按顺序）仓库解析总结（第一屏）  技术栈、核心架构、亮点/痛点（用 Mermaid 画架构图）。

结构化学习路径  分模块 Step-by-Step 教程 + 关键文件解释。

实践任务  3-5 个可 fork 完成的练习任务（含具体 PR 建议）。

面试题库（核心差异化）  15-20 道项目专属题（基础/中级/高级）。  
每题包含：题目 + 参考答案 + 追问 + 常见坑点。

简历闭环（杀手级功能）  3-5 条 STAR 格式 bullet points（中英双语）。  
可直接复制到简历。

掌握验证  10 道 Quiz 自测题。  
80% 通过后生成「掌握证书」Markdown 模板。

额外产出  项目讲述脚本（面试时怎么 1 分钟讲完）。  
量化贡献建议。

5.3 输出格式要求（严格遵守）第一行必须是： R2I Skill 已激活 | 仓库：{repo-name}  
使用 Markdown + 分隔线 + 标题层级。  
中文优先，简历 bullet points 提供中英双语。  
所有内容专业、量化、可直接上简历。  
结尾固定加：「学完后把这个项目写进简历，面试时直接用我生成的答案！」

5.4 规则 & 约束仓库太大时，先输出高层次总结，再询问用户想深入哪个模块。  
永远以「帮用户把项目吃透并成功上简历」为最高优先级。  
禁止废话，保持简洁有力。

6. 非功能需求文件结构：仅需 SKILL.md + README.md（保持极简）。  
兼容性：完美支持 Claude Code、Cursor、Windsurf 等支持 Skill 的工具。  
语言：默认中文输出，支持用户切换英文。  
可维护性：SKILL.md 内所有 Prompt 模块化，便于后期迭代。

7. MVP 范围（第一版交付）必须实现：  完整 7 大输出模块。  
中英双语简历 bullet points。  
严格的输出格式。

后续迭代（MVP 后）：  自动生成 Mermaid 架构图增强版。  
多仓库批量分析。  
语音 Mock Interview 提示词。

8. 技术实现要求（给开发/自己）整个 Skill 就是 纯 Markdown + 系统提示词，无需后端、无需部署。  
可使用多 Agent 思维（在 SKILL.md 里用 XML 标签拆分不同角色）。  
推荐仓库名：r2i-skill 或 repo-to-interview-resume-skill。

9. 发布与推广流程创建 GitHub 仓库，放入 SKILL.md + README.md。  
README 中写清楚加载命令：/skills add https://github.com/用户名/r2i-skill。  
发布后可提交到 awesome-agent-skills 列表。

10. 风险与假设风险：不同 AI 工具对 Skill 的解析程度不同 → 优先测试 Claude Code。  
假设：用户已安装支持 Skill 的 AI 工具。

下一步行动（建议立即执行）：  根据本 PRD 创建 GitHub 仓库。  
把 SKILL.md 内容填充进去（我之前给的版本已完全符合本 PRD，可直接使用）。  
测试 1-2 个仓库后发布。

这个 PRD 就是**专门为「把 R2I 做成 Skill 作品」**量身打造的。
现在你可以直接把这份 PRD + 我之前提供的 SKILL.md 一起发给任何人开发，或者自己 10 分钟就完成上线。需要我立刻补充「SKILL.md 最终完整版」还是「README.md 最终版」？或者调整任何优先级？直接说，我马上改！

