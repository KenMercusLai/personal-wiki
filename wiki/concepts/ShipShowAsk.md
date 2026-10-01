---
title: "Ship / Show / Ask"
type: concept
tags: [software-engineering, branching, pull-requests, continuous-integration]
sources:
  - rouan-wilsenach-ship-show-ask
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[ShipShowAsk]] is a per-change framework for choosing direct mainline integration, non-blocking pull-request visibility, or pre-merge discussion according to uncertainty, risk, learning value, and team context.

## Current Synthesis
The framework separates three concerns often collapsed into one pull-request rule: integrating work, making work visible, and asking for permission or help. Ship integrates an established, low-surprise change directly. Show uses a short-lived pull request and automated checks but lets the author merge without waiting, preserving a space for asynchronous feedback and team learning. Ask waits because discussion may materially change the approach.

This flexibility is conditional on a strong delivery system. Mainline must remain releasable; branches must stay short-lived and current; automated verification and feature toggles must constrain risk; and authors must continue engaging with feedback after a Show merge. The choice should move toward Show or Ask as novelty, uncertainty, coordination needs, or consequence increase, while regulation may impose approval independently of the framework.

The model does not make pull requests the whole conversation. Direction should be discussed before substantial implementation when alternative approaches are still cheap, and teams need a feedback culture even for directly shipped work. Its core contribution is therefore not a new branch topology but a vocabulary for matching feedback timing and merge authority to each change.

## Key Claims
- Integration, visibility, and permission are separate decisions rather than one mandatory pull-request bundle.
- Ship fits routine changes made through established patterns when mainline safety controls are strong.
- Show preserves rapid integration while exposing interesting work for non-blocking feedback and learning.
- Ask fits uncertainty, experiments, consequential changes, or work that needs help before merge.
- The mix should vary with risk, novelty, trust, shared standards, contributor context, and regulatory obligations.
- Early conversation remains necessary because review after implementation can anchor discussion to sunk work.

## Evidence
- Three paths: [[rouan-wilsenach-ship-show-ask]] defines Ship as direct integration, Show as self-merged pull-request visibility, and Ask as waiting for feedback.
- Flow conditions: [[rouan-wilsenach-ship-show-ask]] requires automated checks, a releasable mainline, feature toggles, short-lived branches, and frequent rebasing.
- Queue pressure: [[rouan-wilsenach-ship-show-ask]] argues that universal approval can either slow progress or degrade feedback when review demand exceeds capacity.
- Contextual balance: [[rouan-wilsenach-ship-show-ask]] links more Shipping to established patterns and shared standards, and more Showing or Asking to novelty, lower familiarity, and greater need for conversation.
- Conversation timing: [[rouan-wilsenach-ship-show-ask]] warns that late pull-request review can anchor reviewers to an already-implemented solution.

## Counterevidence & Qualifications
The evidence is one practitioner's team experience rather than a controlled comparison. Self-merge can miss defects, security concerns, knowledge gaps, or architectural drift when automated checks and conversation are weak. Post-merge feedback may arrive too late to prevent harm or may be ignored, while job seniority alone is a poor proxy for risk. Regulated, safety-critical, security-sensitive, or hard-to-reverse changes may require independent approval and stronger evidence even when the implementation looks routine.

## What Changed
- Established Ship / Show / Ask as a framework that separates integration, visibility, and permission.
- Made technical safety, feedback culture, and contextual risk explicit adoption conditions.
- Preserved regulation and high-consequence change as limits on author-controlled merge.

## Related Concepts
- [[TrunkBasedDevelopment]] - Ship and rapid Show merges preserve frequent mainline integration.
- [[CodeReviewPractice]] - Show makes review advisory while Ask makes it pre-merge and decision-shaping.
- [[PRReviewHygiene]] - selective blocking and short-lived changes protect scarce reviewer attention.
- [[ContinuousDelivery]] - automated checks and a releasable mainline make low-delay integration feasible.
- [[GitHubFlow]] - Ship / Show / Ask varies whether a branch and approval wait are needed per change.
- [[WorkplaceCollaboration]] - early conversation and later feedback remain necessary across all three paths.
