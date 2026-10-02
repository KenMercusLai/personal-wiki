---
title: "Stop Overengineering"
type: source
tags: [engineering, software-development, simplicity, product-development]
date: 2023-07-14
source_file: /mnt/ken_personal_wiki/Articles/Stop Overengineering.md
---

## Summary
This personal appeal argues that [[Overengineering]] replaces outcome-focused work with speculative constraints, extra abstraction, and precise bets about an uncertain future. It connects unnecessary complexity to coupling, maintenance burden, missed deadlines, and slower learning toward [[ProductMarketFit]], while offering no cases or measurements that establish when anticipatory engineering becomes excessive.

## Key Claims
- Overengineering diverts effort from real results toward constraints a team already knows how to solve.
- Extra moving parts, specification, and indirection can increase coupling and fragility rather than create useful optionality.
- Every added mechanism expands the knowledge-transfer, bug, and maintenance burden.
- Engineering an unlikely edge case should be evaluated through frequency, failure impact, resource cost, and discounted future value.
- Speculative design is a precise bet on future requirements and should be discounted as uncertainty increases.
- Overengineering can delay delivery and customer learning, working against product-market fit.

## Key Quotes
> "Generalizing abstractions rarely creates the optionality that we convince ourselves it does."

> "The more assumptions you make about the future, the more it should be discounted."

## Connections
- [[Overengineering]] - the source's central critique of complexity unsupported by present requirements or proportional risk.
- [[SoftwareAbstraction]] - generalization can add indirection and coupling when it precedes demonstrated reuse or change pressure.
- [[TechnicalDebt]] - unnecessary machinery can create future maintenance cost even when it was initially intended to prevent debt.
- [[UnknownUnknowns]] - solving imagined familiar constraints can displace experiments that expose unrecognized product or system risks.
- [[ProductMarketFit]] - delayed delivery reduces the opportunity to learn whether customers value the product.
- [[InternalSoftwareQuality]] - the appeal creates a stopping-rule tension between sufficient maintainability and uneconomic polish.

## Contradictions
- The categorical claim that overengineering is never a reasonable allocation is definitionally circular and can obscure legitimate anticipatory work for safety, security, regulation, irreversible choices, or high-cost failure; this qualifies rather than directly contradicts [[InternalSoftwareQuality]] and [[TechnicalDebt]].
