---
title: "Understand, Design, Build"
type: concept
tags: [software-engineering, problem-solving, engineering-management]
sources:
  - understand-design-build-a-framework-for-problem-solving-lob-blog
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[UnderstandDesignBuild]] is a three-step problem-solving sequence - understand the business outcome, the current blocker, and the existing technical landscape; design competing approaches with their benefits, risks, and mitigations; then build - that treats problem definition and solution choice, not code production, as the core engineering work.

## Current Synthesis
The source presents the sequence as a correction to a common misconception among new software professionals: that becoming excellent at writing code makes someone an excellent engineer. The claim is that the job is to find and solve problems that move the business, and that when projects fail or take two to ten times longer than they should, it is almost always because the implementer built something that did not solve the problem or did not work well enough, so the work had to be discarded. Each step removes a different avoidable cost. Understanding removes the interrupts and wrong-product outcomes that come from [[PrematureImplementation]], and it also removes estimation error, because teams unfamiliar with existing code, infrastructure, and prior solutions estimate orders of magnitude away from reality. Design removes the default-to-first-idea failure by forcing explicit comparison through [[BenefitsRisksMitigations]]. Build then becomes the easy part, and attention can go to domain logic, edge cases, and tests instead of unresolved design questions.

Inside the wiki, the framework is the delivery-side sibling of [[EngineeringLedOrganizationDesign]]: both apply a define-understand-design-validate loop, one to software projects and one to teams. Its most distinctive application is mentoring. Checking in after each step gives a mentor x-ray vision into a less experienced engineer's reasoning, which makes blind spots, wrong directions, and rabbit holes visible early and cheap to correct.

## Key Claims
- Engineering work is problem-solving that moves the business; code production is necessary but not the point.
- Project failure and extreme schedule overruns usually come from building something that did not solve the problem or did not function well.
- Understanding has three parts: the desired business outcome, the current blocker, and what existing code or infrastructure helps or hinders change.
- Skipping the Understand step costs both interrupt time and a deliverable that misses the problem.
- Design means generating and comparing several approaches by benefits, risks, and mitigations instead of committing to the first idea.
- Build is cheap relative to the design decisions that precede it, so quality work on logic, edge cases, and tests depends on those decisions already being made.
- The framework doubles as mentoring and diagnostic tooling: step-by-step check-ins expose reasoning, and prolonged backtracking usually means the problem was not understood or the design was not finished.

## Evidence
- Problem-solving framing: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] says the job is to find and solve problems that move the business forward and that great code is a necessary but insufficient skill.
- Failure mechanism: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] attributes failure and 2x-10x overruns to diligently building something that did not solve the problem or did not function well, forcing the code to be thrown away.
- Understand questions: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] lists the business outcome wanted, what prevents it today, and what already exists in the codebase or infrastructure.
- Interrupt and wrong-solution costs: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] names frequent stops to ask others for information and building something that does not solve the problem as the consequences of implementing without understanding.
- Context caching: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] says design docs and kickoff meetings exist to push business understanding into everyone's head so fewer retrievals are needed.
- Technical landscape and estimation: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] says similar prior problems, reusable infrastructure, and existing constraints determine difficulty, and that estimates will be orders of magnitude off without that familiarity.
- Design comparison: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] argues that mature companies have fewer obvious solutions, that the first idea is unlikely to be the best, and that researching several options exposes the trade-offs.
- Design forms: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] lists whiteboarding, a design doc or one-pager, and a full technical design review as the ways the Design step happens.
- Build as the easy step: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] compares it to writing an essay after the outline and says it is faster, more educational, and more fun when design decisions are already made.
- Application and mentoring: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] names mentoring interns and entry-level engineers, open-ended problems, and project diagnosis as the main uses, and says check-ins after each step reveal reasoning and prevent rabbit holes.

## Counterevidence & Qualifications
The page rests on one company's coaching write-up. The reported outcomes - less backtracking, fewer interruptions, simpler projects, less toil, higher success rates - are Lob's own framing rather than measured comparisons. The framework front-loads analysis, so it can become an argument for extended design when the cheapest learning would come from shipping something small; the wiki's [[ContinuousDelivery]] and prolific-build material argue for early deployed feedback instead. The source also does not say how to recognize that the business outcome itself is wrong, how much understanding is enough, how the sequence changes for easily reversible changes, or how it interacts with deadlines that make another design iteration impossible. Its claim that senior engineers converge on the framework intuitively is an observation about practice, not evidence that teaching the steps causes better results.

## What Changed
- Created the concept from Lob's 2019 engineering-blog post.

## Related Concepts
- [[PrematureImplementation]] - the failure mode the Understand step exists to prevent.
- [[BenefitsRisksMitigations]] - the design-review method the framework uses to compare approaches.
- [[EngineeringLedOrganizationDesign]] - the same design loop applied to teams rather than to software projects.
- [[StartupHypothesisTesting]] - both replace default building with explicit, inspectable reasoning before commitment.
- [[ContinuousDelivery]] - tension: it prefers deploying early for real feedback where the framework prefers understanding first.
- [[AttentionManagement]] - caching context locally is how the framework protects colleagues from interrupt cost.
- [[JuniorEngineerLearning]] - check-ins after each step turn the framework into apprenticeship feedback.
- [[StrategicWriting]] - design docs and one-pagers are the written artifacts that carry this reasoning.
