---
title: "linkinator"
type: entity
tags: [link-checker, crawler, nodejs, open-source]
sources:
  - link-checkers-recurse
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[Linkinator]] is a Node.js link-checking library and crawler built around a concurrency-limited asynchronous queue.

## Current Profile
Linkinator relies on the single-threaded JavaScript event loop to serialize its visited-set check and insertion without a mutex. New URLs are claimed before their checks are queued, while a pending-check map lets repeated references await one in-flight request and still associate a broken result with multiple parents.

Its queue's `onIdle()` promise signals completion only when nothing is queued or running. Crawling uses `GET` because recursion needs a response body for extraction, while leaf checking can use `HEAD`. The design is embeddable through events but retains results and relationships in memory and reacts to `429` responses rather than proactively enforcing a general per-host concurrency cap.

## Key Characteristics
- Uses event-loop serialization for atomic visited-set admission.
- Runs work through a queue with configurable concurrency and an `onIdle()` completion promise.
- Tracks in-flight checks and parent-link relationships separately from URL identity.
- Uses body-bearing `GET` requests for pages that must be crawled.
- Exposes lifecycle events for embedding and scripting.
- Applies reactive per-host delay after `429` responses rather than general proactive pacing.

## Evidence
- Admission and reuse: [[link-checkers-recurse]] shows cache insertion, pending-promise creation, and queue admission in one event-loop callback.
- Completion: [[link-checkers-recurse]] identifies `queue.onIdle()` as the queued-plus-running quiescence signal.
- Fetch semantics: [[link-checkers-recurse]] shows the choice between `GET` for crawling and `HEAD` for leaf checking.
- Tradeoffs: [[link-checkers-recurse]] describes single-core parsing, in-memory relationship growth, event-based embedding, and reactive `429` delays.

## Qualifications
The profile is based on an external source-code reading rather than project documentation or measured evaluation. Single-threaded admission removes one shared-state race but can make CPU-heavy parsing contend for the event loop. The source does not quantify throughput, memory growth, request fairness, or the effectiveness of reactive rate handling.

## What Changed
- Created the project profile from the comparative recursion teardown.
- Recorded the distinction between event-loop-serialized admission and queue-managed concurrency.

## Relationships
- [[CrawlerArchitecture]] - exemplifies enqueue-time claiming, a concurrency-limited frontier, and idle-based termination.
- [[DistributedTerminationDetection]] - delegates quiescence to the queue's `onIdle()` promise.
- [[AdaptiveBackpressure]] - limits global queue concurrency but handles host pressure reactively through `429` delay state.
- [[Lychee]] - clarifies why response bodies and shared-state ownership are different implementation costs across runtimes.
