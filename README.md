<p align="center">
  <img src="assets/images/logo-croc-nexus-4k.png" alt="Croc Nexus AI Technologies" width="400" />
</p>

<h1 align="center">Croc Nexus AI Technologies</h1>

<p align="center">
  <strong>An AI startup — smarter site alerts, faster response, full accountability</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/AI-Startup-7c3aed" alt="AI Startup" />
  <img src="https://img.shields.io/badge/Platform-In%20production-16a34a" alt="In production" />
</p>

<br/>

> **AI-first, not bolt-on.** We use AI to **understand events**, **score urgency**, **call the right person**, and **escalate** — with humans in control.  
> **Site requirement:** working network (Wi‑Fi or wired) at each location.

<br/>

---

## How AI changes response

| Old way | With Croc Nexus AI |
|:--------|:-------------------|
| Every alarm feels equally urgent | **Urgency score (0–100)** with plain-language reasons |
| Staff wait and guess | AI **calls admin or agent** to go check |
| Wrong person gets pinged | AI **routes by role, zone, and availability** |
| Camera footage unused | **Linked images** support the decision when available |
| Chain breaks if no answer | **Auto-escalation** to the next contact |
| No record of actions | Full **audit log** of AI and human steps |
| One-size-fits-all rules | **Per-site** scoring, call lists, and escalation |

---

## Why us

| | |
|:--|:--|
| **AI-native** | Recognition, scoring, routing, and calls are the product — not an add-on |
| **People in charge** | AI handles routine steps; **humans approve** what matters |
| **Rules first** | Fixed safety rules always run; AI never lowers urgency silently |
| **Wholly ours** | Platform, apps, cloud, and AI — **owned and operated by Croc Nexus only** |
| **CAO** | In-house small model in training — **exclusive, not open** |
| **Roadmap** | People today → **embodied intelligence, drones, security devices**, and more |

**Contact:** partnerships@crocnexus.com · +084-349525

---

## Products

<table>
<tr>
<td width="50%" valign="top">

### Croc Sentinel *(live)*
AI-powered site monitoring

- Event recognition on the map  
- **3–30 s** alerts to phones  
- Automatic calls to admin or agent  
- Camera context when linked  
- iPhone & Android apps  

</td>
<td width="50%" valign="top">

### Croc Coordination
AI that turns alerts into action

- Urgency score + readable reasons  
- Who to call and what to do first  
- Escalation if nobody answers  
- Human approval before sensitive steps  
- Full audit trail  

</td>
</tr>
</table>

### CAO *(internal, not open)*

Compact in-house model for deeper coordination — scoring, routing, follow-up. **Croc Nexus exclusive**; not licensed or rebranded. Production sites use **rules + Coordination** today.

---

## Scenes

Government buildings · malls · hospitals · plazas · parks · roads · traffic junctions · commercial districts · campuses · residential · *personal / home use on roadmap*

---

## Response flow

```text
  Event detected
       │
       ▼
  AI recognises + scores urgency
       │
       ├── Call + app alert to admin or agent
       └── Audit log
       │
       ▼
  Person checks on site          ← today
       │
       ▼
  Machines & devices on site     ← roadmap
  (embodied AI · drones · security equipment · more)
```

| Step | What AI does |
|:-----|:-------------|
| **Understand** | Classify event type — emergency, security, maintenance, etc. |
| **Score** | 0–100 urgency with reasons anyone can read |
| **Route** | Call the right administrator or assigned agent |
| **Escalate** | Next contact if no answer |
| **Record** | Timestamp every AI decision and human action |

**Later (step by step per site):** same AI brain can also route **embodied systems**, **drones**, and **on-site security devices** — still logged, human-gated where it counts. Details in [docs/EXTENSIBILITY.md](docs/EXTENSIBILITY.md).

---

## Platform

<p align="center">
  <img src="assets/images/architecture-four-layers.svg" alt="Cloud, mobile app, and AI layer" width="720" />
</p>

| Layer | Role |
|:------|:-----|
| **Cloud** | Recognition, scoring, routing, escalation |
| **Mobile app** | Map, timeline, alerts, approvals — **Croc Nexus apps only** |
| **AI** | Understand events, pick who to call, plan follow-up |

We configure **rules, call lists, and escalation per site** on our stack. We do **not** offer white-label or customer-branded apps. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and [docs/PRODUCT_OVERVIEW.md](docs/PRODUCT_OVERVIEW.md).

---

## Mobile app

<p align="center">
  <img src="assets/images/app-overview-dashboard.jpeg" alt="Home" width="220" />
  &nbsp;&nbsp;
  <img src="assets/images/app-events-timeline.jpeg" alt="Events" width="220" />
  &nbsp;&nbsp;
  <img src="assets/images/app-device-activation.jpeg" alt="Add device" width="220" />
  &nbsp;&nbsp;
  <img src="assets/images/app-signals-routing.jpeg" alt="Activity" width="220" />
</p>

<p align="center"><sub>Map · events · setup · activity</sub></p>

---

## Repository

```bash
git clone https://github.com/DD-111/CROC-AI-SYSTEMS.git
```

| Folder | Contents |
|:-------|:---------|
| `docs/` | Architecture, product overview, extensibility |
| `assets/` | Logo and app imagery |
| `samples/` | Example event data |
| `src/` | Shared helpers |

---

<p align="center">
  <strong>Croc Nexus AI Technologies</strong><br/>
  partnerships@crocnexus.com · +084-349525<br/>
  <sub>© Croc Nexus AI Technologies · <a href="LICENSE">MIT License</a></sub>
</p>
