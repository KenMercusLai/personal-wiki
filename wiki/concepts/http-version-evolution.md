---
title: "HTTP版本演进"
description: "HTTP从极简请求发展为带元数据、缓存、连接复用、多路Stream和QUIC传输的应用协议。"
type: "concept"
updated: "2026-08-30"
source_keys: ["chen-hao-http-history"]
featured: true
---

## 演进主线

HTTP的版本变化可以沿四条主线理解：消息表达、连接复用、并发模型和传输层选择。

- **HTTP/0.9 → 1.0：** 从极简GET扩展到版本、头部、状态码和内容类型。
- **HTTP/1.1：** 持久连接、Host、缓存和内容协商让HTTP成为可扩展Web基础协议。
- **HTTP/2：** 用二进制帧、HPACK和连接内多Stream提高并发效率。
- **HTTP/3：** 把HTTP映射到[QUIC]({{< relref "/wiki/entities/quic.md" >}})，避免TCP单一有序字节流把丢包等待扩散到所有HTTP Stream。

## 关键认识

版本升级不是简单地“更快”。每次变化都重新划分了元数据与内容、连接与请求、Stream与传输之间的职责。HTTP/1.1 Pipeline和HTTP/2优先级树也说明：进入标准的机制仍可能因[队头阻塞]({{< relref "/wiki/concepts/http-head-of-line-blocking.md" >}})、实现复杂度或部署收益不足而被弱化或废弃。

## 来源

- [《HTTP的前世今生》]({{< relref "/wiki/sources/chen-hao-http-history.md" >}})
