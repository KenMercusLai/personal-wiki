---
title: "Daniel Lemire"
type: entity
tags: [software-engineer, researcher, performance]
sources:
  - lemire-parsing-json
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[DanielLemire]] is represented in this wiki as the author of a selective JSON-processing benchmark and a contributor to the [[Fastsimdjson]] Python binding for simdjson.

## Current Profile
Lemire frames JSON performance as a joint runtime, parser, allocation, and reduction problem. His example partitions 2.2 million GH Archive events across free-threaded Python workers, keeps counters local to each worker, lazily materializes only accessed JSON values, and merges the small aggregate state after all events have been processed.

## Key Characteristics
- Designs a benchmark around an end-to-end analytical question rather than parser throughput alone.
- Attributes much of the measured advantage to avoiding discarded Python-object creation.
- Uses independent per-thread state to keep synchronization out of the event-processing hot path.

## Evidence
- Workload design: [[lemire-parsing-json]] counts event types and opened pull requests by repository language across 7.6 GB of GH Archive NDJSON.
- Selective materialization: [[lemire-parsing-json]] compares lazy fastsimdjson views with typed msgspec structures and fully materializing parsers.
- Parallel reduction: [[lemire-parsing-json]] gives each thread two counters and merges them only after `map_many` returns.

## Qualifications
This profile is bounded to one article and does not attempt a general biography or independent account of Lemire's broader research. The benchmark and library characterization are author-supplied, hardware- and version-specific, and do not include independent reproduction or full end-to-end I/O cost.

## What Changed
- Created a source-bounded profile of Lemire's JSON parsing and parallel-reduction work.

## Relationships
- [[Fastsimdjson]] - Python binding whose lazy parallel interface Lemire benchmarks.
- [[SelectiveJSONParsing]] - optimization principle emphasized by the benchmark.
- [[Python]] - runtime used for the free-threaded experiment.
- [[ParallelProgramming]] - work is distributed across 64 CPU threads with local aggregation.
