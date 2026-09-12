---
title: "A first peek behind the scenes of Hillary Clinton's technology operation"
type: source
tags: [campaign-tech, product, fundraising, politics]
date: 2016-04-21
source_file: "/mnt/ken_personal_wiki/Articles/A first peek behind the scenes of Hillary Clinton’s technology operation.md"
---

## Summary
This first-person campaign technology article describes [[HillaryClinton]]'s official engineering operation as a product organization serving Digital, Analytics, Finance, and Organizing. It gives concrete examples of [[OfficialCampaignTechnology]] through donation optimization, the [[CommitToVote]] voter information app, and the emergency [[BalloonEmail]] mass-mailing system, showing campaign software as a mix of fundraising infrastructure, field support, voter education, analytics, and rapid incident response.

## Key Claims
- [[HillaryClinton]]'s campaign technology team had roughly 50 backend services, 20 frontend applications, 237 Git repositories, and a 15 TB query-intensive data warehouse serving analysts and data scientists.
- The team worked across Digital, Analytics, Finance, and Organizing rather than treating software as a detached technical silo.
- The web donation platform processed more than 1 million donations, supported ACH to reduce card fees, and used A/B tests that produced conversion-rate improvements above 200%, 105%, and 80%.
- A redesigned saved-card flow used the donor's already-entered email, detected account state, removed a click, and reportedly increased saved-card opt-in by 238.8% at 99% confidence.
- [[CommitToVote]] helped more than 574,000 voters find polling or caucus locations and used CDN Geo IP data to infer state.
- [[BalloonEmail]] was built in Python and AWS in about four hours after a vendor outage, sent more than 14 million emails, and reportedly saved over $700,000 in donations.
- The stack mixed Python/Django, Node.js, some Ruby/Rails and PHP, React, NuclearJS, and Sass.

## Key Quotes
> "We don't operate at Google scale, but we scale people and products rapidly." - opening framing

## Connections
- [[HillaryClinton]] - candidate whose official campaign technology operation is described from inside the team.
- [[OfficialCampaignTechnology]] - central model of staffed campaign software for fundraising, analytics, organizing, and voter education.
- [[CommitToVote]] - voter commitment and polling/caucus lookup product.
- [[BalloonEmail]] - emergency fundraising email application built after a vendor outage.
- [[ConversionRateOptimization]] - saved-card redesign and A/B testing are the source's strongest product optimization example.
- [[ProductMetricLadder]] - donation and saved-card metrics connect short-cycle experiments to fundraising outcomes.
- [[CampaignTechnologyAccountability]] - centralized campaign technology clarifies ownership but still carries high-consequence voter and fundraising responsibilities.
- [[VolunteerCampaignTechnology]] - contrast case for the Sanders volunteer software ecosystem.

## Contradictions
- Qualifies [[2016-bernies-army-of-coders-politico-magazine]] by showing that Clinton's more centralized campaign technology operation was not merely slow hierarchy; it had substantial internal engineering scale, production systems, and rapid-response capacity.
