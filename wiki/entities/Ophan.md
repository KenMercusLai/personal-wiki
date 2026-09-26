---
title: "Ophan"
type: entity
tags: [analytics, journalism, internal-tools]
sources:
  - constantly-tweaking-how-the-guardian-continues-to-develop-its-in-house-analytics-system-nieman-journalism-lab
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Overview
[[Ophan]] is [[TheGuardian]]'s in-house newsroom analytics system, created at a 2011 hack day and represented in a 2015 report as a widely accessible tool for live editorial feedback.

## Current Profile
Ophan exposed article, section, and site performance through views such as page views, median attention time, live stories, referrals, and views per minute. Bookmarklets and a mobile interface lowered access friction, while configurable email alerts surfaced exceptional traffic without requiring continuous dashboard monitoring.

Its development model was as important as its metrics. Editorial staff proposed changes, audience-engagement and development teams discussed improvements, and developers shipped minimum versions before refining them. A live search-referral experiment also attempted to humanize aggregate Google traffic by showing the individual queries behind the small visible subset.

## Key Characteristics
- Provides live article, section, and site-level audience-performance views.
- Emphasizes understandable measures and low-friction access for non-specialist newsroom staff.
- Breaks traffic down by referrer and connects it with attention time, page views, and current story rank.
- Supports configurable email alerts based on traffic source, views-per-minute thresholds, and duration.
- Evolves through direct editorial feedback and minimum-first iteration.

## Evidence
- Audience and performance views: [[constantly-tweaking-how-the-guardian-continues-to-develop-its-in-house-analytics-system-nieman-journalism-lab]] and its retained screenshots show story totals, attention time, week-long traffic, referral mix, live rankings, and current traffic rates.
- Access design: [[constantly-tweaking-how-the-guardian-continues-to-develop-its-in-house-analytics-system-nieman-journalism-lab]] describes bookmarklets, mobile access, and deliberately understandable core measures for more than 900 newsroom users.
- Proactive monitoring: [[constantly-tweaking-how-the-guardian-continues-to-develop-its-in-house-analytics-system-nieman-journalism-lab]] and its alert screenshot show named threshold rules for traffic from Twitter, Facebook, Google, Drudge Report, and unknown sources.
- Development and experimentation: [[constantly-tweaking-how-the-guardian-continues-to-develop-its-in-house-analytics-system-nieman-journalism-lab]] describes the 2011 hack-day origin, three-minute initial retention, regular editorial feedback, and an experimental live Google-query ticker.

## Qualifications
The evidence is a single 2015 journalistic account and a set of interface screenshots. It does not establish causal improvements in story quality, audience value, revenue, or newsroom performance; it also reports only one week of analyzed content and 10-20 percent visibility into Google search terms. The product may have changed substantially since publication.

## What Changed
- Established Ophan as an accessible editorial-feedback system rather than merely a traffic dashboard.
- Added visual evidence of article, ranking, referral, alert, and search-query interfaces.

## Relationships
- [[TheGuardian]] - organization that created, deployed, and iterated Ophan.
- [[NewsroomAnalytics]] - editorial practice the product operationalizes.
- [[DataInformedCulture]] - decision culture supported by shared, interpretable evidence.
- [[AgileSoftwareDevelopment]] - iterative feedback model used to evolve the system.
