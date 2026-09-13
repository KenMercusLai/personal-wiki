---
title: "Simple Ain't Easy, but Hard Ain't Simple: Leaving Clojure for Ruby"
type: source
tags: [clojure, ruby, programming-languages, developer-experience]
date: 2026-03-28
source_file: /mnt/ken_personal_wiki/Articles/Appcanary - Simple Ain't Easy, but Hard Ain't Simple- Leaving Clojure for Ruby.md
---

## Summary
[[PhillipMendoncaVieira]] reflects on why [[Appcanary]] built its first version in [[Clojure]] and then returned to [[Ruby]]. The essay argues that early startups should prefer familiar tools, avoid distributed systems as long as possible, and treat developer happiness as a real design concern rather than a shallow preference for ease. It critiques a common use of [[SimpleMadeEasy]] rhetoric when "simple is not easy" becomes permission to ignore poor affordances, errors, and onboarding in [[DeveloperTooling]].

## Key Claims
- Time-pressed startups should bias toward tools the team already knows because the business problem is hard enough without adding a major tooling-learning curve.
- Small teams should avoid distributed systems for as long as possible because deployment and coordination complexity must match team size and organizational capacity.
- Clojure's ecosystem felt powerful but user-hostile in this context because its tooling assumed high tolerance for digging through errors, code, idioms, and runtime quirks.
- The essay accepts the distinction between conceptual simplicity and ease, but argues that treating simplicity as supreme can make teams discount developer experience.
- Ruby's enduring contribution is its explicit design value of making programming fun and making programmers happy, even though Ruby tooling has technical flaws.
- Critiques of programming languages can be received as critiques of community identity, so authors need to establish charitable intent when discussing tool tradeoffs.

## Key Quotes
> "If you're starting a project where you're really pressed for time, you should be biased towards tools you know really well." - startup tool-choice advice.

> "Avoid building a distributed system for as long as you can." - architecture advice for small teams.

> "All programming languages should strive to be fun and make programmers happy." - language-design value claim.

## Connections
- [[Appcanary]] - startup whose first Clojure implementation was discarded.
- [[PhillipMendoncaVieira]] - author reflecting on the RubyConf talk and later Clojure-community response.
- [[Clojure]] - language and community whose tooling and "simple versus easy" rhetoric are criticized from a context-specific user perspective.
- [[Ruby]] - language the team returned to because it was familiar and valued programmer happiness.
- [[SimpleMadeEasy]] - Rich Hickey idea the essay treats as insightful but often misused against ease of use.
- [[DeveloperExperience]] - central criterion the essay says programming tools should actively optimize.
- [[ToolFamiliarity]] - startup tool-choice principle for time-pressed teams.
- [[DistributedSystemRestraint]] - architecture principle of delaying distributed systems until team capacity justifies them.
- [[TechnologyStackComplexity]] - broader stack-cost frame reinforced by the warning against tool learning and premature distribution.
- [[MicroserviceOperationalOverhead]] - adjacent architecture warning that service boundaries should reflect team coordination capacity.

## Contradictions
- No direct contradictions found. The source qualifies simplicity-oriented architecture and language-design arguments by saying conceptual simplicity does not excuse unfriendly tools, but it also acknowledges that unfamiliarity and context shaped Appcanary's Clojure experience.
