---
title: "Context Coding"
type: concept
tags: [ai, software-engineering, developer-tools, context-engineering]
sources:
  - blog-guangzhengli-vibe-coding-and-context-coding
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ContextCoding]] is Guangzhengli's label for disciplined AI-assisted programming where the central skill is supplying, maintaining, and debugging the right project context for an LLM or coding agent.

## Current Synthesis
The source argues that serious AI-assisted programming should be understood as context-driven rather than vibe-driven. Model capability matters, but tool progress is explained through better context channels: open IDE files, cursor-local completion context, project-wide RAG, explicit file and folder references, Git history, documentation indexes, rules files, command-line code search, MCP tools, logs, browser diagnostics, and project instruction files.

Context coding also changes developer practice. Teams should record durable project facts such as stack, directory structure, naming conventions, commands, utilities, core modules, and development norms in tool-specific instruction files, but should avoid stuffing them with stale context. At task time, the developer and agent should use small changes, existing patterns, current documentation, targeted logs, tests, and retrieval tools to keep generated code grounded in the actual system.

## Key Claims
- AI coding improvements come from context quality as well as stronger base models.
- Context engineering includes Chat, RAG, rules, MCP, documentation, tool output, and future context channels.
- IDE-based context and direct editing made Copilot and Cursor important milestones, while command-line search gives Claude Code a different strength.
- RAG and grep/search solve different context problems and should eventually coexist in mature AI IDEs.
- Durable project context belongs in maintained instruction or rules files, while stale context can be worse than no context.
- Good context coding borrows ordinary engineering habits: learn existing patterns, make gradual changes, keep code readable, avoid unjustified new tools, log aggressively while debugging, and verify behavior.
- Context coding is not pure no-review vibe coding; it requires human judgment, review, and production responsibility.

## Evidence
- Tool progression: [[blog-guangzhengli-vibe-coding-and-context-coding]] traces Copilot's open-file context, Cursor's codebase RAG and rules, and Claude Code's command-line project exploration as context milestones.
- Core mechanism: [[blog-guangzhengli-vibe-coding-and-context-coding]] says AI-assisted coding improvements outside model quality all come from giving LLMs more appropriate context.
- RAG role: [[blog-guangzhengli-vibe-coding-and-context-coding]] describes Cursor indexing a codebase into chunks, embedding it, storing it in a cloud vector database, and retrieving nearest neighbors through Turbopuffer.
- Grep role: [[blog-guangzhengli-vibe-coding-and-context-coding]] says Claude Code searches the project with Unix tools in a way that resembles a programmer following names, calls, and business-relevant code paths.
- Instruction files: [[blog-guangzhengli-vibe-coding-and-context-coding]] recommends `.github/copilot-instructions.md`, Cursor rules, and `CLAUDE.md` for stable project context.
- Staleness warning: [[blog-guangzhengli-vibe-coding-and-context-coding]] warns that outdated instruction-file context can be more harmful than omitting it.
- Debugging context: [[blog-guangzhengli-vibe-coding-and-context-coding]] recommends logs, context7-like documentation MCPs, browser console information, and web search as ways to improve the model's working context.

## Counterevidence & Qualifications
The source is a practitioner essay rather than a benchmark, and its tool comparisons depend on the author's experience, model availability, token budgets, pricing, and product behavior at the time of writing. It does not prove that grep beats RAG or that command-line agents always beat IDEs; instead, it argues that code retrieval needs both semantic and exact, current, business-aware search. The proposed instruction-file practice also has a maintenance cost because stale rules can mislead agents.

## What Changed
- Created the concept page for context coding as the disciplined counterpart to no-review vibe coding.

## Related Concepts
- [[VibeCoding]] - context coding is proposed as a clearer name for serious AI-assisted coding than broad popular use of vibe coding.
- [[LLMContextManagement]] - context coding is a software-development instance of controlling model context.
- [[AICodingPractice]] - context coding supplies concrete habits for safer agent-assisted programming.
- [[AgenticRAG]] - live search/read loops provide current code context during coding tasks.
- [[RetrievalAugmentedGeneration]] - project RAG is one context source used by AI IDEs.
- [[CodingAgentMinimalTooling]] - command-line tools, grep, file reads, and edits form a context-gathering substrate.
- [[HumanCodeResponsibility]] - disciplined context does not remove human accountability for generated code.
- [[SoftwareVerification]] - tests and logs turn context coding into checked behavior rather than fluent output.
