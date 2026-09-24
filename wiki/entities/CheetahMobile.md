---
title: "Cheetah Mobile"
type: entity
tags: [company, mobile-apps, android, adtech]
sources:
  - android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Overview
[[CheetahMobile]] is a Chinese mobile-app company represented in the wiki by a 2018 BuzzFeed News investigation alleging that seven of its Android apps manipulated install attribution to collect bounties for downloads they did not cause.

## Current Profile
The source describes Cheetah Mobile as a New York Stock Exchange-listed developer whose utility and keyboard apps reached more than 2 billion combined downloads when counted with Kika Keyboard. Kochava alleged that Cheetah apps monitored new installations, injected attribution clicks, sometimes opened newly installed apps, and dispersed claims through ad networks to win last-click bounties. Cheetah disputed the account: it first blamed third-party SDK behavior and later denied that its own SDKs performed click injection, although Kochava said the relevant SDK was Cheetah-owned.

## Key Characteristics
- Operated seven Android apps implicated in the reported attribution scheme.
- Combined broad installation visibility with the ability to launch other apps.
- Was alleged to inject late clicks and automatically open apps to improve its chance of receiving install bounties.
- Used a proprietary SDK that Kochava tied to the suspect activity.
- Generated substantial utility-product revenue while the implicated apps formed an important part of that product category.
- Denied that its own SDKs engaged in click injection and described two app removals as voluntary and temporary.

## Evidence
- App portfolio and scale: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] names Clean Master, CM File Manager, CM Launcher 3D, Security Master, Battery Doctor, CM Locker, and Cheetah Keyboard and reports more than 20 million downloads across them in the preceding 30 days.
- Alleged mechanism: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] says the apps detected new downloads, searched for active bounties, sent attribution clicks, and sometimes launched the new app without user knowledge.
- Concealment: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] says proprietary software distributed attribution claims through many networks and sometimes used false app names.
- Business significance: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] reports $196 million in quarterly utility-products-and-services revenue, roughly half of company revenue, without isolating revenue from install claims.
- Response: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] records Cheetah's third-party-SDK explanation, denial about its own SDKs, and statement that CM Locker and Battery Doctor were removed voluntarily.

## Qualifications
The profile is based on a November 2018 investigation and does not establish Cheetah Mobile's current products, ownership, policies, or conduct. Kochava supplied the principal technical evidence while Cheetah and Kika were its customers, BuzzFeed News also commissioned an analysis from Method Media Intelligence, and the article does not reproduce a complete independent audit. Allegations of fraud remain disputed by Cheetah, and reported company revenue cannot be attributed specifically to fraudulent installs.

## What Changed
- Created Cheetah Mobile as the main company alleged to have operationalized install-attribution manipulation across seven apps.
- Preserved the conflict between Kochava's proprietary-SDK finding and Cheetah's denials.

## Relationships
- [[KikaTech]] - mobile-app company that received a Cheetah investment and was implicated in the same investigation.
- [[Kochava]] - attribution provider that detected and documented the alleged behavior.
- [[AppInstallAttributionFraud]] - alleged mechanism by which Cheetah apps claimed unearned install bounties.
- [[Android]] - operating-system environment whose app permissions and install events were used.
- [[GooglePlay]] - marketplace that distributed the implicated apps and later lacked two of them after publication.
