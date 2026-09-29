---
title: "I told a senior developer at Microsoft he was wrong."
type: source
tags: [software-engineering, internship, mentorship, workplace-learning]
date: 2016-09-13
source_file: "/mnt/ken_personal_wiki/Articles/I told a senior developer at Microsoft he was wrong.md"
---

## Summary
A first-person account of a six-month [[Microsoft]] internship traces the author's move from intimidated rule-following to independent engineering judgment. Repeated code review, sustained questions to senior colleagues, and a memory-leak investigation inside [[MicrosoftGroove]] eventually showed that seniority does not guarantee correctness and that junior engineers create value by understanding a system well enough to identify and improve what others missed. The account gives a concrete apprenticeship case for [[JuniorEngineerLearning]], [[WorkplaceLearning]], and [[EngineeringExpertise]] while preserving the unusually supportive environment and retrospective nature of the lesson.

## Key Claims
- A new engineer entering a roughly ten-million-line C++ codebase may need months of feedback, questions, and repeated attempts before becoming productive; initial slowness does not establish inability.
- Line-by-line review and permission to restart helped expose weak decisions, but regular access to another senior developer's extended explanations made the code workable and converted seemingly basic questions into system knowledge.
- Blind obedience to senior colleagues limits professional value because experience does not make any individual infallible.
- Investigating a memory leak from tool signal to code history let the intern connect a raw-pointer method signature with broken smart-pointer deallocation behavior and propose the correction to a senior author.
- The senior author's immediate acceptance of the finding turned disagreement into a low-friction correction rather than a status contest, illustrating a practical form of [[PsychologicalSafety]].
- Confidence grew from accumulated evidence of useful diagnosis and contribution, not reassurance alone; after the first correction, the author increasingly found and fixed overlooked problems.
- By the end of the internship, the author reports changing thousands of lines across backend, file-system, synchronization, and SharePoint-integration code, although the essay supplies no independent outcome or quality measures.

## Key Quotes
> "Oh yeah. You're right, it should be the other way." - the senior developer accepting the intern's diagnosis.

> "Never doubt that you can do something better than your superiors." - the author's closing lesson about independent judgment.

## Connections
- [[Microsoft]] - employer and large-codebase setting for the internship account.
- [[MicrosoftGroove]] - peer-to-peer business-sharing product whose storage, synchronization, and SharePoint integration supplied the technical work.
- [[JuniorEngineerLearning]] - repeated review, questions, restarts, and gradually harder work built practical judgment.
- [[WorkplaceLearning]] - senior explanations and a real memory-leak investigation turned production work into apprenticeship.
- [[EngineeringExpertise]] - the memory-leak diagnosis shows expertise emerging through system tracing and mechanism-level reasoning.
- [[PsychologicalSafety]] - asking basic questions and challenging a senior developer produced explanation and correction rather than humiliation.
- [[ImposterSyndrome]] - the author initially interpreted slow progress and dependence on senior help as evidence that he might not belong or add value.
- [[CodeReviewPractice]] - line-by-line review repeatedly exposed problems and guided new attempts, though at high mentoring cost.

## Contradictions
- The account qualifies any simple rule that senior direction should be followed without challenge: senior expertise accelerated learning, but a senior engineer also introduced the defect that the intern diagnosed.
- The source is a retrospective personal essay. It does not measure the internship's code quality, team outcomes, mentoring cost, or whether its three-month confidence shift generalizes across people, teams, and codebases.
