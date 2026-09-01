---
title: "Declarative container control loops"
description: "容器平台通过描述期望状态，并由控制器持续调和实际状态和预期状态，降低容器管理复杂度。"
type: "concept"
updated: "2026-09-02"
source_keys: ["jysperm-2018-technical-year-review"]
---

来源：[2018 年度小结（技术方面）]({{< relref "/wiki/sources/jysperm-2018-technical-year-review.md" >}})

Declarative container control loops 指容器平台把管理操作从“逐步执行命令”转成“声明期望状态”，再由控制器持续把系统拉回这个状态。王子亭认为，这是容器平台能够简化容器管理的重要原因：开发者描述最终想要的结果，平台负责观察实际状态并执行必要动作。

Kubernetes 是来源中的主要例子。作者强调 Kubernetes 不只是工具，而是一个平台：它用 RESTful API 将功能抽象为资源，每种资源背后都有 Controller 负责把对象的实际状态同步到预期状态。这个模型也解释了为什么 Kubernetes 容易扩展：团队可以添加自定义资源和对应 Controller，让平台用同一套调和机制管理新的领域对象。

这个概念的关键不在于 YAML 或配置文件本身，而在于声明式对象、实际状态观测和控制器调和三者组合。只写配置而没有控制循环，仍然需要人工或脚本补齐变化；有控制循环后，平台可以持续处理失败、重启、扩缩容和状态漂移。
