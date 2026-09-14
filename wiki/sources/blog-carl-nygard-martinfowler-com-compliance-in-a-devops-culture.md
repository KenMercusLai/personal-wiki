---
title: "Compliance in a DevOps Culture"
type: source
tags: [devops, compliance, ci-cd, governance, architecture]
date: 2021-11-02
source_file: /mnt/ken_personal_wiki/Articles/Blog - Carl Nygard (martinfowler.com) - Compliance in a DevOps Culture.md
---

## Summary
[[CarlNygard]] argues that regulated software delivery should treat compliance as measurable evidence, objective validation, and audit records rather than as a late manual approval ritual. The article compares manual, pipeline, composition, and point-of-change compliance patterns, concluding that scaled [[ContinuousDelivery]] works best when [[ComplianceArchitecture]] separates measurement from validation, stores trusted evidence, and verifies policy at the moment a production change is made.

## Key Claims
- [[ComplianceArchitecture]] starts with properties, measurements, evidence, constraints, and validations, plus an audit process that checks whether compliance itself is operating consistently.
- Manual compliance can work at small scale, but FIFO approval queues, growing forms, and compliance-office capacity limits can enlarge deployment batches, delay value, and encourage shadow IT or false responses.
- [[DeploymentPipeline|Pipeline compliance]] improves developer feedback by embedding fitness functions and audit logs in CI/CD, but central pipeline ownership and manual gates can become a bottleneck when teams need frequent pipeline change.
- Composition compliance reuses approved "golden" container images, but its value depends on homogeneous needs, low variation, and realistic assumptions about whether compliance remains valid under composition and customization.
- Point-of-change compliance decomposes fitness functions into measurement and validation, lets development teams gather evidence, stores that evidence in a system of record, and uses admission-controller-style checks to verify constraints before deployment.
- The inspected diagrams show a progression from manual FIFO gates, to central pipelines, to compliant container images, to point-of-change verification; the scale curves show manual, pipeline, and composition approaches becoming inhibiting at high organizational scale while point-of-change compliance keeps supporting growth longer.

## Key Quotes
> "The regulations and Compliance structures are meant to ensure quality and correctness of the system and are a form of risk management." - on compliance as risk management.

> "The primary reason for a pipeline to exist is to provide a central tool in the software development process." - on why centrally co-opting pipelines for compliance creates friction.

> "Compliance verification requires that all evidence exists in a SoR" - on the point-of-change model.

## Connections
- [[CarlNygard]] - author of the Martin Fowler article.
- [[Thoughtworks]] - employer context and publisher network for the article.
- [[ComplianceArchitecture]] - central concept extracted from the article's theory and pattern comparison.
- [[ContinuousDelivery]] - delivery context whose autonomy, small batches, frequent releases, and MTTR goals shape the compliance tradeoffs.
- [[DeploymentPipeline]] - compliance checks can be embedded as fitness functions and gates, but central ownership can damage pipeline usefulness.
- [[DeploymentAutomation]] - release automation supplies evidence and audit trails when compliance checks are automated.
- [[ChangeSafety]] - compliance is framed as risk management for safe production change.
- [[Kubernetes]] - example platform for measuring open ports and enforcing point-of-change constraints through admission-controller-style deployment checks.
- [[ProductionAccessControl]] - threat model includes unaudited access to build or production paths.
- [[CodeClimate]] - example tool for code-coverage evidence.
- [[SonarQube]] - example tool for code-coverage evidence.
- [[PostgreSQL]] - example golden-image capability in the composition compliance pattern.

## Contradictions
- No direct contradiction found. The source qualifies earlier positive [[DeploymentPipeline]] material by warning that pipelines can lose developer value when centralized for orthogonal compliance control, and it complements [[ChangeSafety]] by adding regulatory evidence and auditability as a separate delivery constraint.
