---
title: "Agentic Code Search Recall"
type: concept
tags: [ai, software-engineering, retrieval, coding-agents]
sources:
  - thoughts-on-slowing-the-fuck-down
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[AgenticCodeSearchRecall]] is the proportion of code, decisions, dependencies, and reusable implementations relevant to a coding task that an agent successfully discovers before changing a system.

## Current Synthesis
The source identifies discovery as a distinct limit on coding-agent performance. Before an agent can make a coherent change, it must find all affected locations and existing components worth reusing. Shell search, language servers, code indexes, and vector retrieval can improve discovery, but none guarantees complete recall as codebases and architectural complexity grow.

Low recall creates a reinforcing loop. An agent misses an existing implementation or constraint, adds a duplicate or locally plausible abstraction, and thereby enlarges the future search space. Separate runs also lack much of the reasoning and pain history behind earlier decisions. The result can be internally inconsistent code that becomes progressively harder for later agents and humans to understand or repair.

## Key Claims
- Coding quality depends on discovering affected and reusable code before implementation, not only on generating a locally correct patch.
- Larger and more complex codebases increase the chance that relevant code or prior decisions will be missed.
- Grep, indexes, language servers, and vector search improve access but do not guarantee complete task-specific recall.
- Missed reuse and dependencies encourage duplication, inconsistent abstractions, and incomplete changes.
- Low-recall changes can enlarge the codebase and make future retrieval harder, creating a self-reinforcing complexity loop.

## Evidence
- Discovery boundary: [[thoughts-on-slowing-the-fuck-down]] argues that an agent must locate all code requiring change and all relevant reusable code before it can do reliable work.
- Tool-independent limit: [[thoughts-on-slowing-the-fuck-down]] names ripgrep, queryable indexes, language servers, and vector databases while claiming that recall still falls as the search space grows.
- Compounding mechanism: [[thoughts-on-slowing-the-fuck-down]] connects missed existing code with duplication, inconsistent local decisions, and further complexity.

## Counterevidence & Qualifications
The source offers a practitioner mechanism, not a measured retrieval study. It does not define recall labels, compare tools, establish a codebase-size curve, or distinguish failures caused by retrieval from those caused by planning, context selection, architecture, or model reasoning. Strong modular boundaries, ownership maps, tests, typed interfaces, current documentation, human guidance, and hybrid retrieval may improve effective recall. A bounded task can also succeed without discovering every technically related file when its interface and verification boundary are reliable.

## What Changed
- Created a concept separating code discovery completeness from local code-generation capability.
- Identified a feedback loop in which missed reuse creates complexity that further weakens later retrieval.

## Related Concepts
- [[ContextCoding]] - uses explicit project context and retrieval traces to improve discovery before code generation.
- [[AgenticRAG]] - supplies search and retrieval patterns whose usefulness depends partly on recall over live code.
- [[LLMContextManagement]] - determines which discovered evidence remains available during reasoning and implementation.
- [[BottleneckAwareAICoding]] - treats discovery and human verification capacity as possible constraints on safe throughput.
- [[InternalSoftwareQuality]] - duplication and inconsistent abstractions created by missed context reduce changeability.
- [[SoftwareVerification]] - can expose some missed dependencies but does not guarantee that all relevant code was found.
