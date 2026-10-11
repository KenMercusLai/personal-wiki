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
  - hu-tu-shuo-yin-dan-fei-guo-xian-feng-da-sha
  - why-llms-cant-really-build-software
  - ai-bian-cheng-shi-yi-zhong-kuang-jia-piglei
  - ai-shi-dai-lao-niao-de-kuang-huan-he-diao-ling-nolla
  - control-the-ideas-not-the-code
  - ye-tian-zhi-shu-121-when-code-is-cheap
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[AICodingPractice]] is the set of engineering behaviors, team norms, and review habits used when software developers work with AI coding agents.

## Current Synthesis
The sources frame AI coding practice as a sociotechnical discipline rather than a prompt library. Piglei emphasizes the individual and team practice layer: understand generated code, shape the design, control review size, prefer stable libraries for mature problems, verify behavior, and protect learning. The AI-first source expands the frame to organization-level workflow design: agents become useful at production speed only when surrounded by tests, CI/CD, monitoring, task management, architecture, feature flags, and human strategic review. Onevcat adds a practitioner workflow view from intensive [[ClaudeCode]] use: fast [[VibeCoding]] works best when tasks are planned or prototyped deliberately, kept small enough to understand, verified continuously, and paced so the tool does not dictate the human tempo. [[ChunYinUncle]]'s source sharpens the task-granularity rule: "AI wrote 99%" can be controlled when the human writes precise file-aware instructions, but becomes dangerous when broad delegation produces code nobody can explain.

At project scale, AI coding practice can become role design, document ownership, spec handoffs, memory hygiene, and CI discipline. The unit of practice shifts from "developer plus agent" to an [[AgentTeam]] whose work is coordinated through the file system.

Responsible agent coding also needs a verification-centered operating rule: do not let agents change tests and implementation freely in the same pass. [[AgentTDDResidual]] alternates test-only and implementation-only phases so the previous usable version, deterministic outputs, and snapshots become a fixed point. This shifts human effort from reading all generated code to judging behavior residuals, core expected outputs, and snapshot diffs.

Späti adds a craft-preservation boundary: AI can help with autocomplete and well-defined functions, but the farther a task reaches into architecture, long-term planning, or future maintenance, the more the human needs to think manually. His argument treats coding as both skill exercise and maintenance ownership, so speed is not enough if the developer loses understanding or the will to maintain what was generated.

Antirez adds the strongest capability-shift claim in the current evidence set. Across his Redis, DwarfStar, and systems-programming examples, he argues that for many projects writing code by hand—and now even reading every generated line—is becoming less sensible than deciding what to build, forming a clear mental model, communicating it to the LLM, testing behavior, and guiding corrections. The newer essay proposes `DESIGN.md`-style descriptions of data structures and implementation ideas as the durable control surface. This directly tensions craft-preservation and full-review arguments, while fitting the broader shift from typing toward problem framing, explicit design, verification, and ownership.

Guangzhengli reframes the practical layer as [[ContextCoding]]. The source says AI coding gets better when developers provide more relevant context: codebase structure, commands, conventions, core modules, rules files, current documentation, MCP tools, logs, and search traces. This strengthens the page's existing rule that AI coding is not mere delegation; the developer's job shifts toward context design, retrieval choice, small changes, debugging instrumentation, and verification.

AI coding practice also needs a system-flow correction. Faster code generation is not automatically faster delivery: AI can inflate PR size, review latency, work in progress, and rework if the true bottleneck is requirements, compatibility analysis, review, testing, or trust. In that frame, good practice means using specs, focused skills, verification loops, small PRs, and WIP-limited parallel sessions to move work through the whole SDLC rather than merely generating more code.

Parmaksız adds a craft-and-review-cost qualification. Giving an agent broad control made him feel unable to follow the work; reviewing every generated commit restored understanding but turned programming into continuous code review. His current compromise is task-selective: delegate tedious or unusually slow work, write the enjoyable parts manually, and perform a final human quality pass. This makes workflow fit depend not only on throughput and correctness but also on whether the division of labor preserves comprehension, motivation, and willingness to maintain the result.

Hutusi supplies an earlier, smaller task-to-code case and the strongest automation forecast in the bounded evidence. ChatGPT took a loosely stated frontend need through staged refinement, JavaScript generation, TypeScript conversion, and debugging guidance, leading the author to call LLMs a possible software-development "silver bullet." Yet the transcript itself preserves the limiting mechanism: the user decomposed the need, supplied missing local facts, corrected copy omissions, and judged the running result. The case therefore supports substantial translation leverage while undercutting the claim that analysis, design, debugging, and verification simply disappear.

Irwin makes that limiting mechanism explicit as a model-comparison loop. The agent may write code, run tests, add logging, and operate a debugger, but engineering still requires a stable representation of both intended behavior and actual behavior so someone can decide whether a failure belongs to the implementation, the test, the requirement, or an incomplete diagnosis. This sharpens the page's general context and ownership rules: good AI coding practice must preserve project intent across local investigations instead of mistaking fluent output or recent context for the whole system.

