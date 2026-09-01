---
title: "Containerized application startup resilience"
description: "让容器化应用在配置、工作目录或外部依赖暂时不可用时通过默认值、创建资源和退避重试完成稳健启动。"
type: "concept"
updated: "2026-09-01"
source_keys: ["kelsey-hightower-12-fractured-apps"]
---

来源：[12 Fractured Apps]({{< relref "/wiki/sources/kelsey-hightower-12-fractured-apps.md" >}})

Containerized application startup resilience 指应用在容器环境中启动时，不把所有外部条件都假设为已经就绪。Kelsey Hightower 的示例应用最初要求配置文件存在、数据目录存在、数据库立即可连；这些条件任何一个失败，应用就直接退出。

这篇来源强调，容器编排、配置管理和 shell entrypoint 不应成为应用启动脆弱性的长期补丁。如果数据库只是暂时不可达，应用应记录错误并使用退避重试；如果工作目录不存在，应用可以尝试创建它；如果配置文件缺失，应用可以加载默认值并允许环境变量覆盖。

这个概念的重点是把启动韧性放在最靠近业务进程的地方。部署系统仍然负责调度和注入运行时信息，但应用不应要求运维人员用固定服务顺序、额外脚本或外部检查来弥补它对正常启动路径的过度依赖。
