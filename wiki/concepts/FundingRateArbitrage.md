---
title: "Funding Rate Arbitrage"
type: concept
tags: [crypto, arbitrage, derivatives]
sources:
  - blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[FundingRateArbitrage]] is a crypto arbitrage strategy that attempts to collect perpetual-contract funding payments while offsetting token-price exposure, commonly by holding spot and shorting the corresponding perpetual contract.

## Current Synthesis
The Taresky source presents funding-rate arbitrage as the more powerful but riskier step beyond exchange lending. In a bull market, leveraged long demand often makes longs pay shorts. A trader can split capital, buy spot Bitcoin, short Bitcoin perpetuals, and aim for near-zero directional exposure while collecting funding every eight hours. The strategy's returns depend on capital utilization, funding level, fees, spread control, leverage, and whether the position survives volatility without liquidation.

## Key Claims
- Funding-rate arbitrage depends on imbalanced perpetual demand, especially bull-market long demand paying short positions.
- Spot-plus-short-perpetual positioning can neutralize directional price exposure while preserving funding income.
- Yield must be adjusted for capital utilization because only part of the capital may be deployed as the funding-receiving leg.
- High funding can be temporary because expensive funding encourages crowded positions to close.
- The main practical risks are liquidation, bad spot-perpetual spread entry, fees, frequent rebalancing, execution failure, and concentration in volatile small coins.
- Data tools such as [[Coinglass]] and execution tools such as [[AICOIN]] are useful but do not remove strategy risk.

## Evidence
- Payment source: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] says bull-market long demand often means long perpetual holders pay shorts.
- Neutral construction: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] explains buying spot BTC while shorting BTC perpetuals so spot gains offset contract losses and vice versa.
- APY math: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] gives a 0.1% per-settlement example: 0.3% per day, 109.5% annualized before the 50% capital-utilization adjustment to 54.75%.
- Instability: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] says high funding can disappear as positions close to avoid fees.
- Visual market evidence: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] includes inspected Coinglass screenshots showing many assets above 50% annualized funding and some extreme positive or negative rates.
- Execution warning: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] says poor spread control, frequent opening and closing, API/local-machine problems, or misunderstanding tool parameters can erase gains or cause losses.

## Counterevidence & Qualifications
The source describes a favorable March 2024 bull-market environment. It does not prove that funding-rate arbitrage remains profitable after fees, slippage, taxes, borrow costs, exchange risk, stablecoin risk, and liquidation tail events across market regimes. The strategy is also capacity-limited: more arbitrage capital can compress the opportunity.

## What Changed
- Created the concept to capture the source's main crypto arbitrage strategy.

## Related Concepts
- [[PerpetualFutures]] - funding-rate arbitrage exists because perpetual contracts use periodic funding.
- [[DeltaNeutralStrategy]] - the strategy's spot-plus-short construction is meant to neutralize price direction.
- [[ExchangeLending]] - lower-threshold yield source compared with funding-rate arbitrage.
- [[CryptoArbitrage]] - broader family containing this strategy.
- [[InvestmentRiskDiscipline]] - necessary guardrail against leverage, liquidation, and bull-market temptation.
