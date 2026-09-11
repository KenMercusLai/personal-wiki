---
title: "HTTP/1.1"
type: concept
tags: [networking, protocol, web]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Definition
[[HTTP11]] is the HTTP version that extended HTTP/1.0 with persistent connections, pipelining, chunked responses, cache control, content negotiation, Host routing, and additional methods such as OPTIONS.

## Current Synthesis
The source frames HTTP/1.1 as the version that turned HTTP from a simple resource-transfer protocol into a broader application-layer communication standard. Persistent connections reduced repeated TCP handshake overhead, while Host, caching, negotiation headers, chunked responses, CORS-related OPTIONS use, and later WebSocket-era patterns made HTTP more adaptable to modern web applications and APIs.

The article also treats HTTP/1.1 as a two-era protocol: before and after the 2014 RFC series. That later standardization is presented as a bridge toward HTTP/2 and as a reason fewer systems needed to build private RPC alternatives.

## Key Claims
- Persistent connections reduce the cost of establishing a new TCP connection for each resource.
- Pipelining can reduce total response time but has method-safety and dependency limitations.
- Chunked responses let servers stream responses without declaring the full content length upfront.
- Cache control, negotiation headers, Host, and OPTIONS made HTTP/1.1 more useful for real web and API deployment.
- The 2014 RFC series strengthened HTTP's safety and application-protocol breadth.
- HTTP/1.1 still retained ordering and blocking limitations that motivated [[HTTP2]].

## Evidence
- Connection reuse: [[chen-hao-http-de-qian-shi-jin-sheng]] says keepalive avoids repeated wide-area TCP handshakes.
- Pipelining limits: [[chen-hao-http-de-qian-shi-jin-sheng]] notes non-idempotent POSTs and dependent requests cannot safely be pipelined.
- Streaming model: [[chen-hao-http-de-qian-shi-jin-sheng]] describes chunked responses as a way to avoid relying on Content-Length before the response ends.
- Deployment features: [[chen-hao-http-de-qian-shi-jin-sheng]] lists cache control, Language, Encoding, Type, Host, and OPTIONS among HTTP/1.1 additions.
- Post-2014 role: [[chen-hao-http-de-qian-shi-jin-sheng]] says HTTP/1.1's later RFCs increased security and broadened supported application patterns.
- Remaining limitation: [[chen-hao-http-de-qian-shi-jin-sheng]] explains that HTTP/1.1 still sent requests in order even when TCP connections were reused.

## Counterevidence & Qualifications
The source praises HTTP/1.1's standardization role but also treats it as performance-limited. It does not separately analyze deployments that avoided pipelining or used multiple parallel TCP connections to mitigate practical latency.

## What Changed
- Created the HTTP/1.1 concept page for the protocol's persistent-connection and API-era role.

## Related Concepts
- [[HTTP]] - HTTP/1.1 is one stage in HTTP's wider protocol lineage.
- [[HTTP2]] - HTTP/2 responds to HTTP/1.1's request-ordering and textual-transfer costs.
- [[HeadOfLineBlocking]] - HTTP/1.1 pipelining can block later requests behind an earlier one.
- [[HTTP3]] - HTTP/3 addresses a later transport-level version of HTTP blocking.
