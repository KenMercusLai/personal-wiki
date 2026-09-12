---
title: "SonarQube"
type: entity
tags: [developer-tools, code-quality]
sources:
  - a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[SonarQube]] is a code-quality tool cited in the Bourgau source as a default analyzer that can list TODO comments and assign them remediation cost.

## Current Profile
The source presents SonarQube as both support and caution for TODO-based [[TechnicalDebtTracking]]. It can surface TODO comments automatically, but its default fixed remediation cost may misrepresent debt because not every TODO has the same effort, urgency, or risk.

## Key Characteristics
- Code-quality analyzer that reports TODO comments.
- Applies remediation-cost assumptions to TODOs in the source's account.
- Illustrates the need to adapt tool defaults to team context.

## Evidence
- TODO reporting: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] says CodeClimate and SonarQube list TODOs as issues in their default configuration.
- Remediation caveat: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] warns that SonarQube assigns a fixed remediation cost to TODO comments even though real cost varies.
- Configuration implication: [[a-seamless-way-to-keep-track-of-technical-debt-in-your-source-code-philippe-bourgaus-blog]] says teams may need to adapt the remediation cost to their context.

## Qualifications
The source reflects the author's experience and tool behavior around the 2017 article date. It does not establish current SonarQube defaults or broader code-quality capability.

## What Changed
- Created the entity for SonarQube as a code-quality tool with useful but potentially misleading TODO defaults.

## Relationships
- [[TodoComments]] - comments SonarQube can report.
- [[TechnicalDebtTracking]] - workflow SonarQube may support or distort through default costs.
- [[PhilippeBourgau]] - author who cites SonarQube as both tool support and caveat.
