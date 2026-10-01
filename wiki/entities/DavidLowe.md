---
title: "David Lowe"
type: entity
tags: [software-engineering, perl, code-maintenance]
sources:
  - nestoria-dev-blog-tombstones-for-dead-code
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[DavidLowe]] is the author of a [[Nestoria]] engineering article describing a Perl implementation of [[DeadCodeTombstones]].

## Current Profile
Lowe presents dead-code removal as an evidence problem: code that appears unused may still run through rare or indirect production paths. His implementation instruments suspected paths with author-and-date identifiers, captures invocation context, and deliberately sacrifices complete event counting to keep the application safe and fast.

The profile is source-bounded. The article establishes authorship and implementation details but does not provide Lowe's role, employment dates, broader work history, or independent evaluation of the technique.

## Key Characteristics
- Advocates runtime observation before deleting code that only appears unused.
- Presents an operationally defensive Perl probe that returns rather than disrupting callers when telemetry fails.
- Uses ownership metadata, stack traces, centralized collection, retention, and a web report to make cleanup decisions inspectable.

## Evidence
- Deletion judgment: [[nestoria-dev-blog-tombstones-for-dead-code]] warns that blindly removing apparently dead code can create production failures.
- Defensive implementation: [[nestoria-dev-blog-tombstones-for-dead-code]] shows per-probe quotas, non-blocking locking, silent returns on errors, and dropped excess events.
- Decision support: [[nestoria-dev-blog-tombstones-for-dead-code]] records author, date, location, time, and stack traces, then presents centrally collected results in a web report.

## Qualifications
This profile comes from one first-person company engineering article. It does not establish how much of the surrounding system Lowe designed, how the method compared with alternatives, or whether the reported outcomes generalized beyond Nestoria's infrastructure.

## What Changed
- Established a source-bounded profile around Lowe's production-instrumentation approach to dead-code removal.

## Relationships
- [[Nestoria]] - organization and production setting described in Lowe's article.
- [[DeadCodeTombstones]] - code-maintenance technique Lowe explains and recommends.
- [[ServiceObservability]] - broader discipline within which the runtime probes and reports operate.
