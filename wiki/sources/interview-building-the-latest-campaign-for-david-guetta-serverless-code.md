---
title: "Interview: Building the Latest Campaign for David Guetta -- Serverless Code"
type: source
tags: [serverless, aws, digital-campaign, web-audio, deployment]
date: 2016-01-13
source_file: "/mnt/ken_personal_wiki/Articles/Interview- Building the Latest Campaign for David Guetta -- Serverless Code.md"
---

## Summary
Ryan S. Brown interviews [[JamesHall]] about the five-person [[ParallaxAgency]] team that built the twelve-language [[ThisOnesForYouCampaign]] in roughly six or seven weeks. The campaign combined a static CloudFront/S3 front end with Lambda, API Gateway, DynamoDB, SES, direct browser-to-S3 uploads, personalized image generation, branch testing environments, and multiple recording fallbacks, making it a concrete early [[ServerlessComputing]] case for bursty public demand.

## Key Claims
- [[ServerlessComputing]] let the team design for press-driven traffic spikes without operating long-lived application servers or pre-provisioning a dedicated image-generation queue and EC2 worker fleet.
- The request path separated static delivery from narrow APIs: CloudFront cached S3 assets, the browser generated a UUID, Lambda endpoints handled locale detection and subscriptions, and temporary tokens let recordings upload directly to UUID-specific S3 paths.
- Lambda image generation combined a team flag, a David Guetta image, and the participant's name, then stored social-size graphics and a static Open Graph page so each result had a shareable URL.
- The recording UI used progressive compatibility layers: WebRTC microphone capture, a Flash desktop fallback, and mobile file input, with real-device testing because camera and microphone behavior was unreliable or absent in emulators.
- [[InfrastructureAsCode]] used the early Serverless Framework and CloudFormation to orchestrate the platform, but separate branches that added endpoints could not share one framework stage cleanly.
- Bamboo and Stash created a URL and testing environment for every branch and commit, while Bugsnag covered browser errors and CloudWatch covered Lambda monitoring.
- Internationalized server-side image generation required shipping a large Unicode font because bare Lambda/ImageMagick execution did not reproduce browser font fallback; the team routed only non-Latin names through that heavier endpoint.

## Key Quotes
> "Writing a simple Lambda function and letting Amazon do all the hard work seemed like the obvious choice." — Hall on choosing Lambda over a conventional LAMP and EC2 worker design.

> "Cameras and microphones behave very differently in emulators" — Hall on why the team tested recording flows on physical devices.

## Connections
- [[JamesHall]] — interviewee who designed the cloud architecture and wrote the Lambda functions.
- [[ParallaxAgency]] — digital agency whose five-person team delivered the campaign application.
- [[DavidGuetta]] — artist whose UEFA EURO 2016 anthem and fan participation campaign anchored the product.
- [[ThisOnesForYouCampaign]] — multilingual recording and personalized-artwork experience described by the interview.
- [[ServerlessComputing]] — Lambda-centered architecture chosen for burst elasticity and reduced server operations.
- [[AWS]] — provider of Lambda, API Gateway, CloudFront, S3, DynamoDB, SES, and CloudWatch.
- [[InfrastructureAsCode]] — Serverless Framework and CloudFormation encoded the service composition.
- [[DeploymentAutomation]] — Bamboo built per-branch environments and posted their URLs into company chat.
- [[ServiceObservability]] — Bugsnag and CloudWatch separated browser-side and function-side error monitoring.
- [[ContinuousDelivery]] — every pushed branch or commit received a test deployment before merge decisions.

## Contradictions
- The interview says the architecture could handle "any level" of demand and was more robust than the team's conventional stack, but reports no load-test results, production traffic, latency, error rate, cost, availability, or campaign outcome. It demonstrates design intent rather than verified infinite scale.
- The team expected a million participants, but the source does not establish whether that target was reached or whether any submitted voices entered the released song.
- Six local image references point to a missing sidecar directory, so the architecture, deployment-bot, Unicode-comparison, and Testdroid images could not be independently inspected; image-derived claims were not added.
