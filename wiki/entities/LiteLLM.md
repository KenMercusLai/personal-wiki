---
title: "LiteLLM"
type: entity
tags: [company, open-source, ai-infrastructure, security]
sources:
  - litellm-security-incident-attack-chain
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[LiteLLM]] is represented here as the maintainer of an open-source model-access project and associated agent and release infrastructure whose `v1.107.0` package and container release was compromised in October 2026.

## Current Profile
LiteLLM's own root-cause analysis describes a security boundary that extended beyond its main repository. An experimental self-hosted Agent Platform held a broadly scoped GitHub CLI token for an organization owner and exposed that token through an API reachable with a master key accidentally committed to a public harness repository. Failure to complete the identified revocation let the initial exposure remain exploitable for more than four months.

The attacker then used GitHub-hosted CI as a credential-exfiltration mechanism, accumulated maintainer identities, changed a private release workflow to build a lookalike fork, and used separate stolen tokens to trigger, approve, and conceal the malicious release. LiteLLM's response locked public registries, reduced the GitHub organization to one trusted account, assumed organization-wide credential exposure, and delayed further releases until it believed the process was safe.

## Key Characteristics
- Maintains software distributed through PyPI, Docker Hub, and GitHub Container Registry.
- Operated an experimental Agent Platform for self-hosted cloud agents that could file GitHub pull requests.
- Bound the Agent Platform to a GitHub organization owner's broadly scoped CLI OAuth token rather than a dedicated least-privilege service identity.
- Used a private project-releaser workflow with staging, production approval, signing, and registry publication.
- Temporarily allowed any two engineers to trigger and approve releases during a higher-frequency release period.
- Responded to the compromise with registry lockdown, drastic GitHub membership reduction, comprehensive credential rotation, forensic reconstruction, and delayed release restoration.

## Evidence
- Initial exposure and authority: [[litellm-security-incident-attack-chain]] says a public repository briefly contained the Agent Platform master key and the platform API later returned an organization owner's GitHub CLI token.
- Credential escalation: [[litellm-security-incident-attack-chain]] traces throwaway workflows that posted repository secrets, including two maintainer tokens, to an attacker-controlled endpoint.
- Release subversion: [[litellm-security-incident-attack-chain]] says the attacker overrode branch protection, redirected the releaser to a lookalike fork, passed the production gate with a stolen token, and published signed packages and images.
- Containment: [[litellm-security-incident-attack-chain]] records registry lockdown, removal of nearly all organization members, broad rotation, and a temporary halt to releases.
- Investigation quality: [[litellm-security-incident-attack-chain]] distinguishes its reconstructed timeline from earlier public updates and correlates actions through audit logs, token hashes, commit SHAs, network indicators, and registry events.

## Qualifications
This profile is based on LiteLLM's own incident report, not an independent audit. It provides unusually specific timestamps, credentials, commits, IP addresses, and corrective statements, but does not include the malicious payload analysis, complete internal architecture, raw audit evidence, full token inventory, customer impact, or proof that every accessible credential and persistence path was found. The report says process improvements would be published later, so it does not establish the durability or effectiveness of the remediation program.

## What Changed
- Created LiteLLM's entity profile around the `v1.107.0` release compromise and response.
- Recorded the Agent Platform, GitHub organization, CI-secret, and release-workflow boundaries that formed the attack chain.
- Preserved the first-party evidence and incomplete-remediation qualifications.

## Relationships
- [[ReleasePipelineSecurity]] - LiteLLM's compromised release is the central case for identity, source, approval, signing, and audit controls.
- [[SecretManagement]] - missed revocation and CI-accessible tokens enabled escalation from one exposed key to organization-wide authority.
- [[GitHub]] - hosted the identities, repositories, workflows, branch protections, and audit records involved in the incident.
- [[DeploymentPipeline]] - LiteLLM's staging and production path built, signed, and published attacker-selected source.
- [[IncidentManagement]] - LiteLLM used broad containment assumptions and staged restoration after detecting the malicious release.
- [[IncidentCommunication]] - the company published status updates followed by a corrective canonical root-cause analysis.
