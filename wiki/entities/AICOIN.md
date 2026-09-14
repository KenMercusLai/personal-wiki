---
title: "AICOIN"
type: entity
tags: [trading-tool, crypto]
sources:
  - blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[AICOIN]] appears in the wiki as a crypto trading tool used for funding-rate arbitrage order execution.

## Current Profile
The source names AICOIN as a mainstream tool for placing the simultaneous or parameterized orders needed in funding-rate arbitrage, where spread, funding rate, and timing matter. The article emphasizes operational caution: users should test settings with small orders and understand every parameter before scaling.

## Key Characteristics
- Supports order execution for crypto arbitrage workflows in the article's account.
- Matters because spread and timing can turn a positive funding rate into a losing trade.
- Is described as a local tool whose API keys and requests stay on the user's computer.
- Introduces operational risk if the user's network or machine fails mid-trade.

## Evidence
- Execution role: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] says AICOIN is the mainstream tool for the spread/rate/timing problem.
- Small-order testing: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] tells readers to test order parameters in small amounts before committing capital.
- Local security model: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] says API keys and requests are local, which shifts reliability risk to the user's network and computer.

## Qualifications
The wiki has not inspected AICOIN directly. This page records only the role and risks assigned to it by the source.

## What Changed
- Created AICOIN as the execution-tool entity in the funding-arbitrage workflow.

## Relationships
- [[FundingRateArbitrage]] - strategy whose execution AICOIN helps coordinate.
- [[DeltaNeutralStrategy]] - position structure that requires careful simultaneous spot and perpetual execution.
- [[InvestmentRiskDiscipline]] - the article's small-order testing advice is a risk-control practice.
