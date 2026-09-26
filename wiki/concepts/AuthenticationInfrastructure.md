---
title: "Authentication Infrastructure"
type: concept
tags: [identity, authentication, infrastructure, reliability]
sources:
  - a-look-at-auth0-cloud-architecture-5-years-in
  - your-users-dont-need-a-password-aleksandr-krivoshchekov-medium
  - valentin-mouret-simple-authentication-with-only-postgresql
  - building-account-systems-mikes-blog
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[AuthenticationInfrastructure]] is the application and production infrastructure that keeps identity, login, recovery, authorization, sessions, sign-out, abuse controls, credential or token validation, and related account workflows secure, available, scalable, extensible, and observable.

## Current Synthesis
The sources describe authentication at several different scales. [[Auth0]] treats it as a shared production critical path: once many applications depend on a hosted identity service, reliability work spreads across routing, services, data stores, queues, custom-code execution, CDN behavior, deployments, tests, monitoring, logs, alerts, and operational playbooks. [[AleksandrKrivoshchekov]] shows that even a small passwordless flow creates its own critical chain: email delivery, durable token state, expiry and replay checks, abuse throttling, callback handling, and session issuance. [[ValentinMouret]] supplies the smallest password-based case, where PostgreSQL creates and verifies salted bcrypt hashes inside the database. [[MikeHearn]] widens the boundary beyond login implementation to identifiers, recovery, signup and brute-force abuse, multi-factor support, session revocation, device fit, and transactional-email reputation.

Authentication architecture therefore begins with a trust-and-ownership decision: operate the lifecycle locally, delegate it to a specialist service, or federate proof from an identity provider. Core flows must tolerate infrastructure failure, while every credential or proof mechanism creates specific dependencies, recovery paths, support burdens, and abuse paths. Removing a local password shifts security and availability toward an email, phone, or identity-provider account plus token and session handling. Keeping a password requires secure adaptive hashing and careful verification, but hashing alone does not provide recovery, throttling, sessions, multi-factor authentication, sign-out, or safe SQL function design. Outsourcing can reduce implementation burden without eliminating provider dependency, privacy, portability, outage, or account-recovery risk.

## Key Claims
- Authentication is a lifecycle spanning identity, recovery, abuse controls, multi-factor support, sessions, sign-out, notifications, and deliverability rather than only credential verification.
- Teams should explicitly choose which parts of that lifecycle to own, delegate to a specialist platform, or federate to an external identity provider.
- Authentication systems become shared critical infrastructure when downstream applications depend on login and authorization paths.
- High availability requires coordinated routing, application, data, queue, testing, monitoring, and recovery layers.
- Authentication-method choices relocate dependencies: email links depend on inbox control and delivery, federation depends on providers, and passwords depend on protected storage and recovery.
- Session design needs both low-friction continuity and a server-side way to invalidate stolen or administratively revoked sessions.
- Database-resident password verification can be compact, but a salted hash is only one control inside the larger account-security lifecycle.

