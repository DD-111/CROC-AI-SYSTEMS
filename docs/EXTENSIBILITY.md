# Extensibility Guide / 扩展性指南

Croc Platform 采用 **事件驱动 + 插件化 Agent** 架构，可在不重构核心的前提下扩展到多种场景。

## 插件接入点

| 接入点 | 路径（私有库） | 用途 |
|--------|---------------|------|
| Tool Plugin | `plugins/*/tools.py` | 自定义数据查询、通知钩子 |
| Skill Plugin | `plugins/*/skills.py` | 领域策略（校区夜间升级等） |
| Agent Plugin | `plugins/*/agents.py` | 新 Worker Agent |
| Security Agent | `agents/security/` | Sentinel 专用安全 Agent |
| MCP Server | CAO `CAO_MCP_SERVERS` | 外部工具（GitHub、Slack 等） |

## 扩展场景

### 无人机巡检 / Drone Patrol

```text
Drone telemetry event → Event Bus → Vision Agent + Geo Skill
                                  → cMax 3D map overlay
                                  → Commander dispatch
```

- 新设备类型注册到 Sentinel MQTT topic schema
- Vision Agent 分析航拍帧（YOLO / 专用 CV 模型）
- 地理围栏 Skill 触发自动巡逻路径调整

### 具身智能 / Embodied AI

```text
CAO Plan → Execution Agent (sandbox) → Approval Gate → Deploy
```

- CAO V2 Execution Agent：`file_editor`, `command_runner`, `git_executor`
- 所有动作生成 provenance；高风险需 `cao_execution_approval_required=true`
- 适用于机器人任务编排、自动化运维脚本

### 移动 SOS 警报 / Mobile SOS

```text
Mobile app SOS → FCM push → Alarm record → AI enrich → Twilio SMS escalate
```

- 已有：FCM 推送、Communication Agent、Follow-up SLA（15s ZSET）
- 扩展：Twilio provider、`mobile_sos` 触发类型、GPS 响应人排序

### 数字孪生 / Digital Twin

```text
Device state stream → cMax 2D/3D renderer → Agent overlay
```

- 实时设备位置、状态、报警热力图
- AI 决策链可视化（CAO provenance → 3D timeline）

### AI 法律 / AI Law

```text
Agent output → Reviewer Agent → Approval Framework → Audit log
```

- Reviewer 五轴审查：正确性、安全、性能、成本、可维护性
- 多阶段审批：deployment_approval, security_approval
- 全链路审计满足合规与事后追溯

## 示例：注册自定义 Skill（公开桩代码）

见 `src/croc_orchestrator/workflow_sample.py` 中的 `school_zone_skill` 示例。

## 设计原则

1. **规则只升不降** — AI 不得降低规则引擎给出的最高风险等级
2. **人工批准门控** — 高危动作默认 `Awaiting approval`
3. **可审计** — 每条决策记录 `agent_provenance`
4. **优雅降级** — LLM 不可用时纯规则输出
5. **租户隔离** — 所有扩展默认继承 `tenant_id` 过滤
