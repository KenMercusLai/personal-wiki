---
title: "Oracle Routing"
type: concept
tags: [ai, agents, verification, human-in-the-loop]
sources:
  - duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[OracleRouting]] is the practice of routing unresolved verification or intent questions from automated agent pipelines to a human decision-maker only when automated gates cannot safely decide.

## Current Synthesis
The source uses oracle routing to handle a core limit in AI-agent systems: user intent is not directly observable. Specs, plans, designs, and code are projections of that intent, and each projection can lose information. Automated gates can test consistency between projections, but when the projection itself is ambiguous or wrong, a path back to the human is the only way to recover source-level intent.

Oracle routing also keeps human review scalable. LLM reviewers classify failures into automatically fixable issues versus questions requiring human judgment, so people are not forced to review every artifact in the pipeline. Over time, repeated human decisions can migrate into reviewer rules or deterministic checks.

## Key Claims
- User intent is not observable directly by the agent pipeline.
- Verification gates can check projection consistency but cannot prove fidelity to the user's real intent.
- Human escalation is necessary when ambiguity, product judgment, or architectural choice cannot be resolved from artifacts.
- LLM reviewers can route issues by deciding whether a failure is auto-fixable or needs human judgment.
- Repeated human decisions can be encoded into cheaper rules, moving the boundary of automation.

## Evidence
- Intent boundary: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] states that intent exists in the user's head and every artifact is a lossy projection.
- Consistency limit: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] says gates can check whether code matches design or design matches plan, but not whether the result matches true intent.
- Routing role: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] describes LLM reviewers routing issues to automatic repair or human decision.
- Boundary migration: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] says recurring stochastic or human judgments can become deterministic checks or LLM rules.

## Counterevidence & Qualifications
Oracle routing reduces human review load but does not eliminate human responsibility. It also depends on the reviewer's ability to recognize uncertainty; a reviewer that confidently misroutes ambiguous intent can hide rather than solve the problem.

## What Changed
- Created the concept page from the multi-agent distributed-systems source.

## Related Concepts
- [[TrustTopology]] - oracle routing is the human-escalation mechanism inside the topology.
- [[SoftwareVerification]] - verification gates need escalation when checks cannot decide semantic intent.
- [[HumanCodeResponsibility]] - humans remain responsible for final intent and risk judgments.
- [[AIAgentCollaboration]] - collaboration includes knowing when the agent must ask rather than continue.
- [[HarnessEngineering]] - routing rules are part of the scaffold around agent work.
