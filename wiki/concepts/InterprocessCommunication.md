---
title: "Interprocess Communication"
type: concept
tags: [concurrency, parallel-programming, distributed-systems]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[InterprocessCommunication]] is the exchange or sharing of information between cooperating processes that need to complete a common task.

## Current Synthesis
Wulc's article frames communication as mandatory once a program is parallelized, because separate processes are still working toward one task. The source names two broad patterns: shared state, where processes access common resources, and [[MessagePassing]], where each communication step copies data into a message.

The tradeoff is consistency and distribution versus memory overhead. Shared state can be efficient and simple for read-only data, but writable shared data needs protections such as mutexes or locks. Message passing uses more memory because data is copied, but the source emphasizes that it improves consistency, works across local and distributed contexts, and is easier for programmers to implement.

## Key Claims
- Cooperating processes need communication to complete one task.
- Shared state lets processes access common resources.
- Writable shared state requires protection against simultaneous modification.
- [[MessagePassing]] improves data consistency by copying data per transfer.
- Message passing applies both locally and in distributed environments.
- Communication style affects scalability and interoperability.

## Evidence
- Communication need: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says communication is necessary because parallelized processes complete the same task.
- Shared-state limits: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says one process's erroneous operation on shared resources can affect others and that distributed use is difficult.
- Protection requirement: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says writable data needs mechanisms such as mutexes or thread locks.
- Message-passing benefits: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says message passing improves consistency, can work locally or distributed, supports scalability and interoperability, and is easier for programmers.

## Counterevidence & Qualifications
The source simplifies a large field. It does not cover concrete IPC primitives such as pipes, sockets, shared memory APIs, queues, actors, channels, or transactional memory, and it does not quantify the memory or latency costs of copying messages.

## What Changed
- Created the concept page from the article's shared-state versus message-passing communication model.

## Related Concepts
- [[MessagePassing]] - one of the two communication models emphasized by the source.
- [[ConcurrentProgramming]] - concurrent processes often need coordination through communication.
- [[ParallelProgramming]] - parallelized processes communicate because they cooperate on one task.
- [[DistributedProgramming]] - distributed work makes message-based communication more natural.
- [[RaceCondition]] - unsafe shared-state updates can produce timing-dependent bugs.
