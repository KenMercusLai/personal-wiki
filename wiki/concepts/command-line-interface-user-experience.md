---
title: "Command-line interface user experience"
description: "把命令行工具视为产品界面来设计，系统处理帮助、输入、输出、错误、交互、性能和文件位置。"
type: "concept"
updated: "2026-09-01"
source_keys: ["jeff-dickey-twelve-factor-cli-apps"]
---

来源：[12 Factor CLI Apps]({{< relref "/wiki/sources/jeff-dickey-twelve-factor-cli-apps.md" >}})

Command-line interface user experience 指把 CLI 当作完整产品界面，而不是简单的命令解析入口。Jeff Dickey 认为，CLI 相比 Web 应用更容易快速构建，也更适合被技术用户组合进高级工作流，但它缺少图形界面的可见引导，因此需要通过命令本身承担更多说明、反馈和容错责任。

在这篇来源中，CLI UX 覆盖多个层面：帮助系统要能从常见入口打开；输入形式要尽量用清晰 flags 表达意图；版本信息要易于获得；stdout、stderr 和 tty 状态要被正确区分；错误消息要给出修复路径；颜色、进度条和提示要能在交互式环境中改善体验，也要能在脚本环境中退回朴素行为。

这个概念的重点是，CLI 用户体验不只属于“漂亮输出”。真正可用的 CLI 需要同时服务人和机器：人需要示例、诊断信息、确认提示和可读表格，机器需要稳定输出、可关闭的装饰、可覆盖的提示、结构化格式和标准文件位置。
