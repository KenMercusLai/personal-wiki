---
title: "The Eternal Sloptember"
type: source
tags: [ai, software-engineering, coding-agents, organizational-risk]
date: 2026-05-24
source_file: "/mnt/ken_personal_wiki/Articles/The Eternal Sloptember.md"
---

## Summary
[[GeorgeHotz]] argues that current LLM coding agents imitate the statistical surface of programming without reliably performing the error correction, causal reasoning, and sustained polishing required of software engineers. Based on six months of using agents on [[Tinygrad]] and an ASM2464PD firmware-reversing project, he finds them useful for search and rapid prototypes but slower than manual work when quality and completion matter. He predicts that organizations which reward generated volume without close human understanding will accumulate plausible-looking defects and features faster than high-performing individuals or small teams that preserve tight feedback loops.

## Key Claims
- Increasingly fluent model output can become harder to audit because syntax and grammar look correct even when the artifact fails under interaction, extension, or maintenance.
- Agents front-load visible progress on prototypes but often fail to finish the final polish, turning late-stage correction into repeated probabilistic retries.
- The author reports trying multiple models, harnesses, and prompts on real systems work while still believing he could have produced the result faster and better manually.
- AI remains useful as a search aid and for prototypes where polish is unimportant; the practical requirement is choosing tasks and trust levels deliberately.
- High-performing practitioners mitigate risk by reading and understanding generated code, learning when to use agents, and correcting errors through tight feedback loops.
- Large organizations may be more exposed because slow feedback, weak alignment, and output incentives can amplify the work of people least able to recognize plausible-looking failure.
- The article predicts more code, applications, and features but a lower average quality distribution unless the field develops agents with stronger world models and trustworthy error correction.

## Key Quotes
> "The output is broken, but in a way that’s getting harder and harder to detect." — on fluency weakening traditional surface-quality proxies.

> "The key aspect is knowing when to use it and when not to." — on selective rather than universal adoption.

> "A trait you find in all high performing people is the ability to error correct" — on the human capability the author believes separates useful assistance from organizational harm.

## Connections
- [[GeorgeHotz]] - author reporting first-person experiments with coding agents.
- [[AICodingPractice]] - contributes a strongly skeptical, task-selective practice boundary based on human comprehension and error correction.
- [[BottleneckAwareAICoding]] - argues that fast initial generation can move cost into hard-to-detect defects, polishing, and organizational recovery.
- [[OrganizationalScaleTradeoffs]] - predicts that slow feedback, weak alignment, and output incentives make large organizations unusually vulnerable to generated-code volume.
- [[HumanCodeResponsibility]] - high-performing users are described as reading and understanding each line except in confined domains.
- [[SoftwareVerification]] - passing tests is not sufficient when an agent can alter or neutralize the test instead of repairing the intended behavior.
- [[Tinygrad]] - one of the real projects on which the author tested agent-assisted development.

## Contradictions
- The essay directly contests sources that report coding agents crossing an expert's daily-work baseline or justify reduced line-by-line review through design control and strong behavioral tests; it supplies first-person counterexperience rather than a controlled comparison.
- Claims that LLMs will never program and require world models are theoretical judgments, not demonstrated impossibility results, and the article does not define or evaluate a qualifying world model.
- The organizational forecast provides no defect rates, maintenance outcomes, productivity measurements, sampling method, or controlled comparison across company sizes and performance levels.
- The Apple adoption example is introduced as hearsay, and the macOS quality question is a prediction rather than evidence.
- The supplied Markdown contains no effective image references, so no visual assets or manifest were required.
