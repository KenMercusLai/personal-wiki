---
title: "OpenAI"
description: "An AI company whose API keys and embedding interface are used in the source's private-data chatbot tutorial."
type: "entity"
updated: "2026-09-02"
source_keys: ["build-chatgpt-with-private-data"]
entity_kind: "ai-company"
---

[零基础｜搭建基于私域数据的ChatGPT]({{< relref "/wiki/sources/build-chatgpt-with-private-data.md" >}}) requires an OpenAI account and API key for the chatbot's model access. The source also describes using LangChain to call OpenAI's embeddings interface so text chunks and user questions can be represented for similarity search.

The tutorial tests the system with text copied from OpenAI's Wikipedia page, then compares answers from the private-data chatbot against a baseline model response without that external data.
