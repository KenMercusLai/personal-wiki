---
title: "Compliance Architecture"
type: concept
tags: [compliance, devops, governance, release-engineering]
sources:
  - blog-carl-nygard-martinfowler-com-compliance-in-a-devops-culture
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ComplianceArchitecture]] is the design of controls, evidence flows, validation boundaries, audit records, and ownership structures that prove software changes satisfy regulatory or organizational requirements without unnecessarily blocking delivery.

## Current Synthesis
Carl Nygard's source treats compliance as a system of measurable properties and validations rather than a paperwork event. A compliance process measures system properties, records evidence, validates that evidence against constraints, and keeps enough audit trail to prove the process is operating consistently. That makes compliance close to [[SoftwareVerification]], but with stronger attention to governance, evidence provenance, threat models, and auditability.

The article's main pattern map is scale-sensitive. Manual compliance is simple when releases are rare and forms are small, but it creates central FIFO queues and can push teams toward large batches or avoidance. Pipeline compliance embeds fitness functions into CI/CD and improves feedback, yet it can become harmful when a central team owns every pipeline change. Composition compliance reuses already approved building blocks such as golden container images, but it works best under homogeneous requirements and can distort architecture when teams need capabilities outside the approved catalog. Point-of-change compliance is the mature form: split measurement from validation, let teams gather evidence, store trusted evidence in systems of record, and enforce constraints through deployment-time policy checks.

## Key Claims
- Compliance can be modeled as properties, measurements, evidence, constraints, validations, and audits.
- Manual approval processes are simple at small scale but tend to become queueing bottlenecks as organizational scale grows.
- Pipeline compliance improves feedback when checks are automated, but central pipeline ownership can undermine team autonomy and delivery speed.
- Composition compliance reuses approved components, yet depends on low variance and careful assumptions about composition and customization.
- Point-of-change compliance reduces coupling by separating evidence measurement from policy validation.
- Trusted systems of record, signed evidence, and admission-controller-style checks make compliance more data-driven and auditable.

## Evidence
- Process model: [[blog-carl-nygard-martinfowler-com-compliance-in-a-devops-culture]] defines property, measurement, evidence, constraint, validation, and audit as the compliance primitives.
- Manual bottleneck: [[blog-carl-nygard-martinfowler-com-compliance-in-a-devops-culture]] describes manual checklist submissions, FIFO approval queues, larger batches, shadow IT, and 6-9 month approval cases.
- Pipeline tradeoff: [[blog-carl-nygard-martinfowler-com-compliance-in-a-devops-culture]] says embedded fitness functions improve feedback and audit trails, while central ownership and manual gates can slow teams.
- Composition tradeoff: [[blog-carl-nygard-martinfowler-com-compliance-in-a-devops-culture]] says compliant container images can save repeated work but become restrictive when solution needs diverge.
- Point-of-change model: [[blog-carl-nygard-martinfowler-com-compliance-in-a-devops-culture]] describes systems of record, signed evidence, exceptions, and admission-controller verification before deployment.
- Visual evidence: [[blog-carl-nygard-martinfowler-com-compliance-in-a-devops-culture]] includes inspected diagrams showing the four process architectures and scale curves where point-of-change compliance remains supportive longer than manual, pipeline, or composition approaches.

## Counterevidence & Qualifications
The source is practitioner architecture guidance, not empirical proof that one pattern universally dominates. Point-of-change compliance is explicitly more complex, and the article says it is most justified where organizational scale creates real bottlenecks. The argument also assumes compliance requirements can be expressed as objective constraints often enough for measurement and validation to be meaningfully separated.

## What Changed
- Created the concept from Nygard's compliance-process theory, pattern comparison, and inspected diagrams.

## Related Concepts
- [[ContinuousDelivery]] - compliance architecture must preserve frequent, low-risk software delivery.
- [[DeploymentPipeline]] - pipeline compliance embeds validation in release flow but can be over-centralized.
- [[DeploymentAutomation]] - automated checks gather evidence and create audit trails.
- [[ChangeSafety]] - compliance is one form of risk management around production change.
- [[SoftwareVerification]] - compliance evidence often comes from tests, scans, and objective validation.
- [[ProductionAccessControl]] - compliance threat models depend on trustworthy access and audit boundaries.
- [[InternalDeveloperPlatform]] - shared controls can be packaged as reusable paved paths without centralizing every team process.
