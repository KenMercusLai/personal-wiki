---
title: "Agent Interface As Context"
type: concept
tags: [ai, agents, interface-design, context]
sources:
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[AgentInterfaceAsContext]] is the idea that GUI and TUI design can deliberately place timely constraints, diagnostics, warnings, and workflow structure into the context an AI agent observes while acting.

## Current Synthesis
RORIRI argues that interfaces are not just human-facing surfaces in agentic systems; they can be active context-delivery mechanisms. Static Skills can explain general rules before reasoning starts, and MCP can return data after a function call, but neither guarantees that the right diagnostic appears at the right moment. A well-designed interface can make process constraints, quality checks, and domain warnings visible exactly where the agent is acting.

## Key Claims
- Interface design can decide what information enters the agent's context, when it appears, and how it is framed.
- Static prompt instructions cannot reliably inject timely process diagnostics during an unfolding task.
- Optional help functions or tool calls cannot guarantee that the model asks for the needed guidance.
- Domain software can encode professional quality-control practice into visible workflow states.
- Statistical analysis is a strong example because correct code execution does not guarantee valid analysis or interpretation.
- GUIs and TUIs can therefore be agent-safety and domain-reasoning infrastructure, not just presentation layers.

## Evidence
- Context-delivery question: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] asks who decides which information appears in LLM context during inference, at what time, and in what form.
- Statistics example: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says LLM-written R or Python can run while still making data-cleaning, method, or interpretation errors.
- QC software example: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] points to SPSS, Jamovi, and Minitab as software that can surface assumptions, diagnostics, and warnings through the analysis flow.
- Skill limit: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says Skills are static and front-loaded rather than dynamically placed in the moment.
- MCP limit: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says MCP can return data but cannot guarantee the model will call the right help function when needed.

## Counterevidence & Qualifications
The source does not claim every warning should always be visible or that interfaces can replace verification. The design problem is balancing useful contextual defaults against overwhelming users and agents with irrelevant information.

## What Changed
- Created the concept page for interfaces as active context-delivery mechanisms for agents.

## Related Concepts
- [[AgentExperience]] - interface-as-context spans all three AX layers.
- [[LLMContextManagement]] - interface content becomes part of model context.
- [[AXFriendlyInterfaceDesign]] - UI patterns must make important state visible to agents.
- [[StatisticalModelThinking]] - statistical diagnostics are a domain example of needed context.
- [[UXResearchInformationDesign]] - both treat information placement as an argument or reasoning aid.
- [[ModelContextProtocol]] - tool calls complement but do not replace interface-delivered context.
