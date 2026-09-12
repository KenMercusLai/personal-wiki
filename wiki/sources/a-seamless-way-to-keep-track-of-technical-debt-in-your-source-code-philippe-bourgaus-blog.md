---
title: "A seamless way to keep track of technical debt in your source code"
type: source
tags: [software-engineering, technical-debt]
date: 2017-04-12
source_file: /mnt/ken_personal_wiki/Articles/A seamless way to keep track of technical debt in your source code - Philippe Bourgau’s Blog.md
---

## Summary
Philippe Bourgau argues that teams can track lightweight technical debt directly in source code with ordinary `TODO` comments rather than heavier custom annotations. The practice works because common IDEs and code-quality tools already surface TODOs, but it needs team agreement, coding-convention documentation, and regular cleanup so comments do not become stale debt themselves.

## Key Claims
- Heavy `@TechnicalDebt` annotations created too much ceremony, made developers reluctant to change nearby code, and went stale.
- Simple `TODO` comments can act as low-friction technical-debt markers because existing tools already display them.
- Teams can distinguish actionable refactoring ideas from unclear smells with conventions such as `TODO` and `TODO SMELL`.
- The practice should be accepted as a team working agreement rather than imposed silently.
- Tool defaults need interpretation: commit warnings and fixed remediation costs may not match lasting technical-debt tracking.
- Regularly fixing old TODOs and linking recurring problems to TODO comments can reveal technical-debt hotspots for retrospectives.

## Key Quotes
> "very old TODO comments are technical debt of their own" - warning about stale markers

## Connections
- [[PhilippeBourgau]] - author of the practice note.
- [[TechnicalDebtTracking]] - central practice of using source-code comments as a lightweight debt register.
- [[TodoComments]] - the specific marker used for actionable refactoring ideas and code smells.
- [[CodeClimate]] - example dashboard surfacing TODO comments as issues.
- [[SonarQube]] - example analyzer that reports TODO comments with a default remediation cost.
- [[IntelliJIDEA]] - example IDE whose TODO tab and commit-window warning affect the workflow.
- [[ProductRetrospectives]] - recurring problem logs can be reviewed alongside TODOs to find hotspots.

## Contradictions
- None identified.
