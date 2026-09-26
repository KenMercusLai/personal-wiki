---
title: "Vibe Coding"
type: concept
tags: [ai, software-engineering, developer-tools]
sources:
  - yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou
  - du-li-kai-fa-zhe-fen-xiang-ai-coding-de-mi-jue-yi-huo-de-shou-quan
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
  - blog-guangzhengli-vibe-coding-and-context-coding
  - write-less-code-be-more-responsible-orhuns-blog
  - hu-yuan-ming-wo-gei-10-ge-claude-code-da-gong
  - blog-peter-steinberger-shipping-at-inference-speed
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[VibeCoding]] is an AI-assisted software work mode whose original Karpathy sense meant steering code almost entirely by conversation and visible results while barely reading or hand-editing the code; in broader wiki usage it also covers speed-amplified coding-agent workflows that need planning, context, review, and verification.

## Current Synthesis
The sources frame vibe coding as a real shift in software iteration speed and human role. The developer spends less time hand-writing boilerplate and more time setting direction, choosing task boundaries, managing context, reviewing generated changes, and verifying behavior. That speed is double-edged: it can make product iteration dramatically faster, but it can also create competitive pressure, overlarge diffs, shallow understanding, context failure, unhealthy pace, and delayed project risk unless paired with small steps, tests, planning, and explicit human judgment. The independent-developer example adds a concrete positive pattern: natural-language instructions can behave like code when they are precise enough about files, interfaces, data flow, UI behavior, and acceptance criteria.

The mihomo-rust source shows a heavier version of vibe coding for large systems. Instead of one fast conversation, agent acceleration is organized through role separation, specs, ADRs, memories, milestone resets, and full CI. In this mode, "vibe" is not improvisation; it is high-throughput implementation inside a deliberately designed harness.

Guangzhengli adds a naming correction. The article argues that many debates confuse Karpathy's original no-review, throwaway-project vibe coding with broader AI-assisted programming. For maintainable software, the better label is [[ContextCoding]]: developers still use AI heavily, but the important work is managing context, rules, retrieval, tools, debugging signals, and verification rather than surrendering code ownership.

Parmaksız adds an open-source trust perspective and a compact behavioral boundary: do not “vibe code and commit.” His concern is not that AI use invalidates software, but that cheap creation makes it easier to publish projects whose maintainers do not fully understand the code or cannot guarantee safe future releases. His mixed workflow preserves AI leverage while reserving final quality judgment and selected enjoyable implementation work for the human.

Hu Yuanming supplies an extreme expert-user case close to the original no-review meaning: he deliberately avoids reading code beyond `CLAUDE.md`, runs multiple Claude Code sessions in parallel, and judges the system through task completion, tests, merges, and whether his private CEO tool works for him. The case shows how much infrastructure can sit underneath apparently effortless vibe coding—queues, worktrees, streamed logs, recovery rules, backups, persistent lessons, Plan Mode, and a custom control plane—but it does not resolve whether commit velocity or dispatch success produces maintainable software.

A second expert, low-code-reading case has a different operating shape. [[PeterSteinberger]] queues conversational work across one main project and several satellite projects, lets [[Codex]] spend substantial time inspecting repositories, keeps durable subsystem docs, reuses examples from neighboring codebases, and starts products with a CLI that the agent can execute and check. His account sharpens the bottleneck shift: implementation can become cheap enough that architecture, dependencies, system boundaries, product feel, inference time, and human attention dominate. It also sharpens the unresolved risk, because knowing the system map and checking behavior are not equivalent to reviewing the generated implementation.

## Key Claims
- Vibe coding's most visible effect is faster product iteration and lower scope cost, but local activity measures such as commits or agent completions do not by themselves establish delivery value.
- Command-line agents can produce a deeper vibe-coding experience than editor-bound AI when they understand and modify whole projects.
- Planning is useful for existing systems and architecture-sensitive work, but it may happen through an ordinary exploratory conversation rather than a separately restricted mode; prototypes may still benefit from faster implementation-first loops.
- Small, reviewable iterations and fine-grained natural-language implementation instructions usually beat large uncontrolled generations because they preserve understanding and rollback ability.
- Context windows, documentation, codebase exploration, compaction, and session boundaries become workflow constraints whose best handling can vary by model and task.
- Verification, human pace, and reviewability matter: accelerated tools should not eliminate compilation, tests, linting, thinking time, formal roles, specs, CI, or production responsibility.
- Pure no-review vibe coding is especially risky for non-programmers and public-software maintainers because security, subscription, API-key, database, comprehension, later-release, user-trust, and review failures can arrive faster than the builder can understand or safely maintain them.

