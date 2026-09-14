---
title: "Extract Value Streams"
type: concept
tags: [software-architecture, legacy-systems, migration]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ExtractValueStreams]] is a legacy-displacement sequencing approach where a business value stream or capability is moved out of a legacy system while surrounding legacy processes continue operating.

## Current Synthesis
The Legacy Mimic article uses Logistics as the example value stream extracted from a legacy system that also supports Sales and Business Performance. Extracting that capability changes the architecture before every dependent process has moved. As a result, the transition needs event interception from legacy sales and metrics replication back into legacy reporting.

The pattern matters here less as a full standalone taxonomy than as the trigger for old/new coexistence. Once a value stream leaves the monolith, [[LegacyMimic]] components may be needed so unreplaced processes can continue to use the interfaces and data shapes they expect.

## Key Claims
- Extracting a value stream can make modernization incremental instead of all-at-once.
- The extracted capability may still depend on legacy upstream events or downstream reporting needs.
- Value-stream extraction creates temporary architecture that must satisfy both new-domain and legacy-contract requirements.
- Mimics and anti-corruption layers help keep the extracted system useful without fully inheriting the legacy model.

## Evidence
- Example choice: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says extracting the Logistics capability is the option being considered.
- Before/after diagrams: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] shows Sales, Logistics, and Business Performance inside one legacy system, then Logistics as a New Logistics System outside it.
- Transition effects: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] shows event interception for sales fulfillment and a legacy mimic for business-performance metrics.

## Counterevidence & Qualifications
The article only sketches Extract Value Streams enough to explain the Legacy Mimic pattern. It does not define selection criteria for which value stream to extract first or how to govern the full migration program.

## What Changed
- Created the concept from the article's logistics extraction example.

## Related Concepts
- [[LegacyDisplacement]] - value-stream extraction is one sequencing approach for displacement.
- [[TransitionalArchitecture]] - extracted value streams create old/new coexistence.
- [[LegacyMimic]] - keeps legacy neighbors functioning around an extracted value stream.
- [[EventInterception]] - feeds legacy activity into the extracted system.
- [[CapabilityOrientedIntegration]] - extracted value streams benefit from clear capability boundaries.
