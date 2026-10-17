---
title: "fastsimdjson"
type: entity
tags: [python, json, parser, software-library]
sources:
  - lemire-parsing-json
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[Fastsimdjson]] is a Python binding for simdjson that exposes multi-threaded event mapping and optional lazy JSON views.

## Current Profile
In Lemire's benchmark, `map_many` partitions newline-delimited JSON events across a requested number of threads and invokes a Python callback for each event. With `lazy=True`, the callback receives a parsed view that creates Python objects only for values the callback accesses. Combined with free-threaded Python 3.14 and thread-local counters, the library reportedly reaches 65.7 GB/s on a 64-core dual-Xeon server.

## Key Characteristics
- Maps NDJSON records across multiple threads inside one Python process.
- Offers lazy views that defer Python-object creation until a value is accessed.
- Returns after every event callback completes, allowing a separate reduction over thread-local state.
- Also supports eager parsing, which isolates some of the lazy-materialization benefit in the reported comparison.

## Evidence
- Interface: [[lemire-parsing-json]] uses `map_many(callback, data, format="lines", threads=64, lazy=True)` over an in-memory byte buffer.
- Selective access: [[lemire-parsing-json]] reads event type and a nested pull-request language only when the event qualifies.
- Reported performance: [[lemire-parsing-json]] measures 2.13 GB/s on one core and 65.7 GB/s on 64 cores for lazy mode, versus 0.63 and 29.8 GB/s for eager mode.

## Qualifications
The page reflects fastsimdjson 0.6.0 through one maintainer-authored benchmark. Results depend on the tested processor, free-threaded Python build, input shape, callback work, accessed-field fraction, memory residency, and best-run protocol. The source does not evaluate malformed-input behavior, API completeness, memory use, portability, tail latency, or production reliability.

## What Changed
- Created the library profile with its parallel mapping, lazy-view behavior, measured results, and benchmark limits.

## Relationships
- [[DanielLemire]] - author who presents and benchmarks the binding.
- [[Python]] - language runtime and object model at the library boundary.
- [[SelectiveJSONParsing]] - lazy views implement on-demand value materialization.
- [[ParallelProgramming]] - `map_many` partitions record processing across threads.
