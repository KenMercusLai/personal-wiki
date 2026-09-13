---
title: "Recorded Traffic Testing"
type: concept
tags: [testing, software-engineering, reliability]
sources:
  - alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[RecordedTrafficTesting]] is a testing pattern where real network request-response traffic is captured once and replayed in later test runs to make integration-like tests faster and more deterministic.

## Current Synthesis
The Twilio Segment source uses recorded traffic testing to remove live partner APIs from routine destination tests. Destination tests originally made outbound HTTP requests, so expired credentials, slow endpoints, internet conditions, and partner-side failures could break tests unrelated to the change under review. [[TrafficRecorder]], built on yakbak, recorded request-response pairs and checked them into the repo so later runs replayed the saved interaction.

The pattern matters architecturally because it changed what repository and service structure was feasible. A monorepo with 140-plus destinations needed a combined suite that developers could trust and run quickly; recorded traffic turned live endpoint variability into versioned test fixtures.

## Key Claims
- Live external dependencies can make otherwise local test suites slow and flaky.
- Recording request-response traffic can preserve realistic integration behavior without calling the external service every run.
- Checking recordings into the repo turns external interactions into reviewable test fixtures.
- Recorded traffic testing can make large monorepo test suites feasible.
- The pattern improves determinism but still requires judgment about when recordings need refreshing.

## Evidence
- Flake cause: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says outbound HTTP requests were the primary cause of failing tests.
- Slowness cause: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says some destination endpoint tests took up to five minutes.
- Recording mechanism: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says [[TrafficRecorder]] saves requests and responses to files.
- Replay mechanism: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says later tests play back the saved request and response.
- Monorepo effect: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says all 140-plus destination tests ran in milliseconds after integration.

## Counterevidence & Qualifications
Recorded traffic can make tests less representative if partner APIs change, if recordings are stale, or if assertions only confirm old behavior. The source demonstrates speed and resilience gains but does not describe refresh policy, fixture review practice, or coverage for live integration failures.

## What Changed
- Created the concept from Segment's Traffic Recorder test strategy.

## Related Concepts
- [[TrafficRecorder]] - concrete tool implementing the pattern in the source.
- [[DeterministicTesting]] - replayed traffic reduces environmental nondeterminism in test output.
- [[SnapshotTesting]] - recorded responses act like versioned behavioral fixtures.
- [[MonolithConsolidation]] - fast reliable tests made service consolidation safer.
- [[SoftwareVerification]] - recorded traffic is one repeatable validation technique.
