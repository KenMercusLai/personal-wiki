---
title: "Data Center Site Selection"
type: concept
tags: [data-centers, infrastructure, reliability, procurement, sustainability]
sources:
  - how-the-data-center-site-selection-process-works-at-dropbox
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[DataCenterSiteSelection]] is the governed process of converting capacity needs into a verified, risk-weighted, and commercially viable choice of facility, network paths, operating support, and lease terms.

## Current Synthesis
The Dropbox case presents site selection as a funnel rather than a single real-estate comparison. Capacity forecasts first become explicit power, cabinet-space, and availability-date requirements; providers that cannot meet them are excluded or expose the tradeoff requiring negotiation. The remaining candidates pass through an RFP, bid leveling, a technical questionnaire, an in-person site walk, weighted scoring, fiber-route diligence, and counterproposal negotiation.

The important control is evidence escalation. Provider statements establish candidates, detailed answers reveal design differences, physical inspection tests whether the offer matches the site, and route review tests whether nominally redundant circuits actually fail independently. Commercial variables then include not only rent and electricity but escalation, capacity ramps, efficiency overhead, incentives, and operational commitments. Sustainability and reliability therefore enter the contract and ranking model rather than sitting outside the acquisition decision.

## Key Claims
- Define the workload and deadline first: service demand and cabinet counts should resolve into required power, physical space, and an online date before provider comparison.
- Use progressive diligence: market screening, RFP requirements, questionnaires, site visits, route inspection, scoring, and negotiation answer different uncertainty classes.
- Verify physical reality independently of paperwork because installed equipment, loading access, construction status, building condition, monitoring, and fiber exposure can diverge from a proposal.
- Evaluate redundancy by failure domain, not component count; shared fiber routes, converged pathways, short emergency-power duration, weak alerting, or delayed generators can defeat nominal backup capacity.
- Weight nonnegotiable requirements explicitly across space, power, cooling, network, security, hazards, operations, logistics, staffing, and proximity rather than relying on an undifferentiated total.
- Join technical and commercial terms: rental rate, utility cost, escalation, capacity ramps, PUE, incentives, and tenant obligations determine whether a technically acceptable site remains economically and environmentally aligned.

## Evidence
- Capacity and gating: [[how-the-data-center-site-selection-process-works-at-dropbox]] starts with service and cabinet forecasts, then screens providers against power, space, and lease-commencement needs.
- Facility design and efficiency: [[how-the-data-center-site-selection-process-works-at-dropbox]] asks for Tier III-oriented design, floor-load support, carrier access, PUE, airflow containment, and renewable-energy preference.
- Failure-mode diligence: [[how-the-data-center-site-selection-process-works-at-dropbox]] reports a 30-second inertia-wheel bridge versus a five-minute conventional UPS example, construction-delay exposure, and inadequate automated alerts.
- Physical validation: [[how-the-data-center-site-selection-process-works-at-dropbox]] reports a loading dock that could not receive a promised 53-foot trailer directly, exposed exterior fiber, and wildlife inside a facility.
- Weighted decision model: [[how-the-data-center-site-selection-process-works-at-dropbox]] scores location, physical space, electricity, cooling, networking, physical security, hazards, and operations before reducing four to six site visits to two or three counterproposals.
- Path and contract diligence: [[how-the-data-center-site-selection-process-works-at-dropbox]] checks on-net and near-net carriers for shared fate and negotiates rent, electricity, escalation, ramping, PUE, abatements, allowances, and support space.

## Counterevidence & Qualifications
The synthesis rests on one first-party 2023 Dropbox account of three recent selection processes. It provides anecdotes and an illustrative scorecard but no candidate identities, raw responses, score definitions, weights, uncertainty analysis, realized uptime, lifecycle emissions, water use, final economics, or independent confirmation of “best in class” results. PUE measures facility energy overhead rather than the carbon intensity or full environmental footprint of electricity, and a contractual number still depends on measurement boundaries, operating conditions, and tenant behavior. Tier classification, weighted totals, and redundancy labels can also create false precision unless critical thresholds and correlated failure domains remain explicit. The process is most applicable to large tenants with enough demand, engineering expertise, provider access, and bargaining power to run a formal competitive RFP.

## What Changed
- Created a staged site-selection model joining capacity definition, technical diligence, physical verification, weighted scoring, network-path analysis, sustainability, and lease economics.

## Related Concepts
- [[SystemReliability]] - site selection chooses physical failure domains, monitoring, staffing, and recovery capacity before deployment.
- [[ReliabilityInvestment]] - redundancy and fault tolerance compete for capital and contractual commitment with cost and schedule.
- [[FailureInformedVendorSelection]] - proposal review and site walks search for concrete operational failure modes before vendor commitment.
- [[PrivateCloudStrategy]] - site selection implements one part of an owned or leased infrastructure strategy whose business justification remains separate.
- [[EnterpriseCloudMigration]] - retained physical capacity can complement, constrain, or delay a broader migration destination.
- [[CloudCostOptimization]] - rent, power, escalation, efficiency overhead, ramping, incentives, and utilization shape infrastructure cost beyond headline rates.
