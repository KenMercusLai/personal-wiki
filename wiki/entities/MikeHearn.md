---
title: "Mike Hearn"
type: entity
tags: [software-engineering, authentication, account-security]
sources:
  - building-account-systems-mikes-blog
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Overview
[[MikeHearn]] is a software engineer and practitioner-author represented here by a 2017 account-system design essay informed by his earlier work on Google's unified account system and anti-hijacking.

## Current Profile
Hearn presents authentication as a lifecycle and operations problem rather than a login-form feature. His advice favors outsourcing identity where possible, avoiding site-specific passwords and secret questions, treating CAPTCHAs as limited throttles, accounting for multi-factor recovery and support, retaining a server-side forced-logout path, and protecting transactional email deliverability from marketing reputation.

## Key Characteristics
- Draws account-security guidance from work on Google's unified account system and anti-hijacking.
- Treats build-versus-buy as the first authentication architecture decision.
- Connects security controls to usability, deliverability, support cost, and operational failure modes.
- Uses deliberately strong defaults while acknowledging that devices and target markets constrain passwordless methods.

## Evidence
- Practitioner background: [[building-account-systems-mikes-blog]] says Hearn worked on Google's unified account system, specifically anti-hijacking.
- Outsourcing position: [[building-account-systems-mikes-blog]] recommends federated identity because modern account systems accumulate recovery, abuse, MFA, notification, profile, and multi-device obligations.
- Lifecycle scope: [[building-account-systems-mikes-blog]] discusses identifiers, passwordless login, recovery, CAPTCHAs, 2FA, session renewal and invalidation, email reputation, and credential-database value.
- Contextual qualification: [[building-account-systems-mikes-blog]] notes that email-link login is awkward on televisions and game consoles and that phone-only users may require code-based sign-in.

## Qualifications
This profile is grounded in one 2017 practitioner essay rather than a complete biography or current security standard. Its absolute recommendations are useful provocations but do not independently compare federation, passkeys, regulated environments, privacy requirements, provider lock-in, account portability, or later authentication guidance.

## What Changed
- Created the entity as the authorial and practitioner context for the account-system guidance.

## Relationships
- [[Google]] - Hearn says he worked on Google's unified account and anti-hijacking systems.
- [[AuthenticationInfrastructure]] - his article treats authentication as a broad production lifecycle.
- [[EmailMagicLinkAuthentication]] - he recommends inbox-based sign-in when full third-party federation is unsuitable.
