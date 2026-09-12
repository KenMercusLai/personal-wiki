---
title: "Oclif"
type: entity
tags: [cli, framework, developer-tools]
sources:
  - 12-factor-cli-apps-jeff-dickey-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Oclif]] is a Node-based CLI framework presented in "12 Factor CLI Apps" as a way to build command-line applications that follow strong help, documentation, autocomplete, plugin, and startup-performance conventions.

## Current Profile
The source presents oclif as both evidence and implementation vehicle for [[CLIApplicationDesign]]. It is shown through screenshots where `oclif --help` displays a description, version, usage, and command table. The article also credits the framework with online docs, in-CLI docs, autocomplete, plugin support, command-topic conventions, and lazy command loading that keeps startup overhead around a practical target.

## Key Characteristics
- Provides generated in-terminal help with version, usage, and command listings.
- Supports online documentation and shell autocomplete as help surfaces.
- Encodes plugin extension as a way for external contributions to become reusable CLI functionality.
- Uses "topics" for deeper command organization.
- Aims to minimize startup overhead by loading only the command about to run.

## Evidence
- Help surface: [[12-factor-cli-apps-jeff-dickey-medium]] shows `oclif --help` with version, usage, and commands such as `command`, `help`, `hook`, `multi`, `plugin`, and `single`.
- Documentation and completion: [[12-factor-cli-apps-jeff-dickey-medium]] says oclif provides online docs, in-CLI docs, and autocomplete.
- Plugin model: [[12-factor-cli-apps-jeff-dickey-medium]] says oclif plugins let contributors extend a CLI and can later become core plugins.
- Startup performance: [[12-factor-cli-apps-jeff-dickey-medium]] says oclif avoids requiring every command file and has roughly 150ms overhead on the author's machine.
- Command organization: [[12-factor-cli-apps-jeff-dickey-medium]] calls sub-subcommands "topics" in oclif.

## Qualifications
The source is favorable because it is written by an oclif maintainer/practitioner and does not compare oclif against other CLI frameworks, languages, or maintenance costs.

## What Changed
- Created the initial oclif entity page as the framework case for CLI design conventions.

## Relationships
- [[JeffDickey]] - author presents oclif as the framework embodiment of the factors.
- [[Heroku]] - related developer-tooling ecosystem and source context.
- [[CLIApplicationDesign]] - oclif operationalizes many of the source's design rules.
- [[CommandLineUX]] - oclif help and autocomplete improve terminal user experience.
- [[CLICommandGrammar]] - oclif topics are one approach to multi-level command structure.
