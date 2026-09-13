---
title: "Distributed System Restraint"
type: concept
tags: [software-architecture, startups, operations]
sources:
  - appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[DistributedSystemRestraint]] is the practice of delaying distributed architecture until product needs, team size, and operational capacity justify the extra coordination and failure-mode complexity.

## Current Synthesis
The Appcanary source argues that distributed systems impose expensive complexity on small teams. Architecture should reflect a team's organization and ability to coordinate, so early startups should avoid distributed systems as long as they can and spend their scarce attention on product and business learning.

## Key Claims
- Distributed systems add complexity that small teams may not be able to pay.
- Microservices are more appropriate when architecture matches a larger team's coordination structure.
- Deployment style should reflect organizational capacity, not architectural fashion.
- Avoiding distributed systems protects scarce startup attention for the business problem.
- Simpler architecture is a strategic choice only when it preserves enough product capability.

## Evidence
- Complexity warning: [[appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby]] says distributed systems introduce expensive complexity.
- Team-fit principle: [[appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby]] says coding and deployment should reflect the team's organization and ability to coordinate.
- Startup focus: [[appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby]] links architecture restraint to solving a business problem under time pressure.

## Counterevidence & Qualifications
The source does not argue that distributed systems or microservices are always wrong. Its claim is stage-sensitive: defer them until their benefits outweigh the cost for the team that must operate them.

## What Changed
- Created the concept from Appcanary's warning against premature distributed systems.

## Related Concepts
- [[MicroserviceOperationalOverhead]] - microservice cost is one concrete form of distributed-system burden.
- [[TechnologyStackComplexity]] - distributed architecture adds operational and reasoning complexity.
- [[StartupFocus]] - restraint preserves attention for product and business learning.
- [[SystemReliability]] - distributed systems expand failure modes and recovery obligations.
- [[MonolithConsolidation]] - consolidation can be a response when distributed boundaries become too costly.
