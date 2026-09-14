---
title: "Starvation"
type: concept
tags: [concurrency, reliability, scheduling]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[Starvation]] is a concurrency failure where a process cannot continue because it never receives the CPU time or resources it needs.

## Current Synthesis
Wulc presents starvation as a progress problem rather than a state-corruption bug. The source's example is scheduling-oriented: process A has higher priority than process B and keeps occupying the CPU because its workload is heavy, so process B remains unable to run.

This distinguishes starvation from [[Deadlock]]. Deadlock depends on a closed resource cycle; starvation can happen through unfair priority, scheduling, or allocation even without a circular wait graph.

## Key Claims
- Starvation means a process cannot obtain the resources it needs to continue.
- Priority differences can cause lower-priority work to wait indefinitely.
- Heavy high-priority work can monopolize CPU access in the source's example.
- Starvation is a progress failure rather than necessarily a data-consistency failure.
- Starvation differs from deadlock because it does not require a closed wait cycle.

## Evidence
- Definition evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] defines starvation as a process never receiving its resources and being unable to continue.
- Scheduling example: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] describes process A with higher priority occupying the CPU and preventing process B from running.
- Contrast evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] presents starvation separately from the circular-wait deadlock example.

## Counterevidence & Qualifications
The source does not cover starvation prevention, fairness policies, aging, priority inversion, queue design, or resource arbitration in distributed systems.

## What Changed
- Created the concept page from Wulc's priority-based starvation example.

## Related Concepts
- [[ConcurrencyFailureModes]] - starvation is one of the source's named hazards.
- [[ConcurrentProgramming]] - scheduler behavior can cause or prevent starvation.
- [[Deadlock]] - both block progress, but through different mechanisms.
- [[ParallelProgramming]] - parallelized systems still need fair resource allocation.
