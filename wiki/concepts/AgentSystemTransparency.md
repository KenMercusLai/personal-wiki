---
title: "Agent System Transparency"
type: concept
tags: [ai, agents, safety, auditability]
sources:
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[AgentSystemTransparency]] is the ability for users and systems to know what an agent is doing, trace why it acted, inspect what changed, and recover when an action was wrong.

## Current Synthesis
RORIRI places transparency between user intent and external action. Coding agents expose the problem sharply because they can operate filesystems and command lines; a stream of confirmation prompts formally asks for consent but often fails as a human-factors system. Better transparency requires independent records of actions and context, semantic versioning or checkpointing, behavior-level alarms, and permission models that match risk.

## Key Claims
- Prompt-by-prompt permission confirmation can transfer risk judgment to users who lack time, expertise, or attention.
- Auditability should bind external changes to the conversation and intent context that produced them.
- File and database changes need recoverable, inspectable histories independent of the agent's own narration.
- Behavior alarms can catch dangerous action patterns without asking the user to approve every low-risk step.
- Sandboxes reduce blast radius but become difficult when the agent's legitimate task crosses sandbox boundaries.
- Transparency is a product-design problem, not merely a warning label or a stronger model problem.

## Evidence
- Confirmation fatigue: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] argues that repeated prompts make even experienced developers approve actions mechanically.
- High-authority examples: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] discusses destructive Claude Code and Terraform cases as evidence that agent actions need post-hoc traceability and prevention.
- Audit direction: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] cites Git/chat binding, Aura's semantic version-control idea, and Git-Context-Controller-style checkpointing as early directions.
- Behavior alarms: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] proposes static rules for patterns such as deleting root paths, rewriting Git history, or writing outside the project.
- Sandbox qualification: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says Docker-style isolation can help coding agents but conflicts with system agents that must operate outside the container.

## Counterevidence & Qualifications
The source gives product and architectural directions, not a complete security model. Auditability and alarms still need careful definitions of intent, scope, privacy, false positives, and rollback semantics.

## What Changed
- Created the concept page for agent transparency as action traceability, auditability, behavior monitoring, and recovery.

## Related Concepts
- [[AgentExperience]] - transparency is a cross-layer requirement for AX.
- [[AgentPermissionModel]] - risk-tiered permissions operationalize transparent control.
- [[VibeCoding]] - coding agents make transparency urgent because they act on code, files, and infrastructure.
- [[ChangeSafety]] - both focus on making operational changes inspectable and recoverable.
- [[HumanCodeResponsibility]] - human accountability requires enough visibility to review agent work.
