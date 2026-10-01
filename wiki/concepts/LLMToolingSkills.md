---
title: "LLM Tooling Skills"
type: concept
tags: [ai, llm, prompting]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de
  - yan-li-how-llm-agents-became-what-they-look-like-in-2026
  - lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai
  - context-engineering-from-the-inside-out
  - dont-trust-ai-agents-nanoclaw-blog
  - mario-zechner-what-if-you-dont-need-mcp-at-all
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[LLMToolingSkills]] are agent-readable packages that add domain knowledge, procedures, and reasoning guidance and may also carry reference implementations or executable assets; instructions shape model behavior, while runtime integration determines any actual capability.

## Current Synthesis
The sources present Skills as prompt-level workflow guidance. A Skill imports expert structure into the prompt so the model can approach a task with better assumptions and workflow, but it does not enforce execution like a runtime API. Its value is highest when a task needs richer thinking, domain framing, or loose coordination that cannot easily be reduced to RPC-style functions.

The loading model is the practical distinction. Rules are short always-on constraints, specs are business-state inputs, and skills are on-demand workflows that can include SOP steps, few-shot references, and CLI/script hooks. Skill-following is still probabilistic, but it can improve when relevant instructions are loaded near generation time with a much higher signal-to-noise ratio than a long global rule file.

The newest source reframes Skills as a distribution format rather than only a prompting technique. It calls agent-skills a protocol for dynamic prompt injection in which the agent decides which prompts to load, and notes that in practice a skill is nothing more than a set of files. That makes the folder the product: `prompt.md`, `tools.sh`, `helper.py`, executables, shared libraries, and arbitrary assets can all travel together, and because the skill needs no runtime or dependencies as long as the client agent already operates at the general-OS stage, its author expects it to be adopted more widely than [[ModelContextProtocol]]. The imagined end state is an OS package manager that installs a program and its agent skill in the same command.

In OpenClaw's operational model, a Moltbook Skill is not only explanatory prose: the main file records endpoints, authentication boundaries, request templates, response shapes, rate limits, and refusal conditions, while companion heartbeat and messaging files shape recurring participation and notification behavior. This supports the folder-as-distribution framing but also exposes its safety boundary: natural-language restrictions remain probabilistic unless the runtime independently scopes credentials, hosts, tools, and sensitive actions.

The newest source explains why on-demand loading matters inside the prompt. Only skill names and selection descriptions need remain in the always-on index; the full procedure enters context after the current task makes it relevant. This protects limited effective attention from unrelated workflows and puts the selected instructions near the current generation. It also distinguishes skills from hooks: the model selects a skill by task relevance, while the runtime triggers a hook around a particular action.

NanoClaw adds a security and installation variant: a skill includes instructions plus a working reference implementation that a coding agent merges into the owner's codebase after review. In that model, skills keep the core small and make installed integrations explicit, but review and selective installation—not the skill format itself—provide the intended security benefit. Once merged, executable code joins the trusted installation and still needs runtime isolation, credential scoping, and verification.

Zechner adds an intentionally informal analogue: a 225-token README documents a small browser CLI and is loaded only for sessions that need it. The files can be placed on PATH and reused across agents without relying on a particular skill-discovery implementation. This reinforces progressive disclosure and folder-based distribution, while also showing what formal skill systems add: discovery conventions and non-technical accessibility. The article's concern that automatic discovery may be unreliable and may preload metadata is one user's experience, not a general comparison of skill implementations.

## Key Claims
- Skills add instructions and expert cognitive structure to the model context.
- Skill-following depends on the model's respect for context and remains probabilistic, and over-constraining behavior can make reasoning less flexible.
- Skills guide reasoning rather than enforce execution; the execution channel can be a separate tool, a bundled executable asset, or reviewed reference code merged into the installation.
- Skills remain useful when a task is too open-ended, low-interaction, or expensive to encode as a dedicated server API.
- Skills can encode more than linear SOPs; exploration and brainstorming skills may be valuable precisely because they prompt multi-dimensional analysis.
- Skills work best when separated from rules and specs: a lightweight always-on index plus on-demand full instructions protects context capacity and instruction salience better than one undifferentiated prompt file.
- A skill or informal README-described tool folder can ship instructions, examples, scripts, metadata, safety rules, and recurring-work conventions when the client agent already supplies the runtime.

