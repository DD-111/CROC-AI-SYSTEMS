# Croc Platform — Public Artifact Repository

**Croc Nexus AI Technologies · MAIC Nexus Challenge 2026 Artifact Link**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **重要声明 / Important Notice**  
> 本仓库为 **公开制品（Public Artifact）**，仅用于 **MAIC Nexus Challenge 2026** 所需的 Artifact Link 与能力说明。  
> **公司全部核心代码、固件、生产配置、密钥与商业实现均位于 Private 仓库**，不在此公开。  
> This repository is a **curated public artifact** for competition review only.  
> **All production code, firmware, secrets, and commercial implementations remain private.**

📄 **MAIC 提交文档 PDF：** [`docs/MAIC-Nexus-Challenge-2026-Croc-Sentinel.pdf`](docs/MAIC-Nexus-Challenge-2026-Croc-Sentinel.pdf)  
📋 **PDF 结构化摘要：** [`docs/MAIC_SUBMISSION.md`](docs/MAIC_SUBMISSION.md)

---

## MAIC 2026 提交摘要 / Submission at a Glance

| 项目 | 内容 |
|------|------|
| **产品** | Croc Sentinel — AI-Powered Emergency Response & Smart Monitoring Platform |
| **赛道** | AI Public Services & Smart City |
| **状态** | **Production-ready** — 真实 IoT 硬件 + 云端 API + iOS/Android App |
| **告警送达** | **3–30 秒**（信号自适应），约为电话树的 **10×** |
| **核心差异** | 唯一组合：**IoT + Interactive GIS + AI 视觉评估 + 移动指挥 App** |

**目标公共设施：** 学校与校园 · 医院 · 政府楼宇 · 市政 CCTV（DBKL）· 社区中心 · 公交枢纽

```text
Trigger → Cloud+AI → Alert → Respond
  按钮/传感器    分类+危险评分   推送全体操作员   地图/GPS/撤防
```

---

## 关于我们 / About Us

**Croc Nexus AI Technologies** — 专注于 **硬件 + 软件一体化** 的 AI 科技公司，核心方向包括：

| 领域 | 说明 |
|------|------|
| **AI Agent & Agent Teams** | 多 Agent 编排、CAO（Chief Agent Orchestrator）操作系统、工具/技能插件化 |
| **数字孪生 Digital Twin** | 设备、园区、事件流的实时映射与可观测性 |
| **AI 法律 AI Law** | 合规审查、审批框架、可审计决策链 |
| **cMax 工作平台** | 2D / 3D 可观测性 AI 工作台，统一运维、编排与智能分析视图 |

本公开仓库展示的是 **Croc Sentinel（物联网告警平台）** 与 **Croc AI Orchestrator（应急事件 AI 编排平台）** 的 **架构概览与示例代码**，不代表完整私有代码库。

---

## 系统全景 / System Overview

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                         Croc Platform Ecosystem                        │
├──────────────────────────────┬──────────────────────────────────────────┤
│   Croc Sentinel (Private)    │   Croc AI Orchestrator (Private)         │
│   · ESP32 全球接入            │   · Agent 流水线 v2                       │
│   · MQTT / OTA / 多租户       │   · CAO 多模型编排                        │
│   · 海康 / 大华 报警抓图       │   · 规则 + LLM 混合推理                   │
│   · App / 邮件 / Telegram     │   · 可靠队列 / Outbox / Follow-up SLA    │
│   · 设备组联动响铃             │   · 与 Sentinel AI Enrich 同机集成        │
└──────────────────────────────┴──────────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  cMax 2D/3D 平台  │  ← 可观测性、数字孪生、Agent 团队视图
                    └──────────────────┘
