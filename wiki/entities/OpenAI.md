---
title: "OpenAI"
type: entity
tags: [ai, api, llm]
sources:
  - ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt
  - a-comprehensive-guide-to-build-your-own-language-model-in-python
  - yan-li-how-llm-agents-became-what-they-look-like-in-2026
  - what-is-chatgpt-doing-and-why-does-it-work
  - exclusive-interview-openais-sam-altman-talks-chatgpt-and-how-artificial-general-intelligence-can-break-capitalism
  - greg-brockman-define-cto-openai
  - openai-scaling-postgresql-to-power-800-million-chatgpt-users
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[OpenAI]] appears in the wiki from its 2015-2017 formation as a research organization joining engineering with machine-learning research, through its later GPT research, model and embedding APIs, tool calling, ChatGPT productization, mixed release modes, and AGI-oriented governance.

## Current Profile
Across the sources OpenAI functions as both research lineage and infrastructure. The private-data chatbot tutorial uses OpenAI APIs and embeddings through LangChain, and treats the underlying model's language ability as something that can be decoupled from its built-in knowledge by retrieving from user documents. The language-modeling tutorial cites OpenAI's February 2019 GPT-2 release as the example of a large transformer-based generative model that can be run through PyTorch-Transformers. The staged-history source credits OpenAI's API with introducing tool calling, described as the first standardized wrapper around structured output, while noting that it returns JSON arguments and does not execute the tool.

The ChatGPT explanation adds the research side of the same institution. It treats ChatGPT as a GPT-3 network of about 175 billion weights, and describes the post-training stage in which human ratings are used to train a model that then acts like a loss function on the original network - the step the essay credits with much of the system's usefulness as a chatbot. The same source records an explicitly deflationary reading of the result: without access to external computational tools, the system produces text that sounds right rather than text that has been verified.

The Forbes interview connects that research lineage to product judgment and institutional design. [[SamAltman]] says ChatGPT's base capability had already been available through the API, while fine-tuning and interaction design produced the public breakthrough; he pushed to ship despite internal hesitation. He presents public products as a way for society to encounter benefits and harms, stronger APIs as conditional on safety, and open source as selective rather than universal. The company's capped-return structure and safety-override provisions in the [[Microsoft]] relationship are described as preparations for an outcome in which [[ArtificialGeneralIntelligence]] no longer fits the ordinary technology-company playbook.

[[GregBrockman]]'s January 2017 retrospective adds the earliest institutional layer. He traces OpenAI from an August 2015 founding discussion through recruiting and organization design to [[OpenAIGym]] and [[OpenAIUniverse]]. The stated design joined an academic-style mission and openness with private-industry resources, valued research and engineering equally, and moved founder attention between administration and coding as constraints changed. This is a founder's interested account of the organization's aspirations and division of work, not an independent history or evidence that its cooperative vision succeeded.

The PostgreSQL case adds the production-infrastructure layer behind the later products. OpenAI reports serving ChatGPT and API demand through one PostgreSQL writer and nearly 50 regional read replicas, while moving shardable write-heavy workloads to other systems. Its reliability practice is explicitly cross-layer: caching, connection pooling, workload tiers, rate limits, query blocking, hot-standby failover, cautious schema changes, and capacity headroom are used together because upstream failures and retries can turn database saturation into product-wide degradation.

## Key Characteristics
- Began, in Brockman's account, by combining an academic-style mission and private-industry resources, equal status for research and engineering, and early Gym and Universe infrastructure.
- Provides model, embedding, and tool-calling APIs used for grounded applications and structured external action.
- Is credited with GPT-2, the GPT-3 lineage behind early ChatGPT, and a human-feedback tuning stage that improved instruction following.
- Turned an already API-accessible base capability into ChatGPT through fine-tuning, interaction design, and a disputed internal decision to ship.
- Operates global product infrastructure through workload-specific scaling, including a read-heavy PostgreSQL deployment and migration of shardable write-heavy work.
- Uses cross-layer isolation, admission control, caching, pooling, failover, and conservative change to protect critical product paths.
- Uses public products, safety-gated APIs, selective open source, capped returns, safety overrides, and shared downstream accountability as a mixed release-and-governance portfolio.

