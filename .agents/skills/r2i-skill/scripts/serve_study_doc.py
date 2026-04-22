#!/usr/bin/env python3
"""Build and serve a local preview for an R2I study-doc markdown file or docs bundle."""

from __future__ import annotations

import argparse
import html
import http.server
import re
import socketserver
import sys
from dataclasses import dataclass
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
  --max: 1320px;
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
  font-size: clamp(30px, 5vw, 48px);
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
  grid-template-columns: 270px minmax(0, 1fr) 250px;
  gap: 22px;
  margin-top: 26px;
  align-items: start;
}

.nav,
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

.doc {
  background: var(--panel);
  border: 1px solid rgba(216, 205, 184, 0.72);
  border-radius: 24px;
  padding: 34px;
  box-shadow: var(--shadow);
}

.nav h2,
.toc h2 {
  margin: 0 0 14px;
  font: 700 15px/1.2 ui-sans-serif, system-ui, sans-serif;
  letter-spacing: 0.02em;
}

.nav-section,
.toc-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.nav a,
.toc a {
  color: var(--accent);
  text-decoration: none;
  font: 500 14px/1.45 ui-sans-serif, system-ui, sans-serif;
  border-radius: 12px;
  padding: 8px 10px;
}

.nav a.active {
  background: var(--accent-soft);
  color: #1d2b31;
  font-weight: 700;
}

.nav a:hover,
.toc a:hover {
  text-decoration: underline;
}

.doc h1,
.doc h2,
.doc h3,
.doc h4 {
  color: var(--ink);
  letter-spacing: -0.02em;
}

.doc h1 {
  font-size: 2.15rem;
  margin-top: 0;
  margin-bottom: 1rem;
}

.doc h2 {
  font-size: 1.6rem;
  margin-top: 2.5rem;
  margin-bottom: 0.8rem;
  border-bottom: 1px solid var(--line);
  padding-bottom: 0.45rem;
}

.doc h3 {
  font-size: 1.22rem;
  margin-top: 1.8rem;
  margin-bottom: 0.55rem;
}

.doc p,
.doc li,
.doc blockquote {
  font-size: 17px;
  line-height: 1.8;
}

.doc p { margin: 0.7rem 0 1rem; }
.doc ul,
.doc ol { padding-left: 1.4rem; }
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

@media (max-width: 1100px) {
  .layout { grid-template-columns: 1fr; }
  .nav,
  .toc { position: static; }
  .doc { padding: 24px 20px; }
}
"""


@dataclass
class PageInfo:
    source_path: Path
    output_name: str
    title: str
    headings: List[tuple[int, str, str]]


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", text.strip()).strip("-").lower()
    return slug or "section"


def prettify_stem(stem: str) -> str:
    stem = re.sub(r"^\d+[-_ ]*", "", stem)
    stem = stem.replace("-", " ").replace("_", " ").strip()
    return stem.title() if stem else "Untitled"


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
                    "<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>"
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
            if ordered_items:
                flush_lists()
            list_items.append(bullet_match.group(1).strip())
            continue

        ordered_match = re.match(r"^\d+\.\s+(.*)$", stripped)
        if ordered_match:
            flush_paragraph()
            if list_items:
                flush_lists()
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


def first_heading(markdown_text: str) -> str | None:
    headings = extract_headings(markdown_text)
    return headings[0][1] if headings else None


def discover_pages(input_path: Path) -> List[PageInfo]:
    if input_path.is_file():
        text = input_path.read_text(encoding="utf-8")
        return [
            PageInfo(
                source_path=input_path,
                output_name="index.html",
                title=first_heading(text) or prettify_stem(input_path.stem),
                headings=extract_headings(text),
            )
        ]

    markdown_files = sorted(
        path for path in input_path.iterdir() if path.is_file() and path.suffix.lower() == ".md"
    )
    pages: List[PageInfo] = []
    for idx, markdown_path in enumerate(markdown_files):
        text = markdown_path.read_text(encoding="utf-8")
        output_name = "index.html" if idx == 0 else f"{markdown_path.stem}.html"
        pages.append(
            PageInfo(
                source_path=markdown_path,
                output_name=output_name,
                title=first_heading(text) or prettify_stem(markdown_path.stem),
                headings=extract_headings(text),
            )
        )
    return pages


def build_html(page: PageInfo, pages: List[PageInfo], source_label: str, title: str | None = None) -> str:
    markdown_text = page.source_path.read_text(encoding="utf-8")
    body = render_markdown(markdown_text)
    doc_title = title or page.title

    page_links = "\n".join(
        f'<a href="{info.output_name}" class="{"active" if info.output_name == page.output_name else ""}">{html.escape(info.title)}</a>'
        for info in pages
    ) or '<span style="color: var(--muted); font: 500 14px/1.5 ui-sans-serif, system-ui, sans-serif;">No pages found.</span>'

    toc_items = "\n".join(
        f'<a href="#{anchor}" style="padding-left:{max(level - 1, 0) * 12}px">{html.escape(text)}</a>'
        for level, text, anchor in page.headings
    ) or '<span style="color: var(--muted); font: 500 14px/1.5 ui-sans-serif, system-ui, sans-serif;">No headings on this page.</span>'

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
      <p>这个本地端口现在会优先按多页学习文档来预览，结构更接近 onboarding docs / repo wiki，而不是把全部内容堆在一页里。</p>
      <div class="meta">
        <div class="pill">Source: {html.escape(source_label)}</div>
        <div class="pill">Current page: {html.escape(page.source_path.name)}</div>
      </div>
    </section>
    <div class="layout">
      <aside class="nav">
        <h2>学习路径</h2>
        <div class="nav-section">{page_links}</div>
      </aside>
      <article class="doc">{body}</article>
      <aside class="toc">
        <h2>本页目录</h2>
        <div class="toc-list">{toc_items}</div>
      </aside>
    </div>
    <div class="footer">R2I preview server · reload the page after updating the markdown source</div>
  </div>
</body>
</html>"""


