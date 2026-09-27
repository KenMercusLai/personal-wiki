---
title: "Edge Computing at Chick-fil-A"
type: source
tags: [edge-computing, kubernetes, iot, restaurants]
date: 2018-07-30
source_file: "/mnt/ken_personal_wiki/Articles/Edge Computing at Chick-fil-A - Chick-fil-A Tech Blog - Medium.md"
---

## Summary
The [[ChickFilA]] IoT/Edge team explains why the restaurant company built a distributed [[Kubernetes]] platform for low-latency, internet-independent applications rather than treating edge infrastructure as an end in itself. Its 2018 architecture kept higher-order control services in the cloud while using more than 2,000 planned restaurant clusters to combine cloud forecasts with live point-of-sale and equipment data, retain ephemeral data through outages, and support local automation. The case frames [[EdgeComputing]] as a selective fallback for availability and latency requirements inside a broader cloud-first strategy.

## Key Claims
- [[EdgeComputing]] puts compute near restaurant operations when low latency, high availability, or continued operation during internet loss is essential; the source still prefers cloud deployment when those constraints do not apply.
- Local decision-making can improve cloud forecasts by combining them with real-time point-of-sale keystrokes, equipment state, and work-in-progress inventory.
- The target topology was unusual in breadth rather than per-cluster size: more than 2,000 restaurant clusters with tens of containers each, connected through redundant in-store network infrastructure.
- The cloud control plane handled device identity, data ingestion and routing, telemetry, and GitOps-style deployment management, while restaurant clusters ran authentication, MQTT messaging, log and monitoring agents, microservices, and machine-learning models.
- Edge data was mostly ephemeral but replicated across nodes so a restaurant could retain it during an outage, then exfiltrate, aggregate, compress, or discard it according to business need.
- An owned, open IoT platform let internal teams and partners reuse security, identity, connectivity, onboarding, and messaging capabilities instead of adopting disconnected vendor silos.
- Commodity hardware costing roughly $1,000 per restaurant and multiple physical hosts supported incremental capacity and the no-single-point-of-failure goal, although the economics and reliability figures are company-reported.
- [[Kubernetes]] was chosen to preserve desired replicas and speed production delivery, not because adopting fashionable infrastructure was itself valuable.

![Chick-fil-A edge architecture linking cloud control services, a Kubernetes-based restaurant platform, and connected devices](../../wiki-assets/edge-computing-at-chick-fil-a-chick-fil-a-tech-blog-medium/restaurant-edge-architecture.png)

![Diagram contrasting a few very large clusters with Chick-fil-A's geographically distributed fleet of small restaurant clusters](../../wiki-assets/edge-computing-at-chick-fil-a-chick-fil-a-tech-blog-medium/distributed-restaurant-clusters.png)

## Key Quotes
> "Edge Computing" is the idea of putting compute resources close to the action. - defining the deployment model.

> "The simplest possible solution is usually the best solution." - limiting Kubernetes advocacy to contexts where its capabilities are needed.

## Connections
- [[ChickFilA]] - restaurant company and operator of the described IoT and edge platform.
- [[EdgeComputing]] - central architecture pattern for local availability, latency, data handling, and automation.
- [[Kubernetes]] - orchestration layer used across the cloud control plane and restaurant clusters.
- [[InternetOfThingsData]] - equipment and point-of-sale signals become inputs to local decisions and automation.
- [[ContainerNativePractice]] - containers provide dependency isolation, testing consistency, resource controls, and autonomous delivery.
- [[CloudHighAvailability]] - the edge design extends availability into restaurants rather than relying on cloud connectivity alone.
- [[SystemReliability]] - multiple hosts, replicated data, redundant networking, and replica reconciliation remove single points of failure.

## Contradictions
- The case qualifies [[Kubernetes]] restraint rather than contradicting it: thousands of intermittently connected sites with local availability requirements differ from workloads that fit a simpler managed container platform.
- The rollout beyond 2,000 clusters, more than 100,000 connected devices, and related benefits were plans stated in 2018, not independently verified outcomes or current architecture.
- The retained diagrams are only 60 pixels wide in the source export, so their broad topology is visible but most labels cannot be independently read; the detailed component account therefore comes from the article text.
