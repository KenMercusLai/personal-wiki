---
title: "OpenClaw"
type: entity
tags: [ai, agents, security]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
  - mu-jiang-chui-zi-ding-zi
  - lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai
  - dont-trust-ai-agents-nanoclaw-blog
  - openclaw-architecture-explained-how-it-works
  - chuang-zao-yi-zhi-long-xia-xu-yao-xie-shi-me-frosts-blog
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Overview
[[OpenClaw]] is a local-first personal-agent platform created by [[PeterSteinberger]]. It combines a central Gateway, messaging and control interfaces, an embedded agent engine, injected tools, file-based Skills, durable sessions, memory, and scheduled work, while exemplifying the risks created when probabilistic models receive real system permissions.

## Current Profile
Across the sources, OpenClaw moves from a product and safety reference to a concrete runtime architecture. PsiACE frames it as a skill-extensible personal assistant entering daily life, in contrast with [[Bub]]'s multi-person group-chat orientation. Guanlan uses it to motivate production controls for agents with broad permissions.

Lencx's analysis and a second code-oriented overview supply complementary architectural accounts. Pi runs in process as the model, streaming, agent-loop, and tool-execution engine, while OpenClaw owns sessions, channels, capability injection, sandbox integration, and product policy. A single WebSocket Gateway is the control plane: channel adapters and desktop, CLI, web, or mobile clients converge on access checks and session resolution before the runtime assembles context, invokes the model, executes tools, persists state, and returns platform-formatted output. Plugins extend channel, tool, memory, and provider surfaces without changing that core flow.

Durability is split across workspace instructions, configuration, credentials, session event logs, memory files, and searchable indexes. Session metadata plus append-only transcripts, branchable histories, compaction, pre-compaction memory flushes, and hybrid semantic/keyword retrieval support long-running work, while heartbeats and webhooks enable proactive or externally triggered tasks. Session routing also supports distinct workspaces, models, instructions, and policy per channel or group, making a session both a continuity unit and a proposed trust boundary.

This flexibility raises rather than removes the control burden. Hostile web, email, or [[Moltbook]] content can influence an agent that also holds shell, filesystem, network, and API authority. The combined record supports transparent logs, scoped tools, confirmation for sensitive side effects, dry runs, sandboxing, allowlists, and least privilege, while the production-infrastructure source argues that resumability and durable effect semantics must go further than ordinary process isolation.

Frost Ming uses OpenClaw differently: as the visible target that a small coding agent can reproduce through Telegram, basic tools, and Skills, and then as a foil for removing most framework-owned behavior. That prototype strengthens the claim that some integrations can be composed outside a large runtime, but it does not reproduce or evaluate OpenClaw's memory, routing, isolation, recovery, policy, or observability layers.

[[NanoClaw]]'s builder supplies an adversarial comparison: he says OpenClaw executes on the host by default, makes sandboxing opt-in, and shares one container across agents when sandboxing is enabled. Paolo's overview itself is inconsistent about defaults, variously saying DM and group sessions are sandboxed by default, can default to isolation, and that sandboxing is opt-in. The combined record therefore supports policy and deployment flexibility, not a verified default-isolation guarantee. The NanoClaw account is first-party competitor commentary rather than an independent audit, and its own size evidence conflicts: the prose says nearly half a million lines, while the embedded treemap labels OpenClaw as 839,234 lines without a reproducible counting method.

## Key Characteristics
- Centers one WebSocket Gateway per host as the control plane between channel adapters, control clients, session routing, and the Pi-based runtime.
- Normalizes messaging channels while allowing sessions to map to different workspaces, models, instructions, tools, and trust policies.
- Injects a centrally governed tool surface and discovers plugins for channels, tools, memory backends, and model providers.
- Persists append-only session events and external memory, including branches, compaction summaries, pre-compaction flushes, and hybrid retrieval.
- Loads relevant file-based Skills selectively and connects external protocols such as MCP through bridges rather than expanding the core engine.
- Supports heartbeats, cron jobs, webhooks, Canvas/A2UI, voice, and device nodes alongside request-response messaging.
- Combines broad utility with significant permission, prompt-injection, cross-agent isolation, observability, external-effect recovery, privacy, and token-cost risks.

