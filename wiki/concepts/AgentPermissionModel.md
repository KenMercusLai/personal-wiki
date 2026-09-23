---
title: "Agent Permission Model"
type: concept
tags: [ai, agents, safety, permissions]
sources:
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
  - lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[AgentPermissionModel]] is a risk-tiered control system for deciding when an AI agent may read, write, delete, execute, access private data, or perform irreversible operations.

## Current Synthesis
RORIRI argues that current agent permission prompts are too flat: asking the user to approve everything produces fatigue, while YOLO-style permission skipping removes the safety boundary. A better model should resemble operating-system and mobile permission design, where low-risk actions are quiet, privacy-sensitive actions are visible, destructive actions require confirmation, and account- or system-level actions demand stronger authentication.

OpenClaw makes the threat composition behind these tiers concrete: untrusted content, tool authority, and autonomous scheduling can turn prompt injection into external action. Sandboxing, network allowlists, least-privilege operating-system identities, domain-bound credentials, and confirmation for sensitive operations move policy from prose toward enforceable boundaries, though they do not by themselves establish semantic legitimacy or safe recovery.

## Key Claims
- All-or-nothing permissions are a poor fit for agents with heterogeneous action risk.
- Confirmation dialogs should be reserved for operations whose reversibility, scope, or sensitivity warrants interruption.
- Low-risk read or routine actions can be silent when surrounded by auditability and scope control.
- Privacy-sensitive actions should be visible even when they do not require immediate blocking.
- Destructive or high-impact actions should require explicit confirmation or stronger authentication.
- Permission systems need behavior-level alarms and audit trails because users cannot reliably judge every command or API call.
- Skills may describe credential and host restrictions, but the runtime should independently enforce scopes, destinations, and sensitive-action gates.

## Evidence
- Flat prompt problem: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says current coding-agent permission dialogs ask users to judge every read, write, and command.
- YOLO risk: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] treats `--dangerously-skip-permissions` as evidence that friction can push users into unsafe bypasses.
- Tiered analogy: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] compares possible agent permissions with Android and iOS handling of camera, microphone, screen recording, confirmations, and passwords.
- Action tiers: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] sketches read as silent, write as visible, delete as confirmable, and disk-formatting-like actions as requiring stronger authentication.
- Alarm integration: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] argues that dangerous behavior sets can be statically intercepted without asking users about every harmless action.
- Threat composition: [[lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai]] combines hostile inputs, shell and file access, and scheduled autonomy into a prompt-injection-to-action risk.
- Layered controls: [[lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai]] recommends sandboxing, domain allowlists, least-privilege users, scoped key handling, dry runs, and approval for sensitive actions.

## Counterevidence & Qualifications
The sources outline a product direction rather than a complete permission taxonomy. Real deployments still need domain-specific risk scoring, user role models, audit storage, escalation paths, revocation, side-effect semantics, and integration with sandbox or capability systems. Local execution and written Skill rules do not guarantee that a model will distinguish hostile data from instructions.

## What Changed
- Created the concept page for tiered agent permissions as an alternative to constant prompts or unchecked YOLO mode.
- Added the untrusted-input plus tool-access plus autonomy threat composition and runtime-enforced network, credential, sandbox, and approval controls.

## Related Concepts
- [[AgentSystemTransparency]] - audit trails and visible state make permissions meaningful.
- [[AgentExperience]] - permission design is a core AX layer for high-authority agents.
- [[CapabilityGateway]] - capability gateways can enforce permission policy around tool calls.
- [[ChangeSafety]] - permission tiers reduce the risk of destructive operational changes.
- [[VibeCoding]] - coding-agent workflows expose permission fatigue and destructive-action risk.
- [[HeadlessAgentArchitecture]] - scheduled background work increases the need for enforceable authority boundaries.
