---
title: "Kevin Dangoor"
type: entity
tags: [person, software-architecture, software-engineering]
sources:
  - real-world-engineering-challenges-8-breaking-up-a-monolith
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[KevinDangoor]] is represented in the wiki as a former Khan Academy principal software architect and migration leader who helped shape and document its move from a Python monolith to Go services.

## Current Profile
Dangoor's contribution centers on technology selection, architectural strategy, incremental shipping, and disciplined scope. His reflections connect Go's consistency and memory efficiency, GraphQL federation, one-writer data ownership, small production slices, and direct behavior ports to a migration that stayed close to its multi-year estimate.

## Key Characteristics
- Helped lead the architecture and early execution of Khan Academy's monolith rewrite.
- Documented the language decision and the team's experience after substantial Go adoption.
- Emphasized small continuously shipped slices even when early dependency extraction was difficult.
- Supported one-service write ownership as a way to keep distributed data changes understandable.
- Attributes estimate stability partly to direct ports and resistance to scope expansion.

## Evidence
- Architecture and language: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] cites Dangoor's account of choosing Go and federated GraphQL.
- Incremental delivery: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] records his view that continuously shipping small slices separated success from failure.
- Data ownership: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] attributes the one-writer rule to an early leadership decision he described.
- Estimation: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] reports his judgment that direct ports kept the two-year MVE estimate close to actual completion.

## Qualifications
This profile is limited to one case study drawing on interviews and Khan Academy engineering posts. It does not independently attribute team outcomes to Dangoor or provide a general account of his work at Mozilla, Adobe, GitHub, or elsewhere.

## What Changed
- Established a source-bounded profile of Dangoor as an architect of Khan Academy's incremental rewrite.

## Relationships
- [[KhanAcademy]] - organization where Dangoor served as principal software architect during most of the rewrite.
- [[BrianGenisio]] - fellow migration leader and interview source in the case study.
- [[GraphQL]] - federation supplied the coexistence and composition layer for the migration.
- [[MicroserviceDataBoundaries]] - one-writer ownership was a core boundary rule he highlighted.
