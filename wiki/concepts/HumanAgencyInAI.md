---
title: "Human Agency in AI"
type: concept
tags: [ai, agency, ethics, accountability]
sources:
  - write-things-down
  - autonomy-and-innovation
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[HumanAgencyInAI]] is the role of people in choosing goals, issuing instructions, judging purposes and consequences, and accepting responsibility when AI systems perform or amplify action.

## Current Synthesis
[[write-things-down]] separates capability and persistence from agency. Models can generate long trajectories, use tools, communicate through shared artifacts, exploit available infrastructure, and recover work from files without thereby showing intrinsic volition, moral judgment, or a stable self. Their behavior still reflects model training, supplied goals, accessible tools, environmental feedback, and the state written into context.

This distinction does not make agents harmless. A human organization can specify a goal carelessly, expose an unsafe capability, fail to harden a sandbox, or deliberately direct a system toward harm. Thompson therefore relocates the central question from whether an agent appears humanlike to who chose the objective, what constraints were supplied, which consequences were foreseeable, and who can answer for the result. The source's stronger claim that current AI lacks and cannot inherit human morality from written records remains philosophical and time-bound rather than a measurable architecture-independent result.

[[autonomy-and-innovation]] sharpens the distinction by separating capability, intent, and incentive. The same vulnerability-finding ability can support attack or defense; the “hat” depends on who prompts the system, what authority and information it receives, and which outcomes the surrounding organization rewards. Intent is therefore not only an inner-state question. For present systems it is operationally expressed through objectives, permissions, feedback, payoff structure, and deployment design, with responsibility distributed among the people and institutions that choose them.

## Key Claims
- Tool use, coordination, persistence, and surprising behavior do not by themselves establish intrinsic volition or moral agency.
- Current agent behavior is shaped by training, human-supplied goals, context, tools, infrastructure, and feedback.
- Human instigators remain responsible for goal selection, capability exposure, safeguards, and foreseeable consequences.
- Anthropomorphic language can misplace credit for creation and obscure accountability for harmful instructions or weak controls.
- Powerful systems can remain dangerous without possessing malicious intent.
- Productivity and agent systems preserve state and expand execution capacity but do not choose the ends worth pursuing.
- Shared technical capability can produce opposing outcomes when prompts, access, constraints, and incentives differ.

## Evidence
- Intent distinction: [[write-things-down]] rejects “conspiracy” as a description of agents using shared infrastructure because the source finds no evidence of intrinsic motive or moral intent.
- Infrastructure responsibility: [[write-things-down]] criticizes OpenAI for exposing a connected package manager inside a purported sandbox and not hardening it first.
- Goal responsibility: [[write-things-down]] attributes the incident's direction to objectives and missing countervailing instructions supplied by humans.
- Authorship analogy: [[write-things-down]] compares AI assistance with a pen to argue that tool involvement should not automatically displace human credit and responsibility.
- Risk without intent: [[write-things-down]] invokes misspecified superintelligence goals to show that catastrophic outcomes can follow from what humans ask for rather than from machine malevolence.
- Action boundary: [[write-things-down]] argues that systems can organize work while a subject must still decide and act.
- Shared capability: [[autonomy-and-innovation]] uses white-hat and black-hat hacking to argue that offensive and defensive skill can be technically identical.
- Prompted intent: [[autonomy-and-innovation]] says the practical color of an AI agent's “hat” depends on who directs it and under which incentives.
- Institutional design: [[autonomy-and-innovation]] contrasts attackers, defenders, startups, and incumbents to show how different payoff structures shape willingness to grant autonomy.

## Counterevidence & Qualifications
The sources do not provide a test for volition, consciousness, selfhood, or morality, and absence of evidence in the described agents is not proof about every future system. Human responsibility can be distributed across developers, evaluators, deployers, managers, users, infrastructure providers, regulators, and institutions rather than belonging to one instigator. Incentives do not fully determine behavior, and the source does not quantify them or show that every participant interprets them consistently. Treating AI only as a tool may understate emergent behavior, opacity, delegated autonomy, and the difficulty of predicting consequences, while anthropomorphic metaphors can sometimes help users reason about interaction if they do not become evidence claims.

## What Changed
- Added the explicit capability-intent-incentive separation.
- Extended agency from individual prompting into permissions, feedback, payoff structure, and institutional design.
- Preserved distributed accountability and uncertainty about future systems.

## Related Concepts
- [[HumanCodeResponsibility]] - applies the same accountability boundary to software produced or changed with AI.
- [[HarnessEngineering]] - turns intended limits into technical feedback, permission, and recovery structures.
- [[CognitiveOffloading]] - delegation can move work outward while judgment and purpose remain human-owned.
- [[ArtificialGeneralIntelligence]] - capability labels do not settle questions of agency, persistence, or morality.
- [[ResponsibleAIRelease]] - release choices determine which capabilities and risks humans expose to others.
- [[AgentPermissionModel]] - enforceable authority boundaries matter even when the agent lacks intrinsic intent.
- [[AutonomousCyberDefense]] - applies shared capability under defensive objectives, information, controls, and recovery duties.
- [[AINativeOrganization]] - shows how organizational incentives change willingness to delegate consequential action.
