---
title: "Centrifuge"
type: entity
tags: [infrastructure, queues, segment]
sources:
  - alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[Centrifuge]] is the Twilio Segment infrastructure component that replaced many individual destination queues and fed events into a single destination service.

## Current Profile
In the source, Centrifuge is the architectural bridge that makes [[MonolithConsolidation]] practical. Rather than forcing one worker to poll every destination-specific queue, Centrifuge takes over event delivery responsibility between the router and the monolithic destination service. The inspected diagram shows API input flowing to a router, then to Centrifuge, then to one destination service handling Google Analytics, Optimizely, Mixpanel, and other endpoints.

## Key Characteristics
- Replaces per-destination queues in the server-side destinations pipeline.
- Sends events to the single destination service after router distribution.
- Reduces the queue-polling complexity that would have made one service uncomfortable.
- Became backend infrastructure for Segment Connections in the source's note.

## Evidence
- Queue replacement: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says Centrifuge would replace individual queues.
- Monolith bridge: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says it was responsible for sending events to the single monolithic service.
- Diagram evidence: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] shows API to router to Centrifuge to destination service.
- Product note: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says Centrifuge became backend infrastructure for Connections.

## Qualifications
The source names Centrifuge's architectural role but does not document its internal design, algorithms, data model, or later evolution.

## What Changed
- Created Centrifuge as the queue-replacement infrastructure enabling Segment's single destination service.

## Relationships
- [[TwilioSegment]] - company and product context where Centrifuge is used.
- [[TaskQueueDesign]] - Centrifuge changes the queue topology around asynchronous destination delivery.
- [[MonolithConsolidation]] - Centrifuge removes one barrier to consolidating destination workers.
- [[HeadOfLineBlocking]] - Centrifuge follows earlier attempts to avoid cross-destination blocking.
