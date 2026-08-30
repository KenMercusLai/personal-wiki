---
title: "HTTP中的队头阻塞"
description: "前方未完成的数据阻止后续独立工作继续；阻塞发生在哪一层决定影响范围。"
type: "concept"
updated: "2026-08-30"
source_keys: ["chen-hao-http-history"]
featured: false
---

## 定义

队头阻塞是队列前部的工作未完成，导致后续本可独立推进的工作一起等待。讨论HTTP时必须区分它发生在HTTP语义层还是传输层。

## 两种典型形态

- **HTTP/1.1 Pipeline：** 同一连接上的响应必须保持请求顺序；前一个响应变慢会阻挡后续响应。
- **HTTP/2 over TCP：** HTTP/2的Stream彼此独立，但都承载在一个TCP有序字节流上；TCP丢包恢复期间，后续已到达字节不能越过缺口交付，因而多个HTTP Stream可能一起等待。

[QUIC]({{< relref "/wiki/entities/quic.md" >}})为不同Stream分别维护有序交付，减少跨Stream的传输层队头阻塞。但受影响Stream内部仍需排序和重传，网络拥塞也仍会影响连接整体；“消除队头阻塞”必须限定层次。

## 来源

- [《HTTP的前世今生》]({{< relref "/wiki/sources/chen-hao-http-history.md" >}})
