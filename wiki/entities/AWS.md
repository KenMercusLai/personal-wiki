---
title: "AWS"
type: entity
tags: [cloud, ec2, infrastructure, hosting]
sources:
  - wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[AWS]] is used in the source as the self-managed cloud alternative for hosting a Next.js application on an EC2 server.

## Current Profile
The article positions AWS less as a managed developer platform and more as raw infrastructure that can reduce cost when the developer accepts more operations work. The author buys a 4-core, 8GB EC2 Ubuntu server and deploys Next.js with PM2 or Docker behind Nginx, DNS, and Certbot-managed HTTPS.

## Key Characteristics
- Provides virtual server infrastructure through EC2.
- Supports lower-level deployment control compared with Vercel's integrated platform workflow.
- Requires the developer to handle process management, reverse proxying, DNS, and TLS configuration.
- Serves as the infrastructure layer that Vercel is described as abstracting over.

## Evidence
- EC2 deployment: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] describes buying an Ubuntu EC2 server with 4 cores and 8GB RAM.
- PM2 path: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] gives commands for `pnpm build`, `pm2 start`, Nginx proxying, DNS A records, and Certbot certificates.
- Docker path: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] gives a Dockerfile and local port mapping before reusing the same Nginx, DNS, and HTTPS steps.
- Abstraction comparison: [[wo-ba-wang-zhan-qian-yi-dao-cf-sheng-le-ji-wan-kuai]] claims Vercel effectively wraps AWS infrastructure while charging a premium for convenience.

## Qualifications
The AWS profile is narrow and source-scoped. The article does not compare AWS managed services, reserved pricing, autoscaling, operational risk, or total cost beyond its EC2 deployment example.

## What Changed
- Created the AWS entity profile as a self-managed deployment option in the wiki.

## Relationships
- [[NextJSDeployment]] - AWS EC2 hosts the PM2 and Docker deployment examples.
- [[Vercel]] - Vercel is compared to AWS as a convenience layer over underlying cloud infrastructure.
- [[CloudCostOptimization]] - AWS self-hosting is one cost-reduction route in the source.
- [[Cloudflare]] - Cloudflare is the lower-operations managed alternative discussed beside AWS.
