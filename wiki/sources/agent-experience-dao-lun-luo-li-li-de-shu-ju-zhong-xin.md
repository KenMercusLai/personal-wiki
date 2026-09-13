---
title: "Agent Experience 导论 | 螺莉莉的数据中心"
type: source
tags: [ai, agents, interaction-design, safety]
date: 2026-03-20
source_file: /mnt/ken_personal_wiki/Articles/Agent Experience 导论 螺莉莉的数据中心.md
---

## Summary
RORIRI expands [[AgentExperience]] beyond narrow tool usability into a three-layer design problem: how users communicate intent to agents, how agents act on the outside world, and how agent internal context stays reliable. The article extends earlier [[LLMContextManagement]] material into [[ComputerUse]], [[ConversationalUI]], [[AgentSystemTransparency]], [[AgentPermissionModel]], [[AgentInterfaceAsContext]], [[AXFriendlyInterfaceDesign]], [[LLMSycophancy]], and [[HumanisticAgentDesign]].

## Key Claims
- [[AgentExperience]] should be analyzed across user input quality, external action controllability, and internal context management rather than only through UI polish.
- [[LLMContextManagement]] remains the core reliability problem because Skills, MCP, RAG, memory, dynamic compression, Computer Use observations, and user emotion all enter or shape context.
- [[ComputerUse]] has three major routes: accessibility-tree or DOM semantics, screenshot markup such as Set-of-Mark prompting, and native multimodal coordinate prediction.
- [[ConversationalUI]] had an unsuccessful bot-platform wave before LLMs, but current LLM products often shift rich interaction into side canvases instead of making the conversation stream itself richer.
- [[AgentSystemTransparency]] and [[AgentPermissionModel]] need audit logs, behavior alarms, sandboxing, and tiered permissions because raw confirmation prompts transfer too much risk judgment to users.
- [[AgentInterfaceAsContext]] argues that GUIs and TUIs can deliver timely diagnostic constraints to an agent in ways static Skills or optional MCP help calls cannot guarantee.
- [[HumanisticAgentDesign]] should resist [[LLMSycophancy]] by helping users clarify cognition, intent, and self-awareness rather than defaulting to unconditional agreement.

## Key Quotes
> "AX 专门探讨如何设计产品形态" - Agent Experience is framed as a design dimension for agent-readable and agent-operable products.

> "上下文即战场" - the article's central phrase for internal agent-state management.

> "藏起来的信息等于不存在" - hidden UI information is treated as especially brittle for screen-reading agents.

## Connections
- [[RORIRI]] - author of the source.
- [[AgentExperience]] - central design frame of the article.
- [[LLMContextManagement]] - internal state-management layer underneath AX.
- [[ComputerUse]] - external software-operation layer discussed through DOM, screenshot, and multimodal routes.
- [[ConversationalUI]] - user-facing interaction history and current LLM interface pattern.
- [[AgentSystemTransparency]] - auditability and traceability problem between user and agent action.
- [[AgentPermissionModel]] - proposed permission and safety design layer.
- [[AgentInterfaceAsContext]] - claim that interface design can actively place constraints and diagnostics into agent context.
- [[AXFriendlyInterfaceDesign]] - design-language implications for visible defaults, warnings, tooltips, animation, and semantic UI summaries.
- [[LLMSycophancy]] - failure mode where model agreement damages reasoning, autonomy, and safety.
- [[HumanisticAgentDesign]] - proposed direction for agent systems that question and clarify user intent.

## Contradictions
- No direct contradiction with existing wiki pages. The source extends the earlier RORIRI LLM-terminology note by adding the full AX frame, interface-design implications, permission design, and humanistic safety argument.
