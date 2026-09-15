---
title: "How to go fast"
type: source
tags: [software-development, agile, continuous-delivery]
date: 2019-03-02
source_file: /mnt/ken_personal_wiki/Articles/Chris James - How to go fast.md
---

## Summary
[[ChrisJames]] argues that software teams can move quickly without burnout by keeping scope small, deploying from the first "hello world," and using real user and business feedback rather than large upfront plans. The article connects [[AgileSoftwareDevelopment]], [[ContinuousDelivery]], and [[InternalSoftwareQuality]]: sustainable speed comes from small trusted teams, low WIP, tests, continuous refactoring, simple architectures, and short feedback loops.

## Key Claims
- Teams should align on the user, problem, non-goals, validation signals, and cancellation criteria before they argue about architecture or backlog size.
- [[ContinuousDelivery]] should begin with the first deployed "hello world" so every green main-branch build can reach production, run smoke tests, and collect feedback.
- Speed is sustainable only when teams protect quality and mental health through small batches, low WIP, automated tests, continuous refactoring, support ownership, and 10-20% learning time.
- Small co-located teams, pairing, direct stakeholder access, and user observation reduce communication friction and waste.
- For a small trusted pairing team, branches and pull requests can add review ceremony that weakens tight feedback loops; the source treats fast repair and shared responsibility as the preferred control.
- Monoliths, progressive enhancement, mature tools, simple build setup, and minimal deployment environments are preferred until real evidence justifies extra complexity.
- User stories should start conversations about user problems and success measures rather than prescribe implementation decisions.

## Key Quotes
> "Start with hello world, fully deployed with continuous delivery." - on establishing the release loop before feature buildout.

> "User stories should describe a user problem" - on keeping requirements conversational rather than prescriptive.

## Connections
- [[ChrisJames]] - author of the article.
- [[AgileSoftwareDevelopment]] - the article's operating model centers on user problems, frequent working-software feedback, small teams, collaboration, and adaptation.
- [[ContinuousDelivery]] - the article recommends automatic deployment to live on green builds with tests and smoke tests.
- [[InternalSoftwareQuality]] - tests, refactoring, simple design, and support ownership are presented as speed enablers.
- [[CodeReviewPractice]] - the article qualifies pull-request review for small trusted pairing teams.
- [[DistributedSystemRestraint]] - the monolith-over-microservices recommendation argues against premature distributed-system complexity.
- [[ProductFlowFriction]] - progressive enhancement and 80% shipping reduce implementation and feedback friction for users and teams.

## Contradictions
- Partly qualifies [[CodeReviewPractice]]: code review remains useful for shared learning and risk control elsewhere in the wiki, but this source argues that small trusted pairing teams may be faster without pull-request gates.
