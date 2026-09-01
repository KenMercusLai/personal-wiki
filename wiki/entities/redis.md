---
title: "Redis"
description: "Server-side data store used as the state, consistency, and atomic operation foundation for a cloud task queue implementation."
type: "entity"
updated: "2026-09-02"
source_keys: ["jysperm-2018-technical-year-review"]
entity_kind: "software"
---

来源：[2018 年度小结（技术方面）]({{< relref "/wiki/sources/jysperm-2018-technical-year-review.md" >}})

Redis 是王子亭实现云引擎任务队列时重度使用的服务器端软件。来源中，任务队列用 Redis 存储所有状态、提供一致性保证，再由 Node.js Worker 执行调度流程，并调用 Lua Script 完成原子操作。

作者认为 Redis 是自己用过最好的服务器端软件之一，原因在于它找准了定位，使设计保持简单。来源还提到 Redis 5 的 Stream 类型很适合任务队列，值得用来实现更充分利用 Stream 特性的队列系统。
