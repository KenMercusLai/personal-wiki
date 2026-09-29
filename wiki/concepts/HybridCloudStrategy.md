---
title: "Hybrid Cloud Strategy"
type: concept
tags: [cloud, enterprise, portability, strategy]
sources:
  - ibms-old-playbook-stratechery-by-ben-thompson
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[HybridCloudStrategy]] is an enterprise technology strategy that seeks consistent application deployment and management across private infrastructure and multiple public-cloud providers.

## Current Synthesis
The 2018 IBM–Red Hat case frames hybrid cloud as a response to both legacy workload constraints and concentrated public-cloud supply. [[OpenShift]] and [[Kubernetes]] promise a portable application layer that can span on-premises systems and competing providers, allowing [[IBM]] to integrate above clouds it does not own. That is pragmatic after losing the infrastructure race, but portability is not automatically customer value: provider-specific services, data gravity, management complexity, internal capability, trust, and the integrator's own lock-in incentives remain.

## Key Claims
- Hybrid cloud can provide a staged path for workloads that cannot move directly from private infrastructure to one public provider.
- Portable containers and orchestration can reduce some infrastructure dependence across environments.
- A supplier that missed hyperscale infrastructure may compete at the cross-cloud management and integration layer.
- Owning the abstraction layer can create a new dependency even when the stated goal is reducing provider lock-in.
- Strategy success depends on real customer problems, product execution, competitive differentiation, and organizational readiness—not portability claims alone.

## Evidence
- Workload premise: [[ibms-old-playbook-stratechery-by-ben-thompson]] quotes IBM arguing that many enterprise workloads remained outside public cloud because of portability, security, and management concerns.
- Technical mechanism: [[ibms-old-playbook-stratechery-by-ben-thompson]] links OpenShift and Kubernetes to consistent operation across private and several public clouds.
- Strategic position: [[ibms-old-playbook-stratechery-by-ben-thompson]] interprets Red Hat as IBM's admission that it should build above other providers rather than catch them in hyperscale infrastructure.
- Execution risk: [[ibms-old-playbook-stratechery-by-ben-thompson]] questions demand, IBM lock-in, customer self-service, Microsoft competition, and IBM's culture.

## Counterevidence & Qualifications
The source is an acquisition-era thesis rather than evidence of later adoption or outcomes. Kubernetes portability does not automatically make data, identity, networking, observability, managed services, cost models, or operating practices portable. Private infrastructure can also be a justified destination rather than merely a migration stage.

## What Changed
- Created the concept with an explicit distinction between orchestration portability and complete workload or organizational portability.

## Related Concepts
- [[EnterpriseCloudMigration]] - supplies the broader workload, sequencing, and incumbent-displacement context.
- [[Kubernetes]] - provides part of the portable orchestration substrate.
- [[EnterpriseIntegrationBusinessModel]] - explains the value IBM hoped to capture above fragmented infrastructure.
- [[PrivateCloudStrategy]] - distinguishes a bounded private stage or justified destination from indefinite migration delay.
- [[PlatformStickiness]] - qualifies claims that a cross-cloud layer necessarily eliminates lock-in.
