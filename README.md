<p align="center">
  <img src="assets/images/logo-croc-nexus-4k.png" alt="Croc Nexus AI Technologies" width="400" />
</p>

<h1 align="center">Croc Sentinel Systems</h1>

<p align="center">
  <strong>AI-powered site monitoring and response</strong><br/>
  <sub>A product of <strong>Croc Nexus AI Technologies</strong></sub>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/AI-Startup-7c3aed" alt="AI Startup" />
  <img src="https://img.shields.io/badge/Status-In%20production-16a34a" alt="In production" />
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="#platform">Platform</a> ·
  <a href="#ai-today">AI today</a> ·
  <a href="#evolving">Evolving</a> ·
  <a href="#scenes">Scenes</a> ·
  <a href="#mobile">Mobile</a> ·
  <a href="#repository">Repository</a> ·
  <a href="#contact">Contact</a>
</p>

<br/>

> **Croc Sentinel Systems** turns site alerts into **scored, routed, accountable action** — detect, score urgency, call the right person, escalate, and log every step.  
> **Humans stay in control.** Each site needs **network** (Wi‑Fi or wired internet).

<br/>

---

<h2 id="overview">Overview</h2>

Most site security still stops at a loud bell or a generic text. **Everyone gets the same alert. Nobody knows how serious it is. Someone has to guess who should go.**

**Croc Sentinel Systems** is Croc Nexus’s platform for connected sites: monitoring on the map, **3–30 second** alerts, automatic calls to staff, and a full audit trail — on **Croc Nexus–owned** cloud and mobile apps.

| Before | With Croc Sentinel Systems |
|:-------|:---------------------------|
| Every alarm feels equally urgent | **Urgency score (0–100)** with plain-language reasons |
| Staff wait and guess | AI **calls admin or agent** to go check |
| Wrong person gets pinged | AI **routes by role, zone, and availability** |
| Camera footage unused | **Linked images** when available |
| Chain breaks if no answer | **Auto-escalation** to the next contact |
| No record | Full **audit log** of AI and human steps |

**Straight talk:** today, **people still go to the site to check**. The platform makes that faster and clearer — on-site response is not fully automated yet.

---

<h2 id="platform">Platform</h2>

<p align="center">
  <img src="assets/images/app-overview-dashboard.jpeg" alt="App dashboard" width="280" />
  &nbsp;&nbsp;
  <img src="assets/images/app-events-timeline.jpeg" alt="Events" width="280" />
</p>

<table>
<tr>
<td width="50%" valign="top">

### Monitoring
**Live today**

- Event recognition on the map  
- **3–30 s** alerts to phones  
- Automatic calls to admin or agent  
- Camera context when linked  
- iPhone & Android apps  

</td>
<td width="50%" valign="top">

### Coordination
**Live today**

- Urgency score + readable reasons  
- Who to call and what to do first  
- Escalation if nobody answers  
- Human approval before sensitive steps  
- Full audit trail  

</td>
</tr>
</table>

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
  Machines & devices on site     ← not open yet
```

<p align="center">
  <img src="assets/images/architecture-four-layers.svg" alt="Cloud, mobile app, and AI layer" width="640" />
</p>

| Layer | Role |
|:------|:-----|
| **Cloud** | Recognition, scoring, routing, escalation |
| **Mobile app** | Map, timeline, alerts, approvals — **Croc Nexus apps only** |
| **AI** | Understand events, pick who to call, plan follow-up |

We configure **rules, call lists, and escalation per site** on our stack. **No white-label or customer-branded apps.**

**Principles:** safety rules always run first · AI never lowers urgency silently · sensitive steps need human approval · full audit trail.

---

<h2 id="ai-today">What the AI does today</h2>

**In production** on Croc Nexus infrastructure *(full source not in this repository)*:

| Capability | What happens |
|:-----------|:-------------|
| Detect & recognise | Events on map with type and context |
| Score urgency | **0–100** with plain-language reasons |
| Summarise | Short operator-facing text |
| Route | **Phone call + app alert** to admin or agent |
| Camera context | Linked images when available |
| Escalate | Next contact if no answer |
| Human gate | Sensitive steps need approval |
| Audit | Every step timestamped |

---

<h2 id="evolving">What we are building next</h2>

| Stage | Status |
|:------|:-------|
| **Monitoring + Coordination AI** | ✅ Live |
| **CAO** (Croc Nexus in-house model) | Not open — in training; exclusive to Croc Nexus |
| **Richer orchestration** | Not open — internal; [edge sketch only](src/croc_orchestrator/coordination_edge.py) here |
| **Embodied intelligence, drones & devices** | Not open — planned |
| **Personal / home use** | Not open — planned |

**CAO** deepens coordination over time. Production today uses **rules + Coordination**. CAO is not licensed or rebranded.

We ship **gradually**. Humans stay in the loop where it matters.

---

<h2 id="scenes">Scenes</h2>

Government buildings · malls · hospitals · plazas · parks · roads · traffic junctions · commercial districts · campuses · residential · *personal / home — not open yet*

| You need | We provide |
|:---------|:-----------|
| Different rules per zone | Custom scoring and call lists on Croc Nexus |
| Mobile access | **Our apps** — your site configuration |
| New scene types | Scoped per project |

---

<h2 id="mobile">Mobile app</h2>

<p align="center">
  <img src="assets/images/app-device-activation.jpeg" alt="Setup" width="220" />
  &nbsp;&nbsp;
  <img src="assets/images/app-signals-routing.jpeg" alt="Activity" width="220" />
</p>

<p align="center"><sub>Setup · activity — part of Croc Sentinel Systems</sub></p>

---

<h2 id="repository">This repository</h2>

Public overview and **minimal samples** for **Croc Sentinel Systems** — not production code, CAO weights, or cloud backends.

```bash
git clone https://github.com/DD-111/CROC-AI-SYSTEMS.git
cd CROC-AI-SYSTEMS
python -m src.croc_orchestrator.demo_assess samples/orchestrator/alarm_event.json
```

| Folder | Contents |
|:-------|:---------|
| [`docs/`](docs/) | [Architecture](docs/ARCHITECTURE.md) · [Product overview](docs/PRODUCT_OVERVIEW.md) · [Extensibility](docs/EXTENSIBILITY.md) · [Coordination (brief)](docs/COORDINATION.md) |
| [`assets/`](assets/) | Logo and app imagery |
| [`samples/`](samples/) | Example event data |
| [`src/`](src/) | Minimal sample helpers |

See [LICENSE](LICENSE) for scope.

---

<h2 id="contact">Contact</h2>

**Croc Nexus AI Technologies**  
partnerships@crocnexus.com · +084-349525

---

<p align="center">
  <strong>Croc Sentinel Systems</strong> · a product of <strong>Croc Nexus AI Technologies</strong><br/>
  partnerships@crocnexus.com · +084-349525<br/>
  <sub>© Croc Nexus AI Technologies · <a href="LICENSE">MIT License</a> (repo materials only)</sub>
</p>
