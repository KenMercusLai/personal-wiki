---
title: "OKX"
type: entity
tags: [exchange, crypto]
sources:
  - blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[OKX]] appears in the wiki as a cryptocurrency exchange example for hourly auction-based lending.

## Current Profile
The source describes OKX lending as a dark-pool auction: lenders set a minimum acceptable rate, deposit funds, and are matched hourly from lower to higher rates against borrower demand. This structure can produce fairer clearing and occasional high yields, but the result is unstable because user funds can remain unmatched.

## Key Characteristics
- Uses minimum-rate lending orders rather than immediate fixed-rate subscription.
- Matches supply and demand around each hourly auction interval.
- Can clear all matched lenders at a higher marginal rate in the source's simplified example.
- Creates standing-idle risk when offered funds are not matched.

## Evidence
- Auction mechanics: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] explains that lenders set a minimum rate and OKX matches hourly according to borrowing demand.
- Clearing example: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] gives a scenario where lower-rate and partially higher-rate lenders both receive the 10% clearing rate.
- Tradeoff: [[blog-taresky-wu-feng-xian-nian-hua-360-xiao-bai-crypto-tao-li]] says the model can be fair and occasionally high-yielding but unstable.

## Qualifications
The page reflects the article's March 2024 description and does not verify later OKX product design, availability, or jurisdiction-specific restrictions.

## What Changed
- Created OKX as an exchange entity tied to auction-style lending.

## Relationships
- [[ExchangeLending]] - OKX is the auction-based model in the article's exchange comparison.
- [[Binance]] - contrasted dynamic flexible lending model.
- [[Bitfinex]] - contrasted order-book lending model.
