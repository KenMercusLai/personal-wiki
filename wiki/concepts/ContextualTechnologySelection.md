---
title: "Contextual Technology Selection"
type: concept
tags: [software-engineering, architecture, decision-making, tradeoffs]
sources:
  - you-are-not-google-bradfield
last_updated: 2026-09-22
knowledge_schema: synthesis-v1
---

## Definition
[[ContextualTechnologySelection]] is the practice of choosing a technical solution by comparing its design priorities, historical origin, costs, and scale assumptions with the adopter's actual problem rather than with the prestige of its creator.

## Current Synthesis
[[OzNova]] packages this practice as UNPHAT: understand the problem in its own domain, enumerate multiple solutions, read the relevant paper, recover the historical context, compare advantages with sacrificed properties, and think explicitly about fit. The last question - what fact would have to change to reverse the decision - turns an architectural preference into a falsifiable judgment.

The examples all distinguish a technology's quality from its suitability. Cassandra, Kafka, service-oriented architecture, GFS, and MapReduce addressed real availability, throughput, coordination, or data-volume pressures at Amazon, LinkedIn, and Google. A read-heavy 4 GB dataset, dozens of daily transactions, or a tiny team has a different problem. Rough orders of magnitude and workload shape are therefore decision inputs, not implementation details to consider after adopting the fashionable system.

## Key Claims
- Begin in the problem domain and establish workload, scale, availability, and organizational constraints before discussing products.
- Compare multiple candidates rather than treating a preferred tool as the default answer.
- Read primary design material and recover the historical problem that caused each solution to prioritize some properties over others.
- Evaluate disadvantages and deliberately deprioritized properties alongside advertised advantages.
- Use orders-of-magnitude estimates to test whether the adopter resembles the technology's motivating environment.
- Make the decision falsifiable by naming evidence that would change it.
- Reject prestige transfer: copying a successful company's architecture does not transfer the conditions or outcomes that made it successful.

## Evidence
- Decision process: [[you-are-not-google-bradfield]] defines UNPHAT as understanding, enumerating, reading, historicizing, weighing, and thinking about fit and disconfirming facts.
- Workload mismatch: [[you-are-not-google-bradfield]] contrasts Cassandra's write-availability origin with a read-heavy daily batch and Kafka's immense LinkedIn throughput with a few dozen valuable transactions per day.
- Quantitative check: [[you-are-not-google-bradfield]] notes that roughly 4 GB of data taking unexpectedly long to query points toward diagnosis and tuning before distributed replacement.
- Organizational context: [[you-are-not-google-bradfield]] places Amazon's service-oriented architecture move at approximately 7,800 employees and $3 billion in sales, unlike a startup dividing brochureware into tiny services.
- Originator behavior: [[you-are-not-google-bradfield]] says Google stopped using MapReduce for indexing once another approach fit better, demonstrating that provenance is not permanent endorsement.

## Counterevidence & Qualifications
The source is a polemical practitioner essay, not a controlled comparison of architecture outcomes, and its company-scale figures are illustrative snapshots rather than complete capacity models. Low present volume does not by itself rule out a distributed system: hard availability requirements, burst behavior, regulatory isolation, geographic distribution, expected growth, existing expertise, or managed-service economics may justify one. Historical context should constrain analogy without becoming a rule that only companies resembling the inventor may use the technology.

## What Changed
- Created the concept from UNPHAT and the article's Cassandra, Kafka, service-oriented architecture, and MapReduce mismatch examples.

## Related Concepts
- [[DistributedSystemRestraint]] - applies contextual selection specifically to the timing of distributed architecture.
- [[TechnologyStackComplexity]] - supplies the operational and reasoning costs that candidate comparison must count.
- [[BoringTechnology]] - favors mature tools when novelty has no contextual payoff.
- [[ToolFamiliarity]] - team experience is one local constraint that affects adoption cost and reliability.
- [[ArchitectureAlignmentForces]] - technology governance changes with the scope and coordination needs of the organization.
- [[DefaultTrialRetire]] - limits technology variety after candidate selection and experimentation.
- [[SystemReliability]] - availability and failure requirements can justify complexity that raw throughput cannot.
