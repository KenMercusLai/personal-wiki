---
title: "AI Coding Practice"
type: concept
tags: [ai, software-engineering, developer-tools]
sources:
  - yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei
  - wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo
  - yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou
  - du-li-kai-fa-zhe-fen-xiang-ai-coding-de-mi-jue-yi-huo-de-shou-quan
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
  - agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha
  - blog-simon-spati-will-ai-replace-human-thinking
  - blog-antirez-dont-fall-into-the-anti-ai-hype
  - blog-guangzhengli-vibe-coding-and-context-coding
  - wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de
  - write-less-code-be-more-responsible-orhuns-blog
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[AICodingPractice]] is the set of engineering behaviors, team norms, and review habits used when software developers work with AI coding agents.

## Current Synthesis
The sources frame AI coding practice as a sociotechnical discipline rather than a prompt library. Piglei emphasizes the individual and team practice layer: understand generated code, shape the design, control review size, prefer stable libraries for mature problems, verify behavior, and protect learning. The AI-first source expands the frame to organization-level workflow design: agents become useful at production speed only when surrounded by tests, CI/CD, monitoring, task management, architecture, feature flags, and human strategic review. Onevcat adds a practitioner workflow view from intensive [[ClaudeCode]] use: fast [[VibeCoding]] works best when tasks are planned or prototyped deliberately, kept small enough to understand, verified continuously, and paced so the tool does not dictate the human tempo. [[ChunYinUncle]]'s source sharpens the task-granularity rule: "AI wrote 99%" can be controlled when the human writes precise file-aware instructions, but becomes dangerous when broad delegation produces code nobody can explain.

At project scale, AI coding practice can become role design, document ownership, spec handoffs, memory hygiene, and CI discipline. The unit of practice shifts from "developer plus agent" to an [[AgentTeam]] whose work is coordinated through the file system.

Responsible agent coding also needs a verification-centered operating rule: do not let agents change tests and implementation freely in the same pass. [[AgentTDDResidual]] alternates test-only and implementation-only phases so the previous usable version, deterministic outputs, and snapshots become a fixed point. This shifts human effort from reading all generated code to judging behavior residuals, core expected outputs, and snapshot diffs.

Späti adds a craft-preservation boundary: AI can help with autocomplete and well-defined functions, but the farther a task reaches into architecture, long-term planning, or future maintenance, the more the human needs to think manually. His argument treats coding as both skill exercise and maintenance ownership, so speed is not enough if the developer loses understanding or the will to maintain what was generated.

Antirez adds the strongest capability-shift claim in the current evidence set. From his Redis and systems-programming examples, he argues that for many projects writing code by hand is becoming less sensible than deciding what to build, forming a clear mental model, communicating it to the LLM, inspecting results, and guiding corrections. This directly tensions craft-preservation arguments, but it also fits the page's broader rule: AI coding practice is now less about typing and more about problem framing, review, verification, and ownership.

Guangzhengli reframes the practical layer as [[ContextCoding]]. The source says AI coding gets better when developers provide more relevant context: codebase structure, commands, conventions, core modules, rules files, current documentation, MCP tools, logs, and search traces. This strengthens the page's existing rule that AI coding is not mere delegation; the developer's job shifts toward context design, retrieval choice, small changes, debugging instrumentation, and verification.

AI coding practice also needs a system-flow correction. Faster code generation is not automatically faster delivery: AI can inflate PR size, review latency, work in progress, and rework if the true bottleneck is requirements, compatibility analysis, review, testing, or trust. In that frame, good practice means using specs, focused skills, verification loops, small PRs, and WIP-limited parallel sessions to move work through the whole SDLC rather than merely generating more code.

Parmaksız adds a craft-and-review-cost qualification. Giving an agent broad control made him feel unable to follow the work; reviewing every generated commit restored understanding but turned programming into continuous code review. His current compromise is task-selective: delegate tedious or unusually slow work, write the enjoyable parts manually, and perform a final human quality pass. This makes workflow fit depend not only on throughput and correctness but also on whether the division of labor preserves comprehension, motivation, and willingness to maintain the result.

