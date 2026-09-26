---
title: "CoinHive"
type: entity
tags: [cryptocurrency, browser-mining, web-monetization]
sources:
  - cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Overview
[[CoinHive]] is represented as a browser-based cryptocurrency-mining service that websites could embed to convert visitor CPU work into revenue.

## Current Profile
The October 2017 source describes CoinHive as a newly launched and rapidly adopted browser-mining tool. AdGuard searched for its code alongside JSEcoin in the Alexa top 100,000 sites and found 220 sites that initiated mining from their home pages. The Pirate Bay brought public attention to the service, while Showtime properties were also reported as early adopters before removing the code after media coverage.

CoinHive reportedly asked site operators to disclose mining and obtain permission, but AdGuard argued that the service could not enforce that recommendation or technically prevent stealth use. CoinHive therefore illustrates a platform-governance gap: an embeddable monetization tool can recommend consent while leaving actual disclosure and control to operators, users, blockers, and infrastructure providers.

## Key Characteristics
- Supplied embeddable code for mining cryptocurrency in website visitors' browsers.
- Launched on September 14, shortly before AdGuard's October 2017 measurement.
- Became publicly associated with The Pirate Bay and Showtime browser-mining incidents.
- Recommended that operators notify users and request permission.
- Could not, in AdGuard's account, prevent operators from deploying the miner covertly.

## Evidence
- Adoption signal: [[cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening]] uses CoinHive and JSEcoin signatures to identify 220 mining-enabled sites.
- Public examples: [[cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening]] names The Pirate Bay and Showtime properties among early adopters.
- Governance limit: [[cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening]] reports CoinHive's consent recommendation while arguing that it could not forbid stealth mining.

## Qualifications
This profile rests on one AdGuard-authored snapshot from CoinHive's first month. It does not independently verify deployments, distinguish authorized from unauthorized installations site by site, quantify CoinHive's own revenue, explain its mining protocol, or describe the service's later history. The scan's audience and profit figures apply to the detected group rather than CoinHive alone.

## What Changed
- Created CoinHive as the enabling service and governance example in the browser-mining source.

## Relationships
- [[BrowserCryptomining]] - monetization mechanism implemented through CoinHive's embeddable code.
- [[AdGuard]] - company that scanned for CoinHive and added user-facing controls.
- [[Cloudflare]] - infrastructure provider reported as enforcing consent against mining sites.
- [[WebAdEconomics]] - CoinHive offered websites a resource-based alternative to ad revenue.
