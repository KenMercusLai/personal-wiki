---
title: "Cloudflare"
type: entity
tags: [cloud, edge, hosting, dns, storage]
sources:
  - wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai
  - 2023-focusing-on-a-single-product-pays-off
  - cloudflare-outage-on-february-20-2026
  - cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening
  - nick-craver-https-on-stack-overflow-the-end-of-a-long-road
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[Cloudflare]] is an edge-infrastructure company represented in the sources through low-cost hosting, DNS, security, compute, data, and storage services; policy enforcement against undisclosed browser mining; employment and product-development context; and a first-party account of a serious network-configuration outage.

## Current Profile
The migration article frames Cloudflare as both a Vercel alternative and a broader service-substitution platform. Pages can deploy Next.js projects, while DNS, security features, Workers, D1, and R2 can replace or complement services bought from Vercel, AWS, Supabase, or other providers. Rozen's retrospective adds an organizational angle: Cloudflare employment can support slow independent SaaS building, and internal D1 work can draw on product and writing skills developed outside the company.

The February 2026 postmortem adds the platform's operational risk boundary. Cloudflare's Addressing API was the authoritative source for customer IP configuration and propagated changes to its global edge. A newly automated BYOIP cleanup task sent an ambiguous empty-valued query, received all prefixes rather than only pending deletions, and withdrew about 1,100 customer prefixes before being stopped. Recovery took six hours and seven minutes because some records also lost service bindings and required a global configuration rollout, showing that a low-cost global edge platform also concentrates configuration-state and change-control risk.

An earlier 2017 AdGuard source adds an infrastructure-governance role. It reports that Cloudflare suspended accounts and denied service to sites that mined cryptocurrency in visitors' browsers without permission. The brief account shows how an infrastructure intermediary can enforce a consent norm that an embeddable mining provider could recommend but not guarantee.

The [[StackOverflow]] HTTPS retrospective supplies a historical customer case. Cloudflare was chosen for local TLS termination, DDoS protection, CDN delivery, globally distributed DNS, responsiveness, and the promise of Railgun. Real-user tests found slightly slower page loads in the US and Canada but equal or better results elsewhere. Stack Overflow later retired Railgun after prolonged instability and moved to [[Fastly]] when programmable edge behavior, propagation speed, and automated configuration better matched its needs.

## Key Characteristics
- Offers low-cost or free-tier-friendly website infrastructure for small independent projects.
- Provides Pages, Workers, DNS, security controls, D1, and R2 across hosting, compute, database, and storage needs.
- Requires edge-runtime compatibility work for Next.js applications.
- Operates authoritative addressing workflows in which customer configuration can propagate to BGP routers and edge machines.
- Has committed to typed API schemas, desired-versus-operational-state separation, staged health-mediated snapshots, and circuit breakers after the 2026 BYOIP outage.
- Was reported in 2017 as suspending service for websites that conducted browser mining without user permission.
- Historically supplied Stack Overflow with distributed DNS, CDN, DDoS protection, proxying, and local TLS termination before its move to Fastly.

## Evidence
- Platform breadth and cost: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] describes Pages, Workers, DNS, security controls, D1, and R2 as a lower-cost service combination.
- Compatibility boundary: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] says Cloudflare-hosted Next.js projects must use edge runtime and replace incompatible Node.js APIs.
- Employment and D1 work: [[2023-focusing-on-a-single-product-pays-off]] says Cloudflare employment enabled Rozen's patient work on [[OnlineOrNot]] and connected him to a founding-engineer role on [[CloudflareD1]].
- Authoritative network configuration: [[cloudflare-outage-on-february-20-2026]] says Addressing API changes trigger operational workflows that propagate IP advertisement and product binding changes to the global edge.
- Outage scale and recovery: [[cloudflare-outage-on-february-20-2026]] reports about 1,100 withdrawn BYOIP prefixes, roughly 300 prefixes requiring manual/global configuration recovery, and a six-hour-seven-minute incident.
- Remediation direction: [[cloudflare-outage-on-february-20-2026]] proposes schema standardization, snapshots, health gates, configured/operational-state separation, and broad-change circuit breakers.
- Consent enforcement: [[cryptocurrency-mining-affects-over-500-million-people-and-they-have-no-idea-it-is-happening]] reports that Cloudflare suspended sites that mined through visitor browsers without permission.
- Stack Overflow deployment: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] says distributed DNS improved user-local lookup performance and proxy tests were neutral or faster outside a slight US/Canada regression.
- Railgun boundary: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] says its diffing and persistent-connection design could improve performance but the deployment's instability eventually cost more than it saved.

## Qualifications
These sources are not a comprehensive or independent Cloudflare assessment. The low-cost migration source is strongly favorable but leaves service-migration questions unresolved; Rozen describes Cloudflare mainly as employer and work context. The Stack Overflow comparison reflects one large customer's 2017 requirements, legacy deployment, and provider capabilities, so it should not be generalized to current products. The 2017 enforcement claim is a short second-party report that does not identify affected accounts, policy language, consistency, appeals, or outcomes. The outage account is Cloudflare's own postmortem, supplies no independent customer-impact measure, and describes remediation commitments rather than completed controls. Its timeline also distinguishes website failures from DNS: one.one.one.one returned 403 errors, but 1.1.1.1 resolver traffic, including DNS over HTTPS, remained available.

## What Changed
- Added the historical Stack Overflow case for distributed DNS, CDN, DDoS protection, proxying, and edge TLS.
- Added real-user regional performance evidence and Railgun's eventual operational rejection.
- Distinguished Cloudflare's integrated model from Fastly's more programmable edge model in one 2017 customer's account.

## Relationships
- [[Vercel]] - Cloudflare Pages is presented as a lower-cost managed alternative to Vercel.
- [[NextJS]] - Cloudflare can host Next.js projects when adapted for edge runtime.
- [[EdgeRuntime]] - Cloudflare's Next.js support is constrained by edge-runtime compatibility.
- [[CloudCostOptimization]] - Cloudflare is used for service consolidation and cost reduction.
- [[CloudflareD1]] - Cloudflare database product where Rozen became a founding engineer.
- [[MaxRozen]] - Cloudflare employment made Rozen's patient SaaS work possible.
- [[ChangeSafety]] - Cloudflare's BYOIP outage demonstrates the need for staged, health-mediated configuration changes.
- [[NetworkAutomation]] - Cloudflare automates customer prefix and edge-configuration workflows through APIs.
- [[BrowserCryptomining]] - Cloudflare is reported as enforcing a user-consent boundary at the infrastructure layer.
- [[StackOverflow]] - historical customer that used Cloudflare during its HTTPS and proxy transition.
- [[Fastly]] - provider Stack Overflow later selected for programmable edge behavior and automation.
- [[HTTPSMigration]] - Cloudflare supplied several edge capabilities needed during the migration.
