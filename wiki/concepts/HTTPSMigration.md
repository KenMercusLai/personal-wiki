---
title: "HTTPS Migration"
type: concept
tags: [https, tls, security, infrastructure, migration]
sources:
  - nick-craver-https-on-stack-overflow-the-end-of-a-long-road
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[HTTPSMigration]] is the coordinated transition of a web system's domains, certificates, edge routing, applications, identity, content, internal traffic, and rollout controls from HTTP to HTTPS.

## Current Synthesis
The [[StackOverflow]] case shows that migration complexity grows with domain count, legacy URLs, user-submitted content, shared cookies, third-party services, internal APIs, and performance-sensitive traffic. The certificate is only one dependency. Domain topology must be certifiable; externally hosted subdomains must not inherit sensitive cookies; applications and user content must stop creating mixed content; redirects and canonical URLs must preserve search behavior; and edge routing must not send internal calls on avoidable public detours.

The safest sequence is incremental and evidence-led. First make development match production, block new insecure content, establish browser measurements and integration tests, deploy behind reversible feature flags and inactive load balancers, test temporary redirects, and observe small representative sites before permanent redirects or HSTS. Performance can support the business case because TLS enables browser use of HTTP/2 and local edge termination reduces handshake distance, but those gains depend on the actual certificate, DNS, CDN, and connection architecture.

## Key Claims
- HTTPS migration is a cross-layer systems program, not a certificate-installation task.
- Domain and cookie boundaries constrain certificate design, login architecture, third-party hosting, and HSTS policy.
- Mixed-content work should first prevent new insecure references and then remediate the backlog by measured prevalence and risk.
- Real-user monitoring and configuration integration tests answer different questions and are both needed.
- Reversible staging should precede permanent 301 redirects, HSTS, and network-wide activation.
- CDN and proxy changes can reduce global TLS latency but also alter DNS, caching, internal API paths, and failure modes.
- Historical protocol and provider choices require re-evaluation rather than direct copying.

## Evidence
- Cross-layer scope: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] links certificates, DNS, login, cookies, applications, user content, ads, websockets, APIs, redirects, and search migration.
- Domain constraints: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] explains why `*.stackexchange.com` could not cover four-level child-meta names and why moving them affected login and HSTS.
- Measurement and testing: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] combines browser timings, a test domain, httpUnit configuration checks, secondary load balancers, and staged site rollout.
- Content remediation: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] reports blocking new insecure embeds before upgrading or unlinking legacy resources.
- Failure evidence: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] documents protocol-blind redirect caching, internal API detours, and an incorrect content backfill.

## Counterevidence & Qualifications
The evidence is one large platform's first-party 2017 account. Smaller systems may not share its domain, cookie, traffic, advertising, websocket, or single-origin constraints. Current TLS versions, HSTS requirements, certificate automation, browser policy, HTTP/2 behavior, and CDN capabilities must be checked against current standards and providers; HPKP and server-push discussion in particular is historical.

## What Changed
- Created a systems-level migration concept from Stack Overflow's certificate, edge, application, content, identity, and rollout work.
- Distinguished performance telemetry from configuration correctness testing.
- Made irreversible browser and redirect state a reason for staged activation.

## Related Concepts
- [[HTTP2]] - browser HTTP/2 availability supplied a performance incentive for HTTPS in the source.
- [[WebPerformanceOptimization]] - handshake distance, round trips, connection reuse, and edge placement shape migration performance.
- [[ChangeSafety]] - reversible rollout and observation should precede permanent redirect and HSTS state.
- [[NetworkAutomation]] - DNS and edge configuration must stay synchronized across providers and environments.
- [[AuthenticationInfrastructure]] - shared login and cookie scope constrain safe domain topology.
