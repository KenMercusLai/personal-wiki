---
title: "2018 年度小结（技术方面）"
description: "王子亭回顾 2018 年的个人项目、Kubernetes 和容器实践、游戏后端方案以及 Redis 任务队列实现，强调尽快发布可用版本和面向平台的架构。"
type: "source"
updated: "2026-09-02"
source_key: "jysperm-2018-technical-year-review"
image_status: "not_selected"
author: "王子亭"
source_date: "2019-01-30"
source_url: "https://jysperm.me/2019/01/programming-of-2018/index.html"
---

## 摘要

这篇年度技术小结记录了王子亭在 2018 年的个人项目和工作实践。个人项目方面，他认为自己完成的业余项目很少，核心教训是一次专注一个项目，并尽快完成阶段性可用版本、发布出去获得反馈。DeployBeta 持续两年仍未达到公开发布标准，是反例；Elecpass 在 2017 年快速发布两个版本，随后长期自用，并在 2018 年集中一周发布 v3，是更接近可持续节奏的正例。

容器部分把 Kubernetes 视为平台而不只是工具。作者认为容器平台能够简化管理，是因为它让开发者用描述式定义表达期望的最终状态；Kubernetes 进一步把能力抽象成 RESTful 资源，并由各类 Controller 把实际状态同步到预期状态。作者还用 Node.js 为 Dockerfile 做了一个简易 DSL，将 Dockerfile 分段并结构化保存指令，最后生成规范格式，以改善跨应用、跨语言的缓存复用。

文章也反思了生产环境中的容器使用方式。仅仅把现有程序放进容器里，并不等于做到 Container Native；如果容器仍依赖本地存储、缺少有效健康检查，或者不能正确处理信号完成平滑关闭，容器平台能发挥的能力会受到限制。

游戏后端部分来自 LeanCloud 的消息转发服务场景。为了满足反作弊需要，团队需要在服务器端运行游戏逻辑。作者主张把服务器端游戏逻辑也作为客户端接入消息服务，让它围绕消息转发服务与其他客户端交互，从而复用客户端和服务器端的大部分游戏逻辑，平滑支持从单机游戏到动作同步、状态同步的迁移，并保持服务器逻辑和消息转发服务解耦。这个方案后来演化为 LeanCloud 的 Client Engine 产品。

最后，作者总结了云引擎任务队列的实现经验。由于原有云函数已经基于 HTTP，任务队列主要提供调度能力而不额外提供计算资源。实现上使用 Redis 存储状态、提供一致性保证，用 Node.js 实现 Worker，并通过 Lua Script 完成原子操作。作者认为 Redis 的定位和设计非常简洁，并设想 Redis 5 的 Stream 类型适合进一步实现任务队列。

## 关键观点

- 业余项目应尽快进入“已发布”的状态，用真实使用和反馈维持后续迭代动力。
- 容器平台的核心价值来自描述式期望状态和控制器调和循环，而不只是启动容器。
- Container Native 需要应用配合容器生命周期，包括健康检查、信号处理、平滑关闭和避免本地状态依赖。
- 服务器端游戏逻辑可以作为消息系统中的特殊客户端，以减少协议和逻辑重复。
- Redis 适合作为任务队列的状态与一致性基础，Lua Script 和 Stream 都能支撑原子调度语义。

## 相关知识

- [Minimum viable product validation]({{< relref "/wiki/concepts/minimum-viable-product-validation.md" >}})
- [Single-feature MVP scope control]({{< relref "/wiki/concepts/single-feature-mvp-scope-control.md" >}})
- [减少切换的专注工作]({{< relref "/wiki/concepts/focused-work-without-context-switching.md" >}})
- [Declarative container control loops]({{< relref "/wiki/concepts/declarative-container-control-loops.md" >}})
- [Containerized application startup resilience]({{< relref "/wiki/concepts/containerized-application-startup-resilience.md" >}})
- [Server-side game logic as client]({{< relref "/wiki/concepts/server-side-game-logic-as-client.md" >}})
- [Redis-backed task queues]({{< relref "/wiki/concepts/redis-backed-task-queues.md" >}})
- [Docker]({{< relref "/wiki/entities/docker.md" >}})
- [Kubernetes]({{< relref "/wiki/entities/kubernetes.md" >}})
- [Redis]({{< relref "/wiki/entities/redis.md" >}})
