---
title: "LeanCloud"
type: entity
tags: [cloud-platform, backend, game-backend]
sources:
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[LeanCloud]] is the cloud platform company context for Wang Ziting's 2018 work on container services, game backend features, [[ClientEngine]], and cloud-engine task queues.

## Current Profile
In the source, LeanCloud appears as a backend platform that extends existing services through container orchestration, message forwarding for games, server-side game logic, and HTTP-invoked cloud-engine tasks. The strongest profile is not a corporate overview but a product-platform context where new features are judged by how well they fit existing user concepts and workflows.

## Key Characteristics
- Provides cloud-engine and container-service capabilities that can be wrapped around [[Kubernetes]].
- Offers a game backend solution centered on message forwarding and state synchronization between clients.
- Productized server-side game logic through [[ClientEngine]] after an internal architecture debate and demo.
- Explores task queue scheduling as an extension of existing HTTP-based cloud functions.

## Evidence
- Container service context: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says the author deeply used Kubernetes at work to package a container service.
- Game backend context: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] describes a LeanCloud game backend solution as a message-forwarding service for client communication and state sync.
- Client Engine productization: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says the demo pattern was later released as the official [[ClientEngine]] product.
- Cloud-engine queue extension: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] presents task queues as scheduling around existing HTTP cloud functions rather than a new compute substrate.

## Qualifications
The source discusses LeanCloud only through one engineer's 2018 project work. It does not provide a full product catalog, business history, or customer evaluation.

## What Changed
- Created the LeanCloud entity page as the platform context for the retrospective.

## Relationships
- [[WangZiting]] - employee-author reflecting on LeanCloud-related technical work.
- [[Kubernetes]] - infrastructure base for the container service work.
- [[ClientEngine]] - LeanCloud product for server-side game logic.
- [[TaskQueueDesign]] - cloud-engine queue feature designed to fit existing HTTP cloud functions.
