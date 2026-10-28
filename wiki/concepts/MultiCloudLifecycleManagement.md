---
title: "Multi-Cloud Lifecycle Management"
type: concept
tags: [cloud, infrastructure, cmdb, terraform]
sources:
  - ai-harness-engineering
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Definition
[[MultiCloudLifecycleManagement]] is the coordinated provisioning, operation, change, observation, and retirement of resources across cloud providers while preserving explicit provider differences, shared identity controls, and consistent CMDB state.

## Current Synthesis
The source separates the problem by operation type instead of forcing every cloud action through one abstraction. Declarative create, update, and delete operations travel from a CMDB to [[TFEngine]], which renders HCL, plans and applies Terraform changes, manages state and execution, and returns results plus logs. Imperative Day 2 actions travel from the CMDB to [[CloudKitService|CloudKit]], whose plugins wrap provider SDK workflows behind a common gateway.

This split keeps provider variability visible behind capability-specific interfaces. AWS, Alibaba Cloud, Huawei Cloud, and Kingsoft Cloud differ in models and SDK completeness, so a plugin implements one capability across providers rather than claiming the providers share identical resource semantics. A common identity layer coordinates SSO, multi-cloud accounts and tokens, RBAC, secrets, and audit across both execution paths.

Operational ownership is also part of the design. Operations staff maintain HCL templates, end users request supported resources through forms, and Terraform logs remain visible for direct diagnosis. The reported system has implemented virtual-machine and object-storage lifecycle management, but the article does not establish general coverage across services or providers.

## Key Claims
- Declarative provisioning and imperative Day 2 operations have different execution semantics and benefit from separate engines.
- A CMDB can provide one workflow and resource record while preserving provider-specific behavior behind capability plugins.
- Shared identity, account, credential, authorization, secret, and audit controls are cross-cutting infrastructure rather than plugin-local details.
- Transparent plans, results, state, and logs let operations staff diagnose automation failures closer to the provider boundary.
- Capability-oriented plugins can isolate inconsistent SDKs and models without pretending four clouds are behaviorally identical.

## Evidence
- Split lifecycle paths: [[ai-harness-engineering]] and its retained architecture route Terraform-backed create, update, and delete operations through TFEngine and Day 2 actions through CloudKit.
- Provider adaptation: [[ai-harness-engineering]] names model differences, Huawei Cloud's enterprise-project identifier, and incomplete Kingsoft Cloud SDKs as reasons for provider-specific encapsulation.
- Shared controls: [[ai-harness-engineering]] shows SSO, account and token management, RBAC, secure credential storage, and audit beneath the CMDB and both engines.
- Operational interface: [[ai-harness-engineering]] says operations staff own HCL templates while users work through forms and retain access to Terraform execution logs.

## Counterevidence & Qualifications
The concept currently rests on one self-authored architecture account. It does not provide a resource and operation coverage matrix, contract tests, drift behavior, rollback semantics, state-locking design, failure recovery, credential threat model, audit guarantees, SDK upgrade policy, latency, scale, staffing cost, or comparison with existing multi-cloud platforms. A common API can conceal meaningful differences, while plugin multiplication can shift rather than remove maintenance cost. The reported success covers virtual machines and object storage, not complete parity across four clouds.

## What Changed
- Established a two-path model separating Terraform lifecycle operations from provider-SDK Day 2 operations under one CMDB and identity plane.

## Related Concepts
- [[InfrastructureAsCode]] - supplies the declarative resource-lifecycle path.
- [[Terraform]] - implementation selected for common provider support in the reported four-cloud environment.
- [[TFEngine]] - executes plans, applies, destroys, state, and logs for declarative operations.
- [[CloudKitService]] - wraps provider-specific imperative capabilities through plugins.
- [[InternalDeveloperPlatform]] - can present templates and provider operations through governed user-facing workflows.
- [[CloudAccountSegmentation]] - account and credential boundaries constrain multi-cloud blast radius.
