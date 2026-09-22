---
title: "Builder-User Fluency Gap"
type: concept
tags: [ux, software-development, user-support]
sources:
  - are-users-trying-to-make-developers-angry-exception-not-found
  - you-are-not-your-customer-greylock-perspectives
last_updated: 2026-09-22
knowledge_schema: synthesis-v1
---

## Definition
[[BuilderUserFluencyGap]] is the difference between what a product builder finds obvious because they know the system intimately and what a user can infer from the interface, instructions, and their own task context.

## Current Synthesis
The Exception Not Found essay shows this gap in everyday support work. The developer knows which text to read, which button to click, which link reveals information, and which inputs a search box accepts, so user mistakes look absurd from the builder side. Users, however, approach the same interface through incomplete context and task pressure: a link's placement may imply the wrong destination, a missing set of separate fields may imply a removed feature, and instructions may not stand out at the point of need. Greylock extends the same mechanism from support into product strategy: employees and early adopters become so fluent that their shared enthusiasm can validate niche features while hiding the needs of prospective users. The gap is therefore both an empathy problem and a sampling problem, closed through explanation, interface evidence, and deliberate testing with people who lack insider knowledge.

## Key Claims
- Builders can mistake their own system fluency for universal obviousness.
- Users infer possible actions from visible cues, placement, labels, and prior software experience.
- Support requests can reveal mismatches between the product model in the builder's head and the model users construct.
- Explanation without judgment can turn confusion into learning and preserve trust.
- Repeated "simple" mistakes may indicate product affordance or hierarchy problems, not only inattentive users.
- Early adopters can cross from useful novice evidence into expert behavior, so teams should not assume their preferences still predict new-user adoption.
- Employee agreement is weak validation when the team shares the same accumulated product and domain knowledge.

## Evidence
- Obviousness mismatch: [[are-users-trying-to-make-developers-angry-exception-not-found]] says actions obvious to the developer were foreign to users.
- Link interpretation: [[are-users-trying-to-make-developers-angry-exception-not-found]] describes a user who did not click a link because its position suggested it would take them to a different tool.
- Search-field inference: [[are-users-trying-to-make-developers-angry-exception-not-found]] describes a user assuming address search was removed because city, state, and zip did not have separate labeled boxes.
- Grateful learning: [[are-users-trying-to-make-developers-angry-exception-not-found]] reports users thanking the developer when the tool was explained without judgment.
- Expertise drift: [[you-are-not-your-customer-greylock-perspectives]] argues that employees and early adopters cease to represent newcomers after accumulating extensive product knowledge.
- Strategic consequence: [[you-are-not-your-customer-greylock-perspectives]] says expert-oriented feature requests can consume experiments and add complexity without improving growth.

## Counterevidence & Qualifications
The sources do not claim all confusion is a product defect. Users can skip instructions, enter unexpected data, or need training, and some workflows may be intrinsically complex. Nor does fluency make employee or power-user feedback worthless: expert users can identify depth, reliability, and workflow needs that newcomers cannot. The concept is therefore a diagnostic caution about matching evidence to the question, not a rule to ignore experienced users.

## What Changed
- Extended the fluency gap from individual support misunderstandings to roadmap sampling and growth decisions.
- Distinguished useful expert feedback from evidence about newcomer comprehension and adoption.

## Related Concepts
- [[HanlonsRazor]] - the fluency gap supplies a non-malicious explanation for frustrating user behavior.
- [[InformationHierarchy]] - visible ordering and placement shape what users believe is possible.
- [[CognitiveLoadInUXResearch]] - hidden interpretation work can produce mistakes users cannot easily explain.
- [[TechnicalAccessibility]] - both concepts warn creators not to assume an artifact explains itself.
- [[CustomerLedProductDevelopment]] - support encounters can expose real user models and product gaps.
- [[CognitiveOverheadInProductDesign]] - insider fluency can conceal comprehension costs imposed on newcomers.
- [[ProductUserSegmentation]] - fluency level is one basis for separating user evidence and product needs.
