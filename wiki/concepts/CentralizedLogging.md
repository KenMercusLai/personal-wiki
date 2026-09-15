---
title: "Centralized Logging"
type: concept
tags: [logging, observability, security, operations]
sources:
  - an-infrastructure-guide-for-founders-starting-up-security-medium
  - central-logging-in-multi-account-environments-aws-architecture-blog
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[CentralizedLogging]] is the practice of collecting application, host, and infrastructure logs into a shared, queryable system for investigation, troubleshooting, dashboards, and policy decisions.

## Current Synthesis
The source treats centralized logging as an early infrastructure primitive because local or missing logs give teams little leverage during incidents. The same log corpus helps security investigation and product availability: developers can debug performance and outages without chasing scattered files, while security teams can reconstruct events and make policy choices from observed usage.

For an AWS startup, the article suggests CloudWatch Logs as a reasonable default because it can ingest logs at scale, provide a single query surface, and support rudimentary dashboards. The important design move is not the specific product but the decision to corral application logs, `/var/log` system logs, CloudTrail, and optional network flow data into a place the team can actually use.

The AWS Architecture Blog source turns that general recommendation into a concrete multi-account pipeline. Application-account CloudWatch log groups subscribe to a same-region logs destination in a central logging account; that destination writes to a Kinesis stream, Firehose reads the stream, invokes a Lambda processor to unzip and validate log records, and stores transformed output in an S3 logging bucket with optional Glacier archival. Once logs land in S3, Athena can query them with ordinary SQL, as shown by the VPC flow-log example.

## Key Claims
- Local or absent logs provide little incident-response leverage.
- Centralized logs serve availability and troubleshooting as much as security investigation.
- Application, system, and cloud-provider logs should be considered as separate but connected streams.
- A queryable default logging location lets teams build dashboards and make policy decisions from actual usage.
- Logging design should happen early because later retrofits leave gaps in historical evidence.
- In multi-account AWS environments, log ingestion, transformation, storage, archival, and analysis can be separated across CloudWatch Logs, Kinesis, Firehose, Lambda, S3, Glacier, and Athena.

## Evidence
- Incident leverage: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] says a team without coherent logging will be mostly useless during a security incident.
- Availability value: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] argues logs often help product availability more than security risk.
- Log buckets: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] separates application, system, and infrastructure logs including CloudTrail and network flow data.
- AWS default: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] recommends CloudWatch Logs as a practical early default for scalable centralized logging and basic dashboards.
- Cross-account flow: [[central-logging-in-multi-account-environments-aws-architecture-blog]] shows CloudWatch log groups in application accounts subscribing to a destination in a central logging account.
- Delivery pipeline: [[central-logging-in-multi-account-environments-aws-architecture-blog]] uses Kinesis, Firehose, and a Lambda processor before writing transformed logs into S3.
- Analysis path: [[central-logging-in-multi-account-environments-aws-architecture-blog]] demonstrates Athena querying VPC flow logs from the central S3 location.

## Counterevidence & Qualifications
The sources do not compare CloudWatch Logs with alternatives or specify privacy, redaction, or incident-response runbook details. The AWS recipe is service-specific and source-date-specific, including an old Node.js Lambda runtime example, and centralization creates a sensitive evidence store that needs access control, retention policy, and cost management.

## What Changed
- Added a concrete AWS multi-account logging architecture that clarifies how subscription filters, destinations, Kinesis, Firehose, Lambda, S3, Glacier, and Athena can compose into a central log system.

## Related Concepts
- [[ServiceObservability]] - centralized logs are one layer of broader observability.
- [[StartupSecurityDebt]] - missing or scattered logs are an early form of security debt.
- [[ProductionAccessControl]] - better logs reduce the need for invasive production host access.
- [[SystemReliability]] - queryable logs support outage diagnosis and recovery.
- [[CloudAccountSegmentation]] - central logging can be implemented as a dedicated account receiving application-account log streams.
