---
title: "Virtual Memory"
type: concept
tags: [operating-systems, linux, memory, x86-64]
sources:
  - virtual-memory
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Definition
[[VirtualMemory]] is the hardware-and-kernel abstraction that gives each process a protected virtual address space and translates its used pages to physical frames with permissions, residency state, and backing semantics.

## Current Synthesis
Virtual memory is simultaneously an isolation mechanism, a sparse naming system, and a policy surface. VMAs describe valid ranges and permissions at a coarse level; hierarchical page tables describe current page-level mappings; the MMU enforces translations and permissions; and the TLB caches recent translations. This separation lets large address ranges be reserved without consuming equal RAM, lets physical frames be allocated and reclaimed lazily, and lets processes share code, files, or COW pages without exposing physical layout.

The abstraction is intentionally incomplete for performance reasoning. Page size, access order, working-set size, fault path, page type, cross-core invalidation, and NUMA placement determine costs that adjacent virtual addresses do not reveal. Correct diagnosis therefore separates reservation from residency, faults from translation misses, and logical locality from physical placement.

## Key Claims
- Per-process address spaces and page permissions provide memory isolation while allowing controlled sharing.
- Sparse multilevel page tables avoid allocating a flat entry for every possible virtual page.
- VMAs record valid intended mappings, while page tables and PTE state record current physical realization.
- TLBs make translation practical but expose page-granular locality and capacity limits.
- The same abstraction supports demand paging, copy-on-write, file mappings, swap, huge pages, and page migration.
- Virtual-address uniformity hides heterogeneous costs from storage faults, reclaim, shootdowns, and NUMA topology.

## Evidence
- Address-space and translation structure: [[virtual-memory]] describes Linux segments, four-level x86-64 page tables, canonical addresses, CR3-rooted hardware walks, and permission bits.
- Lazy and shared realization: [[virtual-memory]] traces first-touch allocation, swapped and file-backed faults, COW after `fork`, and page-cache mappings.
- Performance boundaries: [[virtual-memory]] relates access patterns, page sizes, TLB reach, multicore invalidation, and NUMA placement to application behavior.

## Counterevidence & Qualifications
The source centers Linux and common x86-64 four-level configurations. Other architectures and operating systems use different address widths, table structures, page sizes, fault semantics, and reclaim policies; even within Linux, five-level paging, kernel mitigations, allocator behavior, THP policy, and CPU-specific TLBs change details. Virtual memory enables overcommit and transparent recovery, but it cannot make an oversized hot working set cheap: under sustained pressure, reclaim can become thrashing.

## What Changed
- Created a unified model joining isolation, sparse translation, lazy residency, sharing, and hidden physical cost.

## Related Concepts
- [[DemandPagingAndReclaim]] - turns address-space promises into resident pages and later frees frames under pressure.
- [[MemoryMappedIO]] - uses virtual mappings to expose page-cache-backed file data.
- [[NUMAMemoryPlacement]] - locates physical frames within the topology hidden by virtual addresses.
- [[LatencyHierarchy]] - places TLB lookup, page walks, DRAM, and storage faults on different cost scales.
- [[HighThroughputIOOptimization]] - applies page and translation mechanics to end-to-end data paths.
