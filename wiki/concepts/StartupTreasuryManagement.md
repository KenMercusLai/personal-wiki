---
title: "Startup Treasury Management"
type: concept
tags: [startup, treasury, banking, risk]
sources:
  - my-startup-banking-story
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[StartupTreasuryManagement]] is the operating discipline of safeguarding, allocating, monitoring, and moving a startup's cash across accounts and financial institutions while maintaining payment continuity, fraud controls, liquidity, and clear ownership.

## Current Synthesis
The HashiCorp case shows treasury becoming a distinct management problem when funding transforms a founder-opened account into a material corporate cash position. The risk was not only that roughly $35 million sat at one bank; it also came from treating the account as infrastructure requiring no relationship, inventory, monitoring, or retirement process. Hiring a finance leader improved safeguarding and cash use, moved the main balance, and eventually diversified the banking setup, but migration was incomplete because customer payment instructions still pointed at the old account.

That incomplete lifecycle created the source's most durable lesson. A zero balance did not make the account irrelevant: incoming receivables restored funds, recurring fraudulent wires escaped notice, and the later fraud lock removed the normal electronic exit path. Good treasury management therefore spans both strategic allocation and mundane controls—knowing every open account, reconciling activity, updating counterparties, revoking obsolete routes, closing accounts promptly, maintaining escalation contacts, and planning how controls behave during an incident.

## Key Claims
- Treasury risk grows with cash scale and operating complexity even when the underlying bank account has not changed.
- Bank diversification can reduce concentration exposure, but it does not replace reconciliation, access control, or account-lifecycle discipline.
- A banking migration is incomplete until inbound payment instructions, residual balances, authorities, and obsolete accounts are reconciled and retired.
- Relationship banking can supply context and escalation paths; declining it may leave a startup with only generic processes during exceptional events.
- Fraud containment may deliberately restrict liquidity, so incident and closure plans must account for blocked electronic transfers and branch or instrument limits.
- Professional finance ownership can surface risks that a product-focused founder neither recognizes nor monitors consistently.

## Evidence
- Scale transition: [[my-startup-banking-story]] traces one account from a $20,000 founder loan to roughly $35 million after seed, Series A, and Series B funding.
- Professional ownership: [[my-startup-banking-story]] says a new VP of Finance identified the concentrated cash balance as unsafe and proposed better safeguarding and use.
- Diversification: [[my-startup-banking-story]] says HashiCorp had spread balances across multiple banks before the later Silicon Valley Bank crisis.
- Incomplete migration: [[my-startup-banking-story]] says the Chase account stayed open because closure required an in-person visit and some customers continued paying it.
- Monitoring failure: [[my-startup-banking-story]] says recurring fraudulent wires exceeded $100,000 over more than a year before a routine internal audit found them.
- Control-liquidity collision: [[my-startup-banking-story]] says the fraud lock disabled electronic transfers, requiring advance branch funding and a roughly $1 million cashier's check to close the account.
- Relationship gap: [[my-startup-banking-story]] recounts repeated outreach from the original banker that the founder dismissed before later needing unusual branch coordination.

## Counterevidence & Qualifications
The source is a single retrospective case, not comparative evidence that relationship banking, diversification, or a specific control would have prevented the fraud. It does not identify the attacker, compromised credential or authorization path, reconciliation cadence, insurance, account terms, or internal control design. Reported branch incentives are unverified second-hand testimony, and Chase ultimately recovered all stolen funds. The case supports lifecycle and monitoring principles but not a universal bank-selection rule or current legal, regulatory, or deposit-insurance guidance.

## What Changed
- Established treasury management as a startup operating discipline distinct from fundraising and general finance literacy.
- Added incomplete account migration and forgotten inbound payment routes as sources of residual financial risk.
- Added the tension between fraud lockdown and liquidity or account-closure needs.

## Related Concepts
- [[BusinessFinanceLiteracy]] - provides the practical financial understanding founders need before they can govern treasury choices.
- [[StartupFundingRound]] - creates cash inflows that can abruptly change the scale and risk of an existing banking setup.
- [[StartupRunway]] - treasury safeguards the liquid resources that determine how long the company can operate.
- [[OnePersonTeamRisk]] - founder-only knowledge and authority can make financial operations fragile as the company scales.
