---
title: "HTTP/1.1"
type: concept
tags: [networking, protocol, web]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
  - robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[HTTP11]] is the HTTP version that added persistent connections, pipelining, chunked responses, cache control, content negotiation, Host routing, and additional methods while retaining a sequential response model on each connection.

## Current Synthesis
HTTP/1.1 turned HTTP from a simple resource-transfer protocol into a broader application-layer communication standard. Persistent connections reduced repeated TCP handshake overhead, while Host, caching, negotiation headers, chunked responses, CORS-related OPTIONS use, and later WebSocket-era patterns made HTTP more adaptable to web applications and APIs.

Its framing still cannot identify interleaved chunks from different responses. A response's headers and payload must therefore be delivered in full before another response can use the same connection, so a large or slow object can block later objects. Browsers mitigated this with several parallel TCP connections, accepting extra server state, handshakes, TLS work, and independent congestion controllers. Pipelining can overlap requests and save round trips, but responses must remain in request order and cannot be truly multiplexed.

## Key Claims
- Persistent connections reduce the cost of establishing a new TCP connection for each resource.
- Pipelining can overlap requests but cannot reorder or interleave responses, so response-side [[HeadOfLineBlocking]] remains.
- HTTP/1.1 framing cannot identify chunks from different resources, preventing true response multiplexing on one connection.
- Browsers use several parallel TCP connections to reduce serialization, at the cost of extra state, setup work, and separate congestion controllers.
- Chunked responses let servers stream one response without declaring its full length upfront; they do not create cross-resource multiplexing.
- Cache control, negotiation headers, Host, and OPTIONS made HTTP/1.1 broadly useful for web and API deployment.
- HTTP/1.1's ordering and framing limits motivated [[HTTP2]].

## Evidence
- Connection reuse and platform role: [[chen-hao-http-de-qian-shi-jin-sheng]] describes keepalive, cache control, negotiation, Host, OPTIONS, chunking, and the 2014 RFC series.
- Serialization mechanism: [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] shows that headers delimit whole responses but provide no chunk-level resource identity for interleaving.
- Parallel-connection workaround: [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] says browsers typically opened about six TCP connections per origin to reduce blocking.
- Pipelining boundary: [[chen-hao-http-de-qian-shi-jin-sheng]] and [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] describe pipelining limits; the latter's inspected sequence diagram shows overlapped requests followed by complete, ordered responses.

## Counterevidence & Qualifications
Parallel connections can make well-tuned HTTP/1.1 competitive with a single multiplexed connection on lossy networks because one connection's loss or congestion response does not directly stall the others. This does not remove HTTP/1.1's per-connection serialization, and it spends more connection, TLS, server, and congestion-control resources. The sources explain mechanisms and historical browser behavior rather than providing current comparative benchmarks.

## What Changed
- Clarified that HTTP/1.1 pipelining overlaps requests but does not multiplex or reorder responses.
- Added the browser parallel-connection workaround and its congestion-control and setup tradeoffs.
- Distinguished chunked transfer of one response from multiplexing chunks across resources.

## Related Concepts
- [[HTTP]] - HTTP/1.1 is one stage in HTTP's wider protocol lineage.
- [[HTTP2]] - HTTP/2 adds framed stream identity to overcome HTTP/1.1 response serialization.
- [[HeadOfLineBlocking]] - a slow HTTP/1.1 response blocks later responses on the same connection.
- [[HTTP3]] - HTTP/3 addresses the later transport-level blocking exposed by HTTP/2 over TCP.
