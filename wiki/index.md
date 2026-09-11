# Wiki Index

This file is maintained by the LLM. Updated on every ingest.

## Overview
- [Overview](overview.md) - living synthesis across all sources

## Sources
- [陈皓 - HTTP的前世今生](sources/chen-hao-http-de-qian-shi-jin-sheng.md) - A history of HTTP from early request-response versions through HTTP/1.1, HTTP/2, HTTP/3, and QUIC.
- [锐评主流AI推理负载均衡开源实现](sources/rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian.md) - A technical critique of open-source inference load-balancing implementations, focusing on tokenization, metric collection, routing, and KV-cache-aware design.
- [褪墨 - 提高工作效率的十条好习惯](sources/tuimo-10-timeless-work-habits-to-boost-productivity.md) - Ten lightweight habits for improving productivity through priority-setting, focus, batching, delegation, and simple routines.
- [费曼学习法实践 / INDIGO 的信息获取与知识输出方法论](sources/feynman-technique-in-practice-indigo-information-acquisition-knowledge-output-methodology.md) - A Feynman-style learning workflow connecting focused reading, structured output, personal knowledge bases, and AI-assisted note organization.

## Entities
- [AIBrix](entities/AIBrix.md) - AI inference platform gateway critiqued for tokenizer choices, metric collection paths, and large-scale polling cost.
- [Bernard Marr](entities/BernardMarr.md) - Author credited for the productivity habits article.
- [Chen Hao](entities/ChenHao.md) - Technical author explaining HTTP history through protocol engineering and architecture tradeoffs.
- [Dan Shipper](entities/DanShipper.md) - Author quoted on note taking as a relationship with a future self.
- [Dynamo Inference Platform](entities/DynamoInferencePlatform.md) - Inference platform whose router uses local tokenizers, KV events, cost-based routing, and replica synchronization.
- [Edgar Dale](entities/EdgarDale.md) - Educational theorist cited for Dale's Cone of Experience.
- [Gateway API Inference Extension](entities/GatewayAPIInferenceExtension.md) - Endpoint-picker extension for inference routing, evaluated for byte-based token estimates and centralized EPP architecture.
- [Google](entities/Google.md) - Web-platform actor associated in the source with SPDY, QUIC, Chrome, and HTTP/2/HTTP/3 evolution.
- [INDIGO](entities/INDIGO.md) - Practitioner-author describing a personal learning, research, writing, and note-system workflow.
- [Kthena](entities/Kthena.md) - Single-binary inference router noted for weighted routing composition and critiqued for tokenizer encoding choice.
- [Richard Feynman](entities/RichardFeynman.md) - Physicist cited as the origin figure for the Feynman Technique.
- [Steven Covey](entities/StevenCovey.md) - Productivity author cited for the urgent/important time-management quadrants.
- [Tim Berners-Lee](entities/TimBernersLee.md) - CERN engineer credited in the source with inventing HTTP and the World Wide Web.

## Concepts
- [AI Knowledge Assistant](concepts/AIKnowledgeAssistant.md) - AI-supported summarization, association, classification, and retrieval for personal notes.
- [Active Learning](concepts/ActiveLearning.md) - Learning through explanation, teaching, recreation, writing, and other output-oriented use.
- [Attention Management](concepts/AttentionManagement.md) - Protecting focus by reducing multitasking, noisy inputs, and avoidable interruptions.
- [Feynman Technique](concepts/FeynmanTechnique.md) - Learning by setting a target, explaining simply, reviewing gaps, and internalizing understanding.
- [Focused Reading](concepts/FocusedReading.md) - Topic-driven information filtering that turns broad intake into reusable research material.
- [Head-of-Line Blocking](concepts/HeadOfLineBlocking.md) - A blocking pattern where later HTTP work waits behind stalled earlier work or lost TCP data.
- [HTTP](concepts/HTTP.md) - The web application protocol whose evolution moves from simple request-response transfer to QUIC-based transport.
- [HTTP/1.1](concepts/HTTP11.md) - HTTP version that added persistent connections, richer negotiation, caching, Host routing, and API-era features.
- [HTTP/2](concepts/HTTP2.md) - HTTP version using binary framing, multiplexing, header compression, and server push to improve performance.
- [HTTP/3](concepts/HTTP3.md) - HTTP version that runs over QUIC and UDP to reduce TCP-level blocking and connection setup costs.
- [Inference Load Balancing](concepts/InferenceLoadBalancing.md) - Routing and quota layer that distributes AI inference requests using tokenized workload, live metrics, and cache state.
- [Inference Tokenization](concepts/InferenceTokenization.md) - Model-aligned token accounting used by inference gateways for load estimates, quotas, and cache-aware routing.
- [KV-Cache-Aware Routing](concepts/KVCacheAwareRouting.md) - Routing strategy that considers reusable key-value cache blocks to reduce inference prefill work.
- [Knowledge Output](concepts/KnowledgeOutput.md) - Turning intake and research into notes, articles, explanations, or courses that deepen learning.
- [Personal Productivity](concepts/PersonalProductivity.md) - Arranging priorities, attention, routines, and task triage to complete meaningful work efficiently.
- [Personal Knowledge Management](concepts/PersonalKnowledgeManagement.md) - Capturing, organizing, retrieving, and reusing notes and source material for future thinking.
- [QUIC](concepts/QUIC.md) - UDP-based transport protocol used by HTTP/3 for multiplexing, reliability, TLS integration, and connection identity.
- [Second Brain](concepts/SecondBrain.md) - An external knowledge system that supports memory, retrieval, connection, and synthesis.
- [Time Management Quadrants](concepts/TimeManagementQuadrants.md) - Sorting tasks by urgency and importance to protect important work.
- [Work Habits](concepts/WorkHabits.md) - Repeatable routines and practices that shape how work gets done.

## Syntheses
