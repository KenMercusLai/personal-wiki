---
title: "muffet"
type: entity
tags: [link-checker, crawler, go, open-source]
sources:
  - link-checkers-recurse
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[Muffet]] is a concurrent website link checker written in Go.

## Current Profile
The source presents muffet as the closest comparison to [[Lychee]]: a fast, focused, single-binary checker whose crawler shape was present from the beginning. A mutex-protected visited set claims a URL at enqueue time, a daemon channel schedules pages, and a `sync.WaitGroup` tracks dynamic work until all descendants finish.

Its frontier and execution limits are distinct. The daemon manager can launch a goroutine for each scheduled page, while a semaphore and per-host throttler bound actual network concurrency. This makes recursion straightforward but leaves the in-memory frontier and goroutine population subject to resource growth.

## Key Characteristics
- Uses a mutex-protected string set to claim URLs before scheduling them.
- Feeds qualifying links discovered by a fetch back into the same page-admission method.
- Uses `sync.WaitGroup` accounting for termination after dynamically created pages complete.
- Separates frontier scheduling from semaphore-based concurrency and per-host throttling.
- Ships as a focused command-line tool rather than a reusable plugin-oriented library.

## Evidence
- Admission and recursion: [[link-checkers-recurse]] traces `addPage` through the visited set and back from fetched qualifying links.
- Completion: [[link-checkers-recurse]] shows each scheduled page incrementing a `WaitGroup` and decrementing it after processing descendants.
- Capacity: [[link-checkers-recurse]] distinguishes the daemon channel from the semaphore and host throttler that limit requests.
- Scope: [[link-checkers-recurse]] characterizes muffet as a fast CLI without a plugin surface or disk-backed frontier.

## Qualifications
The profile comes from another link-checker maintainer's code reading, not muffet documentation or a controlled benchmark. The source does not quantify throughput, memory use, goroutine count, fairness, failure recovery, or maximum practical crawl size. Implementation details and project capabilities may change after the reviewed revision.

## What Changed
- Created the project profile from the comparative recursion teardown.
- Recorded its separation of frontier, termination accounting, and request limiting.

## Relationships
- [[CrawlerArchitecture]] - exemplifies a recursive frontier with enqueue-time identity and explicit quiescence.
- [[DistributedTerminationDetection]] - uses a Go `WaitGroup` to keep descendants counted before parents finish.
- [[AdaptiveBackpressure]] - uses separate semaphore and host throttling rather than frontier capacity as the request limit.
- [[Lychee]] - offers the closest Go-based architectural comparison in the source.
