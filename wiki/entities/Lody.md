---
title: "Lody"
type: entity
tags: [ai, coding-agents, local-first, developer-tools]
sources:
  - sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[Lody]] is a cross-platform control plane and proposed team workspace for coding agents running on user-controlled machines.

## Current Profile
The described current product synchronizes coding-agent conversations across desktop, web, and mobile clients, manages Git worktrees for parallel agent tasks, integrates multiple coding CLIs through ACP, and exposes files, diffs, branches, pull requests, and CI state. Its planned scope is broader: use [[Loro]] to preserve structured team context locally, associate it with code and history, and let an agent leader route work among heterogeneous specialist models.

## Key Characteristics
- Controls remote or local coding-agent processes from desktop, web, and mobile interfaces.
- Isolates parallel agent work in automatically managed Git worktrees while leaving the human's ordinary workspace unchanged.
- Combines conversations with code changes, files, branches, pull requests, CI state, and image exchange.
- Uses ACP to switch among coding CLIs and models within one interface.
- Builds synchronization and planned context history on [[Loro]]'s local-first CRDT layer.
- Proposes a context-aware heterogeneous [[AgentTeam]] leader as a future orchestration layer.

## Evidence
- Cross-platform interface: [[sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao]] describes desktop, web, and mobile control and retains desktop and mobile screenshots showing session, conversation, file-change, and pull-request surfaces.
- Parallel coding: [[sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao]] says Lody creates, refreshes, associates, and reclaims agent-only worktrees and branches.
- Model and review surface: [[sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao]] reports ACP-based CLI integration, model switching, per-turn diffs, PR visibility, and CI information.
- Context roadmap: [[sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao]] proposes structured, versioned, local-first storage for decisions, conversations, designs, and iteration history linked to code.

## Qualifications
The available evidence is one founder presentation and product screenshots. It does not independently verify reliability, conflict handling, encryption, account-policy compliance, performance, task quality, security, or productivity, and the context layer plus heterogeneous agent leader are explicitly future directions rather than demonstrated end-to-end capabilities.

## What Changed
- Established Lody's current profile as a cross-platform coding-agent control and review surface.
- Separated current worktree, synchronization, and multi-model behavior from the planned context and agent-leader roadmap.

## Relationships
- [[Loro]] - supplies Lody's local-first CRDT synchronization and planned context data layer.
- [[LeonZhao]] - co-founder and presenter describing the product and roadmap.
- [[AgentTeam]] - planned heterogeneous orchestration pattern for delegating development work.
- [[LocalFirstSoftware]] - governs Lody's user-owned, synchronized context model.
- [[AgentSystemTransparency]] - Lody exposes conversations, diffs, files, pull requests, and CI state to the operator.
