---
title: "Service Observability"
type: concept
tags: [observability, monitoring, logging, operations]
sources:
  - a-look-at-auth0-cloud-architecture-5-years-in
  - asanas-september-8-outage
  - blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ServiceObservability]] is the operational ability to understand service health and behavior through metrics, probes, alarms, dashboards, logs, audit trails, and escalation channels.

## Current Synthesis
The Auth0 source presents observability as a layered operating system for a production SaaS. CloudWatch covers AWS-generated metrics such as load-balancer errors, target-group health, and SQS delays. DataDog stores and monitors time-series metrics from hosts, AWS resources, off-the-shelf services, and custom services. Pingdom probes continuously exercise core functionality, while Kibana and SumoLogic divide application logs, service logs, audit trails, and AWS-generated logs.

Alert routing is part of the design. CloudWatch alarms usually route through PagerDuty to Slack and phones; DataDog alerts usually go to Slack, with PagerDuty reserved for issues likely to wake people because they are customer-impacting. The future work points to observability as an automation target: standard metric naming, generated dashboards, generated monitors, and log-derived metrics can reduce manual dashboard and monitor maintenance.

Asana's outage shows the failure mode of partial or misleading observability. The first signals pointed to search indexing lag and API downtime, while the team initially suspected the database even though the databases were underloaded. Customer support supplied the decisive user-impact signal, and the separate dogfooding environment masked employee-visible severity because it ran on different AWS EC2 instances from production.

Balakrishnan's Delos source adds a design-placement rule for infrastructure systems. Observability should live above APIs and outside implementations where possible, so teams can switch implementations and compare behavior without embedding measurement bugs in each implementation. It also warns that hard-to-measure properties such as consistency are easy to forget unless critical checks are pushed into deployment itself.

## Key Claims
- Observability should combine infrastructure metrics, service metrics, external probes, logs, audit trails, and escalation policy.
- Different monitoring tools can have distinct roles: provider metrics, time-series service metrics, external checks, and log analysis.
- Alert routing should distinguish informational signals from customer-impacting pages.
- Low-level metrics and high-level service states both matter for operating distributed systems.
- Manual metric and dashboard work becomes a scaling problem as the service mesh and engineering organization grow.
- Observability must connect internal alerts to customer impact, because healthy internal or dogfooding environments can hide production-only overload.
- Swappable infrastructure benefits from implementation-independent observability and deployment-integrated checks for hard-to-measure correctness properties.

## Evidence
- Provider metrics: [[a-look-at-auth0-cloud-architecture-5-years-in]] uses CloudWatch for AWS-generated alarms such as load-balancer HTTP errors, unhealthy targets, and SQS delays.
- Service metrics: [[a-look-at-auth0-cloud-architecture-5-years-in]] uses DataDog for host, AWS, NGINX, MongoDB, and custom-service time-series metrics.
- External probes: [[a-look-at-auth0-cloud-architecture-5-years-in]] says Pingdom probes run every minute to check core functionality.
- Logs and audit trails: [[a-look-at-auth0-cloud-architecture-5-years-in]] describes Kibana for application and service logs and SumoLogic for audit trails and AWS-generated logs.
- Escalation policy: [[a-look-at-auth0-cloud-architecture-5-years-in]] routes likely customer-impacting alerts to PagerDuty while sending broader alerts to Slack.
- Misleading symptoms: [[asanas-september-8-outage]] says the first page came from search-indexer lag and the next from API downtime, while the actual bottleneck was web-server CPU saturation.
- Customer-impact escalation: [[asanas-september-8-outage]] says customer support told on-call engineers that users were unable to use the app after the initial investigation underestimated severity.
- Environment gap: [[asanas-september-8-outage]] says engineers used a dogfooding version on different AWS EC2 instances that were not overloaded, making the incident harder to perceive internally.
- Implementation-independent measurement: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says observability should be above APIs and external to implementations where possible.
- Comparison support: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says this placement helps teams switch implementations and compare performance without measurement-code bugs.
- Correctness checks: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says difficult-to-measure attributes such as consistency require special attention and that critical checks should be pushed into deployment when possible.

## Counterevidence & Qualifications
The sources list tools and examples rather than a full observability taxonomy. Auth0 admits fragmentation: it was evaluating centralizing logging and automating metrics because manual dashboards and multiple providers had become operational overhead. Asana's postmortem is a single incident account, but it usefully shows that pages and dashboards can still mislead when they do not make user impact and environment differences obvious. Balakrishnan's placement rule is strongest for infrastructure with multiple implementations; simpler applications may not need the same abstraction boundary.

## What Changed
- Created the concept from Auth0's monitoring, alerting, logging, and metrics practices.
- Added Asana's outage as a case where partial signals, dogfooding divergence, and customer-support escalation shaped diagnosis.
- Added Delos-derived guidance on implementation-independent observability and deployment-integrated correctness checks.

## Related Concepts
- [[SystemReliability]] - observability reveals reliability problems and supports response.
- [[ChangeSafety]] - release safety depends on monitoring, alerts, and rollback signals.
- [[DeploymentAutomation]] - deployments need pre/post checks and production visibility.
- [[CloudHighAvailability]] - availability mechanisms need metrics and alerts to detect failover conditions.
- [[InternalDeveloperPlatform]] - platform defaults can standardize metrics, logs, dashboards, and monitors.
- [[FailureOwnership]] - postmortems use observability gaps to improve future detection and triage.
- [[ProductionInfrastructureLeadership]] - infrastructure leaders decide where observability lives relative to APIs and implementations.
