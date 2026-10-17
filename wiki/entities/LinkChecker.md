---
title: "LinkChecker"
type: entity
tags: [link-checker, crawler, python, open-source]
sources:
  - link-checkers-recurse
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[LinkChecker]] is a Python link checker and synchronous thread-pool crawler whose history in the source dates to 2000.

## Current Profile
LinkChecker uses a hand-written joinable `UrlQueue` as its recursive frontier. The queue is deliberately unbounded so all worker threads cannot block while producing descendants into a full queue. Its unfinished-work counter increments during `put()` and decrements only after a worker has processed an item and enqueued its children, letting `join()` observe quiescence without a premature zero.

A placeholder in the result cache claims each URL during enqueue, before any request. Fixed worker threads and per-host pacing limit execution separately from frontier storage, while a URL cap, cleanup, and timed abort mitigate some risks of unbounded queue growth.

## Key Characteristics
- Uses blocking I/O and a fixed Python worker-thread pool.
- Keeps an unbounded joinable URL queue to avoid recursive producer deadlock.
- Claims URLs at `put()` time with a placeholder in the result cache.
- Tracks unfinished tasks under a condition lock and exposes `join()` for completion.
- Provides per-host request pacing, output loggers, and a plugin system.
- Uses URL caps, cleanup, and join timeouts as practical safeguards.

## Evidence
- Frontier and completion: [[link-checkers-recurse]] describes the unbounded deque, synchronized unfinished-task counter, `task_done()`, and `join()`.
- Deduplication: [[link-checkers-recurse]] shows a `None` result-cache sentinel inserted before the URL reaches a worker.
- Capacity and politeness: [[link-checkers-recurse]] describes fixed threads and randomized per-host request spacing.
- Extensibility and limits: [[link-checkers-recurse]] notes plugins and output loggers alongside thread, GIL, and in-memory-frontier constraints.

## Qualifications
The source is an external maintainer's code reading rather than a LinkChecker-authored architecture statement or benchmark. Calling the tool the lowest-throughput comparison is qualitative and configuration-dependent. An unbounded queue avoids one deadlock class by shifting the bound to memory, URL caps, cleanup, and operator policy.

## What Changed
- Created the project profile from the comparative recursion teardown.
- Recorded why its unbounded frontier is an explicit anti-deadlock choice rather than an absent capacity policy.

## Relationships
- [[CrawlerArchitecture]] - implements a joinable frontier, enqueue-time identity, bounded workers, and per-host pacing.
- [[DistributedTerminationDetection]] - its synchronized unfinished-task counter gives `join()` WaitGroup-like semantics.
- [[AdaptiveBackpressure]] - separates an unbounded producer frontier from thread-count and per-host execution limits.
- [[ConcurrencyFailureModes]] - avoids cyclic queue deadlock by ensuring recursive producers do not block on frontier capacity.
