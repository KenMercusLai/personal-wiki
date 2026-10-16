---
title: "Local-First Software"
type: concept
tags: [software, architecture, privacy, agents]
sources:
  - zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory
  - sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao
  - sneakerweb-hu-lian-wang-de-cui-ruo-yu-ren-xing-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-10-16
knowledge_schema: synthesis-v1
---

## Definition
[[LocalFirstSoftware]] is an application design approach in which the user's device is the primary home and execution context for data, configuration, and interaction, while network services remain optional or explicitly scoped.

## Current Synthesis
The DeepChat case makes local-first design especially consequential for agents. Personal computers hold workspaces, files, histories, preferences, and credentials that can improve context quality, so local placement joins privacy with capability rather than treating it only as offline storage. The client keeps conversations, files, memories, model configuration, and API keys locally, encrypts its SQLite database, integrates with the system Keychain, and requires user authorization before exposing an export key.

The Lody and Loro case adds replicated collaboration to that placement model. The user's device remains the primary data home, while CRDT operations synchronize state across devices and team members, allow offline work, preserve versions, and converge once replicas receive the same operation set. This distinguishes local-first from local-only storage and cloud-centralized authority, but convergence is not the same as intent correctness: an automatic merge can still resolve a conflict in a way users did not mean. Sneakerweb extends the placement model from application state to published websites: a reader imports a complete replayable copy and the proposed Willow layer makes USB, local radio, LAN, or internet links interchangeable synchronization transports.

Local placement is not a security boundary by itself. Another locally privileged agent can still search for credentials, prompt injection can induce disclosure, and model calls intentionally transmit selected content. Local-first agent software therefore needs encryption, scoped authority, auditability, per-agent isolation, explicit export and synchronization rules, and controls over what leaves the machine.

## Key Claims
- The user's computer can hold more complete and current personal work context than a remote service alone.
- Local-first placement reduces default custody by the application vendor but does not eliminate network transmission or local compromise.
- Local storage needs encryption and operating-system credential protection because other agents and processes may share the machine.
- Export, synchronization, and cloud backup should be explicit user-controlled capabilities rather than hidden consequences of ordinary use.
- For agents, privacy and capability are coupled: richer local context can improve results while expanding the harm of excessive authority.
- Local-first collaboration needs explicit convergence, versioning, offline, conflict, and recovery semantics; device ownership alone does not define them.
- Local-first publishing can give readers independently replayable copies, but durable custody also needs identity, integrity, dependency capture, discovery, and compatible runtimes.

## Evidence
- Context and placement: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] says DeepChat treats the personal computer as the most complete workspace for work and creative context.
- Local data controls: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] reports local conversations, files, memories, keys, encrypted SQLite, Keychain integration, and authorized export.
- Threat boundary: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] recounts a user's warning that another local agent could read and upload stored API keys.
- Convenience tradeoff: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] reports that many users still trade some privacy for convenience despite privacy-sensitive institutional and individual users.
- Replicated collaboration: [[sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao]] presents Loro CRDT operations as the basis for offline-first multi-device and multi-user convergence with version history.
- Topology and conflict boundary: [[sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao]] includes an inspected local-first topology and explicitly says convergent merges may still violate human intent.
- Transport-independent publishing: [[sneakerweb-hu-lian-wang-de-cui-ruo-yu-ren-xing-luo-li-li-de-shu-ju-zhong-xin]] describes imported site packages intended to synchronize over physical media, local links, or the internet while remaining replayable offline.

## Counterevidence & Qualifications
This page rests on three first-party project accounts rather than comparative evidence. They do not measure breach incidence, user preferences, offline reliability, synchronization-conflict rates, replay longevity, recovery, administrative controls, or the cost of maintaining embedded runtimes, encrypted stores, archives, and replicated state. Loro's encryption and ownership claims lack a protocol description, threat model, key lifecycle, or audit; Willow and Sneakerweb are described as immature and slow. A local-first label also says nothing by itself about telemetry, update checks, remote dependencies, synchronization metadata, key compromise, malicious content, or operating-system access.

## What Changed
- Added CRDT-backed offline and multi-device convergence as a collaboration mechanism distinct from local-only storage.
- Made convergence-versus-intent correctness, key management, synchronization metadata, and recovery explicit qualification boundaries.
- Extended local-first from private application state to publisher-generated, independently replayable website replicas.
- Added transport independence and long-term replay as distinct from ordinary cloud synchronization.

## Related Concepts
- [[DeepChat]] - first project case grounding this concept.
- [[AgentPermissionModel]] - limits what a locally running agent may read, execute, or transmit.
- [[AgentMemory]] - local persistence can hold durable personal state but needs lifecycle and privacy controls.
- [[SemanticIsolation]] - local execution still requires capability, credential, network, and side-effect boundaries.
- [[HeadlessAgentArchitecture]] - another agent form that can operate locally while reaching remote channels and services.
- [[Loro]] - project case for CRDT-backed local-first synchronization and versioned context.
- [[Lody]] - agent product applying local-first synchronization across desktop, web, mobile, and team context.
- [[Sneakerweb]] - applies local usability and later synchronization to packaged websites.
- [[OfflineWebDistribution]] - treats physical and local transports as first-class paths for local-first replicas.
- [[DigitalContentDurability]] - identifies the preservation and runtime requirements beyond merely storing a local copy.
