---
title: "Gift Card Fraud"
type: concept
tags: [fraud, payments, retail, gift-cards]
sources:
  - inside-the-wild-west-world-of-gift-card-bitcoin-brokering
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[GiftCardFraud]] is the theft, coercive acquisition, counterfeiting, account compromise, double spending, or laundering of stored-value card balances through redemption and resale channels.

## Current Synthesis
The source shows gift-card fraud as a systems problem rather than a single deceptive sale. Victims or compromised accounts can supply codes; brokers and marketplaces move them across borders; mobile apps turn numbers into checkout barcodes; retailers validate balances while often lacking provenance; card-for-card purchases convert exposed value into fresh codes; and downstream resellers return value to [[Bitcoin]] or cash-like markets.

Controls therefore act at several boundaries. Counterparty histories and delayed bitcoin release protect the broker, while transaction limits, restrictions on buying gift cards with gift cards, denomination controls, employee training, and chargeback liability can protect victims or issuers. These goals are not equivalent: a balance check can prevent the broker from being cheated while still completing the laundering of stolen value.

## Key Claims
- Gift-card codes can move internationally without physical transfer and function as cash-like settlement instruments.
- Card-for-card conversion can replace a compromised or jointly known code with a fresh one, protecting a broker while also laundering stolen value.
- Reputation checks, balance redemption, and delayed settlement reduce counterparty risk but do not prove lawful provenance.
- Retailer rules matter because checkout is the point where digital codes become newly activated and more marketable cards.
- Narrow limits can be bypassed when enforcement applies by card type or denomination rather than by customer, transaction, or aggregate value.
- Fraud losses and prevention incentives can be unevenly distributed among victims, issuers, retailers, marketplaces, and brokers.

## Evidence
- Transferability: [[inside-the-wild-west-world-of-gift-card-bitcoin-brokering]] describes buyers sending codes that a broker loaded into an app and redeemed through a barcode.
- Conversion loop: [[inside-the-wild-west-world-of-gift-card-bitcoin-brokering]] documents Walmart cards purchasing PlayStation and Steam cards for overseas resale and bitcoin reacquisition.
- Dual-use protection: [[inside-the-wild-west-world-of-gift-card-bitcoin-brokering]] says fresh cards reduced the risk that an original seller would drain the balance, while noting the same step could legitimize stolen value.
- Fraud sources: [[inside-the-wild-west-world-of-gift-card-bitcoin-brokering]] names coercive scams, account hacking, display-card theft, phishing, counterfeiting, and simultaneous resale and draining.
- Retail controls: [[inside-the-wild-west-world-of-gift-card-bitcoin-brokering]] reports card-value limits, purchase limits, gaming-card restrictions, and employee training announced by Walmart, Target, and Best Buy.
- Enforcement gap: [[inside-the-wild-west-world-of-gift-card-bitcoin-brokering]] reports that the broker continued buying multiple restricted cards by varying denominations despite Walmart's stated policy.

## Counterevidence & Qualifications
The article provides a detailed mechanism and one observed transaction but no representative prevalence estimate for fraudulent cards within peer-to-peer trades. The broker paid for the observed card, and the source does not allege that his transaction used stolen value. Reported retailer policy and store-level practice also conflicted, and the 2018 snapshot does not establish present controls or fraud patterns.

## What Changed
- Created a systems-level model separating broker self-protection from proof of lawful gift-card provenance.
- Added retailer checkout and card-for-card conversion as critical fraud-control boundaries.

## Related Concepts
- [[PeerToPeerCryptoTrading]] - provides a cross-border market in which gift cards can settle cryptocurrency trades.
- [[MarketplaceTrust]] - reputation and disputes reduce transaction uncertainty without eliminating provenance risk.
- [[AppInstallAttributionFraud]] - another fraud system that exploits gaps between observable signals and the underlying source of value.
- [[MarketplaceReviewFraud]] - similarly uses legitimate-looking transactions to manufacture a stronger downstream signal.
