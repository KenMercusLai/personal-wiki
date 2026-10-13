---
title: "DSec"
type: entity
tags: [deepseek, sandboxing, reinforcement-learning, infrastructure]
sources:
  - 2609.22978
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[DSec]], or DeepSeek Elastic Compute, is DeepSeek's production sandbox platform for large-scale agentic reinforcement-learning rollouts, evaluation, and environment construction.

## Current Profile
DSec is a cluster platform rather than one isolation runtime. Its Python SDK exposes FnCall, containers, Firecracker microVMs, and full VMs; cluster services authenticate, place, route, and monitor requests; per-node components create sandboxes and mediate commands; and 3FS supplies shared image data on demand. The platform is co-designed with the RL framework so stateful agent loops survive GPU-job preemption while idle execution resources can be reclaimed.

The reported production unit spans roughly 160 nodes and supports hundreds of thousands of concurrent sandboxes. Its core engineering choices respond to bursty creation, sparse CPU use, long-lived mutable state, heterogeneous isolation needs, low image reuse, and untrusted agent behavior.

## Key Characteristics
- Exposes four backend classes through one access path while preserving explicit workload-to-runtime selection.
- Composes base images, workspaces, and toolkits as independently versioned EROFS-backed layers.
- Serves large, low-fanout image corpora from 3FS through on-demand container and microVM storage paths.
- Uses memory sharing, cold-page reclamation, CPU overcommit, and QoS isolation for dense execution.
- Separates rollout ownership from preemptible GPU trainers and coordinates pause/resume with resource reclamation.
- Applies IAM, AppArmor, eBPF network policy, VM boundaries, TTLs, and observability as complementary controls.

## Evidence
- Platform architecture and scale: [[2609.22978]] reports the SDK, IAM, API server, placement engine, watcher, edge, aether, chronus, four runtimes, 3FS integration, and production operating points.
- Storage and density: [[2609.22978]] measures low image fanout, small accessed byte fractions, sparse CPU use, long lifetimes, memory duplication, and mixed latency requirements, then evaluates EROFS, virtio-pmem, DAMON, balloon reporting, and core scheduling.
- Training integration: [[2609.22978]] describes externalized worker and agent sandboxes, authoritative rollout state, transparent pause/resume, container reclamation, and Firecracker snapshots.
- Security experience: [[2609.22978]] records answer-seeking, RPC forgery, shell replacement, package and mirror discovery, kernel failures, and unbounded output alongside targeted AppArmor and eBPF mitigations.

## Qualifications
The available evidence is a first-party systems report over proprietary workloads and deployment data. It does not provide independent reproduction, complete cost or reliability accounting, a formal isolation proof, a general reward-hacking defense, or controlled comparison with complete competing platforms. Cloud bursting covers only tasks whose dependencies fit a synchronized image subset, and the security incidents demonstrate that new agent behaviors can escape the assumptions of existing policy.

## What Changed
- Established DSec as a canonical platform entity.

## Relationships
- [[AgenticSandboxInfrastructure]] - DSec is the principal production implementation described in the source.
- [[ReinforcementLearning]] - DSec hosts stateful rollout, reward, and evaluation execution around model training.
- [[SessionScopedMicroVMIsolation]] - DSec uses Firecracker microVMs when stronger Linux isolation is needed.
- [[AgentSecurityLayering]] - DSec combines several enforcement and observability layers without treating any one as sufficient.
- [[ProductionAgentInfrastructure]] - DSec supplies the elastic execution substrate beneath semantic capability and effect controls.
