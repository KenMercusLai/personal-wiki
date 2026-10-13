---
title: "Local-First Software"
type: concept
tags: [software, architecture, privacy, agents]
sources:
  - zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[LocalFirstSoftware]] is an application design approach in which the user's device is the primary home and execution context for data, configuration, and interaction, while network services remain optional or explicitly scoped.

## Current Synthesis
The DeepChat case makes local-first design especially consequential for agents. Personal computers hold workspaces, files, histories, preferences, and credentials that can improve context quality, so local placement joins privacy with capability rather than treating it only as offline storage. The client keeps conversations, files, memories, model configuration, and API keys locally, encrypts its SQLite database, integrates with the system Keychain, and requires user authorization before exposing an export key.

Local placement is not a security boundary by itself. Another locally privileged agent can still search for credentials, prompt injection can induce disclosure, and model calls intentionally transmit selected content. Local-first agent software therefore needs encryption, scoped authority, auditability, per-agent isolation, explicit export and synchronization rules, and controls over what leaves the machine.

## Key Claims
- The user's computer can hold more complete and current personal work context than a remote service alone.
- Local-first placement reduces default custody by the application vendor but does not eliminate network transmission or local compromise.
- Local storage needs encryption and operating-system credential protection because other agents and processes may share the machine.
- Export, synchronization, and cloud backup should be explicit user-controlled capabilities rather than hidden consequences of ordinary use.
- For agents, privacy and capability are coupled: richer local context can improve results while expanding the harm of excessive authority.

## Evidence
- Context and placement: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] says DeepChat treats the personal computer as the most complete workspace for work and creative context.
- Local data controls: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] reports local conversations, files, memories, keys, encrypted SQLite, Keychain integration, and authorized export.
- Threat boundary: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] recounts a user's warning that another local agent could read and upload stored API keys.
- Convenience tradeoff: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] reports that many users still trade some privacy for convenience despite privacy-sensitive institutional and individual users.

## Counterevidence & Qualifications
This page currently rests on one first-party project interview rather than a comparative study of local-first and cloud agent products. It does not measure breach incidence, user preferences, offline reliability, synchronization conflicts, recovery, administrative controls, or the cost of maintaining embedded runtimes and encrypted stores. A local-first label also says nothing by itself about telemetry, update checks, model-provider transmission, dependency downloads, or operating-system access.

## What Changed
- Established local-first agent software as a joint context-quality, custody, and permission design problem.
- Made local process and cross-agent access explicit limits on claims of privacy.

## Related Concepts
- [[DeepChat]] - first project case grounding this concept.
- [[AgentPermissionModel]] - limits what a locally running agent may read, execute, or transmit.
- [[AgentMemory]] - local persistence can hold durable personal state but needs lifecycle and privacy controls.
- [[SemanticIsolation]] - local execution still requires capability, credential, network, and side-effect boundaries.
- [[HeadlessAgentArchitecture]] - another agent form that can operate locally while reaching remote channels and services.
