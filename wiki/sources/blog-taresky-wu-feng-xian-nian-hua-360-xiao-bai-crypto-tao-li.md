---
title: "无风险年化 360%？小白也能懂的 Crypto 套利"
type: source
tags: [crypto, arbitrage, funding-rate, investing]
date: 2024-03-04
source_file: "/mnt/ken_personal_wiki/Articles/Blog - taresky - 无风险年化 360%？小白也能懂的 Crypto 套利.md"
---

## Summary
[[Taresky]] explains why bull-market cryptocurrency markets can offer high apparent "risk-free" yields through exchange lending and [[FundingRateArbitrage]], while repeatedly narrowing "risk-free" to market-neutral positioning rather than exchange, stablecoin, liquidation, operational, or behavioral safety. The article frames [[CryptoArbitrage]] profits as coming from leveraged speculative demand and argues that arbitrage competition can improve liquidity and reduce trader friction. It gives beginner-friendly mechanics for [[ExchangeLending]], [[PerpetualFutures]], and [[DeltaNeutralStrategy]], then closes with risk discipline: avoid gambling, start small, lower expectations, and leave when the market regime changes.

## Key Claims
- Crypto arbitrage yield is funded by leveraged traders and exchange borrowers rather than by magic passive income.
- [[ExchangeLending]] differs by platform design: [[Bitfinex]] exposes an order book, [[OKX]] uses hourly dark-pool auction matching, and [[Binance]] dynamically matches flexible lending demand.
- [[PerpetualFutures]] use funding fees to pull contract prices toward spot prices when long or short demand becomes imbalanced.
- [[FundingRateArbitrage]] can be built by holding spot while shorting the corresponding perpetual contract, producing a [[DeltaNeutralStrategy]] that collects funding when longs pay shorts.
- The rough yield calculation in the source is APY = capital utilization x funding rate x 3 x 365, because funding commonly settles every eight hours.
- High headline APYs are unstable and come with liquidation, spread, fee, execution, exchange, stablecoin, API, network, and temptation-to-gamble risks.
- Inspected images show March 2024 examples of exchange lending yields near 20-46%, Coinglass heatmaps with many coins above 50% annualized funding, and high/low funding-rate rankings with extreme positive and negative rates.

## Key Quotes
> "利润，来自于其他人的亏损" — the article's zero-sum explanation of crypto arbitrage yield.

> "APY = 资金利用率 x 资金费 x 3 x 365" — the article's simplified funding-arbitrage yield formula.

## Connections
- [[Taresky]] - author explaining crypto arbitrage to non-specialists while disclaiming system and behavior risks.
- [[CryptoArbitrage]] - central practice described across exchange lending and funding-rate strategies.
- [[ExchangeLending]] - beginner strategy where users lend funds through exchange products to margin borrowers.
- [[FundingRateArbitrage]] - main strategy explained through spot-plus-short perpetual positioning.
- [[PerpetualFutures]] - derivative mechanism whose funding fees create the arbitrage opportunity.
- [[DeltaNeutralStrategy]] - market-neutral posture used to reduce directional exposure while collecting funding.
- [[Binance]] - exchange example for dynamic flexible lending.
- [[OKX]] - exchange example for hourly dark-pool auction lending.
- [[Bitfinex]] - exchange example for order-book lending.
- [[AICOIN]] - tool the source names for simultaneous spread/rate order execution.
- [[Coinglass]] - funding-rate heatmap and ranking source shown in inspected screenshots.
- [[Bitcoin]] - main-coin example used in the funding-arbitrage explanation.
- [[Ethereum]] - appears in the Coinglass heatmap as a major funding-rate market.
- [[InvestmentRiskDiscipline]] - adjacent concept: the article warns against leverage, temptation, overconcentration in high APY names, and chasing bull-market returns.

## Contradictions
- No direct contradiction found. The source's "risk-free" language is qualified internally and should not be read as contradicting the wiki's investment-risk pages, which emphasize behavioral, counterparty, and leverage risk.
