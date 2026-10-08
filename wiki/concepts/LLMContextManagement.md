---
title: "LLM Context Management"
type: concept
tags: [ai, llm, context]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou
  - ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache
  - mu-jiang-chui-zi-ding-zi
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
  - gei-ren-wen-gong-zuo-zhe-de-ai-shi-yong-zhi-nan
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
  - blog-guangzhengli-vibe-coding-and-context-coding
  - context-engineering-from-the-inside-out
  - philipp-schmid-gemini-3-prompting-best-practices-for-general-usage
  - effective-context-engineering-for-ai-agents-anthropic
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[LLMContextManagement]] is the practice of controlling what information, instructions, tool results, histories, and compressed summaries enter an LLM's context so the model can reason and act without being overwhelmed or misled.

## Current Synthesis
The sources treat many LLM terms and coding-agent workflows as answers to the same underlying problem: context is powerful but fragile. Skills add expert instructions, MCP narrows action choices through tool schemas, RAG retrieves only relevant outside information, memory writes and retrieves persistent information, dynamic compression removes or externalizes low-value material, and Computer Use introduces external action channels whose observations return to context. Onevcat's Claude Code retrospective turns that architecture into operational advice: decompose tasks, write plan documents, use subagents, compact at natural breakpoints, and start new sessions when a context is overloaded.

Context management also has a provider-facing request-shape layer. Stable system prompts, tools, message prefixes, and cache-control breakpoints can lower repeated inference cost, while private cache edits can make selected tool results disappear from the provider-side cached view without changing the local conversation.

PsiACE's agent essay adds a state-model layer. It argues that sessions, summaries, compaction, forks, merges, handoff, and memory often assume that state must be continuously inherited. [[TapeAndAnchors]] offers a different model: preserve history on an append-only tape, write minimal anchors at stage changes, and assemble context for each task through retrieval and selection rather than automatic continuation.

The mihomo-rust case study adds an operational rule: do not treat a long-running agent team's context as the canonical project state. Put decisions, status, specs, and feedback memory in files, then respawn agents at milestone boundaries so stale intermediate context does not dominate later work.

Hanyang's humanities guide extends the same principle beyond software agents. For research and writing, context management means preparing clean Markdown or text, removing webpage noise, extracting facts and structure before drafting, compressing rich material rather than expanding from thin prompts, and using retrieval or staged batches when the material exceeds the model's useful working memory.

The full AX essay broadens context management from a tooling concern into one of three core [[AgentExperience]] layers. User intent, tool feedback, screenshots, emotional pressure, external observations, and interface warnings all compete inside the agent's working state. This makes context management inseparable from [[AgentInterfaceAsContext]] and [[AXFriendlyInterfaceDesign]]: the system should decide which information reaches the model at the right moment, not merely hope the model calls the right help function or remembers an old prompt.

Guangzhengli turns context management into a practical history of AI coding tools. In that account, Copilot, Cursor, and Claude Code are not only better models or interfaces; they are progressively richer ways to select, retrieve, and expose project context. The source also adds a maintenance warning: instruction files help only when they are concise and current, because stale context can mislead an agent more severely than missing context.

The newest source makes this practice explicit as context engineering and gives it two coupled objectives: curate what the model can use effectively, and keep the reusable prefix stable enough for KV-cache reuse. It maps always-on project instructions to the beginning of context, task-selected skills and action-triggered hooks to timely loading near the current action, and recursive CLI discovery to a way of avoiding large always-loaded tool-schema catalogs. It also treats pattern pollution as distinct from factual noise: examples of undesirable behavior in the trajectory can become implicit instructions that the model repeats.

Schmid's Gemini 3 guide adds a prompt-level placement rule that fits this architecture. Stable roles and behavioral constraints belong at the beginning or in the system instruction, while the concrete question over a large document, codebase, or media context belongs after that material and should explicitly point back to it. This separates persistent policy from the recency-sensitive task. The same guide treats modalities as one context rather than isolated channels: if text, images, audio, or video must jointly inform the result, the instruction should name that synthesis requirement.

Anthropic's first-party synthesis supplies a compact governing objective: context is a finite attention budget, so selection should maximize expected task value per token rather than fill the nominal window. It distinguishes stable preload from runtime discovery. Clear system instructions and a small non-overlapping tool set provide durable orientation; paths, links, stored queries, metadata, and targeted shell operations let the agent progressively disclose task-specific material. A hybrid can preload stable, high-value context for speed and reserve dynamic evidence for just-in-time exploration.

