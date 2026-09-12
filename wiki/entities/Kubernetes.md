---
title: "Kubernetes"
type: entity
tags: [infrastructure, containers, orchestration]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Kubernetes]] is a container orchestration and platform system discussed as both a successful declarative infrastructure model and, in a separate agent-infrastructure source, a lower-level isolation layer that cannot by itself provide agent semantic safety.

## Current Profile
The sources split Kubernetes into two roles. Wang Ziting's retrospective treats Kubernetes as more than a tool: a REST-style resource platform where controllers reconcile actual state toward desired state and custom resources extend the system. Guanlan's agent-infrastructure essay treats Kubernetes as correct at the process and resource layer but insufficient for judging semantic side effects of high-permission agents.

## Key Characteristics
- Solves resource and process isolation problems.
- Uses declarative desired-state definitions to simplify container management.
- Exposes platform capabilities as REST-style resources.
- Uses controllers to reconcile actual state toward expected state.
- Supports extensibility through custom resources and controllers.
- Operates below the semantic layer of agent tool calls.
- Cannot judge whether an agent's legitimate API request is maliciously steered.

## Evidence
- Declarative model: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says Kubernetes succeeds partly because it lets developers describe the desired final state.
- Resource and controller model: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says Kubernetes abstracts functions as RESTful resources and controllers synchronize actual state to expected state.
- Extensibility: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says custom resources and controllers can extend Kubernetes.
- Layer boundary: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says Kubernetes can contain a process but cannot see tool-call semantics.
- Legitimate-channel risk: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says dangerous agent behavior can happen through real API keys and normal HTTP requests.
- Abstraction distinction: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] groups Kubernetes with systems that provide execution isolation rather than semantic isolation.

## Qualifications
The sources are not in conflict. One praises Kubernetes at the container-platform abstraction layer; the other says that same layer cannot provide semantic isolation for model-chosen external side effects.

## What Changed
- Added the declarative resource/controller interpretation from Wang Ziting's 2018 Kubernetes experience.

## Relationships
- [[SemanticIsolation]] - Kubernetes is contrasted with the semantic isolation agents require.
- [[ProductionAgentInfrastructure]] - Kubernetes may support workloads below the agent-specific primitive layer.
- [[CapabilityGateway]] - capability gateways address risks Kubernetes cannot evaluate.
- [[DeclarativeInfrastructure]] - Kubernetes is the main example of desired-state reconciliation in the retrospective.
- [[ContainerNativePractice]] - Kubernetes simplifies orchestration but still depends on container-native workload behavior.
