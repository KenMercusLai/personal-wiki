---
title: "Mobile Agent Development"
type: concept
tags: [ai, developer-tools, mobile, cloud-development]
sources:
  - claude-code-on-the-go
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[MobileAgentDevelopment]] is a coding-agent workflow where a phone acts as the human control surface for cloud-hosted development sessions, with agents doing long-running work and notifying the user when input is needed.

## Current Synthesis
The current evidence is a single concrete architecture: a phone uses Termius and mosh over Tailscale to connect to an isolated Vultr VM running [[ClaudeCode]]. tmux preserves sessions when the phone sleeps or networks change, while git worktrees let several feature branches run in separate windows. The decisive design move is not the phone terminal alone; it is the notification loop. Claude Code's PreToolUse hook catches AskUserQuestion events, sends the question through a Poke webhook, and lets the user resume only when human judgment is needed.

This makes mobile development less like typing code on a tiny screen and more like supervising asynchronous work. The phone is used for task kickoff, review, and clarification, while compute, repo state, long-running shells, and multiple agent sessions live on the cloud VM. The setup also defines a trust boundary: permissive agent mode is tolerated because the VM is disposable, lacks production access, contains only necessary development secrets, blocks public SSH, and is cost-bounded by hourly pricing and explicit start/stop scripts.

## Key Claims
- Phones can supervise coding agents when the actual development environment runs on a persistent cloud VM.
- Network-resilient shells, private networking, and tmux session persistence are infrastructure prerequisites for practical mobile agent work.
- Push notifications turn agent clarification into an interrupt-driven loop instead of requiring constant terminal polling.
- Parallel agent sessions need worktree isolation and deterministic port assignment to avoid local-development conflicts.
- Permissive agent operation from a phone depends on environmental isolation, limited secrets, no production access, and cost controls.
- The workflow works best for tasks that can run asynchronously for minutes before asking for human input.

## Evidence
- Cloud control surface: [[claude-code-on-the-go]] describes running six Claude Code agents from a phone using Termius, mosh, Tailscale, and a Vultr VM.
- Architecture flow: [[claude-code-on-the-go]] includes a diagram where Phone -> Tailscale VPN -> Vultr VM -> Claude Code -> PreToolUse hook -> Poke webhook -> Phone forms the clarification loop.
- Resilient connection: [[claude-code-on-the-go]] says mosh survives WiFi/cellular transitions, dead zones, and phone sleep, while tmux keeps sessions alive after disconnects.
- Notification loop: [[claude-code-on-the-go]] uses a Claude Code hook for AskUserQuestion that extracts the question and POSTs it to Poke so the phone notification shows the needed input.
- Parallel isolation: [[claude-code-on-the-go]] uses separate git worktrees per feature and a hash of branch name to allocate deterministic local ports.
- Trust boundary: [[claude-code-on-the-go]] says permissive mode is bounded by a disposable VM, no production access, only necessary secrets, Tailscale-only SSH, cloud firewalling, nftables, fail2ban, and hourly VM cost.

## Counterevidence & Qualifications
The evidence is one practitioner's setup rather than a general benchmark. It assumes comfort with terminals on phones, cloud VM administration, Tailscale, tmux, worktrees, hooks, and paying for burst cloud compute. The source also notes one operational limitation: mosh does not forward the SSH agent, so some GitHub-authenticated git operations still require regular SSH inside tmux.

## What Changed
- Created the concept to capture phone-controlled, cloud-hosted coding-agent work.

## Related Concepts
- [[ClaudeCode]] - the source's central coding agent.
- [[AgenticWorkflowPatterns]] - mobile agent development combines async checkpoints, parallel sessions, and human-in-the-loop clarification.
- [[AgentExperience]] - notifications are an interaction layer for agent clarification.
- [[AgentPermissionModel]] - isolation and limited secrets form the safety boundary.
- [[AICodingPractice]] - mobile supervision changes how coding-agent work is paced and reviewed.
- [[SoftwareVerification]] - worktree and port isolation keep parallel feature work checkable.
- [[BottleneckAwareAICoding]] - parallel sessions help only if review and verification capacity are not overwhelmed.
