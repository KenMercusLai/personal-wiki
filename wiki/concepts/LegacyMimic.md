---
title: "Legacy Mimic"
type: concept
tags: [software-architecture, legacy-systems, migration]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[LegacyMimic]] is a transitional architecture pattern where a new or replacement component deliberately conforms to a legacy interface, event stream, database schema, or semantic contract so an incremental migration can keep existing processes running.

## Current Synthesis
Cartwright, Horn, and Lewis frame Legacy Mimic as an enabler for incremental [[LegacyDisplacement]]. During displacement, the target system cannot always be isolated from the existing system. Old processes may still need data from newly extracted capabilities, and new capabilities may still need events, requests, or records emitted by the old world. The mimic exists to honor those contracts while the migration sequence continues.

The source distinguishes two common forms. A service-providing mimic hides a new implementation behind a legacy-facing interface, as with an [[EventInterception]] component consuming legacy sales events and forwarding work into a new logistics system. A service-consuming mimic lets the new world interact with an unreplaced legacy system through that system's existing interface, as with a metrics component updating a legacy reporting database using the expected schema and semantics.

## Key Claims
- Legacy mimics preserve existing contracts during incremental replacement.
- A service-providing mimic presents a legacy-compatible surface over new implementation behavior.
- A service-consuming mimic calls or writes to legacy systems through their existing interfaces.
- Mimics often use services, adapters, translators, and facades.
- A mimic is transitional and should not be mistaken for a permanent target-architecture component.
- [[AntiCorruptionLayer]] and Legacy Mimic share adapter and translation forces, but differ when the adapter is enduring rather than temporary.

## Evidence
- Migration need: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says new systems may need to meet existing, often implicit, contracts to keep legacy processes running.
- Service-providing form: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] describes a new implementation encapsulated behind a legacy interface so legacy collaborators do not see the replacement.
- Service-consuming form: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] describes new components collaborating with unreplaced legacy systems through existing legacy interfaces.
- Visual evidence: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] includes inspected diagrams showing a legacy sales event intercepted for a new logistics system and logistics metrics written back into a legacy database.
- Transience: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says the event interceptor and metrics mimic in the example do not endure in the target architecture.

## Counterevidence & Qualifications
The source is pattern guidance rather than empirical migration evidence. It also warns by implication that mimicking legacy contracts can preserve legacy semantics longer than desired; the point is to create migration options, not to let transitional compatibility become the permanent design.

## What Changed
- Created the concept from the Legacy Mimic pattern article and inspected diagrams.

## Related Concepts
- [[TransitionalArchitecture]] - legacy mimics are temporary structures inside an incremental migration architecture.
- [[LegacyDisplacement]] - mimics help split replacement work into sequenced parts.
- [[AntiCorruptionLayer]] - shares translation mechanisms but may be enduring rather than transitional.
- [[EventInterception]] - can act as a service-providing mimic when it consumes legacy events.
- [[ExtractValueStreams]] - the example extracts logistics while mimics keep surrounding processes alive.
- [[CapabilityOrientedIntegration]] - both hide implementation complexity behind a boundary shaped for consumers.
