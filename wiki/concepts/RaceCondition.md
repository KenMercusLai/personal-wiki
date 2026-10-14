---
title: "Race Condition"
type: concept
tags: [concurrency, reliability, shared-state]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
  - how-we-found-a-bug-in-the-hyper-http-library
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Definition
[[RaceCondition]] is a timing-dependent bug where a system's output depends on the order or timing of events that the programmer did not properly control.

## Current Synthesis
The available sources show two forms of the same ordering failure. Wulc's account-balance example demonstrates a shared-state race: both actors read an old value before either final update is applied, so a later write overwrites the other operation. Cloudflare's [[Hyper]] incident demonstrates a lifecycle race without a shared counter: response encoding completed, a socket flush remained pending, and shutdown proceeded before buffered bytes reached the kernel.

The hyper failure appeared only when a large response, real concurrency, and a briefly slower production reader filled the socket buffer. Fast readers such as curl let the flush finish immediately, while broader `strace` instrumentation perturbed timing enough to hide the bug. The robust response was not merely to repeat production traffic, but to encode the decisive schedule into a deterministic stream wrapper that accepted one write and then returned `Poll::Pending`.

## Key Claims
- Race conditions are bugs when events happen outside the programmer's intended order.
- Shared mutable state is vulnerable when multiple processes read and write it without synchronization, but races can also arise between asynchronous lifecycle states such as flush and shutdown.
- The same operations can produce different results depending on interleaving, readiness, buffer capacity, and observer-induced timing changes.
- Correct application-level completion does not prove that lower transport layers completed their work.
- Deterministic tests can model the critical schedule directly by controlling readiness and partial progress.
- Repairs should enforce the actual invariant at the narrowest lifecycle boundary; hyper's final fix flushes immediately before shutdown.

## Evidence
- Definition evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] quotes a race-condition definition and explains it as uncontrolled timing among uncertain processes or signals.
- Account example: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] includes inspected account-balance tables showing a correct sequence and an incorrect interleaving.
- Synchronization warning: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says multiple processes modifying the same variable without the required time sequence can cause data errors.
- Protection context: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says writable shared data needs mechanisms such as mutexes and locks.
- Production symptom: [[how-we-found-a-bug-in-the-hyper-http-library]] reports large HTTP bodies truncated near socket-buffer size despite status `200`, successful encoding, and no application error.
- Syscall sequence: [[how-we-found-a-bug-in-the-hyper-http-library]] contrasts complete multi-write responses with a failing partial `sendto` followed immediately by `SHUT_WR`.
- State-machine cause: [[how-we-found-a-bug-in-the-hyper-http-library]] traces a discarded `Poll::Pending` from `poll_flush` into connection completion and premature shutdown.
- Deterministic regression: [[how-we-found-a-bug-in-the-hyper-http-library]] uses a stream that accepts 8 KB once and then blocks to make the critical interleaving repeatable.
- Lifecycle repair: [[how-we-found-a-bug-in-the-hyper-http-library]] reports that the upstream fix awaits a complete flush inside `poll_shutdown`.

## Counterevidence & Qualifications
Wulc's source is an introductory process-level example and does not cover memory models, atomic operations, transaction isolation, idempotency, or distributed message ordering. Cloudflare's account is a first-party incident explanation with strong internal evidence but no independent reproduction or fleet-wide rate. Its December architecture change is presented as the condition that exposed a pre-existing bug, not proof that faster local communication generally increases race risk. Instrumentation can alter timing, but that does not make kernel tracing uniquely sufficient; deterministic tests, application telemetry, protocol validation, and code reasoning remain complementary.

## What Changed
- Extended the concept from shared-state overwrite to asynchronous flush-versus-shutdown ordering.
- Added buffer capacity, reader pace, and observer effects as conditions that can expose or hide a race.
- Added controlled readiness as a way to turn a production-only race into a deterministic regression test.
- Added boundary-local invariant enforcement through flush-before-shutdown.

## Related Concepts
- [[ConcurrencyFailureModes]] - race condition is one of the source's named hazards.
- [[InterprocessCommunication]] - unsafe shared-state communication can produce race conditions.
- [[MessagePassing]] - message passing can avoid some shared-memory races by copying data.
- [[ConcurrentProgramming]] - interleaving under concurrency can expose race conditions.
- [[ParallelProgramming]] - true simultaneous execution can also expose race conditions.
- [[Hyper]] - its HTTP/1 lifecycle supplied the asynchronous transport case.
- [[AdaptiveBackpressure]] - socket saturation made an incomplete flush observable as `Poll::Pending`.
- [[ServiceObservability]] - kernel syscall evidence distinguished encoded response completion from actual socket delivery.
- [[SystemReliability]] - lifecycle completion must include all state required by the external contract.
