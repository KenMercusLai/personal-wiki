---
title: "Claude Code orchestration"
description: "把多个 Claude Code 实例组织成可调度、可观察的开发执行系统。"
type: "concept"
updated: "2026-09-01"
source_keys: ["yuanming-hu-ten-claude-code-agents"]
---

Claude Code orchestration 是指在单个 Claude Code 之外构建管理层，让多个实例可以被启动、调度、监控和复盘。胡渊鸣的文章中，orchestration 包括在 EC2 上运行 Claude Code、使用任务列表实现 Ralph loop、为每个 Git worktree 启动独立实例，以及用 stream JSON 日志让 manager 判断子任务的状态和失败原因。

这种做法把 Claude Code 从交互式开发伙伴变成后台执行组件。作者还把 Claude Code 的 Plan Mode 封装进自己的开发中心，用于批量发起计划任务并集中 review，从而减少每个任务开始时的意图偏差。

来源：[胡渊鸣 | 我给 10 个 Claude Code 打工]({{< relref "/wiki/sources/yuanming-hu-ten-claude-code-agents.md" >}})
