---
title: "OpenClaw Architecture, Explained: How It Works"
type: source
tags: [ai, agents, openclaw, architecture, security]
date: 2026-02-11
source_file: "/mnt/ken_personal_wiki/Articles/OpenClaw Architecture, Explained How It Works.md"
---

## Summary
This code-oriented secondary analysis presents [[OpenClaw]] as a local-first personal-agent platform whose single WebSocket Gateway separates messaging and control interfaces from session routing, context assembly, model invocation, tool execution, and persistent state. It describes extensibility, multi-agent routing, Canvas/A2UI interaction, memory, security controls, and deployment topologies, while showing that self-hosted orchestration does not make model calls local or eliminate prompt-injection and capability risks. The article also attributes OpenClaw's early productization and rapid adoption to creator [[PeterSteinberger]], but its implementation details and growth claims are point-in-time assertions rather than an independently reproduced audit.

![Chart compares cumulative GitHub stars for OpenClaw, React, Vue, Linux, and Next.js and depicts OpenClaw rising almost vertically to roughly 180,000 stars in early 2026](../../wiki-assets/openclaw-architecture-explained-how-it-works/github-star-growth.png)

## Key Claims
- OpenClaw uses a hub-and-spoke architecture: messaging channels and control clients converge on one Gateway, which applies access control and session resolution before dispatching work to the agent runtime.

![OpenClaw hub-and-spoke architecture routes desktop, CLI, web, mobile, and messaging channels through a Gateway, access control, and session manager into the Pi agent runtime, memory, prompt builder, tool executor, and capabilities](../../wiki-assets/openclaw-architecture-explained-how-it-works/system-architecture.png)

- Channel adapters normalize authentication, inbound text and media, sender and group policy, platform formatting, chunking, and outbound delivery, keeping channel-specific behavior outside the runtime.
- The runtime resolves a session, assembles history, workspace instructions, selected Skills, memory, and tool definitions, then streams model output through an iterative tool-call loop and persists the resulting state.

![Prompt assembly combines built-in and plugin tool definitions, session history, selected Skills, memory search, AGENTS.md, SOUL.md, TOOLS.md, and Pi Agent Core instructions into conversation history, user message, and system prompt for model invocation](../../wiki-assets/openclaw-architecture-explained-how-it-works/prompt-assembly.png)

![End-to-end message sequence checks channel permissions, returns a pairing code when access fails, or resolves a session, builds a prompt, streams model and tool calls, saves state, and formats response chunks when access succeeds](../../wiki-assets/openclaw-architecture-explained-how-it-works/message-flow.jpg)

- Plugins are discovered from package metadata and extend four surfaces—channels, tools, memory, and model providers—through validated registration into the relevant core subsystem.

![Plugin loader and registry discover package metadata and TypeBox schemas, then integrate channel, tool, memory, and provider plugins with the channel router, tool executor, memory search, and agent runtime](../../wiki-assets/openclaw-architecture-explained-how-it-works/plugin-extension-flow.png)

- Session keys also express trust boundaries: operator, DM, and group contexts can receive different workspaces, models, tool policies, and sandbox rules; routing can map channels to fully separate agent instances.

![Multi-agent routing maps WhatsApp, Discord, and Telegram sessions to default, community, and support agents with different models, workspaces, AGENTS.md, SOUL.md, and Skills](../../wiki-assets/openclaw-architecture-explained-how-it-works/multi-agent-routing.jpg)

- Canvas runs separately from the Gateway and uses a bidirectional A2UI sequence: the agent pushes declarative HTML, the user action returns as an event and tool call, and updated state is pushed back to the client.

![Canvas and A2UI sequence sends agent HTML to the Canvas server and browser, returns a user action as a canvas tool call, and pushes the agent's updated state back to the display](../../wiki-assets/openclaw-architecture-explained-how-it-works/canvas-a2ui-sequence.jpg)

- Configuration, workspace instructions, credentials, sessions, and searchable memory are separate state domains; the article describes append-only session events, compaction with a pre-compaction memory flush, and hybrid vector plus BM25 retrieval.

![OpenClaw storage layout separates workspace files and Skills, environment-overridden configuration, credentials, sessions, and memory databases around Gateway and agent runtime processes](../../wiki-assets/openclaw-architecture-explained-how-it-works/storage-layout.png)

- Security is layered across loopback binding, authentication, device and DM pairing, allowlists, group mention policies, tool-policy precedence, session-specific sandboxing, and constrained filesystem and network exposure; prompt text is guidance, while these runtime controls provide enforcement.
- The same Gateway architecture can run locally, as a macOS background service, on a loopback-bound VPS reached by SSH or Tailscale, or in a public Fly.io container backed by persistent storage.

![Local development keeps browser, CLI, and Gateway on one loopback-bound developer machine](../../wiki-assets/openclaw-architecture-explained-how-it-works/local-development.png)

![macOS production runs the loopback-bound Gateway as a LaunchAgent managed by a menu bar app with WebChat and Voice Wake](../../wiki-assets/openclaw-architecture-explained-how-it-works/macos-production.png)

![Remote VPS deployment connects local web and CLI clients to a loopback-bound systemd Gateway through an encrypted SSH port-forward](../../wiki-assets/openclaw-architecture-explained-how-it-works/vps-ssh-tunnel.png)

![Tailscale deployment connects macOS, web, and CLI clients over tailnet HTTPS to a Gateway exposed by Tailscale Serve on a VPS](../../wiki-assets/openclaw-architecture-explained-how-it-works/vps-tailscale.png)

![Fly.io deployment places a persistent OpenClaw volume and containerized Gateway behind public managed HTTPS ingress](../../wiki-assets/openclaw-architecture-explained-how-it-works/flyio-deployment.png)

## Key Quotes
> "The LLM provides intelligence; OpenClaw provides the operating system." - on the distinction between the model and its execution environment.

## Connections
- [[OpenClaw]] - project whose control plane, runtime, state, extension, security, and deployment layers are analyzed.
- [[PeterSteinberger]] - identified as OpenClaw's creator and the focal builder at the early ClawCon event.
- [[HeadlessAgentArchitecture]] - the interface/runtime separation and persistent Gateway exemplify an IM-first agent control plane.
- [[LLMToolingSkills]] - relevant Skills are selectively injected into the per-turn context rather than all being loaded blindly.
- [[AgentMemory]] - sessions, memory files, compaction, vector search, and BM25 support continuity beyond the active prompt.
- [[AgentPermissionModel]] - channel checks, pairing, allowlists, policy precedence, and sandbox rules assign authority by trust context.
- [[ProductionAgentInfrastructure]] - the source supplies a concrete execution stack while leaving durable external-effect recovery less developed.
- [[ConversationalUI]] - Canvas and A2UI add generated interactive surfaces beside messaging conversation.

## Contradictions
- The article says DM and group sessions are sandboxed by default, later says sandboxing is opt-in, and elsewhere uses the softer formulation that those sessions "can default" to Docker isolation. This unresolved configuration/default distinction should not be treated as a verified guarantee.
- The star-history graphic supports the direction of rapid growth but does not provide its extraction date, counting method, or reproducible data, so the roughly 180,000-star figure remains a point-in-time source claim.
- The source's self-hosted and private framing is qualified by its own account: configured model and voice providers still receive requests, and host-side credentials and tools remain exposed to whatever boundaries the operator actually configures.
