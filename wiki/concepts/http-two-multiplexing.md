---
title: "HTTP/2 多路复用"
description: "HTTP/2 以 SPDY 为基础，通过二进制帧、单 TCP 连接并发请求、HPACK 头压缩和服务端推送提升 HTTP 吞吐。"
type: "concept"
updated: "2026-09-01"
source_keys: ["chen-hao-http-history"]
---

HTTP/2 多路复用是来源中解释 HTTP 从连接复用走向请求并发的关键机制。

来源：[陈皓 - HTTP的前世今生]({{< relref "/wiki/sources/chen-hao-http-history.md" >}})

## 解决的问题

HTTP/1.1 虽然可以复用 TCP 连接，但请求仍然需要按顺序处理，网页资源请求量大时会限制吞吐。HTTP/1.1 的文本传输也依赖压缩来节省带宽，增加前端和后端 CPU 成本。

HTTP/2 基于 Google 的 SPDY 思路，把协议改为二进制格式，并允许在一个 TCP 连接中并发传输多个 HTTP 请求。它还使用 HPACK 压缩相似请求头，减少重复头部带来的传输开销；服务端推送则允许服务端把与当前请求相关的资源提前放入客户端缓存。

## 取舍

来源认为 HTTP/2 显著提高了 HTTP 性能，并推动标准更快落地；同时它也大幅增加协议复杂度，例如需要维护优先级树来调度资源和请求。这种复杂度会影响协议的可维护性和可扩展性。