For work that outlives one window, the same objective produces three different continuity mechanisms. Compaction carries a high-recall summary into a fresh window; structured notes persist goals, decisions, and progress outside the prompt; and subagents isolate deep exploration before returning a distilled result. These mechanisms are not interchangeable: the task's latency, decomposability, retrieval environment, and cost of losing subtle detail determine the appropriate mix.

## Key Claims
- LLMs generate from probability distributions over tokens, so context strongly shapes both reasoning and action.
- Skills, MCP, RAG, Memory, and Computer Use can be understood as different context-management and action-interface patterns.
- Longer context windows reduce capacity pressure but do not prevent declining precision, context pollution, or distraction from irrelevant material, messy formats, failed attempts, contradictory instructions, emotional pressure, lossy summaries, and misleading tool traces.
- Stable system/tool prefixes, deterministic tool results, dynamic conversation suffixes, and provider-side cache edits offer ways to balance context adaptation with prompt-cache reuse.
- Long coding-agent and group-chat sessions create practical failure modes when auto-compaction happens mid-task, topics run in parallel, or a task is too large for one session.
- Always-on project files, on-demand skills, action-triggered hooks, append-only history, milestone resets, file-backed state, and just-in-time retrieval avoid carrying every possible input forward; persistent constraints belong early, while task-specific evidence should be loaded when useful.
- Compaction, structured notes, and subagents extend long-horizon work through different lossy or externalized handoffs; their fit depends on task structure, latency, and the cost of missing subtle context.

## Evidence
- Shared framing: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] explicitly says Skills, MCP, and coding-agent command execution are different openings from LLM text generation into the outside world, then frames them as solving context pollution.
- Retrieval framing: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says RAG keeps large knowledge bases and histories outside the prompt until retrieved.
- Noise risk: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] argues that noisy tool returns, failed reasoning traces, and user emotional pressure can degrade later behavior.
- Compression and caching: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] contrasts passive compression with dynamic compression and notes that modifying context conflicts with strict prefix-cache reuse.
- Coding-agent session tactics: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] describes context-window pressure, auto-compaction confusion, task decomposition, subagents, manual compacting at breakpoints, and plan documents for restarting work.
- Provider request shape: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] shows Claude Code preserving cacheable prompt structures and using cache edits to logically remove high-volume tool results from the provider-side view.
- Tape and anchors: [[mu-jiang-chui-zi-ding-zi]] proposes treating history as an append-only tape, storing only minimal anchors, and assembling context through exploration and selection for each new task.
- Milestone respawn: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] requires all teammates to shut down and respawn at milestone completion after saving state to files.
- Humanities source preparation: [[gei-ren-wen-gong-zuo-zhe-de-ai-shi-yong-zhi-nan]] recommends clean text or Markdown, noise removal from webpages, fact and structure extraction before writing, and compression from rich material as practical ways to protect limited model context.
- Context-window realism: [[gei-ren-wen-gong-zuo-zhe-de-ai-shi-yong-zhi-nan]] warns that long inputs are not automatically remembered well, so users should batch, retrieve, or compress material instead of expecting a model to hold everything equally.
- AX layer: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] names internal agent state as the most complex AX layer because user input and outside-world feedback both flow into limited, degradable, pollutable context.
- Interface context: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] argues that GUI and TUI diagnostics can place warnings and constraints into the agent's observed context at the moment of action, unlike static Skills or optional help calls.
- AI coding context: [[blog-guangzhengli-vibe-coding-and-context-coding]] compares Copilot's open-file and cursor context, Cursor's RAG/rules/Git-history/documentation context, and Claude Code's Unix-tool project exploration.
- Instruction-file staleness: [[blog-guangzhengli-vibe-coding-and-context-coding]] warns that outdated project context in rules files can be more harmful than no saved context.
- Context visibility: [[blog-guangzhengli-vibe-coding-and-context-coding]] includes an inspected Claude Code `/context` screenshot that breaks usage into system prompt, tools, MCP tools, messages, and free space.
- Effective attention: [[context-engineering-from-the-inside-out]] uses the lost-in-the-middle pattern to distinguish nominal context capacity from the smaller region where instructions and evidence remain salient.
- Placement and loading: [[context-engineering-from-the-inside-out]] assigns broad project rules to concise `AGENTS.md`/`CLAUDE.md` files, task-specific procedures to on-demand skills, and action-specific guardrails to hooks immediately around tool execution.
- Pattern and cache hygiene: [[context-engineering-from-the-inside-out]] warns that trajectories teach behavior by example and recommends stable ordering plus removal of irrelevant timestamps, UUIDs, and metadata from tool results when cross-request reuse matters.
- Lossy handoff: [[context-engineering-from-the-inside-out]] frames compaction and subagents as sequential and parallel uses of fresh context that both compress information at the handoff boundary.
- Prompt-layer placement: [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] recommends placing role and behavior constraints at the beginning while putting the specific task after a large context block with an explicit bridge to the preceding material.
- Multimodal coherence: [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] says prompts should reference the modalities to be synthesized rather than leave them as disconnected inputs.
- Finite attention budget: [[effective-context-engineering-for-ai-agents-anthropic]] argues that context has diminishing marginal returns and should contain the smallest sufficient set of high-signal tokens.
- Prompt, tool, and example design: [[effective-context-engineering-for-ai-agents-anthropic]] recommends direct minimal-but-sufficient system instructions, non-overlapping token-efficient tools, and diverse canonical examples rather than exhaustive edge-case lists.
- Runtime retrieval: [[effective-context-engineering-for-ai-agents-anthropic]] describes paths, links, stored queries, metadata, file hierarchy, and targeted shell commands as lightweight handles for progressive just-in-time discovery.
- Hybrid loading: [[effective-context-engineering-for-ai-agents-anthropic]] allows stable context to be retrieved up front for speed while the agent explores further evidence at runtime when the task warrants it.
- Long-horizon continuity: [[effective-context-engineering-for-ai-agents-anthropic]] separates high-recall compaction, persistent structured notes, and specialized subagents that return distilled findings.

