---
title: "Khan Academy"
type: entity
tags: [education, online-learning, platform]
sources:
  - big-data-mooc-research-breakthrough-learning-activities-lead-to-achievement-edtech-researcher-education-week
  - real-world-engineering-challenges-8-breaking-up-a-monolith
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[KhanAcademy]] is a nonprofit online-learning platform represented through both learner-analytics research and a multi-year production architecture migration.

## Current Profile
One source discusses an SRI International study of Khan Academy use in 20 schools from 2011 to 2013, using the platform as an example of rich learner behavior reduced to a simple relationship between minutes logged in and math scores. A later engineering case describes Khan Academy's 2019-2023 migration of roughly one million lines of Python 2 into more than 40 mostly Go services behind federated GraphQL. The program reached an identity-preserving MVE after two years and completed after another 18 months through field-level routing, behavioral comparison, explicit data ownership, and deadline-driven coordination.

## Key Characteristics
- Provides detailed learner activity logs in school-based online-learning use.
- Appears as an example of big education data compressed into a small effort metric.
- Supplies a correlation case where more platform time is associated with stronger math outcomes without establishing causality.
- Operated a large Python 2 monolith before moving production behavior into more than 40 mostly Go services.
- Used GraphQL federation, incremental traffic transfer, and one-writer data ownership to manage coexistence.
- Sustained a 3.5-year migration whose technical completion carried substantial feature, staffing, and organizational opportunity costs.

## Evidence
- Platform logs: [[big-data-mooc-research-breakthrough-learning-activities-lead-to-achievement-edtech-researcher-education-week]] says Khan Academy records behavioral activity such as video time and problem attempts.
- Study setting: [[big-data-mooc-research-breakthrough-learning-activities-lead-to-achievement-edtech-researcher-education-week]] describes SRI's 20-school implementation study.
- Summary metric: [[big-data-mooc-research-breakthrough-learning-activities-lead-to-achievement-edtech-researcher-education-week]] notes that the log analysis centered on minutes logged in.
- Migration scale: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] reports roughly one million Python lines, more than 40 services, 3.5 years, and around 100 participating engineers at peak.
- Rollout method: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] documents field-level shadowing, comparison, canarying, cutover, fallback, and deletion.
- Architecture and ownership: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] depicts a federated GraphQL gateway and reports a rule that only one service could write a given piece of data.
- Organizational cost: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] reports long periods with little feature work, cross-functional frustration, and possible product and design attrition.

## Qualifications
The analytics article reports Khan Academy through Reich's critique rather than as a complete evaluation of the platform or SRI study. The migration article is a second-party practitioner case based largely on interviews and Khan Academy engineering posts; it offers no independent before-and-after reliability, delivery-rate, attrition, or total-cost analysis. Its claimed Go savings do not settle whether changing language repaid the learning cost.

## What Changed
- Created the entity page for Khan Academy as an online-learning analytics example.
- Expanded the profile with the 2019-2023 monolith migration, its safety mechanisms, and its organizational tradeoffs.

## Relationships
- [[MOOCLearningAnalytics]] - Khan Academy provides one cited learner-log case.
- [[BehavioralData]] - Khan Academy's platform use generates learner action traces.
- [[JustinReich]] - Reich critiques how the platform's data were summarized.
- [[GergelyOrosz]] - reported the migration through company material and leadership interviews.
- [[IncrementalMonolithMigration]] - Khan Academy supplies the wiki's field-level production case.
- [[MinimumViableExperience]] - Khan Academy used this scope boundary for the migration's first phase.
- [[GraphQL]] - federation composed fields across the monolith and successor services.
