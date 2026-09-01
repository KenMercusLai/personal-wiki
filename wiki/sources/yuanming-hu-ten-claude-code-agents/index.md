---
title: "胡渊鸣 | 我给 10 个 Claude Code 打工"
description: "胡渊鸣介绍自己用 Claude Code、Git worktree、任务管理器和语音输入提升 agentic coding 吞吐量，并讨论定制软件与组织管理在 AI 时代的变化。"
type: "source"
updated: "2026-09-01"
source_key: "yuanming-hu-ten-claude-code-agents"
image_status: "remote-images-omitted"
author: "E"
source_date: "2026-04-21"
---

这篇文章记录了胡渊鸣在开发个人 CEO 支持软件时，把 Claude Code 从单个交互式工具扩展为多实例、可排队、可观察的 agentic coding 系统的过程。文章的重点不是某个应用功能，而是如何提高 AI 编程吞吐量，让自己从直接写代码转向为 AI 建立环境、反馈闭环和管理机制。

## 背景

作者自述 2017 年从清华姚班毕业，随后在 MIT 做计算机图形学博士，开发过 Taichi 编程语言及其编译器。创业后，他创办太极图形并转向 Meshy AI。文中称 Meshy 是 3D AI 领域的重要产品，并表示自己后来使用 Ethan 作为英文名。

这次实践的起点是一个面向个人工作的 CEO 支持系统。作者希望它能覆盖日常文档写作、重要邮件查收、会议安排，以及一种带语音输入的 agentic 文档编辑体验。需求包括 Mac 与 iPhone 双端使用、对文档上下文聊天、中英双语编辑、自动整理中英文排版细节、校对，以及用思维导图检查结构。

## Agentic Coding 吞吐量

文章把作者的工作流分为十个阶段：

1. 从 Cursor Agent 转向 Claude Code。作者认为 Cursor Agent 已经能显著提升高性能 GPU DSL 设计效率，但 Claude Code 在远程和手机 SSH 场景下更适合随时派发任务。
2. 把 Claude Code 放进云端容器并跳过权限确认。作者在 EC2 上运行 Claude Code，以减少频繁权限弹窗带来的等待。
3. 使用 Ralph loop 式任务队列。作者让 Claude Code manager 从任务列表中不断取任务，单个任务完成后自动启动新的 Claude Code 实例。
4. 用 Git worktree 并行化。多个 worktree 中分别运行 Claude Code，使多个任务可以同时推进，再通过 Git 管理结果。
5. 用 `CLAUDE.md` 和 `PROGRESS.md` 保存长期上下文。`CLAUDE.md` 承载相对稳定的架构和规范，`PROGRESS.md` 用来沉淀执行中的经验教训。
6. 把开发界面从 SSH 转为手机网页。作者用 Python subprocess 封装非交互式 Claude Code 调用，并在 iPhone Safari 中把网页包装为应用。
7. 用结构化日志管理 Claude Code。作者使用 stream JSON 输出，让 manager 能分析子实例执行中的错误和状态，从而提升任务派发成功率。
8. 用语音识别做自然语言编程。作者给输入框加入语音识别，让想法可以在走路、坐车、睡前等场景中快速转为开发任务。
9. 给开发中心加入 Plan Mode。作者把 Claude Code 的规划模式封装进任务管理器，以便同时发起多个计划任务并统一 review。
10. 避免微管理 AI 写出的代码。作者把关注点从逐行看代码转为描述目标、设计上下文、建立测试和版本控制，以及提高 AI 的有效产出。

## 观点

文章提出，agentic coding 会让软件开发成本大幅降低，进而削弱标准化软件和传统 SaaS 的意义。作者认为当有开发能力的用户可以快速定制个人工具时，通用软件必须面对越来越多高度个性化的替代品。

作者还把 AI 管理与团队管理进行类比：AI 可以 7x24 工作、反馈更快、沟通更直接，因此管理 AI 迫使人更快暴露目标定义不清的问题。文章最后把这种技术变化和组织、学习、人类独特价值的重新定义联系起来，表达了强烈的兴奋感与焦虑感。
