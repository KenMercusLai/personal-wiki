---
title: "Secret Management"
type: concept
tags: [security, credentials, infrastructure, operations]
sources:
  - an-infrastructure-guide-for-founders-starting-up-security-medium
  - bmpi-serverless-ying-yong-kai-fa-xiao-ji
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[SecretManagement]] is the practice of storing, distributing, consuming, and rotating credentials, API keys, and other sensitive tokens without leaking them through code, chat, laptops, environment misuse, or ad hoc workflows.

## Current Synthesis
The source treats leaked secrets as one of the most common and costly early security failures. Founding teams often put credentials in repositories, environment variables, Slack messages, or laptop copy-paste buffers because that is faster than building a real secrets path. The article argues that handling this early can prevent a painful refactor once many applications and systems depend on unsafe patterns.

The priority order is practical: first keep secrets out of repositories, Slack, and copy-paste workflows by any means necessary; then work toward seamless and fast rotation. Rotation is harder because it requires applications and deployment systems to consume secrets in ways that can change safely.

The bmpi.dev implementation supplies a weaker but common operational compromise: it prompts for a Terraform variable and injects the Tushare token into the ECS task as an environment variable, avoiding repository storage while declining KMS or Secrets Manager because the author considers the secret low sensitivity. This improves on committing a token but does not by itself provide managed storage, auditability, or rotation.

## Key Claims
- Secrets leakage is a primary root cause of cloud security incidents in the source's experience.
- Early teams often normalize unsafe storage in code, environment variables, chat, and engineer laptops.
- Retrofitting secrets management later can require application and build-system rewrites.
- The first priority is keeping secrets out of repositories, Slack channels, and copy-paste buffers.
- Fast, seamless rotation is the harder second-order capability.
- Keeping a secret out of source control is necessary but not equivalent to managed storage, access auditing, and rotation.

## Evidence
- Incident cause: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] says leaked secrets are the primary root cause of security incidents the author has worked on.
- Unsafe locations: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] lists source code, environment variables, and engineer laptop copy-paste buffers as early anti-patterns.
- Public leakage: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] says the recurring failure is an API secret appearing on Pastebin or GitHub.
- Retrofit cost: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] warns that mature refactors can require custom application and system-build overhauls.
- Rotation: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] distinguishes keeping secrets out of unsafe places from the harder goal of quick seamless rotation.
- Manual injection: [[bmpi-serverless-ying-yong-kai-fa-xiao-ji]] passes a prompted Terraform variable through the ECS task definition into a container environment variable so the API token is not committed to the repository.
- Deliberate compromise: [[bmpi-serverless-ying-yong-kai-fa-xiao-ji]] rejects KMS and Secrets Manager for this token because their security and operating cost are judged unnecessary for the use case.

## Counterevidence & Qualifications
The startup-security source treats environment variables as a common unsafe location, while the bmpi.dev source accepts container environment injection for a low-sensitivity token. These positions differ in risk tolerance rather than proving a universal rule. Environment variables can be a delivery mechanism when backed by controlled storage and access, but manual Terraform input alone does not establish encryption at rest, audit history, least-privilege retrieval, or rotation. Neither source compares specific products or threat models systematically.

## What Changed
- Added and qualified a pragmatic Terraform-to-ECS environment-variable pattern that avoids repository storage but omits managed-secret controls.
- Created the concept from the article's startup secrets-handling and rotation warnings.

## Related Concepts
- [[StartupSecurityDebt]] - unsafe secrets workflows are a classic early shortcut that becomes expensive to unwind.
- [[WeakCredentialExposure]] - leaked or weak credentials can turn reachable systems into compromise paths.
- [[ProductionAccessControl]] - temporary access and role-based workflows reduce standing credential risk.
- [[RuntimeConfiguration]] - secrets are a sensitive subset of runtime configuration.
- [[ServerlessComputing]] - managed workloads still need explicit secret storage, delivery, access, and rotation decisions.
