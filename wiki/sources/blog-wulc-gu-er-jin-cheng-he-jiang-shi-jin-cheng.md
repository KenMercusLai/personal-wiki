---
title: "孤儿进程和僵尸进程"
type: source
tags: [linux, operating-systems, process-lifecycle]
date: 2015-12-05
source_file: /mnt/ken_personal_wiki/Articles/Blog - wulc - 孤儿进程和僵尸进程.md
---

## Summary
[[Wulc]] explains two special child-process states in Unix-like process management: [[OrphanProcess]] and [[ZombieProcess]]. The source argues that orphan processes are normally harmless because `init` adopts and reaps them, while zombie processes can consume process IDs if a parent never calls `wait` or `waitpid` to collect the child's termination status.

## Key Claims
- A child process becomes an [[OrphanProcess]] when its parent exits while the child is still running.
- Orphan processes are adopted by `init` process ID 1, which performs the needed status collection.
- A child becomes a [[ZombieProcess]] after termination when its parent has not called `wait` or `waitpid` to collect its status.
- Kernels retain terminated-process metadata such as PID, exit status, and CPU time until the parent reaps the child.
- Large numbers of zombie processes can exhaust available PIDs and prevent new process creation.
- A practical cleanup path is to terminate the zombie process's parent, causing the zombie child to be adopted and reaped by `init`.

## Key Quotes
> "当父进程退出，而它的一个或多个子进程还在运行时，这些子进程就成为孤儿进程。" - on orphan-process formation.

> "大量的僵尸进程会耗尽可用的进程号，导致系统无法创建新的进程。" - on the operational harm of zombie processes.

## Connections
- [[Wulc]] - author of the technical note.
- [[OrphanProcess]] - central harmless child-process state explained by the source.
- [[ZombieProcess]] - central hazardous child-process state explained by the source.
- [[ConcurrentProgramming]] - related broader context because asynchronous parent and child execution creates lifecycle states that must be coordinated.

## Contradictions
- No direct contradictions found. The source complements the existing Wulc concurrency overview by adding process-lifecycle cleanup rather than another concurrency failure mode.
