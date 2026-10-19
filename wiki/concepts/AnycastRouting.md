---
title: "Anycast Routing"
type: concept
tags: [anycast, routing, networking, resilience, latency]
sources:
  - tom-bowles-anycast-dns-part-1
  - smart-tiered-cache-public-clouds
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Definition
[[AnycastRouting]] is a network delivery method in which multiple locations advertise or answer through the same IP address and routing sends each packet or flow toward a currently preferred reachable instance.

## Current Synthesis
Anycast moves endpoint selection from the client-visible address into the routing system. In the DNS case, several servers advertise one shared address, simplifying client configuration while route metrics and ECMP choose among instances and health-triggered withdrawal removes an unhealthy server. In the public-cloud case, the same property makes an address a poor locator: separate observers can reach separate provider edges for one IP, after which the provider carries traffic internally to a backend in another region.

This produces a dual effect. Anycast can improve locality, distribution, maintenance, and failure handling for the advertised service, yet systems that use endpoint latency to infer a unique downstream location can make systematically wrong choices. [[CloudflareSmartTieredCache]] therefore tests for physically implausible multi-checkpoint latency, avoids single-tier pinning when an origin seems anycast, and accepts explicit cloud-region context when the frontend address cannot identify the backend.

## Key Claims
- One shared address can hide a distributed set of answering locations and shift instance choice from applications or clients into routing.
- Route metrics, ECMP, and health-triggered withdrawal can provide locality, traffic distribution, and availability without changing the client-visible address.
- Latency to an anycast address measures the path to the answering edge, not necessarily the location or latency of a backend behind that edge.
- Multi-vantage measurements can reveal that one fixed endpoint location is physically implausible, but they do not by themselves identify the intended backend region.
- Systems layered on anycast need an explicit boundary between frontend reachability and backend placement, sometimes supplied through configuration or provider metadata.
- Availability depends on health semantics, withdrawal, convergence, capacity, and downstream state; address sharing alone does not prove resilience or performance.

## Evidence
- Shared-address DNS: [[tom-bowles-anycast-dns-part-1]] describes several servers advertising one DNS address, with route selection, ECMP, and health-aware withdrawal determining delivery.
- Operational simplification: [[tom-bowles-anycast-dns-part-1]] links the shared address to simpler DHCP, static configuration, ACLs, maintenance, and migration.
- Frontend/backend split: [[smart-tiered-cache-public-clouds]] explains that a cloud anycast IP represents the provider front end rather than one physical backend location.
- Location ambiguity: [[smart-tiered-cache-public-clouds]] shows how a Singapore backend can be reached through a Chicago cache tier selected from misleading frontend probe latency.
- Detection and response: [[smart-tiered-cache-public-clouds]] describes multi-checkpoint physical-latency tests, safe multi-tier fallback, and explicit cloud-region hints.

## Counterevidence & Qualifications
Both sources are favorable first-party or practitioner accounts rather than controlled evaluations. The DNS source does not measure route convergence, health-check errors, path stability, capacity during failure, or traffic balance. The Cloudflare source does not publish the anycast classifier, false-positive or false-negative rates, probe coverage, hairpin incidence, hint correctness, or before-and-after latency and cache efficiency. Regional unicast can create similar observation ambiguity without being anycast in the strict shared-global-prefix sense. Long-lived flows, stateful services, DDoS behavior, asymmetric paths, and provider-internal routing remain architecture-specific.

## What Changed
- Generalized the existing DNS-specific evidence into a shared-address routing concept.
- Added the distinction between latency to an advertised frontend and placement of a downstream backend.
- Added multi-vantage physical plausibility as an anycast-detection signal and explicit metadata as a location-recovery mechanism.

## Related Concepts
- [[AnycastDNS]] - applies anycast to shared-address DNS availability and distribution.
- [[NetworkLoadBalancing]] - anycast selects serving locations through routing rather than a conventional forwarding tier.
- [[ServiceHealthChecks]] - health state can control whether a location continues advertising the shared address.
- [[NetworkResilienceTradeoffs]] - locality and redundancy depend on convergence, capacity, state, and failure-domain choices.
- [[CloudflareSmartTieredCache]] - must distinguish the anycast frontend from the public-cloud backend region when choosing a cache tier.
