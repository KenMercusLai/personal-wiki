---
title: "Liquidity Provision"
type: concept
tags: [crypto, defi, markets]
sources:
  - blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[LiquidityProvision]] is the act of depositing assets into a market, exchange, or smart-contract pool so other users can trade or borrow against that depth.

## Current Synthesis
In the Taresky stablecoin-mining source, liquidity provision is the bridge between decentralized exchange usability and yield farming. A DEX can quote prices through an [[AutomatedMarketMaker]], but if the pool is shallow, trades suffer large slippage and bad execution. Platforms therefore reward liquidity providers with swap fees and often incentive tokens, turning market depth into a paid role with its own price, contract, and incentive risks.

## Key Claims
- Decentralized exchanges need liquidity depth because pricing logic alone does not make trades attractive.
- Liquidity providers deposit assets into smart contracts and earn a share of trading fees.
- Incentive tokens can make liquidity provision more attractive but also connect provider returns to platform-token price support.
- Providing liquidity is economically similar to market making and can underperform simply holding assets when prices trend.
- Stablecoin liquidity provision narrows volatility exposure but remains exposed to stablecoin and platform risks.

## Evidence
- DEX depth problem: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] says thin pools make prices swing sharply and become unattractive for swappers.
- Fee reward: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] describes 0.2%-0.3% swap fees distributed among market makers.
- Incentive layer: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] says platform tokens turn basic liquidity provision into the more mature form of mining.
- Market-making tradeoff: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] compares XYK liquidity provision to an infinite grid strategy that buys down and sells up.
- Stablecoin qualification: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] treats stablecoin liquidity as lower impermanent-loss but not riskless because any constituent stablecoin or smart contract can fail.

## Counterevidence & Qualifications
The source explains liquidity provision through AMM pools and does not cover order-book market making, concentrated liquidity, professional market-maker agreements, or post-2021 protocol changes.

## What Changed
- Added liquidity provision as the market-depth behavior underlying DEX fees and yield farming.

## Related Concepts
- [[AutomatedMarketMaker]] - mechanism that prices trades against liquidity pools.
- [[StablecoinYieldFarming]] - common DeFi use case built on stablecoin liquidity provision.
- [[ImpermanentLoss]] - key tradeoff borne by liquidity providers.
- [[ExchangeLending]] - adjacent way to supply capital to crypto market participants.
