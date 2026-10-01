---
title: "HTTPS on Stack Overflow: The End of a Long Road"
type: source
tags: [https, infrastructure, web-performance, cdn, security]
date: 2017-05-22
source_file: "/mnt/ken_personal_wiki/Articles/Nick Craver - HTTPS on Stack Overflow- The End of a Long Road.md"
---

## Summary
[[NickCraver]] recounts [[StackOverflow]]'s four-year transition to HTTPS-by-default across a multi-domain, multi-tenant network with user content, advertising, APIs, websockets, and a single active data-center origin. The migration joined certificate and domain redesign, [[Cloudflare]] and later [[Fastly]] edge delivery, [[HAProxy]] TLS termination, real-user performance measurement, mixed-content cleanup, application refactoring, and staged search-impact testing. The case argues that HTTPS at this scale was a dependency-management and systems-migration program whose security benefits became easier to justify when paired with [[HTTP2]] performance and DDoS resilience. Its protocol support, HPKP discussion, provider capabilities, and unfinished work describe the 2017 deployment state rather than current guidance.

## Key Claims
- HTTPS deployment across hundreds of domains required coordinated changes to certificates, DNS, cookies, login, application URLs, user content, ads, APIs, websockets, redirects, and edge infrastructure.
- Moving child meta sites under `*.meta.stackexchange.com` avoided an impossible multi-label wildcard pattern, but required universal login and left legacy-domain complications for HSTS preloading.
- A combined certificate and shared edge IPs were chosen partly to preserve non-SNI compatibility and enable cross-origin [[HTTP2]] connection reuse and planned server push.
- Real-user browser timings from about 5% of traffic gave Stack Overflow billions of measurements for comparing DNS, proxy, and page-load performance across regions.
- [[Cloudflare]] improved global DNS and proxy performance but Railgun's operating cost and instability outweighed its benefit; [[Fastly]] was later selected for programmable VCL, rapid propagation, and automated configuration.
- Mixed-content cleanup followed a stop-then-drain sequence: block new insecure embeds, upgrade known URLs, and convert the small remainder of unsupported images to links rather than proxying them.
- Staged feature flags, secondary load balancers, integration tests, temporary redirects, canonical URL changes, and search-impact monitoring limited rollout risk.
- The migration exposed systemic mistakes, including protocol-relative URLs in non-web contexts, internal API traffic detouring through the CDN, protocol-blind cached redirects, and a faulty Help Center backfill.

## Key Quotes
> "The activation of this is quite literally flipping a switch" - on the small final action after years of prerequisite work.

> "Plug the hole, then drain the ship." - on stopping new mixed content before cleaning the backlog.

## Connections
- [[NickCraver]] - author and Stack Overflow infrastructure engineer describing the migration.
- [[StackOverflow]] - multi-site platform whose Q&A network moved to HTTPS by default.
- [[HTTPSMigration]] - coordinated security, networking, application, content, and rollout program described by the source.
- [[HTTP2]] - performance motivation involving multiplexing, header compression, fewer connections, and planned server push.
- [[Fastly]] - final CDN/proxy provider selected for programmable edge control and automation.
- [[Cloudflare]] - earlier DNS, CDN, DDoS, and proxy provider whose Railgun deployment was ultimately retired.
- [[HAProxy]] - local TLS terminator and load balancer using separate HTTP and HTTPS processes and abstract sockets.

## Contradictions
- No direct contradiction was found. The source qualifies simplistic accounts of HTTPS as certificate installation by documenting cross-layer dependencies and migration risk.
- The article is a first-party 2017 retrospective. TLS 1.0/1.1 support, HPKP evaluation, HTTP/2 server-push plans, browser behavior, CDN features, and provider comparisons should not be treated as current recommendations.
- Reported performance, traffic, websocket, and HSTS redirect figures are operational snapshots without independent verification or a published dataset.

## Image Notes
The Markdown contains no effective image embeds, although the prose refers to architecture diagrams, timing dashboards, certificate screenshots, and an HAProxy dashboard. Those visuals were unavailable for inspection, so no claims were inferred from them and the visual evidence is incomplete.
