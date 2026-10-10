---
title: "Namespace"
type: entity
tags: [continuous-integration, infrastructure, bare-metal, data-center]
sources:
  - so-you-want-to-build-your-own-datacenter
last_updated: 2026-10-10
knowledge_schema: synthesis-v1
---

## Overview
[[Namespace]] is a developer-infrastructure company represented here through its first-party account of building a vertically integrated platform for isolated, ephemeral CI jobs.

## Current Profile
Namespace says it began on [[AWS]] `z1d.metal`, later used Equinix Metal and other bare-metal providers, and by early 2024 ran more than 95% of its platform on owned infrastructure across several US and European locations. Its platform couples hypervisor and scheduler control with workload-specific compute, local storage, network fabric, cache snapshots, image management, IP space, transit relationships, and physical capacity planning.

The unifying design choice is [[BuildOptimizedInfrastructure]] rather than general-purpose production hosting. Namespace selects high-clock CPUs, local NVMe, and 25–100 Gbit inter-node links for bursty, I/O-heavy builds; its [[TopologyAwareBuildCaching]] routes a job to an existing cache revision and attaches a snapshot just in time. That integration may improve build latency and price-performance, but it also transfers procurement, power, cooling, forecasting, network, facility, and recovery work to the company.

## Key Characteristics
- Operates a vertically integrated CI platform spanning orchestration, compute, storage, caching, networking, and facilities.
- Designs hardware around build critical paths, local I/O, burst utilization, and platform-specific processor performance.
- Uses uniform rack designs with compute-, memory-, and storage-oriented servers plus redundant top-of-rack switching and out-of-band management.
- Couples topology-aware cache revisions with scheduler placement to avoid repeated archive download, extraction, packing, and upload.
- Accepts advance capacity planning and specialized physical operations in exchange for control over performance, economics, and network identity.

## Evidence
- Platform scope: [[so-you-want-to-build-your-own-datacenter]] says owning the hypervisor led Namespace to build orchestration, scheduling, storage, image management, and supporting hardware.
- Hardware fit: [[so-you-want-to-build-your-own-datacenter]] describes high-frequency AMD EPYC, Apple Silicon, Macs, many NVMe drives, and network links up to 100 Gbit for build workloads.
- Rack and network design: [[so-you-want-to-build-your-own-datacenter]] describes two top-of-rack switches, an out-of-band management switch, three server roles, Clos topology, controlled IP ranges, and direct transit peering.
- Cache locality: [[so-you-want-to-build-your-own-datacenter]] says the scheduler tracks cache revisions by node and attaches topology-aware snapshots to ephemeral jobs.
- Operating trade-off: [[so-you-want-to-build-your-own-datacenter]] reports three data-center design revisions and continuing difficulties with power balance, procurement, forecasting, physical contingencies, and networking.

## Qualifications
The profile is based on one company-authored engineering article. It supplies no independent verification, reproducible benchmark, direct cost model, uptime history, capacity figures, customer outcomes, scheduler specification, or incident record. “More than 95%” does not define the remaining workload or denominator, and the claimed performance multiples are not separated by instance, compiler, repository, cache state, or job type. The account therefore establishes Namespace's stated architecture and rationale, not general superiority over hyperscalers or rented bare metal.

## What Changed
- Established Namespace as a workload-specific, vertically integrated CI infrastructure operator.
- Recorded cache-locality scheduling and owned network control as core differentiators.
- Made physical capacity planning and operational responsibility explicit limits on the model.

## Relationships
- [[BuildOptimizedInfrastructure]] - Namespace's hardware and facility strategy is organized around CI workload shape.
- [[TopologyAwareBuildCaching]] - Namespace's scheduler and snapshot layer implement node-local cache reuse.
- [[DataCenterNetworkFabric]] - Clos topology and known link capacity support placement of data-moving jobs.
- [[CloudCostOptimization]] - Namespace trades managed-cloud convenience and elasticity for workload-specific price-performance and operator responsibility.
- [[AWS]] - Namespace's initial `z1d.metal` platform and reference point for its unit-economics argument.
- [[DigitalOcean]] - prior infrastructure experience credited to a Namespace team member.
