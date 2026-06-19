# MAIC Nexus Challenge 2026 — Submission Summary

> 完整提交文档 PDF：[`MAIC-Nexus-Challenge-2026-Croc-Sentinel.pdf`](MAIC-Nexus-Challenge-2026-Croc-Sentinel.pdf)  
> Full submission PDF linked above.

| 字段 | 内容 |
|------|------|
| **赛事** | MAIC Nexus Challenge 2026 — Malaysia AI Innovation Platform |
| **赛道** | AI Public Services & Smart City |
| **产品** | Croc Sentinel — AI-Powered Emergency Response & Smart Monitoring Platform |
| **公司** | Croc Nexus AI Technologies |
| **状态** | Production-ready（真实硬件 + 云端 API + iOS/Android App） |

---

## Executive Summary / 执行摘要

Croc Sentinel 是面向马来西亚公共基础设施与智慧城市的 **移动优先 IoT 安防平台**。它将紧急按钮、运动传感器、警笛与 CCTV 触发器接入统一云端，在 iOS / Android 上提供实时指挥中心，配合 **Interactive GIS 多站点地图**，告警推送在 **3–30 秒**内送达（随信号强度自适应）。

与面向单栋商业楼宇的传统系统不同，Croc Sentinel 支持 **多站点、多机构** 监控——学校、医院、政府楼宇与市政 CCTV 网络可在保持 RBAC 的前提下共享设备组。

| 指标 | 数值 |
|------|------|
| 告警送达 | 3–30 秒（信号自适应） |
| 监控 | 24/7 连续 |
| 地图 | 多站点 GIS Dashboard |
| 移动端 | iOS + Android 原生 App |

---

## Problem Statement / 问题陈述

公共设施面临 **碎片化安防系统** 危机：CCTV、报警、传感器各自为政，电话树延迟 5–15 分钟，缺乏跨站点地图视图，企业级方案价格过高。

**典型场景：** 学校走廊 23:00 运动传感器触发，保安手机未收到告警——传感器与通知分属不同平台，12 分钟后才到场。Croc Sentinel 旨在将告警在 **3–30 秒** 内送达所有授权操作员。

---

## Why Croc Sentinel / 竞争优势

| 能力 | 传统系统 | Croc Sentinel |
|------|----------|---------------|
| 告警速度 | 5–15 分钟（电话树） | **3–30 秒**（推送 + Live Stream） |
| 多站点 GIS | ✗ | ✓ 实时告警 Pin |
| 移动指挥 | 桌面为主 | ✓ 完整 iOS / Android App |
| AI 事件智能 | 人工盯屏 | ✓ 摄像头 AI 评分 + 自动电话升级 |
| 部署成本 | 企业级高价 | ✓ 公共部门可负担的 IoT 边缘硬件 |
| 上线状态 | 数月部署 | ✓ **已生产运行** — QR 激活 |

**唯一组合：** 生产 IoT 部署 + Interactive GIS 多站点指挥 + AI 视觉威胁评估 + 移动 App。

---

## Solution Architecture / 四层架构

```text
LAYER 1 — Edge IoT        传感器、紧急按钮、警笛、继电器；QR 激活
LAYER 2 — Cloud API       安全 API、Live Streaming、Push Gateway、RBAC、跨机构组共享
LAYER 3 — Mobile App      原生指挥中心：GIS 地图、事件时间线、ARM ALL / DISARM ALL、GPS 巡逻
LAYER 4 — AI Engine       视觉威胁评分、智能路由、电话自动升级
```

**数据流：**

- 上行：Edge → Cloud Hub → AI 分类 → Live Broadcast + Push
- 下行：Mobile App → Cloud API → Device Command（布防 / 撤防 / 警笛）
- 双通道冗余：Live Stream + Push，单通道失败仍可送达

---

## Emergency Flow / 四阶段应急流程

```text
1 Trigger  →  2 Cloud+AI  →  3 Alert  →  4 Respond
  按钮/传感器      分类+危险评分      推送全体操作员    地图 Pin / GPS / 撤防
```

| 阶段 | 内容 |
|------|------|
| **Trigger** | 边缘设备检测按钮 / 运动 / 警笛，毫秒级上报云端 |
| **Cloud + AI** | 事件分类、摄像头抓图 AI 危险系数、按区域与机构规则路由 |
| **Alert** | Live Stream 更新所有在线会话 + Push 深链到后台 App |
| **Respond** | GIS 地图告警 Pin、时间线审查、ARM ALL 全校警笛、GPS 巡逻调度、完整审计日志 |

