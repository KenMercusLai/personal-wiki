---
title: "Multi-Site High Availability"
type: concept
tags: [distributed-systems, high-availability, disaster-recovery, active-active]
sources:
  - kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le
  - nick-craver-stack-overflow-the-architecture-2016-edition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[MultiSiteHighAvailability]] is the design of a service to continue or rapidly resume critical operation across machine, data-center, network, and city-scale failures through redundant serving paths, state replication, traffic control, and tested failover boundaries.

## Current Synthesis
Kaito's progression makes the protected failure boundary the organizing idea. Backups preserve data but leave restoration time and a data-loss window; replicas, duplicate ingress, and stateless application copies progressively remove machine-level single points. Same-city and cross-city sites add facility and regional protection, but distance makes synchronous remote access a latency and reliability hazard. Cross-city active-active therefore needs local serving loops, writable local state or explicit ownership, asynchronous convergence, and conflict controls.

Stack Overflow's 2016 topology supplies a bounded implementation example rather than full active-active proof. New York had paired racks, dual power and network connections, four ISPs and routers, and a Colorado disaster-recovery site. A 10 Gbps MPLS path supported replication and recovery bursts, while two OSPF routes through the ISPs were higher-cost failovers. SQL replicas in Colorado were asynchronous and masters carried most load, so the design protected multiple path and facility failures without claiming zero lag, zero recovery time, or simultaneous write activity at both sites.

Multi-site expansion compounds routing, replication, capacity, and operational complexity. A mesh increases synchronization paths; a hub reduces per-site coordination while making hub promotion critical. In every topology, redundancy is evidence only when capacity, lag, routing convergence, conflict behavior, recovery objectives, and failover exercises are known.

## Key Claims
- Availability improvement comes from reducing both failure exposure and recovery time, not from duplicate hardware alone.
- Cold standby, hot standby, same-city active-active, cross-city active-active, and disaster-recovery replicas protect different boundaries.
- Geographic distance makes synchronous cross-site calls and writes a latency and link-reliability hazard.
- Alternate links and asynchronous replicas improve survivability but do not imply zero recovery time, zero data loss, or active-active state mutation.
- Cross-city active-active requires local serving loops plus explicit state ownership, convergence, and conflict prevention.
- Real readiness depends on surviving-site capacity, routing convergence, observability, and rehearsed failover.

## Evidence
- Architecture progression: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] contrasts backups, cold and hot standby, same-city active-active, cross-city active-active, and multi-site topologies.
- Distance boundary: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] rejects distant application paths that still depend on synchronous remote storage access.
- Local redundancy: [[nick-craver-stack-overflow-the-architecture-2016-edition]] describes paired racks, dual power feeds, dual 10 Gbps connectivity, four ISPs, router pairs, and redundant application tiers in New York.
- Inter-site routing: [[nick-craver-stack-overflow-the-architecture-2016-edition]] describes one preferred MPLS path and two higher-cost OSPF failover routes between New York and Colorado.
- State recovery: [[nick-craver-stack-overflow-the-architecture-2016-edition]] places asynchronous SQL replicas and separate Elasticsearch clusters in Colorado rather than claiming synchronous dual-site writes.
- Multi-site state design: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] contrasts replication meshes with a hub-and-spoke design and its critical-center promotion requirement.

## Counterevidence & Qualifications
The evidence combines one conceptual practitioner guide with one first-party 2016 architecture snapshot. Neither publishes failover-test results, route-convergence times, measured replication lag, RTO, RPO, or incident outcomes. “Everything is redundant” should not be read literally: Stack Overflow's preferred MPLS route was one link with alternates, its SQL replicas were asynchronous, and normal state ownership remained master-centered. Active-active is not one universal consistency model; strongly consistent or global data can require different ownership, consensus, partitioning, or managed-database tradeoffs.

## What Changed
- Added Stack Overflow as a concrete disaster-recovery topology with layered local redundancy, alternate inter-site routes, and asynchronous replicas.
- Sharpened the distinction between redundant paths, disaster-recovery readiness, and true multi-writer active-active operation.

## Related Concepts
- [[TrafficUnitization]] - assigns related traffic and writes to one local site to avoid cross-site conflicts.
- [[CloudHighAvailability]] - applies similar failure-boundary reasoning to zones, regions, and managed data stores.
- [[SystemReliability]] - supplies the broader architecture, operations, recovery, and organizational context.
- [[EventDrivenConsistency]] - addresses retry, idempotency, lag, and repair for asynchronous convergence.
- [[DistributedConsensus]] - coordinates one ordered state when asynchronous convergence is insufficient.
- [[ProductionCapacityBuffer]] - provides headroom for displaced traffic and degraded operation.
