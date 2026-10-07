---
title: "Service Observability"
type: concept
tags: [observability, monitoring, logging, operations]
sources:
  - a-look-at-auth0-cloud-architecture-5-years-in
  - asanas-september-8-outage
  - blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database
  - details-on-the-january-9th-2017-asana-outage
  - rule-11-reader-learning-from-the-post-mortem
  - dang-agent-zou-xiang-sheng-chan-infra-mian-lin-na-xie-tiao-zhan
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[ServiceObservability]] is the operational ability to understand service health and behavior through metrics, probes, alarms, dashboards, logs, audit trails, and escalation channels.

## Current Synthesis
The Auth0 source presents observability as a layered operating system for a production SaaS. CloudWatch covers AWS-generated metrics such as load-balancer errors, target-group health, and SQS delays. DataDog stores and monitors time-series metrics from hosts, AWS resources, off-the-shelf services, and custom services. Pingdom probes continuously exercise core functionality, while Kibana and SumoLogic divide application logs, service logs, audit trails, and AWS-generated logs.

Alert routing is part of the design. CloudWatch alarms usually route through PagerDuty to Slack and phones; DataDog alerts usually go to Slack, with PagerDuty reserved for issues likely to wake people because they are customer-impacting. The future work points to observability as an automation target: standard metric naming, generated dashboards, generated monitors, and log-derived metrics can reduce manual dashboard and monitor maintenance.

Asana's outage shows the failure mode of partial or misleading observability. The first signals pointed to search indexing lag and API downtime, while the team initially suspected the database even though the databases were underloaded. Customer support supplied the decisive user-impact signal, and the separate dogfooding environment masked employee-visible severity because it ran on different AWS EC2 instances from production.

Asana's January capacity incident adds an actionability boundary. Other provisioning-job copies noticed that they could not acquire the lock and timed out, but those alerts did not page and went unnoticed over the weekend. The system therefore emitted evidence of a stuck capacity-control path without converting that evidence into timely human attention.

Balakrishnan's Delos source adds a design-placement rule for infrastructure systems. Observability should live above APIs and outside implementations where possible, so teams can switch implementations and compare behavior without embedding measurement bugs in each implementation. It also warns that hard-to-measure properties such as consistency are easy to forget unless critical checks are pushed into deployment itself.

White adds post-incident reconstruction as a way to improve this operating system. Teams should map how a failure moved from occurrence to detection, identify where it could have surfaced earlier, and evaluate lower dwell time against the collateral cost of false positives. Mapping the troubleshooting path then reveals what evidence was hard to find and what instrumentation could shorten diagnosis next time.

For autonomous agents, Ci Jian De Shan Lin extends observability beyond service diagnosis. If people cannot inspect every action, traces must support heterogeneous verification, prove what happened, attribute decisions and effects, and enable replay or review of failures. Observability then becomes [[AccountabilityInfrastructure]]: not only a way to operate the system, but part of the evidence that makes machine-scale autonomous action socially and organizationally governable.

## Key Claims
- Observability should combine infrastructure metrics, service metrics, external probes, logs, audit trails, and escalation policy.
- Different monitoring tools can have distinct roles: provider metrics, time-series service metrics, external checks, and log analysis.
- Alert routing should distinguish informational signals from pages, escalate control-plane failures that can predict later customer impact, and balance shorter detection dwell time against false-positive cost.
- Low-level metrics and high-level service states both matter for operating distributed systems.
- Manual metric and dashboard work becomes a scaling problem as the service mesh and engineering organization grow.
- Observability must connect internal alerts to customer impact, because healthy internal or dogfooding environments can hide production-only overload.
- Swappable infrastructure benefits from implementation-independent observability and deployment-integrated checks for hard-to-measure correctness properties, while autonomous agents additionally need end-to-end evidence for verification, attribution, and redress.

