---
title: "Anycast DNS"
type: concept
tags: [dns, anycast, routing, availability]
sources:
  - tom-bowles-anycast-dns-part-1
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[AnycastDNS]] is a DNS service architecture in which multiple distributed servers advertise the same client-visible IP address and the routing system directs a request toward the preferred reachable instance.

## Current Synthesis
The source reframes DNS high availability and distribution as a routing problem. Instead of giving clients several resolver addresses and depending on operating-system-specific ordering and retry behavior, each server advertises one shared host route. Route metrics select a nearby or otherwise preferred instance, while ECMP can share traffic across equally preferred paths.

The model simplifies the interface presented to clients, DHCP, static configurations, ACLs, and operators, but it transfers responsibility into the routing and health-integration layers. In the reported [[Infoblox]] deployment, internal DNS health checks withdraw an instance's route when DNS stops, permitting maintenance without changing the service address. That benefit depends on correct health semantics, advertisement withdrawal, routing convergence, and sufficient alternate capacity; the article measures none of them.

## Key Claims
- A shared service address removes the need for each client to choose consistently among multiple DNS server addresses.
- Network route selection can direct clients toward a preferred nearby instance, while ECMP can divide traffic across equally preferred instances.
- Health-triggered route withdrawal can remove a failed or maintained server from new-request routing without changing client configuration.
- One address reduces configuration and ACL sprawl, but concentrates correctness requirements in routing, health checks, and convergence.
- Distributed sites can spread or localize some attack traffic, but Anycast is not by itself detection, filtering, scrubbing, or proof of adequate capacity.
- The mechanism can apply beyond DNS when a service tolerates route changes and shared-address delivery.

## Evidence
- Client-policy shift: [[tom-bowles-anycast-dns-part-1]] contrasts heterogeneous client retry behavior with routing-system selection of a shared address.
- Shared-address topology: the retained diagram in [[tom-bowles-anycast-dns-part-1]] shows two clients following separate paths to nearby servers that all present `10.10.10.10`.
- Availability integration: [[tom-bowles-anycast-dns-part-1]] reports that Infoblox withdraws a server's route when internal checks detect that DNS has stopped.
- Distribution: [[tom-bowles-anycast-dns-part-1]] identifies route metrics and optional ECMP as the mechanisms for nearest-instance selection and load sharing.
- Operating simplification: [[tom-bowles-anycast-dns-part-1]] links one address to simpler DHCP, static configuration, ACLs, maintenance, and migration.
- Scope beyond DNS: [[tom-bowles-anycast-dns-part-1]] notes that the routing method is generic and reports NTP as another Infoblox use.

## Counterevidence & Qualifications
The evidence is one favorable first-person deployment overview rather than a design specification or controlled evaluation. It does not identify the routing protocol, define “nearest,” show how state or long-lived traffic behaves during route changes, quantify ECMP balance, measure withdrawal or convergence time, test false health decisions, or report remaining capacity during maintenance and failure. The DDoS discussion is especially bounded: route distribution may spread or shift traffic, but site selection, backbone capacity, filtering, attack direction, and convergence determine whether users remain served. A single shared address also becomes a common policy and configuration object even though the serving infrastructure is distributed.

## What Changed
- Created the concept as route-based DNS distribution rather than client-managed resolver failover.
- Added health-triggered withdrawal and routing convergence as coupled availability mechanisms.
- Qualified operational simplicity and DDoS mitigation against the source's missing measurements and implementation detail.

## Related Concepts
- [[NetworkLoadBalancing]] - Anycast distributes requests through route selection rather than a conventional proxy or packet-forwarding tier.
- [[ServiceHealthChecks]] - instance health must control whether a route remains eligible to receive requests.
- [[NetworkResilienceTradeoffs]] - path and site diversity reduce some failures while adding routing state, convergence, and shared-policy risks.
- [[DDoSTrafficMonitoring]] - monitoring and enforcement remain separate from Anycast's traffic-distribution effect.
