---
title: "Parallel Programming"
type: concept
tags: [parallel-programming, concurrency, software-development]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ParallelProgramming]] is a programming model where multiple processes or units of work execute at the same time, typically by using separate CPU cores.

## Current Synthesis
Wulc distinguishes parallel programming from concurrency by grounding parallelism in a multi-core environment. The inspected parallel-programming diagram shows one parallel program dispatching processes to CPU01 through CPU04, making the defining feature simultaneous execution rather than scheduler-created pseudo-parallel progress on one CPU.

The source treats parallel programming as one member of a broader family that also includes concurrent and distributed programming. Because parallelized processes still work on the same task, communication remains necessary, and shared state, message passing, deadlock, starvation, and race conditions remain part of the design surface.

## Key Claims
- Parallel programming is true simultaneous execution in the source's model.
- Multi-core hardware is the basis for running several processes at the same time.
- Parallelism is distinct from scheduler-mediated [[ConcurrentProgramming]].
- Parallelized processes need communication because they cooperate on one task.
- Parallel programming inherits coordination hazards such as [[Deadlock]] and [[RaceCondition]].

## Evidence
- Multi-core definition: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says each core can run a process at the same time in a multi-core environment.
- Diagram evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] includes an inspected diagram with four processes mapped to four CPUs.
- Communication requirement: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says communication is necessary because parallelized processes complete the same task.
- Failure scope: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] groups deadlock, starvation, and race conditions under problems encountered in parallelized programming.

## Counterevidence & Qualifications
The article is introductory and process-oriented. It does not distinguish threads from processes in depth, discuss Python's GIL, compare data parallelism with task parallelism, or cover GPU/SIMD parallel execution.

## What Changed
- Created the concept page from Wulc's multi-core parallel-programming overview.

## Related Concepts
- [[ConcurrentProgramming]] - concurrency is contrasted as pseudo-parallel scheduling.
- [[DistributedProgramming]] - distributed programming spreads work across physically separate machines.
- [[InterprocessCommunication]] - parallelized processes need shared state or message passing.
- [[PythonConcurrencyLibraries]] - Python modules provide practical routes into concurrent, parallel, and distributed work.
- [[ConcurrencyFailureModes]] - parallel work can expose resource and synchronization hazards.
