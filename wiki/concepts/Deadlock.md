---
title: "Deadlock"
type: concept
tags: [concurrency, reliability, operating-systems]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[Deadlock]] is a concurrency failure where processes wait in a closed dependency cycle, each needing another process's resource while holding its own.

## Current Synthesis
Wulc explains deadlock with the classic resource-wait pattern: multiple processes each need resources held by others, but none can complete and release its own resource until it obtains the next one. The inspected diagram shows a simple cycle among A, B, and C, where A points to C, C points to B, and B points to A.

In this source, deadlock is presented as a structural dependency problem rather than a Python-specific bug. It belongs to the broader family of [[ConcurrencyFailureModes]] that programmers must consider when processes coordinate through shared resources or locks.

## Key Claims
- Deadlock requires a closed loop of resource dependence.
- Each participant blocks because another participant holds a needed resource.
- Progress is impossible while participants refuse or cannot release their own resources.
- Deadlock is a general operating-system and concurrency concept, not only a Python issue.
- Visual dependency cycles make deadlock easier to identify.

## Evidence
- Definition evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says deadlock occurs when multiple processes need one another's resources and form a closed circular relationship.
- Diagram evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] includes an inspected A-B-C cycle illustrating circular resource waiting.
- Resource-release condition: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says other processes cannot obtain a process's resource before that process releases it, but the process needs another resource to finish and release.

## Counterevidence & Qualifications
The source explains deadlock conceptually but does not discuss necessary Coffman conditions, prevention strategies, lock ordering, detection algorithms, timeouts, or recovery policies.

## What Changed
- Created the concept page from Wulc's circular resource-wait example.

## Related Concepts
- [[ConcurrencyFailureModes]] - deadlock is one of the source's named hazards.
- [[InterprocessCommunication]] - shared resources and coordination can create deadlock risk.
- [[Starvation]] - both are progress failures, though starvation does not require a closed cycle.
- [[ParallelProgramming]] - parallelized processes can deadlock when resource coordination fails.
