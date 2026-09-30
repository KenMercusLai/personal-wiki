---
title: "Slock"
type: entity
tags: [ai, agents, collaboration, messaging]
sources:
  - intention-is-all-you-need
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[Slock]] is an agent-native instant-messaging application presented as a Slack-like group-chat environment for collaboration among agents across machines.

## Current Profile
The source values Slock less as a novel messaging product than as an interface choice. Agents communicate through ordinary chat messages, while channels separate working contexts; a familiar human collaboration primitive thereby becomes the visible orchestration surface. This is evidence about the product's design framing and the author's experience, not a complete account of its runtime, protocol, security, persistence, or reliability architecture.

## Key Characteristics
- Uses group chat as the primary cross-agent collaboration surface.
- Uses channels to separate contexts rather than exposing low-level orchestration constructs to users.
- Frames agent coordination through familiar human collaboration behavior.
- Presents itself with playful Slack-like naming while the source credits its design as substantively agent-native.

## Evidence
- Collaboration surface: [[intention-is-all-you-need]] says agent-to-agent communication occurs through normal group-chat messages.
- Context boundary: [[intention-is-all-you-need]] says channels isolate working context.
- Design contrast: [[intention-is-all-you-need]] contrasts Slock's visible simplicity with an agent-generated proposal containing a task graph, event log, scheduler, versioned artifacts, approval gates, and recovery machinery.

## Qualifications
The evidence comes from one enthusiastic user essay and one screenshot of a conversation inside the product. The screenshot describes an agent's proposed architecture rather than Slock's implementation, and the source provides no benchmark, protocol specification, security analysis, failure test, or comparison with other orchestration systems. A simple interface can conceal rather than eliminate distributed coordination and production-safety complexity.

## What Changed
- Created the entity page from the first source describing Slock's agent-native group-chat design.

## Relationships
- [[IntentionDrivenSoftware]] - Slock is presented as an interface whose abstraction level matches human collaborative intent.
- [[AIAgentCollaboration]] - messages and channels provide its visible multi-agent coordination model.
- [[DistributedConsensus]] - simple chat interaction does not remove the need to reconcile incompatible agent interpretations.
- [[ProductionAgentInfrastructure]] - runtime permissions, effects, recovery, and audit remain below the source's interface-level account.
