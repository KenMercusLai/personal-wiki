---
title: "12 Fractured Apps"
description: "Kelsey Hightower argues that containerized applications should handle their own startup configuration, directories, and dependency retries instead of relying on Docker entrypoint scripts or deployment ordering."
type: "source"
updated: "2026-09-01"
source_key: "kelsey-hightower-12-fractured-apps"
image_status: "not_selected"
author: "Kelsey Hightower"
source_date: "2015-12-14"
---

## 摘要

这篇文章以 Docker 化应用为背景，讨论 Twelve-Factor App 原则在真实部署中的断裂点。Kelsey Hightower 认为，Docker 让日志写到 stdout、用环境变量传配置等十二因素实践更自然，但也让很多应用以“把旧系统搬进容器”的方式暴露出启动过程中的脆弱假设。

文章中的示例 Go 应用在启动时必须读到 `/etc/config.json`、看到工作目录、并立即连上 MySQL 数据库；任何一个条件暂时不满足，应用就退出。这类行为看似只是部署脚本要补齐的前置条件，实际上会把应用自身的责任转嫁给配置管理工具、服务启动顺序或自定义 Docker entrypoint。

Hightower 展示了常见补丁：用 shell entrypoint 在容器启动时生成配置文件、创建数据目录、等待数据库。这能让应用跑起来，但也引入新的维护层，让镜像为了脚本环境从 `scratch` 换成 Alpine，并可能让脚本逻辑和应用逻辑逐渐脱节。

作者的主张是把这些启动责任尽量放回应用内部。配置文件应是可选输入，缺失时使用合理默认值；环境变量可以直接覆盖配置；工作目录缺失时应用可以创建并记录错误；外部数据库暂时不可达时，应用应记录失败、退避重试，而不是要求运维人员按固定顺序部署所有服务。

## 关键观点

- Docker 和 Twelve-Factor App 配合良好，但容器不会自动修复应用启动时的脆弱假设。
- 不要为了不同环境把配置文件烘焙进不同镜像；镜像应更接近可复用的应用制品，运行时配置应在启动时注入。
- 自定义 Docker entrypoint 可以帮助包装无法修改的应用，但对于自己控制的应用，它常常只是掩盖应用层应承担的启动逻辑。
- 应用应优先自己处理可选配置、环境变量覆盖、工作目录创建和外部服务重试。
- 配置管理和部署编排不应被用来弥补应用无法容忍短暂依赖不可用的问题。

## 相关知识

- [Containerized application startup resilience]({{< relref "/wiki/concepts/containerized-application-startup-resilience.md" >}})
- [Container runtime configuration]({{< relref "/wiki/concepts/container-runtime-configuration.md" >}})
- [Kelsey Hightower]({{< relref "/wiki/entities/kelsey-hightower.md" >}})
- [Docker]({{< relref "/wiki/entities/docker.md" >}})
- [Twelve-Factor App]({{< relref "/wiki/entities/twelve-factor-app.md" >}})
