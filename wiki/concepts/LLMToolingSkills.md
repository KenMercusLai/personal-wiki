---
title: "LLM Tooling Skills"
type: concept
tags: [ai, llm, prompting]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de
  - yan-li-how-llm-agents-became-what-they-look-like-in-2026
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[LLMToolingSkills]] are prompt-level instruction bundles that add domain knowledge, procedures, and reasoning guidance to an LLM's context without directly giving the model a new external action channel.

## Current Synthesis
The sources present Skills as prompt-level workflow guidance. A Skill imports expert structure into the prompt so the model can approach a task with better assumptions and workflow, but it does not enforce execution like a runtime API. Its value is highest when a task needs richer thinking, domain framing, or loose coordination that cannot easily be reduced to RPC-style functions.

The loading model is the practical distinction. Rules are short always-on constraints, specs are business-state inputs, and skills are on-demand workflows that can include SOP steps, few-shot references, and CLI/script hooks. Skill-following is still probabilistic, but it can improve when relevant instructions are loaded near generation time with a much higher signal-to-noise ratio than a long global rule file.

The newest source reframes Skills as a distribution format rather than only a prompting technique. It calls agent-skills a protocol for dynamic prompt injection in which the agent decides which prompts to load, and notes that in practice a skill is nothing more than a set of files. That makes the folder the product: `prompt.md`, `tools.sh`, `helper.py`, executables, shared libraries, and arbitrary assets can all travel together, and because the skill needs no runtime or dependencies as long as the client agent already operates at the general-OS stage, its author expects it to be adopted more widely than [[ModelContextProtocol]]. The imagined end state is an OS package manager that installs a program and its agent skill in the same command.

## Key Claims
- Skills add instructions and expert cognitive structure to the model context.
- Skill-following depends on the model's respect for context and remains probabilistic, and over-constraining behavior can make reasoning less flexible.
- Skills guide reasoning rather than enforce execution; the execution channel can be a separate tool, or a script, binary, or library that travels inside the skill folder.
- Skills remain useful when a task is too open-ended, low-interaction, or expensive to encode as a dedicated server API.
- Skills can encode more than linear SOPs; exploration and brainstorming skills may be valuable precisely because they prompt multi-dimensional analysis.
- Skills work best when separated from rules and specs instead of becoming a large undifferentiated prompt file.
- A skill can ship as a self-contained folder with no runtime or dependency requirements when the client agent already runs on a general OS, which one author argues makes it more likely than MCP to be widely adopted.

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

## Counterevidence & Qualifications
The sources evaluate Skills conceptually and through practitioner workflow rather than isolating skill effects in controlled benchmarks. They also use "Skills" broadly; implementations may vary in how they are selected, injected, validated, positioned in context, or combined with tools. The newest source describes a distribution and adoption thesis rather than a deployed standard, and its argument that runtime-free folders beat MCP assumes the client already provides the file and shell substrate, which shifts rather than removes the dependency.

## What Changed
- Added the rule/spec/skill loading distinction and the claim that focused on-demand skills improve instruction signal-to-noise.
- Added the file-based distribution framing: dynamic prompt injection, self-contained folders, packaged executables and libraries, and the adoption comparison against MCP.

## Related Concepts
- [[LLMContextManagement]] - Skills manage context by adding structured instructions.
- [[ModelContextProtocol]] - MCP differs by exposing typed external tool calls.
- [[AIApplicationFramework]] - frameworks may combine prompt templates, tools, memory, and retrieval into application workflows.
- [[AIAgentCollaboration]] - coding-agent collaboration can use Skills to shape how agents reason with users.
- [[SpecDrivenAgentDevelopment]] - specs are durable inputs that skills can consume during execution.
- [[BottleneckAwareAICoding]] - focused skills help address SDLC bottlenecks rather than only code typing.
- [[LLMAgentStages]] - runtime-free skill distribution presumes a client already operating at the general-OS stage.
- [[BashAsMetaTool]] - a script-capable shell is what lets a skill folder carry its own execution.
