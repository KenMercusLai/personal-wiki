---
title: "Rouan Wilsenach"
type: entity
tags: [software-engineering, continuous-integration, code-review]
sources:
  - rouan-wilsenach-ship-show-ask
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[RouanWilsenach]] is a software practitioner represented in the wiki through the [[ShipShowAsk]] branching and feedback framework.

## Current Profile
Wilsenach argues that teams should decide the integration and feedback path for each change rather than subject every contribution to one approval ritual. His framework combines delivery autonomy with visible work, asynchronous learning, and deliberate pre-merge discussion when uncertainty or risk makes it useful.

The source also treats technical and social conditions as inseparable. Automated checks, a releasable mainline, short-lived branches, and feature toggles support rapid integration; trust, shared standards, early conversation, and attention to later feedback determine whether that autonomy remains healthy.

## Key Characteristics
- Frames branching as a per-change judgment among Ship, Show, and Ask.
- Separates opportunities for feedback from mandatory permission to deliver.
- Treats early conversation as a complement to pull-request discussion.
- Connects delivery autonomy to automation, mainline safety, team trust, and shared standards.
- Presents practitioner guidance with explicit regulatory limits but no comparative outcome study.

## Evidence
- Framework: [[rouan-wilsenach-ship-show-ask]] defines direct Ship, self-merged Show, and feedback-blocked Ask paths.
- Delivery conditions: [[rouan-wilsenach-ship-show-ask]] requires short-lived branches, frequent rebasing, automated checks, feature toggles, and a releasable mainline.
- Collaboration stance: [[rouan-wilsenach-ship-show-ask]] recommends talking before implementation and continuing feedback even when review does not gate merge.
- Conditionality: [[rouan-wilsenach-ship-show-ask]] varies the balance with novelty, trust, experience, shared standards, and regulation.

## Qualifications
The profile rests on one self-authored 2021 practitioner essay. It does not provide comparative measurements of review quality, change failure rate, lead time, contributor development, or team trust, and it does not specify how the framework should be adapted for regulated or high-consequence systems.

## What Changed
- Created a source-bounded profile of Wilsenach's integration, review, and collaboration philosophy.

## Relationships
- [[ShipShowAsk]] - Wilsenach's per-change integration and feedback framework.
- [[TrunkBasedDevelopment]] - supplies the frequent-integration objective behind Ship and Show.
- [[CodeReviewPractice]] - receives Wilsenach's distinction between feedback and permission.
- [[ContinuousDelivery]] - provides the technical conditions for rapid safe integration.
- [[WorkplaceCollaboration]] - early and ongoing conversation remains part of the model.
