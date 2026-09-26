---
title: "Python Web 框架中的后台任务"
type: source
tags: [python, web, async, fastapi, background-tasks]
date: 2025-04-08
source_file: /mnt/ken_personal_wiki/Articles/yuchanns - Python Web 框架中的后台任务.md
---

## Summary
Yuchanns distinguishes FastAPI's request-triggered `BackgroundTasks` facility from a continuously running worker that should start and stop with the web service. The preferred pattern uses [[FastAPI]] lifespan management and Python's `asyncio.create_task()` to run an in-process coroutine, then cancels and awaits it during shutdown. This adds a focused modern-async example to [[PythonConcurrencyLibraries]] while leaving durable queues, multi-process coordination, and crash recovery outside the article's scope.

## Key Claims
- FastAPI `BackgroundTasks` suit cleanup or follow-up work triggered by an HTTP request, not a consumer that should run for the full service lifetime.
- [[ServiceLifetimeBackgroundTasks]] can start inside an asynchronous lifespan context before the application begins serving and stop after the lifespan yield completes.
- `asyncio.create_task()` lets the worker run cooperatively beside the web server without introducing a dedicated thread or process in the shown design.
- Graceful shutdown requires cancelling the task, awaiting it, and treating `asyncio.CancelledError` as the expected termination path.
- A long-running loop should contain operational error handling and a cooperative sleep so one processing error does not terminate the worker or create a tight retry loop.
- The coroutine-and-lifespan structure can be extended to multiple in-process background tasks.

## Key Quotes
> "我需要的是服务启动就开始运行，并且持续执行的后台任务。" - the requirement that excludes request-scoped follow-up work.

> "使用 FastAPI 的 lifespan 来管理任务的生命周期" - the central lifecycle-management choice.

## Connections
- [[FastAPI]] - web framework whose request background-task facility and lifespan hook are compared.
- [[Python]] - language and runtime ecosystem used by the example.
- [[PythonConcurrencyLibraries]] - `asyncio` adds cooperative coroutine scheduling to the wiki's earlier threading, multiprocessing, and distributed-task map.
- [[ServiceLifetimeBackgroundTasks]] - pattern of binding an in-process worker to application startup and shutdown.
- [[TaskQueueDesign]] - related but distinct approach when work needs external scheduling, durable state, retries, or separate workers.
- [[SystemReliability]] - cancellation, error containment, and shutdown behavior are lifecycle reliability concerns.

## Contradictions
- The source does not directly contradict existing pages. It extends the 2016 [[PythonConcurrencyLibraries]] inventory, which explicitly lacked modern `asyncio` coverage.
- The recommendation is source-scoped: the article does not address multiple server processes, duplicate worker execution, blocking or CPU-bound work, durable delivery, process crashes, distributed coordination, or production supervision.
