---
title: "Concurrency Failure Modes"
type: concept
tags: [concurrency, reliability, software-development]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
  - lychee-recursion
  - link-checkers-recurse
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[ConcurrencyFailureModes]] are bugs or progress failures that arise when multiple processes coordinate resources, execution time, or shared state.

## Current Synthesis
Wulc's source introduces three basic hazards for parallelized programming: [[Deadlock]], [[Starvation]], and [[RaceCondition]]. The article's examples place them on a spectrum: deadlock is circular resource dependence, starvation is indefinite non-progress for one process, and race conditions are timing-dependent wrong results from unsynchronized operations.

The inspected images make the hazards concrete. A three-node cycle shows each process waiting on another process's resource. Two account-balance tables show how different operation orders can lead to a correct final balance or an incorrect one after overlapping reads and writes.

The [[Lychee]] recursion history extends this introductory taxonomy into asynchronous pipelines. Cyclic sender ownership can prevent natural channel closure; bounded backpressure can make a response consumer wait on the request capacity that only continued response consumption can release; counters can briefly or permanently disagree with dynamically created work; and multiple pages can race to submit the same URL before a cache marks it seen. These failures show that progress, completion, memory visibility, and admission identity require separate invariants.

The cross-tool comparison provides positive controls for those failures. All four established crawlers claim URL identity during enqueue rather than after completion. Their termination primitives count or observe queued and active work together, with descendants admitted before a parent can make the system appear idle. Their concurrency and host limits remain separate from the recursive frontier. Single-threaded runtimes serialize admission without locks, while Go, Python, and Rust need explicit synchronization; the invariant remains the same even when the race surface differs.

## Key Claims
- Deadlock occurs when processes form a closed loop of resource needs while refusing to release their own resources.
- Starvation occurs when a process cannot continue because it never obtains CPU time or needed resources.
- Race conditions occur when output depends on uncontrolled timing or ordering.
- Shared mutable state makes race conditions visible when operations interleave incorrectly.
- Cyclic pipelines can deadlock through lifecycle and capacity dependencies even without explicit user-level locks.
- Dynamic asynchronous work needs explicit termination and admission invariants; a semaphore or post-completion cache does not supply them.
- Removing a shared-memory race through event-loop serialization does not remove quiescence, capacity, or memory-growth hazards.

## Evidence
- Deadlock evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] describes processes A, B, and C each needing another process's resource and includes an inspected circular dependency diagram.
- Starvation evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] uses a priority example where process A runs continuously and process B never runs.
- Race-condition evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] defines race conditions through ordering dependence and shows account-balance interleavings that produce incorrect state.
- Channel-lifecycle evidence: [[lychee-recursion]] shows a recursion handler retaining the sender required to keep generating work while also waiting for the response stream, which itself depended on request-stream closure.
- Backpressure evidence: [[lychee-recursion]] reports a full request channel blocking the response handler and thereby preventing the capacity release needed to unblock it.
- Dynamic-work evidence: [[lychee-recursion]] traces premature completion and hanging to counters that were updated separately from asynchronously discovered tasks.
- Duplicate-admission evidence: [[lychee-recursion]] says parallel pages could submit the same URL before any completed request populated the cache.
- Enqueue-time defense: [[link-checkers-recurse]] finds visited-set or cache claiming before requests in muffet, LinkChecker, linkinator, and broken-link-checker.
- Completion ordering: [[link-checkers-recurse]] shows counters, idle promises, and drain events remaining safe only when descendants enter the tracked lifecycle before their parents complete.
- Capacity separation: [[link-checkers-recurse]] shows recursive frontiers paired with distinct semaphores, worker counts, socket caps, rate limits, and host throttlers.

## Counterevidence & Qualifications
The sources do not cover livelock, priority inversion, lock-free algorithms, or formal verification of concurrent systems. The lychee evidence is a first-party retrospective and maintainer-authored comparison, not a minimized formal model or controlled runtime study; some reported failures combine several mechanisms and do not establish that Rust or Tokio uniquely causes them. Enqueue-time claiming can also suppress legitimate retries or revisits unless state transitions are modeled explicitly. The hazard taxonomy is useful but not exhaustive.

## What Changed
- Added cross-runtime evidence for enqueue-time identity and descendant-aware completion.
- Distinguished event-loop race avoidance from the remaining completion and capacity obligations.
- Added frontier-versus-limiter separation as a defense against recursive queue deadlock.

## Related Concepts
- [[Deadlock]] - circular waiting is one named failure mode.
- [[Starvation]] - unfair or blocked progress is one named failure mode.
- [[RaceCondition]] - timing-dependent state corruption is one named failure mode.
- [[InterprocessCommunication]] - communication and shared resources create coordination obligations.
- [[SystemReliability]] - concurrency hazards are one class of reliability risk.
- [[DistributedTerminationDetection]] - determines when dynamic work is truly quiescent rather than momentarily absent.
- [[AdaptiveBackpressure]] - capacity signals become a progress hazard when feedback cycles block their own consumer.
- [[CrawlerArchitecture]] - combines the admission, frontier, worker, and quiescence invariants that prevent these failures.
