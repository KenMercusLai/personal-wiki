---
title: "Traceable Multi-Source Comparison"
type: concept
tags: [evidence-provenance, multimodal-analysis, comparison, human-review]
sources:
  - vane-data-hawdb-video-comparison
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[TraceableMultiSourceComparison]] is a workflow for retrieving claims from multiple text or media sources, deciding whether their subjects, metrics, and conditions permit comparison, and preserving enough versioned evidence to reconstruct and human-check every conclusion.

## Current Synthesis
The workflow separates four questions that are easy to collapse: whether a passage is relevant, whether a model extracted its claim correctly, whether claims from two sources are comparable, and whether comparable claims agree or conflict. A relevant fragment may name the wrong device, omit a nearby duration, or contain only one part of a visual table. Structured fields help expose those gaps, but original transcript ranges, adjacent cues, frames, timestamps, and source versions remain the authority.

Traceability is a joint data and application property. Stable evidence identifiers, processing runs, source relationships, and consistent reads preserve what was analyzed; application rules verify citation ranges, restore context, reject unsupported fields, and provide playback. Historical reproducibility additionally requires model, prompt, protocol, runner, cache, and source-version identity, not merely a stored final JSON result.

## Key Claims
- Retrieval relevance is not evidence that passages discuss the same subject or answer the same comparison question.
- Comparability should be evaluated before agreement or conflict, with missing conditions treated as unknown rather than equal.
- Structured extraction makes claims, conditions, uncertainties, and citations inspectable but does not make them complete or correct.
- Source versions and evidence locations must travel with derived results so later edits or reprocessing do not erase the original basis.
- Human review needs adjacent transcript and visual context because decisive qualifiers may sit outside a selected range or in a frame.
- Incremental reuse requires identity across the question, model configuration, protocol, runner, source versions, and completeness state.

## Evidence
- Relevance versus identity: [[vane-data-hawdb-video-comparison]] shows a passage retrieved for an iPhone 18 Pro question that actually described Duo, with the identifying cue omitted from the initial citation.
- Conditions versus relation: [[vane-data-hawdb-video-comparison]] finds a three-minute 4K60 experience and a 30-minute stress-test temperature non-comparable before judging their relation undetermined.
- Visual and adjacent context: [[vane-data-hawdb-video-comparison]] recovers device labels, battery-health differences, and test duration from frames and surrounding material missed by automatic fields.
- Versioned replay: [[vane-data-hawdb-video-comparison]] stores selected processing runs with results and traces each side back to original transcript or frame evidence and playback.
- Reuse gate: [[vane-data-hawdb-video-comparison]] permits cached extraction and pairwise comparisons only when all relevant execution and source identities remain unchanged.

## Counterevidence & Qualifications
The source demonstrates one curated four-video proof of concept and does not measure extraction accuracy, citation precision, retrieval recall, reviewer agreement, cost, latency, or scaling. The demo summaries and watch recommendations were prepared in advance rather than produced by complete real-time video analysis. Five-second frame sampling can miss short-lived visual evidence, while denser sampling cannot guarantee completeness. Preserving a source snapshot improves auditability but does not prove that the source, transcription, OCR, model interpretation, or human review is correct.

## What Changed
- Established relevance, extraction validity, comparability, and claim relation as four separate judgments.
- Added versioned transcript-and-frame replay as the evidence boundary for multimodal comparison.
- Defined the cache-reuse gate across question, model, protocol, runner, source version, and completeness.

## Related Concepts
- [[RetrievalAugmentedGeneration]] - supplies candidate evidence, but relevance alone does not establish comparability or citation validity.
- [[MultimodalDataPipelines]] - carries transcripts, frames, timestamps, and structured outputs through the workflow.
- [[GraphModeling]] - represents provenance relationships among authors, videos, processing runs, and evidence.
- [[HumanAgencyInAI]] - human checking resolves omitted conditions, wrong subjects, and incomplete visual interpretation.
- [[EvidenceBasedSoftwareEngineering]] - shares the requirement that conclusions remain tied to inspectable evidence and explicit limitations.
