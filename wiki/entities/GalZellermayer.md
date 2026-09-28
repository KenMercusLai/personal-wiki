---
title: "Gal Zellermayer"
type: entity
tags: [software-management, agile, software-quality]
sources:
  - gal-zellermayer-0-bugs-policy
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[GalZellermayer]] is represented here as a VMware Israel R&D manager who proposed the [[ZeroBugsPolicy]] from experience with several Scrum teams.

## Current Profile
In the 2016 article, Zellermayer argues that software teams should replace indefinite bug deferral with a prompt fix-or-close decision. He treats in-sprint defects as evidence that a feature is unfinished, while other defects should be repaired immediately or in the next sprint only when the value warrants the effort.

His account combines lifecycle-cost reasoning with an organizational claim: old bugs lose context and create repeated triage work, while feature pressure repeatedly pushes them down a mixed backlog. He also reports a culture effect in which developers pursue higher quality because defects cannot be parked for later. These are practitioner judgments from his own management experience rather than comparative measurements.

## Key Characteristics
- Frames retained bug inventory as avoidable repair and coordination cost.
- Uses Scrum's definition of done to require immediate repair of in-sprint defects.
- Prefers explicit non-repair decisions over low-priority promises that are unlikely to be honored.
- Challenges hardening phases, bug sprints, and mixed backlogs as remedies for chronic defect accumulation.
- Treats the zero-bug rule as an unusual case where explicit process can support culture change.

## Evidence
- Experience base: [[gal-zellermayer-0-bugs-policy]] says the policy arose from five years across several Scrum teams and identifies VMware Israel as the author's professional setting.
- Decision rule: [[gal-zellermayer-0-bugs-policy]] instructs teams to fix each new defect or close it as “won't fix.”
- Backlog mechanism: [[gal-zellermayer-0-bugs-policy]] shows a five-stage planning sequence in which feature reprioritization displaces bugs and the next sprint begins with more defects.
- Reported operation: [[gal-zellermayer-0-bugs-policy]] says the author spent about half an hour a month on bug management and never saw the same bug twice.
- Cultural claim: [[gal-zellermayer-0-bugs-policy]] reports that the policy moved developers toward higher quality standards.

## Qualifications
The profile derives from one first-person 2016 article. Its efficiency and culture claims are not independently verified, it supplies no baseline or outcome measures, and its “only way” framing exceeds the evidence presented. The article also does not address formal defect traceability, regulated or safety-critical work, or cases where immediate repair is blocked by missing evidence or dependencies.

## What Changed
- Created Zellermayer's source-bounded profile around the zero-bugs proposal.

## Relationships
- [[ZeroBugsPolicy]] - defect-management rule Zellermayer proposes.
- [[VMware]] - organizational context named in his biography and acknowledgments.
- [[AgileSoftwareDevelopment]] - Scrum and definition-of-done practices frame his argument.
- [[InternalSoftwareQuality]] - software-quality outcomes are a stated motivation for the policy.
- [[JoelSpolsky]] - “Software Inventory” is cited as an influence on the article.
