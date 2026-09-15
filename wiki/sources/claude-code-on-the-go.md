---
title: "Claude Code On-The-Go"
type: source
tags: [ai, developer-tools, mobile, cloud-development]
date: 2026-01-02
source_file: /mnt/ken_personal_wiki/Articles/Claude Code On-The-Go.md
---

## Summary
Miguel Granda describes a [[MobileAgentDevelopment]] setup for running six [[ClaudeCode]] agents from a phone through Termius, mosh, Tailscale, a pay-per-use Vultr VM, tmux, git worktrees, and push notifications. The post's architecture diagram shows a phone connecting through a Tailscale VPN to a cloud VM, where Claude Code uses a PreToolUse hook and Poke webhook to notify the phone when human input is needed.

## Key Claims
- A phone can become a practical control surface for parallel coding-agent work when terminal access, network resilience, session persistence, and notifications are combined.
- The architecture uses Termius plus mosh over Tailscale to reach an isolated Vultr VM with no public SSH listener.
- tmux persistence lets multiple Claude Code agents keep working across phone sleep, network transitions, and reopened terminal sessions.
- Claude Code hooks can turn AskUserQuestion events into push notifications, shifting the workflow from constant terminal checking to async human intervention.
- Running Claude Code in permissive mode is framed as acceptable only because the VM is disposable, isolated from production, and cost-bounded.
- Git worktrees and deterministic branch-name-based port allocation allow multiple features and agents to run concurrently without port conflicts.
- The workflow fits tasks that can run for 10-20 minutes before needing user input, letting development happen in small gaps rather than at a dedicated desk.

## Key Quotes
> "The loop is: kick off a task, pocket the phone, get notified when Claude needs input." - on the async phone-driven workflow.

> "The VM is isolated--no access to production systems, no secrets beyond what's needed for development." - on the trust boundary for permissive mode.

## Connections
- [[ClaudeCode]] - central coding agent being operated from a phone and cloud VM.
- [[MobileAgentDevelopment]] - the source is a concrete architecture for phone-controlled agent work.
- [[AgenticWorkflowPatterns]] - the setup combines async checkpoints, parallel agents, and worktree-isolated tasks.
- [[AgentExperience]] - push notifications make clarification requests visible outside the terminal.
- [[AgentPermissionModel]] - the trust model relies on isolation, limited secrets, and bounded cost rather than fine-grained permissions.
- [[AICodingPractice]] - the setup extends AI coding practice into mobile, parallel, cloud-hosted workflows.
- [[SoftwareVerification]] - parallel worktrees and deterministic port allocation help keep concurrent feature work testable.
- [[LLMContextManagement]] - tmux sessions, worktrees, and persistent shell environments externalize state around Claude Code sessions.

## Contradictions
- No direct contradiction found. The source extends existing Claude Code and agent-workflow pages by showing a mobile, cloud-hosted operating environment rather than a new agent architecture.
