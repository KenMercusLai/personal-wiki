---
title: "Technical Debt Tracking"
type: concept
tags: [software-engineering, technical-debt]
sources:
  - a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog
  - using-technical-debt-as-a-time-machine-brian-york-medium
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[TechnicalDebtTracking]] is the practice of recording, surfacing, and revisiting codebase liabilities or aggregate debt trends so teams can decide what to tolerate, when to repay it, and how maintenance choices relate to product and organizational change.

## Current Synthesis
The two sources operate at different levels. Bourgau presents technical-debt tracking as a low-friction workflow for individual liabilities: his team replaced explicit `@TechnicalDebt` annotations with ordinary [[TodoComments]] already understood by IDEs, dashboards, and command-line search. York uses an aggregate time series of repository size and technical debt to interpret [[Bliss]]'s changing company priorities, including early customer validation, fundraising, and engineering hiring.

Together, they frame tracking as decision support rather than an automatic repayment queue. Teams need shared conventions, contextual interpretation, and regular review; an individual TODO can be actionable or merely flag a smell, while an aggregate percentage can look precise without explaining its calculation. York's 20% endpoint and acceptable zone are therefore useful as Bliss's stated risk tolerance, not as universal standards. The common principle is to make debt visible enough to support explicit tradeoffs without treating zero debt as the goal.

## Key Claims
- Low-friction markers can make technical-debt tracking easier to keep current than custom annotations.
- Tracking works better when the marker is visible in everyday development tools.
- Teams need a shared convention for distinguishing actionable refactoring tasks from unresolved code smells.
- Longitudinal aggregate measures can connect engineering change to customer validation, fundraising, and hiring.
- Debt thresholds and tool-generated severity require local interpretation rather than universal acceptance.
- Regular review turns scattered markers and trend data into explicit maintenance decisions.

## Evidence
- Low-friction markers: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] reports that `@TechnicalDebt` annotations became too ceremonious and stale, while ordinary TODO comments were easy to add.
- Tool visibility: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] cites IntelliJ, SonarQube, Rails, CodeClimate, IDE TODO tabs, and grep as built-in discovery surfaces.
- Shared convention: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] distinguishes direct TODO refactoring suggestions from `TODO SMELL` comments where the problem is visible but the action is unclear.
- Longitudinal context: [[using-technical-debt-as-a-time-machine-brian-york-medium]] maps a repository plateau to fundraising and later code growth with controlled debt to new engineering hires.
- Local interpretation: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] warns that fixed tool costs may misrepresent lasting debt, while [[using-technical-debt-as-a-time-machine-brian-york-medium]] presents 20% and an expanding acceptable zone without defining a general calculation.
- Maintenance decisions: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] recommends cleanup and retrospective review; [[using-technical-debt-as-a-time-machine-brian-york-medium]] describes reducing debt before and during team expansion to limit later refactoring and onboarding cost.

## Counterevidence & Qualifications
Both sources are practitioner accounts rather than comparative studies. TODO-based tracking may fail when teams lack cleanup habits or need richer ownership, prioritization, compliance, or risk metadata. Aggregate debt percentages can hide heterogeneous risks, depend heavily on the measurement tool, and invite false comparison across repositories; York's chart does not identify its debt formula or repository-size unit. Neither source establishes that a particular debt ratio causes better product, financial, or staffing outcomes.

## What Changed
- Expanded the concept from item-level TODO tracking to include aggregate debt trends over time.
- Added business and organizational context as inputs to debt-tolerance decisions.
- Qualified numerical debt thresholds as locally defined measures rather than universal benchmarks.

## Related Concepts
- [[TodoComments]] - source-code marker used as the tracking mechanism.
- [[CodeReviewPractice]] - reviewers and pairs may encounter TODOs while deciding whether nearby code should change.
- [[SoftwareVerification]] - debt markers need separate evidence before they become safe code changes.
- [[ProductRetrospectives]] - recurring problem review can identify TODO hotspots.
- [[StartupScaling]] - fundraising and team growth can change which debt level is sustainable.
- [[ProductMarketFit]] - early validation pressure can justify temporarily accepting more debt.
