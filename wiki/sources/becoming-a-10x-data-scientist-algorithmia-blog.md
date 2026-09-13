---
title: "Becoming a 10x Data Scientist"
type: source
tags: [data-science, software-engineering, productivity]
date: 2017-08-21
source_file: /mnt/ken_personal_wiki/Articles/Becoming a 10x Data Scientist - Algorithmia Blog.md
---

## Summary
[[Algorithmia]] argues that data scientists can become more effective by borrowing engineering habits from high-performing developers. The article emphasizes business context, data provenance, clear code, small functions, documentation, exception handling, unit tests, version control, appropriate tools, model deployment, and debugging as the practical substance behind the "10x" framing.

## Key Claims
- [[IndustryDataScience]] requires understanding business goals, signoff paths, stakeholders, data provenance, quality control, gaps, and alternative data sources before modeling begins.
- [[DataScienceEngineeringPractice]] is the article's central prescription: data scientists should write clear, consistently styled, well-named, testable, documented, version-controlled code rather than clever notebooks or one-off scripts.
- Testing should extend beyond model validation into data queries, cleaning, transformation, and other pipeline code to reduce garbage-in-garbage-out failures.
- Tool choice is part of productivity: use libraries, APIs, pretrained models, centralized automation, and deployment platforms when they fit the job better than custom work.
- Debugging is the recurring practical skill behind the article's 10x framing, supported by exception handling, IDE debuggers, talking through code, and reading library source when errors arise.
- The 10x-developer evidence is treated as debated background; the article focuses on improvable behaviors rather than proving literal 10x productivity.

## Key Quotes
> "clarity or clearness beats cleverness" - code-design maxim used to argue against overly terse data-science code.

> "Garbage In, Garbage out" - warning attached to untested queries, cleaning, and transformation code.

## Connections
- [[Algorithmia]] - publisher and company context for the article.
- [[IndustryDataScience]] - the article extends company data-science practice from business framing into production-minded engineering habits.
- [[DataScienceEngineeringPractice]] - main concept captured from the article's developer-practice recommendations.
- [[SoftwareVerification]] - testing data acquisition and transformation code is presented as a quality gate before production.
- [[DeveloperExperience]] - clear naming, consistent style, useful errors, and documentation make code easier for teammates and future selves to use.
- [[DeploymentAutomation]] - centralized automation and model deployment make data products easier to debug, share, and operate.
- [[Ansible]] - named as one example of centralized automation tooling that can replace hard-to-debug scattered scripts and cron jobs.

## Contradictions
- No direct contradictions found. The source qualifies rather than contradicts existing wiki material: it accepts that the literal 10x-developer claim is debated while still treating developer practices as transferable to data-science work.
