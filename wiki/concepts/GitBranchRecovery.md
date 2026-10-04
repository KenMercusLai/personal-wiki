---
title: "Git Branch Recovery"
type: concept
tags: [git, branch-recovery, reflog, version-control]
sources:
  - git-local-branch-shan-chu-hou-ru-he-hui-fu
last_updated: 2026-10-04
knowledge_schema: synthesis-v1
---

## Definition
[[GitBranchRecovery]] is the restoration of a deleted Git branch reference by locating the commit that the branch formerly identified and creating a new branch reference at that commit.

## Current Synthesis
Deleting a local branch removes its name, not necessarily the commit objects it reached. When the branch contained commits that were never pushed, the local reflog can retain enough history to identify the former tip: inspect `git reflog`, select the intended commit SHA, and recreate the branch with `git checkout -b <branch> <sha>`.

This is reference recovery, not recovery of uncommitted working-tree changes. It is also time-sensitive: the source establishes the basic procedure but does not define how reflog retention, object reachability, expiration, garbage collection, worktrees, or repository configuration affect the recovery window. The SHA should therefore be verified before treating the restored branch as authoritative.

## Key Claims
- A deleted branch name and the commits it referenced have distinct lifecycles.
- Reflog history can identify a deleted local branch's former tip commit.
- Creating a branch at the selected SHA restores a named reference to that history.
- The method applies to committed local history, not unsaved working-tree content.
- Recovery is conditional on the relevant reflog entry and Git objects still existing.

## Evidence
- Recovery mechanism: [[git-local-branch-shan-chu-hou-ru-he-hui-fu]] prescribes `git reflog` followed by `git checkout -b <branch> <sha>` after forced local-branch deletion.
- Scope: [[git-local-branch-shan-chu-hou-ru-he-hui-fu]] frames the problem as a branch with work not yet pushed to a remote, making the local repository the recovery source.
- Evidence boundary: [[git-local-branch-shan-chu-hou-ru-he-hui-fu]] gives no retention or garbage-collection guarantee, so indefinite recovery is not supported by the note.

## Counterevidence & Qualifications
The evidence is a seven-line practitioner procedure backed only by a linked Stack Overflow discussion; it supplies no tested Git version, repository state, failure cases, or validation steps. A reflog may contain several plausible commits, and recreating a branch at the wrong SHA can produce a misleading result. The method cannot reconstruct changes that were never committed, and it may fail after relevant reflog entries expire or unreachable objects are pruned. Remote references, other clones, worktrees, backups, and object-recovery tools are possible alternatives but are outside this source.

## What Changed
- Established deleted-branch recovery as restoration of a Git reference rather than automatic loss of committed history.
- Recorded reflog lookup and branch recreation as the source-backed minimal procedure.
- Bounded the method by commit state, SHA selection, reflog retention, and object availability.

## Related Concepts
- [[GitFlow]] - defines branch roles and release lanes; recovery repairs an accidentally removed local branch within any such topology.
- [[GitHubFlow]] - uses short-lived local branches that can require the same reference-restoration procedure.
- [[ChangeSafety]] - version-control checkpoints and verification reduce the consequence of destructive local operations.
- [[BackupAndRecovery]] - provides the broader principle that recovery depends on retained, identifiable state.
