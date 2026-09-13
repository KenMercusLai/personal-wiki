---
title: "Crashlytics"
type: entity
tags: [product, mobile, developer-tools]
sources:
  - advocating-for-a-complete-product-redesign-google-design-medium
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[Crashlytics]] is presented as a crash-reporting tool for mobile app developers that helps teams understand why apps crash and decide what to fix.

## Current Profile
The source treats Crashlytics as a well-loved but design-debt-laden product created in 2011 and later moved from [[Fabric]] into [[Firebase]] after Google's acquisition. Its redesign was prompted by the need to adopt [[MaterialDesign]], but the team used that migration to rethink the whole user experience. The main product problem was not missing core capability; it was that users struggled to find important crash information and sometimes requested features that already existed but were buried in the interface.

## Key Characteristics
- Helps mobile developers monitor crashes, affected users, crash-free users, crash-free sessions, versions, events, devices, logs, keys, data, and stack traces.
- Had four critical user journeys: monitoring a newly released app version, checking app stability, prioritizing crashes to fix, and debugging a customer problem.
- Shared a recurring [[InvestigateAndFixFlow]] across those journeys.
- Accumulated design debt and unclear [[InformationHierarchy]] after years of product growth.
- Became part of [[Firebase]] after the [[Fabric]] acquisition and was redesigned in Firebase's [[MaterialDesign]] environment.
- The inspected screenshots show a clearer Firebase overview and issue-detail surface than the older Fabric dashboard.

## Evidence
- Product role: [[advocating-for-a-complete-product-redesign-google-design-medium]] defines Crashlytics as a crash-reporting tool that helps mobile app developers understand crashes.
- Critical journeys: [[advocating-for-a-complete-product-redesign-google-design-medium]] lists monitoring a new release, checking stability, prioritizing crashes, and debugging a customer problem as the four most important journeys.
- Shared flow: [[advocating-for-a-complete-product-redesign-google-design-medium]] says mapping the journeys revealed a recurring investigate-and-fix micro-journey.
- Design debt: [[advocating-for-a-complete-product-redesign-google-design-medium]] says Crashlytics had design debt, hidden features, and unclear hierarchy by the time of the Firebase migration.
- Redesigned surface: [[advocating-for-a-complete-product-redesign-google-design-medium]] includes inspected images where Firebase Crashlytics surfaces crash-free statistics, event trends, filters, issue tables, device/version breakdowns, session summaries, and stack-trace tabs more directly.

## Qualifications
The source is a product-design retrospective from the redesign team, so it emphasizes the case-building process and final alignment more than independent user outcomes, crash-fixing performance, or long-term adoption metrics.

## What Changed
- Created the entity page for Crashlytics as a developer-tool product redesigned through journey mapping and information-hierarchy repair.

## Relationships
- [[Firebase]] - Crashlytics was redesigned and rebuilt into Firebase.
- [[Fabric]] - Crashlytics came to Google through the Fabric acquisition.
- [[Google]] - Google acquired Fabric and owns Firebase in the source context.
- [[MaterialDesign]] - Firebase's design system shaped the required visual update.
- [[ProductRedesign]] - Crashlytics is the main case.
- [[InformationHierarchy]] - unclear hierarchy was the primary user-experience problem.
- [[UserJourneyMapping]] - journey maps aligned the team around how Crashlytics was used.
- [[InvestigateAndFixFlow]] - recurring Crashlytics micro-journey.
- [[InternalCoDesign]] - teammate cutout sessions diagnosed dashboard pain points.
