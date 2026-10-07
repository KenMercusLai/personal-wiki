---
title: "Firecracker"
type: entity
tags: [infrastructure, microvm, isolation]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
  - seven-years-of-firecracker-marcs-blog
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[Firecracker]] is an open-source microVM technology used by [[AWS]] to provide hardware-backed workload isolation, fast disposable environments, adjustable resources, and snapshot cloning while remaining below application-level capability and side-effect semantics.

## Current Profile
Firecracker moves the security-critical interface from a general-purpose operating-system boundary toward hardware virtualization and a smaller virtual-machine monitor. The earlier agent-infrastructure source presents it as combining VM isolation with container-like speed but not deciding whether an agent should use a legitimate external credential for a particular operation.

The newer AWS account supplies two concrete production patterns. [[AmazonBedrockAgentCore]] assigns one resizable microVM to each agent session and destroys it at session end. [[AuroraDSQL]] restores database-specific query processors from snapshots, shares unchanged clean pages across clones, keeps dirty pages private, and retires processors on a fixed schedule. Together these examples show that Firecracker's value comes from how isolation, resource control, state placement, cloning, and lifecycle rules fit the larger system.

## Key Characteristics
- Provides hardware-virtualized microVM workload isolation through a comparatively small monitor.
- Supports session-scoped and transaction-scoped disposable execution environments.
- Can adjust VM CPU and memory use in place for variable workloads.
- Supports snapshot restoration and repeated cloning of initialized VM state.
- Allows clones to share unchanged clean pages while preserving private written pages.
- Helps execution isolation but cannot enforce semantic authorization or side-effect recovery on its own.

## Evidence
- Isolation role: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] describes Firecracker microVMs as combining VM isolation and container speed.
- Semantic limit: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says such isolation layers cannot tell whether an agent should perform an API-key-backed action.
- Layer distinction: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] places Firecracker on the execution-isolation side of the execution-versus-semantic distinction.
- Agent sessions: [[seven-years-of-firecracker-marcs-blog]] says AgentCore gives each session a separate Firecracker microVM, resizes resources in place, and destroys the VM when the session ends.
- Transaction processors: [[seven-years-of-firecracker-marcs-blog]] describes PostgreSQL-derived DSQL query processors running in separate Firecracker instances and handling one transaction at a time.
- Cloning: [[seven-years-of-firecracker-marcs-blog]] says DSQL restores initialized processor snapshots rather than repeating Linux and PostgreSQL startup.
- Memory sharing: [[seven-years-of-firecracker-marcs-blog]] diagrams exclusive dirty pages and clean pages shared across clones.

## Qualifications
The earlier article does not compare Firecracker deployments or performance and uses it only to establish an abstraction-layer limit. The newer article is a first-party AWS account that supplies production mechanisms but not startup timings, memory savings, cache measurements, density, cost, attack analysis, or failure behavior. Snapshots also need extra work to restore per-instance uniqueness. MicroVM teardown removes local state but not external effects, memory-service records, tool writes, or logs.

## What Changed
- Added AgentCore's per-session, resizable, disposable microVM pattern.
- Added DSQL's prepared clones, clean-page sharing, and fixed-lifetime processor pattern.
- Preserved the boundary between execution isolation and semantic control of external actions.

## Relationships
- [[SemanticIsolation]] - Firecracker is useful execution isolation but not semantic isolation.
- [[ProductionAgentInfrastructure]] - Firecracker may be part of the lower runtime layer.
- [[CapabilityGateway]] - capability mediation covers risks outside Firecracker's scope.
- [[AmazonBedrockAgentCore]] - uses Firecracker as the boundary for each agent session.
- [[AuroraDSQL]] - uses Firecracker for isolated PostgreSQL-derived query processors.
- [[SessionScopedMicroVMIsolation]] - scopes local agent state to a disposable session environment.
- [[VMSnapshotCloning]] - restores prepared VM state and shares unchanged pages.
- [[BoundedLifetimeSimplification]] - makes teardown part of resource reclamation and architectural simplification.
