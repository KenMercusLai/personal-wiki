---
title: "Prompt Engineering"
type: concept
tags: [ai, llm, prompting, context-engineering]
sources:
  - philipp-schmid-gemini-3-prompting-best-practices-for-general-usage
  - manage-requirements-like-code
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[PromptEngineering]] is the empirical design of instructions, context boundaries, examples, process cues, and output constraints so a language model can perform a defined task reliably enough for its intended use.

## Current Synthesis
[[PhilippSchmid]]'s Gemini 3 playbook treats a strong prompt as a small interface contract. It states the goal directly, defines ambiguous parameters, uses one consistent structural language such as XML or Markdown, and names the required output. Persona and behavioral constraints sit at the beginning or in the system instruction; when a large body of evidence is supplied, the specific task sits after it and explicitly reconnects the question to that evidence. These are complementary placement rules for different prompt layers, not a requirement to put every instruction in two places.

For more complex work, the prompt can request decomposition, an input-completeness check, method selection, progress tracking, and a final constraint review. Agentic variants add persistence and recovery when a tool fails, while research variants require claim-level citation. Multimodal tasks need the instructions to identify which text, image, audio, or video inputs must be combined rather than leaving the model to treat them as unrelated attachments.

Zhang's custom product-management Gem shows how that interface contract can become a reusable operating protocol. Its instructions define initialization, document schema, semantic versions, atomic-edit boundaries, plan-confirm-execute gates, named review commands, PRD/prototype synchronization rules, session isolation, and separate channels for discussion and deliverables. This moves prompting from wording a single request toward governing a multi-artifact workflow, while also showing the risk that a long natural-language contract becomes internally inconsistent or only partially followed.

The most durable principle across both sources is experimental: templates are baselines. Extra planning, reflection, tags, personas, gates, or protocols should earn their cost through better task results, and practices that work for one model, domain, or latency budget should be measured before becoming defaults elsewhere.

## Key Claims
- State the goal, definitions, constraints, desired output, and boundaries among instructions, source material, process, and output directly and consistently.
- Put durable behavior constraints early, but place a question about a large supplied context after the evidence and anchor it back to that material.
- Ask for decomposition, missing-input detection, method selection, or self-review when task complexity justifies the added process.
- Reference modalities explicitly when an answer must synthesize text, images, audio, or video.
- Tie agentic persistence and tool use to verification, failure recovery, and the user's actual completion criterion.
- Reusable system instructions can define commands, state transitions, approval boundaries, artifact identity, and output channels for a continuing workflow.
- Treat every template or protocol as a model- and task-dependent hypothesis to iterate and evaluate.

## Evidence
- Direct contract: [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] recommends precise instructions, defined parameters, explicit verbosity, and consistent XML or Markdown structure.
- Placement: [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] puts roles and behavioral constraints early while placing long-context questions after the supplied data with an anchoring phrase.
- Multimodal coherence: [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] asks prompts to reference specific modalities and synthesize them as equal-class inputs.
- Reasoning workflow: [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] supplies decomposition, completeness, alternative-method, outline, and critique checklists.
- Agentic execution: [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] combines persistence after tool failure with pre-tool statements of purpose and expected evidence.
- Iteration boundary: [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] calls its template a starting point and says optimal structure depends on data, latency, task, and domain.
- Workflow protocol: [[manage-requirements-like-code]] defines a custom Gem whose instructions govern initialization, PRD structure, versions, scoped edits, review commands, Canvas output, and cross-artifact synchronization.
- Approval boundary: [[manage-requirements-like-code]] shows a change briefing that stops for explicit confirmation before mutating the PRD and requires permission before synchronizing the prototype.
- Recovery behavior: [[manage-requirements-like-code]] recommends topic isolation, artifact export, a structured context-migration summary, and a clean session after sustained answer drift.

## Counterevidence & Qualifications
The evidence comes from two practitioner accounts, not controlled comparisons across prompts, models, tasks, or users. Neither measures whether explicit planning, review personas, approval gates, TODO tracking, self-critique, XML, Markdown, or channel rules improve correctness enough to justify extra tokens, latency, and interaction. Visible process can become ceremonial, and a long instruction contract can contain competing rules or be followed selectively. The product-management case also embeds version history in generated prose rather than an independently enforced store. Model training and product behavior change, so model-specific advice should be retested; high-stakes work still needs external evidence, deterministic checks, and accountable human review rather than confidence in prompt wording alone.

## What Changed
- Extended prompt engineering from single-task structure to reusable workflow protocols with commands, gates, artifact identity, and output channels.
- Added instruction-length, partial-compliance, and ceremonial-process risks.
- Preserved empirical evaluation and model specificity as boundaries on template reuse.

## Related Concepts
- [[LLMContextManagement]] - prompt placement and selective context determine what instructions and evidence remain salient.
- [[StructuredProblemSolving]] - decomposition and completeness checks provide a reasoning scaffold for complex prompts.
- [[AgenticWorkflowPatterns]] - persistence, tools, feedback, and validation turn an instruction into an execution loop.
- [[PromptCaching]] - stable reusable prompt prefixes can affect the cost of instruction structure.
- [[SchemaBasedReasoning]] - explicit structures can constrain how inputs and outputs are organized.
- [[SoftwareVerification]] - external checks are stronger evidence of correctness than self-critique alone.
- [[RequirementsAsCode]] - applies prompt-level workflow contracts to versioned PRDs, prototypes, reviews, and recovery.
