# Croc Platform Architecture (Public Overview)

> 本文档为公开版架构说明。完整实现见私有仓库。

## 1. Two-System Design

### Croc Sentinel — Edge + Cloud IoT

```text
ESP32 Device ──MQTT(TLS)──► Mosquitto/EMQX
       │                           │
       │ LAN snapshot              ▼
       ▼                    FastAPI API + Dashboard
Hikvision / Dahua                   │
       │                            ├── SQLite/PostgreSQL
       └── JPEG upload ─────────────├── FCM / Email / Telegram
                                     └── OTA nginx (/fw/)
```

**Key properties:**

- Multi-tenant isolation at API layer (`owner_admin` scope)
- Device group linkage: same owner + same group → siren fan-out
- Factory registration: 80-char CSPRNG serial, MAC binding
- Camera credentials never persisted on device flash

### Croc AI Orchestrator — Agent Pipeline

```text
Alarm Event ──► POST /v1/enrich/alarm (HMAC)
                      │
                      ▼
              enrich_orchestration workflow
                      │
    ┌─────────────────┼─────────────────┐
    ▼                 ▼                 ▼
  risk ∥ vision    commander      communication
    │                 │                 │
    └──────── summary ┴ responder ─ follow_up
                      │
                      ▼
              IncidentAssessment JSON
                      │
                      ▼
              Sentinel webhook / Outbox
```

**Key properties:**

- Self-hosted orchestration kernel (no LangGraph dependency)
- Rules-first hybrid inference with LLM fallback
- CAO leader for multi-model debate + consensus + review
- Reliable queue (BRPOPLPUSH) + transactional outbox

## 2. Integration Contract

| Sentinel field | Orchestrator field |
|----------------|-------------------|
| `alarms.id` | `event_id` = `alarm-{id}` |
| `owner_admin` | `tenant_id` |
| device telemetry | `battery`, `rssi`, `trigger_count` |
| snapshot success | `snapshot_exists=true` |

Enrich budget: **2.5 seconds** on same machine (`127.0.0.1:9240`).

## 3. CAO — Chief Agent Orchestrator

Five-layer OS model (private implementation):

1. **Task Intake** — classify incident / software / integration work
2. **Task Planning** — DAG of sub-tasks with dependencies
3. **Agent Assignment** — model router picks best LLM per task type
4. **Multi-Model Debate + Consensus** — threshold 0.75 default
5. **CAO Review** — correctness, security, performance, cost, maintainability

V3 adds: Event Bus, persistent memory (SQLite/PG/Redis), approval framework, security agents.

## 4. cMax Observability Platform

cMax provides 2D/3D views over:

- Device fleet health (online/offline, RSSI, battery)
- Alarm event streams and AI enrichment results
- Agent team execution traces (CAO provenance)
- Digital twin overlays for campus / building deployments

This public repo does not include cMax UI assets.

## 5. Security Layers

| Layer | Sentinel | Orchestrator |
|-------|----------|--------------|
| Transport | MQTT TLS, HTTPS OTA | Nginx TLS, API Key / JWT |
| Command auth | CMD_AUTH_KEY (64-bit) | RBAC scopes |
| OTA | Host allowlist + token | — |
| Tenant | owner_admin isolation | API Key → tenant_id |
| Audit | audit_events table | audit_runs + provenance |