Piglei's framework-versus-library analogy adds control placement and lifecycle cognitive cost to this synthesis. When developers pursue the shortest possible prompt and let the agent determine the program's overall structure, they use AI in a framework-style mode: immediate effort falls, but architecture and implementation knowledge become hidden debt. A library-style mode keeps the human as system designer and invokes AI for bounded work through explicit structure, durable constraints, precise prompts, and code review. These are endpoints on a continuum, not permanent labels for a tool, and the right position depends on risk, lifetime, novelty, customization, and verification strength.

Nolla adds an organizational convergence lens. Routine frontend, CRUD, and first-pass testing may become cheap enough that implementation output is no longer the scarce step, but production still requires contracts, regression tests, staged rollout, rollback, observability, risk judgment, and a person willing to approve the result. The same shift creates a workforce-design obligation: if teams remove entry-level implementation work without replacing its learning function, short-run senior leverage can undermine the pipeline that produces future senior judgment.

A test-conditioned review model emerges from [[TisonKun]]'s open-source systems work. In the Cronexpr case, a bounded parser rewrite could receive little line-by-line inspection because existing behavior, new success and error snapshots, CI, and production use supplied a strong regression boundary. HawkEye's less exhaustively testable rewrite was instead reviewed from its CLI, configuration, errors, and other external contracts inward, while DataSketches and Cronexpr changes received intervention when they had the wrong design shape. This makes “read the code” versus “trust the tests” a task-specific allocation decision: confidence depends on scope clarity, behavioral coverage, audience, hidden-risk surface, and the maintainer's ability to detect implausible designs.

The source also sharpens the human-capacity boundary. When implementation, benchmark construction, examples, documentation, and repetitive tests become cheap, the scarce work becomes stating the desired outcome, choosing names and semantics, constructing a credible route through core decisions, and having enough reasoning energy to turn plausible output into convincing software. Agentic speed therefore does not remove cognitive work; it concentrates that work in judgment and acceptance.

## Key Claims
- AI coding practice requires shared team expectations because inconsistent agent-use habits can create collaboration friction.
- Engineers remain responsible for generated systems, maintainability, and final judgment, but review depth can range from line inspection to design and behavioral acceptance according to scope, verification strength, human readership, and hidden-risk exposure.
- Collaboration with agents should include design exploration and implementation reasoning, with structural control placed deliberately because broad framework-style delegation trades immediate leverage against later modifiability, diagnosis, and cognitive debt.
- Fast AI output increases the need for small PRs, review aids, pre-PR self-review, WIP limits, and review-capacity awareness.
- Verification through tests, self-checks, residual review, deterministic feedback, snapshot diffs, benchmarks, and downstream trials is part of the workflow, not a later review responsibility.
- Junior engineers, independent developers, and intensive coding-agent users need practices and deliberately preserved learning work that protect human pace, task control, craft enjoyment, production judgment, sustainable ownership, and task-horizon judgment rather than optimize only for generated-code volume.
- AI-first, agentic, and LLM-first coding practice depends on clear problem representation, stable requirement and behavior models, context quality, engineering systems, explicit roles, document boundaries, specs, memories, and verification gates that let agent output be diagnosed, checked, shipped, observed, and rolled back quickly.

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
- Early task-to-code case: [[hu-tu-shuo-yin-dan-fei-guo-xian-feng-da-sha]] shows ChatGPT implementing and explaining a small Next.js feature, refining timed output, translating it to TypeScript, and helping resolve type errors.
- Silver-bullet qualification: [[hu-tu-shuo-yin-dan-fei-guo-xian-feng-da-sha]] predicts that LLMs may compress traditional engineering stages, but its own transcript still depends on requirement decomposition, local context, debugging, and human acceptance.
- Engineering-loop model: [[why-llms-cant-really-build-software]] frames software work as repeated comparison of intended behavior with actual program behavior rather than code production alone.
- Ambiguous feedback: [[why-llms-cant-really-build-software]] argues that a failed test does not itself determine whether the code, test, requirement, or diagnosis should change.
- Context failure mechanisms: [[why-llms-cant-really-build-software]] names context omission, recency bias, and hallucination as reasons current models lose the stable project view needed for non-trivial iteration.
- Control placement: [[ai-bian-cheng-shi-yi-zhong-kuang-jia-piglei]] distinguishes agent-controlled framework-style work from human-structured library-style use without treating either as a fixed property of the tool.
- Cognitive-cost boundary: [[ai-bian-cheng-shi-yi-zhong-kuang-jia-piglei]] argues that minimal prompts can conceal architectural and implementation debt that emerges during debugging or customization.
- Concrete practices: [[ai-bian-cheng-shi-yi-zhong-kuang-jia-piglei]] recommends explicit program structure, durable constraints in `AGENTS.md`, code-aware prompts, and review of generated code.
- Convergence controls: [[ai-shi-dai-lao-niao-de-kuang-huan-he-diao-ling-nolla]] names contracts, regression tests, staged rollout, rollback, and observability as the guardrails through which experienced engineers turn plausible output into production-ready software.
- Responsibility shift: [[ai-shi-dai-lao-niao-de-kuang-huan-he-diao-ling-nolla]] argues that implementation abundance raises the relative cost of consistency, complexity control, risk convergence, and accountable approval.
- Career-pipeline risk: [[ai-shi-dai-lao-niao-de-kuang-huan-he-diao-ling-nolla]] warns that removing junior tasks can also remove the practice path into future senior judgment.
- Idea-centered control: [[control-the-ideas-not-the-code]] argues that design models, QA, optimization, and product direction are higher-leverage uses of scarce human attention than exhaustive inspection of abundant generated code.
- Durable design interface: [[control-the-ideas-not-the-code]] proposes human-readable descriptions of each data structure, its design, and its implementation techniques so future changes begin from the right mental model.
- Conditional source review: [[control-the-ideas-not-the-code]] retains manual review for Redis because human contributors will read and modify it, making the review boundary dependent on project audience and workflow.
- Novice learning: [[control-the-ideas-not-the-code]] questions whether reviewing generated application code teaches beginners enough and suggests manually implementing small interpreters, databases, and hash tables instead.
- Test-conditioned review: [[ye-tian-zhi-shu-121-when-code-is-cheap]] reports accepting a bounded Cronexpr parser rewrite largely through preserved tests and snapshots while inspecting less of the implementation.
- Contract-first rewrite review: [[ye-tian-zhi-shu-121-when-code-is-cheap]] describes reviewing HawkEye from CLI, configuration, errors, and external behavior inward because the rewrite's end-to-end behavior was less exhaustively testable.
- Expert correction: [[ye-tian-zhi-shu-121-when-code-is-cheap]] shows the author rejecting unnecessary public helpers and a poor error design even when agent output otherwise appeared plausible.
- Human-capacity limit: [[ye-tian-zhi-shu-121-when-code-is-cheap]] identifies clear wishes, core technical decisions, health, and reasoning effort as the constraints on converting agent output into convincing software.

