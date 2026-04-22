#!/usr/bin/env python3
"""Validate that a study-doc bundle meets the R2I baseline structure."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable


EXPECTED_PAGES = [
    "00-overview.md",
    "01-quick-start.md",
    "02-system-map.md",
    "03-key-flows.md",
    "04-reading-path.md",
    "05-checklist.md",
    "06-pitfalls-and-faq.md",
]


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate an R2I study-doc markdown file or docs bundle directory."
    )
    parser.add_argument("--input", required=True, help="Path to a study-doc file or docs bundle directory.")
    return parser.parse_args(list(argv))


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").lower()


def has_any(text: str, needles: list[str]) -> bool:
    return any(needle in text for needle in needles)


def add_issue(issues: list[str], kind: str, message: str) -> None:
    issues.append(f"[{kind}] {message}")


def validate_bundle(bundle_path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    missing = [name for name in EXPECTED_PAGES if not (bundle_path / name).exists()]
    for name in missing:
        add_issue(errors, "error", f"missing canonical page: {name}")

    if missing:
        return errors, warnings

    overview = load_text(bundle_path / "00-overview.md")
    quick_start = load_text(bundle_path / "01-quick-start.md")
    system_map = load_text(bundle_path / "02-system-map.md")
    key_flows = load_text(bundle_path / "03-key-flows.md")
    reading_path = load_text(bundle_path / "04-reading-path.md")
    checklist = load_text(bundle_path / "05-checklist.md")
    pitfalls = load_text(bundle_path / "06-pitfalls-and-faq.md")

    if not has_any(overview, ["confidence", "high confidence", "lower confidence", "uncertainty"]):
        add_issue(warnings, "warn", "overview does not clearly signal confidence or uncertainty")

    if not has_any(overview, ["track", "learner", "contributor", "interviewer"]):
        add_issue(warnings, "warn", "overview does not expose learning tracks")

    if not has_any(quick_start, ["success signal", "healthy if", "working", "pass", "port"]):
        add_issue(errors, "error", "quick-start is missing a concrete success signal")

    if not has_any(system_map, ["source of truth", "source-of-truth", "generated", "secondary", "artifact"]):
        add_issue(errors, "error", "system-map does not distinguish source-of-truth from generated or secondary material")

    if not has_any(key_flows, ["workflow", "flow", "drill-down"]):
        add_issue(warnings, "warn", "key-flows page may be missing workflow or drill-down language")

    if not has_any(reading_path, ["ignore", "defer", "first pass"]):
        add_issue(warnings, "warn", "reading-path should say what to ignore or defer on first pass")

    if not has_any(reading_path, ["learner lane", "contributor lane", "interviewer lane"]):
        add_issue(warnings, "warn", "reading-path is missing one or more recommended lanes")

    if not has_any(checklist, ["checkpoint questions", "practice tasks"]):
        add_issue(errors, "error", "checklist must include checkpoint questions and practice tasks")

    if not has_any(checklist, ["safe change", "safe change ideas"]):
        add_issue(warnings, "warn", "checklist should include at least one first safe change idea")

    if not has_any(pitfalls, ["misread", "trap", "wrong", "avoid"]):
        add_issue(warnings, "warn", "pitfalls page may be too weak on misreads or traps")

    if not has_any(pitfalls, ["generated", "secondary", "artifact", "edit target"]):
        add_issue(warnings, "warn", "pitfalls page should warn about generated or secondary files")

    return errors, warnings


def validate_single_file(file_path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = load_text(file_path)

    required_topics = [
        "overview",
        "quick start",
        "system map",
        "key flows",
        "reading path",
        "checklist",
        "pitfalls",
    ]
    for topic in required_topics:
        if topic not in text:
            add_issue(warnings, "warn", f"single-file study-doc may be missing topic: {topic}")

    heading_count = text.count("\n#") + text.count("\n##")
    if heading_count < 8:
        add_issue(warnings, "warn", "single-file study-doc looks thin; expected a richer onboarding-style structure")

    if "success signal" not in text and "healthy if" not in text:
        add_issue(errors, "error", "single-file study-doc is missing a success signal")

    return errors, warnings


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)
    input_path = Path(args.input).expanduser().resolve()
    if not input_path.exists():
        print(f"[error] input path not found: {input_path}", file=sys.stderr)
        return 1

    if input_path.is_dir():
        errors, warnings = validate_bundle(input_path)
    else:
        errors, warnings = validate_single_file(input_path)

    for issue in warnings:
        print(issue)
    for issue in errors:
        print(issue)

    if errors:
        print("Study-doc verification failed.")
        return 1

    if warnings:
        print("Study-doc verification passed with warnings.")
    else:
        print("Study-doc verification passed.")
    return 0
