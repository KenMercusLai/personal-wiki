---
title: "Concurrent Programming"
type: concept
tags: [concurrency, operating-systems, software-development]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ConcurrentProgramming]] is a programming model where multiple processes or tasks make progress over time through scheduling, even if only one process occupies the CPU at a given instant.

## Current Synthesis
Wulc's source presents concurrent programming as pseudo-parallelism rather than true simultaneous execution. The inspected model diagram shows a concurrent program split into processes, a scheduler, a process queue, and a CPU; the scheduler decides which process can access the CPU, so apparent simultaneity comes from controlled interleaving.

This makes concurrency primarily a coordination and scheduling idea. It can improve program structure or responsiveness, but it also creates failure possibilities when access to CPU time, resources, or shared state is not coordinated.

## Key Claims
- Concurrency is not the same as multi-core parallel execution.
- A scheduler and process queue mediate access to CPU time.
- Only one process occupies the CPU at a given moment in the source's simple model.
- Interleaving creates a need for resource coordination and communication.
- Concurrency can expose failure modes such as [[Starvation]] and [[RaceCondition]].

## Evidence
- Scheduler model: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] describes concurrent programming as one process occupying the CPU at a time under scheduling control.
- Diagram evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] includes an inspected diagram with two processes, a scheduler, a process queue, and a CPU.
- Failure connection: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] later explains starvation and race conditions as problems that arise in parallelized programming contexts.

## Counterevidence & Qualifications
The source uses a simplified teaching model and does not cover modern async runtimes, coroutine scheduling, preemption details, Python's GIL, or the difference between CPU-bound and I/O-bound concurrency.

## What Changed
- Created the concept page from Wulc's scheduler-based concurrency explanation.

## Related Concepts
- [[ParallelProgramming]] - parallelism is contrasted with scheduler-mediated concurrency.
- [[InterprocessCommunication]] - concurrent processes require communication when they cooperate on one task.
- [[ConcurrencyFailureModes]] - scheduling and shared resources can produce concurrency hazards.
- [[Starvation]] - one process can fail to progress when scheduling or resource allocation is unfair.
- [[RaceCondition]] - unsynchronized interleaving can corrupt shared state.
