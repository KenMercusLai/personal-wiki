---
title: "Race Condition"
type: concept
tags: [concurrency, reliability, shared-state]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[RaceCondition]] is a timing-dependent bug where a system's output depends on the order or timing of events that the programmer did not properly control.

## Current Synthesis
Wulc explains race conditions through shared account-balance updates. In the correct inspected sequence, one actor reads and adds money before the other actor reads the updated balance and withdraws money, producing the expected final value. In the broken sequence, both actors read the original balance before either final update is applied, so later writes overwrite each other and the final balance becomes wrong.

The example links race conditions directly to shared mutable state and synchronization. If multiple processes modify the same variable without preserving the intended time sequence, the source says the synchronization breaks and data becomes incorrect.

## Key Claims
- Race conditions are bugs when events happen outside the programmer's intended order.
- Shared mutable state is vulnerable when multiple processes read and write it without synchronization.
- The same operations can produce different results depending on interleaving.
- Race-condition examples often require tracking reads and writes, not just final operations.
- Locks, mutexes, or avoiding shared mutable state are relevant protective ideas in the source's surrounding discussion.

## Evidence
- Definition evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] quotes a race-condition definition and explains it as uncontrolled timing among uncertain processes or signals.
- Account example: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] includes inspected account-balance tables showing a correct sequence and an incorrect interleaving.
- Synchronization warning: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says multiple processes modifying the same variable without the required time sequence can cause data errors.
- Protection context: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says writable shared data needs mechanisms such as mutexes and locks.

## Counterevidence & Qualifications
The source gives a simple process-level account example. It does not cover memory models, atomic operations, transaction isolation, idempotency, or race conditions in distributed message ordering.

## What Changed
- Created the concept page from Wulc's timing-dependent account-balance examples.

## Related Concepts
- [[ConcurrencyFailureModes]] - race condition is one of the source's named hazards.
- [[InterprocessCommunication]] - unsafe shared-state communication can produce race conditions.
- [[MessagePassing]] - message passing can avoid some shared-memory races by copying data.
- [[ConcurrentProgramming]] - interleaving under concurrency can expose race conditions.
- [[ParallelProgramming]] - true simultaneous execution can also expose race conditions.
