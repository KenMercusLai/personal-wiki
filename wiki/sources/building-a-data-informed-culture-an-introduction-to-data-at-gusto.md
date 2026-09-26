---
title: "Building a Data-Informed Culture: An Introduction to Data at Gusto"
type: source
tags: [data-culture, data-engineering, analytics, data-warehouse]
date: 2016-12-13
source_file: "/mnt/ken_personal_wiki/Articles/Building a Data-Informed Culture- An Introduction to Data at Gusto.md"
---

## Summary
[[Gusto]] describes becoming data-informed as combining evidence with values, principles, and experience rather than allowing metrics to replace judgment. The company chose a foundation-first path: centralize major operational, event, and vendor data in [[AmazonRedshift]], build governed warehouse layers, orchestrate transformation and quality checks with [[ApacheAirflow]], and expose analysis through [[Looker]] before expanding predictive modeling. The referenced architecture diagram could not be inspected because its local file is missing, so the architecture recorded here is limited to the article's prose.

## Key Claims
- A [[DataInformedCulture]] uses data within a broader decision process that still includes organizational values, principles, and experience.
- Gusto prioritized reliable shared infrastructure over early data-science wins so future analysts and scientists could spend more time on models and insight generation.
- The warehouse used raw source schemas at the bottom, denormalized BI tables in the middle, and team-specific joined or aggregated views at the top.
- Sensitive raw schemas and separated PII schemas had stricter access controls; self-service did not mean unrestricted access to personal data.
- Engineers owned infrastructure and tools, data scientists built predictive and statistical systems, and analysts connected current insights to operational teams.
- Analysts could write Airflow SQL transformations and publish new BI tables into Looker, reducing engineering handoffs while the company's scale still made this operating model practical.
- Gusto planned to apply predictive models to fraud prevention, growth targeting, and customer-facing payroll and benefits insight.

## Key Quotes
> "we apply our values, principles, and experiences when we gather, analyze, and incorporate data into our decision-making" - Gusto's definition of data-informed culture.

> "lay the right foundation first" - rationale for building reliable warehouse infrastructure before pursuing more immediate data-science wins.

## Connections
- [[Gusto]] - company describing its 2015-2016 data-team and platform development.
- [[DataInformedCulture]] - decision model and organizational capability at the center of the source.
- [[LayeredDataWarehouse]] - raw, BI, and team-view structure used to balance fidelity, usability, governance, and reuse.
- [[DataScienceEngineeringPractice]] - infrastructure, testing, role boundaries, and analyst-authored transformations make analytical work more reproducible and usable.
- [[ApacheAirflow]] - orchestration layer for ingestion, SQL transformations, testing, and quality alerts.
- [[AmazonRedshift]] - central analytical warehouse receiving production replicas and transformed data.
- [[Looker]] - exploration and dashboard interface exposed to teams across the company.

## Contradictions
- No direct contradiction found. The source complements data-driven operations and event-pipeline material by emphasizing that shared infrastructure, governance, role design, and human judgment precede or constrain analysis.
