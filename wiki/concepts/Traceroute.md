---
title: "Traceroute"
type: concept
tags: [networking, diagnostics, icmp]
sources:
  - traceroute-the-world-ka-wa-bang-ga
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[Traceroute]] is a network-diagnostic method that sends probes with increasing IP time-to-live values and uses destination responses or TTL-expiry errors to infer where a path progresses or stops.

## Current Synthesis
The source uses traceroute's control mechanism but discards its usual path-reconstruction goal. Conventional tooling sends several probes at each TTL and waits for replies, which is useful for inspecting one route but expensive across billions of destinations. [[TracerouteTheWorld]] instead asks only when a destination first returns an ICMP echo reply, scanning all candidates once per TTL and eliminating early responders. The result is a scalable high-TTL search signal, not a complete or stable route measurement.

## Key Claims
- Increasing TTL exposes successive forwarding limits because routers normally decrement the field and may return an expiry error when it reaches zero.
- ICMP echo replies can indicate that a destination was reachable with a given starting TTL.
- Conventional sequential probing trades throughput for per-hop detail, timeouts, and repeated samples.
- First-reply TTL is not identical to a count of visible, unique, or stable routers.

## Evidence
- Protocol mechanism: [[traceroute-the-world-ka-wa-bang-ga]] identifies ICMP echo/reply and TTL-expiry errors as the basis of ping and traceroute diagnostics.
- Scaling limitation: [[traceroute-the-world-ka-wa-bang-ga]] estimates centuries for a sequential full-IPv4 sweep and attributes much of the cost to waiting per hop and per target.
- Measurement reinterpretation: [[traceroute-the-world-ka-wa-bang-ga]] retains only the first TTL round in which each destination echo-replies.
- Incomplete visibility: the final image in [[traceroute-the-world-ka-wa-bang-ga]] shows a destination at hop 34 while four intermediate positions supply no reply.

## Counterevidence & Qualifications
Routers and destinations may filter, rate-limit, deprioritize, source replies from another address, follow asymmetric paths, change routes between probes, or mishandle TTL. Missing hop responses do not prove missing forwarding devices, and an echo reply at TTL 34 does not show 34 named routers. The source's observed result is tied to one Singapore vantage point and one measurement period.

## What Changed
- Established the distinction between conventional route reconstruction and first-response-TTL scanning.
- Added the 34-hop observation as qualified evidence rather than a verified route-length record.

## Related Concepts
- [[InternetWideNetworkScanning]] - applies TTL rounds across the IPv4 address space.
- [[TracerouteTheWorld]] - project that optimizes for finding high-TTL responders rather than detailed paths.
