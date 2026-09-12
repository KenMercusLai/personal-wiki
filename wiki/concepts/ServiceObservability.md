---
title: "Service Observability"
type: concept
tags: [observability, monitoring, logging, operations]
sources:
  - a-look-at-auth0-cloud-architecture-5-years-in
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[ServiceObservability]] is the operational ability to understand service health and behavior through metrics, probes, alarms, dashboards, logs, audit trails, and escalation channels.

## Current Synthesis
The Auth0 source presents observability as a layered operating system for a production SaaS. CloudWatch covers AWS-generated metrics such as load-balancer errors, target-group health, and SQS delays. DataDog stores and monitors time-series metrics from hosts, AWS resources, off-the-shelf services, and custom services. Pingdom probes continuously exercise core functionality, while Kibana and SumoLogic divide application logs, service logs, audit trails, and AWS-generated logs.

Alert routing is part of the design. CloudWatch alarms usually route through PagerDuty to Slack and phones; DataDog alerts usually go to Slack, with PagerDuty reserved for issues likely to wake people because they are customer-impacting. The future work points to observability as an automation target: standard metric naming, generated dashboards, generated monitors, and log-derived metrics can reduce manual dashboard and monitor maintenance.

## Key Claims
- Observability should combine infrastructure metrics, service metrics, external probes, logs, audit trails, and escalation policy.
- Different monitoring tools can have distinct roles: provider metrics, time-series service metrics, external checks, and log analysis.
- Alert routing should distinguish informational signals from customer-impacting pages.
- Low-level metrics and high-level service states both matter for operating distributed systems.
- Manual metric and dashboard work becomes a scaling problem as the service mesh and engineering organization grow.

## Evidence
- Provider metrics: [[a-look-at-auth0-cloud-architecture-5-years-in]] uses CloudWatch for AWS-generated alarms such as load-balancer HTTP errors, unhealthy targets, and SQS delays.
- Service metrics: [[a-look-at-auth0-cloud-architecture-5-years-in]] uses DataDog for host, AWS, NGINX, MongoDB, and custom-service time-series metrics.
- External probes: [[a-look-at-auth0-cloud-architecture-5-years-in]] says Pingdom probes run every minute to check core functionality.
- Logs and audit trails: [[a-look-at-auth0-cloud-architecture-5-years-in]] describes Kibana for application and service logs and SumoLogic for audit trails and AWS-generated logs.
- Escalation policy: [[a-look-at-auth0-cloud-architecture-5-years-in]] routes likely customer-impacting alerts to PagerDuty while sending broader alerts to Slack.

## Counterevidence & Qualifications
The source lists tools and examples rather than a full observability taxonomy. It also admits fragmentation: Auth0 was evaluating centralizing logging and automating metrics because manual dashboards and multiple providers had become operational overhead.

## What Changed
- Created the concept from Auth0's monitoring, alerting, logging, and metrics practices.

## Related Concepts
- [[SystemReliability]] - observability reveals reliability problems and supports response.
- [[ChangeSafety]] - release safety depends on monitoring, alerts, and rollback signals.
- [[DeploymentAutomation]] - deployments need pre/post checks and production visibility.
- [[CloudHighAvailability]] - availability mechanisms need metrics and alerts to detect failover conditions.
- [[InternalDeveloperPlatform]] - platform defaults can standardize metrics, logs, dashboards, and monitors.
