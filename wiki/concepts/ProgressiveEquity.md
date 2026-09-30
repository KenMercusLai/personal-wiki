---
title: "Progressive Equity"
type: concept
tags: [startup, equity, compensation, employee-ownership]
sources:
  - introducing-progressive-equity-detour-blog-medium
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[ProgressiveEquity]] is an employee-equity design that caps part of a participant's upside at a company-defined financial-independence threshold and redistributes the released value pro rata to eligible employees at a major liquidity event.

## Current Synthesis
[[AndrewMason]] proposed the design at [[Detour]] after concluding that conventional startup equity had produced highly concentrated employee outcomes at [[Groupon]] and that redistribution attempted after success was costly and difficult to approve. In the published implementation, employee grants are divided equally between ordinary and progressive RSUs. Progressive RSUs stop appreciating once their value reaches half the threshold; ordinary RSUs continue appreciating, creating the intended effect of retaining half of value above the threshold. A separate kicker pool starts empty, receives the released value, and is distributed pro rata once at a large secondary sale, acquisition, or IPO.

The design changes the distribution of very large employee payoffs without reducing investor value because investors are excluded. That makes it narrower than company-wide progressive taxation and different from [[EmployeeProfitSharing]]: it reallocates participating employee equity proceeds at a liquidity event rather than recurring profit. It also does not remove ordinary [[EmployeeEquityRisk]]. Employees still depend on company success and a qualifying event, cannot opt out, and lose kicker eligibility if they leave before redistribution. Whether it broadens ownership fairly depends on the actual threshold, pro-rata denominator, grant distribution, termination rules, and legal and tax implementation, none of which the source validates through a completed outcome.

## Key Claims
- The program encodes an ex-ante rule for limiting extreme employee-equity concentration instead of relying on founders or boards to redistribute value after success is visible.
- Splitting grants evenly between ordinary and capped progressive RSUs implements an effective 50% reduction in appreciation above the threshold.
- The kicker pool turns value released by participants above the threshold into additional employee proceeds at one qualifying liquidity event.
- Investors remain outside the program, so redistribution occurs within participating employee equity rather than across the whole capitalization table.
- Eligibility is conditional: employees cannot opt out, and people who leave before the trigger do not receive the redistribution.
- The proposal is a documented mechanism and incentive hypothesis, not evidence that it improves retention, performance, fairness, or realized employee wealth.

## Evidence
Mechanism and objective:
- [[introducing-progressive-equity-detour-blog-medium]] states the objective of increasing the number of employees who reach financial independence while reducing newly created dynastic wealth.
- [[introducing-progressive-equity-detour-blog-medium]] describes equal normal and Progressive RSU pools, caps the progressive half at 50% of the threshold, and routes released value into a kicker pool.

Trigger and scope:
- [[introducing-progressive-equity-detour-blog-medium]] makes redistribution a one-time event at a large secondary, sale, or IPO and excludes investors from participation.
- [[introducing-progressive-equity-detour-blog-medium]] says employees cannot opt out and leavers do not participate in the kicker pool.

Motivation and portability:
- [[introducing-progressive-equity-detour-blog-medium]] cites concentrated outcomes at Groupon, failed attempts at later board-approved redistribution, and adverse tax effects from personal transfers as reasons to establish the rule early.
- [[introducing-progressive-equity-detour-blog-medium]] publishes a legal template for reuse and improvement but reports no adoption or completed payout.

## Counterevidence & Qualifications
The evidence is one founder's 2015 first-party proposal using fictional figures. It does not disclose Detour's actual threshold, cap table, pool sizes, distribution weights, employee grant dispersion, governance approvals, or realized outcome. A pro-rata kicker may still favor employees who already hold larger grants, while investor exclusion leaves the broader founder-investor-employee distribution unchanged. Leaver exclusion can intensify retention pressure and becomes especially consequential around involuntary termination or a delayed exit. The post does not analyze taxes, securities law, accounting, dilution, acquisition treatment, international employees, preferences, debt, exercise or settlement mechanics, or whether the published paperwork remains usable. The author's report that employees liked the program is not a survey, and his dismissal of objections does not address legitimate risk, liquidity, or household-finance differences.

## What Changed
- Established Progressive Equity as an ex-ante, threshold-based redistribution mechanism rather than a general equity grant formula.
- Separated the capped progressive RSUs, ordinary RSUs, and event-funded kicker pool.
- Made investor exclusion, mandatory participation, leaver ineligibility, and the absence of realized outcome evidence explicit.

## Related Concepts
- [[EmployeeEquityRisk]] - Progressive Equity changes the upside distribution while retaining company, liquidity-event, eligibility, and employment-duration risk.
- [[StartupEquityTransparency]] - the threshold, cap, trigger, denominator, eligibility, and termination rules must be legible to employees.
- [[EmployeeEquityGrantSizing]] - determines an initial award, whereas Progressive Equity changes how part of that award appreciates and redistributes.
- [[EmployeeProfitSharing]] - shares value broadly through recurring profit rather than a one-time employee-equity transfer.
- [[CapTableDilution]] - remains relevant to employee ownership even though the proposed redistribution is designed not to affect investors.
- [[ExtendedStockOptionExerciseWindow]] - addresses post-departure preservation of vested options, while Progressive Equity excludes leavers from the kicker.
