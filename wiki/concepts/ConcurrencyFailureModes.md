---
title: "Concurrency Failure Modes"
type: concept
tags: [concurrency, reliability, software-development]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ConcurrencyFailureModes]] are bugs or progress failures that arise when multiple processes coordinate resources, execution time, or shared state.

## Current Synthesis
Wulc's source introduces three basic hazards for parallelized programming: [[Deadlock]], [[Starvation]], and [[RaceCondition]]. The article's examples place them on a spectrum: deadlock is circular resource dependence, starvation is indefinite non-progress for one process, and race conditions are timing-dependent wrong results from unsynchronized operations.

The inspected images make the hazards concrete. A three-node cycle shows each process waiting on another process's resource. Two account-balance tables show how different operation orders can lead to a correct final balance or an incorrect one after overlapping reads and writes.

## Key Claims
- Deadlock occurs when processes form a closed loop of resource needs while refusing to release their own resources.
- Starvation occurs when a process cannot continue because it never obtains CPU time or needed resources.
- Race conditions occur when output depends on uncontrolled timing or ordering.
- Shared mutable state makes race conditions visible when operations interleave incorrectly.
- Diagrams and simple account examples can expose concurrency hazards more clearly than definitions alone.

## Evidence
- Deadlock evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] describes processes A, B, and C each needing another process's resource and includes an inspected circular dependency diagram.
- Starvation evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] uses a priority example where process A runs continuously and process B never runs.
- Race-condition evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] defines race conditions through ordering dependence and shows account-balance interleavings that produce incorrect state.

## Counterevidence & Qualifications
The source does not cover livelock, priority inversion, memory visibility, atomicity, lock-free algorithms, or formal verification of concurrent systems. The hazard taxonomy is useful but not exhaustive.

## What Changed
- Created the umbrella concept for the source's deadlock, starvation, and race-condition section.

## Related Concepts
- [[Deadlock]] - circular waiting is one named failure mode.
- [[Starvation]] - unfair or blocked progress is one named failure mode.
- [[RaceCondition]] - timing-dependent state corruption is one named failure mode.
- [[InterprocessCommunication]] - communication and shared resources create coordination obligations.
- [[SystemReliability]] - concurrency hazards are one class of reliability risk.
