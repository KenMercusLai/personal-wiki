---
title: "Command-Line UX"
type: concept
tags: [cli, ux, developer-tools]
sources:
  - 12-factor-cli-apps-jeff-dickey-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[CommandLineUX]] is the user experience of interacting with software through terminal commands, help text, flags, prompts, messages, progress indicators, and output formats.

## Current Synthesis
The source treats command-line UX as a product problem made of small terminal contracts. Users need to discover commands without a GUI, understand input roles, diagnose failure, see progress during long work, and trust that output can be redirected or parsed. The best CLI experience is therefore both helpful and restrained: rich when attached to an interactive terminal, plain when used in automation, and explicit when something goes wrong.

## Key Claims
- Help should appear wherever users naturally ask for it and should include descriptions, arguments, flags, and examples.
- User input is clearer when named flags replace ambiguous multi-role positional arguments.
- Errors should teach repair by including codes, titles, descriptions, fixes, and URLs.
- Visual polish such as colors, dimming, spinners, progress bars, notifications, prompts, and selection widgets can improve confidence during interactive use.
- Rich UX must respect terminal capabilities and user preferences so automation and accessibility are not sacrificed.

## Evidence
- Help behavior: [[12-factor-cli-apps-jeff-dickey-medium]] lists standard root and subcommand invocations that should show help and shows an oclif help screen with version, usage, and commands.
- Flag clarity: [[12-factor-cli-apps-jeff-dickey-medium]] contrasts `heroku fork FROMAPP --app TOAPP` with `heroku fork --from FROMAPP --to TOAPP`.
- Error repair: [[12-factor-cli-apps-jeff-dickey-medium]] gives a file-permission error format with an error code, title, description, chmod fix, and URL.
- Interactive polish: [[12-factor-cli-apps-jeff-dickey-medium]] includes examples of stderr progress, spinners, prompts, app-name confirmation, and checkbox/radio-style selection.
- Fallback constraints: [[12-factor-cli-apps-jeff-dickey-medium]] says colors, spinners, and progress bars should not write ANSI control behavior into redirected output and should respect `TERM=dumb`, `NO_COLOR`, and `--no-color`.

## Counterevidence & Qualifications
The article emphasizes developer and power-user CLIs. Consumer-facing terminal tools, Unix-traditional tools, embedded systems, or environments with strict logging policies may prefer more minimal output and fewer interactive affordances.

## What Changed
- Created the initial concept page for command-line UX.

## Related Concepts
- [[CLIApplicationDesign]] - command-line UX is the user-facing layer of CLI application design.
- [[AutomationFriendlyCLI]] - automation constraints qualify how rich terminal UX should behave.
- [[StructuredCLIOutput]] - table and machine-readable formats affect user experience.
- [[CLICommandGrammar]] - command and subcommand structure shape discoverability.
- [[PlayerGuidance]] - both concern guiding users through interaction, though CLI UX uses textual terminal surfaces.
