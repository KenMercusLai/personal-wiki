---
title: "Distributed System Restraint"
type: concept
tags: [software-architecture, startups, operations]
sources:
  - appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby
  - architecting-for-continuous-delivery-thoughtworks
  - you-are-not-google-bradfield
last_updated: 2026-09-22
knowledge_schema: synthesis-v1
---

## Definition
[[DistributedSystemRestraint]] is the practice of delaying distributed architecture until product needs, team size, and operational capacity justify the extra coordination and failure-mode complexity.

## Current Synthesis
The Appcanary source argues that distributed systems impose expensive complexity on small teams. Architecture should reflect a team's organization and ability to coordinate, so early startups should avoid distributed systems as long as they can and spend their scarce attention on product and business learning.

The same restraint applies inside monolith decomposition. Runtime services can improve autonomy, cycle time, independent deployment, and scaling, but only when the organization is mature enough to use microservices effectively. The restraint is therefore not anti-service; it is a timing and readiness rule.

Nova adds a quantitative and historical test for readiness. Cassandra's write-availability priorities, Kafka's LinkedIn-scale throughput, Amazon's service-oriented organization, and Google's web-scale data processing each arose from particular constraints. A roughly 4 GB read-heavy dataset, dozens of daily transactions, or a tiny organization does not inherit those constraints merely by adopting the same tool. Restraint therefore requires comparing orders of magnitude and workload shape, not simply preferring a monolith by default.

## Key Claims
- Distributed systems add complexity that small teams may not be able to pay.
- Microservices are more appropriate when architecture matches a larger team's coordination structure.
- Deployment style should reflect organizational capacity, not architectural fashion.
- Avoiding distributed systems protects scarce startup attention for the business problem.
- Simpler architecture is a strategic choice only when it preserves enough product capability.
- Service extraction can be the right CD move when boundaries and organizational readiness support it.
- Distributed-system restraint should be revisited when workload, availability, geographic, or organizational evidence makes distribution's benefits exceed its costs.

## Evidence
- Complexity warning: [[appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby]] says distributed systems introduce expensive complexity.
- Team-fit principle: [[appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby]] says coding and deployment should reflect the team's organization and ability to coordinate.
- Startup focus: [[appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby]] links architecture restraint to solving a business problem under time pressure.
- Positive service case: [[architecting-for-continuous-delivery-thoughtworks]] says services can provide autonomy, independent deployment, and independent scaling.
- Readiness gate: [[architecting-for-continuous-delivery-thoughtworks]] says microservices are not free and require enough organizational maturity.
- Scale mismatch: [[you-are-not-google-bradfield]] contrasts Kafka's LinkedIn-scale event stream and Amazon's service-oriented organization with adopters handling only dozens of daily transactions or a small application.
- Workload mismatch: [[you-are-not-google-bradfield]] argues that Cassandra's write-availability priorities did not fit a read-heavy system performing one large daily write.
- Originator revision: [[you-are-not-google-bradfield]] says Google stopped using MapReduce to build its index when the tool no longer fit, showing that restraint includes replacing a once-appropriate architecture.

## Counterevidence & Qualifications
The sources do not argue that distributed systems or microservices are always wrong. Their shared claim is stage-sensitive: defer them until their benefits outweigh the cost for the team that must operate them, but consider them when monolithic structure is itself blocking delivery feedback, ownership, and throughput. Nova's figures are illustrative rather than a capacity model, and low throughput alone cannot dismiss hard availability, isolation, geographic, burst, or growth requirements.

## What Changed
- Created the concept from Appcanary's warning against premature distributed systems.
- Added Thoughtworks' service-extraction qualification for continuous-delivery bottlenecks.
- Added workload shape, order-of-magnitude comparison, and originator-revision tests from "You Are Not Google."

## Related Concepts
- [[MicroserviceOperationalOverhead]] - microservice cost is one concrete form of distributed-system burden.
- [[TechnologyStackComplexity]] - distributed architecture adds operational and reasoning complexity.
- [[StartupFocus]] - restraint preserves attention for product and business learning.
- [[SystemReliability]] - distributed systems expand failure modes and recovery obligations.
- [[MonolithConsolidation]] - consolidation can be a response when distributed boundaries become too costly.
- [[CDComponentization]] - componentization can use services when readiness supports the added distribution.
- [[ContinuousDelivery]] - delivery bottlenecks can justify revisiting architecture restraint.
- [[ContextualTechnologySelection]] - supplies the historical, quantitative, and falsifiable method for deciding when restraint should end.
