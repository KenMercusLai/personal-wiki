---
title: "No, you don't need ML/AI. You need SQL"
type: source
tags: [sql, machine-learning, e-commerce, customer-retention, automation]
date: 2018-07-01
source_file: "/mnt/ken_personal_wiki/Articles/No, you don't need ML-AI. You need SQL.md"
---

## Summary
[[CelestineOmin]] argues from his work at [[Konga]] that small e-commerce businesses should exhaust explicit database queries and scheduled workflows before adopting machine learning for routine segmentation and intervention. The examples behind [[SQLFirstBusinessAutomation]] include customer rewards, win-back campaigns, purchase-based newsletters, abandoned-cart reminders, payment-on-delivery controls, delivery-delay notices, and simple payment-attempt flags. The reported outcomes are useful hypotheses rather than established effects because the article supplies no cohorts, denominators, experimental design, costs, or independent verification.

## Key Claims
- SQL queries can turn existing order, basket, cart, payment-attempt, and delivery-state data into actionable customer or operations lists without a trained model.
- Deterministic rules are especially plausible when the business condition and intervention are already legible: reward the week's largest basket, contact customers inactive for three months, remind carts untouched for 48 hours, or notify orders outside a seven-day service window.
- Query output becomes an operating system only when paired with delivery and scheduling mechanisms such as Bash, cron, email, SMS, coupons, and human follow-up.
- The author reports that customer-of-the-week rewards produced repeat purchases among 99% of recipients, win-back campaigns converted more than 50%, and purchase-informed newsletters opened at roughly 25-30% versus a claimed 7-10% norm.
- Simple count- or threshold-based rules can provide an initial control for repeated payment-on-delivery cancellations or several failed cards, while machine learning may become justified for larger or more complex cases.

## Key Quotes
> "But if you're running a small online store with between 1,000 - 10,000 customers, then you can still very much live on SQL." - the article's stated scope boundary.

## Connections
- [[CelestineOmin]] - author and practitioner recounting the e-commerce examples.
- [[Konga]] - former workplace explicitly identified in the customer-of-the-week example.
- [[SQLFirstBusinessAutomation]] - central pattern of implementing legible business rules with queries and scheduled actions before predictive modeling.
- [[GrowthEngineering]] - the campaigns join segmentation, messaging, instrumentation, and customer behavior around retention outcomes.
- [[CustomerLifetimeValue]] - retention and repeat purchase are the business outcomes the proposed interventions seek to improve.
- [[NoCodeWorkflowAutomation]] - adjacent trigger-condition-action model, implemented here with database queries and scripts rather than a no-code interface.

## Contradictions
- The title and much of the rhetoric contrast SQL with ML/AI, but the closing says ML/AI has a place and narrows the recommendation to small stores. SQL retrieves or transforms data; Bash, cron, messaging systems, coupons, and human operations actually execute most interventions.
- The outcome figures are first-person retrospective claims without sample sizes, time windows, baselines, control groups, attribution methods, revenue, margin, unsubscribe, deliverability, or long-term retention data. They do not establish that the workflows outperformed advertising or caused the reported behavior.
- The illustrative SQL is pseudocode rather than runnable, schema-aware queries. Production use would also require data-quality checks, eligibility rules, exclusions, idempotency, monitoring, failure recovery, and treatment of returns, fraud, inventory, margin, and duplicate identities.
- Purchase-based targeting and behavioral intervention create privacy, consent, fairness, frequency, and security obligations that the article does not address. Hard thresholds for cancellations or failed cards can misclassify legitimate customers and should not become unreviewed punitive decisions.
- The source contains no effective image references, so no visual evidence or asset manifest was required.
