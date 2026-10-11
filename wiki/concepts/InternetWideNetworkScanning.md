---
title: "Internet-Wide Network Scanning"
type: concept
tags: [networking, measurement, performance, storage]
sources:
  - traceroute-the-world-ka-wa-bang-ga
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[InternetWideNetworkScanning]] is high-rate probing across a substantial address space to measure a narrowly defined network property, with packet generation, reply attribution, state representation, rate control, ethics, and uncertainty treated as one system.

## Current Synthesis
The source presents a specialized breadth-first scan for long [[Traceroute]] responses. Rather than allocate a waiting process to every target, one path emits probes and another consumes replies; separate rounds encode TTL externally, eliminating the need to recover it from each received echo reply. AF_XDP and XDP reduce packet-path overhead, a BPF ring buffer exports only accepted records, and an IPv4-indexed bitmap compresses response state to 512 MiB per round. `mmap` simplifies random bit updates and sparse files reduce physical allocation when written regions remain limited. These optimizations improve feasibility but do not solve measurement bias, Internet-scan safety, or proof of completeness.

## Key Claims
- Separate send and receive paths remove per-target waiting and reduce process-scheduling overhead.
- Repeating the address space once per TTL trades extra rounds for simple reply attribution and candidate elimination.
- Early packet filtering and bounded kernel-to-user transfer reduce unnecessary user-space work.
- Dense address domains can be represented compactly by using the address integer as a bitmap index.
- Rate limiting is both an operational constraint and a measurement-design choice, not merely unused capacity.
- Efficient execution does not make ICMP response behavior an unbiased measure of path length.

## Evidence
- Concurrency design: [[traceroute-the-world-ka-wa-bang-ga]] replaces send-and-wait traceroute processes with independent packet emission and reply collection.
- TTL attribution: [[traceroute-the-world-ka-wa-bang-ga]] scans in successive TTL rounds and removes destinations once they return an echo reply.
- Packet processing: [[traceroute-the-world-ka-wa-bang-ga]] assigns AF_XDP to egress, XDP to ingress filtering, and a BPF ring buffer to accepted address records.
- State compression: [[traceroute-the-world-ka-wa-bang-ga]] derives 512 MiB for one bit across all 2^32 IPv4 values, then uses `mmap` and sparse files for updates and allocation.
- Throughput planning: [[traceroute-the-world-ka-wa-bang-ga]] estimates about 11.9 hours per address-space pass at its chosen 100,000-packet-per-second limit.

## Counterevidence & Qualifications
The estimate uses nominal bandwidth and frame size rather than measured sustained throughput and omits some on-wire and systems overhead. Full numeric IPv4 coverage is not the same as valid routed-target coverage; scanners should define exclusions, authorization, source identification, opt-out and abuse handling, and rate distribution. ICMP filtering, loss, rate limits, alternate response addresses, route changes, and TTL anomalies affect both candidate survival and the meaning of the final TTL. Sparse-file savings depend on filesystem behavior and the locality of written blocks, not merely on writing one bits.

## What Changed
- Established a joined model of asynchronous probing, TTL-round attribution, early filtering, compact state, and rate control.
- Added measurement validity and responsible-scanning controls as necessary boundaries on performance claims.

## Related Concepts
- [[Traceroute]] - supplies the TTL-dependent response signal being measured.
- [[TracerouteTheWorld]] - concrete project implementing the staged scan.
- [[DigitalOcean]] - hosting environment whose stated link limit anchors the source's capacity estimate.
