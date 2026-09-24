---
title: "Kika Tech"
type: entity
tags: [company, mobile-apps, keyboard, adtech]
sources:
  - android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Overview
[[KikaTech]] is the developer of Kika Keyboard, represented in the wiki by a 2018 investigation alleging that the app used its visibility into Play Store searches and installations to perform click flooding and click injection.

## Current Profile
The source describes Kika Tech as a Chinese company headquartered in Silicon Valley that received a significant 2016 investment from [[CheetahMobile]]. Its Kika Keyboard app reportedly had 60 million monthly active users and 205 million downloads. Kochava alleged that the app monitored Play Store searches, looked for related install bounties, generated attribution clicks, displayed offer-linked ads, and listened even when the keyboard was inactive. Kika said it had no intention of committing fraud, took data security seriously, and would investigate whether improper code had entered the product.

## Key Characteristics
- Developed Kika Keyboard, a high-scale Android keyboard app.
- Held permission to observe typed input and allegedly used Play Store search signals for attribution activity.
- Was alleged to perform both click flooding and click injection.
- Used proprietary software that independent analysis said contained the relevant behavior.
- Distributed attribution claims across multiple ad networks to obscure their source.
- Denied intentional wrongdoing and promised an internal investigation.

## Evidence
- Scale and ownership context: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] reports 60 million monthly active users, 205 million downloads, and Cheetah Mobile's 2016 investment.
- Search-based flooding: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] says Kika listened for Play Store searches, found related bounty offers, and generated clicks in anticipation of later installs.
- Background activity: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] says the app listened for store searches even when the keyboard was not active and could claim credit without a user clicking an ad.
- Proprietary implementation: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] reports that Kochava and Method Media Intelligence tied the behavior to Kika's own software and built-in functions.
- Response: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] records Kika executives' denial of intent, privacy-policy defense, and promise to investigate.

## Qualifications
The profile records disputed allegations from a November 2018 article, not a current audit of Kika Tech or Kika Keyboard. The article summarizes videos and code analysis but does not publish a complete reproducible technical report. The evidence supports a conflict between observed behavior and company explanations; it does not by itself establish which individuals authorized or knew about the implementation.

## What Changed
- Created Kika Tech as the keyboard developer alleged to have combined search monitoring with click flooding and injection.
- Preserved Kika's denial of intent and the unresolved question of organizational knowledge.

## Relationships
- [[CheetahMobile]] - investor and fellow app developer implicated in the same investigation.
- [[Kochava]] - attribution company that recorded and analyzed Kika Keyboard's behavior.
- [[AppInstallAttributionFraud]] - alleged practice implemented through flooding and injected clicks.
- [[Android]] - platform where keyboard permissions and app-store activity supplied useful signals.
- [[GooglePlay]] - store whose searches and installations were allegedly monitored.