## Evidence
- Iteration speed: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] says AI-assisted development can compress product work from days to hours and intensify competition.
- Tool shape: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] argues that editor AI keeps attention near a file or selected lines, while command-line agents can build project-level understanding.
- Planning fit: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] recommends Plan Mode for existing architecture and maintenance work, but allows faster prototyping when code quality and long-term maintenance matter less.
- Iteration control: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] reports that huge one-shot changes can become hard to inspect, debug, and salvage, while small steps aid control and learning.
- Risk postponement: [[du-li-kai-fa-zhe-fen-xiang-ai-coding-de-mi-jue-yi-huo-de-shou-quan]] argues that broad AI coding can leave developers with late-stage failures in code they cannot understand.
- Precise steering: [[du-li-kai-fa-zhe-fen-xiang-ai-coding-de-mi-jue-yi-huo-de-shou-quan]] shows prompts that name exact files, functions, callbacks, localization files, and reviewable change summaries.
- Context constraints: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] highlights context-window pressure, auto-compaction risk, subagents, task decomposition, plan documents, and new sessions as practical context-management tactics.
- Verification: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] recommends compile-test-lint loops, TDD, cross-review, version control, and modular work.
- Human boundary: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] warns that tools should serve people rather than force unsustainable acceleration.
- Structured acceleration: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] uses Agent Team roles, spec documents, memory rules, milestone respawn, and layered tests for a large Rust port.
- Original meaning: [[blog-guangzhengli-vibe-coding-and-context-coding]] uses the inspected Karpathy screenshot to ground vibe coding in a no-review, conversational, result-steered workflow suitable mostly for throwaway weekend projects.
- Naming distinction: [[blog-guangzhengli-vibe-coding-and-context-coding]] argues that disciplined AI-assisted programming is better understood as [[ContextCoding]] than as vibe coding.
- Non-programmer risk: [[blog-guangzhengli-vibe-coding-and-context-coding]] uses Leo's March 2025 screenshots to show how a Cursor-built SaaS with no hand-written code quickly ran into API-key exhaustion, subscription bypass, database abuse, and shutdown.
- Expert leverage: [[blog-guangzhengli-vibe-coding-and-context-coding]] contrasts the Leo case with @levelsio's AI-built flight-simulator example, where the builder's prior programming experience made takeover and repair more plausible.
- Open-source trust: [[write-less-code-be-more-responsible-orhuns-blog]] describes the unease of adopting an impressive but visibly vibe-coded project without confidence that a future release will be safe or maintainable.
- Workflow boundary: [[write-less-code-be-more-responsible-orhuns-blog]] rejects unreviewed commits while retaining AI for tedious or slow work and applying a final human quality pass.
- Expert no-review case: [[hu-yuan-ming-wo-gei-10-ge-claude-code-da-gong]] describes parallel Claude Code workers, a web task center, automated integration, and a personal application whose author intentionally does not inspect most generated code.
- Hidden infrastructure: [[hu-yuan-ming-wo-gei-10-ge-claude-code-da-gong]] documents worktree isolation, task state, streamed logs, merge and test recovery, `PROGRESS.md`, database backups, and Plan Mode beneath the fast conversational surface.
- Bottleneck shift: [[blog-peter-steinberger-shipping-at-inference-speed]] says coding throughput is increasingly limited by inference time, hard thinking, system design, dependency choice, and the author's own attention rather than typing.
- Repository-scale work: [[blog-peter-steinberger-shipping-at-inference-speed]] reports that Codex may read files for ten to fifteen minutes before editing and can be slower per attempt yet faster overall when fewer corrective passes are needed.
- Conversational planning: [[blog-peter-steinberger-shipping-at-inference-speed]] replaces a separate Plan Mode with research, code exploration, dialogue, plan refinement, and an explicit instruction to build.
- Agent-verifiable interfaces: [[blog-peter-steinberger-shipping-at-inference-speed]] recommends starting with a CLI so the model can invoke the product and inspect its output directly.
- Solo workflow boundary: [[blog-peter-steinberger-shipping-at-inference-speed]] describes direct-to-main work, limited checkpointing, and three-to-eight concurrent projects while explicitly warning that the pattern would not transfer unchanged to a larger team.

## Counterevidence & Qualifications
The sources are personal practitioner accounts rather than comparative studies. They also treat specific models and tools as strong in their moment, so some conclusions may depend on model quality, token allowances, pricing, language/domain coverage, and tool design. The term itself is unstable: some sources use vibe coding broadly for AI-assisted development, while Guangzhengli reserves it for a narrower no-review style and recommends [[ContextCoding]] for serious practice. Hu's and Steinberger's cases benefit from deep expertise, personal infrastructure, and mostly solo or single-user conditions, so they cannot establish that routine non-review is safe for shared or consequential software. Steinberger's one-shot refactor and speed claims lack independent defect, maintenance, security, and lifecycle measurements. Parmaksız's unsafe-future-release example expresses a trust risk, not evidence that a particular project caused harm. Vibe coding is not presented as a replacement for exact IDE refactors, domain expertise, or human responsibility.

## What Changed
- Added Steinberger's contrasting expert workflow: ordinary conversation, deep repository reading, durable docs, cross-project examples, and CLI-first verification rather than a custom worker pool.
- Shifted the current bottleneck account from code production toward inference time, architecture, dependencies, system boundaries, product judgment, and human attention.
- Qualified Plan Mode and session-reset prescriptions as model- and task-dependent rather than universal.
- Strengthened the warning that system-level awareness and executable checks do not by themselves prove generated-code maintainability or safety.

## Related Concepts
- [[AICodingPractice]] - vibe coding needs disciplined norms for human judgment, review, and maintainability.
- [[AIAgentCollaboration]] - developers steer agents through planning, questioning, and feedback.
- [[SoftwareVerification]] - tests and execution checks make generated code accountable.
- [[LLMContextManagement]] - task splitting, subagents, session resets, and compaction timing protect agent reliability.
- [[AIFirstEngineering]] - both describe AI-centered software work, but vibe coding focuses on individual workflow experience.
- [[HarnessEngineering]] - harnesses formalize the checks and scaffolds that make fast agent work safer.
- [[AgentTeam]] - role separation is one way to scale vibe coding beyond a single agent conversation.
- [[ContextCoding]] - proposed label for serious AI-assisted programming where context, review, and verification remain central.
- [[OpenSourceProjectMaintenance]] - public release turns generated-code comprehension and future safety into maintainer obligations.
- [[PersonalSoftware]] - single-user scope can make aggressive vibe coding cheaper while avoiding many public-product obligations.
- [[BottleneckAwareAICoding]] - parallel agents move rather than eliminate constraints in planning, integration, review, and verification.
