---
title: "Claude Code"
description: "文章中用于远程、并行和可调度 agentic coding 的命令行 AI 编程工具。"
type: "entity"
updated: "2026-09-01"
source_keys: ["yuanming-hu-ten-claude-code-agents"]
entity_kind: "software"
---

Claude Code 是胡渊鸣在文章中用于开发个人 CEO 支持软件的主要 AI 编程工具。作者从 Cursor Agent 转向 Claude Code，是因为它更适合在没有图形界面的远程环境中运行，也便于在 iPhone 上通过 SSH 或网页管理器派发任务。

文章中的 Claude Code 被进一步封装为可调度组件：作者在 EC2 上运行它，通过任务队列、Git worktree、stream JSON 日志和 Plan Mode manager 同时驱动多个 Claude Code 实例工作。

来源：[胡渊鸣 | 我给 10 个 Claude Code 打工]({{< relref "/wiki/sources/yuanming-hu-ten-claude-code-agents.md" >}})
