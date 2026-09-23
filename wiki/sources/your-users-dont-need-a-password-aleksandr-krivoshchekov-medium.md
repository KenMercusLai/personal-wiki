---
title: "Your Users Don't Need a Password"
type: source
tags: [authentication, security, ux, web]
date: 2017-10-30
source_file: /mnt/ken_personal_wiki/Articles/Your users don’t need a password - Aleksandr Krivoshchekov - Medium.md
---

## Summary
[[AleksandrKrivoshchekov]] argues that many websites can replace site-specific passwords with [[EmailMagicLinkAuthentication]]: collect an email address, send a time-limited token link, validate it once, and then establish a normal session. The proposal reduces password creation and storage burden but moves the critical trust boundary to the user's email account and to the site's token, delivery, throttling, and session-handling infrastructure.

## Key Claims
- Email-based account confirmation and password reset already let control of an email inbox authorize sensitive account changes, so some sites can use the same channel as the primary sign-in mechanism.
- A magic-link flow can store an email, token, expiry, activation state, and optionally request IP; a valid request must be unexpired, unused, and optionally the newest token issued for that address.
- Marking a token as activated prevents straightforward replay, after which the application can issue the same cookie or JWT used by a password-based flow.
- Rate limiting token requests, such as suppressing repeated mail for ten minutes, can reduce email spam and brute-force pressure.
- The author recommends the method for many content, forum, corporate, billing, and infrequently used sites, but not for email providers and not necessarily for mobile, smart-TV, or IoT clients where cross-device email navigation can be awkward.
- The design avoids maintaining another reusable password database, but it does not eliminate authentication risk; it concentrates security and availability dependence on email control and the link-token lifecycle.

## Key Quotes
> "You only need to know user's email." - the article's concise case for replacing a site password with proof of inbox control.

> "If such a token exists; (AND) it isn't expired; (AND) not used" - the core acceptance conditions for an email sign-in request.

## Connections
- [[AleksandrKrivoshchekov]] - author of the passwordless sign-in proposal.
- [[EmailMagicLinkAuthentication]] - the article's central authentication method.
- [[AuthenticationInfrastructure]] - email delivery, token state, throttling, and session issuance become critical parts of the login path.

## Contradictions
- No direct contradiction with the current wiki was found. The source complements [[AuthenticationInfrastructure]] by describing a small application-level login flow rather than a large hosted identity platform.
- The article's broad claims that passwords are inherently inefficient and that modern email services are much more secure than ordinary websites are not demonstrated with comparative evidence. Inbox compromise, phishing, link leakage, shared-device use, delivery delay, and email-provider outages remain material qualifications.
