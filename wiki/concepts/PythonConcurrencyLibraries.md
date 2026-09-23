---
title: "Python Concurrency Libraries"
type: concept
tags: [python, concurrency, parallel-programming, distributed-systems]
sources:
  - blog-wulc-python-bing-xing-bian-cheng-gai-shu
  - yuchanns-python-web-kuang-jia-zhong-de-hou-tai-ren-wu
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[PythonConcurrencyLibraries]] are Python modules and libraries used to express concurrent, parallel, distributed, or asynchronously scheduled work.

## Current Synthesis
Wulc's article closes its conceptual overview with a short Python module map. It names `threading` as Python's built-in multithreading module, `multiprocessing` as Python's built-in multiprocessing module, Parallel Python as a third-party module for adjustable process counts and dynamic load balancing, and Celery as a distributed task queue for distributed programming. Yuchanns adds a modern web-service example built on `asyncio`: [[FastAPI]] lifespan management owns a continuously running coroutine task from startup through cancellation and shutdown.

Together, the sources show that “concurrency library” spans materially different execution and ownership models: OS threads, processes, distributed queues, and cooperative coroutine tasks. The 2016 list remains a beginner orientation rather than a current recommendation matrix, while the newer source demonstrates one narrow `asyncio` lifecycle pattern rather than surveying the modern ecosystem.

## Key Claims
- Python's standard library includes `threading` for multithreaded programming.
- Python's standard library includes `multiprocessing` for multi-process programming.
- Parallel Python is described as supporting runtime process-count adjustment and dynamic load balancing.
- Celery is described as a distributed task queue for distributed programming.
- `asyncio.create_task()` can run a cooperative in-process worker whose lifetime is owned by a web application's startup and shutdown context.
- Execution mechanism and lifecycle requirements should be matched: a service-owned coroutine is not equivalent to a durable distributed task queue.

## Evidence
- Threading evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] lists `threading` as Python's built-in multithreading module.
- Multiprocessing evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] lists `multiprocessing` as Python's built-in multiprocessing module.
- Parallel Python evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] describes Parallel Python as a third-party module with process-count adjustment and dynamic load balancing.
- Celery evidence: [[blog-wulc-python-bing-xing-bian-cheng-gai-shu]] describes Celery as a distributed task-queue module for distributed programming.
- Coroutine evidence: [[yuchanns-python-web-kuang-jia-zhong-de-hou-tai-ren-wu]] starts a continuous worker with `asyncio.create_task()` inside a FastAPI lifespan context.
- Lifecycle evidence: [[yuchanns-python-web-kuang-jia-zhong-de-hou-tai-ren-wu]] cancels and awaits the coroutine task during application shutdown.
- Scope distinction: [[yuchanns-python-web-kuang-jia-zhong-de-hou-tai-ren-wu]] distinguishes request-triggered FastAPI `BackgroundTasks` from a worker that runs for the service lifetime.

## Counterevidence & Qualifications
Wulc's source dates to 2016 and does not evaluate modern versions, thread/process tradeoffs, the GIL, or whether Parallel Python remains actively maintained. Yuchanns fills part of the `asyncio` gap, but only through one in-process web-worker example; it does not address multi-process duplication, blocking or CPU-bound work, task durability, distributed coordination, or the broader async-library ecosystem.

## What Changed
- Added `asyncio` as a cooperative-concurrency mechanism through a FastAPI service-lifecycle example.
- Distinguished lifespan-owned in-process tasks from request follow-up work and durable distributed queues.

## Related Concepts
- [[Python]] - language ecosystem in which the listed modules operate.
- [[ConcurrentProgramming]] - `threading` is the source's Python multithreading entry.
- [[ParallelProgramming]] - `multiprocessing` and Parallel Python are the source's parallel-work examples.
- [[DistributedProgramming]] - Celery is the source's distributed-programming example.
- [[InterprocessCommunication]] - Python concurrency tools need communication patterns for cooperating processes.
- [[ServiceLifetimeBackgroundTasks]] - `asyncio` pattern for workers owned by application startup and shutdown.
- [[TaskQueueDesign]] - external task infrastructure serves different durability and scheduling requirements.
