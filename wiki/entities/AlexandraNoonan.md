---
title: "Alexandra Noonan"
type: entity
tags: [person, engineering, architecture]
sources:
  - alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[AlexandraNoonan]] is the author of the Twilio Segment engineering article about moving a server-side destinations pipeline from many microservices into one monolithic service.

## Current Profile
The source presents Noonan as an engineering author explaining an architecture migration through operational pain, system diagrams, dependency management, testing strategy, and trade-off analysis. Her central contribution in the wiki is a pragmatic architecture judgment: microservices can be correct for one bottleneck and still become wrong when team size, tooling, and operational surfaces change.

## Key Characteristics
- Explains architecture through concrete system behavior rather than abstract preference.
- Treats microservices and monoliths as context-dependent design choices.
- Emphasizes testing and dependency convergence as prerequisites for safe consolidation.
- Names explicit trade-offs rather than presenting the monolith as free improvement.

## Evidence
- System explanation: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] traces the destination pipeline from shared queue to per-destination services to one destination service.
- Context-dependent architecture: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says microservices solved isolation early but later created operational and productivity costs.
- Testing prerequisite: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] describes [[TrafficRecorder]] as necessary to make the single-repo test suite resilient.
- Trade-off accounting: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] lists fault isolation, cache efficiency, and dependency updates as costs of the monolith.

## Qualifications
The wiki currently has only one source by Noonan. It supports her role as author and architecture explainer for this case, but not a broader profile of her career or later technical views.

## What Changed
- Created Noonan as the source author for the Twilio Segment microservices-to-monolith case.

## Relationships
- [[TwilioSegment]] - company and product context of the migration Noonan describes.
- [[MicroserviceOperationalOverhead]] - central architecture problem in her article.
- [[MonolithConsolidation]] - final architectural direction she explains.
- [[RecordedTrafficTesting]] - testing mechanism she presents as enabling the migration.
