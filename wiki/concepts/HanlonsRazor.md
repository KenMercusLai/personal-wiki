---
title: "Hanlon's Razor"
type: concept
tags: [judgment, user-support, empathy]
sources:
  - are-users-trying-to-make-developers-angry-exception-not-found
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[HanlonsRazor]] is the judgment heuristic of explaining frustrating behavior through ignorance, missing context, confusion, or ordinary error before attributing it to malice.

## Current Synthesis
The Exception Not Found source applies [[HanlonsRazor]] to software support. Developers may receive angry or confused user reports and infer that users are lazy, hostile, or trying to break the application, but the article argues that this inference often reflects developer ego and fluency rather than user intent. In the source's examples, users misunderstood links, search fields, instructions, and possible actions because they did not share the builder's internal model of the tool. The practical stance is to begin with patient explanation, then treat repeated confusion as information about the user's context and the product's affordances.

## Key Claims
- User confusion should be interpreted through missing knowledge before malice.
- Developer frustration can be amplified by ego and by overconfidence that the product is obvious.
- Support interactions often reveal that users want to learn, not avoid responsibility.
- Applying the heuristic changes the developer's role from offended expert to knowledge translator.
- The heuristic does not deny user error; it changes the default explanation for why the error occurred.

## Evidence
- Explicit principle: [[are-users-trying-to-make-developers-angry-exception-not-found]] cites Hanlon's Razor as the right frame for user support.
- User intent: [[are-users-trying-to-make-developers-angry-exception-not-found]] says the users were trying to learn how to use the tool to do their jobs.
- Developer ego: [[are-users-trying-to-make-developers-angry-exception-not-found]] says the author's inflated ego made user questions feel like provocation.
- Knowledge translation: [[are-users-trying-to-make-developers-angry-exception-not-found]] concludes that the knowledgeable developer has a responsibility to move that knowledge where it is needed.

## Counterevidence & Qualifications
The source is a reflective essay rather than a controlled study, and it focuses on ordinary workplace users of an internal or work tool. The heuristic should not erase real abuse, bad-faith behavior, accessibility failures, or organizational incentives that make support interactions adversarial. It is best used as a first interpretive posture, not as proof that all user complaints are innocent or that product design is irrelevant.

## What Changed
- Created the concept from the article's explicit use of Hanlon's Razor as a software-support heuristic.

## Related Concepts
- [[BuilderUserFluencyGap]] - missing shared fluency is the article's main non-malicious explanation for frustrating user behavior.
- [[CognitiveLoadInUXResearch]] - confusion can arise from hidden mental work required by an interface.
- [[CustomerLedProductDevelopment]] - patient support can turn user confusion into product evidence.
- [[InformationHierarchy]] - unclear visibility and ordering can make obvious features seem absent.
