---
title: "Kochava"
type: entity
tags: [company, analytics, attribution, adtech]
sources:
  - android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Overview
[[Kochava]] is an app analytics and attribution company that supplied the main technical investigation behind BuzzFeed News's 2018 report on click flooding and click injection in Cheetah Mobile and Kika Tech apps.

## Current Profile
In the source, Kochava observes attribution traffic, captures app behavior on video, and traces suspicious install claims back through ad networks to the apps that originated them. Its investigators said the implicated apps generated last-click signals without adding marketing value and used proprietary software to obscure the origin of attribution wins. Kochava was also a commercial counterparty: Cheetah and Kika were its customers when it detected the behavior.

## Key Characteristics
- Operated as a mobile analytics and install-attribution provider.
- Detected anomalous click flooding and click injection through attribution data and app observation.
- Traced apparently dispersed network claims back to specific Cheetah and Kika apps.
- Shared videos and findings with BuzzFeed News and offered to assist Google's investigation.
- Had an existing customer relationship with both companies it investigated.

## Evidence
- Investigative role: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] identifies Kochava as the company that detected the scheme and supplied its findings to BuzzFeed News.
- Mechanism analysis: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] attributes the detailed click injection, click flooding, auto-launch, and multi-network concealment account to Kochava.
- Platform escalation: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] says BuzzFeed News gave Google Kochava's captured videos and quotes Kochava offering further help.
- Commercial context: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] states that Cheetah and Kika were Kochava customers when the behavior was discovered.

## Qualifications
The source relies heavily on Kochava's findings and selected videos rather than publishing a complete dataset or reproducible report. Method Media Intelligence provided additional analysis for BuzzFeed News, but the article does not specify all validation methods. Kochava's customer relationship gave it data access and relevant visibility while also making transparent disclosure of its role important.

## What Changed
- Created Kochava as the attribution provider and principal investigator behind the source's fraud claims.
- Recorded its customer relationship with the investigated companies as both context and qualification.

## Relationships
- [[CheetahMobile]] - customer whose apps Kochava alleged generated fraudulent attribution claims.
- [[KikaTech]] - customer whose keyboard Kochava alleged used flooding and injection.
- [[AppInstallAttributionFraud]] - abuse pattern Kochava detected through its attribution position.
- [[MarketingAttribution]] - measurement infrastructure that made Kochava's detection possible and whose last-click rule was exploited.
- [[GooglePlay]] - platform to which the investigated installations and enforcement questions belonged.
