---
title: "AI辅助软件开发的验证循环"
description: "把模型生成限制为小步变更，并用真实代码、编译器、测试、差异和运行结果持续闭环。"
type: "concept"
updated: "2026-08-30"
source_keys: ["hutusi-silver-bullet-software-engineering-history", "yuanming-hu-ten-claude-code-agents"]
featured: true
---

## 循环

1. 给出目标、现有代码、接口和不可违反的约束。
2. 要求最小、可检查的变更，而非一次生成整个系统。
3. 在真实项目中应用变更并查看diff。
4. 运行类型检查、测试、构建和代表性场景。
5. 将精确错误和实际上下文反馈给模型。
6. 修正后重复验证，直到满足完成标准。

模型的解释是候选推理，真实执行结果才是工程证据。验证范围还应覆盖安全、权限、数据迁移、回滚和运行可观测性；代码能编译只是最低门槛。

当多个代理并行工作时，循环还需要任务所有权、隔离工作区、基线同步、合并门禁和失败重试。结构化事件日志能让调度器区分“仍在运行”“需要输入”和“已经失败”，但提交频率本身不能证明任务正确完成。

该循环可以减少局部实现和检索成本，但不会自动决定应该构建什么。端到端收益应同时观察交付时间、缺陷、返工和维护负担。

## 来源

- [《银弹飞过先锋大厦》]({{< relref "/wiki/sources/hutusi-silver-bullet-software-engineering-history.md" >}})
- [《我给10个Claude Code打工》]({{< relref "/wiki/sources/yuanming-hu-ten-claude-code-agents.md" >}})