```

### Croc Sentinel — 四层架构（MAIC 提交版）

| 层级 | 内容 |
|------|------|
| **L1 Edge IoT** | ESP32 边缘：紧急按钮、运动传感器、警笛；QR 分钟级激活 |
| **L2 Cloud API** | 安全 API、Live Streaming、Push Gateway、RBAC、跨机构组共享 |
| **L3 Mobile App** | iOS/Android 原生指挥中心：GIS 地图、事件时间线、ARM ALL / DISARM ALL |
| **L4 AI Engine** | 视觉威胁评分、最近响应人调度、超时自动电话升级 |

**私有库额外能力（未公开）：** 海康 / 大华报警抓图、OTA、MQTT TLS、多租户控制台、邮件 / Telegram

### Croc AI Orchestrator — 应急事件 AI 编排

- **自研轻量编排内核**（无 CrewAI / LangGraph 依赖）
- **7-Agent 流水线**：Risk ∥ Vision → Summary → Commander → Responder → Communication → Follow-up
- **CAO（Chief Agent Orchestrator）**：任务分解、多模型辩论、共识门控、审查输出
- **混合推理**：规则基线 + LLM 增强，LLM 不可用时自动降级
- **生产级能力**：可靠队列、Transactional Outbox、多租户 RBAC、Postgres 分区、Redis HA
- **同机集成**：`POST /v1/enrich/alarm` 为 Croc Sentinel 提供 2.5s 预算内的 AI 增强

---

## 扩展路线图 / Extensibility Roadmap

本平台采用 **插件化 Agent + 工具注册表 + 事件总线** 架构，具备极强的横向扩展能力：

| 扩展方向 | 接入方式 | 状态 |
|----------|----------|------|
| **无人机巡检 / Drone Patrol** | 新设备类型 + Vision Agent + 地理围栏 Skill | 架构预留 |
| **具身智能 / Embodied AI** | CAO Worker + 执行 Agent + 审批框架 | 架构预留 |
| **移动 SOS 警报 / Mobile SOS** | FCM / Twilio + Communication Agent + 升级 SLA | 部分能力已有 |
| **智慧园区 / Smart Campus** | 数字孪生 + 多传感器关联 + 响应人推荐 | 规划中 |
| **AI 法律合规 / AI Law** | Reviewer Agent + Approval Framework + 审计链 | CAO V3 已设计 |
| **cMax 3D 可观测性** | 事件流 → 2D/3D 工作台实时渲染 | 平台方向 |

> 扩展无需重构核心：新增 `plugins/*/agents.py`、`plugins/*/skills.py` 或注册 Security Agent 即可接入新场景。

---

## MAIC 展示能力 / MAIC Demo Capabilities

基于私有代码库的设计与 staging 验证，决赛可展示三块能力卡片：

```text
┌─ AI Incident ────────────────────────┐
│ Category: Emergency    Risk: 89/100  │
│ Confidence: 92%                        │
│ Reason: Repeated · Weak signal ·       │
│         No ack · No camera image       │
│ Action: Check Hik/Dahua · Dispatch     │
│ Status: Awaiting approval              │
└──────────────────────────────────────┘

┌─ Responder ──────────────────────────┐
│ John Tan · 230 m · Response rate 94% │
└──────────────────────────────────────┘

