---
title: "Memory-Mapped I/O"
type: concept
tags: [io, linux, mmap, page-cache]
sources:
  - virtual-memory
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Definition
[[MemoryMappedIO]] maps file-backed page-cache data into a process's virtual address space so ordinary loads and stores drive file access through page faults and page-table mappings.

## Current Synthesis
Buffered `read()` and `mmap()` normally share the same page cache. `read()` copies cached bytes into a caller-owned buffer, while `mmap()` installs PTEs that point to page-cache frames and avoids that copy. The latter is useful for repeated, random, shared, or pointer-oriented access, but it is not free: cold access faults, mappings consume page-table and TLB capacity, invalidation can require shootdowns, and truncation can surface as `SIGBUS` rather than an ordinary read error.

Write semantics depend on mapping mode. `MAP_SHARED` modifies the shared page-cache page and relies on writeback or explicit synchronization for durability; `MAP_PRIVATE` uses COW so modifications diverge into anonymous private pages and do not change the file. Direct I/O is a different choice: it bypasses the normal page-cache path for applications prepared to own buffering, alignment, scheduling, and caching policy.

## Key Claims
- `read()` and `mmap()` usually obtain file contents through the page cache but expose them to user space differently.
- `mmap()` removes the page-cache-to-user-buffer copy by mapping the cache frame directly.
- Cold mappings pay fault and PTE-installation costs, so sequential buffered I/O can remain competitive or faster.
- `MAP_SHARED` and `MAP_PRIVATE` separate shared writeback semantics from private COW divergence.
- Mapped pages can be reclaimed safely because the VMA persists and a later access can reload and remap the data.
- Direct I/O trades kernel cache services for application control and additional alignment and lifecycle responsibility.

## Evidence
- Data paths: [[virtual-memory]] contrasts disk-to-page-cache-to-buffer `read()` with disk-to-page-cache-to-PTE `mmap()`.
- Mapping semantics: [[virtual-memory]] diagrams shared page-cache writes and private COW writes and classifies mappings along backing and visibility axes.
- Tradeoffs: [[virtual-memory]] identifies fault frequency, readahead, page tables, TLB pressure, shootdowns, truncation behavior, and access pattern as workload-dependent costs.

## Counterevidence & Qualifications
Calling `mmap()` “zero-copy” describes one avoided copy, not an absence of I/O, faults, cache traffic, writeback, or kernel work. Readahead exists on both buffered and mapped paths, and actual results depend on file size, access order, reuse, storage, kernel, page size, memory pressure, and measurement boundary. `MAP_SHARED` visibility does not itself guarantee durable storage; explicit synchronization and filesystem semantics remain relevant. `O_DIRECT` requirements and behavior vary by filesystem and device.

## What Changed
- Created a workload-conditional synthesis of buffered I/O, mapped I/O, mapping modes, and direct I/O.

## Related Concepts
- [[VirtualMemory]] - provides the VMA, PTE, permission, and fault mechanisms used by mappings.
- [[DemandPagingAndReclaim]] - loads cold file pages and drops or writes back mapped cache pages.
- [[HighThroughputIOOptimization]] - evaluates copies, page preparation, translation, and storage together.
- [[StoragePerformanceBenchmarking]] - determines which I/O path is favorable for the actual workload.
- [[LatencyHierarchy]] - separates copy, page-fault, page-walk, DRAM, and storage costs.
