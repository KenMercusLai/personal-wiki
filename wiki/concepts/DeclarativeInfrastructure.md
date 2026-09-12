---
title: "Declarative Infrastructure"
type: concept
tags: [infrastructure, kubernetes, control-loop]
sources:
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[DeclarativeInfrastructure]] is infrastructure design where users describe desired final state and controllers continuously reconcile actual system state toward that target.

## Current Synthesis
The source uses Kubernetes as the clearest example of declarative infrastructure. Instead of asking developers to manage containers through imperative steps, Kubernetes represents platform capabilities as REST-style resources. Controllers then synchronize each resource's actual state to the expected state. This makes the system not only a tool but a platform, because teams can add custom resources and controllers to extend the same reconciliation model.

## Key Claims
- Declarative desired-state definitions simplify container management by moving users away from step-by-step operational control.
- Kubernetes implements this model thoroughly through resources and controllers.
- A REST-style resource abstraction turns infrastructure features into an extensible API surface.
- Custom resources and controllers let teams extend the platform without changing the whole orchestration model.

## Evidence
- Desired state: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says container platforms simplify management by letting developers describe the expected final state.
- Kubernetes case: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says Kubernetes implements declarative definitions most thoroughly and that this helps explain its success.
- Resource abstraction: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says Kubernetes abstracts all functions as RESTful API resources.
- Controller reconciliation: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says each resource's controller synchronizes real object state to expected state.
- Extensibility: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says custom resources and controllers can extend Kubernetes.

## Counterevidence & Qualifications
The source explains Kubernetes's conceptual strength but does not discuss the costs of operating controllers, debugging reconciliation loops, or choosing when declarative infrastructure becomes too indirect for a small system.

## What Changed
- Created the concept page from the Kubernetes section of the retrospective.

## Related Concepts
- [[Kubernetes]] - primary platform example of declarative infrastructure in the source.
- [[ContainerNativePractice]] - declarative platforms still depend on services behaving well inside containers.
- [[GameServerCloudNativeDelivery]] - cloud-native delivery can use declarative infrastructure patterns for release, scaling, and rollback.
- [[ProductionAgentInfrastructure]] - both involve infrastructure primitives that constrain higher-level system behavior.
