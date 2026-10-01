---
title: "Heroku"
type: entity
tags: [platform, developer-tools, cli]
sources:
  - 12-factor-cli-apps-jeff-dickey-medium
  - rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[Heroku]] is a cloud application platform represented both as the origin context for twelve-factor application practice and CLI design examples and as [[RainforestQA]]'s former production platform before a 2018 migration to Google Cloud.

## Current Profile
In "12 Factor CLI Apps," Heroku functions as the lived product environment behind advice on ambiguous arguments, reserved help behavior, pass-through parsing, destructive confirmations, and multi-level command grammar. The broader twelve-factor methodology inspired an analogous checklist for [[CLIApplicationDesign]].

Rainforest QA supplies an operator view. Heroku enabled a lean operations team, horizontal scaling, portable stateless applications, and strong developer experience. The company did not leave merely because raw hosting looked expensive; its reported constraints were a then-current one-terabyte database-plan ceiling, private-network security needs, and expensive short-lived compute. The same twelve-factor discipline that shaped Heroku applications reduced migration work when those services moved to containers and Kubernetes.

## Key Characteristics
- Associated with the twelve-factor app methodology that inspired the article's structure.
- Provides practical CLI examples involving app copy, process execution, app names, and destructive actions.
- Uses colon-separated command topics in its CLI to reduce parsing ambiguity.
- Serves as a developer-product context where CLI ergonomics affect support, debugging, and user trust.
- Can reduce operating-team burden through an opinionated runtime, horizontal scaling model, and managed data services.
- Its abstraction can become constraining when workloads require larger databases, private networking, specialized security, or inexpensive compute-intensive batch execution.

## Evidence
- Methodology origin: [[12-factor-cli-apps-jeff-dickey-medium]] says Heroku developed the twelve-factor app methodology for maintainable web applications.
- Argument clarity: [[12-factor-cli-apps-jeff-dickey-medium]] uses `heroku fork --from FROMAPP --to TOAPP` to show why flags can be clearer than mixed positional arguments.
- Pass-through parsing: [[12-factor-cli-apps-jeff-dickey-medium]] uses `heroku run -a myapp -- myscript.sh -a arg1` to explain the `--` stop-parsing convention.
- Command grammar: [[12-factor-cli-apps-jeff-dickey-medium]] contrasts Heroku's `domains:add` style with Git's space-separated subcommands.
- Safety prompts: [[12-factor-cli-apps-jeff-dickey-medium]] describes typing the app name again when destroying a Heroku app.
- Lean operations: [[rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes]] credits Heroku with supporting scale and agility without a large operations team.
- Portability dividend: [[rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes]] says close twelve-factor adherence kept persistent state outside dynos and made application migration comparatively straightforward.
- Exit pressure: [[rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes]] identifies database size, private-network security, and short-lived compute economics as the decisive constraints.
- Database boundary: [[rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes]] says missing PostgreSQL superuser access prevented native replication for the Cloud SQL migration.

## Qualifications
The migration account reflects Rainforest QA's 2018 plans and product constraints, not Heroku's current limits, prices, security offerings, or fitness for other workloads. It is also a first-party exit retrospective, while the same source explicitly credits Heroku's developer experience and total economics for a lean team. These sources do not cover Heroku's full platform history, ownership, or current product strategy.

## What Changed
- Expanded Heroku from CLI context into a qualified platform profile covering its operating leverage, twelve-factor portability dividend, and workload-specific exit pressures.

## Relationships
- [[JeffDickey]] - author uses Heroku experience as evidence.
- [[Oclif]] - CLI framework connected to Heroku's command-line tooling ecosystem.
- [[CLIApplicationDesign]] - Heroku supplies examples and the twelve-factor analogy.
- [[CLICommandGrammar]] - Heroku's colon-separated commands are a grammar example.
- [[RainforestQA]] - operator that retained Heroku as a rollback platform during a staged move to Google Cloud.
- [[Kubernetes]] - target runtime whose container model accepted Rainforest QA's twelve-factor applications.
- [[PostgreSQL]] - managed data layer whose scale and replication boundaries shaped the migration.
