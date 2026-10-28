---
title: "CloudKit Service"
type: entity
tags: [cloud, cmdb, plugins, infrastructure]
sources:
  - ai-harness-engineering
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Overview
[[CloudKitService|CloudKit]] is [[Zhu327]]'s plugin-based microservice for normalizing provider-specific Day 2 cloud operations; the disambiguated page key distinguishes it from Apple's CloudKit platform.

## Current Profile
The service exposes standardized REST/JSON operations through an API gateway with authentication, authorization, rate limiting, and audit logging. A plugin manager handles registration, discovery, versioning, routing, and capability coordination, while individual AWS, Alibaba Cloud, Huawei Cloud, and Kingsoft Cloud plugins wrap their respective SDKs.

The source places CloudKit beside rather than beneath [[TFEngine]]. The CMDB sends imperative query, start, stop, restart, resize, snapshot, backup, tagging, monitoring, and alerting work to CloudKit, while Terraform-backed create, update, and delete work goes to TFEngine. A shared identity layer supplies cloud accounts, credentials, roles, and secure secret storage to both paths.

## Key Characteristics
- Presents a common REST/JSON boundary for provider-specific cloud operations.
- Uses one plugin per capability to encapsulate the corresponding workflows across four public clouds.
- Separates plugin registration, discovery, versioning, routing, and capability coordination from provider SDK wrappers.
- Covers imperative Day 2 operations that the reported system does not assign to Terraform.
- Shares identity, credentials, authorization, and audit controls with the CMDB and TFEngine path.

## Evidence
- Plugin architecture: [[ai-harness-engineering]] says each added capability is a plugin encapsulating the corresponding APIs across AWS, Alibaba Cloud, Huawei Cloud, and Kingsoft Cloud.
- Gateway and management layers: [[ai-harness-engineering]] and its retained architecture show authentication, authorization, rate limiting, audit, routing, versioning, and provider SDK wrappers.
- Lifecycle boundary: [[ai-harness-engineering]] routes Day 2 operations through CloudKit while declarative create, update, and delete operations use TFEngine.

## Qualifications
The source is a builder's account and architecture diagram, not a compatibility or reliability evaluation. It does not document plugin contracts, partial-failure semantics, capability negotiation, SDK-version drift, authentication implementation, audit guarantees, provider conformance tests, or operational scale.

## What Changed
- Created the initial profile and explicitly disambiguated the service from Apple's CloudKit.

## Relationships
- [[Zhu327]] - reported developer of the service.
- [[TFEngine]] - sibling execution system for Terraform-backed lifecycle work.
- [[MultiCloudLifecycleManagement]] - architectural problem the service addresses through provider plugins.
- [[InfrastructureAsCode]] - complementary declarative path used for resource lifecycle changes.
- [[AWS]] - one provider family wrapped by a service plugin.
- [[AlibabaCloud]] - one provider family wrapped by a service plugin.
