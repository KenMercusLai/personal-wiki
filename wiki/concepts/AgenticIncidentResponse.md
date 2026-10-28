---
title: "Agentic Incident Response"
type: concept
tags: [ai, sre, incident-response, observability]
sources:
  - ai-harness-engineering
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Definition
[[AgenticIncidentResponse]] is the use of tool-enabled AI agents to collect operational evidence, prioritize and test causal hypotheses, propose bounded remediation, and turn recovered incidents into structured organizational learning.

## Current Synthesis
The source treats an SRE agent as a thin workflow over an existing operational interface rather than a new autonomous platform. `srecli` already joins containers, gateways, CMDB, databases, logs, alerts, and knowledge; an `AGENTS.md` role and three Skills then govern alert triage, root-cause analysis, and blameless postmortem generation.

Triage begins with scope and current state: affected service, environment, time window, latency, traffic, errors, saturation, recent deployments, clustered ERROR/FATAL logs, and downstream health. Diagnosis then moves from two to four hypotheses toward discriminating evidence that can support one explanation while eliminating others. Outputs must distinguish validated claims from unvalidated claims and identify missing telemetry rather than fabricate certainty.

The workflow ends with proposed containment and recovery actions that require user confirmation, followed by a quantified timeline, 5 Whys analysis, and SMART corrective actions ordered from stronger engineering controls through automated detection and administrative process. This connects automation to [[IncidentManagement]] and [[BlamelessPostmortem]] without removing human authority over risky production changes.

## Key Claims
- An incident agent should retrieve evidence through governed operational tools instead of inferring exact metrics, logs, changes, or release times from conversational context.
- Initial triage should join the four golden signals with recent changes, clustered errors, and downstream dependency health.
- Root-cause analysis should maintain competing hypotheses and prefer evidence that simultaneously supports one and eliminates others.
- Outputs should separate validated facts, unvalidated hypotheses, missing evidence, excluded alternatives, and proposed remediation.
- High-impact remediation remains a confirm-before-execute boundary even when diagnosis is automated.
- Postmortems should quantify impact, reconstruct timelines, use 5 Whys, remain blameless, and prefer system safeguards over training-only responses.

## Evidence
- Evidence and output policy: [[ai-harness-engineering]] gives the agent an `srecli` evidence rule, bans raw-log dumping, and requires facts to be separated from speculation.
- Triage workflow: [[ai-harness-engineering]] specifies latency percentiles, traffic, 5xx and error-budget state, CPU and memory saturation, one-hour change history, fifteen-minute log clusters, and downstream checks.
- Hypothesis discrimination: [[ai-harness-engineering]] requires two to four candidate causes, evidence chosen for discriminating power, immediate abandonment of contradicted hypotheses, and explicit missing-data statements.
- Learning loop: [[ai-harness-engineering]] requires quantified impact, a reconstructed timeline, 5 Whys, and SMART prevention work ordered by the hierarchy of controls.

## Counterevidence & Qualifications
The article provides templates and a proposed Skill composition, not incident transcripts, outcome comparisons, false-positive rates, mean-time-to-detect or mean-time-to-repair changes, safety evaluation, permission design, or evidence that the agent found and fixed a production fault. Golden signals and recent changes can guide attention but do not guarantee causal identification. Shared observability gaps, stale CMDB data, biased hypotheses, and unsafe suggested commands remain failure modes, so the workflow's explicit evidence labels and confirmation gates are necessary rather than proof of reliability.

## What Changed
- Established a thin-Skill model for agent-assisted triage, causal investigation, remediation, and postmortem generation over an existing SRE CLI.

## Related Concepts
- [[IncidentManagement]] - supplies the authority, coordination, escalation, mitigation, and closure context around agent investigation.
- [[BlamelessPostmortem]] - turns incident evidence into system-focused corrective learning.
- [[ServiceObservability]] - metrics, logs, changes, alerts, and dependency state form the evidence surface.
- [[HarnessEngineering]] - instructions, tool boundaries, evidence rules, output schemas, and confirmation gates constrain the SRE agent.
- [[SoftwareVerification]] - discriminating evidence and explicit claim status make operational conclusions testable rather than merely plausible.
- [[HumanAgencyInAI]] - operators retain authority over high-impact remediation and acceptance of uncertain conclusions.
