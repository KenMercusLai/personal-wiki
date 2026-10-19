---
title: "NUMA Memory Placement"
type: concept
tags: [numa, memory, performance, linux]
sources:
  - virtual-memory
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Definition
[[NUMAMemoryPlacement]] is the assignment of physical pages and executing threads across non-uniform memory-access nodes so hot accesses use appropriate local memory or deliberately balance bandwidth across controllers.

## Current Synthesis
Virtual addresses hide which socket owns the backing physical frame. Linux commonly allocates anonymous pages near the CPU that first faults them, so a single-threaded initialization can place a whole shared buffer on one node even when later workers span several sockets. Threads near that node receive local DRAM service; remote threads cross an inter-socket link and can experience consistently higher latency.

For partitioned data, locality comes from coordinating first touch, work partitioning, and CPU affinity. Heavily shared data has no universally local placement: binding favors one node, interleaving distributes capacity and bandwidth while accepting mixed locality, and replication may exchange memory for reads. Automatic NUMA balancing can migrate pages or tasks after observing accesses, but its sampling faults and reactive behavior make deliberate placement more predictable for latency-sensitive workloads.

## Key Claims
- Virtual-memory contiguity does not imply one NUMA node or uniform DRAM latency.
- First-touch allocation couples initialization CPU placement to later physical page placement.
- Thread pinning is necessary when locality assumptions would otherwise be broken by scheduler migration.
- Per-range binding and preferred-node policies give explicit placement control with different fallback behavior.
- Interleaving trades perfect locality for balanced bandwidth across memory controllers.
- Automatic NUMA balancing can repair some misplacement but adds observation and migration overhead after the fact.

## Evidence
- Placement mechanism: [[virtual-memory]] traces page faults from an initializing thread on socket 0 to physical frames on node 0.
- Performance symptom: [[virtual-memory]] shows identical workers splitting into fast local and slower remote groups when they access the same first-touch-placed buffer.
- Controls: [[virtual-memory]] describes affinity, `mbind`, `set_mempolicy`, `numactl`, interleaving, automatic balancing, `numastat`, and `/proc/<pid>/numa_maps`.

## Counterevidence & Qualifications
The source's two-socket diagram is illustrative, and real systems can expose multiple NUMA nodes per socket or more complex distances. Remote-to-local latency ratios vary by CPU, memory, cache state, interconnect, and workload; cache hits may hide DRAM placement entirely. Interleaving can improve bandwidth while worsening locality, and pinning can reduce scheduler flexibility. Stable per-thread slowness should be confirmed against CPU and page placement rather than assumed to be NUMA, because IRQ affinity, locks, frequency, and thermal effects can look similar.

## What Changed
- Created a synthesis connecting first-touch faults, thread affinity, shared-data policy, and NUMA diagnosis.

## Related Concepts
- [[VirtualMemory]] - hides the physical-node identity that placement policy determines.
- [[DemandPagingAndReclaim]] - allocates and may later migrate physical frames at fault and reclaim time.
- [[HighThroughputIOOptimization]] - requires worker, buffer, device, and NIC locality to be considered as one pipeline.
- [[TopologyAwareBuildCaching]] - applies physical and network topology awareness to a different placement problem.
- [[LatencyHierarchy]] - locates local and remote DRAM at distinct effective latency tiers.
