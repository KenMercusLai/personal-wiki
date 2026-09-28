---
title: "Declarative Infrastructure"
type: concept
tags: [infrastructure, kubernetes, control-loop]
sources:
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
  - gitops-operations-by-pull-request
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[DeclarativeInfrastructure]] is infrastructure design where users describe desired final state and controllers continuously reconcile actual system state toward that target.

## Current Synthesis
The sources use Kubernetes as the clearest example of declarative infrastructure. Instead of asking developers to manage containers through imperative steps, Kubernetes represents platform capabilities as resources whose controllers synchronize actual state toward expected state. This makes the system not only a tool but a platform, because teams can add custom resources and controllers to extend the same reconciliation model.

The GitOps case adds an operational boundary: a declarative file records intended state, but the live system remains independently real and can drift. Version control makes the intended state reviewable and recoverable; diff and sync tools are still needed to observe and restore convergence. Declarative infrastructure therefore needs both a state model and a reconciliation loop, not merely configuration files.

## Key Claims
- Declarative desired-state definitions simplify container management by moving users away from step-by-step operational control.
- Kubernetes implements this model thoroughly through resources and controllers.
- A REST-style resource abstraction turns infrastructure features into an extensible API surface.
- Custom resources and controllers let teams extend the platform without changing the whole orchestration model.
- Versioned desired state supports review and recovery, but live-state comparison is required to reveal divergence.
- Drift detection and synchronization are complementary parts of operational reconciliation.

## Evidence
- Desired state: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says container platforms simplify management by letting developers describe the expected final state.
- Kubernetes case: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says Kubernetes implements declarative definitions most thoroughly and that this helps explain its success.
- Resource abstraction: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says Kubernetes abstracts all functions as RESTful API resources.
- Controller reconciliation: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says each resource's controller synchronizes real object state to expected state.
- Extensibility: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says custom resources and controllers can extend Kubernetes.
- Intended-versus-actual boundary: [[gitops-operations-by-pull-request]] says the desired state in Git can differ from what is running in an environment.
- Drift and convergence: [[gitops-operations-by-pull-request]] describes diff tools that report disagreement and sync tools that drive the system back toward its declared state.
- Versioned context: [[gitops-operations-by-pull-request]] connects declarative files with review, comments, issue links, audit history, and recovery.

## Counterevidence & Qualifications
The sources explain Kubernetes's conceptual strength and one company's operating model but do not compare the costs of controllers, reconciliation failures, alert noise, or synchronization mistakes against imperative alternatives. A declared state can itself be wrong, and convergence can propagate that error consistently. Not all runtime data, secrets, or external side effects fit safely into a Git repository or can be reconstructed from it.

## What Changed
- Added the distinction between versioned intended state and independently observable live state.
- Added drift detection and synchronization as complementary operational parts of declarative reconciliation.

## Related Concepts
- [[Kubernetes]] - primary platform example of declarative infrastructure in the source.
- [[ContainerNativePractice]] - declarative platforms still depend on services behaving well inside containers.
- [[GameServerCloudNativeDelivery]] - cloud-native delivery can use declarative infrastructure patterns for release, scaling, and rollback.
- [[ProductionAgentInfrastructure]] - both involve infrastructure primitives that constrain higher-level system behavior.
- [[GitOps]] - applies version control, review, drift detection, and synchronization around declarative infrastructure.
- [[InfrastructureAsCode]] - expresses provisioning and configuration as versioned automation, with overlap but not identity with continuous reconciliation.
