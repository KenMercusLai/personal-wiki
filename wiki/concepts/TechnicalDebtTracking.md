---
title: "Technical Debt Tracking"
type: concept
tags: [software-engineering, technical-debt]
sources:
  - a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[TechnicalDebtTracking]] is the practice of recording, surfacing, and periodically revisiting known codebase liabilities so teams can decide when and how to repay them.

## Current Synthesis
The Bourgau source presents technical-debt tracking as a workflow-design problem rather than a need for a specialized system. The team first tried explicit `@TechnicalDebt` annotations, but the ceremony made people hesitant and allowed annotations to drift out of date. Replacing them with ordinary [[TodoComments]] moved the marker into a format already understood by IDEs, dashboards, and command-line search.

The practice depends on social agreement as much as tool support. The source recommends validating the convention with teammates, documenting it in working agreements or coding conventions, and interpreting tool output with context. A TODO may signal a clear refactoring opportunity, while `TODO SMELL` may only preserve a peer's observation that something feels wrong. Regular cleanup and retrospective review prevent the tracking mechanism from becoming a new layer of debt.

## Key Claims
- Low-friction markers can make technical-debt tracking easier to keep current than custom annotations.
- Tracking works better when the marker is visible in everyday development tools.
- Teams need a shared convention for distinguishing actionable refactoring tasks from unresolved code smells.
- Tool-generated severity and commit warnings should be adapted to the team's intended use of debt markers.
- Regular cleanup and problem-log review turn scattered comments into a continuous-improvement loop.

## Evidence
- Low-friction markers: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] reports that `@TechnicalDebt` annotations became too ceremonious and stale, while ordinary TODO comments were easy to add.
- Tool visibility: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] cites IntelliJ, SonarQube, Rails, CodeClimate, IDE TODO tabs, and grep as built-in discovery surfaces.
- Shared convention: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] distinguishes direct TODO refactoring suggestions from `TODO SMELL` comments where the problem is visible but the action is unclear.
- Tool interpretation: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] warns that IDE commit checks and fixed SonarQube remediation costs may misrepresent lasting technical debt.
- Continuous improvement: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] recommends fixing old TODOs regularly and linking problem logs to TODOs so retrospectives can identify hotspots.

## Counterevidence & Qualifications
The source is a practitioner account from one team and side project, not a comparative study. TODO-based tracking may fail when teams lack cleanup habits, use tools that treat all TODOs as temporary pre-commit work, or need richer ownership, prioritization, compliance, or risk metadata than a comment can carry.

## What Changed
- Created the concept to capture TODO-based technical-debt tracking as a lightweight software-engineering workflow.

## Related Concepts
- [[TodoComments]] - source-code marker used as the tracking mechanism.
- [[CodeReviewPractice]] - reviewers and pairs may encounter TODOs while deciding whether nearby code should change.
- [[SoftwareVerification]] - debt markers need separate evidence before they become safe code changes.
- [[ProductRetrospectives]] - recurring problem review can identify TODO hotspots.
- [[TeamFocus]] - shared agreements reduce coordination friction around debt cleanup.
