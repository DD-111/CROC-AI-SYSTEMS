# MAIC Artifact Notice / 公开制品说明

## 中文

### 为什么需要这个公开仓库？

MAIC（及类似智慧城市 / AI 竞赛）通常要求参赛者提供 **Public Artifact Link**：

- 仓库必须为 **公开（Public）**
- 评审方应能查看 **超过 3 天的 Commit 历史**
- 用于证明项目持续开发与真实存在

### 本仓库与私有代码的关系

| 维度 | 本公开仓库 | 公司私有仓库 |
|------|-----------|-------------|
| 目的 | 评审制品、架构说明、示例代码 | 生产部署、固件、完整 API |
| 代码完整度 | 桩代码 + 示例 JSON | 完整实现（万级设备目标） |
| 密钥 / 配置 | 无 | `.env`、MQTT 密码、OTA Token 等 |
| 固件 | 无 `.bin` | ESP32 完整固件与 NVS 工具 |
| 更新频率 | 按评审节点维护 | 持续 CI/CD |

**结论：** 评审方通过本链接了解 **能力边界与架构设计**；**真实可部署系统** 在私有环境中运行，不对公众开放。

### 评审方可验证的内容

1. README 中的系统架构与 MAIC 展示卡片
2. `samples/` 中的事件与遥测样例
3. `src/` 中的示例数据流（桩代码）
4. Git 历史 ≥ 3 天，体现持续迭代

### 评审方无法从此仓库获得的内容

- 生产固件二进制
- 完整 Dashboard SPA 源码
- 数据库 Schema 与 Alembic 迁移
- CAO V3 完整 Runtime 实现
- 海康 / 大华抓图的完整边缘上传模块

如需现场演示或深度技术尽调，请通过官方渠道预约 **私有 staging 环境** 访问。

---

## English

### Why this public repository exists

MAIC and similar Smart City competitions require a **Public Artifact Link** with:

- A **public** GitHub (or equivalent) repository
- **Commit history spanning more than 3 days**
- Evidence of ongoing development

### Relationship to private codebases

This repo is a **curated public artifact**. The company's **production-grade implementations** of Croc Sentinel and Croc AI Orchestrator live in **private repositories** and are not published here.

| Public artifact | Private repos |
|-----------------|---------------|
| Architecture docs, sample stubs | Full FastAPI services, firmware, Docker stacks |
| Demo JSON events | Real MQTT brokers, OTA pipelines, Key Vault |
| MAIC capability description | CAO, enrich API, Hik/Dahua edge fetch |

### What reviewers can verify here

- System design and extensibility roadmap
- Sample alarm → AI enrich data flow
- Multi-day git commit history

### What is intentionally not published

- Production firmware binaries
- API keys and `.env` templates with real secrets
- Complete agent orchestration runtime
- Commercial deployment playbooks

For live demos or technical due diligence, contact us for **private staging access**.
