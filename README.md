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

<p align="center">
  <a href="#about">About</a> ·
  <a href="#products">Products</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#scenes">Scenes</a> ·
  <a href="#roadmap">Roadmap</a> ·
  <a href="#this-repository">This repo</a> ·
  <a href="#contact">Contact</a>
</p>

<br/>

> **We are an AI company first.**  
> We use AI to **understand events**, **score urgency**, **call the right person**, and **escalate** — with **humans still in control**.  
> **Site requirement:** working network (Wi‑Fi or wired) at each location.

<br/>

---

<h2 id="about">About</h2>

Traditional site security often stops at a loud bell or a generic text — **everyone gets the same alert, nobody knows how serious it is, someone has to guess who should go.**

Croc Nexus closes that gap with an **AI-native** stack we **own end to end**: cloud, mobile apps, coordination logic, and our in-house model **CAO** *(training, not open)*. We do **not** offer white-label or customer-branded apps.

| Old way | With Croc Nexus AI |
|:--------|:-------------------|
| Every alarm feels equally urgent | **Urgency score (0–100)** with plain-language reasons |
| Staff wait and guess | AI **calls admin or agent** to go check |
| Wrong person gets pinged | AI **routes by role, zone, and availability** |
| Camera footage unused | **Linked images** support the decision when available |
| Chain breaks if no answer | **Auto-escalation** to the next contact |
| No record of actions | Full **audit log** of AI and human steps |
| One-size-fits-all | **Per-site** rules, call lists, and escalation |

**Why us as a startup:** built around AI from day one — not a legacy hardware firm adding AI as marketing. Young, focused, and **customisable per site** on our platform.

---

<h2 id="products">Products</h2>

<table>
<tr>
<td width="50%" valign="top">

### Croc Sentinel
**AI-powered monitoring — live today**

- Event recognition on the map  
- **3–30 second** alerts to phones  
- Automatic calls to admin or agent  
- Camera context when linked  
- iPhone & Android apps with live timeline  

</td>
<td width="50%" valign="top">

### Croc Coordination
**AI that turns alerts into action**

- Urgency score + readable reasons  
- Who to call and what to do first  
- Escalation if nobody answers  
- Human approval before sensitive steps  
- Full audit trail  

</td>
</tr>
</table>

### CAO *(internal — not open)*

Compact in-house model for deeper coordination over time. **Exclusive to Croc Nexus** — not licensed or rebranded. Production sites use **rules + Coordination** today.

| | |
|:--|:--|
| **Status** | Internal training |
| **Role** | Sharper scoring, routing, and follow-up on top of fixed safety rules |
| **Ownership** | Croc Nexus only |

---

<h2 id="how-it-works">How it works</h2>

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
```

| Step | What AI does |
|:-----|:-------------|
| **Understand** | Classify the event — emergency, security, maintenance, etc. |
| **Score** | 0–100 urgency with reasons anyone can read |
| **Route** | Call the right administrator or assigned agent |
| **Escalate** | Next contact if no answer |
| **Record** | Timestamp every AI decision and human action |

<p align="center">
  <img src="assets/images/architecture-four-layers.svg" alt="Cloud, mobile app, and AI layer" width="720" />
</p>

| Layer | Role |
|:------|:-----|
| **Cloud** | Recognition, scoring, routing, escalation |
| **Mobile app** | Map, timeline, alerts, approvals — **Croc Nexus apps only** |
| **AI** | Understand events, pick who to call, plan follow-up |

**Principles:** safety rules always run first · AI never lowers urgency silently · sensitive steps need human approval · full audit trail.

---

<h2 id="scenes">Scenes</h2>

Government buildings · malls · hospitals · plazas · parks · roads · traffic junctions · commercial districts · campuses · residential · *personal / home use on roadmap*

We configure **urgency rules, call lists, and escalation** per site on **our platform**.

| You need | We provide |
|:---------|:-----------|
| Different rules per zone | Custom scoring and call lists |
| Mobile access | **Our apps** — your site configuration |
| New scene types | Scoped per project |
| Future device rollout | Same AI brain — see roadmap below |

---

<h2 id="roadmap">Roadmap</h2>

<table>
<tr>
<td width="50%" valign="top">

### Now — AI + people
- AI scores and routes fast  
- **Calls and alerts** the right person  
- **Human confirms on site**  
- Map and timeline guide response  

</td>
<td width="50%" valign="top">

### Later — AI + machines & devices
Same AI brain, more ways to respond *(step by step per site)*:

- **Embodied intelligence** — go to spot or patrol  
- **Drones** — aerial check and fast reach  
- **Security devices** — more on-site equipment on the alert path  
- Still logged, human-gated where it counts  

</td>
</tr>
</table>

---

<h2 id="this-repository">This repository</h2>

Public overview, docs, imagery, and **minimal samples** — not production code or full platform source.

```bash
git clone https://github.com/DD-111/CROC-AI-SYSTEMS.git
cd CROC-AI-SYSTEMS
python -m src.croc_orchestrator.demo_assess samples/orchestrator/alarm_event.json
```

Example output: fictional urgency score + short summary from sample event data.

| Folder | Contents |
|:-------|:---------|
| [`docs/`](docs/) | [Architecture](docs/ARCHITECTURE.md) · [Product overview](docs/PRODUCT_OVERVIEW.md) · [Extensibility](docs/EXTENSIBILITY.md) · [Coordination (brief)](docs/COORDINATION.md) |
| [`assets/`](assets/) | Logo and app screenshots |
| [`samples/`](samples/) | Example event JSON |
| [`src/`](src/) | Minimal sample helpers |

**Not published here:** production APIs, deployment configs, full agent runtime, CAO weights, or integration secrets. See [LICENSE](LICENSE) for scope.

---

<h2 id="mobile-app">Mobile app</h2>

<p align="center">
  <img src="assets/images/app-overview-dashboard.jpeg" alt="Home" width="220" />
  &nbsp;&nbsp;
  <img src="assets/images/app-events-timeline.jpeg" alt="Events" width="220" />
  &nbsp;&nbsp;
  <img src="assets/images/app-device-activation.jpeg" alt="Setup" width="220" />
  &nbsp;&nbsp;
  <img src="assets/images/app-signals-routing.jpeg" alt="Activity" width="220" />
</p>

<p align="center"><sub>Map · events · setup · activity</sub></p>

---

<h2 id="contact">Contact</h2>

**Partnerships & enquiries:** partnerships@crocnexus.com · +084-349525

---

<p align="center">
  <strong>Croc Nexus AI Technologies</strong> — AI startup<br/>
  partnerships@crocnexus.com · +084-349525<br/>
  <sub>© Croc Nexus AI Technologies · <a href="LICENSE">MIT License</a> (repo materials only)</sub>
</p>
