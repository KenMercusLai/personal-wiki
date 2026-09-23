---
title: "Aleksandr Krivoshchekov"
type: entity
tags: [author, authentication, web-development]
sources:
  - your-users-dont-need-a-password-aleksandr-krivoshchekov-medium
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[AleksandrKrivoshchekov]] is represented in the wiki as the author of a 2017 implementation essay advocating email magic links in place of passwords for many websites.

## Current Profile
The available source presents Krivoshchekov as a practitioner explaining an application-level authentication design. His argument combines a user-experience critique of password creation with a concrete token flow: record an email sign-in request, deliver a callback link, validate expiry and one-time use, activate the request, and issue a session. The wiki does not infer a broader biography or security-research role from this single article.

## Key Characteristics
- Advocates replacing site-specific passwords with proof of email-inbox control for suitable services.
- Frames password storage as both an application liability and a user-experience burden.
- Specifies expiry, one-time activation, newest-request checks, and rate limiting around sign-in tokens.
- Treats deployment context as material, excluding email providers and qualifying device-centered products.

## Evidence
- Authorship and thesis: [[your-users-dont-need-a-password-aleksandr-krivoshchekov-medium]] identifies Krivoshchekov as the author and argues that many users do not need a site password.
- Implementation focus: [[your-users-dont-need-a-password-aleksandr-krivoshchekov-medium]] describes token issuance, callback validation, activation state, request IP, and session creation.
- Scope judgment: [[your-users-dont-need-a-password-aleksandr-krivoshchekov-medium]] distinguishes suitable websites and occasional-use services from email, mobile, smart-TV, and IoT contexts.

## Qualifications
The wiki has one source by Krivoshchekov, so this profile is intentionally source-bound. The essay makes broad security comparisons without measurements or independent evidence, and the database table definitions referenced in its prose are absent from the captured Markdown.

## What Changed
- Created a source-bounded profile of Krivoshchekov as the author of an email magic-link authentication proposal.

## Relationships
- [[EmailMagicLinkAuthentication]] - authentication approach he advocates and sketches.
- [[AuthenticationInfrastructure]] - broader technical context for the token and session flow he describes.
