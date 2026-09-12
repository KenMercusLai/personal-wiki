---
title: "2018 年度小结（技术方面）"
type: source
tags: [technical-retrospective, containers, kubernetes, redis, game-backend]
date: 2019-01-30
source_file: /mnt/ken_personal_wiki/Articles/2018 年度小结（技术方面）.md
---

## Summary
[[WangZiting]] reviews his 2018 technical work across side projects, [[Kubernetes]]-based container services, Dockerfile tooling, [[LeanCloud]] game backend products, and an HTTP-triggered task queue implemented with [[Redis]] and Lua scripts. The article argues that small personal projects need fast release loops, container platforms work through declarative desired state and controllers, container adoption is incomplete without container-native service behavior, and backend features should minimize new concepts when they extend an existing platform.

## Key Claims
- [[ReleaseFocusedSideProjects]] require choosing one project at a time and publishing usable versions quickly enough to create feedback and motivation.
- [[Kubernetes]] succeeds partly because it exposes declarative resource definitions and controller reconciliation, making the platform extensible through custom resources and controllers.
- [[ContainerNativePractice]] is different from merely running old programs in containers; services still need healthy storage assumptions, health checks, and signal handling for graceful shutdown.
- [[ServerSideGameLogic]] can be modeled as a client participating in a message-forwarding service, allowing game logic reuse and smoother migration from single-player to action-sync and state-sync modes.
- [[TaskQueueDesign]] should match user needs and platform concepts; [[LeanCloud]]'s cloud-engine queue used HTTP scheduling, [[NodeJS]] workers, Redis state, and Lua-scripted atomic operations.
- [[Redis]]'s product strength comes from a narrow, well-chosen positioning that makes its server-side design feel simple.

## Key Quotes
> "一次要专注于一个项目" - the retrospective's central lesson about side-project focus.

> "Kubernetes 不仅仅是一个工具，同时也是一个平台" - on Kubernetes as an extensible API and controller platform.

> "很多时候只是将已有的程序跑在容器里而已，而没能做到 Container Native" - on the gap between container packaging and container-native operation.

## Connections
- [[WangZiting]] - author of the technical retrospective.
- [[DeployBeta]] - side project that became a negative example of delayed external release despite substantial technical work.
- [[Elecpass]] - side project that became the positive example of fast usable releases and later focused iteration.
- [[Kubernetes]] - container platform the author used deeply and interprets through declarative desired state, resources, and controllers.
- [[Docker]] - container tooling context for the author's Dockerfile DSL and container-native critique.
- [[LeanCloud]] - company context for the container service, game backend, Client Engine, and cloud-engine task queue work.
- [[ClientEngine]] - productized version of the server-side game-logic demo.
- [[Redis]] - state store and atomic-operation substrate for the task queue implementation.
- [[ReleaseFocusedSideProjects]] - side-project process lesson from DeployBeta and Elecpass.
- [[DeclarativeInfrastructure]] - Kubernetes abstraction lesson around desired state and reconciliation.
- [[ContainerNativePractice]] - operational standard the article says many production containers still failed to meet.
- [[ServerSideGameLogic]] - game backend pattern validated by the author's demo.
- [[TaskQueueDesign]] - product and implementation lesson from the cloud-engine queue feature.
- [[ProductEvolution]] - related through phase-based release, user feedback, and productized technical work.

## Contradictions
- No direct contradictions identified. The source complements existing container and game-server material by adding a practitioner view from 2018, before the later sources' reliability and cloud-native frames.
