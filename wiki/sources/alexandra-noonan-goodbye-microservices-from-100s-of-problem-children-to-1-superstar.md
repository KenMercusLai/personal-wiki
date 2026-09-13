---
title: "Goodbye Microservices: From 100s of Problem Children to 1 Superstar"
type: source
tags: [microservices, monolith, architecture, testing]
date: 2018-07-10
source_file: /mnt/ken_personal_wiki/Articles/Alexandra Noonan - Goodbye Microservices From 100s of Problem Children to 1 Superstar.md
---

## Summary
[[AlexandraNoonan]] describes how [[TwilioSegment]] moved its server-side destinations pipeline from one queue and worker, to destination-specific microservices and queues, and eventually back into one monolithic destination service. The source argues that microservices initially solved [[HeadOfLineBlocking]] by isolating partner destinations, but the growing set of repos, services, queues, dependencies, tests, and autoscaling profiles created linear operational overhead. The final design used [[Centrifuge]] and a monorepo-backed service, with [[TrafficRecorder]] making tests resilient enough for consolidated deployment.

## Key Claims
- Microservices fit the first destination-scaling problem because separate queues prevented one failing destination from delaying all others.
- The article's inspected diagrams show an architecture path from API to shared queue and destination worker, to router plus per-destination queues, to router plus [[Centrifuge]] plus one destination service.
- Separate repositories and services improved local test isolation at first, but shared-library drift, dependency divergence, and fragmented test hygiene later outweighed that benefit.
- [[MicroserviceOperationalOverhead]] rose roughly with each destination because every new partner added another repo, queue, service, load pattern, and autoscaling configuration.
- [[MonolithConsolidation]] worked because [[TwilioSegment]] paired it with a monorepo, one dependency version per library, and [[RecordedTrafficTesting]] through [[TrafficRecorder]].
- The monolith improved shared-library delivery and operations, but kept trade-offs around fault isolation, cache efficiency, and dependency updates.

## Key Quotes
> "Something had to change." - on the operational burden of the destination microservice architecture.

> "It felt like magic." - on test speed after integrating Traffic Recorder.

## Connections
- [[AlexandraNoonan]] - author of the article.
- [[TwilioSegment]] - company and product context for the architecture migration.
- [[HeadOfLineBlocking]] - the first queueing failure that motivated destination isolation.
- [[MicroserviceOperationalOverhead]] - central diagnosis of the later service and repo sprawl.
- [[MonolithConsolidation]] - final architectural move back into one destination service.
- [[MonorepoDependencyConvergence]] - dependency and shared-library simplification enabled by one repository.
- [[RecordedTrafficTesting]] - testing pattern used to remove live partner APIs from normal test runs.
- [[Centrifuge]] - infrastructure component replacing per-destination queues before the single destination service.
- [[TrafficRecorder]] - test tool built on yakbak to record and replay destination HTTP traffic.
- [[TaskQueueDesign]] - queue topology and retry behavior shape reliability and operations.
- [[SystemReliability]] - the source connects reliability to isolation, load spikes, tests, deployment, and operational burden.

## Contradictions
- No direct contradictions found. The source qualifies generic pro-microservice arguments by showing a case where service isolation fixed head-of-line blocking but later damaged productivity and operations without enough testing and rollout tooling.
