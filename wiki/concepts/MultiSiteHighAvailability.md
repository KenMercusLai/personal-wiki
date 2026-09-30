---
title: "Multi-Site High Availability"
type: concept
tags: [distributed-systems, high-availability, disaster-recovery, active-active]
sources:
  - kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[MultiSiteHighAvailability]] is the design of a service to continue or rapidly resume critical operation across machine, data-center, network, and city-scale failures by combining redundant serving stacks, traffic control, state replication, and tested failover boundaries.

## Current Synthesis
Kaito's architecture progression makes the protected failure boundary the organizing idea. Backups can recover data after an instance loss but leave restoration time and a data-loss window. Replicas reduce both; duplicating ingress and stateless applications removes more machine-level single points. A second same-city data center then protects against a facility outage, first as cold or hot standby and later as an active participant that continuously handles traffic.

Distance changes the design. Same-city active-active can tolerate some synchronous access to a primary site's storage, but the same topology becomes fragile across cities because every remote write inherits wide-area latency and link quality. Cross-city active-active therefore needs local read-write loops, writable state in each site, asynchronous cross-site convergence, deterministic traffic ownership, and a failover procedure that can move an affected partition without creating uncontrolled concurrent writers.

Multi-site expansion compounds replication paths. A mesh avoids one central relay but grows coordination complexity; a hub-and-spoke topology simplifies each site's synchronization responsibility while turning the hub and its promotion procedure into critical infrastructure. In every topology, the diagram is only a claim: achieved availability depends on data-loss bounds, lag, conflict handling, capacity, routing convergence, rehearsed failover, observability, and the ability of a surviving site to carry displaced load.

## Key Claims
- Availability improvement comes from reducing both failure exposure and recovery time, not from redundancy alone.
- Cold standby, hot standby, same-city active-active, cross-city active-active, and multi-site active-active protect different failure boundaries and have different readiness costs.
- Geographic distance makes synchronous cross-site calls and writes a latency and reliability hazard.
- Cross-city active-active requires local serving loops plus an explicit state-convergence and conflict-avoidance model.
- Expanding from two to many sites trades broader fault isolation and proximity for more replication, routing, capacity, and failover complexity.
- Recovery readiness must be exercised under real traffic and validated operationally; an idle mirror or architecture diagram is not sufficient evidence.

## Evidence
- Availability and recovery: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] connects MTBF and MTTR to permitted outage time and describes backups as slow, potentially incomplete recovery paths.
- Facility-level progression: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] contrasts cold standby, hot standby, and same-city active-active, including gradual traffic introduction to prove the second site.
- Distance boundary: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] estimates cross-city access at tens of milliseconds plus jitter or failure and rejects a topology that keeps remote writes on one primary site.
- Cross-city design: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] combines local read-write paths, bidirectional storage synchronization, eventual convergence, and routed ownership.
- Multi-site topology: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] contrasts a dense replication mesh with a center-mediated star and notes the center's higher stability requirement.

## Counterevidence & Qualifications
The evidence is one conceptual practitioner article, not an implementation specification, benchmark, incident study, or independent comparison. Its “true” active-active pattern is one eventual-consistency design, not a universal definition: strongly consistent global data may remain single-writer, other systems may partition state instead of copying everything, and consensus-based or managed multi-region databases impose different latency and availability tradeoffs. DNS changes, replication retry, and standby capacity do not by themselves guarantee bounded RTO or RPO. Cost, operational staffing, compliance, correlated dependencies, failback, split brain, and disaster exercises determine whether the added sites improve real reliability.

## What Changed
- Created a failure-boundary synthesis spanning standby, same-city active-active, cross-city active-active, and multi-site topologies.

## Related Concepts
- [[TrafficUnitization]] - assigns related traffic and writes to one local site to avoid cross-site conflicts.
- [[CloudHighAvailability]] - applies similar availability reasoning to zones, regions, routing, and datastore-specific recovery in cloud environments.
- [[SystemReliability]] - provides the broader code, architecture, operations, recovery, and organizational context.
- [[EventDrivenConsistency]] - supplies durable-event, retry, idempotency, lag, and repair concerns for asynchronous convergence.
- [[DistributedConsensus]] - alternative coordination family when replicas must agree on one ordered state rather than converge asynchronously.
- [[ReliabilityInvestment]] - multi-site capacity, middleware, exercises, and operations require sustained organizational commitment.
