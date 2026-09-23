---
title: "bmpi.dev"
type: entity
tags: [author, software-development, cloud]
sources:
  - bmpi-serverless-ying-yong-kai-fa-xiao-ji
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[BMPIDev]] is the author and developer behind the AWS serverless application described in "Serverless应用开发小记."

## Current Profile
The source presents bmpi.dev as a hands-on developer combining Python, Docker, Terraform, Serverless Framework, Vue, and Nuxt across a small event-driven application. The account emphasizes practical workload placement, inexpensive managed services, explicit IAM roles, and simple deployment commands, while accepting tradeoffs such as a public-subnet Fargate task and environment-variable secret injection.

## Key Characteristics
- Builds a scheduled ETF-signal application across managed AWS compute, storage, messaging, and web-delivery services.
- Chooses Fargate for the long-running core task and Lambda for the small subscription API.
- Uses Terraform and Serverless Framework as complementary infrastructure automation tools.
- Prioritizes low direct cloud cost and implementation simplicity for a small application.

## Evidence
- Application design: [[bmpi-serverless-ying-yong-kai-fa-xiao-ji]] describes the core, API, and web modules and their AWS service boundaries.
- Tooling choices: [[bmpi-serverless-ying-yong-kai-fa-xiao-ji]] shows a Dockerized Python core, Terraform-managed infrastructure, and a Serverless Framework-managed API and web layer.
- Operating tradeoffs: [[bmpi-serverless-ying-yong-kai-fa-xiao-ji]] chooses Fargate Spot, a public subnet, and simple environment-variable secret injection to control cost and complexity.

## Qualifications
The wiki has one self-authored implementation note for bmpi.dev. It does not independently verify the application's production scale, reliability, security posture, or realized monthly cost.

## What Changed
- Created the profile from the AWS serverless application development note.

## Relationships
- [[ServerlessComputing]] - bmpi.dev applies a hybrid serverless architecture to scheduled analysis, subscriptions, and web delivery.
- [[AWS]] - supplies the managed services used by the application.
- [[InfrastructureAsCode]] - Terraform and Serverless Framework encode the deployment.
- [[Docker]] - packages the Python core for Fargate.
