---
title: "MisterMorph"
type: entity
tags: [ai, agents, security, open-source]
sources:
  - mistermorph-de-agent-an-quan-kai-fa-zha-ji-ge-ci-jing-li
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[MisterMorph]] is an AI-agent project described by its author through the security boundaries used to constrain filesystem, shell, network, credential, and Skill access.

## Current Profile
The source presents MisterMorph as a practical implementation of layered agent security rather than a claim of complete defense. It runs under ordinary operating-system privileges and can rely on systemd or container hardening for the hard local boundary. Its application layer mediates outbound access, redacts known sensitive data, pauses risky workflows for asynchronous approval, and records auditable actions.

Its distinctive mechanism is a named `auth_profile`. A Skill declares which profile it needs, while trusted runtime configuration binds that profile to a secret reference, URL and method restrictions, redirect and proxy policy, private-address denial, and credential injection into a specific tool field. The model and Skill can request an authorized operation without receiving the credential itself.

## Key Characteristics
- Treats agent construction as permission-system engineering rather than prompt rules alone.
- Delegates user, filesystem, process, and basic network boundaries to operating-system, container, or service-manager enforcement.
- Keeps credentials outside model-visible prompts, histories, logs, and tool arguments through runtime mediation.
- Uses named authentication profiles to bind secrets to destinations, methods, and injection rules.
- Limits the application guard to outbound allowlists, redaction, asynchronous approval, and audit.

## Evidence
- Boundary design: [[mistermorph-de-agent-an-quan-kai-fa-zha-ji-ge-ci-jing-li]] describes ordinary-user execution, read-only roots or limited writable directories, systemd hardening, and removal of general network clients.
- Credential mediation: [[mistermorph-de-agent-an-quan-kai-fa-zha-ji-ge-ci-jing-li]] keeps API keys in the runtime and injects them into authorized `url_fetch` calls rather than revealing them to the model or Skill.
- Profile scope: [[mistermorph-de-agent-an-quan-kai-fa-zha-ji-ge-ci-jing-li]] gives a Moltbook profile restricted by URL prefix, HTTP methods, redirects, proxy use, private IPs, and authorization-header injection.
- Guard scope: [[mistermorph-de-agent-an-quan-kai-fa-zha-ji-ge-ci-jing-li]] narrows application controls to outbound allowlists, redaction, approvals, and audit to avoid an unmaintainable policy cross-product.

## Qualifications
The source is the author's experience report, not an independent security assessment. It supplies no penetration test, formal policy model, measured false-positive or false-negative rates, implementation audit, or proof that its controls cover indirect exfiltration, compromised dependencies, runtime flaws, DNS or redirect edge cases, shell-mediated network paths, or malicious authorized endpoints. Redaction is explicitly described as damage limitation rather than primary prevention.

## What Changed
- Created the project profile from the author's security-design account.

## Relationships
- [[AgentSecurityLayering]] - MisterMorph implements the layered division between hard boundaries, credential mediation, and application guards.
- [[Moltbook]] - MisterMorph uses Moltbook as an example of a Skill restricted by an authentication profile.
- [[SemanticIsolation]] - profile-bound tools constrain legitimate actions by credential, destination, method, and network policy.
- [[AgentPermissionModel]] - asynchronous approval and least privilege bound sensitive actions.
- [[SecretManagement]] - runtime injection keeps credentials outside model-visible context.
