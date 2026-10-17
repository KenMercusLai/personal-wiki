---
title: "SSD Data Placement"
type: concept
tags: [ssd, nvme, flash, storage-architecture]
sources:
  - samsung-data-placement
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[SSDDataPlacement]] is host-device coordination that influences which physical erase regions receive logical writes so data with compatible lifetimes can be reclaimed with less movement.

## Current Synthesis
The design space trades host knowledge against device expertise. A conventional SSD hides placement and media management behind a block interface, but cannot directly infer application-level overwrite patterns. At the opposite extreme, Open Channel SSDs expose physical geometry and require a host FTL, giving strong control at the cost of vendor-sensitive wear, error, and NAND-management work.

The durable middle ground keeps media management in the SSD while exposing enough intent or structure to separate writes. NVMe Streams supplies hints but no feedback; [[FlexibleDataPlacement]] adds placement resources and device-state feedback while retaining ordinary block behavior; [[ZonedNamespaceStorage]] enforces sequential, host-managed zones and shifts mapping and reclamation further upward. Adoption therefore depends on interface compatibility, state-management burden, demonstrated workloads, ecosystem support, and end-to-end amplification—not only the minimum device WAF.

## Key Claims
- Mixing data with different overwrite rates in the same erase blocks can increase valid-page relocation and [[SSDWriteAmplification]].
- The host knows workload semantics, while the SSD is better placed to manage device-specific NAND behavior.
- More host control can lower device WAF but increase application state, integration work, and compatibility costs.
- Backward compatibility and compelling deployed use cases matter independently of interface simplicity.
- Workload shape should choose the placement interface; no single mechanism is established as universally best.

## Evidence
- Responsibility spectrum: [[samsung-data-placement]] places conventional SSDs, Streams, FDP, ZNS, and OCSSD in increasing order of host control.
- Historical tradeoff: [[samsung-data-placement]] attributes OCSSD's decline to host-media complexity, Streams' decline to weak use cases and adoption, and ZNS's limited NVMe traction to sequential-interface redesign costs.
- Middle-ground design: [[samsung-data-placement]] presents FDP as host-directed segregation plus feedback while leaving mapping, garbage collection, and media management in the SSD.
- Workload fit: [[samsung-data-placement]] favors ZNS for inherently log-structured writes and FDP as a lower-effort experiment for conventional random-write stacks.

## Counterevidence & Qualifications
The historical and adoption judgments come from a Samsung article advocating FDP and are not independently quantified. A simplified control spectrum can hide device implementation, host software quality, overprovisioning, failure recovery, multi-tenancy, tail latency, cost, and operational maturity. “Minimal changes” and “low traction” are ecosystem- and time-dependent claims, while actual end-to-end results require matched workload measurements.

## What Changed
- Established host-control, compatibility, and integration effort as coequal design dimensions.
- Preserved media management as a distinct responsibility from logical data placement.
- Made workload fit, rather than a universal winner, the current judgment.

## Related Concepts
- [[SSDWriteAmplification]] - supplies the principal device-level cost that placement tries to reduce.
- [[FlexibleDataPlacement]] - represents a feedback-based, backward-compatible middle position.
- [[ZonedNamespaceStorage]] - represents a stricter host-managed placement interface with sequential zones.
- [[StoragePerformanceBenchmarking]] - evaluates placement mechanisms across physical writes, application writes, QoS, endurance, and engineering cost.
