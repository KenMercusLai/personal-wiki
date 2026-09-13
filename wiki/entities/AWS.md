---
title: "AWS"
type: entity
tags: [cloud, ec2, infrastructure, hosting, cost]
sources:
  - wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai
  - a-look-at-auth0-cloud-architecture-5-years-in
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
  - aws-costs-every-programmer-should-know
  - bezos-unbound-exclusive-interview-with-the-amazon-founder-on-what-he-plans-to-conquer-next
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[AWS]] is a cloud infrastructure provider used in the wiki as a self-managed EC2 hosting option, a standardized public-cloud substrate for large-scale SaaS, a managed AI/database stack, a source of unit-cost constraints for infrastructure design, and an Amazon-originated business created by turning internal computing capabilities into an external cloud market.

## Current Profile
One source positions AWS less as a managed developer platform and more as raw infrastructure that can reduce cost when the developer accepts more operations work. The author buys a 4-core, 8GB EC2 Ubuntu server and deploys Next.js with PM2 or Docker behind Nginx, DNS, and Certbot-managed HTTPS.

At SaaS scale, AWS can become a standardized cloud platform when multi-cloud feature parity is too expensive to maintain. In that profile, AWS supplies regions, availability zones, Route53 failover, auto-scaling groups, load balancers, RDS replication, CloudFront, Kinesis, SNS, SQS, CloudWatch metrics, and ECS/EKS-adjacent platform options.

For AI/database workloads, AWS is represented as a managed stack: Amazon Bedrock supplies Titan embeddings, while Amazon RDS for PostgreSQL and Amazon Aurora PostgreSQL provide managed database targets for storing and indexing vectors with pgvector.

AWS also appears as an economic model made of priced units such as compute, memory, storage, requests, and bandwidth. This profile makes reservations, spot pricing, data locality, access patterns, and request volume part of architecture judgment before a system reaches millions of users.

The Forbes profile adds AWS's strategic origin and corporate role inside [[Amazon]]. Bezos saw that Amazon's internal cloud data-storage and computing capabilities could be sold to other businesses; by 2017 AWS had $17.5 billion in revenue. Forbes frames AWS as both one of Amazon's very large markets and the profit engine that let Amazon reinvest in retail, healthcare, advertising, entertainment, hardware, and physical stores.

## Key Characteristics
- Provides EC2 virtual server infrastructure with lower-level deployment control than Vercel's integrated platform workflow.
- Supports large-scale SaaS high availability through regions, availability zones, managed queues, load balancers, Route53, RDS, CloudFront, CloudWatch, and auto-scaling.
- Can create provider-specific leverage after a team stops maintaining equivalent automation and feature sets across multiple clouds.
- Supports RAG-style AI/database workloads through Amazon Bedrock, RDS, Aurora PostgreSQL, and pgvector.
- Prices infrastructure through separable units such as vCPU, RAM, durable storage, requests, and data transfer.
- Originated in Amazon's internal data-storage and computing needs before becoming an external cloud business.
- Serves as one of Amazon's largest growth markets and a profit source that funds other strategic bets.

