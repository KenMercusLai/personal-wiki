---
title: "Parallax Agency"
type: entity
tags: [digital-agency, software-development, design, security]
sources:
  - interview-building-the-latest-campaign-for-david-guetta-serverless-code
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[ParallaxAgency]] is the Leeds digital agency, styled `parall.ax` in the source, that built the web application for [[ThisOnesForYouCampaign]].

## Current Profile
In the 2016 interview, Parallax describes itself as a 25-person agency, supplemented by external contractors, providing application development, security, and design services. It emphasizes highly scalable work in sports, advertising, and fast-moving consumer goods. A five-person team delivered the David Guetta campaign application in roughly six or seven weeks after prior research and prototyping.

## Key Characteristics
- Combines application development, security, and design services in one digital agency.
- Presents scalable sports, advertising, and consumer-goods systems as a specialty.
- Used a small cross-functional team spanning account management, backend and cloud architecture, frontend integration, QA and systems, and compatibility engineering.
- Adopted an early Lambda and Serverless Framework architecture for bursty public campaign traffic.

## Evidence
- Agency profile: [[interview-building-the-latest-campaign-for-david-guetta-serverless-code]] reports 25 full-time employees, external contractors, and the agency's stated service and market focus.
- Delivery team: [[interview-building-the-latest-campaign-for-david-guetta-serverless-code]] names five campaign roles and says the application took about six or seven weeks after research and prototyping.
- Technical approach: [[interview-building-the-latest-campaign-for-david-guetta-serverless-code]] describes the agency's Lambda, API Gateway, CloudFront, S3, DynamoDB, SES, CloudFormation, and Serverless Framework composition.

## Qualifications
The profile rests on one 2016 interview and reflects the agency's own description. It does not establish the company's current size, services, clients, organization, or independently measured delivery and reliability outcomes.

## What Changed
- Created a source-scoped profile of the agency and its five-person campaign team.

## Relationships
- [[JamesHall]] - backend developer and cloud architect interviewed about the agency's work.
- [[ThisOnesForYouCampaign]] - campaign application delivered by a five-person Parallax team.
- [[DavidGuetta]] - artist whose fan-participation campaign the agency supported.
- [[ServerlessComputing]] - architecture model Parallax selected for burst elasticity.
- [[InfrastructureAsCode]] - Serverless Framework and CloudFormation encoded the campaign platform.
