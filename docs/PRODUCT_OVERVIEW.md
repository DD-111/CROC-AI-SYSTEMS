# Croc Sentinel + AI — Product Overview (Public)

> 基于 [`MAIC-Nexus-Challenge-2026-Croc-Sentinel.pdf`](MAIC-Nexus-Challenge-2026-Croc-Sentinel.pdf) 与内部技术文档整理。  
> Derived from the MAIC submission PDF and internal engineering docs.

## 一句话 / One-liner

**Croc Sentinel** 是 Croc Nexus AI Technologies 面向公共设施的 **生产级、移动优先 IoT 安防与智慧监控平台**；**Croc AI Orchestrator** 为其 AI Engine 层提供多 Agent 编排与混合推理能力。

## MAIC 2026 定位

- **赛事：** MAIC Nexus Challenge 2026
- **赛道：** AI Public Services & Smart City
- **状态：** 真实 IoT 硬件 + 云端 API + iOS/Android App **已上线运行**，非概念原型

## 四层架构（提交文档）

1. **Edge IoT** — ESP32 边缘：按钮、传感器、警笛；QR 分钟级激活
2. **Cloud API** — 安全 API、Live Streaming、Push、RBAC、跨机构组共享
3. **Mobile App** — GIS 多站点地图、事件时间线、ARM ALL / DISARM ALL、GPS 巡逻
4. **AI Engine** — 视觉威胁评分、最近响应人、电话自动升级（Orchestrator 私有库深度编排）

## 核心指标

| 指标 | 值 |
|------|-----|
| 告警送达 | 3–30 秒（信号自适应） |
| vs 电话树 | ~10× 更快 |
| 工具整合 | 1 App 替代 3–5 套碎片化工具 |
| 地图规模 | 100+ 站点单图可见 |

## 目标场景

学校与校园 · 医院 · 政府楼宇 · 市政 CCTV（含 DBKL）· 社区中心 · 公共交通枢纽

## 应急四阶段

`Trigger → Cloud+AI → Alert → Respond` — 全链路审计，无电话树延迟。

## 私有库已实现（未在此公开）

- ESP32 MQTT 全球接入、同组联动响铃、多租户隔离
- FCM / 邮件 / Telegram；海康 / 大华报警抓图
- OTA、出厂登记、运维控制台与地图
- Croc AI Orchestrator：7-Agent 流水线、CAO、Enrich API
- cMax 2D/3D 可观测性工作台（平台方向）

## 扩展路线

| 时间 | 内容 |
|------|------|
| Phase 2 · 2026 | AI 异常检测、CCTV 关联、市政分析 Dashboard |
| Phase 3 · 2027+ | 应急调度 API、全国市政推广 |
| 架构预留 | 无人机、具身智能、移动 SOS、数字孪生、AI 法律合规 |

## 联系

- **Email:** partnerships@crocnexus.com
- **Phone:** +084-349525

---

*Public artifact only. Production code remains private.*
