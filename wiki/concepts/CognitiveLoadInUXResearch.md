---
title: "Cognitive Load in UX Research"
type: concept
tags: [ux-research, cognition]
sources:
  - yong-yan-bao-gao-zhong-de-xin-xi-she-ji-yao-su-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[CognitiveLoadInUXResearch]] is the mental work users must perform to understand interface state, infer rules, remember information, recover from errors, and decide what action is possible.

## Current Synthesis
In RORIRI's article, cognitive load is the hidden middle layer that connects interface design to subjective feeling and observed behavior. Poor feedback, unclear language, inconsistent interactions, weak error recovery, and missing help force users to infer what the system should have made visible. Because users may not notice the cognitive task they failed, their subjective ratings can stay calm while their behavior shows repeated mistakes.

## Key Claims
- Cognitive load can be invisible in behavior logs because the failed task happens in the user's understanding rather than as a discrete action.
- Interface design elements such as feedback, consistency, wording, error recovery, and help shape cognitive load.
- High cognitive load can explain low subjective difficulty paired with high objective error.
- Expert walkthrough methods can expose cognitive prerequisites that users themselves may not report.
- Cognitive load should be treated as one possible explanatory layer, not as a fixed report template.

## Evidence
- Hidden cognition: [[yong-yan-bao-gao-zhong-de-xin-xi-she-ji-yao-su-luo-li-li-de-shu-ju-zhong-xin]] says the "user did not identify data type" failure cannot be directly logged because it happens in the mind.
- Design-to-load link: [[yong-yan-bao-gao-zhong-de-xin-xi-she-ji-yao-su-luo-li-li-de-shu-ju-zhong-xin]] connects weak diagnosis, recovery, and help to users needing to infer why a drag operation failed.
- Feeling-to-behavior conflict: [[yong-yan-bao-gao-zhong-de-xin-xi-she-ji-yao-su-luo-li-li-de-shu-ju-zhong-xin]] explains that users may report ease because they do not realize they missed a prerequisite while behavior still records repeated errors.
- Expert inference: [[yong-yan-bao-gao-zhong-de-xin-xi-she-ji-yao-su-luo-li-li-de-shu-ju-zhong-xin]] uses PURE to model what users must understand, infer, and remember at each task step.

## Counterevidence & Qualifications
The source treats cognitive load as an explanatory layer in a specific Jamovi study. It does not measure cognitive load directly through physiological signals or validated cognitive-load scales, and it leaves room for other report structures when the research question or methods differ.

## What Changed
- Created this concept to represent hidden cognitive burden as the mediator between interface design, subjective experience, and observed user behavior.

## Related Concepts
- [[UXResearchInformationDesign]] - cognitive load can organize otherwise conflicting report evidence.
- [[MixedMethodUXResearch]] - observation, questionnaire, PURE, and heuristic data each expose different parts of the cognitive-load chain.
- [[HeuristicEvaluation]] - design-principle violations can be upstream causes of cognitive load.
- [[Jamovi]] - the case where a hidden data-type recognition failure produced repeated visible drag errors.
