---
title: "并行编码代理的Git worktree编排"
description: "用独立工作树隔离多个代理，以任务所有权、基线同步和合并门禁控制并行开发。"
type: "concept"
updated: "2026-08-30"
source_keys: ["yuanming-hu-ten-claude-code-agents"]
featured: true
---

## 基本结构

1. 将任务拆成边界清楚、可独立验证的单元。
2. 为每个任务记录唯一所有者和基线提交。
3. 给每个代理创建独立分支与Git worktree。
4. 代理只修改任务允许的范围，并提交可审查变更。
5. 在最新目标分支上重放或合并，解决冲突。
6. 统一运行测试、构建和集成门禁后才进入主分支。

共享只读数据可以减少复制，但可变状态、凭据和端口需要显式隔离。并行代理越多，任务依赖、资源争用和合并冲突越可能成为瓶颈。

衡量吞吐应使用完成且通过验证的任务、端到端交付时间、返工与缺陷，而非代理数量或commit频率。生成成功只是[验证循环]({{< relref "/wiki/concepts/ai-assisted-software-development-verification-loop.md" >}})的一环。

## 来源

- [《我给10个Claude Code打工》]({{< relref "/wiki/sources/yuanming-hu-ten-claude-code-agents.md" >}})
