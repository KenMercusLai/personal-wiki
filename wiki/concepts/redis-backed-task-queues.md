---
title: "Redis-backed task queues"
description: "用 Redis 保存任务队列状态和一致性边界，通过 Worker、Lua Script 或 Stream 支撑调度、恢复和原子操作。"
type: "concept"
updated: "2026-09-02"
source_keys: ["jysperm-2018-technical-year-review"]
---

来源：[2018 年度小结（技术方面）]({{< relref "/wiki/sources/jysperm-2018-technical-year-review.md" >}})

Redis-backed task queues 指把任务队列的状态、并发控制和原子调度语义放在 Redis 中实现。王子亭在云引擎任务队列中采用这种方式：队列本身主要提供调度能力，不额外提供计算资源，而是通过 HTTP 调用已有云函数。

在这个实现里，Redis 用来存储所有状态并提供一致性保证，Node.js Worker 负责执行调度流程，Lua Script 则用于把多个状态变更压成 Redis 内部的原子操作。这个设计适合任务状态需要在应用重启后恢复、同时又不希望引入复杂外部协调系统的场景。

来源也指出，任务队列需求高度多样，往往与业务和语言运行时相关。作者认为 Redis 5 的 Stream 类型天然适合任务队列，因为它在 Redis 的数据模型内提供了更接近消息流和消费进度管理的能力。
