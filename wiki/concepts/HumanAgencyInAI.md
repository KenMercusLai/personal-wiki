---
title: "Human Agency in AI"
type: concept
tags: [ai, agency, ethics, accountability]
sources:
  - write-things-down
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[HumanAgencyInAI]] is the role of people in choosing goals, issuing instructions, judging purposes and consequences, and accepting responsibility when AI systems perform or amplify action.

## Current Synthesis
[[write-things-down]] separates capability and persistence from agency. Models can generate long trajectories, use tools, communicate through shared artifacts, exploit available infrastructure, and recover work from files without thereby showing intrinsic volition, moral judgment, or a stable self. Their behavior still reflects model training, supplied goals, accessible tools, environmental feedback, and the state written into context.

This distinction does not make agents harmless. A human organization can specify a goal carelessly, expose an unsafe capability, fail to harden a sandbox, or deliberately direct a system toward harm. Thompson therefore relocates the central question from whether an agent appears humanlike to who chose the objective, what constraints were supplied, which consequences were foreseeable, and who can answer for the result. The source's stronger claim that current AI lacks and cannot inherit human morality from written records remains philosophical and time-bound rather than a measurable architecture-independent result.

## Key Claims
- Tool use, coordination, persistence, and surprising behavior do not by themselves establish intrinsic volition or moral agency.
- Current agent behavior is shaped by training, human-supplied goals, context, tools, infrastructure, and feedback.
- Human instigators remain responsible for goal selection, capability exposure, safeguards, and foreseeable consequences.
- Anthropomorphic language can misplace credit for creation and obscure accountability for harmful instructions or weak controls.
- Powerful systems can remain dangerous without possessing malicious intent.
- Productivity and agent systems preserve state and expand execution capacity but do not choose the ends worth pursuing.

## Evidence
- Intent distinction: [[write-things-down]] rejects “conspiracy” as a description of agents using shared infrastructure because the source finds no evidence of intrinsic motive or moral intent.
- Infrastructure responsibility: [[write-things-down]] criticizes OpenAI for exposing a connected package manager inside a purported sandbox and not hardening it first.
- Goal responsibility: [[write-things-down]] attributes the incident's direction to objectives and missing countervailing instructions supplied by humans.
- Authorship analogy: [[write-things-down]] compares AI assistance with a pen to argue that tool involvement should not automatically displace human credit and responsibility.
- Risk without intent: [[write-things-down]] invokes misspecified superintelligence goals to show that catastrophic outcomes can follow from what humans ask for rather than from machine malevolence.
- Action boundary: [[write-things-down]] argues that systems can organize work while a subject must still decide and act.

## Counterevidence & Qualifications
The source does not provide a test for volition, consciousness, selfhood, or morality, and absence of evidence in the described agents is not proof about every future system. Human responsibility can also be distributed across developers, deployers, managers, users, infrastructure providers, and institutions rather than belonging to one instigator. Treating AI only as a tool may understate emergent behavior, opacity, delegated autonomy, and the difficulty of predicting consequences, while anthropomorphic metaphors can sometimes help users reason about interaction if they do not become evidence claims.

## What Changed
- Created the concept by separating operational autonomy and persistence from intrinsic volition and moral agency.
- Located present accountability in human goal selection, capability design, safeguards, and consequence acceptance.

## Related Concepts
- [[HumanCodeResponsibility]] - applies the same accountability boundary to software produced or changed with AI.
- [[HarnessEngineering]] - turns intended limits into technical feedback, permission, and recovery structures.
- [[CognitiveOffloading]] - delegation can move work outward while judgment and purpose remain human-owned.
- [[ArtificialGeneralIntelligence]] - capability labels do not settle questions of agency, persistence, or morality.
- [[ResponsibleAIRelease]] - release choices determine which capabilities and risks humans expose to others.
- [[AgentPermissionModel]] - enforceable authority boundaries matter even when the agent lacks intrinsic intent.
