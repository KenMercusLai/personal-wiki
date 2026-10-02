---
title: "Tom Bowles"
type: entity
tags: [networking, dns, author]
sources:
  - tom-bowles-anycast-dns-part-1
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[TomBowles]] is a network practitioner represented here through a first-person account of adopting [[AnycastDNS]] for a distributed DNS deployment.

## Current Profile
The available source presents Bowles as an operator who learned about Anycast DNS through an [[Infoblox]] user group, examined the design, implemented it, and judged the result favorably. His article focuses on the motivation and operating model; the promised implementation details are deferred to a second part that is not included in this evidence set.

## Key Characteristics
- Writes from direct implementation experience rather than presenting a vendor-neutral benchmark.
- Favors moving resolver selection, availability, and traffic distribution from clients into routing infrastructure.
- Emphasizes operational simplicity, predictable maintenance, and reuse of existing infrastructure.
- Distinguishes the generic Anycast routing method from its DNS application.

## Evidence
- Adoption path: [[tom-bowles-anycast-dns-part-1]] says an Infoblox user group prompted Bowles to evaluate and later implement Anycast DNS.
- Architecture position: [[tom-bowles-anycast-dns-part-1]] argues that route selection is more predictable than heterogeneous client resolver behavior.
- Operating priorities: [[tom-bowles-anycast-dns-part-1]] highlights a single client-visible address, health-triggered withdrawal, daytime maintenance, and more even request distribution.

## Qualifications
This profile comes from one practitioner article and does not establish Bowles's employer, exact topology, routing protocol, deployment scale beyond four referenced servers, or independently measured results. Part 1 omits the implementation details promised for Part 2.

## What Changed
- Created a source-bounded profile of Bowles as an Anycast DNS practitioner-author.

## Relationships
- [[AnycastDNS]] - Bowles advocates the architecture based on his deployment experience.
- [[Infoblox]] - the user community and platform context for his implementation.
- [[NetworkLoadBalancing]] - his design shifts DNS request distribution into network route selection.
