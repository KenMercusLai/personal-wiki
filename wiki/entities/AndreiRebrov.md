---
title: "Andrei Rebrov"
type: entity
tags: [engineering-leadership, email-marketing, startups]
sources:
  - email-marketing-from-tech-perspective-scentbird-tech-medium
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[AndreiRebrov]] is represented in the wiki as [[Scentbird]]'s CTO and the author of a 2016 practitioner account of the company's email-marketing systems.

## Current Profile
Rebrov approaches email as a product and engineering problem built around customer state, segmentation, delivery quality, job control, queues, measurement, and shared suppression rules. His account is useful as a concrete historical architecture, not as a current audit of Scentbird or its vendors.

## Key Characteristics
- Frames email marketing as a data system rather than a volume-only acquisition tactic.
- Separates mass campaigns, immediate transactional messages, and scheduled drip messages by purpose and workload.
- Treats deliverability, unsubscribe behavior, monitoring, and safe job execution as product-quality concerns.

## Evidence
Data-system framing:
- [[email-marketing-from-tech-perspective-scentbird-tech-medium]] says useful email depends on when, why, how, and to whom a message is sent.

Workload architecture:
- [[email-marketing-from-tech-perspective-scentbird-tech-medium]] describes segmentation, scheduled SQL selection, idempotent marking, isolated workers, and separate queues.

Product-quality stance:
- [[email-marketing-from-tech-perspective-scentbird-tech-medium]] closes with monitoring, testing, investment in quality, and the instruction to treat email as a product.

## Qualifications
The source is a self-reported 2016 article. It does not independently measure conversion lift, causal effects, long-term sender reputation, or the relative performance of the tools described.

## What Changed
- Added Rebrov's historical engineering model for mass, transactional, and drip email.

## Relationships
- [[Scentbird]] - company for which Rebrov describes the email system.
- [[EmailLifecycleAutomation]] - operating model developed through customer data, jobs, and queues.
- [[EmailDeliverability]] - quality and reputation discipline emphasized in his account.
