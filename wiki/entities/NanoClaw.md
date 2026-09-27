---
title: "NanoClaw"
type: entity
tags: [ai, agents, security, runtime]
sources:
  - dont-trust-ai-agents-nanoclaw-blog
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[NanoClaw]] is an AI-agent runtime presented by its builder as a small, reviewable alternative whose primary security boundary is per-agent container isolation rather than model obedience or application-level checks.

## Current Profile
The source describes a one-process core that delegates session management and memory compaction to Anthropic's Agent SDK. Each invocation creates an ephemeral Docker or Apple container, runs the agent without privileges, exposes only explicitly mounted directories, and destroys the container afterward. Agents receive separate filesystems and session histories, while group-level rules restrict cross-chat access and actions.

Defense in depth sits outside the agent-controlled project: a mount allowlist blocks sensitive path patterns by default, and application code is mounted read-only. Functionality is added through skills whose code can be reviewed before a coding agent merges it into the local installation. This favors a narrow, owner-selected attack surface, but the account is a vendor-authored design argument rather than an independent audit.

## Key Characteristics
- Uses a fresh per-invocation container as the primary execution boundary.
- Separates agents by container, filesystem, and Claude session history.
- Runs agents as unprivileged users with only explicit directory mounts.
- Stores mount policy outside the project and blocks common sensitive-path patterns by default.
- Mounts host application code read-only so container-local changes do not persist into it.
- Treats non-main groups as untrusted and restricts cross-group data access and actions.
- Keeps a small core and adds owner-selected functionality through reviewable skill implementations.

## Evidence
- Process containment: [[dont-trust-ai-agents-nanoclaw-blog]] describes ephemeral Docker or Apple containers, unprivileged execution, explicit mounts, and teardown after each invocation.
- Agent and group separation: [[dont-trust-ai-agents-nanoclaw-blog]] says agents have distinct filesystems and histories and that non-main groups cannot act across chat boundaries.
- Defense in depth: [[dont-trust-ai-agents-nanoclaw-blog]] describes the external mount allowlist, sensitive-path blocks, and read-only host code.
- Auditability and extensibility: [[dont-trust-ai-agents-nanoclaw-blog]] presents a 3,968-line NanoClaw snapshot and reviewed skill merges as alternatives to a large monolithic installation.

## Qualifications
All security and comparison claims come from NanoClaw's builder. No penetration test, formal threat model evaluation, vulnerability history, reproducible code-count method, performance comparison, or independent audit is supplied. Containers reduce blast radius but are not absolute boundaries: kernel and runtime vulnerabilities, unsafe mounts, credentials, network access, and legitimate external side effects remain relevant.

## What Changed
- Established NanoClaw as a distinct runtime centered on per-agent ephemeral isolation and a small reviewable core.

## Relationships
- [[GavrielCohen]] - builder and author of the source's security model argument.
- [[OpenClaw]] - larger agent runtime used as NanoClaw's principal comparison target.
- [[ProductionAgentInfrastructure]] - NanoClaw supplies process, filesystem, and cross-agent containment primitives.
- [[AgentPermissionModel]] - isolation is positioned as the hard boundary beneath secondary permission and mount policies.
- [[LLMToolingSkills]] - skills add reviewed, owner-selected functionality outside the small core.
