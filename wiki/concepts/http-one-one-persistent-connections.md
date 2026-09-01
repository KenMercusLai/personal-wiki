---
title: "HTTP/1.1 持久连接"
description: "HTTP/1.1 通过 keepalive 复用 TCP 连接，并配合管线化、分块响应、缓存控制和 Host 头改善 HTTP/1.0 的性能与表达能力。"
type: "concept"
updated: "2026-09-01"
source_keys: ["chen-hao-http-history"]
---

HTTP/1.1 持久连接是来源中用于说明 HTTP 性能工程化的重要阶段。

来源：[陈皓 - HTTP的前世今生]({{< relref "/wiki/sources/chen-hao-http-history.md" >}})

## 核心机制

HTTP/1.0 的主要性能问题是每请求一个资源就新建一个 TCP 连接，并且请求串行发生。HTTP/1.1 引入 `keepalive` 复用 TCP 连接，减少每次请求都进行三次握手的广域网开销。

HTTP/1.1 还支持管线化传输，使客户端可以在第一个请求返回前继续发出后续请求；支持分块响应，让服务端不必预先声明完整 `Content-Length`；并加入缓存控制、语言/编码/类型协商、`Host` 头和 `OPTIONS` 方法。

## 协议意义

来源把 HTTP/1.1 分成 2014 年前后两个阶段。2014 年后的 RFC 组合加强了安全性和应用支持，使 HTTP 能覆盖短连接、可复用 TCP 长连接、服务端推送和 WebSocket 等模型，从而更像通用应用层协议而不只是网页资源传输协议。
