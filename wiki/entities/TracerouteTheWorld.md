---
title: "Traceroute the World"
type: entity
tags: [networking, open-source, measurement]
sources:
  - traceroute-the-world-ka-wa-bang-ga
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[TracerouteTheWorld]] is an open-source hobby project for searching the IPv4 address space from Singapore for destinations that first answer ICMP echo probes at unusually high TTL values.

## Current Profile
The project replaces conventional per-target [[Traceroute]] with repeated address-space sweeps. It sends probes through AF_XDP, filters ingress traffic with XDP, transfers accepted reply addresses through a BPF ring buffer, and stores one bit per IPv4 address in `mmap`-backed sparse files. Its source article reports a 34-hop result and links the code repository, while leaving the full measurement corpus, repeatability, address exclusions, and operational safeguards undocumented.

## Key Characteristics
- Searches for high-TTL IPv4 responders rather than reconstructing every intermediate path.
- Separates high-rate sending from asynchronous reply collection.
- Uses kernel-bypass and early-ingress processing to reduce packet-path overhead.
- Represents each scan round as a one-bit-per-address bitmap.
- Is presented as an exploratory hobby project rather than a validated Internet census.

## Evidence
- Scan algorithm: [[traceroute-the-world-ka-wa-bang-ga]] describes eliminating destinations when they first echo-reply and rescanning survivors at the next TTL.
- Packet path: [[traceroute-the-world-ka-wa-bang-ga]] names AF_XDP, XDP, and a BPF ring buffer as the send, receive-filter, and kernel-to-user transfer mechanisms.
- Storage design: [[traceroute-the-world-ka-wa-bang-ga]] derives a 512 MiB IPv4 bitmap and combines it with `mmap` and sparse allocation.
- Reported outcome: [[traceroute-the-world-ka-wa-bang-ga]] includes an MTR screenshot with a destination answering at hop 34 and four intervening positions without replies.

## Qualifications
The project is documented by its author rather than independently evaluated. A high first-reply TTL is affected by ICMP policy and routing behavior and does not prove a globally longest route. The article does not provide source-code revision, run logs, complete candidate counts, repeated measurements, packet-loss analysis, non-routable-address exclusions, abuse-response procedures, or independent reproduction.

## What Changed
- Established the project profile, staged scan design, implementation stack, and reported 34-hop result.

## Relationships
- [[Traceroute]] - supplies the TTL-expiry and echo-reply behavior adapted by the project.
- [[InternetWideNetworkScanning]] - measurement class implemented as repeated full-address-space rounds.
- [[DigitalOcean]] - infrastructure provider for the reported Singapore experiment.
