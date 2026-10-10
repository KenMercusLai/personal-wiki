---
title: "Grok Bot"
type: entity
tags: [ai, agents, automation]
sources:
  - cong-lauren-bu-xin-gui-hua-shuo-qi-wo-yong-grok-bot-da-growth-researcher-cai-guo-de-keng
last_updated: 2026-10-10
knowledge_schema: synthesis-v1
---

## Overview
[[GrokBot]] is an AI teammate product represented here through [[MaiYang]]'s first-person experiments with specialized bot roles, Skills, scheduled routines, and real-world permissions.

## Current Profile
Mai Yang describes creating a Growth Researcher bot intended to scan global growth cases, extract strategy, and deliver a weekday report. The routine ran and produced long memos, but she judged them difficult to understand and unusable for concrete product decisions, so she disabled the schedule. She contrasts this with a narrower AICon bot whose job was to explain conference parameters and metrics and organize notes into an artifact she could follow and edit.

The article presents Grok Bot as capable of scheduled work and actions involving accounts, files, and websites. That capability makes role design and authority design inseparable: the author recommends validating one bounded result before turning the procedure into a Skill or routine, and withholding blanket permission for sending, publishing, spending, deleting, or overwriting until experience supports a narrower grant.

## Key Characteristics
- Supports named bot roles oriented around delegated work.
- Supports Skills that encode how work is performed.
- Supports routines that schedule recurring execution.
- Can interact with real accounts, files, and web surfaces according to the source.
- Produces output whose fluency and length do not guarantee usefulness.
- Requires narrow outcomes, acceptance checks, and staged permissions for reliable use.

## Evidence
- Broad-role failure: [[cong-lauren-bu-xin-gui-hua-shuo-qi-wo-yong-grok-bot-da-growth-researcher-cai-guo-de-keng]] describes the Growth Researcher role, its long memos, repeated structural revisions, and low perceived usefulness.
- Routine state: [[cong-lauren-bu-xin-gui-hua-shuo-qi-wo-yong-grok-bot-da-growth-researcher-cai-guo-de-keng]] includes the retained screenshot showing the daily growth-research report disabled on September 5.
- Narrow-role comparison: [[cong-lauren-bu-xin-gui-hua-shuo-qi-wo-yong-grok-bot-da-growth-researcher-cai-guo-de-keng]] says the AICon bot returned conference notes that the author could follow and revise.
- Capability and risk: [[cong-lauren-bu-xin-gui-hua-shuo-qi-wo-yong-grok-bot-da-growth-researcher-cai-guo-de-keng]] names account login, file action, web use, sending, public publishing, spending, deletion, and overwrite as operations requiring deliberate permission boundaries.

## Qualifications
The page relies on one user's retrospective rather than product documentation, task logs, reliability tests, security analysis, or a representative user sample. The failed Growth Researcher does not distinguish product limitations from role breadth, prompt design, source quality, language, evaluation criteria, or operator expectations. The source reports an intended redesign but no results from the restarted role.

## What Changed
- Created a source-scoped product profile centered on role scope, routine validation, and permission staging.

## Relationships
- [[MaiYang]] - operator reporting the Growth Researcher and AICon bot experiments.
- [[LaurenTan]] - practitioner associated with Grok Bot in the source.
- [[DeliverableFirstAgentDesign]] - proposed operating method for validating Grok Bot roles before automation.
- [[AgentPermissionModel]] - governs the product's access to consequential external actions.
- [[TaskContingentAICollaboration]] - supplies the delegation and acceptance boundary for individual tasks.
