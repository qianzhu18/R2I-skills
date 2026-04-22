# Study Doc Production

Use this file when producing or reviewing a `study-doc` intended for repeated use, local preview, or example storage.

## Production Standard

A production-ready `study-doc` should be:

- stable enough to preview repeatedly
- specific enough to teach a repository
- constrained enough to avoid AI-summary drift
- honest enough to survive interviewer pushback

## Minimum Bundle

Prefer this page set:

1. `00-overview.md`
2. `01-quick-start.md`
3. `02-system-map.md`
4. `03-key-flows.md`
5. `04-reading-path.md`
6. `05-checklist.md`
7. `06-pitfalls-and-faq.md`

## Production Checks

Before treating a bundle as "good enough", confirm:

- `01-quick-start` contains a concrete success signal
- `02-system-map` distinguishes source-of-truth from generated or secondary material
- `04-reading-path` reduces overwhelm rather than listing every interesting file
- `05-checklist` includes checkpoint questions and safe exercises
- `06-pitfalls-and-faq` protects against common misreads and overclaiming

## Failure Modes

Common bad outputs:

- one long essay pretending to be docs
- paraphrased folder names with no learning path
- architecture claims without file anchors
- setup advice without a way to tell whether it worked
- resume-style hype leaking into learning docs

## Storage Guidance

If the user wants reusable preview artifacts, save the markdown source first.

Do not treat rendered HTML as the source of truth.
