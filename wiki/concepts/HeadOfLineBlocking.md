---
title: "Head-of-Line Blocking"
type: concept
tags: [networking, performance, protocol]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Definition
[[HeadOfLineBlocking]] is a performance problem where later work waits behind earlier stalled work, even when the later work could otherwise proceed independently.

## Current Synthesis
The source uses head-of-line blocking to explain multiple stages of HTTP evolution. In HTTP/1.1 pipelining, a blocked request can delay later requests in the same queue. In [[HTTP2]], multiplexed HTTP streams share one TCP connection, but TCP does not know about HTTP stream boundaries; packet loss therefore stalls all streams until the missing TCP data is retransmitted.

The article presents [[HTTP3]] and [[QUIC]] as the response to the TCP-level form of this problem. By moving stream and reliability handling above UDP, QUIC can avoid tying every logical HTTP stream to the same ordered TCP byte stream.

## Key Claims
- HTTP/1.1 pipelining can suffer queue-level head-of-line blocking.
- HTTP/2 reduces HTTP request serialization but still inherits TCP-level head-of-line blocking.
- TCP cannot distinguish which HTTP/2 stream a lost packet belongs to, so loss can stall all multiplexed streams.
- QUIC over UDP is presented as a way to remove TCP's ordered byte-stream constraint from HTTP/3.
- Head-of-line blocking is a traffic-scheduling problem rather than only an HTTP syntax problem.

## Evidence
- HTTP/1.1 queueing: [[chen-hao-http-de-qian-shi-jin-sheng]] says a blocked pipelined request can block all later queued requests.
- HTTP/2 over TCP: [[chen-hao-http-de-qian-shi-jin-sheng]] explains that TCP does not know how many HTTP requests are multiplexed above it.
- Packet-loss consequence: [[chen-hao-http-de-qian-shi-jin-sheng]] says all HTTP requests on a TCP connection wait for retransmission after packet loss.
- QUIC response: [[chen-hao-http-de-qian-shi-jin-sheng]] argues that UDP plus QUIC avoids the TCP version of this blocking.
- Scheduling framing: [[chen-hao-http-de-qian-shi-jin-sheng]] calls the issue a classic traffic-scheduling problem.

## Counterevidence & Qualifications
The article focuses on explaining the protocol-level mechanism. It does not quantify how often head-of-line blocking dominates performance in real networks or compare mitigation strategies outside HTTP/3 and QUIC.

## What Changed
- Created the head-of-line blocking concept page as the performance problem connecting HTTP/1.1, HTTP/2, and HTTP/3.

## Related Concepts
- [[HTTP11]] - HTTP/1.1 pipelining can block later requests behind an earlier one.
- [[HTTP2]] - HTTP/2 still has TCP-level head-of-line blocking despite multiplexing.
- [[HTTP3]] - HTTP/3 is presented as the HTTP response to TCP-level blocking.
- [[QUIC]] - QUIC avoids TCP's ordered byte-stream constraint by running above UDP.