## Counterevidence & Qualifications
The sources are practitioner essays rather than controlled comparisons of AI coding workflows, although the bottleneck-aware source cites controlled and telemetry studies as anchors. They also pull in different directions: Piglei stresses collaboration, understanding, learning protection, human structural control, and code review; the AI-first case study and Hutusi stress automation and role redesign, with Hutusi advancing the strongest silver-bullet claim; Onevcat stresses direct tool experience, small steps, context limits, and humane pacing; Chun Yin Uncle's source stresses independent-developer task decomposition and written expression; the residual-TDD source, Antirez's newer essay, and Tison's project cases shift attention from full generated-code review toward behavioral residuals, QA, explicit design, external contracts, and system ideas; Späti stresses manual competence and the future cost of generated systems people do not understand or enjoy maintaining; Guangzhengli stresses context engineering and retrieval choice; the bottleneck-aware source stresses full-SDLC throughput and WIP control; Parmaksız stresses craft enjoyment and the cost of turning implementation into permanent review; Irwin argues that current models cannot reliably maintain the paired requirement and behavior models needed for the loop itself; Nolla forecasts a disappearing junior-to-senior ladder if automation is not paired with new training infrastructure. Antirez and Tison supply no comparative defect counts for human versus model review, and their ability to control ideas or detect implausible designs without reading all code may depend on expertise that novices have not yet acquired. Tests and snapshots preserve observed behavior but cannot prove missing cases, security, maintainability, or the specification itself. Nolla supplies no workforce data or proof that routine implementation has near-zero marginal cost, and its prose was mostly generated by ChatGPT 5.2. The framework-versus-library model supplies no threshold for changing control modes. The right practice depends on codebase risk, human readership, regulatory demands, product expectations, safety requirements, team maturity, model/tool quality, learning goals, context freshness, review capacity, and verification strength.

## What Changed
- Added test coverage, scope clarity, external contracts, and hidden-risk exposure as explicit determinants of review depth.
- Added project evidence that strong snapshots and regression suites can support selective code reading without eliminating design intervention.
- Added human cognitive energy and the conversion of plausible output into convincing software as practical agent-work constraints.
- Extended cheap-agent labor beyond implementation to benchmarks, examples, documentation, and repetitive verification work.

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
- [[SoftwareEngineering]] - places AI coding inside the broader lifecycle of understanding, delivery, operation, and maintenance.
- [[EssentialAndAccidentalComplexity]] - frames the question of whether LLMs remove, relocate, or conceal difficult software work.
- [[MentalModels]] - requirement and implementation models make failures and corrections interpretable across iterations.
- [[AICodingFrameworkLibraryModel]] - frames AI coding practice as a deliberate choice about structural control and deferred cognitive cost.
- [[AbstractionLeakage]] - explains why broad prompt interfaces eventually expose code-level details during failure or customization.
- [[EngineeringMentorship]] - supplies deliberate learning infrastructure when routine implementation no longer provides an adequate apprenticeship path.
- [[CodeReviewPractice]] - generated-code abundance makes review capacity and the purpose of line inspection explicit design choices.
