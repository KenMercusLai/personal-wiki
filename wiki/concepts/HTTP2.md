---
title: "HTTP/2"
type: concept
tags: [networking, protocol, web]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Definition
[[HTTP2]] is the HTTP version that improves performance through binary framing, concurrent streams over one TCP connection, header compression, server push, and more complex request scheduling.

## Current Synthesis
The source presents HTTP/2 as the major performance response to HTTP/1.1. Where HTTP/1.1 could reuse TCP connections but still serialized request handling, HTTP/2 can multiplex multiple HTTP requests over one TCP connection. It also reduces overhead by using binary framing and HPACK header compression, while server push allows related resources to be sent before the client explicitly requests them.

The article's qualification is that HTTP/2 pays for these improvements with much higher protocol complexity. Priority trees and invisible scheduling mechanisms make the protocol harder to maintain and extend, and [[HeadOfLineBlocking]] remains possible because the multiplexed streams still share TCP.

## Key Claims
- HTTP/2 was based on Google's SPDY experiment and became the standardized successor to that work.
- Binary framing improves transfer efficiency compared with HTTP/1.1's textual framing.
- Multiplexing lets multiple HTTP requests share one TCP connection concurrently.
- HPACK header compression reduces repeated request-header overhead across similar requests.
- Server push can pre-position dependent resources in client-side cache.
- HTTP/2 increases protocol complexity and still inherits TCP-level [[HeadOfLineBlocking]].

## Evidence
- SPDY lineage: [[chen-hao-http-de-qian-shi-jin-sheng]] says Google's SPDY became the basis or close copy for [[HTTP2]].
- Binary framing: [[chen-hao-http-de-qian-shi-jin-sheng]] identifies HTTP/2 as a binary protocol for improved transfer efficiency.
- Multiplexing: [[chen-hao-http-de-qian-shi-jin-sheng]] says HTTP/2 can concurrently send multiple HTTP requests over one TCP connection.
- Header compression: [[chen-hao-http-de-qian-shi-jin-sheng]] names HPACK as the mechanism that removes repeated header parts.
- Server push: [[chen-hao-http-de-qian-shi-jin-sheng]] describes servers sending dependent resources before the client separately requests them.
- Complexity and blocking: [[chen-hao-http-de-qian-shi-jin-sheng]] notes priority-tree complexity and later explains that TCP packet loss can block all multiplexed streams.

## Counterevidence & Qualifications
The source reports broad adoption and strong performance benefits but does not provide benchmark data. It also emphasizes that HTTP/2's complexity created maintainability and extensibility concerns.

## What Changed
- Created the HTTP/2 concept page as the wiki's protocol-performance upgrade node.

## Related Concepts
- [[HTTP]] - HTTP/2 is a performance-oriented version in the HTTP family.
- [[HTTP11]] - HTTP/2 responds to HTTP/1.1's serial request and textual-transfer limits.
- [[HTTP3]] - HTTP/3 keeps the HTTP/2-style application model while changing transport via QUIC.
- [[QUIC]] - QUIC is used by HTTP/3 to address transport limits that HTTP/2 could not solve over TCP.
- [[HeadOfLineBlocking]] - TCP-level blocking is the central unresolved HTTP/2 problem in the source.
