---
title: "私域数据 ChatGPT"
description: "私域数据 ChatGPT 把大语言模型的语义理解和生成能力接入用户自有文档或业务数据，通过检索上下文回答特定资料中的问题。"
type: "concept"
updated: "2026-09-01"
source_keys: ["shensiquan-private-data-chatgpt-langchain"]
---

私域数据 ChatGPT 是一种把 ChatGPT 类大语言模型接入用户自有数据的应用形态。来源 [深思圈的私域数据 ChatGPT 教程]({{< relref "/wiki/sources/shensiquan-private-data-chatgpt-langchain.md" >}}) 用 ChatPDF、ChatDocs 和 ChatExcel 作为例子，说明用户真正需要的往往不是模型参数里已有的通用知识，而是让模型用自然语言读取、分析和回答自己上传的资料。

这个概念的关键在于把模型能力和数据源解耦。教程中的做法是先把私域文本上传到 Replit 项目中，再通过 LangChain 调用 OpenAI Embeddings，把文本片段转成向量并保存到 FAISS。用户提问时，系统对问题向量化并做相似度检索，把相关片段、历史问答和当前问题一起交给大模型生成回复。

私域数据 ChatGPT 可以看作 [检索增强生成]({{< relref "/wiki/concepts/retrieval-augmented-generation.md" >}}) 的应用场景之一。它的价值不在于让模型永久记住某份资料，而在于每次回答时把用户私有知识库中的相关证据临时放入上下文，从而让通用语言模型服务于具体个人或组织的数据。
