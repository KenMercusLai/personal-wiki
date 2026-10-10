---
title: "ToastPlan"
type: entity
tags: [software, productivity, okr, ai-agents]
sources:
  - xiang-zuo-xiang-you-leetao
last_updated: 2026-10-10
knowledge_schema: synthesis-v1
---

## Overview
[[ToastPlan]] is [[Leetao]]'s OKR and task-management software, used both for personal organization and for assigning, tracking, and auditing AI-agent work.

## Current Profile
In the source, ToastPlan acts as a human-facing control and observation layer around [[Kuafu]]. The agent can retrieve a dated task list containing ordinary and AI-assigned work, update task state, and leave timestamped activity records. The graphical interface is primarily for the person supervising the system and gives Leetao a reference point for later agent optimization.

## Key Characteristics
- Combines personal OKR or task management with agent work tracking.
- Lets an agent retrieve and update its own assigned tasks.
- Distinguishes AI and user activity in an audit interface.
- Keeps a graphical oversight surface for the human operator.

## Evidence
- Task integration: [[xiang-zuo-xiang-you-leetao]] shows a Telegram agent retrieving six ToastPlan tasks, including AI-designated work.
- Auditability: [[xiang-zuo-xiang-you-leetao]] shows an AI-filtered audit screen with timestamped task updates.
- Human role: [[xiang-zuo-xiang-you-leetao]] says the graphical product is for people and serves as a reference metric for improving the agent.

## Qualifications
The source provides two screenshots and the builder's brief description, but no full product specification, repository, access-control model, user study, task-completion metric, or evidence that the audit trail is tamper-resistant or sufficient for agent governance.

## What Changed
- Created ToastPlan's profile from its task-retrieval and AI-audit role in Leetao's agent workflow.

## Relationships
- [[Leetao]] - creator who uses ToastPlan to manage personal and agent work.
- [[Kuafu]] - agent runtime connected to ToastPlan tasks and activity tracking.
- [[AgentTeam]] - task visibility can help a human supervise role-separated agent work.
- [[HumanInTheLoop]] - ToastPlan keeps task state and AI activity visible to a person.