┌─ Escalation ─────────────────────────┐
│ No response 15 s → Escalate Tier-2   │
│ (Twilio SMS to duty manager)         │
└──────────────────────────────────────┘
```

**原则：自动建议、人工批准** — 符合安防与智慧城市合规要求。

### AI 能力矩阵（13 项，P0–P3）

| 优先级 | 能力 | 要点 |
|--------|------|------|
| P0 | 事件分类 | Emergency / Security / Maintenance / Fault / Test |
| P0 | 风险评分 | 0–100 分，规则可审计 |
| P0 | 原因说明 | 可解释条目，非黑盒 |
| P0 | 建议步骤 | 查图 → 联系人 → 15 秒无确认升级 |
| P1 | 响应人推荐 | 距离、在岗、历史响应速度 |
| P1 | 升级预测 | 15 秒无确认 → Tier-2 |
| P1 | 误报识别 | 时间规律 + 置信度 |
| P1 | 设备健康预测 | 电池 / 信号 / 心跳趋势 |
| P2 | 事件摘要 | 3–5 句人话总结 |
| P2 | 多事件关联 | 报警 + 抓图 + 门磁 → 疑似入侵 |
| P2 | 图像分析 | Hik/Dahua JPEG 视觉检测 |
| P3 | AI 调度 | 谁 / 何时 / 何渠道；默认待人批准 |
| P3 | 资源推荐 | 急救员、保安、最近 AED 等 |

---

## 本仓库内容 / What's in This Repo

| 路径 | 说明 |
|------|------|
| [`docs/MAIC-Nexus-Challenge-2026-Croc-Sentinel.pdf`](docs/MAIC-Nexus-Challenge-2026-Croc-Sentinel.pdf) | **MAIC 2026 正式提交文档（12 页）** |
| [`docs/MAIC_SUBMISSION.md`](docs/MAIC_SUBMISSION.md) | PDF 结构化摘要（中英） |
| [`docs/PRODUCT_OVERVIEW.md`](docs/PRODUCT_OVERVIEW.md) | 产品一页总览 |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | 双系统架构说明（公开版） |
| [`docs/EXTENSIBILITY.md`](docs/EXTENSIBILITY.md) | 扩展场景与插件接入指南 |
| [`docs/MAIC_ARTIFACT_NOTICE.md`](docs/MAIC_ARTIFACT_NOTICE.md) | 公开制品与私有代码边界说明 |
| [`samples/`](samples/) | 示例 JSON 事件与遥测数据 |
| [`src/croc_orchestrator/`](src/croc_orchestrator/) | Orchestrator 示例桩代码（非生产） |
| [`src/croc_sentinel/`](src/croc_sentinel/) | Sentinel 示例桩代码（非生产） |

**本仓库不包含：** 生产固件、`.env` 密钥、完整 API 实现、数据库迁移、Docker 生产栈。

---

## 快速体验示例 / Quick Sample

```bash
# 克隆公开制品仓库
git clone https://github.com/<your-org>/croc-platform-artifact.git
cd croc-platform-artifact

pip install -r requirements.txt

# 运行示例编排（桩代码，仅演示数据流）
python -m src.croc_orchestrator.demo_assess samples/orchestrator/alarm_event.json
```

---

## 技术栈摘要 / Tech Stack Summary

| 组件 | Croc Sentinel | Croc AI Orchestrator |
|------|---------------|----------------------|
| 设备端 | ESP32 (Arduino / ESP-IDF) | — |
| 消息 | MQTT (Mosquitto / EMQX) | Redis 队列 + Outbox |
| 后端 | FastAPI + SQLite/PG | FastAPI + PostgreSQL |
| AI | 云端 Qwen 双模型（规划） | 自研 CAO + 混合推理 |
| 部署 | Docker Compose | Docker Compose + Nginx HA |
| 可观测 | cMax 2D/3D 工作台 | Prometheus + OpenTelemetry |

---

## 落地阶段 / Implementation Phases

| 阶段 | 内容 | 状态 |
|------|------|------|
| **Phase 1 · Now** | IoT 边缘、GIS Dashboard、双通道告警、移动 App、AI 视觉威胁评估、QR 激活、ARM ALL | ✅ 生产运行（MAIC 提交） |
| **Phase 2 · 2026** | AI 异常检测、CCTV 关联、市政分析 Dashboard | 📋 规划中 |
| **Phase 3 · 2027+** | 应急调度 API、马来西亚紧急服务集成、全国市政推广 | 📋 规划中 |
| **平台扩展** | 无人机 / 具身智能 / 移动 SOS / cMax 3D / AI 法律 | 架构预留（Orchestrator 私有库） |

---

## 许可证 / License

本公开制品仓库采用 [MIT License](LICENSE)。  
私有生产代码与固件受公司内部许可策略约束，未经授权不得使用。

---

## 联系 / Contact

| | |
|--|--|
| **公司** | Croc Nexus AI Technologies |
| **邮箱** | partnerships@crocnexus.com |
| **电话** | +084-349525 |
| **Artifact** | 本公开仓库供 MAIC 评审；核心开发在 Private 仓库 |

---

*Version 2026-06-19 · Public Artifact · 私有实现为准 / Private implementation is source of truth*
