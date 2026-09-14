---
title: "Impermanent Loss"
type: concept
tags: [crypto, defi, markets]
sources:
  - blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ImpermanentLoss]] is the opportunity-cost tradeoff a liquidity provider faces when an AMM pool rebalances away from the assets they would have held outside the pool.

## Current Synthesis
The Taresky stablecoin-mining source argues that impermanent loss is misleadingly named because the core issue is not a strange malfunction but the economics of automated rebalancing. In an XYK pool, the provider is effectively running an infinite grid strategy: buying more of the falling asset and selling more of the rising asset. That can earn fees during choppy, sideways trading, but when one asset trends strongly, the provider can end up worse than a simple holder.

## Key Claims
- Impermanent loss is best understood as relative underperformance versus holding, not necessarily as an absolute loss.
- AMM liquidity provision behaves like continuous rebalancing or grid trading.
- Volatility can increase fee revenue, but trend direction determines whether the rebalancing tradeoff is costly.
- Stablecoin pairs reduce the problem because the pooled assets are intended to stay near the same price.
- The term can confuse beginners by hiding the market-making assumption behind a technical-sounding label.

## Evidence
- Opportunity-cost framing: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] says the strategy earns fees but should be expected to underperform holding when the market does not stay range-bound.
- Grid analogy: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] explains XYK liquidity provision as an infinite grid with no price limits.
- Volatility and fees: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] says higher volume and frequent trades generate more fee income.
- Stablecoin mitigation: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] says stablecoin pools have little impermanent loss because each asset aims to track one dollar.
- Beginner caution: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] says the name itself can mislead new users.

## Counterevidence & Qualifications
The source gives an intuitive explanation rather than a mathematical derivation. It does not quantify impermanent loss under different price moves, fee levels, pool weights, or concentrated-liquidity ranges.

## What Changed
- Added impermanent loss as a named DeFi market-making tradeoff.

## Related Concepts
- [[AutomatedMarketMaker]] - mechanism whose pool rebalancing creates impermanent loss.
- [[LiquidityProvision]] - role that bears the tradeoff.
- [[StablecoinYieldFarming]] - stablecoin pools try to reduce impermanent loss by pairing similarly priced assets.
- [[InvestmentRiskDiscipline]] - conceptually adjacent need to understand risk before chasing advertised yield.
