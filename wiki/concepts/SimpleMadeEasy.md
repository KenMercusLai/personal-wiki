---
title: "Simple Made Easy"
type: concept
tags: [software-design, programming-languages, developer-experience]
sources:
  - appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby
  - simplify-move-code-into-database-functions
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[SimpleMadeEasy]] is the software-design distinction, associated here with Rich Hickey's Clojure talk, between conceptual simplicity and ease of use.

## Current Synthesis
The sources agree that conceptual simplicity and immediate ease are different, then use that distinction in tension. [[DerekSivers]] treats a single database-owned rule set as simpler than coupling database behavior to multiple language-specific class layers, even though PL/pgSQL is harder to use. The Appcanary essay accepts the distinction but warns that elevating simplicity above usability can excuse poor affordances, errors, and onboarding. The combined judgment is that fewer interwoven concepts can improve architecture, but the result still has to be evaluated through the interfaces, skills, and operational burdens people actually face.

## Key Claims
- Conceptual simplicity and immediate ease are different qualities.
- Familiarity can masquerade as ease even when a tool or idea is complex.
- Some simple ideas are hard because they are unfamiliar or require deeper thought.
- Separating a durable rule set from replaceable application layers can reduce interweaving even when the chosen implementation is less pleasant to use.
- The distinction becomes harmful when it excuses bad affordances, errors, or onboarding.
- Developer-facing software still needs usability, accessibility, and kindness even when it is conceptually elegant.

## Evidence
- Distinction: [[appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby]] summarizes the thesis that the conceptually simplest solution is not automatically simple to use.
- Familiarity caveat: [[appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby]] says ease often means familiarity.
- Critique: [[appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby]] argues the idea can become an excuse for making software that is hard to use.
- Developer interface: [[appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby]] says dismissing ease makes it harder to distinguish arbitrary barriers from necessary difficulty.
- Architectural application: [[simplify-move-code-into-database-functions]] calls database-owned intelligence simple because one rule set is not tied across the database and multiple application-language layers.
- Accepted difficulty: [[simplify-move-code-into-database-functions]] describes PL/pgSQL as unattractive but judges the centralized architecture worth that usability cost.

## Counterevidence & Qualifications
Neither source proves that its preferred design produces better outcomes. Appcanary does not reject the distinction itself; it targets its use to discount developer experience. Sivers's architecture may reduce duplicated rule sets, but it also concentrates coupling in PostgreSQL, database permissions, stored-code deployment, and specialized skills, while its snippets omit important production controls. Conceptual ingredient count is therefore one design criterion rather than a substitute for usability, correctness, portability, or operations.

## What Changed
- Added Sivers's affirmative use of the distinction to justify database-owned application logic.
- Reframed simplicity as one architectural criterion that must remain accountable to usability and operational cost.

## Related Concepts
- [[DeveloperExperience]] - the essay argues simplicity must not erase tool usability.
- [[DeveloperTooling]] - developer tools expose the tension between conceptual design and interface quality.
- [[ToolFamiliarity]] - familiarity can be mistaken for ease.
- [[Clojure]] - community context where the idea appears in the source.
- [[TechnologyStackComplexity]] - conceptual simplicity can reduce complexity but may still be hard to use.
- [[DatabaseCentricApplicationLogic]] - applies the distinction by separating database-owned rules from replaceable application adapters.
- [[PostgreSQL]] - the concrete platform on which Sivers accepts implementation difficulty in exchange for centralized rules.
