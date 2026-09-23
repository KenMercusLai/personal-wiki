---
title: "OpenClaw"
type: entity
tags: [ai, agents, security]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
  - mu-jiang-chui-zi-ding-zi
  - lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[OpenClaw]] is presented as a local-first personal-agent runtime that combines an embedded agent engine, messaging channels, injected tools, file-based Skills, durable sessions, and scheduled work. It is also a prominent example of the risks created when probabilistic models receive real system permissions.

## Current Profile
Across the sources, OpenClaw moves from a product and safety reference to a concrete runtime architecture. PsiACE frames it as a skill-extensible personal assistant entering daily life, in contrast with [[Bub]]'s multi-person group-chat orientation. Guanlan uses it to motivate production controls for agents with broad permissions.

Lencx's analysis supplies the architectural account. Pi runs in process as the model, streaming, agent-loop, and tool-execution engine, while OpenClaw owns sessions, channels, capability injection, sandbox integration, and product policy. Messaging applications provide cross-device interaction and asynchronous notifications; a daemon listens for messages, plans and executes tool calls, and reports results. Session metadata plus append-only JSONL transcripts, branchable histories, pre-compaction memory flushes, and pruning safeguards support long-running work, while heartbeats enable proactive tasks.

This flexibility raises rather than removes the control burden. Hostile web, email, or [[Moltbook]] content can influence an agent that also holds shell, filesystem, network, and API authority. The combined record supports transparent logs, scoped tools, confirmation for sensitive side effects, dry runs, sandboxing, allowlists, and least privilege, while the production-infrastructure source argues that resumability and durable effect semantics must go further than ordinary process isolation.

## Key Characteristics
- Embeds Pi as an in-process agent engine while OpenClaw controls sessions, channels, tools, policy, and integration.
- Uses IM channels as low-friction, cross-platform interfaces for asynchronous personal-assistant work.
- Replaces built-in engine tools with a centrally injected and potentially auditable capability surface.
- Persists session metadata and append-only event transcripts, including branches, compaction summaries, and memory flushes.
- Loads file-based Skills and connects external protocols such as MCP through bridges rather than expanding the core engine.
- Supports proactive heartbeat work and personality or continuity files alongside request-response interaction.
- Combines broad utility with significant permission, prompt-injection, observability, recovery, and token-cost risks.

## Evidence
- Product frame: [[mu-jiang-chui-zi-ding-zi]] describes OpenClaw as a skill-extensible personal assistant and contrasts it with Bub's group-chat design.
- Architecture: [[lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai]] describes Pi embedding, custom tool injection, channel routing, durable transcripts, heartbeat scheduling, and context safeguards.
- Long-running continuity: [[lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai]] connects session stores, transcript trees, branch summaries, and pre-compaction persistence.
- Safety signal: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] uses OpenClaw to show that real system permissions make agent risk concrete.
- Runtime controls: [[lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai]] proposes logs, confirmations, dry runs, sandboxing, network allowlists, and least privilege.
- Infrastructure gap: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] argues that ordinary sandbox and workflow systems still lack agent-specific effect logs, capability mediation, and resumability.

## Qualifications
The detailed implementation account comes from one secondary analysis rather than a primary code audit, and features, names, and integrations can change. IM-first interaction relocates rather than eliminates UI needs, local deployment does not neutralize prompt injection, and transcript persistence does not by itself provide safe replay of external side effects. Claims about low resource use, preferred Mac hardware, future web standards, and model-routing economics remain source-scoped.

## What Changed
- Added the embedded Pi engine, injected-tool, IM bus, session-transcript, branch, compaction, and heartbeat architecture.
- Reconciled personal-assistant utility with the stronger production-infrastructure warning about permissions and recoverable side effects.
- Added [[Moltbook]] ecosystem, token-cost, observability, and prompt-injection qualifications.

## Relationships
- [[HeadlessAgentArchitecture]] - OpenClaw is the source's principal IM-first, daemon-based implementation example.
- [[LLMToolingSkills]] - file-based Skills extend OpenClaw's operating knowledge and tool use.
- [[Moltbook]] - agent-oriented network and skill ecosystem connected to OpenClaw.
- [[CapabilityGateway]] - scoped capability mediation is needed around OpenClaw's real system permissions.
- [[SemanticIsolation]] - process sandboxing alone cannot decide whether a model-chosen action is legitimate.
- [[ProductionAgentInfrastructure]] - durable effects, recovery, and resumability extend OpenClaw's session mechanisms.
- [[Bub]] - Bub is contrasted with OpenClaw's personal-assistant orientation.
