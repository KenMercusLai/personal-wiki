---
title: "Chaos testing for release readiness"
description: "Chaos testing before release deliberately injects crashes, abusive traffic, dependency failures, and network outages into staging so teams can observe resilience before production users do."
type: "concept"
updated: "2026-09-02"
source_keys: ["loadmill-seven-reasons-staging-environment-sucks"]
---

来源：[7 Reasons Why Your Staging Environment Sucks]({{< relref "/wiki/sources/loadmill-seven-reasons-staging-environment-sucks.md" >}})

Chaos testing for release readiness 指在发布前的 staging 测试周期中主动加入故障和意外事件，以验证系统在非理想条件下的可靠性。来源把现实系统描述为会不断遇到惊喜：服务器会崩溃，滥用和 DoS 会发生，托管服务可能宕机，网络也会中断。

这种测试的目标不是制造随机破坏，而是让团队在用户之前观察系统的退化方式。把故障注入放进 staging，可以检验监控、恢复、降级和依赖隔离是否真的有效，也能补足单元测试、集成测试和常规功能验收无法覆盖的环境风险。

来源把开源的 Chaos Monkey、Simian Army 以及商业混沌工程工具作为例子，说明这类方法可以从工具化故障注入开始，但最终服务的是更高可用性和更好的用户体验。
