---
title: "Clean WSL reinstall workflow"
description: "通过注销发行版、卸载 Linux 应用、关闭 WSL 相关 Windows Features、重启并重新运行 wsl --install 来重建 WSL 环境。"
type: "concept"
updated: "2026-09-02"
source_keys: ["clean-wsl-reinstall-windows-10-systemd-support"]
---

来源：[Clean WSL Reinstall for Native systemd on Windows 10]({{< relref "/wiki/sources/clean-wsl-reinstall-windows-10-systemd-support.md" >}})

Clean WSL reinstall workflow 指在重新启用 WSL 前先清空旧发行版和 Windows 侧安装状态。来源中的流程从管理员 PowerShell 开始：先用 `wsl -l -v` 列出现有发行版，再用 `wsl --unregister Ubuntu`、`wsl --unregister Debian` 等命令删除对应发行版数据。

Windows 侧还需要清理发行版应用和平台功能。作者建议在 Settings > Apps > Apps & Features 中搜索并卸载 Ubuntu、Debian 或其他 Linux 相关应用，然后在 Windows Features 中关闭 Virtual Machine Platform 和 Windows Subsystem for Linux，并重启机器。

安装阶段反而很短：运行 `wsl --install`，重启后等待默认 Ubuntu 初始化并创建用户。若要换发行版，再用 `wsl --list --online`、`wsl --install -d Debian` 和 `wsl --set-default Debian` 选择目标发行版。这个流程的重点不是复杂安装参数，而是先把旧的发行版状态和 Windows 功能状态处理干净。

来源还提醒，全局 `.wslconfig` 不会因为这套重装流程自动删除或重置。它属于单独的系统级配置，若旧配置本身造成问题，需要另外人工检查。
