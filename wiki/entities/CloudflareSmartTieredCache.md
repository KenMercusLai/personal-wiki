---
title: "Cloudflare Smart Tiered Cache"
type: entity
tags: [cloudflare, caching, cdn, anycast, public-cloud]
sources:
  - smart-tiered-cache-public-clouds
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Overview
[[CloudflareSmartTieredCache]] is a [[Cloudflare]] tiered-caching product that selects upper-tier data centers between lower-tier edge caches and an origin, with public-cloud region hints for origins whose network addresses do not reveal one backend location.

## Current Profile
For a fixed unicast origin, the product probes latency from Cloudflare data centers and directs cache misses through one selected upper tier. That concentration can improve cache reuse and reduce requests and connections reaching the origin. An anycast or regional-unicast cloud front end breaks the location inference because different probes can terminate at different nearby provider edges even when the backend resides in one region.

The public-cloud extension lets an operator associate an origin IP with an AWS, GCP, Azure, or Oracle Cloud region. Cloudflare periodically joins provider IP-prefix files with upper-tier assignments derived from ongoing probes. Matching subnets cast weighted votes for the region's primary tier; the fallback is placed in another PoP. Where probe evidence is sparse, the system starts with the geographically closest Tier 1 PoP and can change to a data-backed choice as origins and observations accumulate.

The hint is configurable per IP or in bulk from the dashboard, as well as through API and Terraform. The dashboard restricts hints to origins Cloudflare has detected as anycast. The launch account describes the system and its intended effect, not measured customer outcomes.

## Key Characteristics
- Chooses one upper tier for clearly located origins so lower-tier misses share a concentrated cache before reaching the origin.
- Detects likely anycast answering through physically implausible combinations of multi-checkpoint probe latency.
- Falls back to several upper tiers when an origin address does not support confident single-location inference.
- Accepts explicit public-cloud region hints for AWS, GCP, Azure, and Oracle Cloud origins.
- Combines provider-prefix refreshes, 15-minute latency-derived assignments, and weighted subnet voting to select each region's tier.
- Places primary and fallback tiers in different PoPs and uses a Tier 1 geographic fallback when evidence is insufficient.
- Supports individual and bulk dashboard configuration plus API and Terraform workflows.

## Evidence
- Cache topology: [[smart-tiered-cache-public-clouds]] and its retained topology show lower tiers funneling misses through one upper tier before the origin.
- Ambiguous addressing: [[smart-tiered-cache-public-clouds]] explains why anycast and regional-unicast front ends make one IP appear near multiple Cloudflare data centers.
- Detection and safe fallback: [[smart-tiered-cache-public-clouds]] describes the speed-of-light test and the multi-upper-tier behavior used when a single location is not credible.
- Region configuration: [[smart-tiered-cache-public-clouds]] documents per-IP and bulk dashboard controls, API and Terraform support, and four launch providers.
- Selection and resilience: [[smart-tiered-cache-public-clouds]] describes periodic IP-range refresh, weighted subnet voting, 15-minute probe-data refresh, separate-PoP primary and fallback tiers, and geographic initialization for sparse regions.

## Qualifications
The only evidence is Cloudflare's launch post. It does not disclose the voting weights, confidence thresholds, checkpoint set, fiber-speed assumptions, provider-file failure handling, control-plane propagation delay, fallback-switch timing, or behavior under incorrect and stale hints. No dataset or before-and-after measurements substantiate the stated hit-ratio, origin-connection, latency, hairpin, availability, or adoption effects. Provider support and dashboard restrictions reflect the July 2026 launch state and may change.

## What Changed
- Created the product profile with the fixed-origin, ambiguous-anycast, and region-hinted selection modes.
- Added the provider-prefix and latency-vote pipeline, sparse-data geographic fallback, and separate-PoP resilience rule.
- Bounded the expected cache and latency benefits against the launch post's lack of outcome measurements.

## Relationships
- [[Cloudflare]] - operates the product, edge data centers, probes, configuration interfaces, and selection pipeline.
- [[AnycastRouting]] - creates the origin-location ambiguity the region hint addresses.
- [[NetworkLoadBalancing]] - selects and concentrates miss traffic at an upper tier rather than distributing all misses directly to origins.
- [[NetworkResilienceTradeoffs]] - balances cache concentration against multiple-tier safety and separate-PoP failover.
- [[AWS]] - supported launch provider whose region metadata can guide tier selection.
- [[ChenxiZhang]] - author of the source explaining the public-cloud extension.
