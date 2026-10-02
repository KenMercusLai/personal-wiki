---
title: "PayPal"
type: entity
tags: [company, payments, marketplace]
sources:
  - 51-examples-of-growth-hacking-strategies-techniques-from-the-worlds-most-innovative-businesses
  - yesterdays-failures-are-todays-successes-learning-by-shipping
  - building-products-without-coding-learning-new-stuff-medium
  - graphql-a-success-story-for-paypal-checkout-paypal-engineering-medium
  - uiuc-2018-commencement-address-too-long-to-tweet
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[PayPal]] is a payments company represented through early referral growth, foundational web-payment infrastructure, lightweight prototype payments, a Checkout engineering migration from REST variants to GraphQL, and [[MaxLevchin]]'s retrospective account of its founding team.

## Current Profile
The article says PayPal faced high advertising costs and difficulty partnering with banks, so it paid users to open accounts and refer others. The source reports that this expensive incentive strategy produced high daily growth and helped PayPal become the preferred payment provider on [[EBay]].

A 2016 Learning By Shipping essay adds the infrastructure reading. It lists PayPal among the technologies that separate the mid-2010s from the dot-com era, on the argument that reliable, secure payment and acceptance of money on the web was itself an enabling capability. The [[BugRex]] source makes that role concrete at prototype scale: PayPal.me let customers pay experts directly without a Stripe integration, enabling a willingness-to-pay test while bypassing BugRex's own fee capture.

PayPal Engineering's 2018 Checkout account adds the internal application layer. It says atomic REST calls imposed high tail network costs, server orchestration responses accumulated fields, and a flexible Bulk REST mechanism was too cumbersome for routine developer use. A three-developer mobile-SDK team reportedly shipped within a six-week window using GraphQL schema discovery and parallel UI/API work, followed by adoption across more than 30 applications or teams.

Levchin's 2018 commencement address adds a narrow founding and team perspective. He says he met [[PeterThiel]] after moving to Palo Alto and founded PayPal with him following four failed companies in three years. He attributes the early team's resilience not to being exceptional at formation, but to curiosity, risk tolerance, and members continually raising one another's expectations; he also says many of the first engineers were his University of Illinois classmates.

## Key Characteristics
- Provides account-to-account transfers using email addresses.
- Used cash rewards for both signup and referral.
- Reportedly spent about $60 million on referrals.
- Became closely connected to eBay marketplace payments; Levchin also portrays its early Illinois-linked team as improving through rising mutual expectations.
- Treated as foundational web-payment infrastructure rather than only a growth example, with the essay reporting more than $80 billion processed per quarter.
- PayPal.me can substitute for an integrated payment system in an early service prototype, at the cost of leaving platform payment economics untested.
- Checkout engineering adopted GraphQL after atomic REST, orchestration, and Bulk REST exposed different latency, over-fetching, and developer-usability costs.

## Evidence
- Referral incentive: [[51-examples-of-growth-hacking-strategies-techniques-from-the-worlds-most-innovative-businesses]] says PayPal paid $10 for opening an account and $10 for each referral.
- Growth metric: [[51-examples-of-growth-hacking-strategies-techniques-from-the-worlds-most-innovative-businesses]] reports daily growth between 7% and 10%.
- Marketplace fit: [[51-examples-of-growth-hacking-strategies-techniques-from-the-worlds-most-innovative-businesses]] says PayPal became the preferred payment provider on eBay.
- Enabling payments: [[yesterdays-failures-are-todays-successes-learning-by-shipping]] credits PayPal with making it reliable and secure to pay and accept money on the web, which it says accelerated the spread of web merchants, and reports it processing over $80 billion a quarter.
- Prototype payment: [[building-products-without-coding-learning-new-stuff-medium]] says BugRex chose PayPal.me over a coded Stripe integration and routed money directly from customers to experts.
- Checkout API migration: [[graphql-a-success-story-for-paypal-checkout-paypal-engineering-medium]] reports that a three-developer mobile team completed its work inside six weeks and that more than 30 applications or teams were building or consuming GraphQL one year later.
- Founding and team account: [[uiuc-2018-commencement-address-too-long-to-tweet]] says Levchin founded PayPal with Thiel and that many early engineers were Illinois classmates who pushed one another to improve.

## Qualifications
The source does not calculate referral payback or distinguish the referral program from PayPal's product utility, eBay seller demand, funding capacity, or network effects.

The infrastructure claim comes from a 2016 essay rather than company data, the quarterly figure is a single reported number with no methodology, and the BugRex case proves neither payment safety nor marketplace monetization. The Checkout account is company-authored and supplies no controlled before-and-after performance, conversion, reliability, server-cost, or maintenance data. Levchin's commencement account is motivational, founder-centered, and does not name all team members or isolate team culture from product, timing, capital, distribution, or market conditions. The sources do not establish PayPal's current competitive, organizational, or technical position.

## What Changed
- Added Levchin's account of co-founding PayPal with Peter Thiel after repeated earlier failures.
- Added Illinois classmates and rising mutual expectations as source-bounded early-team characteristics.

## Relationships
- [[GrowthHacking]] - PayPal is the source's clearest paid-referral example.
- [[MarketplaceTrust]] - PayPal reduces payment friction and risk in marketplace transactions.
- [[EBay]] - PayPal's early growth is linked to eBay marketplace usage.
- [[TechnologyEnablerStack]] - payments are one of the enabling layers that made previously impractical web businesses viable.
- [[BugRex]] - used direct PayPal.me payments between customers and experts.
- [[NoCodeProductPrototyping]] - PayPal supplied a borrowed payment capability for the composed MVP.
- [[GraphQL]] - became the client-shaped API layer described for PayPal Checkout and its mobile SDK.
- [[RESTAPI]] - supplied the atomic endpoints, orchestration response, and Bulk REST predecessor patterns.
- [[MaxLevchin]] - identifies PayPal as the eventual success following his earlier failed startups.
- [[PeterThiel]] - named by Levchin as his PayPal co-founder.
- [[UniversityOfIllinoisUrbanaChampaign]] - source of many early engineers in Levchin's account.
- [[StartupTeamBond]] - captures the trust and mutual-improvement interpretation of the early team.
