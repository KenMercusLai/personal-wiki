---
title: "Hacking law firms with abandoned domain names"
type: source
tags: [cybersecurity, domain-names, email, authentication, legal-services]
date: 2018-08-22
source_file: /mnt/ken_personal_wiki/Articles/Hacking law firms with abandoned domain names - Gabor Szathmari - Medium.md
---

## Summary
[[GaborSzathmari]] and [[JeremiahCruz]] report that re-registering expired domains of former Australian law firms let their research team restore catch-all email, receive sensitive correspondence, verify domain ownership with breach-notification services, and initiate password recovery for social, file-sharing, court, practice-management, payment, advertising, and cloud accounts. The source makes [[AbandonedDomainTakeover]] a business-lifecycle and authentication problem: a dissolved or renamed organization can remain reachable through old addresses long after its active staff, brand, and controls have moved elsewhere.

## Key Claims
- Public `.au` drop lists and keyword searches made former legal-practice domains discoverable; after registration, the new owner could set MX records and receive mail for arbitrary addresses through a catch-all service.
- During a three-month, six-domain research exercise, the authors report receiving about 25,000 messages, including financial notices, legal documents, court material, client inquiries, invoices, personal data, and privileged or confidential correspondence.
- Control of the old domain also satisfied email-based ownership and recovery checks, exposing historical addresses and breached passwords and enabling attempted resets for LinkedIn, Facebook, Twitter, Dropbox, court portals, LEAP, law-society, PayPal, Google Ads, Office 365, and G Suite accounts.
- Password reuse could compound the attack because historical breach credentials might still work on a person's current mailbox or other services.
- Multi-factor authentication blocked the researchers' Office 365 recovery attempt, while they report reaching—but deliberately not completing—the final stages of several other takeover flows.
- The primary control is continued custody of retired domains, supported by closing or updating old accounts, removing obsolete email addresses, notifying clients, enabling MFA, using unique passwords, and hardening professional portals' recovery and password-storage practices.

## Key Quotes
> "keep renewing the former firm’s domain name indefinitely" — the report's primary defensive recommendation.

> "we did not log into or take over the user accounts" — the authors' stated boundary after testing recovery flows.

## Connections
- [[GaborSzathmari]] — lead author and cybersecurity researcher reporting the domain re-registration exercise.
- [[JeremiahCruz]] — co-author credited with the research report.
- [[IronBastion]] — cybersecurity company associated with Szathmari in the author biography.
- [[AbandonedDomainTakeover]] — central attack pattern joining domain expiry, email interception, and account recovery.
- [[AuthenticationInfrastructure]] — account recovery and domain-ownership checks relied on continued control of an email namespace.
- [[WeakCredentialExposure]] — reused passwords recovered from earlier breaches could widen access beyond the abandoned domain.
- [[PasswordHashing]] — the report criticizes a practice-management reset email that returned a password in cleartext, though that observation alone does not prove the exact server-side storage mechanism.

## Contradictions
- No direct contradiction was found. The report materially qualifies claims that inbox control is a sufficient authentication boundary: the security of an email address also depends on long-term custody of the domain behind it.
- The exercise used six selected domains and roughly thirty credential subjects, so it demonstrates a feasible failure mode but does not establish prevalence across Australian law firms or other industries.
