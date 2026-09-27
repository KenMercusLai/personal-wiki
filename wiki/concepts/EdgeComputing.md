---
title: "Edge Computing"
type: concept
tags: [edge, distributed-systems, availability, latency, iot]
sources:
  - edge-computing-at-chick-fil-a-chick-fil-a-tech-blog-medium
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[EdgeComputing]] places compute and short-lived data processing close to the physical activity that generates and uses the data, primarily to reduce latency or preserve operation when wide-area connectivity fails.

## Current Synthesis
The Chick-fil-A case treats edge computing as a selective complement to cloud services, not a blanket replacement. A central control plane remains responsible for identity, routing, observability, and deployment, while each restaurant provides a small, replicated runtime for applications that must react to local demand and equipment state or continue through internet outages. The design's defining scale is a fleet of thousands of modest clusters rather than a few giant clusters.

The operational value comes from closing a local feedback loop. Cloud analytics can create a baseline forecast, but point-of-sale activity and equipment inventory reveal immediate conditions; local models merge both streams into a decision that can guide staff or automation. This benefit has costs: hardware and software must be managed across many sites, so edge placement should be limited to workloads whose availability or latency requirements justify that distributed estate.

## Key Claims
- Edge placement is justified by local availability and latency requirements, while cloud remains the default for workloads without those constraints.
- Cloud and edge can divide responsibilities: centralized services manage the fleet while local clusters execute site-sensitive applications.
- Local signals can correct centralized forecasts quickly enough to support operational decisions and automation.
- A fleet of many small clusters creates a different operational problem from a few high-density cloud clusters.
- Replication and temporary local retention can bridge connectivity loss before data is sent, aggregated, compressed, or discarded.
- Shared platform services let application teams use the edge without each rebuilding identity, messaging, telemetry, and deployment machinery.

## Evidence
- Placement rule: [[edge-computing-at-chick-fil-a-chick-fil-a-tech-blog-medium]] explicitly uses cloud first and edge only for applications requiring restaurant-level availability or latency.
- Closed-loop decisions: [[edge-computing-at-chick-fil-a-chick-fil-a-tech-blog-medium]] combines cloud forecasts with live sales and fryer inventory to adjust food-production guidance.
- Fleet architecture: [[edge-computing-at-chick-fil-a-chick-fil-a-tech-blog-medium]] describes more than 2,000 clusters with tens of containers each, multiple hosts, and redundant in-store networking.
- Outage behavior: [[edge-computing-at-chick-fil-a-chick-fil-a-tech-blog-medium]] retains replicated ephemeral data until connectivity returns and allows local aggregation, compression, or dropping.
- Platform boundary: [[edge-computing-at-chick-fil-a-chick-fil-a-tech-blog-medium]] assigns device identity, ingestion, telemetry, and GitOps-style deployment to cloud services while running MQTT, monitoring, microservices, and models locally.

## Counterevidence & Qualifications
The evidence is a company-authored 2018 case, not a controlled comparison with cloud-only or simpler local deployments. Its cost estimate, reliability rationale, planned fleet size, and projected device rollout are historically bounded and unverified. Edge infrastructure also adds distributed hardware, networking, security, upgrade, and observability responsibilities; the source acknowledges this indirectly through its cloud-first policy but does not quantify the total operating burden.

## What Changed
- Created the concept around physical-site computation, distinct from web-platform [[EdgeRuntime]] compatibility.

## Related Concepts
- [[InternetOfThingsData]] - local sensors and equipment state provide the signals edge applications process.
- [[CloudHighAvailability]] - edge clusters extend availability when access to centralized services is interrupted.
- [[SystemReliability]] - redundancy, replication, and recovery behavior determine whether local operation survives failures.
- [[ContainerNativePractice]] - well-behaved container workloads make a distributed application fleet easier to deploy and reconcile.
- [[EdgeRuntime]] - related use of proximity, but focused on constrained web execution environments rather than on-premises physical operations.
