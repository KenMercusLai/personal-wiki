---
title: "SSD Write Amplification"
type: concept
tags: [ssd, flash, storage, endurance, performance]
sources:
  - samsung-data-placement
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[SSDWriteAmplification]] is the ratio of physical writes performed by an SSD to logical writes requested by its host, with a value of 1 meaning no additional device writes.

## Current Synthesis
NAND flash writes pages but erases much larger blocks and cannot overwrite data in place. An SSD therefore redirects an update to a free page, invalidates the old page, and later reclaims space through garbage collection. When an erase block mixes invalid pages with still-valid data, the device must relocate the valid pages before erasing it; those relocation writes raise WAF, consume finite program/erase cycles, and add latency.

Workload shape and placement determine how much valid data must move. Sequential overwrites can invalidate whole erase blocks and approach WAF 1, while random writes and data with different overwrite rates can create fragmented blocks. [[SSDDataPlacement]] tries to segregate data with similar lifetimes so invalidation and reclamation align more closely.

## Key Claims
- WAF measures device writes divided by host writes; 1 is the ideal device-level value.
- Garbage collection raises WAF when reclaiming a block requires copying its remaining valid pages.
- Higher device WAF consumes NAND endurance and can degrade latency, throughput, and quality of service.
- Sequentiality and grouping data by overwrite rate can reduce valid-page relocation.
- Device WAF alone can hide write amplification moved into host software by interfaces such as [[ZonedNamespaceStorage]].

## Evidence
- Erase-before-write mechanism: [[samsung-data-placement]] explains redirected page writes, invalidation, logical-to-physical mapping updates, and block garbage collection.
- Workload effect: [[samsung-data-placement]] contrasts whole-block invalidation under sequential writes with mixed valid and invalid pages under random writes.
- System boundary: [[samsung-data-placement]] distinguishes ZNS's guaranteed device WAF 1 from application and end-to-end amplification created by host-managed zones.

## Counterevidence & Qualifications
The source gives the governing mechanism but no measured WAF distributions, tail-latency results, endurance tests, device models, workloads, or implementation comparisons. WAF 1 is an interface- or workload-conditioned device result, not proof of minimum total writes, best application performance, or lowest cost. Controllers may also differ in overprovisioning, mapping, wear levelling, caching, and garbage-collection policy.

## What Changed
- Established the distinction between device WAF and end-to-end amplification.
- Connected data temperature and sequential invalidation to garbage-collection cost.

## Related Concepts
- [[SSDDataPlacement]] - organizes host writes to reduce the valid data moved during device garbage collection.
- [[FlexibleDataPlacement]] - uses placement separation and device feedback to pursue WAF near 1.
- [[ZonedNamespaceStorage]] - guarantees device WAF 1 through sequential zones while potentially shifting amplification to the host.
- [[StoragePerformanceBenchmarking]] - tests whether lower WAF improves endurance, latency, throughput, and cost under representative workloads.
