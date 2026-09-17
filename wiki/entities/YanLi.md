---
title: "Yan Li"
type: entity
tags: [writer, ai, agents, blogger]
sources:
  - yan-li-how-llm-agents-became-what-they-look-like-in-2026
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Overview
[[YanLi]] is the author of the blog post "How LLM Agents Became What They Look Like in 2026?", a practitioner essay that reads agent architecture as a staged history and argues for a general operating-system layer over protocol-specific tool integrations.

## Current Profile
The essay presents Li as a practitioner-reasoner rather than a neutral surveyor. It walks a four-stage history - structured output, tool calling, [[ModelContextProtocol]], then bash and filesystem - and, unusually for a review piece, ends each stage on an opinion: MCP "is an over-engineered approach that ultimately failed to become the universal solution", while [[BashAsMetaTool]] is "potentially the only tool an agent needs". The writing pairs a concrete engineering diagnosis with a product-forecast claim. The diagnosis is that intermediate artifacts cannot return to the model in one step, so tool combinations multiply, which is why an [[AgentFilesystem]] is needed. The forecast is that agent-skills, a file-based dynamic-prompt-injection protocol, will be adopted more widely than MCP because it needs no runtime. Li also reasons about training progress as a design variable, expecting separated thinking/output, RL on structured JSON and coding, and larger contexts to make ReAct loops and chain-of-thought prompting less necessary, and closes by listing the deployment constraints that keep agents from being universal.

## Key Characteristics
- Writes practitioner essays about LLM agent architecture rather than model benchmarks or vendor documentation.
- Organizes the field into an explicit four-stage history and labels a next stage.
- States opinions alongside descriptions, including a negative verdict on MCP's universality.
- Argues from engineering mechanism, such as artifact round-tripping and tool-combination growth, rather than from product marketing.
- Treats model training progress as something that can obsolete surrounding workflow scaffolding.
- Reasons about distribution and adoption, notably the file-based, runtime-free packaging of agent-skills.
- Frames remaining limits in product terms: latency, reproducibility, privacy and cost, and unmet multimodal demand.

## Evidence
- Staged history: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] structures the essay as Stage 1 structured output, Stage 2 tool calling, Stage 3 MCP, Stage 4 bash/filesystem/OS, and "Stage NEXT".
- MCP verdict: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] states that MCP is over-engineered and failed to become the universal solution.
- Meta-tool claim: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] argues bash is potentially the only tool an agent needs.
- Mechanism over marketing: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] derives the filesystem stage from the fact that intermediate artifacts cannot be returned to the LLM in a single step.
- Training as design variable: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] expects thinking/output separation and RL for JSON and coding to reduce the need for ReAct and CoT prompting.
- Adoption reasoning: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] argues agent-skills will spread because it is a self-contained folder requiring no runtime or dependencies.
- Deployment limits: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] lists latency versus quality, reproducibility, privacy and cost versus quality, and multimodal demand as the outstanding problems.

## Qualifications
This profile rests on a single source and should not be generalized to Li's other writing or to a stable editorial position. The essay is argumentative rather than empirical: its MCP verdict, meta-tool claim, and adoption forecast are stated without adoption data, benchmarks, or comparisons against typed tools on reliability and permissioning.

## What Changed
- Created the entity page for the essay's author and his stage-model argument.

## Relationships
- [[LLMAgentStages]] - Li is the author of the staged agent history the wiki now carries.
- [[BashAsMetaTool]] - his central tooling argument.
- [[AgentFilesystem]] - his proposed fix for artifact round-tripping.
- [[AgentDeploymentTradeoffs]] - his closing list of constraints on agent deployment.
- [[ModelContextProtocol]] - the protocol he argues against as a universal solution.
- [[LLMToolingSkills]] - the agent-skills distribution argument he makes.
