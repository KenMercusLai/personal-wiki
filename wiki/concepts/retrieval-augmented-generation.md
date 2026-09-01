---
title: "Retrieval-Augmented Generation"
description: "A pattern that retrieves relevant source chunks and provides them as context to a language model before answer generation."
type: "concept"
updated: "2026-09-02"
source_keys: ["build-chatgpt-with-private-data"]
---

[零基础｜搭建基于私域数据的ChatGPT]({{< relref "/wiki/sources/build-chatgpt-with-private-data.md" >}}) outlines a retrieval-augmented workflow for private data question answering. Documents are imported, split into chunks, embedded, and stored in a vector index; a user's question is embedded too, then similar chunks are retrieved and passed to the model with the question and chat history.

The source presents this retrieval step as the mechanism that lets a chatbot answer from newly supplied private information instead of depending only on the model's original knowledge cutoff.
