---
title: "Kelsey Hightower"
description: "Author of 12 Fractured Apps, where he argues that Dockerized applications should own their startup behavior instead of hiding fragility behind entrypoint scripts."
type: "entity"
updated: "2026-09-01"
source_keys: ["kelsey-hightower-12-fractured-apps"]
entity_kind: "person"
---

来源：[12 Fractured Apps]({{< relref "/wiki/sources/kelsey-hightower-12-fractured-apps.md" >}})

Kelsey Hightower 是这篇来源的作者。文章以 Docker、Twelve-Factor App 和一个 Go 示例应用为背景，讨论应用启动时对配置文件、工作目录和数据库连接的脆弱假设。

在来源中，Hightower 的核心主张是把启动引导逻辑尽量放回应用内部。自定义 Docker entrypoint 可以包装无法修改的程序，但对自己控制的应用而言，环境变量覆盖、默认配置、目录创建和依赖重试都更适合由应用代码直接承担。
