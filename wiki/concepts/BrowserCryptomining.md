---
title: "Browser Cryptomining"
type: concept
tags: [cryptocurrency, browsers, monetization, consent, security]
sources:
  - cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Definition
[[BrowserCryptomining]] is the use of code running in a visitor's web browser to perform cryptocurrency-mining computation, allowing a website or script operator to monetize the visitor's CPU time and device energy.

## Current Synthesis
The AdGuard source presents browser mining as neither automatically legitimate nor automatically malicious. Its ethical status turns on control: a site can propose an explicit exchange in which visitors knowingly contribute computation instead of attention or payment, but hidden execution appropriates resources without informed agreement. Because an embeddable service's policy cannot guarantee operator behavior, governance is distributed across site disclosure, affirmative user choice, browser or security-product controls, and infrastructure enforcement.

The source's measurement shows early reach rather than durable viability. AdGuard found mining code on 220 of the Alexa top 100,000 home pages and estimated those sites' aggregate audience at 500 million, yet estimated only US$43,000 in combined revenue over three weeks and noted that large audiences and long sessions were advantageous. This makes browser mining a useful historical case in alternative web monetization, consent, and platform enforcement, but not evidence that it became a scalable replacement for advertising.

## Key Claims
- Browser mining converts visitor computation and energy into a website-side revenue input.
- Hidden execution is ethically distinct from an explicit, informed, and revocable exchange.
- Large audiences and long open sessions improve the economics, making video and streaming sites attractive deployments.
- A service provider's consent recommendation is insufficient when site operators can still embed the code covertly.
- User warnings, blocking software, antivirus detection, and infrastructure sanctions create overlapping enforcement layers.
- Early detected reach does not by itself establish unique affected users, realized mining sessions, profitability, or lasting adoption.

## Evidence
- Early prevalence: [[cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening]] reports 220 detections among 100,000 high-traffic sites.
- Economic scale: [[cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening]] estimates more than US$43,000 in combined revenue across three weeks and emphasizes audience scale and session duration.
- Consent boundary: [[cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening]] argues that sites should ask first and let users opt out.
- Enforcement layers: [[cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening]] describes AdGuard controls, blockers, antivirus products, and Cloudflare sanctions.
- Advertising comparison: [[cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening]] contrasts CPU use with advertising's demands on attention, bandwidth, battery, and personal data.

## Counterevidence & Qualifications
The evidence is a company-authored October 2017 scan using two detectable code signatures and third-party audience estimates. It provides no session telemetry, unique-user count, false-positive analysis, device-level resource measurements, revenue audit, profitability baseline, consent-rate data, or longitudinal outcome. The 500 million figure is aggregate site audience and should not be restated as 500 million confirmed miners. The ethical comparison with advertising also does not establish that browser mining is less harmful: device capability, electricity cost, battery degradation, accessibility, disclosure design, and the ability to withdraw consent can vary materially.

## What Changed
- Created browser cryptomining as a consent-governed web-monetization mechanism rather than treating every implementation as equivalent.
- Separated aggregate audience reach from verified exposure and execution.
- Added layered enforcement across sites, tools, users, and infrastructure providers.

## Related Concepts
- [[WebAdEconomics]] - incumbent attention-funded model that browser mining was proposed to supplement or replace.
- [[AdBlocking]] - user-agent enforcement category extended to mining-script detection and control.
- [[CoinHive]] - embeddable service central to the source's early adoption account.
- [[AdGuard]] - researcher and product vendor offering allow-or-block controls.
- [[Cloudflare]] - infrastructure provider reported as sanctioning mining without permission.
