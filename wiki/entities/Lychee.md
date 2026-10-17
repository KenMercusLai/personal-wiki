---
title: "lychee"
type: entity
tags: [rust, link-checker, open-source, developer-tools]
sources:
  - lychee-recursion
  - link-checkers-recurse
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[Lychee]] is an open-source asynchronous link checker written in Rust and started by Matthias Endler in 2020.

## Current Profile
The source describes lychee as a fast checker for websites, documentation, README files, and Markdown, used by roughly 40,000 GitHub repositories and organizations including Google, AWS, Microsoft, and Cloudflare. Its original pipeline was deliberately one-way: inputs were extracted into requests, checked concurrently, and formatted as results.

That architecture made recursive same-domain crawling unusually invasive. Four implementation attempts between 2021 and 2025 encountered fragile work counters, cyclic channel termination, backpressure deadlocks, duplicate requests, shared-state friction, performance regressions, and changes across most request and response layers. By 2026, a cloneable-guard `WaitGroup`, `HostPool`, unified request handling, and sitemap support had supplied much of the missing infrastructure, but true recursion remained unshipped in the source's account.

A follow-up comparison shows that the resulting primitives now align with established crawlers: dynamic work guards provide the same completion role as a Go `WaitGroup`, joinable queue, idle promise, or drain event; per-URI active-request state provides enqueue-time claiming; and `HostPool` supplies separate per-host limits. This validates the direction without proving the feature complete. Lychee still aims to preserve its faster one-shot stream rather than paying the crawler feedback cost on every non-recursive run.

## Key Characteristics
- Checks links asynchronously across sites, documentation, README files, and Markdown inputs.
- Uses a staged input, extraction, request, response, and output pipeline designed originally as a directed acyclic flow.
- Treats performance on the common non-recursive path as a design constraint.
- Uses a per-host pool for pacing, concurrency limits, caching, and deduplication at the request boundary.
- Uses cloneable work guards to observe completion of a dynamic set of tasks.
- Separates recursive work identity and lifetime from per-host request pacing and concurrency.
- Is maintained as a public volunteer project whose architecture, contributor capacity, and funded work affect feature delivery.

## Evidence
- Project role and adoption: [[lychee-recursion]] describes lychee's supported inputs, Rust implementation, 2020 origin, and reported use across about 40,000 GitHub repositories.
- Architecture: [[lychee-recursion]] documents the initial one-way pipeline and four attempts to add a recursive feedback edge.
- Current primitives: [[lychee-recursion]] describes the merged `WaitGroup`, per-host `HostPool`, unified input fetching, and sitemap support; [[link-checkers-recurse]] maps those pieces to the completion, admission, and limiting roles in four established crawlers.
- Comparative architecture: [[link-checkers-recurse]] argues that lychee now has a column-for-column match for crawler primitives while preserving a separate fast non-recursive path.
- Maintenance context: [[lychee-recursion]] records NLnet funding, contributor review and implementation work, branch staleness, environment failures, and unfinished delivery.

## Qualifications
The adoption count and user names are maintainer-reported and not independently verified here. Both sources are by lychee's maintainer and focus on recursion rather than a complete current product or security assessment. The comparative source verifies patterns through source reading but supplies no controlled cross-tool benchmark. Its architectural equivalence is still prospective evidence: the companion retrospective says recursion was not merged, response-body recovery remained open, and no end-to-end correctness or performance suite for the proposed design is reported.

## What Changed
- Added cross-tool evidence that lychee's newer primitives fill the same roles as established crawler frontiers.
- Clarified that frontier identity, termination, and per-host limiting are distinct responsibilities.
- Preserved the boundary between architectural readiness and shipped recursive crawling.

## Relationships
- [[DistributedTerminationDetection]] - recursive crawling requires lychee to detect quiescence while completed pages can still generate new requests.
- [[AdaptiveBackpressure]] - cyclic admission through bounded channels caused a response-processing deadlock.
- [[ConcurrencyFailureModes]] - repeated designs exposed circular waits, timing races, duplicate admission, and detached-task risks.
- [[OpenSourceProjectMaintenance]] - funding, refactors, contributor capacity, and moving build requirements shaped the feature timeline.
- [[StructuredConcurrency]] - explicit work guards account for dynamically created tasks even though the runtime flow remains cyclic.
- [[CrawlerArchitecture]] - provides the frontier, enqueue-time identity, capacity, and quiescence model lychee is retrofitting.
