---
title: "Scentbird"
type: entity
tags: [subscription-commerce, email-marketing, startups]
sources:
  - email-marketing-from-tech-perspective-scentbird-tech-medium
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[Scentbird]] is represented in the wiki through a 2016 CTO-authored account of email systems supporting its subscription customer journey.

## Current Profile
The account portrays Scentbird as operating separate but coordinated mass and trigger-email paths. Customer acquisition source, geography, subscription state, tenure, engagement, and journey events informed segmentation, while scheduled jobs, queues, sender authentication, monitoring, and synchronized unsubscribe state supported execution.

## Key Characteristics
- Used customer and journey data to segment campaign and trigger messages.
- Combined self-hosted mass-email tooling with a separate triggered-message system.
- Treated sender trust, list health, and cross-system unsubscribe consistency as operational concerns.

## Evidence
Data-driven segmentation:
- [[email-marketing-from-tech-perspective-scentbird-tech-medium]] lists source, time zone, subscription status, tenure, and open behavior as practical segment inputs.

Separated execution paths:
- [[email-marketing-from-tech-perspective-scentbird-tech-medium]] describes [[Sendy]] with Amazon SES for campaigns and Mandrill-backed event and drip messages.

Operational controls:
- [[email-marketing-from-tech-perspective-scentbird-tech-medium]] recommends SPF and DKIM, reputation checks, bounce and complaint handling, independently controllable jobs, queues, and synchronized suppression.

## Qualifications
This is one company-authored 2016 account, not an independent or current system audit. It reports practices and rough limits but provides no campaign-level outcome data, controlled comparisons, or later operating history.

## What Changed
- Added Scentbird's historical email-marketing architecture and operational practices.

## Relationships
- [[AndreiRebrov]] - CTO who authored the source account.
- [[Sendy]] - self-hosted mass-email tool used in the reported stack.
- [[EmailLifecycleAutomation]] - describes the event, schedule, and customer-state model.
- [[EmailDeliverability]] - captures the quality and reputation controls in the account.