## Evidence
- Critical product scope: [[a-look-at-auth0-cloud-architecture-5-years-in]] describes Auth0 as authentication, authorization, and SSO for mobile, web, native, IoT, and internal applications.
- Layered platform: [[a-look-at-auth0-cloud-architecture-5-years-in]] lists application services, MongoDB, Elasticsearch, Redis, PostgreSQL, Kinesis, RabbitMQ, SNS, SQS, rate limiting, bcrypt clusters, feature flags, AWS load balancers, and NGINX proxies.
- Failover maturity: [[a-look-at-auth0-cloud-architecture-5-years-in]] says some services can work with stale data while core functionality keeps working during failover.
- Extensibility: [[a-look-at-auth0-cloud-architecture-5-years-in]] describes Auth0 Extend clusters using EC2 auto-scaling groups, Docker containers, and custom proxies to run customer logic during login transactions.
- Flow testing: [[a-look-at-auth0-cloud-architecture-5-years-in]] describes Selenium and CodeceptJS functional tests across API endpoints, authentication flows, identity providers, and deployment phases.
- Passwordless flow: [[your-users-dont-need-a-password-aleksandr-krivoshchekov-medium]] describes issuing a token by email, accepting it only while current, unexpired, and unused, marking it activated, and then creating a cookie or JWT session.
- Abuse boundary: [[your-users-dont-need-a-password-aleksandr-krivoshchekov-medium]] proposes request-IP storage and send throttling, while implicitly making inbox control and mail delivery part of the authentication critical path.
- Password storage: [[valentin-mouret-simple-authentication-with-only-postgresql]] demonstrates per-record bcrypt salts and verification through PostgreSQL `pgcrypto` rather than retaining plaintext passwords.
- Minimal-system boundary: [[valentin-mouret-simple-authentication-with-only-postgresql]] excludes recovery and other lifecycle controls, and its final function contains identifier, volatility, and null-result defects that separate a sound hashing primitive from a safe authenticator.
- Lifecycle scope: [[building-account-systems-mikes-blog]] enumerates recovery, verification, brute-force defense, multi-factor authentication, hijacking protection, preferences, multi-device sign-in, notifications, and phone-only sign-in as expected account-system capabilities.
- Ownership boundary: [[building-account-systems-mikes-blog]] recommends federated sign-in or specialist providers because implementing and supporting the complete lifecycle is expensive and security-sensitive.
- Session revocation: [[building-account-systems-mikes-blog]] distinguishes local cookie deletion from server-side invalidation and proposes silently renewed short-lived cookies that periodically consult forced-logout state.
- Operational dependencies: [[building-account-systems-mikes-blog]] connects 2FA to delivery and recovery support and warns that marketing complaints can damage the deliverability of verification and recovery mail.

## Counterevidence & Qualifications
The Auth0 material is a single vendor architecture narrative and does not imply that every product needs Auth0-scale redundancy. Both passwordless essays are 2017 practitioner arguments rather than comparative security assessments; they underdevelop inbox compromise, phishing, link leakage, scanners, shared-device risks, email enumeration, provider lock-in, identity-provider account loss, privacy, portability, and regulated use. Hearn's advice not to expire sessions is internally narrowed by his later recommendation for short-lived, silently renewed cookies, and his claim that a site password adds no security when email recovery exists does not cover deliberately layered or risk-scored systems. The PostgreSQL tutorial is likewise not production-ready: its fast SHA-256 step is only pedagogical, its bcrypt cost is implicit, and its final SQL function is flawed. Appropriate authentication infrastructure depends on the application's threat model, customer dependency, traffic, client context, recovery design, credential-upgrade path, provider concentration, and outage cost.

## What Changed
- Expanded the account-system boundary to include identifiers, recovery, abuse defenses, multi-factor support, session invalidation, support, and transactional-email deliverability.
- Added build, specialist-platform, and federated-identity ownership choices while making their transferred risks explicit.
- Reconciled persistent user sessions with short-lived cookie renewal and server-side forced-logout checks.

## Related Concepts
- [[CloudHighAvailability]] - authentication infrastructure depends on multi-AZ and cross-region resilience.
- [[SystemReliability]] - identity reliability spans code, architecture, data, tests, monitoring, and incident response.
- [[DeploymentAutomation]] - identity-service changes need controlled rollout and rollback.
- [[ServiceObservability]] - login systems need metrics, probes, logs, alerts, and escalation paths.
- [[InternalDeveloperPlatform]] - platform defaults can make identity-service operations more consistent.
- [[EmailMagicLinkAuthentication]] - passwordless email links depend on delivery, token validation, replay prevention, and session creation.
- [[PasswordHashing]] - password-based login depends on secure credential storage and verification before the wider session lifecycle begins.
- [[PostgreSQL]] - pgcrypto can host the source's compact bcrypt verification mechanism.
- [[Google]] - supplies the unified-account experience behind Hearn's advice and one of his federated sign-in examples.
