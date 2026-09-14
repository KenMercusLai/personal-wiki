---
title: "Zombie Process"
type: concept
tags: [linux, operating-systems, process-lifecycle, reliability]
sources:
  - blog-wulc-gu-er-jin-cheng-he-jiang-shi-jin-cheng
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ZombieProcess]] is a terminated child process whose parent has not yet called `wait` or `waitpid` to collect the child's exit status, leaving a process descriptor in the system.

## Current Synthesis
Wulc's source treats zombie processes as a resource-retention problem caused by incomplete parent-child cleanup. When a child exits, the kernel keeps enough metadata for the parent to inspect the termination: PID, exit status, CPU usage, and related information. That retained state is normal temporarily, but it becomes a zombie problem when the parent never calls `wait` or `waitpid`.

The operational risk is PID exhaustion. A single zombie is mostly evidence of a cleanup bug, but many zombies can occupy enough process numbers that the system cannot create new processes. The source's practical remediation is parent-focused: terminate the parent so the zombies become [[OrphanProcess|orphan processes]], are adopted by `init`, and can be cleaned correctly.

## Key Claims
- Zombies form after child termination when the parent fails to call `wait` or `waitpid`.
- The kernel keeps terminated-process metadata until the parent collects it.
- Retained zombie metadata includes the process ID, termination status, and CPU usage.
- Zombie processes keep PIDs occupied even though their main execution has ended.
- Large zombie populations can exhaust available PIDs and block creation of new processes.
- Killing the parent can let `init` adopt and clean the zombie child processes.

## Evidence
- Definition and cause: [[blog-wulc-gu-er-jin-cheng-he-jiang-shi-jin-cheng]] defines zombies as terminated child processes whose parents have not collected status through `wait` or `waitpid`.
- Resource harm: [[blog-wulc-gu-er-jin-cheng-he-jiang-shi-jin-cheng]] states that retained process information keeps PIDs occupied and can prevent new process creation at scale.
- Detection and cleanup: [[blog-wulc-gu-er-jin-cheng-he-jiang-shi-jin-cheng]] gives a `ps -A -o stat,ppid,pid,cmd | grep -e '^[Zz]'` command and recommends terminating the parent so `init` can reap the child.

## Counterevidence & Qualifications
The source focuses on a common Linux troubleshooting explanation. It does not discuss application-level fixes such as installing signal handlers, ensuring child reaping loops, avoiding unsafe double-fork assumptions in containers, or distinguishing a transient zombie from a persistent leak.

## What Changed
- Created a canonical concept for zombie processes as a parent-child cleanup failure and PID-exhaustion risk.

## Related Concepts
- [[OrphanProcess]] - terminating the parent can convert zombie children into orphans that `init` adopts and reaps.
- [[ConcurrencyFailureModes]] - zombie processes are not one of Wulc's named concurrency hazards, but they similarly arise from uncoordinated process lifecycle management.
- [[ConcurrentProgramming]] - parent and child processes progress asynchronously, requiring explicit cleanup coordination.
