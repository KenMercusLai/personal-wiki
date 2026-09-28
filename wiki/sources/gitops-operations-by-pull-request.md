---
title: "GitOps - Operations by Pull Request"
type: source
tags: [gitops, kubernetes, devops, operations]
date: 2026-03-04
source_file: "/mnt/ken_personal_wiki/Articles/GitOps - Operations by Pull Request.md"
---

## Summary
[[AlexisRichardson]] describes [[Weaveworks]]'s early [[GitOps]] practice: keep declarative infrastructure and application state in Git, make operational changes through reviewed pull requests and delivery pipelines, detect divergence between intended and live state, and synchronize systems back toward the repository definition. The article uses [[Kubernetes]], AWS provisioning, and Weave Flux to argue that this workflow improves discoverability, auditability, recovery, and developer ownership of operations.

## Key Claims
- [[GitOps]] makes Git the operational source of truth for declarative system state, change history, review, and audit context.
- Pull requests plus build and release pipelines replace routine direct production mutation with a reviewable change path.
- Diff tools must compare repository state with each deployed environment because the live system can diverge from the declared state through ad hoc changes or failed convergence.
- Sync tools complement drift alerts by moving actual state back toward intended state rather than merely reporting disagreement.
- [[Kubernetes]], [[Ansible]], and Terraform can participate in one version-controlled operating model even though they manage different layers.
- The reported recovery from deletion of all AWS Kubernetes clusters in under 45 minutes illustrates the value of reconstructible infrastructure, but it is a single company-reported incident rather than comparative recovery evidence.
- Optimizing for recovery and keeping operational intent discoverable can matter more than preventing every failure.

## Key Quotes
> "Our entire system state is under version control" - on the repository as the intended-state record.

> "Operational changes are made by pull request" - on the normal change-control path.

## Connections
- [[AlexisRichardson]] - author and Weaveworks executive describing the operating model.
- [[Weaveworks]] - company whose cloud service and engineering practice provide the case.
- [[WeaveFlux]] - synchronization project presented as the core of the Git-cluster delivery machinery.
- [[GitOps]] - central operations model defined by pull requests, desired state, drift detection, and convergence.
- [[Kubernetes]] - main declarative application platform managed through the workflow.
- [[DeclarativeInfrastructure]] - supplies the desired-state model that makes repository-to-runtime comparison possible.
- [[InfrastructureAsCode]] - places provisioning definitions and configuration under version control.
- [[DeploymentAutomation]] - build, release, and synchronization pipelines apply reviewed changes.
- [[ChangeSafety]] - peer review, diffs, audit history, drift alerts, and recovery reduce operational change risk.
- [[SystemReliability]] - reconstructibility and recovery time are presented as operational outcomes.
- [[Prometheus]] - records the environment-diff signal used for alerts.
- [[Ansible]] - configuration layer whose deployed state is compared with Git in the case.

## Contradictions
- The article's statement that rollback is provided through Git is valid for reversible desired-state changes but is qualified by [[ChangeSafety]]: reverting a commit cannot by itself undo database mutations, external side effects, or damaged runtime state.
- The case complements rather than resolves the wiki's Kubernetes fit-to-context tension. GitOps can make a complex platform more operable without proving that every workload needs Kubernetes.
