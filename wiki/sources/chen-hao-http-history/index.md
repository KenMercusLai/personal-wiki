---
title: "HTTP的前世今生"
description: "陈皓从HTTP/0.9、1.0、1.1和2写到当时仍在草案期的HTTP/3，重点解释持久连接、多路复用、队头阻塞与QUIC。"
type: "source"
author: "陈皓"
source_date: "2019-10-01"
updated: "2026-08-30"
source_url: "https://coolshell.cn/articles/19840.html"
source_key: "chen-hao-http-history"
featured: true
image_status: "原文没有图片引用"
---

## 核心摘要

这篇文章以性能瓶颈为线索梳理[HTTP版本演进]({{< relref "/wiki/concepts/http-version-evolution.md" >}})：HTTP/0.9只有极简GET请求；HTTP/1.0引入版本、头部、状态码和内容类型；HTTP/1.1通过持久连接、缓存、内容协商和Host等能力扩展Web；HTTP/2使用二进制帧、头部压缩和连接内多路复用；HTTP/3则把HTTP映射到[QUIC]({{< relref "/wiki/entities/quic.md" >}})。

> **历史定位：** 这是2019年的协议生态快照。当时HTTP/3仍在草案和早期部署阶段；正式标准RFC 9114于2022年发布。文章中的采用率、浏览器支持、RFC替代关系和“未来十年”判断必须按2019年语境阅读。

> **图片状态：** 原文没有图片引用，本次Ingest没有生成或补配示意图。

## 版本演进中的稳定主线

### HTTP/0.9与1.0：从极简请求到可扩展消息

文章把版本号、请求/响应头、状态码和`Content-Type`视为协议工程化的重要节点。这个观察的价值在于：元数据、状态表达和内容描述让中间件、缓存、监控与多种媒体类型能够围绕统一协议协作。

### HTTP/1.1：连接复用与Web基础能力

HTTP/1.1的持久连接减少重复建立TCP连接的成本，Host支持同一地址承载多个站点，缓存与内容协商扩展了Web基础设施。文章也讨论Pipeline，但它受HTTP层[队头阻塞]({{< relref "/wiki/concepts/http-head-of-line-blocking.md" >}})和实现复杂度影响，未成为现代浏览器的主流并发方式。

需要修正原文的一点：Chunked Transfer Coding是当响应体长度预先未知时使用的消息分帧机制，不等同于HTTP/2 Server Push，也不要求只能依赖连接EOF界定消息。RFC 7230明确把Chunked描述为HTTP/1.1消息分帧机制。

### HTTP/2：连接内并发

HTTP/2通过二进制帧把多个Stream复用到同一连接，并用HPACK压缩头字段，从而允许多个HTTP交换并发进行。原文提到的“优先级树”属于RFC 7540时代的设计；2022年的RFC 9113已废弃那套优先级信令，因此不能把它当作当前HTTP/2实现的固定要求。

### HTTP/3：HTTP over QUIC

文章准确抓住了HTTP/3的主要动机：HTTP/2的多个Stream共享一个TCP有序字节流，丢包可能使连接内多个Stream一起等待。QUIC在UDP之上提供加密、多路Stream、流量控制、丢包恢复和路径迁移，让丢包造成的传输层等待主要限制在受影响的Stream，而不跨所有HTTP Stream传播。

## 需要保留的纠偏

- HTTP/3不是2018年正式发布；RFC 9114发布于2022年6月。
- QUIC减少的是跨Stream的传输层队头阻塞，不意味着UDP或QUIC世界中不存在顺序、重传和拥塞控制。
- NAT同样可以为UDP维护映射；Connection ID的关键作用是让QUIC连接身份不完全绑定网络五元组，从而支持路径变化。
- QUIC不是简单的“伪TCP + TLS + HTTP/2”。它是独立的安全多路传输协议，HTTP/3是在其上定义的HTTP映射。
- 原文关于握手次数、BBR必然更好、TCP可能成为历史等表述是简化或判断，不编译为稳定结论。

## 可复用认识

- 协议演进通常由可扩展性、可观察性、连接成本和并发瓶颈共同推动。
- 多路复用发生在哪一层，会决定丢包和排序阻塞影响多大的共享范围。
- 标准化不只增加能力，也会废弃复杂度高、部署效果不佳的机制。
- 阅读协议历史文章时，应把“当时部署状态”同“最终RFC定义”分开。

## 来源与标准核对

- 陈皓，[《HTTP的前世今生》](https://coolshell.cn/articles/19840.html)，2019-10-01。
- [RFC 9112：HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112.html)
- [RFC 9113：HTTP/2](https://www.rfc-editor.org/rfc/rfc9113.html)
- [RFC 9000：QUIC](https://www.rfc-editor.org/rfc/rfc9000.html)
- [RFC 9114：HTTP/3](https://www.rfc-editor.org/rfc/rfc9114.html)
