---
title: "Buzzfeed"
type: entity
tags: [company, media, viral-content]
sources:
  - 51-examples-of-growth-hacking-strategies-techniques-from-the-worlds-most-innovative-businesses
  - 9-boxes
  - buzzfeeds-jonah-peretti-news-publishers-only-have-themselves-to-blame-for-losing-out-to-google-and-facebook-the-drum
  - deploy-with-haste-the-story-of-rig-buzzfeed-tech
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[Buzzfeed]] is a digital media company represented in the wiki as a viral-format growth case, a distributed news-and-entertainment publisher, a business diversifying revenue under platform pressure, and an engineering organization that built an internal delivery platform while moving toward service-oriented systems.

## Current Profile
The growth-hacking source presents BuzzFeed's early strength as mastering shareable formats such as quizzes, where participation creates social distribution. The 2017 interview shows the broader media operating system behind that tactic: a global news-and-entertainment organization distributing across more than 30 social platforms, adapting video length to reach or watch-time goals, using behavioral data in branded-content development, and treating digitally native audiences as an aging cohort rather than a youth niche. The later "9 Boxes" memo adds a more adversarial platform-economic stance and a formal portfolio of brands, revenue lines, and operating cells.

The Rig retrospective adds the engineering operating system behind expanding products and teams. BuzzFeed moved from large monolith releases and manual infrastructure coordination toward [[Rig]], a standard service contract and self-service platform spanning local development, CI, AWS deployment, and observability. The company reports 227 production services and roughly 150 deployments per day by February 2017, while acknowledging that Terraform and GPG secret workflows remained difficult.

## Key Characteristics
- Digital media company known for shareable entertainment and news.
- Adapts quizzes, live coverage, short video, long video, and branded content to distinct distribution and engagement goals.
- Operates news and entertainment as complementary divisions across a global bureau and platform network.
- Uses prior audience behavior to inform editorial formats and commercial creative.
- Treats [[Facebook]] and [[Google]] as both essential partners and sources of bargaining pressure.
- Pursues diversified revenue through a portfolio including BuzzFeed, BuzzFeed News, and lifestyle brands such as [[Tasty]].
- Uses shared engineering conventions and platform tooling to decentralize service delivery and production ownership.

## Evidence
- Quiz loop: [[51-examples-of-growth-hacking-strategies-techniques-from-the-worlds-most-innovative-businesses]] describes questionnaire formats whose results users share on Facebook.
- Viral mastery: [[51-examples-of-growth-hacking-strategies-techniques-from-the-worlds-most-innovative-businesses]] frames Buzzfeed's growth as understanding content and distribution in the digital age.
- Distributed operation: [[buzzfeeds-jonah-peretti-news-publishers-only-have-themselves-to-blame-for-losing-out-to-google-and-facebook-the-drum]] reports distribution across more than 30 social platforms, 19 content bureaux, and 11 international editions.
- Format design: [[buzzfeeds-jonah-peretti-news-publishers-only-have-themselves-to-blame-for-losing-out-to-google-and-facebook-the-drum]] describes roughly 40-second video for reach and 12-minute video for watch time, plus Facebook Live election partnerships.
- News-and-entertainment complementarity: [[buzzfeeds-jonah-peretti-news-publishers-only-have-themselves-to-blame-for-losing-out-to-google-and-facebook-the-drum]] says news drives repeat visits and staff pride while entertainment extends reach and format breadth.
- Platform pressure: [[9-boxes]] says Google and Facebook capture much of digital ad revenue and underpay professional content creators.
- Revenue diversification: [[9-boxes]] says BuzzFeed expected revenue outside direct-sold advertising to rise from about a quarter in 2017 to about half in 2019.
- Operating model: [[9-boxes]] shows a nine-box matrix crossing BuzzFeed, BuzzFeed Media Brands, and BuzzFeed News with advertising, commerce, and studio opportunities.
- Engineering platform: [[deploy-with-haste-the-story-of-rig-buzzfeed-tech]] describes Rig's service conventions, CLI, CI, ECS delivery, Terraform infrastructure, and observability defaults.
- Engineering scale: [[deploy-with-haste-the-story-of-rig-buzzfeed-tech]] reports 227 production services and 18,228 tracked deployments, averaging about 150 per day.

## Qualifications
The growth source is a retrospective tactic catalog, the interview relies heavily on company-reported 2017 audience, revenue, engagement, and completion figures, the memo is an internal strategic statement, and the Rig article is a first-party engineering retrospective. Together they show BuzzFeed's intended strategy and self-understanding, but they do not verify profitability, causal effects, later revenue outcomes, deployment quality, developer satisfaction, layoffs, public-market performance, or subsequent platform and infrastructure changes.

## What Changed
- Expanded Buzzfeed from a viral-format case into a publisher-platform and revenue-diversification case.
- Added Tasty and the nine-box matrix as the source's operating-model evidence.
- Added BuzzFeed's distributed newsroom, goal-specific video formats, news-and-entertainment complementarity, and data-informed branded-content practice.
- Added BuzzFeed's engineering-platform transition, service and deployment activity, and remaining infrastructure workflow friction.

## Relationships
- [[ContentLedAcquisition]] - Buzzfeed turns content formats into traffic.
- [[ViralLoops]] - quiz sharing creates user-to-user propagation.
- [[CreatorPlatformMetrics]] - social-platform distribution shapes traffic outcomes.
- [[DigitalMediaMonetization]] - BuzzFeed's strategy centers on diversifying beyond direct-sold ads.
- [[PlatformPublisherRevenue]] - BuzzFeed argues platforms should reward valuable publisher content.
- [[DistributedPublishingStrategy]] - BuzzFeed adapts content and measurement across owned and platform-hosted surfaces.
- [[MediaBrandPortfolio]] - BuzzFeed organizes around multiple audience-facing brands.
- [[Rig]] - BuzzFeed's internal platform for standardized development, deployment, and operation.
- [[InternalDeveloperPlatform]] - BuzzFeed productized shared engineering and reliability conventions as a self-service platform.
