---
title: "Service-Lifetime Background Tasks"
type: concept
tags: [python, async, web-services, lifecycle]
sources:
  - yuchanns-python-web-kuang-jia-zhong-de-hou-tai-ren-wu
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[ServiceLifetimeBackgroundTasks]] are in-process workers whose lifetime is deliberately bound to a service's startup and shutdown rather than to an individual request.

## Current Synthesis
The source separates two meanings often hidden by the phrase “background task.” Request-scoped follow-up work begins because a request handler schedules it, whereas a service-lifetime worker should start with the application and continue consuming or polling until the service stops. In the shown [[FastAPI]] pattern, an asynchronous lifespan context owns that worker: `asyncio.create_task()` starts it, the lifespan `yield` marks normal service operation, and shutdown cancels and awaits the task.

This is a lightweight cooperative-concurrency pattern, not a substitute for every job system. It fits asynchronous work that can safely share one web process and tolerate that process's lifetime. Requirements such as durable delivery, independent scaling, cross-process singleton execution, CPU isolation, or recovery after process failure point toward a supervised external worker or [[TaskQueueDesign]] instead.

## Key Claims
- Background work should be classified by ownership and lifetime before an execution mechanism is chosen.
- A service-lifetime worker needs an explicit startup owner and a matching shutdown path.
- Cooperative coroutine tasks can avoid thread or process overhead for suitable asynchronous I/O work.
- Cancellation should be requested, awaited, and handled as an expected control path.
- Worker loops need error containment and paced retries so transient failures do not kill the worker or cause a hot loop.
- In-process simplicity trades away durability, independent scaling, and automatic cross-process coordination unless additional mechanisms are added.

## Evidence
- Lifetime distinction: [[yuchanns-python-web-kuang-jia-zhong-de-hou-tai-ren-wu]] rejects FastAPI request `BackgroundTasks` for a consumer that must start with the service and keep running.
- Startup ownership: [[yuchanns-python-web-kuang-jia-zhong-de-hou-tai-ren-wu]] creates the worker task before the lifespan context yields.
- Shutdown ownership: [[yuchanns-python-web-kuang-jia-zhong-de-hou-tai-ren-wu]] cancels and awaits the task after the lifespan context resumes.
- Fault containment: [[yuchanns-python-web-kuang-jia-zhong-de-hou-tai-ren-wu]] catches processing exceptions inside the loop and logs them before sleeping.
- Cooperative execution: [[yuchanns-python-web-kuang-jia-zhong-de-hou-tai-ren-wu]] uses `asyncio.create_task()` and `await asyncio.sleep()` rather than the earlier thread-based Twisted attempt.

## Counterevidence & Qualifications
The article demonstrates structure rather than production behavior. It does not address whether every ASGI worker would start a duplicate task, how reloaders affect execution, whether `process_messages()` contains blocking or CPU-heavy work, how cancelled child operations release resources, or how unfinished work survives crashes. Its comparison with Twisted reflects the author's development experience rather than a systematic framework benchmark. External queues or separately supervised workers remain preferable when delivery, isolation, scaling, or recovery must not depend on one web process.

## What Changed
- Established the ownership-and-lifetime distinction between request follow-up work and continuous service workers.
- Added explicit cancellation and awaiting as the shutdown half of the pattern.
- Bounded the pattern to suitable in-process asynchronous work rather than durable job execution.

## Related Concepts
- [[PythonConcurrencyLibraries]] - `asyncio` provides the cooperative task primitive used by the pattern.
- [[TaskQueueDesign]] - external queues address durability, scheduling, retries, and worker separation beyond this pattern.
- [[SystemReliability]] - fault containment and graceful shutdown determine whether the worker fails predictably.
- [[ContainerNativePractice]] - service-bound tasks must cooperate with process signals and platform termination.
