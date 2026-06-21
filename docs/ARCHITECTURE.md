# Architecture

**Croc Nexus AI Technologies** — AI startup, Malaysia. Platform wholly owned by Croc Nexus.

> Each site needs **network** (Wi‑Fi or wired internet).

---

## Overview

```text
Site equipment ──network──► Croc Nexus cloud
                                  │
                    ┌─────────────┴─────────────┐
                    ▼                           ▼
           Croc Sentinel Systems      Croc AI Orchestrator
                    │                           │
                    └─────────────┬─────────────┘
                                  ▼
                         Croc Nexus mobile apps
                         phone / messaging alerts
                         audit logs
```

| Product | Purpose | Status |
|:--------|:--------|:-------|
| **Croc Sentinel Systems** | Monitoring, device groups, alerts, camera context | Trial production *(初步试产)* |
| **Croc AI Orchestrator** | Urgency scoring, routing, escalation, approval | Trial production *(初步试产)* |

---

## Croc Sentinel Systems

```text
Equipment at site
      │  network (required)
      ▼
Cloud service
      ├── alerts to phones
      ├── linked camera photos
      └── remote updates
```

- Each customer sees only its own devices and staff  
- Devices in the same group can react together  
- Sensitive credentials are not stored permanently on local equipment  

---

## Croc AI Orchestrator

```text
Event from Sentinel
      ▼
Score urgency (+ camera if linked)
      ├── call admin or assigned agent
      ├── app alert to on-duty staff
      └── audit log
      ▼
Person checks on site
      ▼
Resolve · escalate · record outcome
```

- Fixed rules run first; AI layers add detail when available  
- If smart services are offline, rule-based calls still work  
- Sensitive automated steps wait for human approval  

**Today:** people respond on site. Orchestrator makes *who* and *how fast* clearer.

**In development — not open *(开发中 · 未开放)*:** CAO in-house model; embodied intelligence, drones, and security devices on the same pipeline; personal/home use. See [EXTENSIBILITY.md](EXTENSIBILITY.md).

---

## Scenes

Government, malls, hospitals, plazas, parks, roads, traffic junctions, commercial zones, campuses, residential — configured per site. Personal / home — **in development, not open**.

---

## Customisation

Per-site groups, escalation paths, and integrations on **Croc Nexus–owned** infrastructure only — no white-label apps. We review fit and timeline before committing.

---

## Safety and access

| Topic | Sentinel Systems | AI Orchestrator |
|:------|:-----------------|:----------------|
| Connections | Encrypted links to cloud | Encrypted access to coordination service |
| Commands | Authorised access only | Permission by role |
| Remote updates | Approved sources only | — |
| Data | Per-customer separation | Per-customer separation |
| History | Full event log | Full decision log |
