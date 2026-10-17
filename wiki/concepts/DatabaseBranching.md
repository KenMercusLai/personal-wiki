---
title: "Database Branching"
type: concept
tags: [databases, branching, copy-on-write, development-workflows]
sources:
  - p4385-pandis
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[DatabaseBranching]] creates an isolated database history from a consistent parent version, ideally by sharing unchanged storage and recording only divergent state.

## Current Synthesis
Lakebase models a branch as a new timeline containing a parent timeline ID and a branch LSN. Creation is therefore an O(1) metadata operation rather than a full database copy. Reads use the child's own layer files and recursively consult its ancestors for unchanged pages, while subsequent WAL diverges independently.

This makes database state follow code-like development and agent workflows, but the analogy to Git is limited. Transactions still active at the branch point are aborted as in crash recovery, the chosen LSN must remain reconstructible within the PITR window, deep ancestry can add read work, detachment asynchronously copies inherited data, and reconciling two writable descendants remains an application-level merge problem.

## Key Claims
- A branch can be a version reference plus copy-on-write divergence rather than a physical clone.
- LSN-addressable storage and retained history make a consistent branch point reconstructible.
- Branches isolate schema, data, migrations, tests, and agent experiments from production state.
- Recursive ancestor lookup shifts creation cost into later reads and retention.
- Detachment can remove ancestry dependence but requires eventual physical copying.
- Database branch merging is not equivalent to text merging and needs domain-aware conflict resolution.

## Evidence
Creation and consistency:
- [[p4385-pandis]] describes a child timeline created from a parent ID and branch LSN, with in-flight transactions aborted at the fork boundary.

Operational use:
- [[p4385-pandis]] reports production hierarchies including some above 500 branches and positions branching as a primitive for rapid human and agent iteration.

Read and retention costs:
- [[p4385-pandis]] shows Pageserver reads recursively searching parent layers and warns that deep hierarchies hurt performance.

Lifecycle boundary:
- [[p4385-pandis]] says detachment is immediate metadata followed by asynchronous ancestry copying, while merge is unsupported.

## Counterevidence & Qualifications
The evidence comes from one first-party system. O(1) describes branch creation, not total lifecycle cost: retained history increases storage, ancestor lookup can increase latency, detachment later copies data, and each active compute still consumes resources. The paper does not quantify branch-specific storage, read degradation by depth, merge tooling, privacy controls, or cleanup behavior across a large agent workload.

## What Changed
- Established copy-on-write database timelines as a distinct workflow primitive with explicit consistency, ancestry, detachment, and merge limits.

## Related Concepts
- [[DisaggregatedTransactionalDatabase]] - makes storage history independent of any one compute lifetime.
- [[ObjectStorageNativeDatabase]] - provides durable shared storage for copy-on-write versions.
- [[GitBranchRecovery]] - supplies the code-version analogy while differing in database merge semantics.
- [[ServerlessComputing]] - lets short-lived branch computes start and stop independently of retained state.
- [[AgenticWorkflowPatterns]] - can use isolated branches to contain state-changing experiments.
