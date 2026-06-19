# Croc Sentinel + AI — Product Overview (Public)

> 整合自内部产品文档，供 MAIC / 智慧城市评审阅读。  
> Synthesized from internal product documentation for public review.

## 一句话 / One-liner

**Croc Sentinel** 是多租户联网报警平台；**Croc AI Orchestrator** 是应急事件 AI 编排层。  
两者同机集成，为园区 / 楼宇 / 智慧城市场景提供 **设备联动 → 证据链 → AI 研判 → 人工批准** 的完整闭环。

## 现有能力（私有库已实现）

- ESP32 全球 MQTT 接入，同组设备联动响铃
- 多租户隔离（superadmin → admin → user）
- FCM / 邮件 / Telegram 异步通知
- 海康 Hikvision + 大华 Dahua 报警抓图（ESP32 局域网边缘上传）
- OTA 固件升级、出厂登记、运维地图
- AI Enrich API 与 7-Agent 编排流水线（Orchestrator 私有库）

## 后续 AI 层（设计对齐）

| 能力 | 说明 |
|------|------|
| 事件分类 | Emergency / Security / Maintenance / Fault / Test |
| 风险评分 | 0–100，规则可审计 |
| Qwen 双模型 | Fast 全覆盖文案；Deep 仅高危异步 |
| 图像分析 | Hik/Dahua JPEG，CV 模型（非 LLM） |
| 升级 SLA | 15 秒无确认 → Tier-2（Twilio 短信扩展） |

## 扩展方向

- 无人机巡检、具身智能、移动 SOS
- 数字孪生 + cMax 2D/3D 可观测性工作台
- AI 法律合规审查与审批框架

## 评审原则

**自动建议、人工批准** — 高危调度动作默认 `Awaiting approval`。

---

*This document is part of the public artifact. Production code remains private.*
