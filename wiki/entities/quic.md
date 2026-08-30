---
title: "QUIC"
description: "基于UDP的安全多路传输协议，为HTTP/3提供Stream、低时延建连、丢包恢复和路径迁移。"
type: "entity"
entity_kind: "protocol"
updated: "2026-08-30"
source_keys: ["chen-hao-http-history"]
featured: false
---

## 概览

QUIC是基于UDP承载的安全多路传输协议。它在用户态实现加密连接、可靠传输、多路Stream、流量与拥塞控制，并成为HTTP/3的传输基础。

## 与HTTP/2 over TCP的关键差别

HTTP/2把多个HTTP Stream复用到一个TCP有序字节流；一个TCP缺口可能暂时阻挡所有Stream。QUIC分别管理Stream的有序数据，使丢包恢复主要阻挡受影响Stream，从而缩小[队头阻塞]({{< relref "/wiki/concepts/http-head-of-line-blocking.md" >}})的传播范围。

QUIC Connection ID让连接身份不完全依赖网络地址和端口，因此可在验证新路径后支持网络切换。它并不表示UDP没有NAT映射，也不意味着QUIC不做重传或拥塞控制。

## 标准边界

来源文章写于2019年，当时HTTP/3仍在草案阶段。QUIC正式标准RFC 9000发布于2021年，HTTP/3 RFC 9114发布于2022年。当前定义应以RFC为准，而不是早期部署描述。

## 来源

- [《HTTP的前世今生》]({{< relref "/wiki/sources/chen-hao-http-history.md" >}})
