---
title: "Email Magic-Link Authentication"
type: concept
tags: [authentication, passwordless, email, security, ux]
sources:
  - your-users-dont-need-a-password-aleksandr-krivoshchekov-medium
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[EmailMagicLinkAuthentication]] is a passwordless sign-in method in which an application sends a short-lived, single-use link to an email address and treats successful use of its token as proof that the user controls that inbox.

## Current Synthesis
The method removes the need for a site-specific reusable password and can make occasional sign-in easier, especially where email already governs account confirmation and password recovery. A minimal flow records a token request, sends the callback link, accepts only a matching token that is current, unexpired, and unused, marks it used, and then establishes a normal application session.

This is a relocation of trust rather than the removal of authentication. Security and usability now depend on the user's email account, message delivery, token entropy and lifetime, single-use enforcement, request throttling, callback handling, and session security. The fit is therefore contextual: an occasional-use website may benefit, while an email provider or device that makes switching to an inbox difficult may not.

## Key Claims
- Email control can serve as the primary authentication factor when it already controls account confirmation and recovery.
- Tokens should be hard to guess, short-lived, single-use, and optionally superseded by the newest request for the same address.
- A successful callback still needs a conventional session mechanism such as a cookie or JWT.
- Request throttling is needed to limit inbox spam and repeated token attempts.
- Passwordless sign-in trades local password-management risk and friction for dependence on email-account security and delivery reliability.

## Evidence
- Existing trust boundary: [[your-users-dont-need-a-password-aleksandr-krivoshchekov-medium]] observes that email confirmation and password-reset links already make inbox control decisive for many accounts.
- Token lifecycle: [[your-users-dont-need-a-password-aleksandr-krivoshchekov-medium]] requires the presented token to exist, remain unexpired and unused, and optionally be the latest request for the email address.
- Replay and session transition: [[your-users-dont-need-a-password-aleksandr-krivoshchekov-medium]] marks the request with an activation time before issuing a cookie or JWT.
- Abuse control: [[your-users-dont-need-a-password-aleksandr-krivoshchekov-medium]] proposes request-IP storage and a ten-minute email-send interval for rate limiting.
- Contextual fit: [[your-users-dont-need-a-password-aleksandr-krivoshchekov-medium]] recommends the flow for many websites and infrequently used services while excluding email services and qualifying mobile, smart-TV, and IoT use.

## Counterevidence & Qualifications
The source is a short 2017 implementation essay rather than a security evaluation, and its exported database table definitions are missing. It does not analyze inbox compromise, phishing, forwarded or leaked links, link scanners, shared devices, email enumeration, delivery failures, token storage, session fixation, or multi-factor recovery. Its assertion that email providers are categorically better protected than ordinary sites may often be directionally plausible but is not established by evidence in the article. Email magic links should therefore be evaluated as one authentication design with shifted failure modes, not as authentication without credentials or risk.

## What Changed
- Created the concept as a bounded account of email-link sign-in and its required token lifecycle.
- Made explicit that password removal transfers the trust boundary to email and application session infrastructure.

## Related Concepts
- [[AuthenticationInfrastructure]] - magic-link delivery, validation, and session creation are components of the login critical path.
- [[WeakCredentialExposure]] - removing a site-specific password avoids one reusable credential store but does not remove account-takeover risk.
- [[EmailLayoutAndStructure]] - the authentication message must present a usable link across email clients, though visual design is secondary to security.
