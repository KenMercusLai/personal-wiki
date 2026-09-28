---
title: "GitOps"
type: concept
tags: [operations, git, declarative-infrastructure, deployment]
sources:
  - gitops-operations-by-pull-request
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[GitOps]] is an operating model in which version-controlled declarative definitions record intended system state, reviewed pull requests change that intent, and automated comparison plus synchronization expose and correct divergence in running environments.

## Current Synthesis
The Weaveworks case combines familiar engineering controls into one operational loop. Git provides history, review, and a discoverable account of intent; declarative tools make intended state machine-readable; delivery automation applies approved changes; diff tools compare each environment with the repository; and synchronization tools drive convergence. The repository is therefore the authoritative intent record, while the live system remains the observable actual state that must be continuously checked.

The model improves recovery only to the extent that infrastructure and application state are reconstructible. The reported full-cluster rebuild shows the potential of versioned definitions, but Git rollback is not a universal undo mechanism for data loss or external side effects.

## Key Claims
- GitOps joins version control, peer review, delivery automation, drift detection, and reconciliation into a closed operational loop.
- Pull requests create a reviewable normal path for changes and preserve why system intent changed.
- Desired state in Git and actual state in production are distinct; continuous comparison is required to reveal drift or failed convergence.
- Alerts make divergence visible, while sync mechanisms act to restore the declared state.
- Reconstructible definitions can shorten disaster recovery, but recovery still depends on external data, credentials, artifacts, and provider services.
- Direct runtime changes create ambiguity unless they are deliberately reconciled back into the authoritative definition.

## Evidence
- Source-of-truth loop: [[gitops-operations-by-pull-request]] says Weaveworks kept system configuration in one repository and made operational changes through pull requests and pipelines.
- Drift control: [[gitops-operations-by-pull-request]] describes kubediff, ansiblediff, and terradiff comparing Git with development and production environments and emitting an alert when a difference persisted.
- Convergence: [[gitops-operations-by-pull-request]] presents Weave Flux as Git-cluster synchronization machinery alongside the diff tools.
- Operational context: [[gitops-operations-by-pull-request]] says reviews, configuration comments, issue links, commits, and product stories make implementation and intent easier to discover.
- Recovery case: [[gitops-operations-by-pull-request]] reports rebuilding multiple AWS services, Kubernetes clusters, applications, and observability after a destructive incident in under 45 minutes.

## Counterevidence & Qualifications
The source is a 2017-era practitioner account from a company also promoting its GitOps product and open-source tooling. It does not compare incident rates, lead time, recovery time, or operating cost against other models. A repository records intended state, not necessarily all runtime data or third-party side effects; synchronization can also faithfully propagate a bad declaration. Emergency intervention, secrets, stateful data, and changes made outside the managed resource boundary need separate controls and reconciliation paths.

## What Changed
- Established GitOps as a closed loop of reviewed intent, automated application, drift detection, and convergence rather than a synonym for storing YAML in Git.
- Distinguished the repository's authoritative intent from the live system's observable actual state.
- Qualified Git-based rollback and recovery at stateful and external-effect boundaries.

## Related Concepts
- [[DeclarativeInfrastructure]] - makes intended state explicit enough to compare and reconcile with runtime state.
- [[InfrastructureAsCode]] - supplies versioned provisioning and configuration definitions used by GitOps workflows.
- [[DeploymentAutomation]] - applies reviewed repository changes to target environments.
- [[ChangeSafety]] - GitOps contributes review, traceability, drift alerts, and restoration paths to operational change control.
- [[SystemReliability]] - reconstructibility and convergence affect recovery time and service resilience.
- [[Kubernetes]] - primary declarative runtime in the Weaveworks case.
