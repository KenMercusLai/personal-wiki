---
title: "Automated Market Maker"
type: concept
tags: [crypto, defi, markets]
sources:
  - blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[AutomatedMarketMaker]] is a smart-contract market mechanism that quotes asset exchange rates from pool balances rather than from a centralized order book.

## Current Synthesis
The Taresky stablecoin-mining source uses the Uniswap-style constant-product formula, X*Y=K, to explain why decentralized exchanges can quote prices directly from liquidity-pool balances. The model makes wallet-to-contract-to-wallet swaps possible, but it also makes price impact depend on pool depth and pushes liquidity providers into a rebalancing strategy. That rebalancing can earn fees in sideways or active markets and underperform holding when one asset trends strongly.

## Key Claims
- AMMs let decentralized exchanges quote and execute swaps through public smart-contract logic.
- The constant-product model raises the marginal price of an asset as its pool balance falls.
- Arbitrageurs connect AMM prices to outside markets when price gaps exceed fees.
- Pool depth determines slippage and therefore whether the quoted trade is attractive.
- AMM liquidity provision resembles an always-on rebalancing or grid strategy.

## Evidence
- Pricing formula: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] explains the classic Uniswap X*Y=K mechanism where K stays constant while X and Y balances shift.
- DEX execution: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] contrasts wallet-signed smart-contract swaps with centralized exchange custody.
- Arbitrage linkage: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] says bots arbitrage differences between exchanges when gaps cover fees.
- Depth and slippage: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] says insufficient funds in a pair make prices move sharply and discourage traders.
- Grid analogy: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] describes XYK as an infinite grid from zero to infinity that continuously buys low and sells high.

## Counterevidence & Qualifications
The source centers the classic constant-product model and briefly names Curve's stablecoin math without explaining it. It should not be treated as a full taxonomy of AMM designs, concentrated liquidity, hybrid curves, or professional liquidity-management strategies.

## What Changed
- Added automated market maker as the pricing mechanism behind the source's DEX and liquidity-mining explanation.

## Related Concepts
- [[LiquidityProvision]] - supplies the pool balances an AMM prices against.
- [[ImpermanentLoss]] - rebalancing tradeoff created by AMM pool mechanics.
- [[SmartContracts]] - AMMs are implemented as smart-contract programs.
- [[StablecoinYieldFarming]] - stablecoin pools often use AMM or AMM-adjacent mechanisms.
