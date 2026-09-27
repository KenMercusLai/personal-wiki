---
title: "Secret"
type: entity
tags: [company, startup, equity, anonymity, privacy, social-networking]
sources:
  - 4-hard-truths-about-equity-while-west
  - demystifying-secret-david-byttow-medium
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[Secret]] was an anonymous social app represented through both its early privacy-and-delivery architecture and its later use as an example of employee-equity disappointment and founder secondary liquidity.

## Current Profile
[[DavidByttow]]'s early account presents Secret as an attempt to spread posts through friends and friends-of-friends without routinely storing real-world identifiers beside message content. Its design used Google-hosted infrastructure, TLS, server-side encryption with off-site key storage, on-device contact hashing, secret-owned ACLs with unique recipient tokens, logically separate user/post/access records, dual-admin access, and delivery thresholds that disclosed more social context only as a user's network grew.

The later equity source supplies a sharply different company outcome lens. It uses Secret to show that employees can hold equity that never becomes useful wealth even when founders obtain liquidity through private secondary transactions. Together, the sources distinguish an ambitious early trust architecture from evidence about the company's eventual compensation asymmetry; neither source provides a complete operational or financial history.

## Key Characteristics
- Distributed anonymous posts through a relevance-ranked social graph rather than broadcasting every post to every contact.
- Used layered identity controls: local contact hashing, tokenized per-recipient access, logical record separation, dual-admin access, and thresholded relationship disclosure.
- Relied on server-side decryption and a shared-salt contact-matching design, leaving the operator and enumerable identifiers inside the trust boundary.
- Serves as a negative employee-equity example tied to founder secondary liquidity and employee illiquidity.

## Evidence
- Social delivery: [[demystifying-secret-david-byttow-medium]] says contacts were one ranking signal, deliveries were unique and reversible, and sparse accounts received fewer posts and less relationship detail.
- Identity controls: [[demystifying-secret-david-byttow-medium]] describes locally hashed contacts, secret-owned ACLs, per-recipient tokens, separate record types, and a two-founder administrative rule.
- Infrastructure protection: [[demystifying-secret-david-byttow-medium]] reports TLS, encrypted datastore writes, an off-site rotating keystore, App Engine, Bigtable-backed storage, and Google Cloud Storage.
- Downside example: [[4-hard-truths-about-equity-while-west]] groups Secret with cases where holding shares did not resemble a winning lottery ticket.
- Founder liquidity and asymmetry: [[4-hard-truths-about-equity-while-west]] links founder secondary sales to Secret while contrasting founders with employees holding small, hard-to-sell positions.

## Qualifications
The architecture source is a founder-authored 2014 explanation rather than an audit. It acknowledges that shared-salt phone-number hashes can be matched if the salt is known, says logical separation adds no physical security, and describes server-side rather than end-to-end encryption. It does not measure deanonymization resistance, insider risk, moderation, retention, or delivery-algorithm outcomes, and its planned AWS migration is not verified here. The equity source mentions Secret briefly and does not independently document the full shutdown, financing, secondary sales, or employee outcomes.

## What Changed
- Added Secret's original product purpose and early storage, identity, administrative-access, and delivery design.
- Qualified its anonymity claims with guessable contact hashes, server-side decryption, shared infrastructure, and absent audit evidence.
- Reframed the company across its early privacy ambition and its later role as an equity-asymmetry example.

## Relationships
- [[EmployeeEquityRisk]] - Secret illustrates the gap between employee equity hopes and realized payout.
- [[StartupEquityTransparency]] - Secret supports disclosure about founder-employee asymmetry and liquidity.
- [[DavidByttow]] - cofounder who documented Secret's early architecture.
- [[AnonymousSocialPrivacyArchitecture]] - Secret is the source case for layered identifier, content, access, and disclosure controls.
- [[Google]] - supplied the app's reported early hosting, datastore, object storage, account, and physical-security substrate.
