---
title: "Jeff Dickey"
type: entity
tags: [author, cli, developer-tools]
sources:
  - 12-factor-cli-apps-jeff-dickey-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[JeffDickey]] is the author of "12 Factor CLI Apps," a practitioner essay about building useful, maintainable, automation-friendly command-line applications.

## Current Profile
Within this wiki, Jeff Dickey appears as a CLI practitioner writing from [[Heroku]] experience and from work on [[Oclif]]. His role in the source is not to present a formal standard, but to distill product lessons into practical [[CLIApplicationDesign]] norms: help should be part of the interface, flags should remove ambiguity, streams should preserve automation, and terminal polish should degrade cleanly.

## Key Characteristics
- Writes from hands-on command-line product experience rather than abstract interface theory.
- Treats CLI design as user experience, not merely argument parsing.
- Uses Heroku examples to show how small command choices create real user confusion or safety.
- Presents oclif as a framework built to encode many of the recommended conventions.

## Evidence
- Practitioner framing: [[12-factor-cli-apps-jeff-dickey-medium]] opens by comparing CLI products with web applications and arguing that CLIs are powerful for developer, admin, and power-user tasks.
- Heroku experience: [[12-factor-cli-apps-jeff-dickey-medium]] uses Heroku examples for ambiguous `fork` arguments, pass-through `heroku run` parsing, a real app named `help`, destructive confirmation, and colon-separated command topics.
- Framework connection: [[12-factor-cli-apps-jeff-dickey-medium]] says oclif was built to follow these principles in Node.
- UX emphasis: [[12-factor-cli-apps-jeff-dickey-medium]] repeatedly links help, examples, errors, prompts, tables, and startup speed to whether users love or avoid a CLI.

## Qualifications
The wiki currently knows Jeff Dickey only through this article. It does not yet include independent biographical material, other writing, or a full history of his Heroku or oclif work.

## What Changed
- Created the initial entity page for Jeff Dickey as the author of the CLI design source.

## Relationships
- [[Heroku]] - product and organizational context for many examples in the source.
- [[Oclif]] - framework associated with the source's implementation advice.
- [[CLIApplicationDesign]] - main topic of Dickey's article.
- [[CommandLineUX]] - design lens Dickey applies to terminal products.
