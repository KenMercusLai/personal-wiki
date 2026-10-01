---
title: "Ship / Show / Ask"
type: source
tags: [software-engineering, branching, pull-requests, continuous-integration]
date: 2021-09-08
source_file: "/mnt/ken_personal_wiki/Articles/Rouan Wilsenach - Ship Show Ask.md"
---

## Summary
[[RouanWilsenach]] presents [[ShipShowAsk]] as a per-change choice among direct mainline integration, self-merged pull requests that invite later feedback, and pull requests that wait for discussion. The framework tries to preserve continuous integration while using pull requests selectively for visibility, learning, uncertainty, and risk rather than making approval a universal gate.

## Key Claims
- **Ship** means committing an established, low-surprise change directly to mainline without waiting for review.
- **Show** means opening a pull request, waiting for automated checks, merging it oneself, and leaving the change visible for asynchronous feedback and learning.
- **Ask** means pausing before merge when the approach is uncertain, help is needed, or discussion should affect the decision.
- The model depends on short-lived branches, frequent rebasing, a releasable mainline, and continuous-integration and delivery controls such as automated checks and feature toggles.
- Team trust, shared quality standards, novelty, contributor experience, and change risk should influence the mix rather than job title or one fixed branching policy.
- Pull requests cannot replace early conversation: discussing direction before implementation can avoid anchoring reviewers to an already-built solution and reduce rework.
- Mandatory approval queues can reduce delivery speed or review quality at scale, but regulation may still require review or approval for every change.

## Key Quotes
> "Every time you make a change, you choose one of three options: Ship, Show or Ask." - the framework's decision rule.

> "Talk to your team before you start" - on avoiding late, solution-anchored review.

## Connections
- [[RouanWilsenach]] - author describing the framework from team practice.
- [[ShipShowAsk]] - central branching and feedback framework.
- [[TrunkBasedDevelopment]] - Ship and rapid self-merge preserve frequent mainline integration.
- [[CodeReviewPractice]] - Show separates feedback from permission, while Ask retains pre-merge discussion for uncertainty and risk.
- [[ContinuousDelivery]] - a releasable mainline, automated checks, and feature toggles make low-delay integration credible.
- [[PRReviewHygiene]] - short-lived changes and selective review protect attention and reduce stale approval queues.
- [[WorkplaceCollaboration]] - early conversation and post-merge feedback remain necessary whether or not a pull request blocks delivery.

## Contradictions
- Qualifies universal approval policies in [[CodeReviewPractice]] by treating mandatory pre-merge review as situational rather than the default for every change.
- Qualifies branch-only [[GitHubFlow]] descriptions by allowing both direct mainline commits and self-merged pull requests within one team.
- The source explicitly leaves regulated review implementation unresolved and provides practitioner experience rather than comparative defect, throughput, or trust measurements.
