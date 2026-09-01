---
title: "陈皓 - HTTP的前世今生"
description: "陈皓按 HTTP 版本回顾协议从简单请求响应、持久连接和缓存控制，演进到 HTTP/2 多路复用与 HTTP/3/QUIC 的性能取舍。"
type: "source"
updated: "2026-09-01"
source_key: "chen-hao-http-history"
image_status: "not_selected"
author: "陈皓"
source_date: "2019-10-01"
source_url: "https://coolshell.cn/articles/19840.html"
---

## 摘要

这篇文章以 HTTP 版本为主线，解释协议如何从 HTTP/0.9 的极简 `GET` 请求，演进为承载现代 Web 与应用 API 的通用应用层协议。作者特别关注工程化、性能、安全性和标准化：HTTP/1.0 引入版本号、请求/响应头、状态码和内容类型，HTTP/1.1 通过持久连接、管线化、分块传输、缓存控制、内容协商、`Host` 和 `OPTIONS` 扩展能力，HTTP/2 用二进制帧、多路复用、HPACK 和服务端推送提高吞吐，HTTP/3 则借助 QUIC 把传输层从 TCP 转向 UDP 以缓解 TCP 层面的队头阻塞。

文章也强调协议演进中的代价。HTTP/2 在性能上显著改善 HTTP/1.1，但复杂度上升，需要维护优先级树等调度结构；HTTP/3/QUIC 能绕开 TCP 丢包导致的连接级阻塞，并通过 connection id、独立重传与拥塞控制、握手合并等设计改善连接体验，但会面对 NAT、负载均衡和头压缩同步等来自网络设备与协议栈的挑战。

## 关键观点

- HTTP/1.0 让协议具备版本、头部、状态码和内容类型等工程化结构，但每个资源都新建 TCP 连接，性能代价很高。
- HTTP/1.1 的持久连接、管线化、分块响应、缓存控制、内容协商、`Host` 头和 `OPTIONS` 方法，推动 HTTP 成为更通用的应用层通信基础。
- 2014 年后的 HTTP/1.1 RFC 组合加强安全性与应用适配能力，使很多专用 RPC 或私有协议更难证明重新发明协议栈的必要性。
- HTTP/2 继承 SPDY 思路，用二进制协议、单 TCP 连接上的并发请求、HPACK 头压缩和服务端推送解决 HTTP/1.1 的串行与传输开销问题。
- HTTP/3 以 QUIC 承载 HTTP/2 式多路复用，用 UDP、自有重传与拥塞控制、connection id 和 QPACK 重新处理 TCP 连接中难以解决的队头阻塞与移动网络切换问题。
- HTTP/3 的普及可能慢于 HTTP/2，因为它改动到底层传输协议，并依赖 NAT、路由、负载均衡和中间网络设备能正确处理 QUIC/UDP 流量。

## 相关知识

- [HTTP 协议演进]({{< relref "/wiki/concepts/http-protocol-evolution.md" >}})
- [HTTP/1.1 持久连接]({{< relref "/wiki/concepts/http-one-one-persistent-connections.md" >}})
- [HTTP/2 多路复用]({{< relref "/wiki/concepts/http-two-multiplexing.md" >}})
- [HTTP/3 与 QUIC]({{< relref "/wiki/concepts/http-three-and-quic.md" >}})
- [队头阻塞]({{< relref "/wiki/concepts/head-of-line-blocking.md" >}})
- [Tim Berners-Lee]({{< relref "/wiki/entities/tim-berners-lee.md" >}})
- [CERN]({{< relref "/wiki/entities/cern.md" >}})
