---
title: "New form of Google banking scam"
type: source
tags: [scam, google, banking, security, social-engineering]
date: 2018-10-19
source_file: "/mnt/ken_personal_wiki/Articles/New form of Google banking scam.md"
---

## Summary
[[AbhijitTomar]] describes a cousin losing INR 9,000 after calling a phone number shown for a local bank branch in a Google business card, then giving the supposed employee his card number and CVV. Tomar reports that the same scammer's number appeared on several nearby bank listings and argues that the attack converted users' trust in [[Google]] into trust in an impersonator. The case supports [[SearchListingImpersonation]] as a platform-integrity failure, but it is one first-person account and its two evidentiary screenshots are missing from the source vault.

## Key Claims
- A failed online transaction led the victim to search Google for his local bank branch, call the displayed number, and treat the respondent as a bank employee.
- The impostor asked for the victim's card number and CVV; after the victim disclosed them, INR 9,000, approximately $125 in the article, was removed from the account.
- Tomar reports that the same scammer-controlled number had been registered for several bank branches in the same region, making the attack a repeated listing-manipulation pattern rather than a single misdial.
- The attack depended on transferred trust: the victim trusted the caller partly because Google presented the number inside an authoritative-looking business-information card.
- Tomar attributes the exposure to easy business claiming, limited verification, owner-transfer friction, and the absence at that time of an obvious fraud-reporting route for users who did not own the business.
- Reviews on a second local-bank listing reportedly warned that its displayed number was fake, yet the number remained visible, suggesting that user warnings and listing correction were not tightly coupled.
- The practical defense is to verify high-consequence contact details through an institution-controlled channel and never disclose card credentials or a CVV to an inbound or newly discovered caller.

## Key Quotes
> "there is a subtext of trust that underlies every interaction we make via any app or website" - on the platform trust the scam exploited.

> "A lot of information you see on Google is user contributed and often not vetted by any human." - on the article's warning against treating a listing as institution-verified.

## Connections
- [[AbhijitTomar]] - author and investigator reporting his cousin's loss and the repeated scammer-controlled number.
- [[Google]] - search and business-listing surface whose presentation transferred credibility to the fraudulent contact detail.
- [[SearchListingImpersonation]] - attack pattern in which manipulated listing data routes a user to an impersonator.
- [[PlatformAbuseResponse]] - verification, reporting, correction, and review-to-enforcement latency determine how long the deceptive listing remains useful.
- [[SocialProof]] - warning reviews provided contrary evidence, but only if users noticed and trusted them over the primary phone field.

## Contradictions
- No direct contradiction with existing wiki claims was found. The case extends earlier Google governance evidence from deceptive content and fraudulent removal requests to user-contributed local-business identity data.
- The article is a single 2018 first-person account. It supplies no bank statement, call record, listing-change history, verification transcript, platform response, prevalence estimate, or evidence about later Google controls.
- The lead photograph was opened and omitted as decorative. The two business-card screenshots referenced by the Markdown are absent from the source vault, so their phone fields, review text, timestamps, and listing states could not be independently inspected or retained; no claim treats the captions as verified visual evidence.
