---
title: "git local branch 删除后如何恢复"
type: source
tags: [git, branch-recovery, reflog, version-control]
date: 2020-04-09
source_file: "/mnt/ken_personal_wiki/Articles/git local branch 删除后如何恢复.md"
---

## Summary
[[MaiYang]] gives a minimal [[GitBranchRecovery]] procedure for a local branch deleted with `git branch -D` before its commits were pushed. The recovery path is to locate the former branch tip's commit SHA in Git's reflog, then create a new branch pointing to that commit.

## Key Claims
- Deleting a local branch name does not necessarily delete the commits it referenced immediately.
- `git reflog` can reveal the SHA of the commit formerly reached through the deleted branch.
- `git checkout -b <branch> <sha>` recreates a branch name at the recovered commit.
- Recovery depends on the relevant reflog entry and underlying Git objects still being available; the note does not promise indefinite recoverability.

## Key Quotes
> “使用 `git reflog` 查找被删除分支的 SHA，然后用该 SHA 重新创建分支。” — the source's complete recovery method

## Connections
- [[MaiYang]] - author of the concise Git recovery note.
- [[GitBranchRecovery]] - operational procedure for finding the former tip and restoring a branch reference.
- [[GitFlow]] - related branch-management model; reflog recovery repairs a lost local reference rather than choosing a branching policy.
- [[GitHubFlow]] - related lightweight branching model whose local branches can require the same recovery technique.

## Contradictions
- No direct contradiction found. The note complements the wiki's branching-strategy pages by addressing accidental local-reference deletion rather than branch topology.
- The procedure is intentionally minimal: it does not discuss reflog expiration, garbage collection, worktrees, remote-tracking branches, uncommitted changes, multiple candidate SHAs, or the newer `git switch -c` interface.
