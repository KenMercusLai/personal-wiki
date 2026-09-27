---
title: "Employee Equity Grant Sizing"
type: concept
tags: [startup, equity, compensation, hiring]
sources:
  - employee-equity-how-much-avc
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[EmployeeEquityGrantSizing]] is the process of converting a startup role, salary, company value, and fully diluted capitalization into a proposed number of employee shares while separating exceptional early-hire negotiation from repeatable later-stage compensation policy.

## Current Synthesis
Wilson's framework draws a stage boundary. A startup's first few key hires may require bespoke grants expressed as percentage points because the company, role, and recruiting risk are not stable enough for a formula. After a core team is operating the business, the company can bracket roles, assign a salary multiplier to each bracket, multiply base salary by that multiplier to obtain a target grant value, and divide by an implied share price. Algebraically, `grant shares = salary × multiplier ÷ best company value × fully diluted shares`.

The method is most useful as a consistency mechanism, not as a claim that private shares have a cash-equivalent value. Its "best value" is a current financing, sale, discounted-cash-flow, or public-comparable estimate rather than a 409A fair-market value. Role multipliers must be refreshed against the actual labor market: the source explicitly warns that its 2010 examples became too low, particularly for senior hires. A complete employee explanation must therefore distinguish the grant-sizing input from strike price, tax, vesting, dilution, payout seniority, and liquidity-adjusted outcomes.

## Key Claims
- The earliest key hires often require bespoke percentage negotiation because formula inputs are least reliable before the company has a core operating team.
- Mature grant programs can improve internal consistency by translating role level and salary into a target equity value before calculating shares.
- Fully diluted shares and a current company "best value" are required to convert the target value into a grant count.
- Role multipliers are market- and time-dependent policy inputs, not durable constants.
- Retention grants can use the same framework with a cadence adjustment, but CEO and COO grants remain board decisions.
- Communicating the method improves legibility only if the company distinguishes internal grant value from realizable employee proceeds.

## Evidence
- Stage boundary: [[employee-equity-how-much-avc]] says the first roughly three to ten key hires may receive negotiated points of equity, while later hiring should move toward a repeatable dollar-value method.
- Target value: [[employee-equity-how-much-avc]] multiplies base salary by a role-bracket multiplier before converting that amount into shares.
- Conversion math: [[employee-equity-how-much-avc]] uses current company "best value" and fully diluted shares, or the equivalent implied share price, to calculate grant count.
- Governance and refresh cadence: [[employee-equity-how-much-avc]] excludes CEO and COO grants from the ordinary formula and halves the target value for grants refreshed every two years.
- Obsolescence warning: [[employee-equity-how-much-avc]] labels its published multipliers as 2010 figures and warns that later use would be below market.
- Communication intent: [[employee-equity-how-much-avc]] recommends describing grants in dollar terms to make the intended value and growth alignment tangible.

## Counterevidence & Qualifications
The framework comes from one investor's simplified adaptation of compensation-consulting practice and supplies no labor-market dataset, employee-outcome sample, bias audit, option-pricing model, or validation that salary multiplication produces fair grants. Salary-linked equity can reproduce existing salary inequities, and role brackets can undervalue scarce contributors outside favored functions. "Best value" is a negotiable company estimate, not a liquid common-share price; the formula omits strike price, tax, vesting, dilution, preferences, debt, exercise windows, and probability or timing of liquidity. The source's three-to-fivefold growth expectation is aspirational, and its numerical multipliers are explicitly obsolete.

## What Changed
- Established a stage-sensitive distinction between bespoke early-hire grants and formula-based grants after a core team exists.
- Added the salary-multiplier and fully diluted share calculation as a consistency framework.
- Made market refresh, salary-equity bias, and the difference between internal grant value and realizable proceeds explicit.

## Related Concepts
- [[MarketBasedCompensation]] - supplies the market-sensitive role and skill context for grant inputs.
- [[StartupValuation]] - provides the company-value estimate used to derive the implied share price.
- [[StartupEquityTransparency]] - requires the calculation and its limitations to be understandable to candidates and employees.
- [[EmployeeEquityRisk]] - explains why calculated grant value can diverge from realized employee wealth.
- [[ExtendedStockOptionExerciseWindow]] - changes whether vested options remain usable after departure without changing initial grant sizing.