## Key Claims
- AI coding practice requires shared team expectations because inconsistent agent-use habits can create collaboration friction.
- Engineers remain responsible for generated code, maintainability, and final judgment.
- Collaboration with agents should include design exploration and implementation reasoning, not only natural-language task assignment.
- Fast AI output increases the need for small PRs, review aids, pre-PR self-review, WIP limits, and review-capacity awareness.
- Verification through tests, self-checks, residual review, deterministic feedback, and snapshot diffs is part of the workflow, not a later review responsibility.
- Junior engineers, independent developers, and intensive coding-agent users need practices that protect learning, human pace, task control, craft enjoyment, sustainable ownership, and task-horizon judgment rather than optimize only for generated-code volume.
- AI-first, agentic, and LLM-first coding practice depends on clear problem representation, context quality, engineering systems, explicit roles, document boundaries, specs, memories, and verification gates that let agent output be checked, shipped, observed, and rolled back quickly.

## Evidence
- Team norm: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] warns that teammates without shared assumptions about AI coding can create project friction.
- Responsibility: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] says engineers should review, understand, and own AI-generated code.
- Collaboration: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] contrasts collaboration with delegation and urges engineers to explore design and structure with agents.
- Reviewability: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] recommends controlling PR size and adding design notes when a large PR cannot be split.
- Verification: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] recommends automated tests, self-testing, and agent-verifiable loops.
- Learning stage: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] gives junior engineers stricter advice on debugging, independent design, documentation, and architecture learning.
- Production harness: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] argues that AI coding speed only helps when automated tests, CI/CD, feature flags, monitoring, task decomposition, and architecture are already strong.
- Task boundary and pace: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] recommends small iterations, version-control safety, modular work, and remembering that faster tools still need human thinking time and life space.
- Task granularity: [[du-li-kai-fa-zhe-fen-xiang-ai-coding-de-mi-jue-yi-huo-de-shou-quan]] contrasts project-breaking large-grain delegation with small, explicit instructions that name files, functions, state flow, UI behavior, localization needs, and acceptance targets.
- Independent-developer control: [[du-li-kai-fa-zhe-fen-xiang-ai-coding-de-mi-jue-yi-huo-de-shou-quan]] shows an independent developer using AI to build unfamiliar iOS and Flutter work while still reviewing code, inspecting changed files, and accepting the result deliberately.
- Multi-agent practice: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] coordinates PM, Architect, Engineer, and QA agents through ADRs, specs, roadmaps, test plans, and CI state.
- Residual-focused testing: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] recommends alternating test-only and implementation-only phases so agents self-correct against a stable side and humans review behavior residuals.
- Task horizon and maintenance: [[blog-simon-spati-will-ai-replace-human-thinking]] uses an AI productivity/error curve to argue that short autocomplete-like gains can turn into rising error and ownership costs when AI is applied to architecture, planning, and code the human did not really make.
- Capability-shift evidence: [[blog-antirez-dont-fall-into-the-anti-ai-hype]] describes using Claude Code to add linenoise UTF-8 support and terminal-cell tests, fix Redis test flakes, create a pure C embedding-inference library, and reproduce Redis Streams internal changes from a design document.
- Problem representation: [[blog-antirez-dont-fall-into-the-anti-ai-hype]] argues that the programmer's scarce work shifts toward knowing what to build, how to build it, and how to communicate a good mental model to the LLM.
- Context practice: [[blog-guangzhengli-vibe-coding-and-context-coding]] recommends recording durable project stack, directory, command, utility, and core-module context in Copilot, Cursor, or Claude Code instruction files.
- Context freshness: [[blog-guangzhengli-vibe-coding-and-context-coding]] warns that stale instruction-file context can be more harmful than providing no context.
- Debugging support: [[blog-guangzhengli-vibe-coding-and-context-coding]] recommends adding logs, using current documentation through MCP-style tools, and bringing browser console or web-search evidence into the agent workflow.
- Bottleneck diagnosis: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] argues that AI can raise individual task and PR throughput while DORA-style delivery metrics stay flat if review and validation remain constrained.
- Flow controls: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] recommends small PRs, WIP limits, validation loops, and bounded parallel sessions so generated work does not overwhelm downstream review.
- Review-cost evidence: [[write-less-code-be-more-responsible-orhuns-blog]] reports that unrestricted Codex use damaged comprehension, while checking every commit restored control but made the work feel like nonstop review.
- Mixed workflow: [[write-less-code-be-more-responsible-orhuns-blog]] delegates boring or slow tasks, preserves enjoyable manual coding, and ends with a human quality pass.
- Open practice: [[write-less-code-be-more-responsible-orhuns-blog]] argues that developers should experiment, disclose AI use, and find a personally workable balance without treating AI assistance as a guilty secret.

