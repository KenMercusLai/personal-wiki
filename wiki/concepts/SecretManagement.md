---
title: "Secret Management"
type: concept
tags: [security, credentials, infrastructure, operations]
sources:
  - an-infrastructure-guide-for-founders-starting-up-security-medium
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[SecretManagement]] is the practice of storing, distributing, consuming, and rotating credentials, API keys, and other sensitive tokens without leaking them through code, chat, laptops, environment misuse, or ad hoc workflows.

## Current Synthesis
The source treats leaked secrets as one of the most common and costly early security failures. Founding teams often put credentials in repositories, environment variables, Slack messages, or laptop copy-paste buffers because that is faster than building a real secrets path. The article argues that handling this early can prevent a painful refactor once many applications and systems depend on unsafe patterns.

The priority order is practical: first keep secrets out of repositories, Slack, and copy-paste workflows by any means necessary; then work toward seamless and fast rotation. Rotation is harder because it requires applications and deployment systems to consume secrets in ways that can change safely.

## Key Claims
- Secrets leakage is a primary root cause of cloud security incidents in the source's experience.
- Early teams often normalize unsafe storage in code, environment variables, chat, and engineer laptops.
- Retrofitting secrets management later can require application and build-system rewrites.
- The first priority is keeping secrets out of repositories, Slack channels, and copy-paste buffers.
- Fast, seamless rotation is the harder second-order capability.

## Evidence
- Incident cause: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] says leaked secrets are the primary root cause of security incidents the author has worked on.
- Unsafe locations: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] lists source code, environment variables, and engineer laptop copy-paste buffers as early anti-patterns.
- Public leakage: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] says the recurring failure is an API secret appearing on Pastebin or GitHub.
- Retrofit cost: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] warns that mature refactors can require custom application and system-build overhauls.
- Rotation: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] distinguishes keeping secrets out of unsafe places from the harder goal of quick seamless rotation.

## Counterevidence & Qualifications
The source intentionally stays at the design-priority level and does not evaluate specific products, encryption models, runtime injection strategies, or audit requirements. It also treats environment variables as risky in the cited context, while other deployment models may use them safely when backed by a managed secret store, strict access control, and rotation.

## What Changed
- Created the concept from the article's startup secrets-handling and rotation warnings.

## Related Concepts
- [[StartupSecurityDebt]] - unsafe secrets workflows are a classic early shortcut that becomes expensive to unwind.
- [[WeakCredentialExposure]] - leaked or weak credentials can turn reachable systems into compromise paths.
- [[ProductionAccessControl]] - temporary access and role-based workflows reduce standing credential risk.
- [[RuntimeConfiguration]] - secrets are a sensitive subset of runtime configuration.
