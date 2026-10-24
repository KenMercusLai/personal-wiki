---
title: "The attack chain behind the v1.107.0 LiteLLM release"
type: source
tags: [security, supply-chain, incident-response, github, ci-cd]
date: 2026-10-23
source_file: /mnt/ken_personal_wiki/Articles/litellm-security-incident-attack-chain.md
---

## Summary
[[LiteLLM]]'s root-cause analysis traces the malicious `v1.107.0` release from a master key accidentally committed to a public repository and never revoked, through an internal agent service that exposed a GitHub organization owner's CLI token, to CI-based theft of two more maintainer tokens. The attacker used those identities to redirect the private release workflow to a lookalike fork, approve and publish signed PyPI and container artifacts, delete workflow records, and force-push the visible history clean, showing why [[ReleasePipelineSecurity]] depends on independent authority boundaries, complete audit evidence, and rapid credential revocation rather than signatures or nominal approval counts alone.

## Key Claims
- A publicly committed Agent Platform master key remained usable for more than four months because the identified revocation action did not occur.
- The internal Agent Platform API returned a GitHub CLI OAuth token tied to an organization owner, converting one service-secret leak into owner-level access across the GitHub organization.
- The attacker used throwaway GitHub Actions workflows to exfiltrate repository secrets, including two additional maintainers' GitHub CLI tokens, and later used distinct stolen identities for release approval and deletion of run records.
- The attacker bypassed branch protection with the owner's token, changed the private release workflow to build from the lookalike `Berri-AI/litellm` fork, and published seven PyPI wheels plus Docker Hub and GHCR images as `v1.107.0`.
- A two-person release gate did not provide independent approval because one attacker controlled both identities; the source also notes that an organization owner could have removed the restriction entirely.
- Deleting workflow runs and force-pushing `main` removed ordinary evidence from the repository view, but commit SHAs, organization audit records, and token hashes preserved enough evidence to reconstruct the chain.
- LiteLLM contained the incident by locking registries, removing almost every GitHub organization member, assuming all organizational authenticators were exposed, and beginning comprehensive rotation before restoring release capability.

## Key Quotes
> "The key used was a GitHub CLI OAuth token associated with our GitHub organization owner's account." - on the authority exposed through the Agent Platform.

> "This incident has provided a strong illustration of the risks associated with failing to rotate a potentially exposed key." - on the missed revocation that enabled the attack chain.

## Connections
- [[LiteLLM]] - publisher of the compromised package and author of the root-cause analysis.
- [[ReleasePipelineSecurity]] - the incident joins source selection, branch protection, CI secrets, approval identities, signing, publication, and audit retention into one attack path.
- [[SecretManagement]] - an unrevoked public secret and CI-accessible maintainer tokens supplied the attacker's escalating credentials.
- [[DeploymentPipeline]] - the attacker subverted the pipeline's source input and approval gate while allowing it to build, sign, and publish normally.
- [[GitHub]] - hosted the repositories, OAuth identities, Actions workflows, branch protections, audit logs, and organization permissions used throughout the incident.
- [[IncidentManagement]] - containment included registry lockdown, organization-wide access removal, broad credential-compromise assumptions, investigation, and staged reinstatement.
- [[IncidentCommunication]] - LiteLLM distinguishes this completed root-cause analysis from earlier status updates whose working assumptions proved incomplete.

## Contradictions
- No direct contradiction with an existing wiki page was found. The incident qualifies [[DeploymentPipeline]] by showing that a passing build, signed artifacts, and two nominal approvers do not establish source integrity or independent authorization when the control plane and identities share a compromise path.
- The post explicitly corrects LiteLLM's earlier public suspicion that the first tokens came from logs of an internal LiteLLM deployment; the completed investigation instead traced the owner token to the Agent Platform API. That earlier post is not present in this wiki.
