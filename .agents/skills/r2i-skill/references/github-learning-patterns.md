# GitHub Learning Patterns

Use this file when shaping `study-doc` output so it feels closer to real GitHub onboarding material instead of an isolated AI summary.

## Why This Exists

The best repository learning docs are usually not one long explanation.

They are stitched from a few stable GitHub-native patterns:
- a quick path to run or verify the project
- a high-level map of the repository
- separate lanes for architecture, contribution, and operations
- explicit warnings about generated files or misleading directories
- drill-down links from system overview to concrete files or components

## Sample Repositories Reviewed

- `flare-foundation/developer-hub`
  - README: local run commands, repo structure, development workflow
  - sidebars: stable category navigation
- `facebook/react-native-website`
  - README: docs source map, versioning notes, local contribution workflow
  - `sidebarsContributing.ts`: contribution docs as a dedicated lane
- `MicrosoftDocs/Agent-Skills`
  - README: quick start, compatibility matrix, curated bundles, catalog split
- `CodeBoarding/CodeBoarding`
  - README: architecture-first onboarding, output artifacts, common commands
- `CodeBoarding/GeneratedOnBoardings`
  - generated onboarding pages: high-level graph plus component drill-down pages
- `netresearch/agent-rules-skill`
  - README: skill structure table, scripts/templates layout, supported project signals

## Patterns Worth Reusing

### 1. Stable Navigation Beats Long Essays

Strong GitHub docs usually split content into a few predictable pages or lanes:
- getting started
- architecture or system map
- contribution or implementation path
- reference or troubleshooting

For R2I, that means `study-doc` should prefer a docs bundle with stable page names.

### 2. Quick Start Must Include A Success Signal

Good repo docs do not stop at setup commands.

They also tell the learner:
- what command to run first
- what "working" looks like
- what artifact, port, page, or test result confirms success

### 3. Repo Structure Should Distinguish Source From Generated Output

Strong docs explicitly separate:
- source of truth
- generated outputs
- example artifacts
- configuration and automation

This prevents beginners from editing the wrong files.

### 4. Architecture Needs Drill-Down Points

The best onboarding docs do not only show a high-level diagram.

They also point the learner toward:
- the best first file to read
- one rich end-to-end workflow
- a few subsystem drill-down candidates

### 5. Contribution Is A Separate Learning Lane

Many mature GitHub doc sites separate:
- "what this system is"
- "how to run it"
- "how to contribute safely"

R2I should preserve this split even when the user mainly wants interview prep.

### 6. Learning Output Should Support More Than One User Intent

GitHub docs often support multiple entry intents:
- reader
- operator
- contributor

For R2I, the equivalent stitched tracks are:
- `understand`: what the repo is and how it is organized
- `verify`: how to run, inspect, or validate it
- `defend`: what you need to explain under interview pressure

## Stitched Rules For R2I

When generating `study-doc`, prefer these rules:

1. `00-overview` should say what the repo is, who it serves, why it matters, and which track to follow first.
2. `01-quick-start` should include prerequisites, first commands, and a concrete success signal.
3. `02-system-map` should include a repo structure table and clearly mark generated or secondary directories.
4. `03-key-flows` should show one main flow plus optional drill-down candidates.
5. `04-reading-path` should offer at least three lanes: learner lane, contributor lane, interviewer lane.
6. `05-checklist` should include checkpoint questions plus one or two first safe change tasks.
7. `06-pitfalls-and-faq` should call out wrong mental models, hidden coupling, and likely "do not edit here first" traps.

## What To Avoid

- giant single-page explanation with no navigation
- folder-name paraphrasing without telling the user where to start
- architecture claims without file anchors
- setup steps without any success signal
- interview questions detached from actual repo structure
- treating generated output directories as core source files

## Nice-To-Have Signals

If the repository evidence is strong enough, add:
- a Mermaid system map
- a small repo structure tree or table
- explicit "best first file" recommendations
- a "first safe change" exercise
- a "what the interviewer will challenge here" note
