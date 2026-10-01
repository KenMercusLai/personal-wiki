---
title: "Search Listing Impersonation"
type: concept
tags: [fraud, search, social-engineering, platform-governance]
sources:
  - new-form-of-google-banking-scam
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[SearchListingImpersonation]] is a social-engineering attack in which an attacker inserts or controls a contact detail on a search or business-listing surface so that a user seeking a legitimate organization is routed to an impersonator.

## Current Synthesis
The documented case combines listing manipulation with telephone impersonation. A victim searching for a bank branch treated the phone number inside Google's business card as institution-vetted, called it about a failed transaction, and disclosed his card number and CVV to a supposed bank employee. The attacker therefore did not need to initiate contact or counterfeit the whole interface: the platform supplied discovery, presentation, and borrowed credibility.

The defense is layered. Platforms need stronger ownership evidence for high-consequence listings, anomaly detection across repeated contact details, usable third-party fraud reports, visible provenance, and timely correction. Organizations need to monitor prominent listings and publish verifiable contact routes. Users should retrieve sensitive-service contacts through institution-controlled channels and refuse requests for secrets such as a CVV. Reviews can warn users, but warning text is a weak control when the primary call action still routes directly to the attacker.

## Key Claims
- The manipulated contact field is both a routing mechanism and a credibility signal.
- User-initiated contact can still be social engineering when an attacker controls the discovery surface.
- One attacker-controlled number appearing across several organizations is a cross-listing anomaly that platform-level detection can use.
- Verification, reporting, correction, and review-to-enforcement latency jointly determine the attack window.
- High-consequence institutions require stronger contact provenance than ordinary user-contributed directory data.
- User education remains necessary but cannot substitute for platform and institution controls.

## Evidence
- Trust transfer: [[new-form-of-google-banking-scam]] says the victim trusted the respondent because he had obtained the number from Google's business card for a bank branch.
- Financial path: [[new-form-of-google-banking-scam]] reports disclosure of a card number and CVV followed by the loss of INR 9,000.
- Cross-listing reuse: [[new-form-of-google-banking-scam]] says the same scammer's phone number appeared on several bank branches in the region.
- Governance gap: [[new-form-of-google-banking-scam]] describes easy claiming, weak apparent verification, owner-transfer friction, and no obvious non-owner fraud-reporting channel at the time.
- Weak warning layer: [[new-form-of-google-banking-scam]] reports reviews calling another bank listing's number fake while that number remained displayed.

## Counterevidence & Qualifications
The concept currently rests on one October 2018 first-person account rather than platform telemetry, controlled testing, police or bank records, or a representative sample. The source cannot establish how the listings were altered, whether the attacker held formal ownership, how long the numbers remained visible, or what platform controls existed or changed later. Its two evidentiary screenshots are missing, so the listing fields and warning reviews cannot be visually verified from the vault.

## What Changed
- Established the attack model linking directory-data manipulation, platform trust transfer, telephone impersonation, and credential theft.
- Separated user verification duties from platform and institution responsibilities.

## Related Concepts
- [[PlatformAbuseResponse]] - determines how manipulated listings are prevented, reported, corrected, and escalated.
- [[SocialProof]] - reviews may warn against a false primary listing field but compete with the interface's stronger authority signal.
- [[UserTrustCapital]] - reliable prior use can make platform-presented information feel safe by default.
- [[IdentityResolution]] - listing governance must bind a claimed business identity to the legitimate organization and its contact routes.
