---
title: "Sendy"
type: entity
tags: [email-marketing, software, amazon-ses]
sources:
  - email-marketing-from-tech-perspective-scentbird-tech-medium
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[Sendy]] is represented in the wiki as the self-hosted mass-email application [[Scentbird]] used with Amazon SES in 2016.

## Current Profile
The historical account emphasizes Sendy's low sending cost, campaign reports, bounce, complaint, and unsubscribe handling, autoresponders, API access, and schedulable campaign and import jobs. It also reports operational burdens: self-hosting, AWS configuration, PHP memory tuning, network throughput constraints, and the need to synchronize suppression state with a separate trigger-email system.

## Key Characteristics
- Self-hosted campaign application using Amazon SES for delivery.
- Exposed campaign reporting, list operations, autoresponders, and an API.
- Required infrastructure, scheduled jobs, AWS identity and domain setup, and SNS integration.
- Introduced performance and coordination work that a hosted service would absorb.

## Evidence
Delivery and campaign role:
- [[email-marketing-from-tech-perspective-scentbird-tech-medium]] says Scentbird moved from [[Mailchimp]] to Sendy for mass email and used its reporting and response handling.

Operating requirements:
- [[email-marketing-from-tech-perspective-scentbird-tech-medium]] describes a PHP and MySQL deployment, AWS credentials and domain verification, SNS topics, and cron-driven scheduling and imports.

Performance and coordination limits:
- [[email-marketing-from-tech-perspective-scentbird-tech-medium]] reports memory and throughput constraints and says trigger-system unsubscribes also needed propagation into Sendy.

## Qualifications
The profile is based on one 2016 user account. Product features, pricing, APIs, installation requirements, AWS integrations, and performance may have changed, and the reported throughput is workload- and environment-specific.

## What Changed
- Added Sendy's historical role and operational tradeoffs in Scentbird's email stack.

## Relationships
- [[Scentbird]] - company using Sendy for mass campaigns in the source.
- [[EmailMarketingAtScale]] - self-hosting exposes throughput and workload-management constraints.
- [[EmailDeliverability]] - bounce, complaint, unsubscribe, and authentication handling affect sender health.
- [[EmailLifecycleAutomation]] - campaign lists must coordinate with trigger and drip suppression state.
