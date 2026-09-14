---
title: "Programmatic Advertising"
type: concept
tags: [advertising, adtech, data, auctions]
sources:
  - blog-wulc-ru-he-yong-shu-ju-lai-zhuan-qian
  - blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[ProgrammaticAdvertising]] is automated ad buying in which exchanges and buying platforms use user, context, and advertiser data to decide whether and how much to bid for an impression.

## Current Synthesis
The sources position programmatic advertising as the stage where ad monetization moves beyond platform-owned targeting data. In the inspected process diagram, a user visits a media site, the site sends an ad request to an ADX, the ADX sends user information and bid requests to multiple DSPs, and DSPs decide whether to bid using advertiser-side data such as cookie mappings and audience criteria. The audience-targeting source adds why those criteria matter: labels can describe user, context, ad, and user-advertiser relationships, including advertiser-specific states such as old users, potential users, and lost users. This makes first-party advertiser data useful in real-time buying and creates demand for third-party or media data that can expand targeting beyond a brand's known users.

## Key Claims
- Programmatic advertising exists because advertiser-specific targeting needs exceed the generic targeting a platform can provide by itself.
- ADX and DSP systems mediate an automated request-bid-response loop between media inventory and advertiser demand.
- First-party advertiser data becomes valuable when a DSP can recognize users who visited, churned, or otherwise match advertiser-defined segments.
- Audience labels can include advertiser-specific user states, making user-advertiser relationship data central to programmatic buying.
- Third-party or media data can expand reach through look-alike modeling when advertiser seed audiences are small.
- Programmatic buying increases participation by smaller advertisers because they can decide impression value more directly.

## Evidence
- Need for customization: [[blog-wulc-ru-he-yong-shu-ju-lai-zhuan-qian]] says bidding ads still cannot satisfy all advertiser-specific targeting needs.
- Exchange flow: [[blog-wulc-ru-he-yong-shu-ju-lai-zhuan-qian]] diagrams user-to-media, media-to-ADX, ADX-to-DSP bid requests, and ad response.
- First-party data: [[blog-wulc-ru-he-yong-shu-ju-lai-zhuan-qian]] uses churned users and site visitors as examples that only the advertiser may know.
- Advertiser-specific labels: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] diagrams user-advertiser labels such as advertiser A's old users, advertiser B's potential users, and advertiser C's lost users.
- Retargeting: [[blog-wulc-ru-he-yong-shu-ju-lai-zhuan-qian]] lists site retargeting, search retargeting, and personalized retargeting.
- Look-alike expansion: [[blog-wulc-ru-he-yong-shu-ju-lai-zhuan-qian]] says DSPs use advertiser seed users and media behavior data to find similar potential customers.

## Counterevidence & Qualifications
The sources explain the product and targeting logic but do not evaluate fraud, brand safety, auction transparency, privacy regulation, cookie deprecation, measurement error, or later adtech ecosystem changes. Their account should therefore be treated as a conceptual 2017 snapshot, not a complete current implementation guide.

## What Changed
- Added advertiser-specific audience labels as the targeting substrate that makes first-party data useful in automated buying.

## Related Concepts
- [[DataMonetization]] - programmatic advertising is an operational form of monetizing traffic-attached data.
- [[AudienceTargeting]] - supplies the user, context, ad, and advertiser-relationship labels that guide bids.
- [[BehavioralTargeting]] - produces behavior-derived labels that can feed retargeting and look-alike decisions.
- [[BehavioralData]] - user actions and intent signals drive bidding, retargeting, and look-alike expansion.
- [[WebAdEconomics]] - programmatic ad buying is part of the indirect funding system for free web services.
- [[MarketingAttribution]] - advertisers need attribution to judge whether programmatic spend creates downstream value.
- [[MobileMessagingAdvertising]] - both are digital ad formats, but messaging ads focus on mobile chat surfaces while programmatic advertising focuses on automated buying infrastructure.
