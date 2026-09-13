---
title: "Monorepo Dependency Convergence"
type: concept
tags: [software-architecture, monorepo, dependencies]
sources:
  - alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[MonorepoDependencyConvergence]] is the practice of bringing related code into one repository and standardizing shared dependency versions so changes can be tested and maintained consistently.

## Current Synthesis
The source shows dependency convergence as one of the hidden benefits of moving from many destination repos to one destination repo. Separate repos gave local test isolation, but they also let shared-library versions drift until common functionality stopped being common. The monorepo migration forced 120 unique dependencies onto one version each, exposing breakage during migration rather than letting every destination evolve separately.

The useful distinction is that a monorepo is not valuable merely because files share a directory. It becomes valuable when it changes the maintenance economics of shared code: one dependency version, one combined test suite, and one deployment path make bulk updates less risky and less tedious.

## Key Claims
- Separate repos can hide shared-library drift until common maintenance becomes expensive.
- A monorepo can make dependency versions explicit and uniform across related components.
- Converging dependencies front-loads breakage during migration but reduces long-term version-tracking complexity.
- A combined test suite is necessary for dependency convergence to remain safe.
- Repository structure should match how often code, tests, dependencies, and releases need to change together.

## Evidence
- Drift problem: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says destination repos ended up using different shared-library versions.
- Dependency count: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says the team standardized 120 unique dependencies.
- Breakage handling: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says destinations were fixed when newer dependency versions broke them.
- Test suite need: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says running all destination tests was a blocker for shared-library updates.
- Deployment improvement: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says one engineer could deploy the consolidated service in minutes.

## Counterevidence & Qualifications
The source also names a real cost: updating a dependency in one repo can require updating multiple destinations at once. Convergence reduces hidden divergence but increases the immediate blast radius of dependency changes.

## What Changed
- Created the concept from Segment's move from many destination repos into one repo.

## Related Concepts
- [[MonolithConsolidation]] - the monorepo supported the single destination service.
- [[MicroserviceOperationalOverhead]] - dependency drift was one form of overhead in the microservice architecture.
- [[RecordedTrafficTesting]] - a fast combined test suite made convergence practical.
- [[SoftwareVerification]] - dependency convergence depends on tests catching cross-destination breakage.
