# Architecture

**Croc Nexus AI Technologies** — AI startup. Platform, apps, and AI are **wholly owned by Croc Nexus**.

> Each site needs **network** (Wi‑Fi or wired internet).

---

## Overview

```text
Site equipment ──network──► Cloud (AI + coordination)
                                  │
                                  ├── Croc Nexus mobile apps
                                  ├── phone / email / messaging
                                  └── audit logs
```

| Component | Purpose |
|:----------|:--------|
| **Croc Sentinel** | Monitoring, alerts, camera context, device groups |
| **Croc Coordination** | Urgency scoring, routing, escalation, approval |
| **CAO** | Internal model in training — exclusive to Croc Nexus |

---

## Croc Sentinel

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

## Croc Coordination

```text
Event detected
      ▼
Recognise + score urgency (+ camera if linked)
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

**Today:** people respond on site.  
**Later:** same pipeline can add embodied systems, drones, and security devices — see [EXTENSIBILITY.md](EXTENSIBILITY.md).

---

## Scenes

Government, malls, hospitals, plazas, parks, roads, traffic junctions, commercial zones, campuses, residential — configured per site. Personal / home use on roadmap.

---

## Customisation

Per-site changes (groups, escalation paths, integrations) run on **Croc Nexus–owned** infrastructure only — no white-label apps. We review fit and timeline before committing.

---

## Safety and access

| Topic | Croc Sentinel | Croc Coordination |
|:------|:--------------|:------------------|
| Connections | Encrypted links to cloud | Encrypted access to coordination service |
| Commands | Authorised access only | Permission by role |
| Remote updates | Approved sources only | — |
| Data | Per-customer separation | Per-customer separation |
| History | Full event log | Full decision log |
