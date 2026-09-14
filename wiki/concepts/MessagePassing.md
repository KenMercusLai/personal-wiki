---
title: "Message Passing"
type: concept
tags: [concurrency, distributed-systems, communication]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[MessagePassing]] is a communication model where processes exchange copied data through messages rather than directly sharing mutable state.

## Current Synthesis
Wulc presents message passing as the safer and more portable alternative to shared state in parallelized programs. Each transfer copies data, which costs more memory than shared-resource access, but the article argues that copying strengthens data consistency and lets the same communication idea work for both local multiprocessing and distributed environments.

The source's emphasis is practical: message passing can reduce shared-state interference, support scalability, allow interoperability between different systems, and be easier for programmers to implement. That does not remove all distributed-system difficulty, but it narrows one class of shared-memory synchronization risk.

## Key Claims
- Message passing copies data for each communication event.
- Copying improves consistency compared with mutable shared state in the source's framing.
- Message passing can operate in local multiprocessing and distributed environments.
- The model supports scalability and interoperability across systems.
- Message passing uses more memory than direct shared-state communication.

## Evidence
- Copy semantics: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says each message transfer copies a piece of data.
- Consistency claim: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] argues that message passing greatly improves data consistency.
- Distributed fit: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] says messages can be transmitted locally or in a distributed environment.
- Tradeoff: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] explicitly notes higher memory use than shared state.

## Counterevidence & Qualifications
The article does not compare specific message systems or address ordering, delivery guarantees, serialization costs, backpressure, idempotency, or failure recovery. Its claims are introductory and model-level.

## What Changed
- Created the concept page from Wulc's message-passing communication section.

## Related Concepts
- [[InterprocessCommunication]] - message passing is one of the source's two IPC families.
- [[DistributedProgramming]] - distributed programming relies naturally on network-transferable messages.
- [[RaceCondition]] - message passing can avoid some shared-memory races by avoiding direct mutable sharing.
- [[ParallelProgramming]] - parallel processes may use messages to coordinate work.
