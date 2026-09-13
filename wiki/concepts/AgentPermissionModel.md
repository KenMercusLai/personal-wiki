---
title: "Agent Permission Model"
type: concept
tags: [ai, agents, safety, permissions]
sources:
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[AgentPermissionModel]] is a risk-tiered control system for deciding when an AI agent may read, write, delete, execute, access private data, or perform irreversible operations.

## Current Synthesis
RORIRI argues that current agent permission prompts are too flat: asking the user to approve everything produces fatigue, while YOLO-style permission skipping removes the safety boundary. A better model should resemble operating-system and mobile permission design, where low-risk actions are quiet, privacy-sensitive actions are visible, destructive actions require confirmation, and account- or system-level actions demand stronger authentication.

## Key Claims
- All-or-nothing permissions are a poor fit for agents with heterogeneous action risk.
- Confirmation dialogs should be reserved for operations whose reversibility, scope, or sensitivity warrants interruption.
- Low-risk read or routine actions can be silent when surrounded by auditability and scope control.
- Privacy-sensitive actions should be visible even when they do not require immediate blocking.
- Destructive or high-impact actions should require explicit confirmation or stronger authentication.
- Permission systems need behavior-level alarms and audit trails because users cannot reliably judge every command or API call.

## Evidence
- Flat prompt problem: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says current coding-agent permission dialogs ask users to judge every read, write, and command.
- YOLO risk: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] treats `--dangerously-skip-permissions` as evidence that friction can push users into unsafe bypasses.
- Tiered analogy: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] compares possible agent permissions with Android and iOS handling of camera, microphone, screen recording, confirmations, and passwords.
- Action tiers: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] sketches read as silent, write as visible, delete as confirmable, and disk-formatting-like actions as requiring stronger authentication.
- Alarm integration: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] argues that dangerous behavior sets can be statically intercepted without asking users about every harmless action.

## Counterevidence & Qualifications
The source outlines a product direction rather than a complete permission taxonomy. Real deployments still need domain-specific risk scoring, user role models, audit storage, escalation paths, and integration with sandbox or capability systems.

## What Changed
- Created the concept page for tiered agent permissions as an alternative to constant prompts or unchecked YOLO mode.

## Related Concepts
- [[AgentSystemTransparency]] - audit trails and visible state make permissions meaningful.
- [[AgentExperience]] - permission design is a core AX layer for high-authority agents.
- [[CapabilityGateway]] - capability gateways can enforce permission policy around tool calls.
- [[ChangeSafety]] - permission tiers reduce the risk of destructive operational changes.
- [[VibeCoding]] - coding-agent workflows expose permission fatigue and destructive-action risk.
