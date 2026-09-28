---
title: "Git-flow"
type: concept
tags: [git, branching, release-management, versioning]
sources:
  - git-flow-yu-github-flow-fen-zhi-ce-lve
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[GitFlow]] is a Git branching model that separates ongoing integration, feature development, release stabilization, stable production history, and emergency repair across `develop`, `feature`, `release`, `master`, and `hotfix` branches.

## Current Synthesis
The model treats `develop` as the main line for upcoming work. Feature branches diverge from it and merge back when complete. A release branch then creates a bounded stabilization phase in which the version should receive bug fixes rather than new features; once considered stable, it enters `master`. Urgent production problems can be repaired through a hotfix branch.

This structure makes release state and parallel maintenance work explicit, which can be useful when a product must support multiple versions. Its cost is additional branch roles, merge paths, and coordination. The model does not by itself specify how long feature branches live or guarantee that `develop` stays healthy, and its existence of a separate stabilization lane means `develop` is not assumed to be continuously release-ready.

## Key Claims
- `develop` integrates work intended for a future release while `master` records stable releases.
- Feature branches isolate new work before it rejoins the development line.
- Release branches separate stabilization and bug fixing from continued feature development.
- Hotfix branches provide an explicit path for urgent repair of a stable production version.
- The model can support simultaneous maintenance of multiple versions.
- Explicit branch roles trade structural clarity for merge and coordination complexity.

## Evidence
- Branch roles: [[git-flow-yu-github-flow-fen-zhi-ce-lve]] describes `develop` as the development main line, feature branches as its derivatives, and `master` as the stable-release line.
- Stabilization boundary: [[git-flow-yu-github-flow-fen-zhi-ce-lve]] says a release branch is a preparation stage in which work normally narrows to bug fixing before promotion to `master`.
- Production repair: [[git-flow-yu-github-flow-fen-zhi-ce-lve]] assigns urgent fixes for the stable version to hotfix branches.
- Operating fit: [[git-flow-yu-github-flow-fen-zhi-ce-lve]] attributes Git-flow's strongest fit to maintaining multiple versions concurrently.
- Governance gap: [[git-flow-yu-github-flow-fen-zhi-ce-lve]] notes that the model neither fixes feature-merge frequency nor defines the required health of `develop`.

## Counterevidence & Qualifications
The evidence is one concise practitioner comparison rather than measured analysis of delivery speed, quality, recovery, or merge cost. Git-flow's named branches do not provide testing, review, observability, security, or deployment controls, and teams may adapt branch names and merge rules. Products with one continuously deployable version may find its release and hotfix lanes unnecessary, while regulated or coordinated releases may still require controls beyond the model.

## What Changed
- Established Git-flow as a version- and release-oriented branching model.
- Made its parallel-version advantage and coordination cost explicit.
- Distinguished branch topology from development-branch health and delivery assurance.

## Related Concepts
- [[GitHubFlow]] - simplifies the branch model around one continuously release-ready main branch.
- [[ContinuousDelivery]] - reduces the need for a separate stabilization lane when every accepted change remains releasable.
- [[ChangeSafety]] - supplies verification and rollout controls that branch roles alone cannot provide.
- [[DeploymentAutomation]] - moves tested revisions into environments independently of how branches are named.
