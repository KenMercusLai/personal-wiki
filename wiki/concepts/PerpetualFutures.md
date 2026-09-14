---
title: "Perpetual Futures"
type: concept
tags: [crypto, derivatives]
sources:
  - blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[PerpetualFutures]] are futures-like derivative contracts without a fixed delivery date, kept near spot price through periodic funding payments between long and short sides.

## Current Synthesis
The source explains perpetual futures by contrasting spot trading, margin shorting, dated futures, and a virtual future with no repayment date. Because there is no delivery deadline, funding fees substitute for expiry pressure: when long demand dominates, longs pay shorts; when short demand dominates, shorts pay longs. This periodic cost encourages crowded positions to close and keeps the perpetual price from drifting too far from spot.

## Key Claims
- Perpetual contracts let traders hold futures-like long or short exposure without a fixed delivery date.
- Funding fees are the mechanism that links perpetual prices back toward spot prices.
- Funding direction reflects relative demand between long and short sides.
- Larger leveraged demand tends to create larger spot-perpetual deviation and higher funding.
- Funding commonly settles every eight hours in the source's explanation.

## Evidence
- Contract contrast: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] walks from spot trading to borrowed shorting to delivery futures to perpetual contracts.
- Price tether: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] describes funding fees as the rubber band tying perpetual prices to spot.
- Direction rule: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] says stronger buyer demand makes buyers pay sellers, and stronger seller demand reverses the payment.
- Leverage pressure: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] says more leveraged demand increases price deviation and funding.
- Settlement cadence: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] uses every-eight-hour funding in both the mechanism and APY calculation.

## Counterevidence & Qualifications
This is a beginner explanation of perpetual futures, not a complete derivatives manual. Actual exchange designs can vary in funding formula, settlement interval, index composition, margin mode, insurance fund, auto-deleveraging, fee schedule, and liquidation mechanics.

## What Changed
- Created the concept to explain the derivative mechanism behind funding-rate arbitrage.

## Related Concepts
- [[FundingRateArbitrage]] - strategy that collects funding payments from perpetual futures.
- [[DeltaNeutralStrategy]] - position structure that pairs spot with perpetual exposure.
- [[CryptoArbitrage]] - broader arbitrage frame where perpetual funding is one source of yield.
