---
title: "Heroku"
type: entity
tags: [platform, developer-tools, cli]
sources:
  - 12-factor-cli-apps-jeff-dickey-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Heroku]] is a cloud application platform that appears in this wiki source as the origin context for both the classic twelve-factor app methodology and several concrete command-line interface examples.

## Current Profile
In "12 Factor CLI Apps," Heroku functions as the lived product environment behind the advice. The source uses Heroku's CLI history to illustrate why ambiguous arguments, reserved help behavior, pass-through parsing, destructive confirmations, and multi-level command grammar matter in real tools. Heroku is also presented as the setting where the broader twelve-factor app methodology inspired an analogous checklist for [[CLIApplicationDesign]].

## Key Characteristics
- Associated with the twelve-factor app methodology that inspired the article's structure.
- Provides practical CLI examples involving app copy, process execution, app names, and destructive actions.
- Uses colon-separated command topics in its CLI to reduce parsing ambiguity.
- Serves as a developer-product context where CLI ergonomics affect support, debugging, and user trust.

## Evidence
- Methodology origin: [[12-factor-cli-apps-jeff-dickey-medium]] says Heroku developed the twelve-factor app methodology for maintainable web applications.
- Argument clarity: [[12-factor-cli-apps-jeff-dickey-medium]] uses `heroku fork --from FROMAPP --to TOAPP` to show why flags can be clearer than mixed positional arguments.
- Pass-through parsing: [[12-factor-cli-apps-jeff-dickey-medium]] uses `heroku run -a myapp -- myscript.sh -a arg1` to explain the `--` stop-parsing convention.
- Command grammar: [[12-factor-cli-apps-jeff-dickey-medium]] contrasts Heroku's `domains:add` style with Git's space-separated subcommands.
- Safety prompts: [[12-factor-cli-apps-jeff-dickey-medium]] describes typing the app name again when destroying a Heroku app.

## Qualifications
This page describes Heroku only as it appears in the CLI design essay. It does not cover Heroku's broader platform history, business ownership, runtime model, or product strategy.

## What Changed
- Created the initial Heroku entity page for the CLI-design source.

## Relationships
- [[JeffDickey]] - author uses Heroku experience as evidence.
- [[Oclif]] - CLI framework connected to Heroku's command-line tooling ecosystem.
- [[CLIApplicationDesign]] - Heroku supplies examples and the twelve-factor analogy.
- [[CLICommandGrammar]] - Heroku's colon-separated commands are a grammar example.
