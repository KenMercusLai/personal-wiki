---
title: "MaskRay"
type: entity
tags: [software-engineering, linkers, linux, performance]
sources:
  - linker-io-tricks-and-their-downsides
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[MaskRay]] is a systems practitioner and technical author who, in the available source, investigates linker performance through filesystem, process, and Linux memory behavior.

## Current Profile
The source shows MaskRay combining implementation-history research with controlled microbenchmarks, system counters, failure demonstrations, and end-to-end linker runs. The analysis emphasizes semantic and measurement boundaries: whether an output keeps its inode, when a build considers a process complete, which resource counters follow forked work, and whether hugepage requests trigger compaction. The author rejects adopting in-place output reuse in lld on the evidence presented and recommends disabling fork mode when benchmarking, profiling, debugging, or budgeting memory.

## Key Characteristics
- Investigates performance claims across application, filesystem, process, and kernel layers.
- Uses counterexamples and negative controls to distinguish visible overhead from causal bottlenecks.
- Treats compatibility and observability changes as costs even when wall time improves.
- Makes practical recommendations while stating missing configurations and unmeasured cases.

## Evidence
- Experimental method: [[linker-io-tricks-and-their-downsides]] varies inode reuse, cache residency, fork mode, page size, storage medium, and hugepage interception while consulting device, VM, and cgroup counters.
- Correctness analysis: [[linker-io-tricks-and-their-downsides]] demonstrates hard-link mutation, failed-output corruption, and a qemu-user mapped binary changing while running.
- Qualified judgment: [[linker-io-tricks-and-their-downsides]] declines the lld optimization and explicitly notes missing `enabled=madvise` data and the need to check the Rust mold port against the C++ release.

## Qualifications
This is a source-bounded profile, not a general biography or complete account of MaskRay's work. The page does not independently verify authorship identity beyond the archived MaskRay blog URL, project roles, benchmark reproduction, or the current state of the referenced linker implementations.

## What Changed
- Established a source-bounded profile centered on linker and kernel performance analysis.
- Recorded the author's emphasis on causal controls and semantic compatibility.

## Relationships
- [[MoldLinker]] - principal linker implementation examined in the study.
- [[WildLinker]] - compared implementation using related optimizations.
- [[LinkerOptimizationTradeoffs]] - central synthesis developed from the author's experiments.
- [[StoragePerformanceBenchmarking]] - methodological connection through cache control, counters, and counterfactuals.
