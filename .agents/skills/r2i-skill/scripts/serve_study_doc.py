#!/usr/bin/env python3
"""Build and serve a local preview for an R2I study-doc markdown file."""

from __future__ import annotations

import argparse
import html
import http.server
import os
import re
import socketserver
import sys
from pathlib import Path
from typing import Iterable, List


CSS = """
:root {
  --bg: #f6f1e7;
  --panel: #fffdf8;
  --ink: #182025;
  --muted: #58636f;
  --line: #d8cdb8;
  --accent: #1f4b57;
  --accent-soft: #dfecef;
  --code: #f3ede2;
  --shadow: 0 20px 40px rgba(27, 39, 45, 0.08);
  --max: 1180px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Georgia, serif;
  color: var(--ink);
  background:
    radial-gradient(circle at top left, rgba(31, 75, 87, 0.08), transparent 28rem),
    linear-gradient(180deg, #f7f2e9, #f1ecdf 48%, #f6f1e7);
}

.shell {
  max-width: var(--max);
  margin: 0 auto;
  padding: 32px 20px 56px;
}

.hero {
  background: linear-gradient(135deg, rgba(31, 75, 87, 0.96), rgba(24, 32, 37, 0.92));
  color: #f9f7f1;
  border-radius: 24px;
  padding: 28px 30px;
  box-shadow: var(--shadow);
}

.eyebrow {
  font: 600 12px/1.2 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: rgba(249, 247, 241, 0.72);
  margin-bottom: 12px;
}

.hero h1 {
  margin: 0 0 12px;
  font-size: clamp(32px, 5vw, 52px);
  line-height: 1.05;
  letter-spacing: -0.03em;
}

.hero p {
  margin: 0;
  max-width: 58rem;
  color: rgba(249, 247, 241, 0.82);
  font-size: 17px;
  line-height: 1.65;
}

.meta {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 18px;
}

.pill {
  padding: 8px 12px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.12);
  color: #f9f7f1;
  font: 500 13px/1.2 ui-sans-serif, system-ui, sans-serif;
}

.layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 270px;
  gap: 24px;
  margin-top: 26px;
  align-items: start;
}

.doc {
  background: var(--panel);
  border: 1px solid rgba(216, 205, 184, 0.72);
  border-radius: 24px;
  padding: 34px;
  box-shadow: var(--shadow);
}

.toc {
  position: sticky;
  top: 20px;
  background: rgba(255, 253, 248, 0.82);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(216, 205, 184, 0.72);
  border-radius: 22px;
  padding: 20px;
  box-shadow: var(--shadow);
}

.toc h2 {
  margin: 0 0 14px;
  font: 700 15px/1.2 ui-sans-serif, system-ui, sans-serif;
  letter-spacing: 0.02em;
}

.toc-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.toc a {
  color: var(--accent);
  text-decoration: none;
  font: 500 14px/1.45 ui-sans-serif, system-ui, sans-serif;
}

.toc a:hover { text-decoration: underline; }

.doc h1, .doc h2, .doc h3, .doc h4 {
  color: var(--ink);
  letter-spacing: -0.02em;
}

.doc h1 {
  font-size: 2.2rem;
  margin-top: 0;
  margin-bottom: 1rem;
}

.doc h2 {
  font-size: 1.6rem;
  margin-top: 2.8rem;
  margin-bottom: 0.8rem;
  border-bottom: 1px solid var(--line);
  padding-bottom: 0.45rem;
}

.doc h3 {
  font-size: 1.25rem;
  margin-top: 2rem;
  margin-bottom: 0.55rem;
}

.doc p, .doc li, .doc blockquote {
  font-size: 17px;
  line-height: 1.8;
}

.doc p { margin: 0.7rem 0 1rem; }
.doc ul, .doc ol { padding-left: 1.4rem; }
.doc li { margin: 0.25rem 0; }

.doc blockquote {
  margin: 1.3rem 0;
  padding: 0.15rem 1rem;
  border-left: 4px solid var(--accent);
  background: var(--accent-soft);
  color: #24323a;
  border-radius: 8px;
}

.doc code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  background: var(--code);
  padding: 0.14rem 0.34rem;
  border-radius: 5px;
  font-size: 0.92em;
}

.doc pre {
  background: #1b252a;
  color: #f7f7f4;
  padding: 18px;
  border-radius: 16px;
  overflow-x: auto;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.06);
}

.doc pre code {
  background: transparent;
  color: inherit;
  padding: 0;
}

.footer {
  margin-top: 30px;
  color: var(--muted);
  font: 500 13px/1.5 ui-sans-serif, system-ui, sans-serif;
  text-align: center;
}

@media (max-width: 980px) {
  .layout { grid-template-columns: 1fr; }
  .toc { position: static; order: -1; }
  .doc { padding: 24px 20px; }
}
"""


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", text.strip()).strip("-").lower()
    return slug or "section"


