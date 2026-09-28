---
title: "GitHub Flow"
type: concept
tags: [git, branching, continuous-delivery, release-management]
sources:
  - git-flow-yu-github-flow-fen-zhi-ce-lve
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[GitHubFlow]] is a lightweight Git branching model built around one release-ready main branch and short-lived branches whose feature or fix changes merge back frequently.

## Current Synthesis
GitHub Flow collapses the stable-release and integration roles into one main branch. Developers perform work on separate branches, whether the change is a one-line fix or a large feature, and merge completed work into main. Because main is assumed to remain releasable and integration happens frequently, the workflow does not require dedicated release or hotfix branch types; fixes follow the same path as other changes.

The simplicity is conditional rather than free. A release-ready main branch requires teams to keep accepted changes safe through practices outside branch topology, such as review, automated tests, staged deployment, feature flags, monitoring, or rapid repair. If integration becomes infrequent or main cannot be released safely, the model's central assumption no longer holds.

## Key Claims
- One main branch represents the release-ready product state.
- Feature and fix work occurs on separate branches and merges back when complete.
- Frequent integration reduces the need for a dedicated release-stabilization branch.
- Bug fixes can follow the same branch-and-merge path as features rather than a special hotfix lane.
- The model's reduced branch structure depends on keeping main genuinely releasable.

## Evidence
- Release-ready main: [[git-flow-yu-github-flow-fen-zhi-ce-lve]] contrasts GitHub Flow's one releasable main branch with Git-flow's separate development and stable-release lines.
- Frequent integration: [[git-flow-yu-github-flow-fen-zhi-ce-lve]] says main receives other branches at a relatively high frequency.
- Unified change path: [[git-flow-yu-github-flow-fen-zhi-ce-lve]] describes feature branches ranging from one-line changes to substantial updates and says completed work ultimately merges into `master`.
- Structural simplification: [[git-flow-yu-github-flow-fen-zhi-ce-lve]] argues that frequent merging removes the need for distinct release and hotfix branch categories.

## Counterevidence & Qualifications
The source explains the model's logic but gives no evidence that adopting it causes faster or safer delivery. A branch named main can still be unreleasable, and frequent merges can spread defects quickly without adequate verification, compatibility, rollout, and recovery practices. The saved note also predates or omits common implementation details such as pull requests, required checks, merge queues, trunk-based variants, feature flags, and environment-specific release approvals.

## What Changed
- Established GitHub Flow as a release-ready-main branching model.
- Made the removal of separate release and hotfix lanes conditional on frequent safe integration.
- Distinguished a simple branch topology from the engineering controls needed to sustain it.

## Related Concepts
- [[GitFlow]] - uses separate development, release, stable, and hotfix lanes for more explicit version management.
- [[ContinuousDelivery]] - provides the frequent, reliable release capability presupposed by a release-ready main branch.
- [[ChangeSafety]] - limits the risk of integrating and releasing changes frequently.
- [[DeploymentAutomation]] - turns merged revisions into repeatable deployment and verification steps.
