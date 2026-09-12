---
title: "12 Factor CLI Apps"
type: source
tags: [cli, developer-tools, software-engineering]
date: 2018-10-10
source_file: /mnt/ken_personal_wiki/Articles/12 Factor CLI Apps - Jeff Dickey - Medium.md
---

## Summary
[[JeffDickey]] argues that command-line products need their own UX discipline because users meet the product through help text, streams, flags, prompts, tables, and process behavior rather than a graphical interface. Drawing on [[Heroku]] and [[Oclif]], the article turns the "12-factor app" spirit into practical [[CLIApplicationDesign]] guidance: make help excellent, prefer clear flags, preserve automation, respect terminal capabilities, keep startup fast, support contribution, structure subcommands deliberately, and follow platform file-location conventions. The screenshots and GIFs reinforce that [[CommandLineUX]] is observable in terminal help, stderr progress, prompts, confirmation flows, selection widgets, and parseable table output.

## Key Claims
- Great CLI help is essential because the CLI itself is the primary interface; help should be available through standard invocations, include flags and arguments, and show concrete examples.
- Flags are usually clearer than multiple positional arguments, especially when inputs have different meanings; parsers should use `--` to stop parsing when passing arguments to another process.
- CLIs should expose version and diagnostic information through predictable commands and flags, and API-backed CLIs can send version strings as user-agent data.
- [[AutomationFriendlyCLI]] depends on separating stdout from stderr, preserving raw output for redirection, falling back when output is not a TTY, and letting prompts be overridden.
- Error output should include a code, title, explanation, repair path, and URL, while debug output and logs should support unexpected failures without polluting normal output.
- [[StructuredCLIOutput]] should use borderless row-oriented tables, screen-width-aware columns, filters, sorting, `--columns`, `--no-headers`, `--no-truncate`, JSON, and CSV so output works for humans and shell pipelines.
- [[CLICommandGrammar]] should distinguish single-command and multi-command CLIs, show help or command lists when invoked without arguments, and choose subcommand separators that avoid ambiguity.
- CLI products should start quickly, be open to contribution with licenses and contribution docs, support plugin extension when useful, and follow XDG-style paths for config, data, and cache files.

## Key Quotes
> "stdout is for output, stderr is for messaging." - concise rule for preserving redirection and structured output.

> "1 type of argument is fine, 2 types are very suspect, and 3 are never good." - rule of thumb for preferring flags over ambiguous positional arguments.

## Connections
- [[JeffDickey]] - author presenting the twelve CLI factors.
- [[Heroku]] - operational product context for examples about app naming, `heroku fork`, `heroku run`, app destruction confirmation, and colon-separated commands.
- [[Oclif]] - CLI framework presented as implementing help, docs, autocomplete, plugins, and startup-performance conventions.
- [[CLIApplicationDesign]] - umbrella design practice described by the twelve factors.
- [[CommandLineUX]] - user-facing terminal experience shaped by help, prompts, output, errors, color, and speed.
- [[AutomationFriendlyCLI]] - principle behind stream separation, TTY checks, prompt overrides, parseable formats, and `--` forwarding.
- [[StructuredCLIOutput]] - table, JSON, CSV, filtering, sorting, and truncation guidance.
- [[CLICommandGrammar]] - single-command versus multi-command structure and subcommand separator choices.
- [[DeveloperTooling]] - broader category of tools whose product quality depends on developer ergonomics.

## Contradictions
- No direct contradictions with existing wiki content. The source adds a developer-tool UX layer that complements existing notes on software reliability, verification, and developer workflows.
