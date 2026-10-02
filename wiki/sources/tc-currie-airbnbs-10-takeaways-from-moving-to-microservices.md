---
title: "Airbnb's 10 Takeaways from Moving to Microservices"
type: source
tags: [microservices, devops, airbnb, continuous-delivery]
date: 2017-10-03
source_file: "/mnt/ken_personal_wiki/Articles/TC Currie - Airbnb's 10 Takeaways from Moving to Microservices.md"
---

## Summary
[[TCCurrie]] reports [[MelanieCebula]]'s FutureStack 2017 account of [[Airbnb]] moving from a large Ruby on Rails monolith toward microservices while retaining the monolith during the transition. The ten lessons join monolith-first timing, engineer production ownership, configuration and alerts as code, standardized monitoring, automated delivery, and one-request service creation into a platform-and-culture program rather than a service-count goal. The source reports substantial 2017 scale but provides no comparative reliability, productivity, cost, or migration-outcome data.

## Key Claims
- Start with a monolith while product and infrastructure needs are still uncertain; Airbnb began investing in services when its Rails application reached about 500,000 lines and was reportedly doubling each year.
- [[DevOpsCulture]] requires engineers to deploy, observe, and recover their own changes, supported by open SysOps training, incident triage, coordination, and communication rather than responsibility without enablement.
- Configuration, metrics, and alerts should live in reviewable code so production state, changes, rollback, and business-level monitoring are visible to developers.
- [[ContinuousDelivery]] across many services depends on standardized, automated creation, testing, packaging, deployment, monitoring, and defaults that make the safe path the easy path.
- Early extracted services should be treated as learning artifacts; the source expects initial designs to be poor and cites Netflix's roughly ten-year transition as a warning against short migration expectations.
- Breaking apart the remaining monolith requires product-team participation and organization-wide investment after shared infrastructure demonstrates a credible delivery advantage.
- The section titled “Services Own Their Data” does not actually explain database or data ownership; its prose instead describes “Democratic Deploys,” where developers own feature deployment, monitoring, rollback, abort, and reversion.

## Key Quotes
> "Don't start with a microservices." - Cebula's monolith-first advice as reported by Currie.

> "So the easy thing is the right thing for developers." - on standardized formats and defaults.

## Connections
- [[TCCurrie]] - author of the conference report.
- [[MelanieCebula]] - Airbnb engineer whose FutureStack talk supplies the ten lessons.
- [[Airbnb]] - company case for a long-running monolith-to-services transition.
- [[DevOpsCulture]] - production authority, on-call learning, and shared incident response are cultural prerequisites.
- [[MicroservicePlatformEngineering]] - standardized configuration, monitoring, alerting, delivery, and service creation form a shared platform layer.
- [[ContinuousDelivery]] - automation and consistent deployment behavior are presented as prerequisites for service proliferation.
- [[IncrementalMonolithMigration]] - the transition begins alongside a retained monolith and later requires product-team-led extraction.
- [[ConfigurationManagement]] - configuration and alerts are made reviewable and reversible through code.
- [[ServiceObservability]] - standard monitoring plus developer-authored business metrics supports production ownership.
- [[ProductionOwnership]] - developers are expected to deploy, monitor, abort, roll back, or revert their own changes.

## Contradictions
- The source complements [[ModularMonolith]] and [[DistributedSystemRestraint]] by rejecting microservices as a starting default, while using rapid monolith growth as Airbnb's context-specific signal to invest in service infrastructure.
- Its “Services Own Their Data” heading is internally unsupported: the associated text concerns developer ownership of feature delivery and recovery, not service-owned databases or write boundaries.
- The reported 3,500 weekly microservice deploys, 75,000 annual production deploys, 900 engineers, and three-engineers-per-service ratio are historical conference claims without definitions, denominators, trend data, or independent verification.

## Image Notes
All five effective local images were opened. The building and speaker photographs were decorative; the ten-takeaway slide, SysOps diagram, and Democratic Deploys slide repeated prose-visible information without adding legible architecture, measurement, or workflow evidence, so none was retained.
