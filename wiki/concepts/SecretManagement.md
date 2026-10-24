---
title: "Secret Management"
type: concept
tags: [security, credentials, infrastructure, operations]
sources:
  - an-infrastructure-guide-for-founders-starting-up-security-medium
  - bmpi-serverless-ying-yong-kai-fa-xiao-ji
  - litellm-security-incident-attack-chain
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[SecretManagement]] is the practice of storing, distributing, consuming, and rotating credentials, API keys, and other sensitive tokens without leaking them through code, chat, laptops, environment misuse, or ad hoc workflows.

## Current Synthesis
The sources treat leaked or overpowered secrets as a common and costly security failure. Founding teams often put credentials in repositories, environment variables, Slack messages, or laptop copy-paste buffers because that is faster than building a real secrets path. Handling this early can prevent a painful refactor once many applications and systems depend on unsafe patterns.

The priority order is practical but now sharper: prevent exposure, scope every credential to the smallest useful identity and capability, complete revocation whenever exposure is possible, and design consumers for fast rotation. Rotation is not administrative cleanup. LiteLLM's incident shows that one identified but unrevoked master key can remain an entry point for months and, when its target service returns a more privileged token, become the first edge in an organization-wide escalation chain.

The bmpi.dev implementation supplies a weaker but common operational compromise: it prompts for a Terraform variable and injects the Tushare token into the ECS task as an environment variable, avoiding repository storage while declining KMS or Secrets Manager because the author considers the secret low sensitivity. This improves on committing a token but does not by itself provide managed storage, auditability, or rotation.

LiteLLM also expands the unit of analysis from individual secret storage to credential graphs. Its experimental Agent Platform held an organization owner's GitHub CLI OAuth token rather than a service-scoped identity; repository workflows could read maintainer tokens; and one attacker used those linked capabilities to steal further credentials, bypass branch protections, approve a production gate, delete evidence, and publish malicious artifacts. Secret management must therefore inventory transitive authority and keep supposedly independent controls from depending on credentials reachable through the same compromised plane.

## Key Claims
- Secrets leakage and missed revocation can turn a brief exposure into a durable compromise path.
- Early teams often normalize unsafe storage in code, environment variables, chat, and engineer laptops.
- Retrofitting secrets management later can require application and build-system rewrites.
- Keeping a secret out of source control is necessary but not equivalent to managed storage, least privilege, access auditing, revocation, and rotation.
- Credential inventories must include transitive authority: what a secret can query, which stronger credentials that system returns, and which controls those credentials can override.
- Separation of duties fails when nominally distinct identities are all obtainable from the same service, repository, or administrative account.

## Evidence
- Incident cause: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] says leaked secrets are the primary root cause of security incidents the author has worked on.
- Unsafe locations: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] lists source code, environment variables, and engineer laptop copy-paste buffers as early anti-patterns.
- Public leakage: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] says the recurring failure is an API secret appearing on Pastebin or GitHub.
- Retrofit cost: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] warns that mature refactors can require custom application and system-build overhauls.
- Rotation: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] distinguishes keeping secrets out of unsafe places from the harder goal of quick seamless rotation.
- Manual injection: [[bmpi-serverless-ying-yong-kai-fa-xiao-ji]] passes a prompted Terraform variable through the ECS task definition into a container environment variable so the API token is not committed to the repository.
- Deliberate compromise: [[bmpi-serverless-ying-yong-kai-fa-xiao-ji]] rejects KMS and Secrets Manager for this token because their security and operating cost are judged unnecessary for the use case.
- Missed revocation: [[litellm-security-incident-attack-chain]] says the Agent Platform master key was identified for revocation after public exposure in May but remained usable in October.
- Transitive privilege: [[litellm-security-incident-attack-chain]] says the master key authorized an API response containing a GitHub organization owner's CLI OAuth token.
- CI secret access: [[litellm-security-incident-attack-chain]] traces throwaway workflows that posted repository secrets, including maintainer tokens, to an attacker endpoint.
- Shared compromise path: [[litellm-security-incident-attack-chain]] says stolen tokens for separate maintainers were used to approve the release and delete workflow records, while the owner token could override branch protections.
- Broad containment: [[litellm-security-incident-attack-chain]] says LiteLLM responded by assuming every organizational token, key, or authenticator could have been exfiltrated and rotating credentials across internal and vendor systems.

## Counterevidence & Qualifications
The startup-security source treats environment variables as a common unsafe location, while the bmpi.dev source accepts container environment injection for a low-sensitivity token. These positions differ in risk tolerance rather than proving a universal rule. Environment variables can be a delivery mechanism when backed by controlled storage and access, but manual Terraform input alone does not establish encryption at rest, audit history, least-privilege retrieval, or rotation.

LiteLLM's report is a first-party reconstruction and does not publish the raw evidence, complete credential graph, or proof that every token and persistence path was found. Its case establishes the consequence of one missed revocation in that architecture, not that rotation alone prevents compromise. Scope, service identity, non-exportable or short-lived credentials, CI permission design, independent approval roots, monitoring, and external audit retention remain separate controls.

## What Changed
- Added missed revocation as an active attack-chain failure rather than administrative debt.
- Expanded secret inventory from storage locations to transitive authority and shared compromise paths.
- Added CI-readable maintainer tokens and owner-level override capability as evidence that nominal identity separation can collapse.

## Related Concepts
- [[StartupSecurityDebt]] - unsafe secrets workflows are a classic early shortcut that becomes expensive to unwind.
- [[WeakCredentialExposure]] - leaked or weak credentials can turn reachable systems into compromise paths.
- [[ProductionAccessControl]] - temporary access and role-based workflows reduce standing credential risk.
- [[RuntimeConfiguration]] - secrets are a sensitive subset of runtime configuration.
- [[ServerlessComputing]] - managed workloads still need explicit secret storage, delivery, access, and rotation decisions.
- [[ReleasePipelineSecurity]] - release integrity depends on scoped, independently rooted credentials for source changes, approvals, signing, and publication.
- [[DeploymentPipeline]] - CI jobs become credential-exfiltration principals when workflow authors can access broad repository secrets.