## Evidence
- Product frame: [[mu-jiang-chui-zi-ding-zi]] describes OpenClaw as a skill-extensible personal assistant and contrasts it with Bub's group-chat design.
- Control plane and message flow: [[openclaw-architecture-explained-how-it-works]] traces clients and channel adapters through Gateway authentication, access control, session resolution, runtime execution, persistence, and response delivery.
- Runtime split: [[lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai]] and [[openclaw-architecture-explained-how-it-works]] describe Pi embedding, OpenClaw-owned routing and policy, custom tool injection, and streaming tool loops.
- Extension and interaction surfaces: [[openclaw-architecture-explained-how-it-works]] diagrams channel, tool, memory, and provider plugins plus Canvas/A2UI, voice, and mobile-node capabilities.
- Long-running continuity: [[lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai]] and [[openclaw-architecture-explained-how-it-works]] connect session stores, transcript trees, branch summaries, compaction, memory flushes, and retrieval.
- Safety signal: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] uses OpenClaw to show that real system permissions make agent risk concrete.
- Runtime controls: [[lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai]] proposes logs, confirmations, dry runs, sandboxing, network allowlists, and least privilege.
- Infrastructure gap: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] argues that ordinary sandbox and workflow systems still lack agent-specific effect logs, capability mediation, and resumability.
- Isolation critique: [[dont-trust-ai-agents-nanoclaw-blog]] claims host execution is the default, sandboxing is optional, and sandboxed agents share a container, creating a possible cross-agent data boundary problem.
- Default ambiguity: [[openclaw-architecture-explained-how-it-works]] internally alternates among default, configurable-default, and opt-in descriptions of DM/group sandboxing.
- Audit-scope critique: [[dont-trust-ai-agents-nanoclaw-blog]] contrasts OpenClaw's broad monolith with NanoClaw's small core, though its prose and treemap disagree materially on OpenClaw's line count.
- Minimal reproduction: [[chuang-zao-yi-zhi-long-xia-xu-yao-xie-shi-me-frosts-blog]] reports that Bub approximated OpenClaw's visible messaging functions apart from memory and tool differences, then replaced framework-owned sending with an agent-created Skill.

## Qualifications
The detailed implementation accounts are secondary analyses rather than reproducible primary code audits, and the sharpest isolation and code-size criticisms come from the builder of a competing project. Features, defaults, counts, paths, and integrations can change; the architecture article's sandbox-default language is internally inconsistent. The Bub comparison covers visible Telegram behavior, not feature parity or production guarantees. IM-first interaction relocates rather than eliminates UI needs, local orchestration does not keep configured model or voice-provider traffic local, and transcript persistence does not by itself provide safe replay of external side effects. The viral-growth chart lacks a reproducible data method. Claims about low resource use, preferred hardware, future web standards, and model-routing economics remain source-scoped.

## What Changed
- Recast the architecture around the single Gateway control plane and the full channel-to-session-to-runtime message path.
- Added plugin, prompt-assembly, Canvas/A2UI, routing, storage, and deployment structure from the diagram-backed source.
- Tightened the security judgment: session policy is flexible, but sandbox defaults are not established consistently and self-hosting does not make every dependency local.
- Added Bub's minimal reproduction as evidence for composable surface behavior, not full runtime equivalence.

## Relationships
- [[HeadlessAgentArchitecture]] - OpenClaw is the source's principal IM-first, daemon-based implementation example.
- [[LLMToolingSkills]] - file-based Skills extend OpenClaw's operating knowledge and tool use.
- [[Moltbook]] - agent-oriented network and skill ecosystem connected to OpenClaw.
- [[CapabilityGateway]] - scoped capability mediation is needed around OpenClaw's real system permissions.
- [[SemanticIsolation]] - process sandboxing alone cannot decide whether a model-chosen action is legitimate.
- [[ProductionAgentInfrastructure]] - durable effects, recovery, and resumability extend OpenClaw's session mechanisms.
- [[Bub]] - Bub is contrasted with OpenClaw's personal-assistant orientation.
- [[NanoClaw]] - competing runtime whose builder contrasts per-agent ephemeral containers and a small core with OpenClaw's architecture.
- [[ConversationalUI]] - Canvas/A2UI supplements messaging with agent-generated interactive interfaces.
- [[AINativeAgentArchitecture]] - uses OpenClaw as the feature target and framework-heavy contrast for a smaller agent-managed runtime.