## Counterevidence & Qualifications
The sources are practitioner essays and code-reading analyses rather than empirical benchmarks. They give vivid model-behavior examples but do not provide controlled evidence for failure rates across models, tools, or task types. The private cache-edit account depends on inferred provider behavior, and the interface-as-context claim remains a design argument rather than a validated UI standard. Guangzhengli's tool comparison is also experience-based and may change with pricing, model quality, and product behavior. The newest source's tagging-agent accuracy is self-reported without a published evaluation protocol, and its claims about thinking-token removal depend on a particular runtime.

The tape-and-anchors model is also conceptual: it gives a useful alternative to inherited session state, but does not yet specify anchor schemas, retrieval evaluation, conflict handling, or deletion/privacy semantics.

The humanities-workflow source gives practical heuristics but not measured thresholds for how much text different models can reliably use, or when RAG, batching, and manual source preparation outperform each other.

Schmid's placement and multimodal recommendations are likewise model-specific practitioner guidance without controlled comparisons. Beginning-and-end placement may improve salience, but it does not guarantee faithful use of the intervening material, and added planning or anchoring language consumes context and latency that simple tasks may not need.

Anthropic's article is first-party design guidance rather than a comparative evaluation. It cites context-rot research and a multi-agent improvement but the supplied text gives no benchmark protocol, model-by-model thresholds, compaction-fidelity measure, or cost/latency comparison between preload, runtime retrieval, notes, and delegation. Its `n²` pairwise-attention explanation is a useful intuition, not a complete causal account of long-context degradation.

## What Changed
- Added the finite-attention objective of maximizing task value per token rather than filling the nominal window.
- Added just-in-time discovery and hybrid preload/runtime retrieval as explicit context-loading strategies.
- Separated compaction, structured notes, and subagents by continuity mechanism and task fit.
- Qualified Anthropic's recommendations as first-party guidance without supplied comparative evaluation.

## Related Concepts
- [[LLMToolingSkills]] - Skills manage context by adding expert instructions.
- [[ModelContextProtocol]] - MCP narrows the action surface through typed tool calls.
- [[RetrievalAugmentedGeneration]] - RAG retrieves context instead of preloading everything.
- [[AgentMemory]] - agent memory adds a writeable retrieval layer.
- [[DynamicContextCompression]] - dynamic compression actively preserves context quality.
- [[ComputerUse]] - Computer Use returns UI state and actions into the agent context loop.
- [[VibeCoding]] - coding-agent speed depends on keeping task and session context manageable.
- [[PromptCaching]] - prompt cache design rewards stable context shape and affects compression choices.
- [[TapeAndAnchors]] - append-only history and anchors provide an alternative context-reconstruction model.
- [[AgentTeam]] - multi-agent workflows intensify context-management pressure.
- [[AIWorkflowDesign]] - workflow design turns context preparation into a repeatable production practice.
- [[AgentInterfaceAsContext]] - interfaces can deliver timely diagnostic context during agent action.
- [[ContextCoding]] - context coding applies these context-management concerns directly to AI-assisted software development.
- [[PromptEngineering]] - turns context selection, boundaries, placement, and output requirements into a task-facing instruction contract.
- [[AgenticWorkflowPatterns]] - subagents isolate deep exploration and return compressed results when task decomposition justifies the handoff.
