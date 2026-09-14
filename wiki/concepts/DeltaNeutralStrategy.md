---
title: "Delta Neutral Strategy"
type: concept
tags: [trading, risk, crypto]
sources:
  - blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[DeltaNeutralStrategy]] is a trading posture that offsets long and short exposure so the position is designed to be relatively insensitive to the underlying asset's price direction.

## Current Synthesis
The source introduces delta neutrality through a simple crypto funding example: use part of the capital to buy spot Bitcoin and part to short the corresponding perpetual future. If Bitcoin rises, the spot leg gains and the short leg loses; if Bitcoin falls, the spot leg loses and the short leg gains. The desired residual return is not directional price movement but funding payments from the side willing to pay for leverage.

## Key Claims
- Delta neutrality aims to remove or reduce directional exposure rather than eliminate all risk.
- A spot-long plus perpetual-short pair can be approximately market-neutral for the same coin.
- Capital allocation affects yield because hedging often requires capital on both sides of the trade.
- Margin mode and leverage choices change liquidation risk even when net directional exposure is near zero.
- Execution spread matters because entering spot and derivative legs at unfavorable prices can overwhelm funding income.

## Evidence
- Exposure offset: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] says BTC spot gains offset perpetual short losses when BTC rises, and vice versa when BTC falls.
- Yield source: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] explains that the short perpetual order receives funding from leveraged longs in the example.
- Capital allocation: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] adjusts annualized yield downward because only half the capital is in the funding-receiving contract leg.
- Liquidation caveat: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] says a 1x short can be liquidated if the contract price nearly doubles, while lower leverage reduces yield by requiring more collateral.
- Spread caveat: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] warns that spot and perpetual prices are close but not identical, so poor entry and frequent repositioning can consume gains.

## Counterevidence & Qualifications
The source's example is simplified. Real delta-neutral trading can still have basis risk, liquidation risk, funding reversal, borrow constraints, exchange outages, margin-mode coupling, slippage, fees, tax effects, and imperfect hedge ratios.

## What Changed
- Created the concept to explain the exposure-management logic behind the funding-rate strategy.

## Related Concepts
- [[FundingRateArbitrage]] - uses delta-neutral construction to collect funding.
- [[PerpetualFutures]] - derivative leg commonly used in the source's example.
- [[CryptoArbitrage]] - broader family of strategies where delta neutrality can reduce price exposure.
- [[InvestmentRiskDiscipline]] - required because neutral exposure is not the same as no risk.
