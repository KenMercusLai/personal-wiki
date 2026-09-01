---
title: "HTTP/3 与 QUIC"
description: "HTTP/3 用 QUIC 在 UDP 上承载 HTTP 多路复用，以缓解 TCP 队头阻塞，并重新设计连接标识、握手、拥塞控制和头压缩。"
type: "concept"
updated: "2026-09-01"
source_keys: ["chen-hao-http-history"]
---

HTTP/3 与 QUIC 是来源中描述 HTTP 继续突破 TCP 限制的协议路线。

来源：[陈皓 - HTTP的前世今生]({{< relref "/wiki/sources/chen-hao-http-history.md" >}})

## 设计动机

HTTP/2 在一个 TCP 连接上复用多个 HTTP 请求，但 TCP 不理解上层请求边界。一旦 TCP 层丢包，复用在同一连接上的所有 HTTP 请求都必须等待重传。来源将这个问题视为 HTTP/3 转向 UDP 和 QUIC 的核心动因。

## QUIC 的角色

来源把 QUIC 概括为运行在 UDP 之上的伪 TCP、TLS 和 HTTP/2 多路复用组合。QUIC 自己处理丢包重传和拥塞控制，可从 CUBIC 走向 BBR 这类测量模型；它还把 TCP 与 TLS 握手合并，减少 HTTPS 连接建立时的网络交互。

QUIC 使用 connection id 标识连接，而不是只依赖源地址、源端口、目标地址和目标端口组成的四元组。这使网络在 3G/4G 与 Wi-Fi 间切换时，理论上可以保持同一连接不断开。

## 部署挑战

HTTP/3 改动到底层传输协议，因此来源判断它的普及可能慢于 HTTP/2。NAT、负载均衡和等价路由设备可能只理解 UDP 四元组而不理解 connection id；HTTP/2 的 HPACK 头压缩也不能直接套用到 UDP 场景，需要 QPACK 重新设计编码端与解码端的同步方式。