## Evidence
- Provider metrics: [[a-look-at-auth0-cloud-architecture-5-years-in]] uses CloudWatch for AWS-generated alarms such as load-balancer HTTP errors, unhealthy targets, and SQS delays.
- Service metrics: [[a-look-at-auth0-cloud-architecture-5-years-in]] uses DataDog for host, AWS, NGINX, MongoDB, and custom-service time-series metrics.
- External probes: [[a-look-at-auth0-cloud-architecture-5-years-in]] says Pingdom probes run every minute to check core functionality.
- Logs and audit trails: [[a-look-at-auth0-cloud-architecture-5-years-in]] describes Kibana for application and service logs and SumoLogic for audit trails and AWS-generated logs.
- Escalation policy: [[a-look-at-auth0-cloud-architecture-5-years-in]] routes likely customer-impacting alerts to PagerDuty while sending broader alerts to Slack.
- Misleading symptoms: [[asanas-september-8-outage]] says the first page came from search-indexer lag and the next from API downtime, while the actual bottleneck was web-server CPU saturation.
- Customer-impact escalation: [[asanas-september-8-outage]] says customer support told on-call engineers that users were unable to use the app after the initial investigation underestimated severity.
- Environment gap: [[asanas-september-8-outage]] says engineers used a dogfooding version on different AWS EC2 instances that were not overloaded, making the incident harder to perceive internally.
- Silent control-plane failure: [[details-on-the-january-9th-2017-asana-outage]] says provisioning-job copies timed out waiting for a lock, but their non-paging alerts went unnoticed until Monday demand exposed the capacity shortage.
- Implementation-independent measurement: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says observability should be above APIs and external to implementations where possible.
- Comparison support: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says this placement helps teams switch implementations and compare performance without measurement-code bugs.
- Correctness checks: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says difficult-to-measure attributes such as consistency require special attention and that critical checks should be pushed into deployment when possible.
- Detection-path review: [[rule-11-reader-learning-from-the-post-mortem]] asks where a failure should have been detected sooner and explicitly qualifies dwell-time reduction by false-positive collateral damage.
- Troubleshooting instrumentation: [[rule-11-reader-learning-from-the-post-mortem]] uses a recorded diagnostic flow to identify evidence that should be instrumented or made easier to find.
- Agent accountability: [[dang-agent-zou-xiang-sheng-chan-infra-mian-lin-na-xie-tiao-zhan]] argues that high-volume autonomous execution needs complete auditability so failures can be proved, attributed, reviewed, and learned from after people leave the per-action verification loop.
- Reality anchoring: [[dang-agent-zou-xiang-sheng-chan-infra-mian-lin-na-xie-tiao-zhan]] connects traces to compilers, rules, databases, and real-world feedback that can check model claims through differently sourced evidence.

## Counterevidence & Qualifications
The sources list tools, incidents, and practitioner guidance rather than a full observability taxonomy. Auth0 admits fragmentation: it was evaluating centralizing logging and automating metrics because manual dashboards and multiple providers had become operational overhead. Asana's two postmortems show distinct limits: pages and dashboards can mislead when user impact or environment differences are obscure, while technically correct alerts still fail when routing does not match the risk of an impaired control plane. Balakrishnan's placement rule is strongest for infrastructure with multiple implementations. White does not quantify an acceptable dwell-time or false-positive frontier, and retrospective maps remain vulnerable to missing records and hindsight bias. The accountability extension is conceptual: logs can be incomplete, tampered with, semantically ambiguous, or too voluminous to review, and observability alone cannot determine intent, liability, acceptable error, or remedy.

## What Changed
- Observability now combines infrastructure and service metrics, external probes, logs, audit trails, routing, and user-impact escalation.
- Outage evidence shows that emitted signals are insufficient when environments diverge, symptoms mislead, or alerts do not trigger action.
- Implementation-independent measurement and deployment checks preserve comparability and expose hard-to-measure correctness properties.
- Detection and troubleshooting reconstruction identify missing evidence while balancing dwell-time reduction against false positives.
- Added accountability as an agent-era extension: traces must support verification, attribution, investigation, and redress at machine scale.

## Related Concepts
- [[SystemReliability]] - observability reveals reliability problems and supports response.
- [[ChangeSafety]] - release safety depends on monitoring, alerts, and rollback signals.
- [[DeploymentAutomation]] - deployments need pre/post checks and production visibility.
- [[CloudHighAvailability]] - availability mechanisms need metrics and alerts to detect failover conditions.
- [[InternalDeveloperPlatform]] - platform defaults can standardize metrics, logs, dashboards, and monitors.
- [[FailureOwnership]] - postmortems use observability gaps to improve future detection and triage.
- [[ProductionInfrastructureLeadership]] - infrastructure leaders decide where observability lives relative to APIs and implementations.
- [[AccountabilityInfrastructure]] - extends operational traces into evidence for governing autonomous agent actions and failures.
