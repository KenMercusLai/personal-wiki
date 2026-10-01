---
title: "Trunk-Based Development"
type: concept
tags: [software-engineering, continuous-delivery, branching]
sources:
  - architecting-for-continuous-delivery-thoughtworks
  - nick-craver-stack-overflow-how-we-do-deployment-2016-edition
  - rouan-wilsenach-ship-show-ask
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[TrunkBasedDevelopment]] is a development practice where teams integrate small changes frequently on a shared mainline so continuous integration and delivery pipelines can validate current product state quickly.

## Current Synthesis
The Thoughtworks source mentions trunk-based development as a practice that deployment pipelines can support. In context, the connection is release-flow visibility: when each commit moves through staged validation toward production, long-lived hidden work becomes less compatible with the feedback model.

The Thoughtworks source does not explain trunk-based development in detail, but it places it inside the continuous-delivery system: small frequent integration, automated tests, and deployment-pipeline confidence reinforce one another.

Stack Overflow's 2016 account supplies a bounded team example. Roughly 15 contributors usually committed directly to `master`; branches were used for early review of new developers, large or risky features, and multi-person work. Merges were usually squashed so the code change remained easier to revert, while impractical squashes were not treated as dogma. The team connected this short-lived integration model to small and medium changes, a short build queue, and frequent deployment, but Craver explicitly declined to recommend it universally.

Ship / Show / Ask adds a per-change decision layer without changing the frequent-integration goal. Routine work can go directly to mainline; interesting work can use a self-merged pull request for visibility; uncertain work can wait for feedback. This flexibility still depends on short-lived branches, automated checks, feature toggles, a releasable mainline, and a feedback culture that does not disappear when review is non-blocking.

## Key Claims
- Trunk-based development fits continuous delivery because it keeps integration frequent and visible.
- Deployment pipelines can support trunk-based development by validating each revision through staged checks.
- The practice depends on automated feedback that makes small changes cheaper to verify.
- Short-lived branches can still serve review and coordination when change size, risk, or contributor experience warrants them.
- Mainline integration is an operating choice whose fit depends on team, review, and deployment conditions rather than a universal rule.
- Branch and review policy can vary per change when risk, uncertainty, visibility, and learning needs differ.

## Evidence
- Pipeline fit: [[architecting-for-continuous-delivery-thoughtworks]] says deployment pipelines can support best practices such as trunk-based development.
- Integration context: [[architecting-for-continuous-delivery-thoughtworks]] says a team is not really practicing CI if it lacks small frequent check-ins or automated tests.
- Team practice: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] says Stack Overflow usually pushed to `master`, with branches reserved for bounded review and coordination cases.
- Release context: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] links small frequent commits to avoiding a large queue and reports multiple production deployments on a typical day.
- Per-change integration: [[rouan-wilsenach-ship-show-ask]] distinguishes direct Ship, self-merged Show, and feedback-blocked Ask while requiring short-lived branches and a releasable mainline.

## Counterevidence & Qualifications
Thoughtworks only mentions trunk-based development briefly, while Stack Overflow and Ship / Show / Ask supply practitioner implementations without comparative defect, review, or delivery data. Direct mainline commits and self-merged pull requests can shorten integration delay but can also weaken pre-merge review or increase shared-mainline risk when tests, review habits, observability, recovery, or post-merge attention are weak. Regulated and high-consequence systems may require independent approval regardless of branch lifetime.

## What Changed
- Created the concept from Thoughtworks' pipeline and CI context.
- Added Stack Overflow's rare-branch, frequent-mainline operating example and its explicit non-universality.
- Added per-change Ship, Show, and Ask paths while preserving automation, mainline safety, and risk qualifications.

## Related Concepts
- [[ContinuousDelivery]] - trunk-based development is one practice that supports frequent reliable release.
- [[DeploymentPipeline]] - the pipeline validates mainline revisions through staged checks.
- [[DeploymentAutomation]] - automated deployment gives integrated changes a path toward production.
- [[SoftwareVerification]] - small frequent integration depends on fast automated validation.
- [[ForwardOnlyDatabaseMigration]] - schema work on mainline still needs cross-version compatibility.
- [[RollingDeployment]] - frequent integration reaches users through bounded fleet updates.
- [[ShipShowAsk]] - selects direct integration, non-blocking visibility, or pre-merge discussion for each change.
