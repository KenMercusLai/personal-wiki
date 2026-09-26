---
title: "白话：区块链\"稳定币挖矿\"是什么"
type: source
tags: [crypto, defi, stablecoin, yield-farming]
date: 2021-04-18
source_file: '/mnt/ken_personal_wiki/Articles/Blog - taresky - 白话：区块链"稳定币挖矿"是什么.md'
---

## Summary
[[Taresky]] explains [[StablecoinYieldFarming]] as a lower-volatility form of DeFi participation: users provide or lend dollar-pegged stablecoins through smart contracts so other traders can swap or speculate, then earn fees, platform-token rewards, or auto-compounded yield. The article walks from centralized exchanges to decentralized exchanges, [[AutomatedMarketMaker]] pricing, [[LiquidityProvision]], platform-token incentives, and [[ImpermanentLoss]], then turns into a risk inventory covering fiat on-ramps, exchange custody, wallet custody, stablecoins, public chains, smart contracts, token approvals, APY presentation, OTC exits, tax, and unknown risk. Its worked example uses [[BeltFinance]] stablecoin liquidity and [[BeefyFinance]] vault compounding while warning that the specific project context was time-sensitive and should not be copied mechanically.

## Key Claims
- Stablecoin mining is like earning commissions from a casino rather than placing the directional bet: the provider supplies stablecoin liquidity or loans and earns from traders' activity.
- [[AutomatedMarketMaker]] pricing can make DEX swaps possible without centralized custody, but useful execution still depends on enough [[LiquidityProvision]] depth.
- Platform-token rewards turn ordinary liquidity provision into yield farming, but platform-token price support is fragile and can be damaged by sell pressure, weak fee revenue, or risky "second mining" pairs.
- [[ImpermanentLoss]] is not a mysterious defect; it is the tradeoff of a rebalancing market-making strategy that underperforms simple holding when prices trend strongly.
- [[StablecoinYieldFarming]] reduces but does not eliminate risk because stablecoin baskets, smart contracts, chain design, wallet custody, token approvals, APY math, OTC flows, and legal/tax issues can each become loss points.
- [[CryptoWalletSecurity]] matters before any yield strategy because copied seed phrases, hot devices, third-party keyboards, malicious signatures, and unlimited token approvals can expose funds.
- [[BeefyFinance]]-style vaults can reduce small-user gas and compounding friction by pooling LP-token staking and reinvestment, but they add another smart-contract interaction and platform dependency.

## Key Quotes
> "你来到了赌场，但不参与赌博，而是赚取其他赌客们的佣金" - the article's analogy for stablecoin yield farming.

> "展示的年化收益率（Annual Percentage Yield, APY）仅代表当前时刻" - the article's warning that headline APY is not a durable return promise.

## Connections
- [[Taresky]] - author explaining stablecoin mining to beginners through plain-language casino and market-making analogies.
- [[StablecoinYieldFarming]] - central practice described by the source.
- [[LiquidityProvision]] - operational behavior of depositing assets into DEX pools to earn fees and rewards.
- [[AutomatedMarketMaker]] - pricing model used to explain Uniswap-style decentralized exchange quotes.
- [[ImpermanentLoss]] - market-making tradeoff that stablecoin pools try to reduce.
- [[DeFiRiskStack]] - risk taxonomy across custody, stablecoins, chains, smart contracts, approvals, APY presentation, and fiat exits.
- [[CryptoWalletSecurity]] - source gives concrete private-key, seed-phrase, hardware-wallet, and authorization guidance.
- [[Binance]] - centralized exchange and BSC context for the source's on-ramp and low-fee-chain discussion.
- [[BeltFinance]] - example stablecoin liquidity protocol used in the walkthrough.
- [[BeefyFinance]] - auto-compounding vault example for staking Belt LP tokens.

## Contradictions
- No direct contradiction found. The article's high APY examples are internally qualified as time-sensitive bull-market observations and are not durable return guarantees.
