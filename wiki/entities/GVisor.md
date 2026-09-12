---
title: "gVisor"
type: entity
tags: [infrastructure, sandboxing, isolation]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[GVisor]] is a user-space kernel sandbox discussed in the source as useful execution isolation that remains below the semantic layer required by production agents.

## Current Profile
The article describes gVisor as providing a Linux-like application kernel in user space. It helps isolate workloads, but it does not understand whether an agent's model-selected tool call should be permitted, logged, or replayed.

## Key Characteristics
- Provides a Linux-like application-kernel layer in user space.
- Strengthens workload isolation.
- Does not understand agent tool-call intent.
- Does not solve raw credential exposure or side-effect recovery.

## Evidence
- Technical role: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] describes gVisor as providing a Linux-like application kernel in user space.
- Semantic gap: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says isolation systems cannot tell whether a legitimate API-key-backed action is safe.
- Shared limitation: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] groups gVisor with systems that isolate execution rather than capabilities and side effects.

## Qualifications
The source does not evaluate gVisor's implementation quality. It uses gVisor only to illustrate the abstraction mismatch between sandboxing and agent semantics.

## What Changed
- Created the entity page for gVisor.

## Relationships
- [[SemanticIsolation]] - gVisor is contrasted with semantic isolation.
- [[ProductionAgentInfrastructure]] - gVisor may support execution containment under agent-specific controls.
- [[CapabilityGateway]] - capability gateways address external-action control outside gVisor's scope.
