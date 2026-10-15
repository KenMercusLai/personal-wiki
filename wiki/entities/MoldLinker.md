---
title: "mold"
type: entity
tags: [linker, linux, performance, open-source]
sources:
  - linker-io-tricks-and-their-downsides
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[MoldLinker|mold]] is a high-speed linker whose tested Linux defaults include output-inode reuse, fork-based asynchronous teardown, and transparent-hugepage requests.

## Current Profile
The source presents mold as optimizing the visible edit-relink critical path across filesystem, process, and virtual-memory layers. It renames and reuses an existing output inode when permitted, performs the link in a forked child while the original parent reports completion after publication, and requests huge pages for output and internal mappings. These choices can shorten favorable workloads, but the measured benefit depends on cache warmth, page size, and memory fragmentation, while surrounding tools may observe changed correctness or lifecycle semantics.

## Key Characteristics
- Reuses an existing output inode for non-shared outputs when its guard permits.
- Uses a pipe and fork so the spawned parent can exit before the linking child finishes memory teardown.
- Requests transparent huge pages for output mappings, arenas, and large hash tables.
- Provides `--no-fork`; the article also discusses version- and output-type-specific safeguards around inode reuse.
- Prioritizes visible link latency while exposing filesystem and process-observability tradeoffs.

## Evidence
- Output behavior: [[linker-io-tricks-and-their-downsides]] reconstructs mold's rename, resize, allocation, mmap, write, cleanup, and `ETXTBSY` fallback paths and demonstrates their hard-link and mapped-reader consequences.
- Process behavior: [[linker-io-tricks-and-their-downsides]] traces the pipe notification and early parent exit, then compares accounting, debugger, tracer, and cgroup observations with `--no-fork`.
- Memory behavior: [[linker-io-tricks-and-their-downsides]] measures teardown with 4 KiB and huge pages and compares explicit `MADV_HUGEPAGE` behavior under fragmentation.

## Qualifications
This profile comes from one critical practitioner study using mold 2.42.1's in-development Rust port on Linux 6.18 rather than a comprehensive project history or current specification. Version-specific implementation details and defaults may change. The experiments demonstrate concrete risks and workload dependence, but do not quantify their population-wide incidence or establish that mold is slower or less reliable overall than other linkers.

## What Changed
- Established the three cross-layer optimizations examined in the source.
- Added measured best-case gains, cold-cache reversals, and observability costs.
- Distinguished visible parent completion from total child resource lifetime.

## Relationships
- [[MaskRay]] - authored the examined implementation study and comparison.
- [[WildLinker]] - uses analogous output-reuse, fork, and hugepage techniques.
- [[LinkerOptimizationTradeoffs]] - synthesizes the benefits and hazards of mold's examined defaults.
- [[StoragePerformanceBenchmarking]] - provides the controls needed to interpret its timing results.
