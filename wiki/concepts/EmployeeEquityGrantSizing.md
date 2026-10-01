---
title: "Employee Equity Grant Sizing"
type: concept
tags: [startup, equity, compensation, hiring]
sources:
  - employee-equity-how-much-avc
  - quip
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[EmployeeEquityGrantSizing]] is the process of converting startup stage, role, level, market position, company value, and capitalization into a proposed employee ownership grant and refresh policy while separating exceptional early-hire negotiation from repeatable later-stage compensation.

## Current Synthesis
Wilson's framework draws a stage boundary. A startup's first few key hires may require bespoke grants expressed as percentage points because the company, role, and recruiting risk are not stable enough for a formula. After a core team is operating the business, the company can bracket roles, assign a salary multiplier to each bracket, multiply base salary by that multiplier to obtain a target grant value, and divide by an implied share price. Algebraically, `grant shares = salary × multiplier ÷ best company value × fully diluted shares`.

Homebrew supplies a second, percentile-based method. It recommends median cash and upper-quartile equity for early-stage employees, shows how ownership benchmarks vary with capital raised, and schedules performance-based refreshers no earlier than year two—at two years for directors and above and three years below director in its stated policy. Its two-offer example also treats cash and ownership as a risk-preference choice rather than a single mechanically correct mix.

Both methods are most useful as consistency mechanisms, not as claims that private shares have a cash-equivalent value. Wilson's "best value" is a current financing, sale, discounted-cash-flow, or public-comparable estimate rather than a 409A fair-market value. Homebrew's percentile depends on the benchmark sample, role match, stage, capitalization, and date. A complete employee explanation must distinguish sizing inputs from strike price, tax, vesting, dilution, payout seniority, and liquidity-adjusted outcomes.

## Key Claims
- The earliest key hires often require bespoke percentage negotiation because formula inputs are least reliable before the company has a core operating team.
- Mature grant programs can improve internal consistency by translating role, level, salary, market percentile, company value, and stage into an equity target.
- Fully diluted shares and a current company "best value" are required to convert the target value into a grant count.
- Role multipliers and market percentiles are time-dependent policy inputs, not durable constants.
- Retention grants can use the same framework with a cadence and seniority adjustment, but CEO and COO grants remain board decisions.
- Communicating the method improves legibility only if the company distinguishes internal grant value from realizable employee proceeds.

## Evidence
- Stage boundary: [[employee-equity-how-much-avc]] says the first roughly three to ten key hires may receive negotiated points of equity, while later hiring should move toward a repeatable dollar-value method.
- Target value: [[employee-equity-how-much-avc]] multiplies base salary by a role-bracket multiplier before converting that amount into shares.
- Conversion math: [[employee-equity-how-much-avc]] uses current company "best value" and fully diluted shares, or the equivalent implied share price, to calculate grant count.
- Governance and refresh cadence: [[employee-equity-how-much-avc]] excludes CEO and COO grants from the ordinary formula and halves the target value for grants refreshed every two years.
- Obsolescence warning: [[employee-equity-how-much-avc]] labels its published multipliers as 2010 figures and warns that later use would be below market.
- Communication intent: [[employee-equity-how-much-avc]] recommends describing grants in dollar terms to make the intended value and growth alignment tangible.
- Percentile policy: [[quip]] recommends targeting the 75th percentile for equity while targeting the 50th percentile for base salary.
- Historical stage benchmark: [[quip]] reports 0.64% as the 75th-percentile Engineering Manager grant in a ten-company 2015 segment that had raised $0–10 million.
- Refresh cadence: [[quip]] recommends performance-based refreshers no earlier than two years and distinguishes directors-and-above from more junior employees.
- Preference trade-off: [[quip]] illustrates two offers with different cash and ownership weights so a candidate can choose a risk profile.

## Counterevidence & Qualifications
The frameworks are investor-authored practitioner methods and supply no employee-outcome sample, bias audit, option-pricing model, or validation that salary multiplication or percentile targeting produces fair grants. Salary-linked equity can reproduce existing salary inequities, and role brackets can undervalue scarce contributors outside favored functions. "Best value" is a negotiable company estimate, not a liquid common-share price; the formula omits strike price, tax, vesting, dilution, preferences, debt, exercise windows, and probability or timing of liquidity. Wilson's numerical multipliers are explicitly obsolete. Homebrew's 2015 table is likewise historical, and its early-stage segment contains only ten companies; 0.64% is not a current or universal benchmark. A dual offer is informative only if the candidate can compare the packages on realistic, intelligible assumptions.

## What Changed
- Added a percentile-based complement to the salary-multiplier grant method.
- Added seniority-sensitive refresh timing and explicit cash-equity preference choice.
- Qualified the 2015 survey example against sample size, market drift, and private-equity risk.

## Related Concepts
- [[MarketBasedCompensation]] - supplies the market-sensitive role and skill context for grant inputs.
- [[StartupValuation]] - provides the company-value estimate used to derive the implied share price.
- [[StartupEquityTransparency]] - requires the calculation and its limitations to be understandable to candidates and employees.
- [[EmployeeEquityRisk]] - explains why calculated grant value can diverge from realized employee wealth.
- [[ExtendedStockOptionExerciseWindow]] - changes whether vested options remain usable after departure without changing initial grant sizing.
- [[StartupCompensationDesign]] - supplies the broader philosophy, levels, governance, and negotiation system around grant sizing.