## Evidence
- API and embedding infrastructure: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] instructs readers to create an OpenAI API key and save it as `OPENAI_API_KEY` in Replit, and says the sample uses LangChain to call OpenAI's embeddings interface.
- Private-data grounding: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] argues that ChatGPT's language understanding can be decoupled from its built-in knowledge by adding external private data, then uses OpenAI Wikipedia content as the uploaded private dataset.
- GPT-2 research context: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] says OpenAI released GPT-2 in February 2019 and describes it as a transformer-based generative language model trained on 40GB of curated internet text.
- Tool-calling origin: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says tool calling was introduced by the OpenAI API, which became the de facto standard for LLM APIs.
- Contract without runtime: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says the API provides JSON arguments for the tool but does not actually execute it.
- GPT-3 and ChatGPT: [[what-is-chatgpt-doing-and-why-does-it-work]] says ChatGPT is a version of the GPT-3 network with 175 billion weights, 96 attention blocks, and 12,288-number embeddings.
- Human-feedback stage: [[what-is-chatgpt-doing-and-why-does-it-work]] describes collecting human ratings of outputs, training a model to predict those ratings, and using it like a loss function to tune the network, a step it credits with a large effect on producing human-like output.
- Instruction following: [[what-is-chatgpt-doing-and-why-does-it-work]] links the essay's account of one-shot instruction use to OpenAI's published instruction-following work.
- Productization: [[exclusive-interview-openais-sam-altman-talks-chatgpt-and-how-artificial-general-intelligence-can-break-capitalism]] says ChatGPT's base model had been in the API for months before fine-tuning and interaction design created the public product moment.
- Release portfolio: [[exclusive-interview-openais-sam-altman-talks-chatgpt-and-how-artificial-general-intelligence-can-break-capitalism]] describes public ChatGPT access, progressively more powerful APIs as safety permits, and selective open-source releases including CLIP, Whisper, and Triton.
- Social-learning rationale: [[exclusive-interview-openais-sam-altman-talks-chatgpt-and-how-artificial-general-intelligence-can-break-capitalism]] says releasing usable tools lets society experience benefits and downsides and shifts the acceptable public-policy discussion around AGI.
- Partnership safeguards: [[exclusive-interview-openais-sam-altman-talks-chatgpt-and-how-artificial-general-intelligence-can-break-capitalism]] says OpenAI's Microsoft deal includes capped returns and safety-override provisions intended to protect the mission.
- Shared accountability: [[exclusive-interview-openais-sam-altman-talks-chatgpt-and-how-artificial-general-intelligence-can-break-capitalism]] assigns responsibility both to model/tool builders and to companies with the final end-user relationship, prompted by harms from open-source image generation.
- Founding design: [[greg-brockman-define-cto-openai]] describes the August 2015 discussions, recruiting process, and early commitment to combine industry resources with an academic-style mission while valuing research and engineering equally.
- Research infrastructure: [[greg-brockman-define-cto-openai]] presents Gym's standardized environments and Universe's keyboard/mouse/screen system as software whose quality and speed affected what researchers could test.
- Constraint-driven organization: [[greg-brockman-define-cto-openai]] says Brockman and Sutskever exchanged administrative and engineering duties when Gym became a bottleneck, then identified a need for full-time organizational execution at roughly forty people.
- Production database scale: [[openai-scaling-postgresql-to-power-800-million-chatgpt-users]] reports one PostgreSQL primary, nearly 50 regional replicas, and millions of QPS for ChatGPT and API workloads.
- Reliability controls: [[openai-scaling-postgresql-to-power-800-million-chatgpt-users]] describes cache locking, PgBouncer, workload isolation, rate limits, query blocking, HA standby, replica headroom, and constrained schema changes.
- Workload boundary: [[openai-scaling-postgresql-to-power-800-million-chatgpt-users]] says shardable write-heavy workloads are moving to sharded systems and new tables are not added to the current PostgreSQL deployment.

## Qualifications
The sources include tutorials, explanatory essays, an edited CEO interview, founder retrospectives, and a first-party infrastructure case rather than independent product, governance, or reliability audits. They should not be used for current API setup, pricing, security, model availability, corporate structure, partnership terms, leadership, or current GPT-family capabilities without verification. The tool-calling history is compressed, the 2017 founding account is partial and interested, and the database article omits workload traces, costs, and independently verified availability or latency. Claims about cooperation, safeguards, organizational design, or infrastructure headroom remain source-bounded.

## What Changed
- Added OpenAI's role as the origin of the standardized tool-calling API.
- Added the GPT-3 and human-feedback lineage behind ChatGPT, together with the essay's deflationary reading of what the model does without external tools.
- Added OpenAI's ChatGPT launch account, mixed release strategy, Microsoft deal safeguards, and AGI-governance rationale.
- Added the 2015-2017 formation, engineering/research culture, Gym and Universe infrastructure, and constraint-driven role allocation from Brockman's retrospective.
- Added the production database architecture, cross-layer reliability controls, and explicit migration boundary for write-heavy workloads.

## Relationships
- [[LangChain]] - LangChain wraps OpenAI model and embedding calls in the tutorial.
- [[Replit]] - Replit stores the OpenAI API key and runs the sample project.
- [[Embeddings]] - OpenAI's embedding API supplies vector representations in the source.
- [[PrivateDataChatbot]] - OpenAI model capability is combined with private data to answer questions.
- [[GPT2]] - pretrained language model credited to OpenAI in the tutorial.
- [[GPT3]] - the network credited to OpenAI behind ChatGPT.
- [[ChatGPT]] - OpenAI's assistant, described in the essay as tuned with human feedback.
- [[NaturalLanguageGeneration]] - GPT-2 is used for completion and generation examples.
- [[LLMAgentStages]] - tool calling is the second stage in the staged agent history.
- [[ModelContextProtocol]] - MCP is described as supplying the tool runtime that OpenAI's contract omits.
- [[SamAltman]] - CEO whose Forbes interview supplies OpenAI's product, release, partnership, and AGI-governance account.
- [[ArtificialGeneralIntelligence]] - mission target used to justify nonstandard ownership, access, profit, and governance arrangements.
- [[ResponsibleAIRelease]] - public tools, gated APIs, selective open source, contracts, and downstream duties form OpenAI's stated release portfolio.
- [[Microsoft]] - partner whose capped return and safety-override terms are presented as mission protections.
- [[GregBrockman]] - co-founder whose 2017 retrospective supplies the early institutional and engineering account.
- [[IlyaSutskever]] - founding research leader described as shaping early strategy, culture, and technical direction.
- [[OpenAIGym]] - standardized reinforcement-learning environments whose engineering quality affected iteration speed.
- [[OpenAIUniverse]] - early keyboard, mouse, and screen environment infrastructure for agents.
- [[MachineLearningResearchEngineering]] - engineering layer treated as a direct input to research progress.
- [[PostgreSQL]] - relational database at the center of the reported ChatGPT and API production architecture.
- [[PostgreSQLReadScaling]] - one-writer, many-replica strategy used for the reported read-heavy workload.
- [[DatabaseOverloadProtection]] - layered controls intended to stop spikes and retries from cascading across products.
