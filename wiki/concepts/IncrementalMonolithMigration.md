---
title: "Incremental Monolith Migration"
type: concept
tags: [software-architecture, migration, monolith, microservices]
sources:
  - real-world-engineering-challenges-8-breaking-up-a-monolith
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[IncrementalMonolithMigration]] is a production transition that moves bounded behavior from a legacy monolith to a successor system in small slices while both implementations coexist behind controlled routing, comparison, fallback, and removal stages.

## Current Synthesis
Khan Academy's case makes the unit of migration unusually small: an individual GraphQL field could move while adjacent fields remained in Python. A federation layer enabled that coexistence, and the rollout advanced from optional shadow requests through response comparison, canary responses, Go-only routing with Python fallback, and final legacy deletion.

The method separated behavioral confidence from traffic exposure. Queries could run against both systems while returning the Python answer; mutations instead needed canaries because replaying writes would be unsafe. Direct behavior ports, production comparisons, and visible traffic share created a measurable path to parity without requiring a big-bang release.

## Key Claims
- Smaller migration slices reduce cutover blast radius and make progress shippable before a whole service is complete.
- A stable routing or composition seam is needed so legacy and successor behavior can coexist.
- Shadow execution and response comparison test behavioral parity without exposing users to successor output.
- Mutating operations need canaries or other single-write controls rather than naive dual execution.
- Retaining the legacy path after primary cutover provides a bounded fallback window before deletion.
- Traffic share is a useful progress signal but does not measure remaining code, internal tools, or organizational work.
- Direct ports improve estimability, while redesign and language changes add learning and scope risk.

## Evidence
- Slice size: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] says fields such as one user property could move independently of adjacent monolith fields.
- Coexistence seam: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] shows GraphQL federation routing about 0.01% of traffic to the first Go service while the Python monolith served about 99.99%.
- Safety sequence: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] documents optional shadowing, side-by-side comparison, canarying, Go-only routing with Python retained, and final removal.
- Mutation boundary: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] says side-by-side execution suited queries but not state-changing mutations.
- Progress and incompleteness: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] reports 95% traffic migration at MVE completion while substantial Python code and all non-MVE behavior still remained.

## Counterevidence & Qualifications
This evidence comes from one unusually large, heavily staffed migration with a GraphQL field boundary and a non-negotiable Python 2 deadline. Other systems may lack a safe composition seam, deterministic output comparison, spare capacity for dual execution, or operations that can be shadowed without privacy, cost, or side-effect risk. Directly porting bugs can preserve parity temporarily but should have an explicit later-remediation path.

## What Changed
- Established a staged migration model separating behavioral comparison, traffic exposure, fallback, and deletion.
- Added the distinction between query shadowing and mutation canaries.
- Qualified traffic share as an incomplete progress measure.

## Related Concepts
- [[ChangeSafety]] - staged exposure, comparison, and fallback bound production risk.
- [[GraphQL]] - federation can provide a field-level coexistence seam.
- [[Incrementalism]] - small shipped slices compound toward a complete architectural transition.
- [[MicroserviceDataBoundaries]] - successor services need explicit ownership as behavior and writes move.
- [[MinimumViableExperience]] - partitions the first migration milestone by essential user behavior.
- [[MicroserviceOperationalOverhead]] - the successor system adds distributed coordination and shared-resource costs.