def apply_inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text


def render_markdown(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    blocks: List[str] = []
    paragraph: List[str] = []
    list_items: List[str] = []
    ordered_items: List[str] = []
    in_code = False
    code_lines: List[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            blocks.append(f"<p>{apply_inline(' '.join(paragraph).strip())}</p>")
            paragraph = []

    def flush_lists() -> None:
        nonlocal list_items, ordered_items
        if list_items:
            items = "".join(f"<li>{apply_inline(item)}</li>" for item in list_items)
            blocks.append(f"<ul>{items}</ul>")
            list_items = []
        if ordered_items:
            items = "".join(f"<li>{apply_inline(item)}</li>" for item in ordered_items)
            blocks.append(f"<ol>{items}</ol>")
            ordered_items = []

    for raw_line in lines:
        line = raw_line.rstrip("\n")
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_paragraph()
            flush_lists()
            if in_code:
                blocks.append(
                    "<pre><code>"
                    + html.escape("\n".join(code_lines))
                    + "</code></pre>"
                )
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not stripped:
            flush_paragraph()
            flush_lists()
            continue

        if stripped.startswith("> "):
            flush_paragraph()
            flush_lists()
            blocks.append(f"<blockquote><p>{apply_inline(stripped[2:].strip())}</p></blockquote>")
            continue

        heading_match = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if heading_match:
            flush_paragraph()
            flush_lists()
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            anchor = slugify(title)
            blocks.append(f'<h{level} id="{anchor}">{apply_inline(title)}</h{level}>')
            continue

        bullet_match = re.match(r"^[-*]\s+(.*)$", stripped)
        if bullet_match:
            flush_paragraph()
            flush_lists() if ordered_items else None
            list_items.append(bullet_match.group(1).strip())
            continue

        ordered_match = re.match(r"^\d+\.\s+(.*)$", stripped)
        if ordered_match:
            flush_paragraph()
            flush_lists() if list_items else None
            ordered_items.append(ordered_match.group(1).strip())
            continue

        paragraph.append(stripped)

    flush_paragraph()
    flush_lists()

    if in_code:
        blocks.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")

    return "\n".join(blocks)


def extract_headings(markdown_text: str) -> List[tuple[int, str, str]]:
    headings: List[tuple[int, str, str]] = []
    for line in markdown_text.splitlines():
        match = re.match(r"^(#{1,4})\s+(.*)$", line.strip())
        if not match:
            continue
        level = len(match.group(1))
        title = match.group(2).strip()
        headings.append((level, title, slugify(title)))
    return headings


def build_html(markdown_path: Path, title: str | None = None) -> str:
    markdown_text = markdown_path.read_text(encoding="utf-8")
    body = render_markdown(markdown_text)
    doc_title = title or markdown_path.stem.replace("-", " ").replace("_", " ")
    headings = extract_headings(markdown_text)
    toc_items = "\n".join(
        f'<a href="#{anchor}" style="padding-left:{max(level - 1, 0) * 12}px">{html.escape(text)}</a>'
        for level, text, anchor in headings
    ) or '<span style="color: var(--muted); font: 500 14px/1.5 ui-sans-serif, system-ui, sans-serif;">No headings yet.</span>'

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(doc_title)} | R2I Study Doc Preview</title>
  <style>{CSS}</style>
</head>
<body>
  <div class="shell">
    <section class="hero">
      <div class="eyebrow">R2I Study Doc Preview</div>
      <h1>{html.escape(doc_title)}</h1>
      <p>本地预览端口已经启动。这个页面用于在 Codex / Claude Code 工作流里快速浏览学习文档、检查结构、继续进入押题和模拟面试阶段。</p>
      <div class="meta">
        <div class="pill">Source: {html.escape(str(markdown_path))}</div>
        <div class="pill">Auto-refresh on reload</div>
      </div>
    </section>
    <div class="layout">
      <article class="doc">{body}</article>
      <aside class="toc">
        <h2>目录</h2>
        <div class="toc-list">{toc_items}</div>
      </aside>
    </div>
    <div class="footer">R2I preview server · reload the page after updating the markdown source</div>
  </div>
</body>
</html>"""


def write_preview(markdown_path: Path, output_dir: Path, title: str | None = None) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    html_path = output_dir / "index.html"
    html_path.write_text(build_html(markdown_path, title=title), encoding="utf-8")
    return html_path


class PreviewHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, directory: str, markdown_path: Path, title: str | None, **kwargs):
        self.markdown_path = markdown_path
        self.title = title
        super().__init__(*args, directory=directory, **kwargs)

    def do_GET(self) -> None:
        if self.path in {"/", "/index.html"}:
            write_preview(self.markdown_path, Path(self.directory), self.title)
        super().do_GET()

    def log_message(self, fmt: str, *args) -> None:
        sys.stdout.write("[preview] " + fmt % args + "\n")


def serve(markdown_path: Path, output_dir: Path, host: str, port: int, title: str | None) -> None:
    write_preview(markdown_path, output_dir, title)
    handler = lambda *args, **kwargs: PreviewHandler(
        *args,
        directory=str(output_dir),
        markdown_path=markdown_path,
        title=title,
        **kwargs,
    )
    with socketserver.TCPServer((host, port), handler) as httpd:
        url = f"http://{host}:{port}"
        print(f"Preview ready at {url}")
        print(f"Serving markdown source: {markdown_path}")
        print("Press Ctrl+C to stop.")
        httpd.serve_forever()


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Serve a local preview for a study-doc markdown file.")
    parser.add_argument("--input", required=True, help="Path to the markdown file to preview.")
    parser.add_argument("--port", type=int, default=4173, help="Local port to serve on.")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind to. Default: 127.0.0.1")
    parser.add_argument("--title", help="Optional page title override.")
    parser.add_argument(
        "--output-dir",
        help="Directory to place generated preview assets. Default: .r2i-preview/<markdown-stem>",
    )
    parser.add_argument(
        "--build-only",
        action="store_true",
        help="Build index.html and exit without starting a server.",
    )
    return parser.parse_args(list(argv))


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)
    markdown_path = Path(args.input).expanduser().resolve()
    if not markdown_path.exists():
        print(f"Markdown file not found: {markdown_path}", file=sys.stderr)
        return 1

    output_dir = (
        Path(args.output_dir).expanduser().resolve()
        if args.output_dir
        else Path.cwd() / ".r2i-preview" / markdown_path.stem
    )

    if args.build_only:
        html_path = write_preview(markdown_path, output_dir, title=args.title)
        print(f"Preview built at {html_path}")
        return 0

    try:
        serve(markdown_path, output_dir, args.host, args.port, args.title)
    except KeyboardInterrupt:
        print("\nPreview server stopped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
