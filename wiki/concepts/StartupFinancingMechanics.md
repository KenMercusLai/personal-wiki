---
title: "Startup Financing Mechanics"
type: concept
tags: [startup, finance, venture-capital]
sources:
  - cap-tables-share-structures-valuations-oh-my-a-case-study-of-early-stage-funding-crunchbase-news
  - dont-get-trampled-the-puzzle-for-unicorn-employees
  - not-all-vcs-are-assholes-mitchell-harper-medium
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[StartupFinancingMechanics]] is the practical system of shares, valuation, investor instruments, conversion terms, senior claims, and ownership and payout math that determines how fundraising changes a startup’s capitalization table and distributes exit proceeds.

## Current Synthesis
The Crunchbase case treats startup financing as a sequence of mechanical events rather than a vocabulary list. A company starts with common stock, founder allocations, and an employee pool; unpriced seed instruments promise future shares; and a priced Series A turns valuation assumptions into share prices, conversions, new shares, dilution, and control changes. Discounts, valuation caps, and conversion triggers determine who owns what after the round.

The exit side completes the same system. Ownership percentage or last-round share price does not determine payout when preferred investors and lenders have senior claims, a gap emphasized by [[dont-get-trampled-the-puzzle-for-unicorn-employees]]. A standard 1x non-participating preference generally lets an investor choose between recovering the original investment first or converting to common; Harper independently treats that form as acceptable and a 2x participating preference as a warning because it can return twice the investment before the investor also shares in the remainder. Debt is another senior claim. Change-of-control provisions can distribute protection or harm across the team, while document complexity can obscure these effects. Financing mechanics must therefore model the post-round cap table, governance provisions, and payout waterfall under multiple exit values, using understandable documents without treating founder comprehension as a substitute for legal review.

## Key Claims
- Financing mechanics begin before outside capital, when founders create common shares and set aside an employee pool.
- Unpriced seed rounds exchange current cash for future equity rather than a known ownership stake at signing.
- A priced round converts valuation into a share price, which then drives investor share counts.
- Seed discounts and caps can increase investor ownership by letting early investors buy shares below the Series A price.
- The actual post-money valuation can exceed simple pre-money plus new cash when conversion terms create additional share value.
- Preference multiples, participation rights, debt, and change-of-control provisions can make payout and team outcomes differ from headline ownership percentage.
- Understanding financing requires modeling both post-round ownership and exit-value distribution across plausible outcomes.

## Evidence
- Incorporation setup: [[cap-tables-share-structures-valuations-oh-my-a-case-study-of-early-stage-funding-crunchbase-news]] starts Internet of Wings with 10 million common shares split among Jill, Jack, and an employee pool.
- Unpriced-seed mechanics: [[cap-tables-share-structures-valuations-oh-my-a-case-study-of-early-stage-funding-crunchbase-news]] says the seed investors give cash without the company receiving a new valuation at that moment.
- Series A pricing: [[cap-tables-share-structures-valuations-oh-my-a-case-study-of-early-stage-funding-crunchbase-news]] calculates the Series A share price from a $15 million pre-money valuation and 10 million existing shares.
- Conversion effects: [[cap-tables-share-structures-valuations-oh-my-a-case-study-of-early-stage-funding-crunchbase-news]] shows one SAFE converting through a 20 percent discount and another through a $10 million valuation cap.
- Post-money qualification: [[cap-tables-share-structures-valuations-oh-my-a-case-study-of-early-stage-funding-crunchbase-news]] says the final post-money valuation is higher than pre-money plus Series A cash because seed conversion terms create additional shares at favorable prices.
- Preference waterfall: [[dont-get-trampled-the-puzzle-for-unicorn-employees]] explains that investors can be paid before common shareholders and warns that preference multiples above a standard 1x non-participating term can eliminate employee proceeds in a moderate exit.
- Debt priority: [[dont-get-trampled-the-puzzle-for-unicorn-employees]] identifies debt repayment as another claim ahead of shareholder distributions.
- Outcome modeling: [[dont-get-trampled-the-puzzle-for-unicorn-employees]] recommends calculating employee option payouts across a range of hypothetical sale or IPO values.
- Terms comparison: [[not-all-vcs-are-assholes-mitchell-harper-medium]] contrasts 1x non-participating preference with a 2x participating minimum and favors fair team change-of-control provisions.
- Document legibility: [[not-all-vcs-are-assholes-mitchell-harper-medium]] says Harper declined to negotiate term sheets he could not understand without a lawyer, framing clarity as a screening signal rather than a complete diligence process.

## Counterevidence & Qualifications
The Crunchbase source is a simplified fictitious case, Belsky provides a diligence framework rather than a worked cap table, and Harper offers a founder heuristic without publishing the relevant documents. Together they still omit stacked versus pari passu preferences, cumulative dividends, anti-dilution formulas, warrants, option-pool refreshes, pro rata rights, board control, debt covenants and maturity, taxes, transaction costs, escrow, earn-outs, exact change-of-control language, and legal-document variation. “Simple” terms can still be unfavorable, and needing counsel is not itself evidence of bad faith. IPO treatment also differs from an acquisition because preferred shares commonly convert and debt may be refinanced rather than paid through the same waterfall. The synthesis is finance literacy, not legal, tax, or investment advice.

## What Changed
- Added a founder-side comparison of 1x non-participating and 2x participating preferences.
- Extended legibility beyond payout math to term-sheet clarity and team change-of-control protections.

## Related Concepts
- [[UnpricedSeedFinancing]] - one early-stage mechanism inside the broader financing system.
- [[CapTableDilution]] - ownership consequence produced by new shares and conversion terms.
- [[BusinessFinanceLiteracy]] - broader ability to reason with business and finance vocabulary.
- [[StartupEquityTransparency]] - employee-side need to understand equity terms affected by financing mechanics.
- [[EmployeeEquityRisk]] - common-share outcomes depend on both ownership and senior claims.
- [[StartupRunway]] - financing leverage and terms can worsen when cash is running short.
