---
title: "TODO Comments"
type: concept
tags: [software-engineering, code-quality]
sources:
  - a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[TodoComments]] are source-code comments that mark future work, such as refactoring, cleanup, or unresolved code smells, in a form commonly recognized by development tools.

## Current Synthesis
The Bourgau source treats TODO comments as a deliberately ordinary infrastructure for [[TechnicalDebtTracking]]. Their value is not that they encode rich metadata, but that they are already visible in places developers look: IDE tabs, code-quality dashboards, framework tasks, and search output. That visibility allowed one teammate to fix a TODO almost immediately after the team changed conventions.

The source also shows why TODOs need naming discipline. A plain TODO should point to a fairly obvious future action, while `TODO SMELL` preserves an observation that the code seems wrong even when the team does not yet know the repair. Community suggestions extend the same idea with custom markers, issue-tracker synchronization, and severity signals such as adding an `X` each time the debt hurts someone.

## Key Claims
- TODO comments are useful technical-debt markers because most development tools already recognize them.
- Plain TODOs and smell-oriented TODOs serve different decision states.
- TODO comments can give later pairs or reviewers a lightweight signal from previous teammates.
- TODO-based tracking needs periodic cleanup because old comments can become debt themselves.
- Teams may improve TODO workflows with custom markers, issue synchronization, or severity conventions.

## Evidence
- Tool recognition: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] names IntelliJ, SonarQube, Rails, CodeClimate, IDE TODO tabs, and grep as discovery surfaces.
- Decision states: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] contrasts direct refactoring comments with `TODO SMELL` comments for unclear responsibilities or other unresolved smells.
- Peer signal: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] says later pairs receive a silent opinion from teammates when they work in the marked code.
- Cleanup need: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] warns that very old TODOs become their own technical debt.
- Workflow extension: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] records reader suggestions for plugins, issue sync, custom markers, and escalating severity through repeated `X` marks.

## Counterevidence & Qualifications
TODO comments are intentionally lightweight and can be ambiguous without ownership, context, or priority. They are a poor substitute for an issue tracker when work needs scheduling, accountability, product tradeoff discussion, or external stakeholder visibility.

## What Changed
- Created the concept to represent TODO comments as a lightweight, tool-supported source-code marker.

## Related Concepts
- [[TechnicalDebtTracking]] - TODO comments can serve as the debt register.
- [[PRReviewHygiene]] - comments should remain clear enough for future reviewers to understand.
- [[SoftwareVerification]] - a TODO is a signal for work, not proof that a change is correct.
- [[CodeReviewPractice]] - review can decide whether to act on, refine, or leave a TODO.
