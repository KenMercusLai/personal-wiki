---
title: "Mobile Agent Development"
type: concept
tags: [ai, developer-tools, mobile, cloud-development]
sources:
  - claude-code-on-the-go
  - hu-yuan-ming-wo-gei-10-ge-claude-code-da-gong
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[MobileAgentDevelopment]] is a coding-agent workflow where a phone acts as the human control surface for cloud-hosted development sessions, with agents doing long-running work and notifying the user when input is needed.

## Current Synthesis
The current evidence is a single concrete architecture: a phone uses Termius and mosh over Tailscale to connect to an isolated Vultr VM running [[ClaudeCode]]. tmux preserves sessions when the phone sleeps or networks change, while git worktrees let several feature branches run in separate windows. The decisive design move is not the phone terminal alone; it is the notification loop. Claude Code's PreToolUse hook catches AskUserQuestion events, sends the question through a Poke webhook, and lets the user resume only when human judgment is needed.

This makes mobile development less like typing code on a tiny screen and more like supervising asynchronous work. The phone is used for task kickoff, review, and clarification, while compute, repo state, long-running shells, and multiple agent sessions live on the cloud VM. The setup also defines a trust boundary: permissive agent mode is tolerated because the VM is disposable, lacks production access, contains only necessary development secrets, blocks public SSH, and is cost-bounded by hourly pricing and explicit start/stop scripts.

Hu Yuanming describes a second architecture that removes the terminal from most interactions. An EC2-hosted Python manager launches non-interactive Claude Code processes, consumes streamed JSON logs, exposes task and planning state through a phone-friendly web interface, and accepts voice instructions. SSH remains a recovery path when the manager fails. Together, the cases suggest a progression from resilient remote shell, to interrupt-driven notifications, to a domain-specific control plane for task creation, planning, status, review, and recovery.

## Key Claims
- Phones can supervise coding agents when the actual development environment runs on a cloud host and the interface is reduced to kickoff, planning, status, review, clarification, and recovery.
- Network-resilient shells, private networking, and tmux session persistence are infrastructure prerequisites for practical mobile agent work.
- Push notifications turn agent clarification into an interrupt-driven loop instead of requiring constant terminal polling.
- Parallel agent sessions need worktree isolation and deterministic port assignment to avoid local-development conflicts.
- Permissive agent operation from a phone depends on environmental isolation, limited secrets, no production access, and cost controls.
- Purpose-built web and voice interfaces can reduce small-screen terminal friction, while SSH remains a useful recovery channel when the control plane fails.

## Evidence
- Cloud control surface: [[claude-code-on-the-go]] describes running six Claude Code agents from a phone using Termius, mosh, Tailscale, and a Vultr VM.
- Architecture flow: [[claude-code-on-the-go]] includes a diagram where Phone -> Tailscale VPN -> Vultr VM -> Claude Code -> PreToolUse hook -> Poke webhook -> Phone forms the clarification loop.
- Resilient connection: [[claude-code-on-the-go]] says mosh survives WiFi/cellular transitions, dead zones, and phone sleep, while tmux keeps sessions alive after disconnects.
- Notification loop: [[claude-code-on-the-go]] uses a Claude Code hook for AskUserQuestion that extracts the question and POSTs it to Poke so the phone notification shows the needed input.
- Parallel isolation: [[claude-code-on-the-go]] uses separate git worktrees per feature and a hash of branch name to allocate deterministic local ports.
- Trust boundary: [[claude-code-on-the-go]] says permissive mode is bounded by a disposable VM, no production access, only necessary secrets, Tailscale-only SSH, cloud firewalling, nftables, fail2ban, and hourly VM cost.
- Web control plane: [[hu-yuan-ming-wo-gei-10-ge-claude-code-da-gong]] wraps `claude -p` in a Python manager with streamed JSON logs, queue state, batched Plan Mode review, and a Safari-installed phone interface.
- Voice and recovery: [[hu-yuan-ming-wo-gei-10-ge-claude-code-da-gong]] adds voice recognition to inputs and keeps SSH as a fallback when the web manager breaks.

## Counterevidence & Qualifications
The evidence consists of two practitioner setups rather than a general benchmark. Both assume cloud administration, worktrees, agent tooling, and comfort recovering failed infrastructure. Granda's setup has an explicit disposable-VM, private-network, limited-secret boundary; Hu mentions EC2 isolation and backups but does not document an equivalent security boundary in detail, and his use of permissive mode materially increases the cost of mistakes. Voice access can improve capture while also creating distraction and accidental-command risks. Granda also notes that mosh does not forward the SSH agent, so some GitHub-authenticated git operations still require regular SSH inside tmux.

## What Changed
- Expanded the control surface from resilient phone terminals and notifications to a purpose-built web manager with voice input and batched planning.
- Preserved SSH as the recovery path beneath the higher-level interface.

## Related Concepts
- [[ClaudeCode]] - the source's central coding agent.
- [[AgenticWorkflowPatterns]] - mobile agent development combines async checkpoints, parallel sessions, and human-in-the-loop clarification.
- [[AgentExperience]] - notifications are an interaction layer for agent clarification.
- [[AgentPermissionModel]] - isolation and limited secrets form the safety boundary.
- [[AICodingPractice]] - mobile supervision changes how coding-agent work is paced and reviewed.
- [[SoftwareVerification]] - worktree and port isolation keep parallel feature work checkable.
- [[BottleneckAwareAICoding]] - parallel sessions help only if review and verification capacity are not overwhelmed.
- [[AIVoiceInput]] - speech reduces task-capture friction when a keyboard is unavailable.
- [[PersonalSoftware]] - Hu's mobile control plane exists to build and operate a private CEO support system.
