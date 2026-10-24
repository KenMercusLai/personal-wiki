---
title: "Agent Operating System"
type: concept
tags: [ai, agents, operating-systems, platforms, multi-user]
sources:
  - zgent-design-journey-3
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[AgentOperatingSystem]] is a shared runtime and governance layer that supplies identity, model access, app lifecycle, storage, authorization, and interaction primitives for multiple agent applications and users.

## Current Synthesis
The ZGent source applies the operating-system analogy to fragmentation among AI tools. Instead of every app independently implementing authentication, provider-specific model APIs, credential handling, storage, sharing, and permissions, a common cloud platform supplies those facilities while conventional front-end and back-end apps implement their distinct agent loops. Apps are installable under accounts, may be shared with other users, and can exchange artifacts through account-owned storage after explicit authorization.

The proposal is notable for keeping apps rather than claiming agents make them disappear. Agent conversation becomes a common app primitive, while code still determines task-specific tools, rendering, interaction, and access behavior. Its strongest unresolved question is enforcement: the article describes grants across owners, callers, apps, folders, and files, but does not specify isolation, revocation, audit, credential, malicious-app, prompt-injection, or recovery semantics.

## Key Claims
- Shared identity, model access, app management, storage, and permissions can serve multiple agent products like an operating-system substrate.
- Model credentials can be mediated centrally so users select a model without receiving its API key.
- Apps can remain conventional software while specializing their agent loops and richer task-specific interactions.
- Account-owned storage can carry artifacts across apps without granting every app blanket access.
- Authorization needs to include the resource owner, acting user, app identity, and file or folder scope.
- First-party and third-party apps can share one installation and interface model instead of occupying privileged architectural tiers.

## Evidence
- Fragmentation diagnosis: [[zgent-design-journey-3]] compares inconsistent AI-tool interfaces, payment mechanisms, sharing, and permissions with pre-operating-system computing.
- Common substrate: [[zgent-design-journey-3]] assigns accounts, authentication, model keys, app installation, agent chat, and storage permissions to ZGent itself.
- App specialization: [[zgent-design-journey-3]] contrasts a basic chat loop with ZSlide's tool use, code rendering, screenshots, and coordinate-based region selection.
- Cross-app artifacts: [[zgent-design-journey-3]] describes ZDev output stored in a user's account and later authorized for ZSlide.
- Scoped collaboration: [[zgent-design-journey-3]] describes an app through which other users write separate records into one owner's folder without gaining general access to it.

## Counterevidence & Qualifications
The concept currently rests on one first-party design article. The operating-system analogy does not itself prove kernel-like isolation, durable compatibility, fair scheduling, security, recovery, or ecosystem adoption. Centralizing model credentials and user artifacts can reduce repeated integration work while increasing platform concentration and blast radius. App-code checks are not equivalent to independently enforced capabilities, and the source does not fully distinguish the two in its participant-specific record example.

## What Changed
- Created the concept for ZGent's shared multi-user agent substrate.
- Distinguished common platform services from app-specific agent loops.
- Recorded multi-dimensional storage grants as the central authorization proposal.

## Related Concepts
- [[AgentNativeComputing]] - broader model in which agents become a primary computing interface while software remains an execution supplier.
- [[AgentPermissionModel]] - defines how high-authority agent and app actions should be scoped and enforced.
- [[AgentFilesystem]] - provides the durable artifact layer used across agent workflows.
- [[AIApplicationFramework]] - packages agent-development components but does not necessarily supply the multi-user governance substrate described here.
- [[ProductionAgentInfrastructure]] - adds isolation, effect tracking, recovery, observability, and operational controls absent from the design narrative.
