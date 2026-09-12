---
title: "AWS"
type: entity
tags: [cloud, ec2, infrastructure, hosting]
sources:
  - wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai
  - a-look-at-auth0-cloud-architecture-5-years-in
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[AWS]] is a cloud infrastructure provider used in the wiki both as a self-managed EC2 hosting option for Next.js and as the standardized public-cloud substrate for Auth0's large-scale authentication SaaS.

## Current Profile
One source positions AWS less as a managed developer platform and more as raw infrastructure that can reduce cost when the developer accepts more operations work. The author buys a 4-core, 8GB EC2 Ubuntu server and deploys Next.js with PM2 or Docker behind Nginx, DNS, and Certbot-managed HTTPS.

Auth0's architecture source adds the opposite scale case: AWS becomes the standardized cloud platform for a multi-environment SaaS that had outgrown multi-cloud feature parity. In that profile, AWS supplies regions, availability zones, Route53 failover, auto-scaling groups, load balancers, RDS replication, CloudFront, Kinesis, SNS, SQS, CloudWatch metrics, and ECS/EKS-adjacent platform options.

## Key Characteristics
- Provides virtual server infrastructure through EC2.
- Supports lower-level deployment control compared with Vercel's integrated platform workflow.
- Requires the developer to handle process management, reverse proxying, DNS, and TLS configuration.
- Serves as the infrastructure layer that Vercel is described as abstracting over.
- Supports large-scale SaaS high availability through regions, availability zones, managed queues, load balancers, Route53, RDS, CloudFront, CloudWatch, and auto-scaling.
- Can create provider-specific leverage after a team chooses to stop maintaining equivalent automation and feature sets across multiple clouds.

## Evidence
- EC2 deployment: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] describes buying an Ubuntu EC2 server with 4 cores and 8GB RAM.
- PM2 path: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] gives commands for `pnpm build`, `pm2 start`, Nginx proxying, DNS A records, and Certbot certificates.
- Docker path: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] gives a Dockerfile and local port mapping before reusing the same Nginx, DNS, and HTTPS steps.
- Abstraction comparison: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] claims Vercel effectively wraps AWS infrastructure while charging a premium for convenience.
- SaaS standardization: [[a-look-at-auth0-cloud-architecture-5-years-in]] says Auth0 moved public cloud infrastructure to AWS after AWS-specific features made multi-cloud parity harder.
- Availability substrate: [[a-look-at-auth0-cloud-architecture-5-years-in]] describes AWS regions, at least three availability zones per region, Route53 failover, load balancers, auto-scaling groups, and RDS replication as part of Auth0's HA design.
- Managed-service pull: [[a-look-at-auth0-cloud-architecture-5-years-in]] says increased use of Kinesis, SQS, ALBs, and other AWS resources helped drive the AWS convergence.
- Platform direction: [[a-look-at-auth0-cloud-architecture-5-years-in]] describes an internal platform proof of concept currently running on ECS and possibly moving toward EKS.

## Qualifications
The AWS profile remains source-scoped. One source emphasizes self-managed EC2 cost tradeoffs, while the Auth0 source emphasizes standardized AWS leverage at SaaS scale. Neither source is a full current comparison of AWS pricing, managed-service reliability, security posture, or alternatives.

## What Changed
- Added Auth0's AWS-standardized SaaS architecture as a second profile beside the existing EC2 self-hosting case.

## Relationships
- [[NextJSDeployment]] - AWS EC2 hosts the PM2 and Docker deployment examples.
- [[Vercel]] - Vercel is compared to AWS as a convenience layer over underlying cloud infrastructure.
- [[CloudCostOptimization]] - AWS self-hosting is one cost-reduction route in the source.
- [[Cloudflare]] - Cloudflare is the lower-operations managed alternative discussed beside AWS.
- [[Auth0]] - Auth0 standardized public SaaS environments on AWS.
- [[CloudHighAvailability]] - AWS regions, availability zones, Route53, RDS, and load balancers support Auth0's HA design.
- [[InfrastructureAsCode]] - Auth0 uses Terraform and SaltStack to provision AWS environments.
