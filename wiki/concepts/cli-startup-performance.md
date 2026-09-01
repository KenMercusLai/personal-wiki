---
title: "CLI startup performance"
description: "以冷启动时间衡量命令行工具的可用性，并控制普通命令进入用户可感知的快速区间。"
type: "concept"
updated: "2026-09-01"
source_keys: ["jeff-dickey-twelve-factor-cli-apps"]
---

来源：[12 Factor CLI Apps]({{< relref "/wiki/sources/jeff-dickey-twelve-factor-cli-apps.md" >}})

CLI startup performance 指命令行工具从调用到产生反馈的启动速度。Jeff Dickey 建议直接用 `time mycli` 测量 CLI，并给出大致判断：100ms 以下非常快，100-500ms 足够快，500ms-2s 可用但不出色，2s 以上则会让用户倾向于避开这个工具。

这篇来源承认，并非所有命令都能快速完成。下载大文件或 CPU 密集型任务需要更多时间时，CLI 应显示进度条或至少显示 spinner，让用户知道工作正在进行。不过这类反馈仍受 tty 和脚本化约束，不能污染非交互式输出。

性能在这里不是单纯的实现指标，而是使用频率的前提。CLI 常被放进短循环、别名、管道和自动化脚本中，冷启动时间过长会让用户在日常工作中感到阻滞，进而减少调用。
