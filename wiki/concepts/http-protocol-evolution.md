---
title: "HTTP 协议演进"
description: "HTTP 从极简请求响应协议逐步演进出版本、头部、状态码、持久连接、多路复用、QUIC 传输和可扩展状态语义等能力。"
type: "concept"
updated: "2026-09-02"
source_keys: ["chen-hao-http-history", "david-humphrey-402-payment-required"]
---

HTTP 协议演进体现了 Web 基础设施从简单文档传输走向通用应用层通信的过程。

来源：[陈皓 - HTTP的前世今生]({{< relref "/wiki/sources/chen-hao-http-history.md" >}})、[402: Payment Required]({{< relref "/wiki/sources/david-humphrey-402-payment-required.md" >}})

## 演进脉络

- HTTP/0.9 只支持极简的 `GET` 请求，没有请求头。
- HTTP/1.0 增加版本号、请求和响应头、状态码以及 `Content-Type`，使协议开始具备工程化边界。
- HTTP/1.1 通过持久连接、管线化、分块响应、缓存控制、内容协商、`Host` 头和 `OPTIONS` 方法扩展性能与应用能力。
- 2014 年后的 HTTP/1.1 RFC 组合强化安全性和应用适配，使 HTTP 更接近通用应用协议标准。
- HTTP/2 用二进制协议、多路复用、头压缩和服务端推送提升传输效率。
- HTTP/3 借助 QUIC 改用 UDP 承载，以绕开 TCP 层面的队头阻塞并改善移动网络连接体验。
- David Humphrey 从状态码语义角度补充了另一种演进方向：HTTP 402 Payment Required 可以被设想为浏览器、网站和支付服务协商付费访问的标准信号。

## 价值判断

来源把 HTTP 的历史解释为工程化和性能瓶颈不断被制度化解决的过程。版本管理、头部、状态码和内容类型让协议可治理；持久连接和多路复用提高吞吐；QUIC 则把问题推进到底层传输模型，试图让 HTTP 在更复杂的网络环境中保持可扩展。

Humphrey 的来源强调，状态码也可以承载经济协调语义。保留给未来用途的 402 如果被浏览器和网站共同实现，就可能把付费访问从各站自建付费墙推进到更通用的用户代理能力。
