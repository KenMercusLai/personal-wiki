---
title: "Understand, Design, Build: A Framework for Problem-Solving"
type: source
tags: [software-engineering, problem-solving, engineering-management, mentoring]
date: 2019-02-25
source_file: "/mnt/ken_personal_wiki/Articles/Understand, Design, Build- A Framework for Problem-Solving - Lob Blog.md"
---

## Summary
The [[Lob]] engineering blog argues that the job of a software professional is to find and solve problems that move the business forward, and that writing great code is necessary but insufficient for that job. The article offers [[UnderstandDesignBuild]] as a three-step coaching framework: Understand the business outcome, what blocks it today, and what already exists in the codebase or infrastructure; Design several candidate approaches and weigh their benefits, risks, and mitigations; then Build once the hard decisions are made. The author reports that projects led by engineers who follow the framework involve less backtracking, are interrupted less often, stay simpler, carry less toil and operational burden, and are more likely to succeed, and recommends it for mentoring new engineers, for open-ended problems, and for diagnosing projects that are going badly.

## Key Claims
- The core engineering job is finding and solving business problems; coding skill is necessary but not the point of the work.
- Most software projects fail or take 2x to 10x too long because the implementer diligently built something that either did not solve the problem or did not function well, and the code had to be discarded.
- Understanding requires three answers: the business outcome wanted, what prevents it today, and what existing code or infrastructure helps or hinders change.
- Starting to implement without understanding the business problem produces two costs: frequent interrupts from people asking others for information, and a deliverable that does not solve the problem.
- Design docs and project kickoffs exist to cache understanding of the problem locally in everyone involved, so fewer retrievals and interrupts are needed later.
- Familiarity with the existing technical landscape determines both difficulty and estimation accuracy; without it, estimates are orders of magnitude off.
- As companies mature, fewer problems have obvious solutions, so the Design step means researching more than one approach and comparing benefits, risks, and mitigations rather than defaulting to the first idea.
- Design work can take the form of a whiteboarding exercise, a design doc or one-pager, or a full technical design review.
- Writing code is the easiest part once the hard design decisions are made, which frees attention for domain logic, edge cases, and tests.
- The framework is most useful for mentoring interns and entry-level engineers, for problems the team does not yet know how to solve, and for diagnosing stalled or backtracking projects; senior engineers tend to converge on something like it intuitively, and sharing it decentralizes decision-making as teams scale.

## Key Quotes
> "Our job isn't to write code. Our job is to find and solve problems that move the business forward." - on why coding skill is necessary but insufficient.

> "Since there are usually several design options, it's not super likely that the first one that comes to mind is the best one." - on why design means comparing alternatives.

> "Writing code is the easiest part when we've already made the hard design decisions." - on why the front-loaded steps carry the difficulty.

## Connections
- [[Lob]] - publisher of the framework and the company that coaches engineers with it.
- [[UnderstandDesignBuild]] - the framework itself, and the source's central contribution.
- [[PrematureImplementation]] - the failure mode the Understand step exists to prevent.
- [[BenefitsRisksMitigations]] - the design-comparison frame the article recommends and attributes to First Round Review.
- [[AttentionManagement]] - interrupts during implementation change the context of more than the person asking.
- [[JuniorEngineerLearning]] - the framework is offered to intern mentors and first-time engineering managers as a way to see a mentee's reasoning.
- [[EngineeringLedOrganizationDesign]] - the same understand-design-build loop applied to building teams rather than software.
- [[StrategicWriting]] - design docs and one-pagers are the written artifacts that carry this reasoning.
- [[ContinuousDelivery]] - the wiki's early-deployment material pulls against this article's preference for up-front understanding.

## Contradictions
- Sits in tension with [[ContinuousDelivery]] and [[AgileSoftwareDevelopment]]: those sources push teams to deploy a first "hello world" and learn from real users, while this framework argues for more understanding and option comparison before committing. Both target rework, so the disagreement is about how much up-front analysis buys speed rather than about whether speed matters.
- Cites Nathan Yergler's essay on the cost of interrupts and a First Round Review matrix for benefits, risks, and mitigations; both are outside the wiki and are recorded here as influences rather than ingested sources.
