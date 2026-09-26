---
title: "AdGuard"
type: entity
tags: [privacy, ad-blocking, browser-security, cryptocurrency]
sources:
  - cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Overview
[[AdGuard]] is represented in the source as an ad-blocking and privacy-software company that studied early browser cryptocurrency mining and added user-facing controls for it.

## Current Profile
In October 2017, AdGuard reported scanning the Alexa top 100,000 websites for CoinHive and JSEcoin code. It found 220 main pages that initiated mining and used third-party audience estimates to place their collective reach at 500 million people. The company positioned itself as both researcher and product vendor: its apps warned when a site attempted to mine and let the user allow or block the script.

AdGuard's policy distinguished browser mining from undisclosed cryptojacking. It argued that mining could become a legitimate alternative to advertising when a site asks first and offers an opt-out, while warnings and blocking should expose and prevent hidden use. That framing is historically useful but comes from AdGuard's own product and advocacy context rather than an independent prevalence study.

## Key Characteristics
- Conducted a code-signature scan for CoinHive and JSEcoin across the Alexa top 100,000 websites.
- Reported 220 mining-enabled home pages with a combined estimated audience of 500 million people.
- Added warnings that let users allow or block detected browser-mining scripts.
- Treated disclosure, permission, and opt-out as the boundary between potentially legitimate mining and abuse.
- Favored user choice over silently blocking every browser miner by default.

## Evidence
- Measurement role: [[cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening]] describes AdGuard's top-100,000 scan and reported detection count.
- Product behavior: [[cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening]] says AdGuard warned users and offered an allow-or-block choice.
- Policy position: [[cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening]] argues for consent-based browser mining rather than a categorical ban.

## Qualifications
The evidence is one AdGuard-authored 2017 article and does not independently validate its scanner coverage, traffic inputs, revenue model, false-positive rate, or product effectiveness. The stated 500 million figure is aggregate estimated site audience, not a verified count of users whose devices mined cryptocurrency. The profile does not describe AdGuard's current products, policies, ownership, or market position.

## What Changed
- Created AdGuard's profile around its early browser-mining measurement, product response, and consent position.

## Relationships
- [[BrowserCryptomining]] - practice AdGuard measured and exposed through user controls.
- [[CoinHive]] - browser-mining service whose code AdGuard searched for.
- [[AdBlocking]] - AdGuard extends blocking software from advertising into undisclosed mining scripts.
- [[WebAdEconomics]] - AdGuard frames consensual mining as a possible advertising alternative.
- [[Cloudflare]] - separate enforcement layer reported as suspending non-consensual mining sites.
