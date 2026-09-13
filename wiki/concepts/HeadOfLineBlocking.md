---
title: "Head-of-Line Blocking"
type: concept
tags: [networking, performance, protocol]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
  - alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[HeadOfLineBlocking]] is a performance problem where later work waits behind earlier stalled work, even when the later work could otherwise proceed independently.

## Current Synthesis
Head-of-line blocking appears at both protocol and application-pipeline layers. In HTTP/1.1 pipelining, a blocked request can delay later requests in the same queue. In [[HTTP2]], multiplexed HTTP streams share one TCP connection, but TCP does not know about HTTP stream boundaries; packet loss therefore stalls all streams until the missing TCP data is retransmitted.

The article presents [[HTTP3]] and [[QUIC]] as the response to the TCP-level form of this problem. By moving stream and reliability handling above UDP, QUIC can avoid tying every logical HTTP stream to the same ordered TCP byte stream.

The same scheduling failure can occur above the network stack. A single shared destination queue can mix new events with retries for many downstream partners, so one slow or failing destination fills the queue with retry work and delays unrelated destinations. Segment's first architectural response was separate destination queues and workers behind a router, trading shared-queue blocking for more services, repos, and operations.

## Key Claims
- HTTP/1.1 pipelining can suffer queue-level head-of-line blocking.
- HTTP/2 reduces HTTP request serialization but still inherits TCP-level head-of-line blocking.
- TCP cannot distinguish which HTTP/2 stream a lost packet belongs to, so loss can stall all multiplexed streams.
- QUIC over UDP is presented as a way to remove TCP's ordered byte-stream constraint from HTTP/3.
- Head-of-line blocking is a traffic-scheduling problem rather than only an HTTP syntax problem.
- Shared application queues can create cross-tenant or cross-destination blocking when retry work from one slow dependency delays unrelated work.
- Queue isolation can remove one blocking path while increasing architectural and operational surface area.

## Evidence
- HTTP/1.1 queueing: [[chen-hao-http-de-qian-shi-jin-sheng]] says a blocked pipelined request can block all later queued requests.
- HTTP/2 over TCP: [[chen-hao-http-de-qian-shi-jin-sheng]] explains that TCP does not know how many HTTP requests are multiplexed above it.
- Packet-loss consequence: [[chen-hao-http-de-qian-shi-jin-sheng]] says all HTTP requests on a TCP connection wait for retransmission after packet loss.
- QUIC response: [[chen-hao-http-de-qian-shi-jin-sheng]] argues that UDP plus QUIC avoids the TCP version of this blocking.
- Scheduling framing: [[chen-hao-http-de-qian-shi-jin-sheng]] calls the issue a classic traffic-scheduling problem.
- Shared retry queue: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says retryable destination failures were put back into the same queue as new events.
- Cross-destination delay: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] says one failing destination could increase delivery times for all destinations.
- Isolation response: [[alexandra-noonan-goodbye-microservices-from-100s-of-problem-children-to-1-superstar]] shows a router distributing events to separate destination queues.

## Counterevidence & Qualifications
The HTTP article focuses on protocol mechanisms and does not quantify how often head-of-line blocking dominates performance in real networks. The Twilio Segment article shows queue isolation solving a real product problem, but also shows that the isolation strategy created later operational overhead. Avoiding one blocking mode is therefore not sufficient proof that the resulting architecture is globally simpler or more reliable.

## What Changed
- Created the head-of-line blocking concept page as the performance problem connecting HTTP/1.1, HTTP/2, and HTTP/3.
- Added Twilio Segment's destination queue as an application-pipeline example where retry traffic from one dependency blocked unrelated destinations.

## Related Concepts
- [[HTTP11]] - HTTP/1.1 pipelining can block later requests behind an earlier one.
- [[HTTP2]] - HTTP/2 still has TCP-level head-of-line blocking despite multiplexing.
- [[HTTP3]] - HTTP/3 is presented as the HTTP response to TCP-level blocking.
- [[QUIC]] - QUIC avoids TCP's ordered byte-stream constraint by running above UDP.
- [[TaskQueueDesign]] - queue topology can either create or relieve blocking among work classes.
- [[MicroserviceOperationalOverhead]] - Segment's queue isolation reduced blocking but later increased service overhead.
