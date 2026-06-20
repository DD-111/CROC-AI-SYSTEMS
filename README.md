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
  <a href="#ai-today">AI today</a> ·
  <a href="#evolving">Evolving</a> ·
  <a href="#products">Products</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#scenes">Scenes</a> ·
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

<h2 id="ai-today">What our AI does today — honestly</h2>

This is **live in production** on Croc Nexus–owned cloud and apps *(not in this GitHub repo)*:

| Capability | What happens |
|:-----------|:-------------|
| **Detect & recognise** | Events from connected sites show on the map with type and context |
| **Score urgency** | **0–100** with plain-language reasons — rules always run first |
| **Summarise** | Short operator-facing text so staff do not read raw telemetry |
| **Route** | AI picks **administrator or assigned agent** and triggers **phone call + app alert** |
| **Camera context** | Linked photos support the decision when available |
| **Escalate** | Next contact if nobody answers — no silent drop-off |
| **Human gate** | Sensitive steps wait for a person to approve |
| **Audit** | Every AI suggestion and human action is logged with a timestamp |
| **Mobile** | iPhone & Android apps — map, timeline, alerts *(Croc Nexus apps only)* |

**Straight talk:** today, **people still go to the site to check**. Our AI makes that faster and clearer — it does not replace on-site response yet. Early deployments depend on **staff on the ground**.

---

<h2 id="evolving">What we are evolving into</h2>

We are actively building — not everything below is shipped yet:

<table>
<tr>
<th>Stage</th>
<th>Status</th>
<th>Direction</th>
</tr>
<tr>
<td valign="top"><strong>Rules + Coordination AI</strong></td>
<td valign="top">✅ Live</td>
<td valign="top">Production sites use proven safety rules plus Coordination features above</td>
</tr>
<tr>
<td valign="top"><strong>CAO</strong> (in-house model)</td>
<td valign="top">🔧 Training</td>
<td valign="top">Deeper coordination, scoring, and follow-up — <strong>exclusive to Croc Nexus</strong>, not open, no weights in this repo</td>
</tr>
<tr>
<td valign="top"><strong>Richer agent orchestration</strong></td>
<td valign="top">🔧 Internal</td>
<td valign="top">Multi-step coordination behind Croc Coordination — we publish only a <a href="src/croc_orchestrator/coordination_edge.py">non-runnable edge sketch</a>, not the runtime</td>
</tr>
<tr>
<td valign="top"><strong>Embodied intelligence</strong></td>
<td valign="top">📋 Roadmap</td>
<td valign="top">Same AI brain could dispatch on-site systems to reach a spot or patrol — step by step per site</td>
</tr>
<tr>
<td valign="top"><strong>Drones & security devices</strong></td>
<td valign="top">📋 Roadmap</td>
<td valign="top">Aerial check, more sensors, locks, barriers on the same alert path — when each site is ready</td>
</tr>
<tr>
<td valign="top"><strong>Personal / home use</strong></td>
<td valign="top">📋 Roadmap</td>
<td valign="top">Same call-and-respond logic, scaled down for households</td>
</tr>
</table>

We will not over-promise: new device types and CAO capabilities roll out **gradually**, with humans still in the loop where it matters.

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

Production today = **rules + Coordination**. CAO adds depth when we are ready — still not licensed or rebranded.

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
| Future device rollout | Same AI brain — see [evolving](#evolving) |

---

<h2 id="this-repository">This repository</h2>

Public overview, docs, imagery, and **minimal samples** — not production code or full platform source.

**What we publish here:** a tiny runnable score + summary demo, plus an **incomplete edge sketch** (`src/croc_orchestrator/coordination_edge.py`) that shows the *shape* of internal coordination — it **cannot** route calls, connect to cloud, or run CAO.

```bash
git clone https://github.com/DD-111/CROC-AI-SYSTEMS.git
cd CROC-AI-SYSTEMS

# Runnable miniature demo (fictional event → score + summary)
python -m src.croc_orchestrator.demo_assess samples/orchestrator/alarm_event.json

# Edge sketch only — RouteStep / FollowUpStep raise NotImplementedError
python -c "from src.croc_orchestrator.coordination_edge import PIPELINE_SHAPE; print(PIPELINE_SHAPE)"
```

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
