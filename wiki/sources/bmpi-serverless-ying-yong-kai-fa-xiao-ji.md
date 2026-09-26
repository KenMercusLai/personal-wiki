---
title: "Serverless应用开发小记"
type: source
tags: [serverless, aws, terraform, docker, cloud-cost]
date: 2020-08-30
source_file: "/mnt/ken_personal_wiki/Articles/bmpi - Serverless应用开发小记.md"
---

## Summary
[[BMPIDev]] documents an AWS application that retrieves ETF price data from Tushare, generates trading signals, stores them in S3, and emails subscribers through SNS. The implementation is a hybrid [[ServerlessComputing]] architecture: a scheduled Dockerized Python core runs on ECS Fargate, a Lambda/API Gateway service manages subscriptions, and a Nuxt/Vue web interface is delivered through S3 and CloudFront, with [[InfrastructureAsCode]] divided between Terraform and Serverless Framework.

## Key Claims
- [[ServerlessComputing]] can combine managed containers, functions, object storage, messaging, scheduling, and CDN delivery rather than requiring every workload to run as a function.
- Long-running scheduled work can fit ECS Fargate better than Lambda, while a small event-driven subscription API fits Lambda and API Gateway.
- [[InfrastructureAsCode]] can be divided by subsystem: Terraform provisions the ECS, IAM, SNS, VPC, and CloudWatch resources, while Serverless Framework provisions Lambda, API Gateway, Route53, CloudFront, certificates, S3, and CloudFormation-backed web infrastructure.
- [[Docker]] image selection affects build reliability: the author chose a Debian Buster-based Python image after Alpine made native TA-Lib compilation slow and error-prone.
- ECS IAM responsibilities should be separated among the application's service role, the task execution role used to pull images, and the events role used by the scheduler to launch tasks.
- A public-subnet Fargate task needs a public IP to reach external APIs when the design intentionally avoids a NAT gateway.
- [[CloudCostOptimization]] depends on workload shape and service composition; the article estimates about $1.02 per month for its assumed traffic, but the quoted prices and comparison are historical and source-specific.

## Key Quotes
> "Fargate 比 Lambda 更适合运行长时间的后台任务。" — the author explains why the scheduled core uses a managed container rather than a function.

> "为服务运行时间付费" — the article summarizes the usage-based billing appeal of serverless systems.

## Connections
- [[BMPIDev]] — author and operator describing the application implementation.
- [[ServerlessComputing]] — architectural model combining Fargate, Lambda, API Gateway, SNS, S3, CloudFront, and scheduled events.
- [[AWS]] — cloud provider supplying the application's compute, messaging, storage, networking, identity, DNS, certificate, and delivery services.
- [[InfrastructureAsCode]] — Terraform and Serverless Framework encode the two infrastructure layers.
- [[Docker]] — packages the Python core and its native TA-Lib dependency for ECS Fargate.
- [[CloudCostOptimization]] — Fargate Spot, public-subnet networking, scale-to-use services, and historical unit prices shape the cost argument.
- [[SecretManagement]] — the article injects the Tushare API token through a manually supplied Terraform variable and container environment variable.

## Contradictions
- The article accepts a plain environment-variable path for a low-sensitivity API token because KMS and Secrets Manager add cost and complexity. This conflicts with [[SecretManagement]] guidance that treats environment variables as a common leakage surface; the source does keep the token out of the repository, but it does not establish rotation, audit, or managed-secret controls.
- The monthly cost comparison is an illustrative calculation based on the article's own traffic and historical prices, not a current AWS quote or a complete total-cost-of-ownership analysis.
