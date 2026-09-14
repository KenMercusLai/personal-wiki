---
title: "怎样用数据洞察你的用户"
type: source
tags: [audience-targeting, user-profiling, behavioral-targeting, advertising]
date: 2017-06-10
source_file: /mnt/ken_personal_wiki/Articles/Blog - wulc - 怎样用数据洞察你的用户.md
---

## Summary
[[Wulc]] summarizes a Zhihu Live on [[AudienceTargeting]] and user profiling, especially how advertising systems turn raw user behavior into demand-relevant labels. The article and inspected diagrams distinguish interpretable user profiles from optimizable targeting labels, compare structured and demand-driven tag systems, and describe [[BehavioralTargeting]] as a pipeline from browsing, search, ad clicks, and conversion signals into weighted tag scores evaluated through Reach/CTR curves.

## Key Claims
- Audience targeting and user profiling both describe users through labels, but targeting emphasizes optimization and advertiser demand while user profiling emphasizes interpretability.
- Targeting labels can describe users, context, user-advertiser relationships, and ads; their uses split between advertiser-facing traffic-sale systems and model features such as CTR prediction.
- Structured taxonomies feel complete but can underperform when they ignore advertiser-specific demand; demand-driven, non-structured tag systems can be more practical.
- Effective tag-system design starts from an industry and its customer decision process, then builds labels around each decision stage rather than around an abstract taxonomy.
- [[BehavioralTargeting]] maps actions such as browsing, sharing, ad display, ad click, search, and conversion into tags using content extraction, manual labels, classification, topic models, and vertical-site categories.
- Behavior signals need weighting and recency handling because different actions express different intent strengths and user interest decays over time.
- Audience-targeting quality can be checked with a Reach/CTR curve: narrower tagged audiences should usually show higher CTR, while a flat or inverted curve suggests the label is not useful.

## Key Quotes
> "不能想当然地描述用户，而是要根据需求方（如广告主）的需求来为用户打上相应标签" - on demand-driven user description.

> "制定标签体系不要刻意追求规整、结构化的标签体系" - on resisting tidy but weak taxonomies.

> "通过 Reach / CTR 曲线评测定向是否有效" - on the source's evaluation criterion.

## Connections
- [[Wulc]] - author and summarizer of the Zhihu Live.
- [[AudienceTargeting]] - central concept: transforming raw behavior into user labels that serve advertiser demand and predictive models.
- [[BehavioralTargeting]] - main method covered in depth, using historical behavior to assign weighted tag scores.
- [[BehavioralData]] - browsing, search, ad-click, conversion, and session logs supply the raw evidence.
- [[DataMonetization]] - targeting labels make traffic more valuable by improving advertiser fit and campaign optimization.
- [[ProgrammaticAdvertising]] - targeting labels and advertiser-specific segments are inputs to automated bidding and look-alike expansion.
- [[ProductUserSegmentation]] - related use of user group distinctions, though this source focuses on ad targeting rather than product design.

## Contradictions
- No direct contradictions found. The source deepens [[blog-wulc-ru-he-yong-shu-ju-lai-zhuan-qian]] by explaining the label-building and evaluation mechanics behind advertising-data monetization, while preserving that earlier source's qualification that some mobile scene-data applications were still immature in 2017.
