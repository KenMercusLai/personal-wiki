---
title: "ChatGPT"
description: "OpenAI 发布的大模型聊天应用；多篇来源用它讨论私域数据问答和大模型辅助软件开发。"
type: "entity"
updated: "2026-09-01"
source_keys: ["hutusi-silver-bullet-software-engineering-history", "shensiquan-private-data-chatgpt-langchain"]
entity_kind: "software"
---

[深思圈的私域数据 ChatGPT 教程]({{< relref "/wiki/sources/shensiquan-private-data-chatgpt-langchain.md" >}}) 把 ChatGPT 作为可以接入外部私域数据的语言能力层来讨论。文章指出，ChatGPT 自身的知识库不能直接覆盖用户上传的最新资料，因此教程通过 OpenAI API、LangChain、Embedding 和 FAISS，把用户私有文本检索出的片段放入上下文，再让 ChatGPT 类模型生成回答。

ChatGPT 是胡涂说文章中讨论大模型时代软件工程的主要实践工具。作者使用 GPT-4 版本的 ChatGPT 辅助实现一个类似 Perplexity 的智能搜索前端页面中的交互需求。

来源：[胡涂说 - 银弹飞过先锋大厦]({{< relref "/wiki/sources/hutusi-silver-bullet-software-engineering-history.md" >}})

在来源的案例中，ChatGPT 先生成 Next.js 页面代码，实现点击按钮后在页面区域显示文字；随后根据追加需求改成分段延时显示，再转换为 TypeScript，并在作者遇到类型推断错误时给出调试方向。作者认为，ChatGPT 的价值不只在于代码生成，也包括解释代码、识别意图和提示容易出错的位置。

这篇来源用 ChatGPT 作为大模型代码能力的代表，进一步讨论模型是否可能把需求直接转化为可运行软件，并因此改变传统软件工程中分析、设计、编码和调试的分工。
