---
title: "Infoblox"
type: entity
tags: [dns, networking, infrastructure]
sources:
  - tom-bowles-anycast-dns-part-1
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[Infoblox]] is a network-infrastructure vendor represented here through one customer's account of using its DNS platform with Anycast routing and service-health integration.

## Current Profile
In Bowles's account, Infoblox DNS servers can run a routing process that advertises a shared service address. Internal checks connect DNS-process health to route availability, withdrawing a server's Anycast route when DNS fails or is stopped. The source also says Infoblox can associate NTP with the same Anycast address, but it does not identify product versions, routing protocols, configuration, support boundaries, or measured behavior.

## Key Characteristics
- Supports a shared Anycast service address across multiple DNS servers in the described deployment.
- Couples internal DNS health with advertisement or withdrawal of the server's route.
- Is presented as enabling maintenance without manually changing client resolver configuration.
- Can reportedly associate NTP service with the DNS Anycast address.
- Appears through a favorable customer account rather than vendor documentation or comparative testing.

## Evidence
- User-community context: [[tom-bowles-anycast-dns-part-1]] says an Infoblox user group prompted evaluation of Anycast DNS.
- Route-health integration: [[tom-bowles-anycast-dns-part-1]] reports that internal health checks remove a server's route when its DNS process fails or is stopped.
- Multi-service claim: [[tom-bowles-anycast-dns-part-1]] says Infoblox can tie NTP to the same Anycast address used for DNS.

## Qualifications
All characteristics derive from a single customer's conceptual overview. The source provides no Infoblox documentation, version, configuration, routing-protocol detail, failover timing, failure test, comparison with alternatives, or independent verification.

## What Changed
- Created a bounded profile of Infoblox's role in the reported Anycast DNS deployment.

## Relationships
- [[TomBowles]] - customer-practitioner reporting the deployment.
- [[AnycastDNS]] - architecture the Infoblox servers implement in the account.
- [[ServiceHealthChecks]] - DNS-process status controls route availability in the described design.
- [[NetworkLoadBalancing]] - shared route advertisements distribute queries among service instances.
