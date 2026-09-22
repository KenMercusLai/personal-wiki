---
title: "You Can't Have a Rollback Button"
type: source
tags: [deployment, devops, reliability, release-engineering]
date: 2017-02-28
source_file: "/mnt/ken_personal_wiki/Articles/You Can’t Have a Rollback Button - Skyliner.md"
---

## Summary
[[DanMcKinley]] argues that a running web application has a current distributed state rather than a self-contained version that can be restored with one safe rollback. Reverting server code does not reverse changes already made to databases, caches, browsers, or concurrently running instances, so [[ChangeSafety]] should favor small, staged, disableable changes and verifiable forward remediation over confidence in a universal rollback button.

## Key Claims
- A web application does not have an independently reversible version once its code has interacted with external state, clients, and other running copies.
- Reverting a deployed commit restores only some code; it does not automatically repair corrupted caches, mutated databases, incompatible clients, or effects produced during mixed-version operation.
- A transition from v1 to v2 and back to v1 can itself be destructive, so the label "rollback" should not be treated as proof that the resulting state is safe.
- Confidence in a panic-button rollback can encourage larger or riskier releases by making recovery appear easier than it is.
- [[ContinuousDelivery]] is safer when teams deploy dark code behind disabled feature flags, ramp exposure gradually, maintain feature off switches, and make small forward corrections.
- A full deployment rollback can remain a last-resort maneuver, but nontrivial state interactions make its consequences difficult to reason about.

## Key Quotes
> "The rollback button is a lie." - the article's central rejection of rollback as a generally safe operation for a running system.

> "The remediation has to occur in the direction of the future." - on repairing the system's current state rather than pretending its prior state still exists.

## Connections
- [[DanMcKinley]] - author presenting rollback skepticism as practical deployment guidance.
- [[ChangeSafety]] - safe recovery must account for persistent state and mixed-version interactions, not only server-code revision.
- [[DeploymentAutomation]] - a rollback control can automate code reversion without making the whole system reversible.
- [[ContinuousDelivery]] - dark launches, gradual ramp-up, off switches, and small forward corrections reduce release blast radius.
- [[HarnessEngineering]] - feature flags and off switches are controls that bound activation and provide a narrower recovery path.

## Contradictions
- Contradicts [[ChangeSafety]] where its earlier synthesis calls rollback "often the most useful response" without making the boundary between code reversion and whole-system restoration sufficiently explicit.
- Qualifies [[DeploymentAutomation]] examples that describe redeploying an earlier commit as rollback: the mechanism may restore code while leaving data, caches, browsers, and concurrent processes in a state the old code cannot safely handle.
