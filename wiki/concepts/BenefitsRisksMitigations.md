---
title: "Benefits, Risks, Mitigations"
type: concept
tags: [decision-making, design-review, engineering-management]
sources:
  - understand-design-build-a-framework-for-problem-solving-lob-blog
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[BenefitsRisksMitigations]] is a design-decision frame that requires a team to state several candidate approaches and, for each one, the benefits it offers, the risks it creates, and the mitigations that would contain those risks.

## Current Synthesis
The Lob source recommends this frame for the Design step of [[UnderstandDesignBuild]] and attributes it to a First Round Review matrix. Its function inside the framework is to stop teams from defaulting to the first idea: the source argues that mature companies have fewer obvious solutions because the easy ones are already solved, so the useful work is researching more than one option and making the trade-offs visible before committing. The frame is a comparison device rather than a scoring model. It produces a shared picture of what each approach gives the business, what exposure it creates, and what would reduce that exposure, which is what a whiteboarding session, design doc, one-pager, or technical design review is meant to capture. Paired with the framework's third step, the output of this analysis is also the reason Build becomes cheap: the hard decisions are already made and recorded.

Within the wiki, the frame sits alongside other decision-shaping practices rather than replacing them. [[MultiplePathsToYes]] describes how many candidate paths are handled for reversible bets, [[ArchitectureAlignmentForces]] varies decision formality by organizational alignment and blast radius, and [[StrategicWriting]] is the medium that makes this reasoning inspectable by people who were not in the room.

## Key Claims
- Design decisions improve when more than one candidate approach is stated explicitly.
- Each approach should be described through benefits, risks, and the mitigations that would limit those risks.
- The first approach that comes to mind is unlikely to be the best one, which is why comparison is the point.
- The need for this analysis grows as a company matures and the obvious solutions are already taken.
- Whiteboarding, design docs, one-pagers, and technical design reviews are the vehicles that make the comparison reviewable.
- Finished design reasoning is what makes implementation the easy step of the process.

## Evidence
- Frame and attribution: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] recommends the benefits, risks, and mitigations matrix and credits a First Round Review article for it.
- Design questions: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] lists the questions the Design step must answer: what approaches could solve the problem, and what are their benefits, risks, and mitigations.
- Mature-company difficulty: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] argues that as companies mature fewer problems have obvious solutions because the easy ones have been solved already.
- First-idea skepticism: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] says it is unlikely that the first option considered is the best one, so time spent researching alternatives reveals the trade-offs being accepted.
- Review vehicles: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] says the work can take the form of a whiteboarding exercise, a design doc or one-pager, or a full-blown technical design review.
- Institutional purpose: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] describes the technical design review as an institutionalized way to ensure reasonable alternatives are considered and their implications explored.

## Counterevidence & Qualifications
The frame comes from a single practitioner description of a First Round Review matrix, and the wiki does not contain that matrix itself. Its discipline is also its cost: documenting several approaches with benefits, risks, and mitigations takes time that small, reversible, or easily measured changes may not deserve, and the wiki's fast-delivery material treats that ceremony as a speed risk for small trusted teams. The frame can also degrade into a ritual where every option receives a benefits, risks, and mitigations list that is never actually used to choose, and the source gives no method for comparing options whose benefits and risks are not commensurable.

## What Changed
- Created the concept from Lob's 2019 engineering-blog post.

## Related Concepts
- [[UnderstandDesignBuild]] - the framework step this frame belongs to.
- [[FirstRoundReview]] - credited publisher of the benefits, risks, and mitigations matrix.
- [[StrategicWriting]] - written design artifacts carry this analysis to people who were not in the room.
- [[MultiplePathsToYes]] - a complementary pattern for running several candidate approaches rather than choosing one.
- [[ArchitectureAlignmentForces]] - varies how formal this kind of decision analysis should be.
- [[BehavioralRiskJudgment]] - the risk half of the frame depends on honest probability and incentive reasoning.
