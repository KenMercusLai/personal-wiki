---
title: "Flexible Data Placement"
type: concept
tags: [nvme, ssd, data-placement, storage]
sources:
  - samsung-data-placement
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[FlexibleDataPlacement]] is an NVMe SSD interface that lets hosts segregate writes through placement identifiers and observe device state while the SSD retains logical-to-physical mapping, garbage collection, and NAND-media management.

## Current Synthesis
FDP occupies a middle position in [[SSDDataPlacement]]. Like Streams, it can preserve normal sequential, random, and overwrite behavior and remain backward compatible when a host does not opt into placement. Unlike hint-only Streams, it provides a feedback loop: the device exposes state and logs that let the host keep writes aligned with available placement resources and adjust its policy.

Samsung presents this combination as a route toward [[SSDWriteAmplification]] near 1 without the application redesign demanded by [[ZonedNamespaceStorage]] or the host-side media management of Open Channel SSDs. The result is conditional rather than automatic: the host still needs useful workload groupings, placement logic, feedback handling, and measurements proving that lower device amplification outweighs integration and operational cost.

## Key Claims
- FDP separates logical writes while leaving the FTL and NAND-media management inside the SSD.
- It is backward compatible with the conventional block interface and permits sequential, random, and overwrite traffic.
- Device feedback distinguishes FDP from Streams' write hints and enables policy adjustment toward WAF near 1.
- Its comparison table describes static write-resource allocation, placement IDs independent of LBA, and sharing across one or more namespaces.
- FDP trades ZNS's hard WAF guarantee for lower host-stack disruption and broader write-pattern compatibility.

## Evidence
- Host-device split: [[samsung-data-placement]] places L2P mapping, garbage collection, and media management inside the SSD for Streams and FDP.
- Feedback behavior: [[samsung-data-placement]] says FDP exposes device state and logs so host placement logic can remain aligned and be tuned.
- Interface comparison: [[samsung-data-placement]] contrasts FDP's ordinary writes, boundary crossing, submission-time LBA knowledge, static resource allocation, and multi-namespace use with ZNS.
- Adoption thesis: [[samsung-data-placement]] describes FDP as customer-driven and optimized for high placement benefit with limited integration effort.

## Counterevidence & Qualifications
The source is a Samsung-authored advocacy article rather than a neutral standard analysis or controlled benchmark. It does not quantify integration effort, feedback-loop stability, resource contention, failure recovery, multi-tenant behavior, tail latency, or end-to-end WAF. “Near 1” is an achievable target conditioned on workload and host policy, not an interface guarantee, and ecosystem-status claims are time-sensitive.

## What Changed
- Established feedback, compatibility, and retained device media management as FDP's defining combination.
- Distinguished achievable near-1 WAF from ZNS's interface-level device guarantee.

## Related Concepts
- [[SSDDataPlacement]] - provides the larger host-control spectrum in which FDP occupies a middle position.
- [[SSDWriteAmplification]] - is the primary optimization target of FDP's placement and feedback loop.
- [[ZonedNamespaceStorage]] - offers stricter sequential placement and a device-WAF guarantee at higher host complexity.
- [[StoragePerformanceBenchmarking]] - is needed to verify FDP's workload-specific amplification and QoS benefits.
