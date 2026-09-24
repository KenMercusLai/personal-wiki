---
title: "App Install Attribution Fraud"
type: concept
tags: [ad-fraud, attribution, mobile-apps, android]
sources:
  - android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[AppInstallAttributionFraud]] is the manipulation of mobile measurement signals so a party receives credit and payment for an app installation it did not cause.

## Current Synthesis
The source shows how last-click app-install attribution can become an attack surface. A legitimate flow records a user's ad click, installation, and first open, then pays the network or publisher associated with that click. Click injection watches for an installation and inserts a later synthetic click before the first open; click flooding sends many speculative clicks so one may become the recorded last touch. When software already on the phone can observe searches or installations, launch apps, and route claims through multiple networks, it can turn ordinary permissions and measurement plumbing into a system for capturing unearned bounties.

## Key Claims
- Last-click attribution creates a winner-take-credit boundary that can reward the latest recorded signal rather than the actor that created demand.
- Click injection reacts to a known installation by emitting a synthetic late click before attribution is finalized.
- Click flooding emits many speculative clicks against apps a user might install, increasing the chance of accidental last-click credit.
- Broad device permissions and app-event visibility can supply fraudsters with high-quality timing and intent signals.
- Automatically opening an installed app can force the conversion event needed to trigger payment.
- Routing claims through many ad networks, false app names, or obscured sub-publishers can hide concentration at the true source.
- Costs extend beyond advertisers to legitimate publishers, developers, users, and platforms through diverted revenue, privacy exposure, battery drain, data use, and trust loss.

## Evidence
- Attribution weakness: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] explains that the first app open performs a lookback and credits the last recorded click.
- Reactive injection: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] says Cheetah apps detected downloads, found active offers, and emitted attribution clicks despite supplying no ad.
- Speculative flooding: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] says Kika used Play Store search terms to send clicks for related apps before possible installations.
- Conversion forcing: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] reports that Cheetah apps sometimes launched a newly installed app without user knowledge because payment depended on an open.
- Concealment: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] says Kika Keyboard and one Cheetah app spread claims across more than 20 ad networks and sometimes used false app names.
- Scale and harm: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] reports eight implicated apps with more than 2 billion downloads, $0.50-$3 bounties, and possible advertiser, publisher, developer, battery, data, and privacy costs.

## Counterevidence & Qualifications
The source is a November 2018 journalistic investigation rather than a complete published forensic report. Kochava supplied the primary detection account, Method Media Intelligence corroborated proprietary-code findings, Cheetah denied that its own SDKs performed click injection, Kika denied intent, and Google initially said it had not confirmed fraud. Download counts indicate distribution scale rather than the number of fraudulent events, and market-wide fraud estimates do not establish losses caused by these eight apps.

## What Changed
- Created a unified concept covering click injection, click flooding, conversion forcing, and attribution-source concealment.
- Framed last-click measurement as both an analytics rule and a security-sensitive attack surface.

## Related Concepts
- [[MarketingAttribution]] - supplies the credit-assignment system that fraudulent clicks manipulate.
- [[ProgrammaticAdvertising]] - provides the multi-network adtech environment through which claims can be routed and obscured.
- [[MobileAppStoreEconomics]] - install bounties and store-scale distribution create the economic setting for the fraud.
- [[IdentityResolution]] - device and attribution identifiers connect clicks, installs, opens, networks, and publishers.
- [[PrivacyPovertyDivide]] - permission-heavy software can exchange user privacy and device resources for hidden commercial gain.
