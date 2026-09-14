---
title: "Beefy Finance"
type: entity
tags: [crypto, defi, vault]
sources:
  - blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[BeefyFinance]] appears in the wiki as the auto-compounding vault platform used in Taresky's stablecoin-mining walkthrough.

## Current Profile
The source presents Beefy as a "vault" layer that can accept LP tokens from another protocol, stake them, harvest rewards, sell reward tokens, and reinvest into the underlying pool. This can reduce gas and operational friction for small users, but it also adds another smart contract and platform dependency. The article also describes Beefy's Boost feature as an additional promotional staking layer with still more interaction risk.

## Key Characteristics
- Aggregates LP-token staking and reward compounding on behalf of users.
- Makes APY sorting and stable-LP filtering part of the user workflow.
- Issues a vault receipt token representing the deposited LP position.
- Reduces repeated manual harvest and reinvest work, especially where gas costs matter.
- Adds platform and contract risk because the user's position passes through another layer.

## Evidence
- Vault workflow: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] instructs users to find the Belt stable LP vault and deposit BeltVenusBLP.
- Receipt token: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] says the deposited Belt LP disappears from the wallet view and is replaced by mooBeltVenusBLP.
- Auto-compounding: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] explains that the moo token quantity stays the same while its claim on Belt LP grows as rewards compound.
- Gas and friction reduction: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] says pooling harvest, sale, and reinvest actions can save gas relative to each small user doing them alone.
- Added risk layer: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] notes that Boost adds another contract interaction and therefore another layer of risk.

## Qualifications
This page records Beefy only as represented in the ingested explainer. It is not a current yield, audit, solvency, or platform-status assessment.

## What Changed
- Added Beefy Finance as the auto-compounding vault layer in the stablecoin-mining source.

## Relationships
- [[StablecoinYieldFarming]] - Beefy is the source's vault example for compounding stablecoin LP rewards.
- [[BeltFinance]] - source workflow deposits Belt LP tokens into Beefy.
- [[DeFiRiskStack]] - Beefy adds vault and extra-contract risk to the strategy.
- [[LiquidityProvision]] - Beefy compounds returns from an existing liquidity position.
