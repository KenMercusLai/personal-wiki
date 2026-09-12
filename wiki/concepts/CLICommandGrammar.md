---
title: "CLI Command Grammar"
type: concept
tags: [cli, command-design, developer-tools]
sources:
  - 12-factor-cli-apps-jeff-dickey-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[CLICommandGrammar]] is the structural design of a command-line interface's commands, subcommands, flags, positional arguments, pass-through boundaries, and default invocation behavior.

## Current Synthesis
The source frames command grammar as a learnability and ambiguity problem. Single-command CLIs fit simple Unix-style tasks, while many product CLIs need subcommands and sometimes topic levels. Grammar choices should make it obvious what is the command, what is an argument, when parsing stops, and what happens when a user invokes the tool with no arguments. The same concern motivates the preference for flags over multiple different positional argument types.

## Key Claims
- Single-command CLIs fit one basic task; multi-command CLIs fit broader products with several operations.
- Invoking a CLI with no arguments should show help or command lists rather than perform surprising default behavior.
- Multiple positional argument roles are hard to understand; named flags make roles explicit.
- `--` should mark the boundary where the CLI stops parsing and passes subsequent arguments onward.
- Multi-level subcommand separators can reduce ambiguity between topic commands, subcommands, and arguments.

## Evidence
- CLI kinds: [[12-factor-cli-apps-jeff-dickey-medium]] contrasts single-command tools such as `cp` and `grep` with multi-command CLIs such as `git` and `npm`.
- Default behavior: [[12-factor-cli-apps-jeff-dickey-medium]] says root invocation should list subcommands for multi-command CLIs or display help for single-command CLIs.
- Flag preference: [[12-factor-cli-apps-jeff-dickey-medium]] gives the Heroku fork example and a rule of thumb that two different argument types are suspect and three are never good.
- Pass-through boundary: [[12-factor-cli-apps-jeff-dickey-medium]] explains `--` with `heroku run` forwarding flags to a dyno command.
- Separator choice: [[12-factor-cli-apps-jeff-dickey-medium]] contrasts Git's space-separated `submodule add` with Heroku's colon-separated `domains:add` and argues colons avoid parser ambiguity for topic-level commands with arguments.

## Counterevidence & Qualifications
Command grammar conventions are ecosystem-sensitive. The source itself notes that familiar Unix-style tools can use obvious positional arguments well, and Git-style spaces may be expected by users despite the author's preference for colons in some multi-level command designs.

## What Changed
- Created the initial concept page for CLI command grammar.

## Related Concepts
- [[CLIApplicationDesign]] - command grammar is a core design layer for CLI apps.
- [[CommandLineUX]] - grammar affects how users discover and remember commands.
- [[AutomationFriendlyCLI]] - grammar determines how scripts pass flags and arguments reliably.
- [[StructuredCLIOutput]] - both make command behavior predictable for humans and tools.
- [[DeveloperTooling]] - command grammar is a recurring developer-tool design concern.
