---
title: "Orphan Process"
type: concept
tags: [linux, operating-systems, process-lifecycle]
sources:
  - blog-wulc-gu-er-jin-cheng-he-jiang-shi-jin-cheng
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[OrphanProcess]] is a child process whose parent has exited while the child is still running.

## Current Synthesis
Wulc's source presents orphan processes as a normal process-lifecycle state rather than an inherent system hazard. Because parent and child processes execute asynchronously, a parent can finish before its child. In that case, the child is adopted by `init`, process ID 1, which then performs the status collection that the original parent no longer can perform.

The practical contrast is with [[ZombieProcess]]. Orphans may look unusual in a process tree, but the source says they are generally safe because the operating system has a reparenting and cleanup path through `init`.

## Key Claims
- Orphan processes arise when a parent exits before one or more children finish.
- Parent and child process lifetimes are asynchronous, so the parent cannot predict exactly when a child will terminate.
- `init` process ID 1 adopts orphan processes.
- `init` performs status collection for adopted orphan processes.
- Orphan processes are normally less dangerous than zombie processes because they have a cleanup owner.

## Evidence
- Formation and adoption: [[blog-wulc-gu-er-jin-cheng-he-jiang-shi-jin-cheng]] defines orphan processes as still-running children whose parent has exited and says `init` adopts them.
- Harmlessness qualification: [[blog-wulc-gu-er-jin-cheng-he-jiang-shi-jin-cheng]] explicitly contrasts orphans with zombies by stating that `init` continues waiting for and cleaning adopted children.

## Counterevidence & Qualifications
The source is a concise Linux-oriented teaching note. It does not discuss `systemd`, subreapers, containers, process namespaces, daemonization patterns, or cases where orphaned background work is operationally unwanted even if the kernel cleanup path is sound.

## What Changed
- Created a canonical concept for orphan processes as a process-lifecycle state distinct from orphan notes and zombie processes.

## Related Concepts
- [[ZombieProcess]] - contrasting terminated child state that remains unreaped by its parent.
- [[ConcurrentProgramming]] - asynchronous parent and child execution creates lifecycle coordination requirements.
