---
title: "Adapting Network Design to Support Automation"
type: source
tags: [networking, automation, infrastructure]
date: 2020-06-24
source_file: /mnt/ken_personal_wiki/Articles/Adapting Network Design to Support Automation « ipSpace.net blog.md
---

## Summary
[[IvanPepelnjak]] argues that almost any network can be automated in principle, but organically grown, snowflake designs can make automation impractically expensive. The article frames [[NetworkAutomation]] as one design requirement among others, not a reason to flatten or simplify a network at the expense of security, convergence, jitter, or other operational properties.

## Key Claims
- [[NetworkAutomation]] does not require an idealized topology; even messy networks can be automated if their operations can be described precisely enough.
- Bad or overly bespoke design raises the cost of describing, implementing, and maintaining automation, sometimes beyond practical value.
- Network design should be simplified and made easier to automate when possible, but automation should not override other required network properties.
- Automation code must stay synchronized with network design changes because stale automation can become as dangerous as stale documentation.
- Engineers should expect skill portfolios to change as technologies commoditize, but complex automated networks still need people who understand failure modes, protocols, and troubleshooting.

## Key Quotes
> "Support for network automation is just another business requirement" - summary of the article's design stance.

## Connections
- [[IvanPepelnjak]] - author of the ipSpace.net article.
- [[IpSpace]] - publication and training context for the article.
- [[NetworkAutomation]] - central concept: automation as a network-design requirement.
- [[InfrastructureAsCode]] - adjacent automation discipline for describing infrastructure through code.
- [[ChangeSafety]] - automation code and topology changes must stay aligned to avoid change-induced failures.
- [[CareerPlanning]] - the source treats automation-era skill change as a recurring career adaptation problem.

## Contradictions
- None identified.
