---
title: "Automation-Friendly CLI"
type: concept
tags: [cli, automation, developer-tools]
sources:
  - 12-factor-cli-apps-jeff-dickey-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[AutomationFriendlyCLI]] is a command-line design principle that keeps tools usable in scripts, shell pipelines, redirected output, and non-interactive environments.

## Current Synthesis
The source argues that CLIs are powerful partly because users can compose them with other tools. That means the interface must protect automation even while offering rich interactive behavior. The core pattern is to distinguish machine-consumable output from human messaging, make prompts optional, expose parseable formats, pass through arguments predictably, and suppress terminal-control effects when output is not attached to a real terminal.

## Key Claims
- stdout should carry primary output, while stderr should carry warnings, progress, and other user messaging.
- Prompts can improve interactive UX but must always be overrideable for scripts.
- TTY checks and no-color conventions prevent ANSI styling and spinners from corrupting redirected output.
- `--` pass-through parsing lets a CLI forward flags to child processes without stealing them.
- JSON, CSV, row-oriented tables, and header/truncation controls make CLI output composable with other tools.

## Evidence
- Stream contract: [[12-factor-cli-apps-jeff-dickey-medium]] states that stdout is for output and stderr is for messaging, using redirected `curl` progress as an example.
- Prompt override: [[12-factor-cli-apps-jeff-dickey-medium]] says prompts are appropriate when stdin is a TTY but should never be required because scripts must automate the CLI.
- TTY fallback: [[12-factor-cli-apps-jeff-dickey-medium]] warns against colors, spinners, and progress bars when stdout or stderr is not connected to a TTY.
- Argument forwarding: [[12-factor-cli-apps-jeff-dickey-medium]] recommends `--` so `heroku run` can pass flags to a dyno command.
- Parseable output: [[12-factor-cli-apps-jeff-dickey-medium]] recommends JSON for structured data, CSV for `cut` and `awk`, and borderless tables where each row is one entry.

## Counterevidence & Qualifications
Automation friendliness can conflict with beginner-friendly interactivity if defaults are chosen carelessly. The source resolves this by allowing rich prompts and polish only when terminal conditions permit and by requiring explicit overrides.

## What Changed
- Created the initial concept page for automation-friendly CLI behavior.

## Related Concepts
- [[CLIApplicationDesign]] - automation friendliness is one design constraint for CLIs.
- [[CommandLineUX]] - interactive UX must degrade into automation-friendly behavior.
- [[StructuredCLIOutput]] - parseable output formats make automation possible.
- [[CLICommandGrammar]] - pass-through parsing and argument boundaries are grammar decisions.
- [[SoftwareVerification]] - automation-friendly behavior is easier to test in scripts and CI.
