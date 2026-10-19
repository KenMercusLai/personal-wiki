---
title: "Demand Paging and Reclaim"
type: concept
tags: [operating-systems, linux, memory, paging]
sources:
  - virtual-memory
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Definition
[[DemandPagingAndReclaim]] is the Linux memory lifecycle in which valid virtual ranges receive physical frames on access and cold frames are later dropped, written back, or swapped according to their backing and state.

## Current Synthesis
Allocation first creates or extends a VMA, which records an address range, permissions, and backing. A first access to an absent page traps into the kernel; the fault handler validates the VMA, selects the resolution path, installs a PTE, and retries the instruction. Anonymous first touch can be satisfied with a zero-filled frame, while cold file data or swapped anonymous data requires storage I/O.

Under pressure, Linux approximates recency using hardware accessed bits, reverse mappings, and aging structures rather than observing every access. Reclaim cost depends on what preserves the page's contents: clean file-backed pages can be discarded, dirty file-backed pages require writeback, and private anonymous or tmpfs data generally requires swap. The relevant capacity boundary is therefore the hot working set and the cost of recovering evicted pages, not simply free RAM.

## Key Claims
- A VMA can promise usable address space before any page table entry or physical frame exists.
- Minor faults require no storage I/O; major faults load file or swap data and are much more expensive.
- Zero-filling reused frames is both demand-allocation behavior and a cross-process confidentiality invariant.
- Reclaim estimates coldness from accessed bits and reverse mappings rather than exact per-access LRU tracking.
- Clean file cache, dirty file pages, anonymous memory, and tmpfs have different eviction paths and costs.
- When active working sets exceed RAM, repeated eviction and refaulting can turn reclaim into thrashing.

## Evidence
- Fault lifecycle: [[virtual-memory]] distinguishes VMA intent from PTE residency and diagrams validation, allocation, mapping, and retry.
- Absence paths: [[virtual-memory]] separates anonymous first touch, swap restoration, file first access, and dropped file-cache reload.
- Reclaim policy: [[virtual-memory]] explains accessed-bit sampling, rmap lookup, active/inactive aging, MGLRU, `kswapd`, direct reclaim, and page-type costs.
- Operational signals: [[virtual-memory]] recommends major-fault counts, `vmstat` swap activity, `/proc/meminfo`, and memory PSI to identify pressure and stalls.

## Counterevidence & Qualifications
The active/inactive-list account is a teaching simplification, and contemporary Linux may use MGLRU or configuration-specific reclaim behavior. A non-present entry does not by itself identify one cause; VMA metadata, PTE encoding, backing type, and fault context determine the path. Major-fault counts include cold file I/O as well as swap, while low free memory can be healthy when much of RAM is clean reclaimable cache. Overcommit policy and OOM selection are tunable and do not guarantee graceful behavior.

## What Changed
- Created a lifecycle synthesis that joins allocation-time promises, fault-time realization, and pressure-time eviction.

## Related Concepts
- [[VirtualMemory]] - supplies the VMAs, PTEs, permissions, and MMU faults used by the lifecycle.
- [[MemoryMappedIO]] - provides the file-backed and page-cache fault paths.
- [[MemoryCompaction]] - can reorganize physical memory when contiguous allocations are needed.
- [[LatencyHierarchy]] - distinguishes in-memory faults from storage-backed major faults.
- [[ServiceObservability]] - exposes residency, faults, swapping, and pressure stalls.
