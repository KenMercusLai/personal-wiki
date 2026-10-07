---
title: "Yan Li"
type: entity
tags: [writer, speaker, ai, agents, blogger]
sources:
  - yan-li-how-llm-agents-became-what-they-look-like-in-2026
  - ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[YanLi]] is a practitioner-writer and PyCon China 2026 speaker whose essays explain the evolution, composition, runtime, state, and lifecycle of LLM agents through operating-system and software-distribution concepts.

## Current Profile
Li treats agent architecture as a systems problem rather than a model feature. The earlier essay organizes the field into structured output, tool calling, [[ModelContextProtocol]], and an operating-system stage built from [[BashAsMetaTool]] and [[AgentFilesystem]]. It is explicitly argumentative: MCP is judged too specialized to be universal, while shell and filesystem provide more general execution and artifact handling.

The newer conference-derived essay replaces the historical sequence with a static decomposition: agent equals context plus runtime. History and instructions determine what the model can use; tools and state management determine what it can do and preserve. Li then follows this decomposition into packaging and lifecycle questions. Agent Skills are high-cohesion bundles but lack a standard boundary among code, configuration, and mutable data; whole-sandbox CoW snapshots are portable but coarse; and a stateful session can define one agent even as steering and asynchronous commands make closed turns an incomplete action model.

Across both essays, Li's characteristic move is to accept a mechanism's usefulness and then identify the missing systems boundary: MCP adds a runtime but not a universal integration layer, Skills distribute files but not a complete state policy, and CoW snapshots reproduce environments but not necessarily independently portable components. The proposed direction repeatedly returns to OS precedents such as shells, filesystems, package managers, XDG conventions, isolation, and explicit lifecycle operations.

## Key Characteristics
- Writes practitioner analyses of LLM agent architecture rather than model benchmarks or vendor documentation.
- Explains agent systems through staged histories and compact decompositions.
- Uses operating-system primitives and conventions as the main design vocabulary for execution, storage, packaging, and state.
- Distinguishes descriptive mechanism from opinionated judgments about universality, adoption, and design direction.
- Traces abstractions to unresolved ownership and granularity boundaries.
- Treats model progress, steering, and asynchronous execution as forces that can obsolete surrounding scaffolding.
- Frames agent-platform design as a conflict between operational freedom and manageability.

## Evidence
- Staged history: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] structures agent development as structured output, tool calling, MCP, bash/filesystem/OS, and a future GUI stage.
- OS runtime: both [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] and [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] center shell and filesystem as general execution and storage primitives.
- Architectural decomposition: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] defines agent as context plus runtime and separates history, instructions, execution, and state management.
- Boundary analysis: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] identifies code/configuration/data ambiguity in Skills and component-level limits in whole-filesystem CoW.
- Lifecycle reasoning: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] defines one agent through a stateful session and uses steering plus asynchronous commands to challenge turn-only modeling.
- Opinionated forecasts: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] predicts wider Skill adoption than MCP, while the newer essay suggests agent platforms may repeat the standardization path of OS distributions.
- Freedom-management conflict: [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] argues that collaboration, sharing, and tool isolation inevitably constrain OS-level agent freedom.

## Qualifications
The profile rests on two related practitioner essays from 2026, one of them derived from a conference talk. They reveal a coherent architectural perspective but do not establish Li's broader biography, employment, implementation record, or stable position beyond these texts. Strong claims about MCP, Skill adoption, turn replacement, and a repeated OS-standardization path are not supported by comparative benchmarks or adoption data.

## What Changed
- Broadened Li's profile from a staged-history author to a systems thinker focused on runtime state and lifecycle.
- Added the recurring freedom-versus-manageability tension and OS-standardization analogy.
- Added PyCon China 2026 speaking context from the newer source.

## Relationships
- [[LLMAgentStages]] - Li authored the staged history synthesized by this concept.
- [[GenerativeAIAgentArchitecture]] - his newer context/runtime decomposition extends the wiki's architecture model.
- [[AgentLifecycleModel]] - his session, state-ownership, steering, and asynchronous-execution argument grounds this concept.
- [[BashAsMetaTool]] - his central general-execution argument.
- [[AgentFilesystem]] - his general storage substrate for artifacts and agent-owned state.
- [[LLMToolingSkills]] - his essays frame Skills as dynamic prompt injection and expose their packaging boundary.
- [[ModelContextProtocol]] - a useful runtime protocol he argues is not a universal state or integration solution.
