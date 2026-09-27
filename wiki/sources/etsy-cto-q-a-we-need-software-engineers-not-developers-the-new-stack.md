---
title: "Etsy CTO Q&A: We Need Software Engineers, Not Developers"
type: source
tags: [etsy, devops, software-engineering, operations, machine-learning]
date: 2016-03-03
source_file: "/mnt/ken_personal_wiki/Articles/Etsy CTO Q-A- We Need Software Engineers, Not Developers - The New Stack.md"
---

## Summary
In this 2016 interview, [[JohnAllspaw]] describes [[Etsy]] as a deliberately straightforward but operationally demanding engineering environment: a small set of familiar technologies, explicit review of new-tool ownership costs, simple deployment, and engineer responsibility for production behavior. His distinction between developers and engineers is not about title or individual omniscience, but about multidisciplinary curiosity, shared operational understanding, and refusal to treat abstractions as permission to ignore failures. He also presents Etsy's long-tail search and recommendation work as useful machine learning while rejecting the idea that algorithms remove human judgment.

## Key Claims
- A small, well-understood technology set can concentrate engineering attention on product work, while each novel tool carries long-term learning, support, and operational costs.
- Architecture reviews can expose prior internal solutions and make the continuing ownership cost of a new technology explicit without eliminating product autonomy.
- Deployment should be simple and confidence-producing enough that a new engineer can reach production during the first day or week; otherwise deployment or onboarding is too difficult.
- Development cannot reproduce Etsy's full production-data diversity, so the company uses containers for development and a read-only proxy rather than trying to synthesize every listing, language, and currency combination.
- [[ProductionOwnership]] connects deploy authority with responsibility for monitoring, alerting, metrics, failure discovery, and recovery rather than allowing engineers to disown production behavior behind abstractions.
- [[SoftwareEngineering]] is multidisciplinary boundary work: engineers need not know every specialty, but should seek experts and continually extend their understanding of applications, databases, networks, and infrastructure.
- Etsy uses machine learning and heuristics to infer taste across a long tail of unique listings, while taking a human-centered view that software-encoded decisions still contain judgment and should be studied through successes as well as failures.

## Key Quotes
> “You build it, you own it.” — on responsibility for code after production deployment

> “Introducing something new and different can bear a huge long-term cost to the organization.” — on technology proliferation

## Connections
- [[JohnAllspaw]] - Etsy CTO interviewed about architecture, hiring, production responsibility, and machine learning.
- [[Etsy]] - marketplace and engineering organization described in the interview.
- [[ProductionOwnership]] - deploy authority creates responsibility for operation, observability, and recovery.
- [[SoftwareEngineering]] - framed as multidisciplinary curiosity and shared understanding rather than code production alone.
- [[DevOpsCulture]] - Etsy's deployment and operations model joins development authority with production accountability.
- [[BoringTechnology]] - a small set of well-known tools protects product attention and limits ownership cost.
- [[ServiceObservability]] - monitoring, alerting, and metrics become immediate concerns when engineers deploy their own code.
- [[MachineLearning]] - used for search and long-tail recommendation while remaining subject to human judgment.

## Contradictions
- The title's opposition between “engineers” and “developers” is rhetorical rather than a stable occupational taxonomy. The interview defines the desired difference through operational scope and learning behavior, not through credentials or a universally accepted title boundary.
- The article reports Etsy's 2016 practices and Allspaw's judgments without comparative delivery, incident, hiring, or recommendation-quality data. It does not establish that the same stack limits or ownership model fit every team, risk level, or regulatory context.
- Simplifying deployment does not make production change inherently safe. The source mentions confidence and observability but does not specify staged rollout, automated verification, access controls, incident load, or safeguards against individual blame.

## Image Notes
All seven embedded images were opened. Six are non-evidentiary photographs of Etsy's Brooklyn office, its artwork, or John Allspaw, and one is a The New Stack sponsor logo; none adds architecture, workflow, measurement, interface state, or factual evidence beyond the prose, so none was retained.
