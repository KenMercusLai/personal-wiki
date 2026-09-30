---
title: "Kubernetes: maybe a few Bash/Python scripts is enough"
type: source
tags: [kubernetes, infrastructure, containers, simplicity]
date: 2024-03-09
source_file: "/mnt/ken_personal_wiki/Articles/Kubernetes maybe a few BashPython scripts is enough.md"
---

## Summary
This Binary Igor essay argues that infrastructure should be chosen from explicit workload requirements rather than from the maximum feature set a platform can provide. For a single team or a few teams running a [[ModularMonolith]] or a small number of predictable containerized services, it presents managed container platforms or reproducible Bash/Python automation on a few virtual machines as potentially simpler alternatives to [[Kubernetes]], while retaining Kubernetes for cases whose service count, scheduling, scaling, isolation, or organizational needs justify its operating model.

## Key Claims
- Infrastructure requirements should be separated into common necessities—reliable builds and deployments, rollback, configuration, networking, reproducibility, backups, logs, metrics, and alerts—and context-dependent features such as automatic scaling, dynamic scheduling, granular team isolation, and canary deployment.
- [[Kubernetes]] provides powerful, configurable container scheduling, reconciliation, service discovery, load balancing, scaling, and extensibility, but its concepts, cluster operation, manifests, synchronization, and packaging tools make the relevant comparison the complete Kubernetes toolchain rather than the scheduler alone.
- [[ModularMonolith|Modular monoliths]] and a small number of services can reduce infrastructure demand because there are fewer deployment units, teams, placement decisions, and cross-service communication paths.
- A bounded DIY platform can combine virtual machines, [[Docker]], SSH-based deployment, a reverse proxy for zero-downtime cutover, [[Prometheus]]-compatible monitoring, encrypted secret distribution, private networking, explicit host mapping, and scheduled backups.
- [[InfrastructureAsCode]] is an outcome—reproducible, versioned infrastructure—not a requirement to adopt Terraform; scripts and configuration files can satisfy it when they completely encode creation and recovery.
- Managed container services such as [[GoogleCloudRun]] trade provider dependence, constraints, and service cost for a narrower abstraction and less infrastructure operation.
- [[EssentialAndAccidentalComplexity|Accidental complexity]] must be assessed across application and infrastructure together because simplifying application code while expanding operational machinery does not simplify the whole system.

## Key Quotes
> "We should judge system complexity holistically" - on including infrastructure in the system's complexity budget.

> "Is this really what we need? What are the tradeoffs and hidden costs?" - the essay's decision test for infrastructure choices.

## Connections
- [[Kubernetes]] - powerful orchestration platform whose fit should depend on workload and organizational requirements.
- [[ModularMonolith]] - application shape that can keep the number of deployment units and infrastructure demands low.
- [[InfrastructureAsCode]] - reproducibility goal that the source says can be met with scripts and configuration files as well as dedicated provisioning tools.
- [[EssentialAndAccidentalComplexity]] - distinction used to treat unnecessary infrastructure machinery as system-wide accidental complexity.
- [[DistributedSystemRestraint]] - supports delaying orchestration and distribution until scale, placement, resilience, or team boundaries require them.
- [[TechnologyStackComplexity]] - Kubernetes must be evaluated together with the tools needed to package, synchronize, deploy, observe, and operate it.
- [[GoogleCloudRun]] - named managed-container alternative that exchanges control and portability for operational convenience.
- [[Docker]] - container boundary retained in both the Kubernetes and script-driven alternatives.
- [[DeploymentAutomation]] - scripts are expected to provide repeatable build, rollout, health verification, cutover, and rollback paths.
- [[ServiceObservability]] - logs, machine and application metrics, visualizations, and alerts remain required regardless of orchestrator choice.
- [[SecretManagement]] - encrypted storage and controlled distribution remain part of the DIY platform's operating burden.

## Contradictions
- The source's broad claim that the script-driven approach covers almost all systems is more expansive than its evidence: it supplies an architecture sketch and practitioner judgment, not measured implementation cost, reliability, security, recovery time, or long-term maintenance outcomes.
- Existing cases qualify the restraint thesis. [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] uses Kubernetes for geo-distributed, autoscaled ingestion, while [[edge-computing-at-chick-fil-a-chick-fil-a-tech-blog-medium]] uses it across thousands of intermittently connected sites; both have placement or resilience needs absent from the essay's assumed small, predictable systems.
- Replacing Kubernetes with scripts removes platform abstractions but transfers responsibility for idempotency, partial failure, credential handling, patching, drift, concurrency, rollback, health semantics, and disaster-recovery testing to locally maintained code and operating procedures.
