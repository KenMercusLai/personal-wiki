---
title: "Selective JSON Parsing"
type: concept
tags: [json, parsing, performance, data-processing]
sources:
  - lemire-parsing-json
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[SelectiveJSONParsing]] processes only fields needed by an application and avoids eagerly constructing native objects for the remainder of each JSON document.

## Current Synthesis
Selective parsing matters when records are large but the computation touches few fields. Lemire's GH Archive task reads event type for every roughly 3.4 kB object, then descends into pull-request payload fields only for opened pull requests. Fastsimdjson expresses that access pattern through lazy views; msgspec expresses it through typed structures that declare required fields in advance.

The benchmark suggests that object materialization can dominate parsing work at this selectivity. On one core, lazy fastsimdjson reportedly reaches 2.13 GB/s versus 0.63 GB/s for its eager mode. Across 64 cores, the corresponding results are 65.7 and 29.8 GB/s. Selectivity composes with parallelism rather than replacing it: independent records are distributed across threads, while small thread-local summaries are merged after parsing.

## Key Claims
- Application access patterns, not only JSON syntax scanning, determine end-to-end parsing cost.
- Lazy views defer native-object creation until code accesses a value.
- Typed partial schemas can skip unused fields but require the needed structure to be declared beforehand.
- Thread-local aggregation keeps shared mutation and synchronization outside the per-record hot path.
- Selective materialization and multi-core record partitioning can provide complementary gains.

## Evidence
- Sparse field use: [[lemire-parsing-json]] accesses only event type for most GH Archive records and nested action and language fields for qualifying pull requests.
- One-core comparison: [[lemire-parsing-json]] reports 2.13 GB/s for lazy fastsimdjson, 1.29 GB/s for typed msgspec, and 0.63 GB/s for eager fastsimdjson.
- Parallel comparison: [[lemire-parsing-json]] reports 65.7 GB/s for lazy fastsimdjson across 64 cores, about 31 times its one-core throughput.
- Reduction design: [[lemire-parsing-json]] creates a counter pair per thread and combines only the final compact summaries.

## Counterevidence & Qualifications
Selective parsing helps only when ignored data is substantial and downstream code does not later demand full materialization. Lazy access can move work into later operations, typed schemas trade flexibility for advance declaration, and callback or aggregation cost may dominate simpler documents. The supplied evidence is one author-run, best-case benchmark with decompressed in-memory data, fixed software versions, one server, one document distribution, and no independent replication, memory, energy, malformed-input, or tail-latency comparison.

## What Changed
- Created the concept from the contrast between lazy views, typed partial structures, and eager object materialization.
- Connected selective parsing to thread-local reduction and free-threaded record parallelism.

## Related Concepts
- [[ParallelProgramming]] - partitions independent JSON records across CPU threads.
- [[Python]] - native-object creation is the allocation cost avoided in the benchmark.
- [[Fastsimdjson]] - implements the source's lazy-view strategy.
- [[StoragePerformanceBenchmarking]] - shares the requirement to define cache, data-residency, workload, and measurement boundaries before generalizing throughput.
