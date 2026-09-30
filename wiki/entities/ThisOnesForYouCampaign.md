---
title: "This One's for You Campaign"
type: entity
tags: [digital-campaign, music, serverless, web-audio]
sources:
  - interview-building-the-latest-campaign-for-david-guetta-serverless-code
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[ThisOnesForYouCampaign]] was a twelve-language web campaign that invited fans to record themselves singing with [[DavidGuetta]] and generate personalized, team-themed artwork around the UEFA EURO 2016 anthem "This One's for You."

## Current Profile
The product joined a static CloudFront/S3 site to Lambda-backed language detection, subscription, upload-token, and image-generation endpoints. Browser-generated UUIDs associated user actions without server-issued cookies, recordings went directly to S3, and generated artwork was published in platform-sized variants through unique Open Graph pages. WebRTC, Flash, and mobile file-input paths broadened recording compatibility, while per-branch deployments and physical-device testing supported the short delivery schedule.

## Key Characteristics
- Designed for bursty publicity-driven demand without long-lived application servers.
- Combined participatory audio recording with personalized and shareable visual output.
- Served twelve languages and handled non-Latin names through a separate Unicode-font image endpoint.
- Used WebRTC, Flash, and mobile file input as graded compatibility paths.
- Created a test environment and URL for every branch or commit.

## Evidence
- Product goal: [[interview-building-the-latest-campaign-for-david-guetta-serverless-code]] describes the virtual studio, personalized team artwork, sharing, embedded video, and competition.
- Service flow: [[interview-building-the-latest-campaign-for-david-guetta-serverless-code]] traces static delivery, client UUIDs, Lambda APIs, DynamoDB and SES subscription work, direct S3 uploads, and image generation.
- Compatibility and delivery: [[interview-building-the-latest-campaign-for-david-guetta-serverless-code]] records three capture implementations, physical-device testing, branch deployments, and the Unicode-font workaround.

## Qualifications
The project profile comes from a team interview published during the campaign. The stated million-fan goal, unlimited-demand framing, scalability advantage, and development-speed advantage are not accompanied by measured results. Six referenced local images are missing, so their architecture and UI evidence could not be inspected.

## What Changed
- Created a consolidated product profile covering purpose, architecture, compatibility, and delivery constraints.

## Relationships
- [[DavidGuetta]] - artist and campaign subject whose image, song, and video anchored the experience.
- [[ParallaxAgency]] - digital agency that built the application.
- [[JamesHall]] - backend developer and cloud architect who described the implementation.
- [[ServerlessComputing]] - managed execution model used for APIs and personalized image generation.
- [[AWS]] - provider of the campaign's compute, API, storage, email, database, CDN, and monitoring services.
- [[DeploymentAutomation]] - per-branch build and testing environments supported review before merge.
