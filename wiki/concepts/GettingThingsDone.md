---
title: "Getting Things Done"
type: concept
tags: [productivity, task-management, attention]
sources:
  - write-things-down
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[GettingThingsDone]] (GTD) is [[DavidAllen]]'s productivity method for capturing unresolved commitments in a trusted external system, clarifying next actions, and reviewing reminders when they can guide action.

## Current Synthesis
[[write-things-down]] presents GTD first as an attention-management philosophy. Incomplete commitments consume limited working memory and recur as distracting open loops; trusted capture lets a person stop rehearsing them, provided the system will be reviewed. Contextual reminders, inboxes, next actions, and ticklers then connect stored commitments to moments when something can actually be done.

The article extends the pattern from people to agent workflows. Thompson's assistants and bots use status boards, future reminders, daily briefings, queues, and next-action dialogs to preserve state and reduce interruption. This analogy is operational rather than cognitive proof: external records can support continuity, but neither a perfectly organized task system nor an agent harness guarantees judgment, motivation, execution, or completion.

## Key Claims
- Unresolved commitments compete for limited attention when they are retained only in working memory.
- Capture is useful only when the destination is trusted and reviewed.
- Reminders should surface in a context where action is possible.
- Inbox, next-action, tickler, queue, and status-board structures turn vague obligations into reviewable state.
- Human assistants and software agents can operate parts of the system on another person's behalf.
- Organization supports execution but cannot replace the decision and effort to act.

## Evidence
- Working-memory argument: [[write-things-down]] quotes Allen's comparison between incomplete commitments and overloaded computer RAM.
- Trusted bucket: [[write-things-down]] emphasizes writing an open loop into a system known to receive later review.
- Contextual recall: [[write-things-down]] uses Allen's dead-flashlight example to distinguish spontaneous reminders from useful reminders.
- Delegated operation: [[write-things-down]] describes assistants maintaining Thompson's inbox and OmniFocus state.
- Agent implementation: [[write-things-down]] describes status boards, ticklers, daily briefings, project queues, and next-action dialogs implemented through agents and deterministic bot logic.
- Execution limit: [[write-things-down]] closes with the failure of a productivity-system book project to argue that systems still require action.

## Counterevidence & Qualifications
The source supplies personal testimony and book excerpts, not a controlled evaluation of GTD. Trusted review itself consumes time, systems can become unwieldy, and delegation depends on resources, shared understanding, privacy, and reliable handoff. The article's assistant and bot examples are unusually resource-intensive and may not transfer to people without comparable autonomy or technical capacity. External capture can reduce rehearsal without resolving priority conflict, motivation, overload, or the underlying work.

## What Changed
- Created the concept around trusted capture, contextual reminders, delegated maintenance, and the system-versus-action boundary.

## Related Concepts
- [[CognitiveOffloading]] - GTD externalizes unresolved commitments from working attention.
- [[PersonalProductivity]] - GTD is one structured method for attention and task management.
- [[AgentMemory]] - file-backed agent state applies a similar persistence pattern outside the active context.
- [[HarnessEngineering]] - deterministic reminders and boards operationalize parts of the method around agents.
- [[HumanAgencyInAI]] - a system can preserve and surface work without choosing the human purpose behind it.