## Evidence
- EC2 deployment: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] describes buying an Ubuntu EC2 server with 4 cores and 8GB RAM.
- PM2 path: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] gives commands for `pnpm build`, `pm2 start`, Nginx proxying, DNS A records, and Certbot certificates.
- Docker path: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] gives a Dockerfile and local port mapping before reusing the same Nginx, DNS, and HTTPS steps.
- Abstraction comparison: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] claims Vercel effectively wraps AWS infrastructure while charging a premium for convenience.
- SaaS standardization: [[a-look-at-auth0-cloud-architecture-5-years-in]] says Auth0 moved public cloud infrastructure to AWS after AWS-specific features made multi-cloud parity harder.
- Availability substrate: [[a-look-at-auth0-cloud-architecture-5-years-in]] describes AWS regions, at least three availability zones per region, Route53 failover, load balancers, auto-scaling groups, and RDS replication as part of Auth0's HA design.
- Managed-service pull: [[a-look-at-auth0-cloud-architecture-5-years-in]] says increased use of Kinesis, SQS, ALBs, and other AWS resources helped drive the AWS convergence.
- Platform direction: [[a-look-at-auth0-cloud-architecture-5-years-in]] describes an internal platform proof of concept currently running on ECS and possibly moving toward EKS.
- AI database stack: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] combines Amazon Bedrock embeddings, LangChain splitting, and PostgreSQL with pgvector on AWS managed database services.
- RDS benchmark: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] tests pgvector indexing on Amazon RDS for PostgreSQL.
- Aurora option: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] names Amazon Aurora PostgreSQL as a target for storing generated embeddings.
- Compute reference: [[aws-costs-every-programmer-should-know]] lists eu-west-1 median monthly cost for one modern vCPU at about $58 on demand, with lower reservation or spot estimates.
- Memory and storage contrast: [[aws-costs-every-programmer-should-know]] compares roughly $10 per GB-month of RAM with much lower SSD, hard disk, S3, and S3 Glacier storage prices.
- Access-pattern warning: [[aws-costs-every-programmer-should-know]] says S3 stored bytes can be cheap while heavy object writes or reads dominate cost.
- Bandwidth economics: [[aws-costs-every-programmer-should-know]] distinguishes free same-AZ transfer from cross-AZ, cross-region, and internet transfer costs.
- Origin story: [[bezos-unbound-exclusive-interview-with-the-amazon-founder-on-what-he-plans-to-conquer-next]] says Amazon built cloud data-storage capabilities for itself and Bezos realized other businesses might want the same capability.
- Revenue and reinvestment role: [[bezos-unbound-exclusive-interview-with-the-amazon-founder-on-what-he-plans-to-conquer-next]] reports AWS had $17.5 billion in 2017 revenue and frames AWS profits as funding Amazon's wider expansion.

## Qualifications
The AWS profile remains source-scoped. Earlier sources emphasize self-managed EC2 cost tradeoffs, standardized AWS leverage at SaaS scale, AWS's AI/database stack, and unit-cost intuition; the Forbes source emphasizes AWS's Amazon-internal origin and 2017 strategic role. None of these is a full current comparison of AWS pricing, managed-service reliability, security posture, cloud competition, margins, or later AWS growth.

## What Changed
- Added the AWS unit-cost reference source covering vCPU, RAM, storage, request-pattern, and bandwidth economics.
- Added Auth0's AWS-standardized SaaS architecture as a second profile beside the existing EC2 self-hosting case.
- Added Amazon Bedrock plus managed PostgreSQL vector search as an AI application infrastructure case.
- Added Forbes's account of AWS as an internal Amazon capability converted into an external cloud business.
- Added AWS's role as Amazon's 2017 profit engine and one of Bezos's large markets.

## Relationships
- [[NextJSDeployment]] - AWS EC2 hosts the PM2 and Docker deployment examples.
- [[Amazon]] - parent company that created AWS from internal data-storage and computing capabilities.
- [[JeffBezos]] - describes cloud as one of Amazon's enormous market opportunities.
- [[AmazonCapabilityLedExpansion]] - AWS is the article's most important example of internal capability becoming an external business.
- [[Vercel]] - Vercel is compared to AWS as a convenience layer over underlying cloud infrastructure.
- [[CloudCostOptimization]] - AWS self-hosting is one cost-reduction route in the source.
- [[Cloudflare]] - Cloudflare is the lower-operations managed alternative discussed beside AWS.
- [[Auth0]] - Auth0 standardized public SaaS environments on AWS.
- [[CloudHighAvailability]] - AWS regions, availability zones, Route53, RDS, and load balancers support Auth0's HA design.
- [[InfrastructureAsCode]] - Auth0 uses Terraform and SaltStack to provision AWS environments.
- [[AmazonBedrock]] - Bedrock supplies Titan embeddings in the pgvector source.
- [[AmazonRDS]] - RDS for PostgreSQL hosts the pgvector benchmark.
- [[AmazonAurora]] - Aurora PostgreSQL is named as another pgvector deployment target.
- [[Pgvector]] - pgvector is used in AWS managed PostgreSQL environments for vector search.
- [[TechnologyStackComplexity]] - AWS unit costs make memory-heavy, storage-heavy, request-heavy, and transfer-heavy architecture choices economically different.