**适用场景：** 学校与校园、医院、市政 CCTV、政府与社区中心。

---

## AI & Intelligent Features / AI 智能能力

```text
Capture → Score → Notify → Call
  摄像头抓图   AI 危险系数   最近响应人推送   超时未撤防自动电话
```

| 能力 | 说明 |
|------|------|
| **视觉威胁评估** | 报警时抓图，AI 计算低→危急危险系数 |
| **自主决策** | 区分误报 / 低优先级 / 真实威胁，减少告警疲劳 |
| **最近响应人调度** | 高危时 Push 最近可用操作员到场撤防 |
| **电话升级** | 可配置提醒窗口后仍未撤防 → 自动拨打值班电话 |
| **智能路由** | 按区域、机构、角色映射通知组 |
| **完整审计** | Capture → Analyse → Escalate → Follow-up → Log 全链路时间戳 |

**未来路线：** 事件时间线异常检测、自动化合规报告、预测性设备健康评分。

---

## Smart City Impact / 智慧城市影响

| 影响维度 | 说明 |
|----------|------|
| **公共安全** | 3–30 秒同步通知所有授权响应人 |
| **多机构协同** | DBKL、学校董事会、医院管理员跨机构共享而不替换现有硬件 |
| **运营效率** | 一个 App 替代 CCTV 查看器 + 报警面板 + 传感器面板 + 电话树 |
| **数字包容** | 低成本 IoT 硬件让公立学校与社区中心也能负担智能安防 |
| **合规审计** | 时间戳事件时间线满足市政事故报告与监管要求 |

| 指标 | 价值 |
|------|------|
| 告警速度提升 | **10×** vs 电话树 |
| 工具整合 | **1 App 替代 3–5 套工具** |
| 规模 | **100+ 站点** 单地图可见 |

---

## Development Roadmap / 发展路线

| 阶段 | 时间 | 内容 |
|------|------|------|
| **Phase 1 · Now** | 当前 | IoT 边缘、GIS Dashboard、双通道告警、iOS/Android App、AI 视觉威胁评估、QR 激活、ARM ALL / DISARM ALL、GPS 巡逻 |
| **Phase 2 · 2026** | 2026 | 事件时间线 AI 异常检测；CCTV 与现场传感器关联；市政分析 Dashboard（热力图、响应时间指标） |
| **Phase 3 · 2027+** | 2027+ | 开放 API 对接应急调度系统；马来西亚紧急服务集成；与州政府 / 市政委员会全国推广 |

### 平台扩展能力（私有架构预留）

在 Croc AI Orchestrator + cMax 平台上，可进一步扩展至：

- **无人机巡检** — 航拍视觉 + 地理围栏 Agent
- **具身智能** — CAO 执行 Agent + 审批门控
- **移动 SOS** — FCM / Twilio + 升级 SLA
- **数字孪生** — cMax 2D/3D 可观测性工作台
- **AI 法律** — Reviewer Agent + 多阶段审批框架

---

## Team & Contact / 团队与联系

| 角色 | 专长 |
|------|------|
| IoT Engineering | 边缘固件、传感器集成、QR 激活 |
| Cloud Development | Live Streaming、Push Gateway、多租户认证 |
| Mobile App Design | Interactive GIS、Push、响应式 UI |
| AI Integration | 视觉威胁评分、智能路由、自动电话 |
| Public Safety | 学校、医院、政府、CCTV 场景 |
| Smart City | 多机构协同与市政规模扩展 |

| 联系 | |
|------|--|
| **公司** | Croc Nexus AI Technologies |
| **邮箱** | partnerships@crocnexus.com |
| **电话** | +084-349525 |

---

## Public vs Private / 公开与私有边界

本 Markdown 与 PDF 为 **MAIC 评审公开材料**。  
**完整生产代码、固件二进制、密钥与商业部署** 位于 **Private 仓库**，详见 [`MAIC_ARTIFACT_NOTICE.md`](MAIC_ARTIFACT_NOTICE.md)。

私有技术栈还包括 **Croc AI Orchestrator**（7-Agent 应急编排 + CAO 多模型操作系统）与 **cMax** 2D/3D AI 可观测性工作台——为 Sentinel 的 AI Engine 层提供深度 Agent 编排能力。

---

*Source: MAIC-Nexus-Challenge-2026-Croc-Sentinel.pdf · June 2026*
