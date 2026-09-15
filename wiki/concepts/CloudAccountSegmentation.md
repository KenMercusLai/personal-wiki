---
title: "Cloud Account Segmentation"
type: concept
tags: [cloud, aws, security, infrastructure]
sources:
  - an-infrastructure-guide-for-founders-starting-up-security-medium
  - central-logging-in-multi-account-environments-aws-architecture-blog
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[CloudAccountSegmentation]] is the practice of splitting cloud infrastructure across multiple accounts or tenancies to manage blast radius, identity, logs, billing, policies, and product or customer boundaries.

## Current Synthesis
The source argues that even young startups can eventually accumulate many AWS accounts, whether for customer requirements, separate products, logs, or identity boundaries. Assuming a future multi-account shape early can reduce later refactors and encourage AWS roles instead of long-lived IAM keys.

The operational tension is velocity versus future complexity. A monolithic account is simpler at the beginning, but the article argues that many companies eventually need account boundaries, centralized logs, centralized identity, AWS Organizations policies, and billing consolidation. Early planning for that mid-game can reduce churn while keeping blast radius explicit.

The AWS central-logging source supplies a concrete boundary pattern: one logging account owns the S3 bucket, log destination, Kinesis stream, Firehose delivery stream, and processing Lambda, while each application account owns its CloudWatch log groups and subscription filters. Cross-account flow is allowed through destination policies and IAM roles rather than by collapsing all logs and applications into one account.

## Key Claims
- Multiple cloud accounts can reduce blast radius by preventing all systems from sharing one administrative and resource boundary.
- Central logging and central identity choices should be designed with account structure in mind.
- Role-based access reduces the impact of leaked IAM keys.
- AWS Organizations can later enforce mandatory policies and centralize billing across accounts.
- Early multi-account thinking trades some developer-workflow complexity for less disruptive future refactoring.
- A dedicated logging account can receive log streams from application accounts through explicit destinations, policies, roles, and subscription filters.

## Evidence
- Growth path: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] says young startups can gather tens of accounts while larger companies can have far more.
- Blast radius: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] lists well-defined blast radius as a reason to avoid a monolithic account assumption.
- Identity and logs: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] connects account strategy to centralized logs and a single IAM source of identity.
- Roles and policies: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] links roles, reduced key-leakage impact, AWS Organizations policy enforcement, and centralized billing.
- Central logging account: [[central-logging-in-multi-account-environments-aws-architecture-blog]] separates the logging bucket, Kinesis stream, Firehose, Lambda processor, and log destination from the source application account.
- Cross-account permissioning: [[central-logging-in-multi-account-environments-aws-architecture-blog]] uses a destination policy naming the source account plus IAM roles for CloudWatch Logs and Firehose delivery.
- Regional constraint: [[central-logging-in-multi-account-environments-aws-architecture-blog]] says the subscription and destination must be in the same AWS region.

## Counterevidence & Qualifications
The startup-security source acknowledges that monolithic account structures can favor early developer speed and simplicity. Multi-account workflows can require role-switching and shell tooling that take time to make ergonomic. The AWS central-logging recipe also adds service and regional constraints: subscriptions and destinations must be same-region, and different storage hierarchies or buckets may require separate destinations.

## What Changed
- Added the AWS central-logging account pattern as a concrete example of account segmentation for shared evidence storage and cross-account log delivery.

## Related Concepts
- [[StartupSecurityDebt]] - account structure is a design choice that can become future security and migration debt.
- [[CentralizedLogging]] - multi-account planning determines where cloud logs should land.
- [[ProductionAccessControl]] - role-based account access shapes who can administer production.
- [[InfrastructureAsCode]] - account boundaries need repeatable provisioning and policy automation.