## Evidence
- Prompt nature: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] describes Skills as instructions shown to the LLM rather than external action channels.
- Compliance limit: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says the model may or may not use the Skill, follow steps, or choose the expected order.
- Flexibility qualification: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] warns that hard constraints can narrow the model's thinking.
- Use case: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Skills are valuable when the work needs fuller reasoning and cannot reasonably be packaged as RPC.
- Loading distinction: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] distinguishes specs as business knowledge, rules as always-loaded engineering constraints, and skills as on-demand workflows.
- Signal-to-noise: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] argues that a focused skill can outperform a long rule file because only task-relevant instructions, examples, and scripts enter the immediate context.
- Skill dimensions: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] describes SOP steps, reference examples, and CLI/script integration as complementary skill ingredients.
- Dynamic injection: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] describes agent-skills as a protocol for dynamic prompt injection where the agent decides which prompts it should load.
- File-only form: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says a skill is in practice nothing more than a set of files.
- Runtime-free distribution: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says a skill is self-contained, easy to distribute, and needs no runtime or dependencies assuming the client agent already operates at Stage 4.
- Arbitrary payloads: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says a skill can pack `prompt.md`, `tools.sh`, `helper.py`, `bin/executable`, `lib/library.so`, and any other OS-runnable asset.
- Adoption forecast: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] argues agent-skills is more likely than MCP to be widely adopted because it is simple, self-contained, and dependency-free.
- Package-manager metaphor: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] imagines an OS distro installing a program and its agent skill in one command.
- Operational contract: [[lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai]] describes a Moltbook Skill containing API endpoints, authentication and domain restrictions, request examples, result formats, and rate limits.
- Recurring behavior: [[lencx-shen-du-jie-du-openclaw-jia-gou-ji-sheng-tai]] adds heartbeat and messaging files that turn one-off tool knowledge into scheduled participation and notification policy.
- On-demand trajectory: [[context-engineering-from-the-inside-out]] shows an always-loaded index of skill names, descriptions, and locations followed by a model-selected read that brings only the relevant skill into the active trajectory.
- Trigger distinction: [[context-engineering-from-the-inside-out]] contrasts task-selected skills with action-triggered hooks that inject safeguards immediately before or after matching tool calls.
- Reviewed installation: [[dont-trust-ai-agents-nanoclaw-blog]] describes skills as instructions with working reference implementations that a coding agent merges only after the owner reviews the proposed code.
- Attack-surface claim: [[dont-trust-ai-agents-nanoclaw-blog]] argues that selective skill installation keeps dormant integrations out of the runtime, unlike a monolith where disabled code remains present.
- Informal progressive disclosure: [[mario-zechner-what-if-you-dont-need-mcp-at-all]] loads a compact browser-tool README only for relevant sessions and puts the scripts on PATH for reuse across different coding agents.
- Formal-system comparison: [[mario-zechner-what-if-you-dont-need-mcp-at-all]] credits skills with progressive disclosure and broad accessibility but prefers explicit README loading because of perceived discovery and metadata overhead.

## Counterevidence & Qualifications
The sources evaluate Skills conceptually and through practitioner workflow rather than isolating skill effects in controlled benchmarks. They also use "Skills" broadly; implementations may vary in how they are selected, injected, validated, positioned in context, combined with tools, or merged as code. Selection can fail when metadata is weak or the model does not recognize relevance, while explicit README loading depends on the user remembering and naming the right file. The runtime-free distribution thesis assumes the client already provides file, shell, scheduling, credential, and policy substrates, which shifts rather than removes dependencies. Written restrictions and human code review are useful controls but are not enforcement boundaries against prompt injection, dependency compromise, review error, or model noncompliance.

## What Changed
- Broadened the definition to cover reviewed reference implementations merged into an installation as well as prompt-only guidance and bundled executable assets.
- Separated the auditability benefit of selective installation from the security guarantees still required at runtime.
- Added explicit README loading as a cross-agent, informal progressive-disclosure variant.

## Related Concepts
- [[LLMContextManagement]] - Skills manage context by adding structured instructions.
- [[ModelContextProtocol]] - MCP differs by exposing typed external tool calls.
- [[AIApplicationFramework]] - frameworks may combine prompt templates, tools, memory, and retrieval into application workflows.
- [[AIAgentCollaboration]] - coding-agent collaboration can use Skills to shape how agents reason with users.
- [[SpecDrivenAgentDevelopment]] - specs are durable inputs that skills can consume during execution.
- [[BottleneckAwareAICoding]] - focused skills help address SDLC bottlenecks rather than only code typing.
- [[LLMAgentStages]] - runtime-free skill distribution presumes a client already operating at the general-OS stage.
- [[BashAsMetaTool]] - a script-capable shell is what lets a skill folder carry its own execution.
- [[AgentPermissionModel]] - runtime-enforced authority must backstop probabilistic safety instructions in skills.
- [[NanoClaw]] - uses reviewed skill merges to keep its installed code surface owner-selected and explicit.