## Counterevidence & Qualifications
The sources are practitioner essays rather than controlled comparisons of AI coding workflows, although the bottleneck-aware source cites controlled and telemetry studies as anchors. They also pull in different directions: Piglei stresses collaboration, understanding, and learning protection; the AI-first case study stresses automation, role redesign, and removing human bottlenecks; Onevcat stresses direct tool experience, small steps, context limits, and humane pacing; Chun Yin Uncle's source stresses independent-developer task decomposition and written expression; the residual-TDD source stresses verification economics and behavior continuity over full generated-code review; Späti stresses manual competence and the future cost of generated systems people do not understand or enjoy maintaining; Antirez stresses that refusing the capability shift is itself a career risk; Guangzhengli stresses context engineering and retrieval choice; the bottleneck-aware source stresses full-SDLC throughput and WIP control; Parmaksız stresses craft enjoyment and the cost of turning implementation into permanent review. The right practice depends on codebase risk, UI complexity, product expectations, safety requirements, team maturity, model/tool quality, learning goals, context freshness, review capacity, personal motivation, and the strength of the surrounding verification harness.

## What Changed
- Added the Claude Code source's practitioner emphasis on small iterations, context-aware task boundaries, and human pace.
- Added the independent-developer source's distinction between dangerous large-grain delegation and controlled file-aware task slicing.
- Added Agent Team practice, residual-focused agent TDD, and Späti's task-horizon warning as complementary checks on AI coding speed.
- Added bottleneck-aware AI coding as the system-flow qualification: faster generation only matters when review, WIP, verification, and upstream design constraints are managed.
- Added the mixed-workflow judgment that review labor, craft enjoyment, and motivation are part of responsible task allocation, not incidental preferences.

## Related Concepts
- [[HumanCodeResponsibility]] - accountability is the foundation of the article's practice model.
- [[AIAgentCollaboration]] - collaboration is the recommended interaction pattern within AI coding practice.
- [[PRReviewHygiene]] - reviewability becomes a central operational control for AI-heavy changes.
- [[SoftwareVerification]] - tests and self-checks are required to make agent output trustworthy.
- [[JuniorEngineerLearning]] - junior engineers need AI practices that protect skill formation.
- [[AIFirstEngineering]] - expands AI coding practice into a company operating model.
- [[HarnessEngineering]] - supplies the tests, constraints, and feedback loops that make agent output usable.
- [[AIApplicationFramework]] - both concern AI developer tooling, but this page focuses on behavior around coding agents rather than application frameworks.
- [[VibeCoding]] - names the speed-amplified workflow where these practices become especially important.
- [[AgentTeam]] - extends AI coding practice into role-based multi-agent project work.
- [[SpecDrivenAgentDevelopment]] - supplies document interfaces for agent implementation.
- [[AgentTDDResidual]] - supplies the article's alternating test/implementation loop for agent work.
- [[AIDependencySkillAtrophy]] - names the loss-of-practice risk when AI substitutes for coding understanding.
- [[PracticalLLMUse]] - Antirez's examples strengthen the practical case for using LLMs on bounded but substantial programming tasks.
- [[ContextCoding]] - names the context-engineering discipline behind effective AI coding practice.
- [[BottleneckAwareAICoding]] - frames AI coding practice around delivery throughput rather than local generation speed.
