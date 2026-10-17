---
title: "Zoned Namespace Storage"
type: concept
tags: [nvme, zns, ssd, zoned-storage]
sources:
  - samsung-data-placement
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[ZonedNamespaceStorage]] is an NVMe data-placement interface that partitions logical address space into host-managed zones and requires writes within each zone to proceed sequentially.

## Current Synthesis
ZNS transfers logical placement, mapping, reclamation, and zone state to the host while leaving NAND-media management inside the SSD. Sequential zone writes align logical invalidation with erase behavior and guarantee device [[SSDWriteAmplification]] of 1, avoiding internal relocation by the SSD.

That guarantee narrows the measurement boundary rather than eliminating all write cost. A host must maintain mappings, select zones, garbage-collect or rewrite live application data, reset zones, and recover state. Already log-structured workloads can fit this model naturally, while random-write applications may need extensive redesign and can incur application-level amplification. ZNS therefore trades a strict device contract for host complexity, non-backward-compatible semantics, and workload dependence.

## Key Claims
- ZNS uses sequentially written zones as its basic host-managed placement unit.
- The host owns logical mapping, zone state, garbage collection, and zone reuse; the SSD retains media management.
- Sequential-zone rules guarantee device WAF 1 but do not guarantee end-to-end WAF 1.
- The interface fits inherently sequential or log-structured workloads better than arbitrary random-write stacks.
- Strict ordering and a nonconventional block interface can require substantial host-stack redesign.

## Evidence
- Responsibility boundary: [[samsung-data-placement]] shows L2P mapping and garbage collection in the host while media management remains in the SSD.
- Interface rules: [[samsung-data-placement]] describes sequential-only writes, boundary restrictions, LBA-based placement, zone append behavior, and host data-movement notifications.
- Amplification boundary: [[samsung-data-placement]] distinguishes guaranteed device WAF 1 from application and end-to-end amplification created by host zone management.
- Adoption fit: [[samsung-data-placement]] reports standardization and SMR HDD use but lower NVMe traction, attributing difficulty to redesign and fragmented stateful host stacks.

## Counterevidence & Qualifications
The source offers no matched ZNS implementation, measured application amplification, failure-recovery analysis, deployment counts, or independent adoption evidence. Random-write conversion cost depends on the host data structure and software quality, while mature log-structured systems may already possess much of the required machinery. Status and traction claims are time-sensitive and come from a vendor positioning FDP as the easier alternative.

## What Changed
- Established the boundary between guaranteed device WAF and conditional end-to-end WAF.
- Made host state management and workload sequentiality central to the current judgment.

## Related Concepts
- [[SSDDataPlacement]] - positions ZNS toward the high-host-control side of the placement spectrum.
- [[SSDWriteAmplification]] - is eliminated inside the device while potentially reappearing in host relocation work.
- [[FlexibleDataPlacement]] - retains conventional writes and device FTL behavior in exchange for a conditional WAF outcome.
- [[ObjectStorageNativeDatabase]] - shares the broader architectural lesson that moving storage responsibility across layers changes coordination and recovery obligations.
