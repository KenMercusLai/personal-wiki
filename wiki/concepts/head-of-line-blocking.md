---
title: "队头阻塞"
description: "队头阻塞指队列或有序传输中前面的请求、数据包或流受阻时，后续工作即使无关也被迫等待。"
type: "concept"
updated: "2026-09-01"
source_keys: ["chen-hao-http-history"]
---

队头阻塞是来源用来解释 HTTP/1.1、HTTP/2 和 HTTP/3 差异的关键性能问题。

来源：[陈皓 - HTTP的前世今生]({{< relref "/wiki/sources/chen-hao-http-history.md" >}})

## 在 HTTP 中的表现

HTTP/1.1 的管线化请求如果前面的请求被阻塞，队列后面的请求也会一起等待。HTTP/2 虽然能在一个 TCP 连接中复用多个 HTTP 请求，但 TCP 层一旦丢包，所有复用在同一 TCP 连接上的 HTTP 请求都要等这个包重传回来，即使丢失的数据并不属于某个具体请求。

## 对 HTTP/3 的影响

来源认为 TCP 本身难以解决这个问题，因为 TCP 无法理解上层 HTTP 请求之间的独立性。HTTP/3 因此选择基于 UDP 的 QUIC，由 QUIC 在应用可控的层面处理可靠性、丢包重传和多路复用，减少单个丢包对所有 HTTP 请求的连带影响。
