---
title: "DeFi Risk Stack"
type: concept
tags: [crypto, defi, risk, investing]
sources:
  - blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[DeFiRiskStack]] is the layered set of risks a user accepts when moving from fiat into decentralized finance, holding assets, granting permissions, earning yield, and exiting back to fiat.

## Current Synthesis
The Taresky stablecoin-mining source treats DeFi risk as a chain rather than a single protocol question. A user can lose money before farming starts through OTC transfer scrutiny, exchange failure, or wallet compromise; during farming through stablecoin failure, public-chain centralization, smart-contract bugs, malicious approvals, misleading APY, gas costs, or extra vault layers; and after farming through dirty-money exposure, foreign-exchange issues, tax ambiguity, and unknown unknowns. The result is a useful warning: reducing price volatility with stablecoins does not remove operational, counterparty, legal, and behavioral risk.

## Key Claims
- DeFi risk starts at the fiat on-ramp, not only inside the yield protocol.
- Wallet custody and token approvals are core user-side risks because signatures and allowances can expose assets.
- Stablecoins carry issuer, reserve, peg, and design risks even when their market price appears calm.
- Public-chain choice changes the trust model; lower fees can come with more centralization or wrapped-asset dependency.
- APY is a fragile display number shaped by current fees, token emissions, compounding assumptions, and exit timing.
- Fiat exit can introduce banking, anti-money-laundering, foreign-exchange, and tax risk.

## Evidence
- On-ramp and exchange custody: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] warns about OTC bank-transfer scrutiny, exchange freezing windows, exchange failure, and hacks.
- Wallet and approvals: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] treats seed phrases as equivalent to private keys and warns that malicious or unlimited approvals can later drain funds.
- Stablecoin and chain risk: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] contrasts trust-backed stablecoins with overcollateralized or algorithmic designs and calls BSC cheaper but more centralized.
- Protocol and APY risk: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] says contract safety is hard for normal users to evaluate and that APY usually reflects only a current moment.
- Exit risk: [[blog-taresky-bai-hua-qu-kuai-lian-wen-ding-bi-wa-kuang-shi-shen-me]] warns that OTC cash-out funds can be tainted and that some fiat conversion paths may create regulatory or tax exposure.

## Counterevidence & Qualifications
The legal and compliance discussion is source-scoped and written for a Chinese retail-user context. It should not be read as current legal advice, jurisdiction-neutral guidance, or a substitute for professional tax, banking, or regulatory analysis.

## What Changed
- Added a layered DeFi risk concept that connects stablecoin farming mechanics to custody, protocol, APY, exit, and legal risks.

## Related Concepts
- [[StablecoinYieldFarming]] - strategy whose lower volatility still inherits the full risk stack.
- [[CryptoWalletSecurity]] - user-side custody and approval layer within DeFi risk.
- [[InvestmentRiskDiscipline]] - broader behavioral discipline around unfamiliar yield and leverage.
- [[CryptoArbitrage]] - adjacent crypto-yield practice with similar exchange, stablecoin, execution, and behavioral risk.
