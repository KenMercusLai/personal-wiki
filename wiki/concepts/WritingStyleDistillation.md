---
title: "Writing Style Distillation"
type: concept
tags: [ai, writing, style, skills]
sources:
  - ru-he-cong-zi-ji-xie-guo-de-wen-zhang-li-ti-lian-xie-zuo-feng-ge-wo-fan-le-12-pian-jiu-wen-zui-hou-zhi-you-2-pian-neng-dang-gu-jia
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[WritingStyleDistillation]] is the practice of deriving a maintained writing guide from an author's verbatim work by selecting evidence by dimension, encoding structural and linguistic regularities, testing them on real drafts, and revising the guide from observed edits.

## Current Synthesis
The source presents style as more than a vocabulary fingerprint. Sentence length, punctuation, heading form, paragraph shape, concrete openings, first-person judgment, admission of mistakes, evidence discipline, and explicit uncertainty all contribute to recognizable writing. A summary is therefore unsuitable as the primary corpus: it can retain the topic while deleting the form that must be learned.

Corpus selection is curatorial rather than additive. Mai Yang separates two articles that can supply structural skeletons from year-end posts that supply candid tone, while refusing to average every sampled weakness into the target. The resulting [[LLMToolingSkills|Skill]] puts two reusable skeletons before a blacklist and retains verbatim voice samples as references. Borrowed prohibitions are treated as hypotheses to test against the author's strongest lines, not universal rules.

The method remains incomplete until it becomes behavioral. A writer applies the guide to a real document, manually edits the result, diffs the machine draft against the accepted version, and updates the guide with the recurring reasons for those changes. For consequential work documents, this feedback loop sits below a non-invention rule: absent numbers, owners, commitments, risk levels, and exact quotations must stay marked as unknown.

## Key Claims
- Verbatim Markdown preserves style evidence that thematic summaries remove.
- Exemplars should be selected by dimension, because structure, tone, and other desirable traits may occur in different texts.
- Generative skeletons describe how a piece moves; blacklists only suppress a subset of unwanted surface habits.
- Borrowed style rules should be falsified against the author's best passages and narrowed when they erase authentic constructions.
- Real-task editing diffs provide stronger feedback than repeated conversational requests for a local rewrite.
- Factual uncertainty and quotation fidelity should override stylistic smoothness in consequential documents.

## Evidence
- Corpus fidelity: [[ru-he-cong-zi-ji-xie-guo-de-wen-zhang-li-ti-lian-xie-zuo-feng-ge-wo-fan-le-12-pian-jiu-wen-zui-hou-zhi-you-2-pian-neng-dang-gu-jia]] contrasts a compressed English summary with a twelve-character Chinese bullet whose formatting, idiom, and brevity carried the style.
- Dimension-specific curation: [[ru-he-cong-zi-ji-xie-guo-de-wen-zhang-li-ti-lian-xie-zuo-feng-ge-wo-fan-le-12-pian-jiu-wen-zui-hou-zhi-you-2-pian-neng-dang-gu-jia]] selects two of twelve posts for structure while using weaker annual reviews only for self-deprecating tone.
- Structure before prohibition: [[ru-he-cong-zi-ji-xie-guo-de-wen-zhang-li-ti-lian-xie-zuo-feng-ge-wo-fan-le-12-pian-jiu-wen-zui-hou-zhi-you-2-pian-neng-dang-gu-jia]] reports that forty-seven banned expressions did not make prior drafts sound like the author, then moves event-led skeletons ahead of the blacklist.
- Rule validation: [[ru-he-cong-zi-ji-xie-guo-de-wen-zhang-li-ti-lian-xie-zuo-feng-ge-wo-fan-le-12-pian-jiu-wen-zui-hou-zhi-you-2-pian-neng-dang-gu-jia]] restores qualified uses of “not A but B” and sentence-internal “honestly” after finding them in favored original passages.
- Revision loop and red lines: [[ru-he-cong-zi-ji-xie-guo-de-wen-zhang-li-ti-lian-xie-zuo-feng-ge-wo-fan-le-12-pian-jiu-wen-zui-hou-zhi-you-2-pian-neng-dang-gu-jia]] recommends a real assignment, manual editing, diff-based rule updates, and placeholders for facts or ownership that remain unknown.

## Counterevidence & Qualifications
The concept currently rests on one author's retrospective and a first-pass Skill that has not yet gone through its own proposed edit-and-diff cycle. Four of twelve posts were available only as summaries, the two structural exemplars were selected subjectively, and the source provides neither the completed files nor blind reader evaluation, cross-task testing, comparison against a smaller prompt, or evidence about how often rules conflict. Dimension-specific curation may also overfit a narrow genre or freeze an author's past habits. A blacklist can still be useful for recurring failure modes, and a broad corpus may reveal stable variation when weighting, genre labels, and quality judgments are explicit. The method should therefore be treated as a testable editorial workflow, not a proven recipe for voice replication.

## What Changed
- Created a concept separating verbatim style evidence, dimension-specific exemplar selection, structural skeletons, blacklists, and voice samples.
- Made real-task editing diffs the update mechanism rather than treating one-time extraction as a finished style model.
- Put non-invention and explicit uncertainty above voice imitation for consequential documents.

## Related Concepts
- [[AIAssistedWriting]] - style distillation supplies reusable guidance while leaving selection, editing, verification, and publication responsibility with the writer.
- [[LLMToolingSkills]] - a style guide can be packaged as on-demand instructions plus reference files and examples.
- [[SemanticAblation]] - verbatim exemplars and side-by-side diffs help detect loss of precise or distinctive language.
- [[PersonaDistillation]] - style distillation targets a bounded production behavior rather than reconstructing a person's identity or full judgment.
- [[PromptEngineering]] - maintained evidence and workflow rules replace repeated generic tone requests.
