---
title: "Structured CLI Output"
type: concept
tags: [cli, data-output, developer-tools]
sources:
  - 12-factor-cli-apps-jeff-dickey-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[StructuredCLIOutput]] is the design of command-line output so it remains readable for humans while staying parseable by shell tools and machines.

## Current Synthesis
The CLI source treats output as an interface contract rather than mere printing. Tables should communicate rows of entries without noisy borders, preserve one entry per line, and adapt columns to terminal width. Users should also be able to choose machine-friendly formats such as JSON and CSV, hide headers, add columns, disable truncation, filter values, and sort by fields.

## Key Claims
- Table rows should map to data entries so standard tools like `wc` and `grep` remain useful.
- Table borders add visual noise and make parsing harder.
- Default columns should be conservative, with opt-in controls for extra fields.
- Width-aware truncation protects terminal readability, while `--no-truncate` preserves full values when needed.
- JSON and CSV output let users choose between structured machine processing and simpler text tooling.

## Evidence
- Row contract: [[12-factor-cli-apps-jeff-dickey-medium]] says each table row should be a single entry of data.
- Border warning: [[12-factor-cli-apps-jeff-dickey-medium]] shows a bordered table as an example of what not to do.
- Pipeline support: [[12-factor-cli-apps-jeff-dickey-medium]] shows plain output being counted with `wc` and filtered with `grep`.
- Column controls: [[12-factor-cli-apps-jeff-dickey-medium]] recommends showing only a few default columns while supporting `--columns`.
- Format controls: [[12-factor-cli-apps-jeff-dickey-medium]] recommends `--no-headers`, `--filter`, `--sort`, `--no-truncate`, JSON, and CSV.

## Counterevidence & Qualifications
The source assumes shell composition is important. Some CLIs that primarily launch interactive full-screen interfaces may use different output conventions, but command output that users pipe or archive benefits from these constraints.

## What Changed
- Created the initial concept page for structured CLI output.

## Related Concepts
- [[AutomationFriendlyCLI]] - structured output is a main enabler of shell automation.
- [[CommandLineUX]] - readable tables and format controls affect terminal experience.
- [[CLIApplicationDesign]] - output design is one of the twelve-factor CLI surfaces.
- [[DataGeneratingProcess]] - both concern preserving data structure through representation choices.
- [[SoftwareVerification]] - structured output gives tests stable behavior to assert.
