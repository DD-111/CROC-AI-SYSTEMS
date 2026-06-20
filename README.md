<p align="center">
  <img src="assets/images/logo-croc-nexus-4k.png" alt="Croc Nexus AI Technologies" width="420" />
</p>

<h1 align="center">Croc Nexus AI Technologies</h1>

<p align="center">
  <strong>Integrated hardware, software, and AI for public safety and smart operations</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/Status-Production-success" alt="Production" />
</p>

---

## Company

**Croc Nexus AI Technologies** builds end-to-end systems that connect field devices, cloud services, mobile operations, and AI decision support.

| Focus | What we do |
|-------|------------|
| **Hardware & IoT** | ESP32 edge devices, sensors, sirens, secure cloud connectivity |
| **AI Agents** | Multi-agent orchestration, tool plugins, hybrid rules + LLM inference |
| **Digital Twin** | Live maps, device state, and event streams across sites |
| **AI Law & Compliance** | Approval workflows, audit trails, human-in-the-loop controls |
| **cMax Platform** | 2D / 3D observability workbench for ops and analytics |

**Contact:** partnerships@crocnexus.com · +084-349525

---

## Platform

CROC AI Systems brings three products together:

| Product | Role |
|---------|------|
| **Croc Sentinel** | IoT alarm platform — devices, cloud API, mobile command app |
| **Croc AI Orchestrator** | Event intelligence — classification, risk scoring, routing, escalation |
| **cMax** | Observability layer — dashboards, maps, agent and system visibility |

---

## Croc Sentinel

Mobile-first security and monitoring for schools, hospitals, government sites, and municipal networks.

**Core capabilities**

- Multi-site **GIS dashboard** with live alarm pins
- **3–30 second** alert delivery (push + live stream)
- Native **iOS & Android** command app
- Multi-tenant **RBAC** and cross-agency group sharing
- Camera-linked evidence (Hikvision / Dahua edge capture)
- QR device onboarding and OTA firmware management

<p align="center">
  <img src="assets/images/architecture-four-layers.svg" alt="Four-layer architecture" width="860" />
</p>

| Layer | Description |
|-------|-------------|
| **Edge IoT** | Panic buttons, sensors, sirens — ESP32 fleet |
| **Cloud API** | Secure API, live streaming, push gateway, tenant isolation |
| **Mobile App** | GIS map, event timeline, ARM ALL / DISARM ALL, GPS patrol |
| **AI Engine** | Threat scoring, smart routing, responder dispatch, phone escalation |

**Response pipeline:** Trigger → Cloud + AI → Alert → Respond

---

## Croc AI Orchestrator

Self-hosted agent platform for emergency and operational workflows.

- **Agent pipeline:** risk & vision analysis → summary → commander → responder → communication → follow-up
- **CAO (Chief Agent Orchestrator):** planning, multi-model routing, consensus, and review
- **Hybrid inference:** rules-first baseline with LLM enhancement; graceful fallback when models are unavailable
- **Local & cloud models:** auto-discovery of Ollama and OpenAI-compatible endpoints; task-based routing
- **Production patterns:** reliable queues, outbox delivery, follow-up SLA, multi-tenant API keys

---

## Mobile App

<p align="center">
  <img src="assets/images/app-overview-dashboard.jpeg" alt="Overview dashboard" width="240" />
  &nbsp;
  <img src="assets/images/app-events-timeline.jpeg" alt="Event timeline" width="240" />
  &nbsp;
  <img src="assets/images/app-device-activation.jpeg" alt="Device activation" width="240" />
  &nbsp;
  <img src="assets/images/app-signals-routing.jpeg" alt="Signals and routing" width="240" />
</p>

Overview · Events · Device activation · Signals & routing

---

## AI Features

- Event classification and **0–100 risk scoring** (auditable rules)
- Visual threat assessment from camera captures
- Nearest-responder notification and timed escalation
- Explainable reasons and recommended actions
- **Human approval** for high-impact decisions

---

## Extensibility

The platform is designed to grow without rewriting the core:

- Drone patrol and aerial vision
- Embodied robotics and field automation
- Mobile SOS and multi-channel alerts
- Smart campus and city-wide digital twin views
- Legal/compliance review agents

Plugin agents, skills, and tools extend behavior per domain.

---

## Tech Stack

| Area | Stack |
|------|-------|
| Edge | ESP32 (Arduino / ESP-IDF) |
| Messaging | MQTT, Redis queues |
| Backend | FastAPI, PostgreSQL / SQLite |
| AI | Ollama, OpenAI-compatible APIs, custom agent runtime |
| Mobile | Native iOS & Android |
| Deploy | Docker Compose, Nginx |
| Observability | cMax 2D/3D, Prometheus, OpenTelemetry |

---

## Repository

```
docs/          Architecture and product documentation
assets/        Brand and product imagery
samples/       Reference event payloads
src/           Shared libraries and integration helpers
```

```bash
git clone https://github.com/DD-111/CROC-AI-SYSTEMS.git
```

---

## License

[MIT License](LICENSE) · © Croc Nexus AI Technologies
