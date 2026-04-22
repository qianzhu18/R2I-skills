# Preview Workflow

Use this file when the user wants to preview a `study-doc` inside Codex app or Claude Code through a local browser port.

## Goal

Do not stop at "I generated markdown in chat."

When the user explicitly asks to preview the learning document:
1. save the `study-doc` content to a local markdown file
2. run the preview server script
3. return the localhost URL

## Canonical Script

Use:

```bash
python3 ${SKILL_DIR}/scripts/serve_study_doc.py --input <markdown-file> --port 4173
```

If port `4173` is busy, try another local port such as `4174` or `4389`.

## File Convention

When possible, write the markdown study doc to:

```text
.r2i-preview/<repo-slug>/study-doc.md
```

This keeps preview artifacts local and easy to regenerate.

## Preview Behavior

The preview should:
- render the markdown as a readable developer document
- expose a localhost URL
- allow the user to reload after markdown changes

## Codex / Claude Code Guidance

If the host can run local shell commands, actually start the local server instead of merely describing it.

If the user asks for a browser preview and shell execution is available, prefer doing the work end to end:
- write the markdown file
- start the server
- report the URL

## When Not To Start The Server

Do not start a local preview server automatically for every `study-doc`.

Start it when:
- the user asks for preview
- the user asks for a local port
- the user is testing the skill end to end
