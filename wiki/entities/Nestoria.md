---
title: "Nestoria"
type: entity
tags: [property-search, software-engineering, perl]
sources:
  - nestoria-dev-blog-tombstones-for-dead-code
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[Nestoria]] is the company engineering context for a Perl-based [[DeadCodeTombstones]] system used to test whether apparently unused production code still executes.

## Current Profile
The source presents Nestoria through one internal maintenance practice. Engineers mark suspected dead paths, write bounded local logs when those paths execute, collect the files centrally through scheduled jobs, delete old logs, and inspect a web report before deciding whether to remove or refactor code.

Nestoria reports both deleting genuinely dead code and avoiding deletion of live “vampires.” The article does not quantify either result or document the wider organization, product architecture, traffic profile, or duration of observation.

## Key Characteristics
- Used production instrumentation to replace intuition alone in dead-code cleanup.
- Designed probe failures, lock contention, and quota limits not to interrupt the application.
- Connected local event capture with scheduled central collection, retention cleanup, and a human-readable report.

## Evidence
- Evidence-led cleanup: [[nestoria-dev-blog-tombstones-for-dead-code]] says the technique helped remove genuinely dead code and preserve code that only appeared dead.
- Production safety: [[nestoria-dev-blog-tombstones-for-dead-code]] documents silent failure behavior, bounded files, and non-blocking file locks.
- Operating workflow: [[nestoria-dev-blog-tombstones-for-dead-code]] describes collection and deletion cron jobs plus a report of tombstones, vampires, stack traces, and deleted probes.

## Qualifications
The profile is deliberately narrow and rests on a single company-authored article. Its outcome claims are unmeasured, and the unpublished infrastructure-specific cron jobs prevent full reproduction of the collection and retention path.

## What Changed
- Established a source-bounded profile of Nestoria's evidence-led dead-code cleanup workflow.

## Relationships
- [[DavidLowe]] - author documenting the company's implementation.
- [[DeadCodeTombstones]] - maintenance technique used in Nestoria's production code.
- [[CentralizedLogging]] - scheduled collection turns local probe files into a shared report.
