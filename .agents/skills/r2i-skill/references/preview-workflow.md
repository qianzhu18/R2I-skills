# Preview Workflow

Use this file when the user wants to preview a `study-doc` inside Codex app or Claude Code through a local browser port.

## Goal

Do not stop at "I generated markdown in chat."

For `study-doc`, prefer a small local docs bundle over a single oversized markdown page.

When the user explicitly asks to preview the learning document:
1. save the `study-doc` content to local markdown files
2. run the preview server script
3. return the localhost URL

## Canonical Script

Use:

```bash
python3 ${SKILL_DIR}/scripts/serve_study_doc.py --input <markdown-file-or-docs-dir> --port 4173
```

If port `4173` is busy, try another local port such as `4174` or `4389`.

## File Convention

When possible, write the study doc as a docs bundle:

```text
.r2i-preview/<repo-slug>/study-doc/
  00-overview.md
  01-quick-start.md
  02-system-map.md
  03-key-flows.md
  04-reading-path.md
  05-checklist.md
  06-pitfalls-and-faq.md
```

Fallback:

```text
.r2i-preview/<repo-slug>/study-doc.md
```

Use the single-file fallback only when the user explicitly wants one file or the output is intentionally tiny.

## Preview Behavior

The preview should:
- render the markdown as a readable developer document site
- expose left-nav page switching when a docs directory is provided
- expose a per-page table of contents
- expose a localhost URL
- allow the user to reload after markdown changes

## Codex / Claude Code Guidance

If the host can run local shell commands, actually start the local server instead of merely describing it.

If the user asks for a browser preview and shell execution is available, prefer doing the work end to end:
- write the docs bundle or markdown file
- start the server
- report the URL

## When Not To Start The Server

Do not start a local preview server automatically for every `study-doc`.

Start it when:
- the user asks for preview
- the user asks for a local port
- the user is testing the skill end to end
