---
title: "Central Logging in Multi-Account Environments"
type: source
tags: [aws, logging, cloudwatch, kinesis, firehose, athena]
date: 2018-03-02
source_file: /mnt/ken_personal_wiki/Articles/Central Logging in Multi-Account Environments - AWS Architecture Blog.md
---

## Summary
The AWS Architecture Blog describes a repeatable [[CentralizedLogging]] pattern for streaming CloudWatch Logs from multiple application accounts into a dedicated logging account. The inspected architecture diagram shows each application account subscribing CloudWatch log groups to a same-region destination in the logging account, where Kinesis, Firehose, a transformation Lambda, S3, optional Glacier archival, and Athena form the delivery and analysis path. The article is an implementation recipe built around CloudFormation templates, IAM roles, destination policies, subscription filters, and an Athena table for VPC flow-log querying.

## Key Claims
- [[CloudAccountSegmentation]] can support central logging by keeping log storage and analysis in a dedicated logging account while application accounts publish through explicit subscriptions.
- CloudWatch Logs destinations and subscription filters must be in the same AWS region, and different S3 hierarchies or buckets require separate destinations.
- A Kinesis stream plus Kinesis Firehose can move subscribed log events into S3 while invoking a reusable Lambda processor to unzip, parse, validate, and transform CloudWatch log records.
- CloudFormation templates make the deployment repeatable across buckets, Lambda processing, log destinations, and application-account subscriptions.
- Centralized S3 log storage enables downstream analysis with Athena SQL, illustrated by a VPC flow-log table and query over accepted and rejected traffic.
- The architecture's access model depends on scoped IAM roles, destination policies naming source accounts, Firehose delivery permissions, and subscription-filter permissions.

## Key Quotes
> "destination and subscription have to be in the same region" - on a deployment constraint for cross-account log streaming.

> "This solution is repeatable" - on deploying the pattern across multiple accounts and logging requirements.

## Connections
- [[AWS]] - cloud provider whose CloudWatch Logs, Kinesis, Firehose, Lambda, S3, Glacier, CloudFormation, IAM, and Athena services are combined in the architecture.
- [[CentralizedLogging]] - the core pattern: application-account logs are delivered to a central logging-account bucket and queried later.
- [[CloudAccountSegmentation]] - the solution separates application accounts from a central logging account while granting cross-account publish rights.
- [[InfrastructureAsCode]] - CloudFormation templates provision the bucket, processor Lambda, destination stack, and subscription filter.
- [[ServiceObservability]] - the log stream creates operational evidence for troubleshooting and security analysis.
- [[CloudCostOptimization]] - S3 plus optional Glacier archival implies retention and storage-tier choices for accumulated logs.

## Contradictions
- No direct contradictions found. The source adds a concrete AWS service implementation to earlier, more general guidance on centralized logs and multi-account planning; service versions, Lambda runtime examples, and console workflows are source-date-specific.
