---
title: "Kubernetes"
type: entity
tags: [infrastructure, containers, orchestration]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Kubernetes]] is a container orchestration system discussed in the source as useful for resource and process isolation but insufficient for agent tool-call semantics.

## Current Profile
The article treats Kubernetes as correct at its own abstraction layer. It can isolate and manage containers, but it cannot distinguish ordinary API traffic from a prompt-injection-driven agent using legitimate credentials in a harmful way.

## Key Characteristics
- Solves resource and process isolation problems.
- Operates below the semantic layer of agent tool calls.
- Cannot judge whether an agent's legitimate API request is maliciously steered.
- Remains useful infrastructure but does not provide [[SemanticIsolation]].

## Evidence
- Layer boundary: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says Kubernetes can contain a process but cannot see tool-call semantics.
- Legitimate-channel risk: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says dangerous agent behavior can happen through real API keys and normal HTTP requests.
- Abstraction distinction: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] groups Kubernetes with systems that provide execution isolation rather than semantic isolation.

## Qualifications
The source does not critique Kubernetes as container infrastructure. Its claim is narrower: Kubernetes alone cannot provide production-agent safety semantics.

## What Changed
- Created the entity page for Kubernetes as an existing infrastructure layer contrasted with agent-specific semantics.

## Relationships
- [[SemanticIsolation]] - Kubernetes is contrasted with the semantic isolation agents require.
- [[ProductionAgentInfrastructure]] - Kubernetes may support workloads below the agent-specific primitive layer.
- [[CapabilityGateway]] - capability gateways address risks Kubernetes cannot evaluate.
