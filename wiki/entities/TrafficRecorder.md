---
title: "Traffic Recorder"
type: entity
tags: [testing, tooling, segment]
sources:
  - alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[TrafficRecorder]] is the Twilio Segment test tool built on yakbak to record destination HTTP requests and replay saved responses in later test runs.

## Current Profile
The source presents Traffic Recorder as the testing infrastructure that made a large destination monorepo practical. It removed routine dependence on live partner endpoints, expired credentials, slow APIs, and internet variability by checking recorded request-response files into the repo. After integration, the source says tests for all 140-plus destinations ran in milliseconds rather than taking up to an hour.

## Key Characteristics
- Records request and response traffic the first time a destination test runs.
- Replays recorded traffic on later test runs instead of calling live partner endpoints.
- Makes tests more resilient to expired credentials, endpoint slowness, and network variability.
- Supports monorepo migration by making the combined test suite fast and stable.

## Evidence
- Recording mechanism: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says Traffic Recorder records requests and responses to files.
- Replay mechanism: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says subsequent tests play back the file rather than contacting the endpoint.
- Test resilience: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says outbound HTTP requests were the main cause of failing tests.
- Speed change: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says all destination tests took milliseconds after integration.

## Qualifications
The source reports Traffic Recorder's impact in this migration but does not provide an independent benchmark, full implementation details, or the maintenance cost of keeping recordings current.

## What Changed
- Created Traffic Recorder as the concrete testing tool behind Segment's recorded-traffic test suite.

## Relationships
- [[RecordedTrafficTesting]] - Traffic Recorder is the source's implementation of recorded HTTP test replay.
- [[TwilioSegment]] - company and product context where the tool was built.
- [[MonolithConsolidation]] - fast reliable tests made consolidation safer.
- [[MonorepoDependencyConvergence]] - one repo needed a combined test suite with stable feedback.