def write_preview(input_path: Path, output_dir: Path, title: str | None = None) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    pages = discover_pages(input_path)
    if not pages:
        raise FileNotFoundError(f"No markdown pages found under {input_path}")

    source_label = str(input_path)
    for page in pages:
        html_path = output_dir / page.output_name
        html_path.write_text(build_html(page, pages, source_label, title=title), encoding="utf-8")
    return output_dir / "index.html"


class PreviewHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, directory: str, source_path: Path, title: str | None, **kwargs):
        self.source_path = source_path
        self.title = title
        super().__init__(*args, directory=directory, **kwargs)

    def do_GET(self) -> None:
        request_path = self.path.split("?", 1)[0]
        if request_path == "/" or request_path.endswith(".html"):
            write_preview(self.source_path, Path(self.directory), self.title)
        super().do_GET()

    def log_message(self, fmt: str, *args) -> None:
        sys.stdout.write("[preview] " + fmt % args + "\n")


def serve(input_path: Path, output_dir: Path, host: str, port: int, title: str | None) -> None:
    write_preview(input_path, output_dir, title)
    handler = lambda *args, **kwargs: PreviewHandler(
        *args,
        directory=str(output_dir),
        source_path=input_path,
        title=title,
        **kwargs,
    )
    with socketserver.TCPServer((host, port), handler) as httpd:
        url = f"http://{host}:{port}"
        print(f"Preview ready at {url}")
        print(f"Serving source: {input_path}")
        print("Press Ctrl+C to stop.")
        httpd.serve_forever()


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Serve a local preview for a study-doc markdown file or a docs bundle directory."
    )
    parser.add_argument("--input", required=True, help="Path to a markdown file or a directory of markdown pages.")
    parser.add_argument("--port", type=int, default=4173, help="Local port to serve on.")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind to. Default: 127.0.0.1")
    parser.add_argument("--title", help="Optional page title override.")
    parser.add_argument(
        "--output-dir",
        help="Directory to place generated preview assets. Default: .r2i-preview/<input-name>",
    )
    parser.add_argument(
        "--build-only",
        action="store_true",
        help="Build html files and exit without starting a server.",
    )
    return parser.parse_args(list(argv))


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)
    input_path = Path(args.input).expanduser().resolve()
    if not input_path.exists():
        print(f"Input path not found: {input_path}", file=sys.stderr)
        return 1

    output_dir = (
        Path(args.output_dir).expanduser().resolve()
        if args.output_dir
        else Path.cwd() / ".r2i-preview" / input_path.stem
    )

    if args.build_only:
        html_path = write_preview(input_path, output_dir, title=args.title)
        print(f"Preview built at {html_path}")
        return 0

    try:
        serve(input_path, output_dir, args.host, args.port, args.title)
    except KeyboardInterrupt:
        print("\nPreview server stopped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
