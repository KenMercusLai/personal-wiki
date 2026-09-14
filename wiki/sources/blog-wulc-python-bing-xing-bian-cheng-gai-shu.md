---
title: "python 并行编程概述"
type: source
tags: [python, concurrency, parallel-programming, distributed-systems]
date: 2016-05-29
source_file: /mnt/ken_personal_wiki/Articles/Blog - wulc - python 并行编程概述.md
---

## Summary
[[Wulc]] gives an introductory map of [[ConcurrentProgramming]], [[ParallelProgramming]], and [[DistributedProgramming]] before explaining how parallelized programs communicate and fail. The article distinguishes shared-state communication from [[MessagePassing]], then introduces [[Deadlock]], [[Starvation]], and [[RaceCondition]] as common hazards. The inspected diagrams reinforce the source's teaching model by showing a scheduler and process queue for concurrency, multiple CPUs for true parallelism, networked nodes for distributed work, a circular wait graph, and two account-balance sequences where unsynchronized interleaving corrupts state.

## Key Claims
- [[ConcurrentProgramming]] resembles pseudo-parallel execution: a scheduler lets different processes access one CPU at different moments.
- [[ParallelProgramming]] depends on a multi-core environment where several processes can run at the same time on separate cores.
- [[DistributedProgramming]] spreads one task across physically separated machines and communicates through a network.
- [[InterprocessCommunication]] is usually framed as either shared state or [[MessagePassing]], with message passing trading memory copies for stronger data consistency and distributed applicability.
- [[ConcurrencyFailureModes]] include [[Deadlock]], [[Starvation]], and [[RaceCondition]], all of which emerge from resource dependence, scheduling, or unsynchronized state updates.
- [[PythonConcurrencyLibraries]] include standard-library threading and multiprocessing plus third-party options such as Parallel Python and Celery for parallel or distributed work.

## Key Quotes
> "任一时刻只有一个进程占用 CPU" - on concurrent programming as scheduled pseudo-parallel execution.

> "同一时间每个核都可以允许一个进程运行" - on multi-core parallel programming.

> "数据的一致性大大增强" - on the main advantage of message passing.

## Connections
- [[Wulc]] - author of the source.
- [[Python]] - programming language context for the listed threading, multiprocessing, Parallel Python, and Celery modules.
- [[ConcurrentProgramming]] - scheduler-mediated model shown in the first diagram.
- [[ParallelProgramming]] - multi-core execution model shown in the second diagram.
- [[DistributedProgramming]] - networked-node model shown in the third diagram.
- [[InterprocessCommunication]] - shared state and message passing are the source's two communication models.
- [[MessagePassing]] - communication model favored by the article for consistency and distributed applicability.
- [[ConcurrencyFailureModes]] - umbrella for the source's deadlock, starvation, and race-condition section.
- [[Deadlock]] - circular resource wait shown by the A, B, C dependency diagram.
- [[Starvation]] - process unable to continue because needed resources or CPU time never arrive.
- [[RaceCondition]] - account-balance examples show incorrect results when operations interleave without synchronization.
- [[PythonConcurrencyLibraries]] - source's list of Python modules and third-party libraries for concurrent, parallel, and distributed programming.

## Contradictions
- No direct contradictions found. The article is a 2016 beginner overview, so its Python module list and examples should be treated as introductory rather than a current library recommendation.
