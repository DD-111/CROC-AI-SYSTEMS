<p align="center">
  <img src="assets/images/logo-croc-nexus-4k.png" alt="Croc Nexus AI Technologies" width="400" />
</p>

<h1 align="center">Croc Nexus AI Technologies</h1>

<p align="center">
  <em>A young company building connected safety systems for real-world sites</em>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/Stage-Startup-7c3aed" alt="Startup" />
  <img src="https://img.shields.io/badge/Sentinel-In%20production-16a34a" alt="In production" />
</p>

<br/>

> **Before you start**  
> Every site needs a **working network** — Wi‑Fi or wired internet — so on-site devices can reach our cloud and send alerts to phones.  
> Without network coverage at the location, the system cannot operate as designed.

<br/>

---

## Who we are

**Croc Nexus AI Technologies** is a **startup** focused on one goal: make it easier to protect schools, hospitals, government buildings, and public facilities.

We design our own field hardware, cloud service, and mobile apps, and we work with customers to **adapt the system to their site** — not force every site into the same box.

| We care about | What that means for you |
|:--------------|:------------------------|
| **Field hardware** | CS-M401–M407 devices for buttons, sensors, sirens, and site control |
| **Cloud + mobile** | Live maps, fast phone alerts, and a clear event history |
| **Smart assistance** | Urgency scores, plain reasons, and suggested next steps — with people still in charge |
| **Your layout** | Workflows, device groups, and alert rules shaped around how your site actually runs |

**Talk to us:** partnerships@crocnexus.com · +084-349525

---

## What we offer today

<table>
<tr>
<td width="50%" valign="top">

### Croc Sentinel
**Alarm & monitoring — live today**

- Multi-site **map** with live markers  
- Phone alerts in about **3–30 seconds**  
- **iPhone & Android** apps  
- Linked **camera photos** on alarm  
- QR setup & remote updates for CS-M devices  

</td>
<td width="50%" valign="top">

### Croc Coordination
**From alert to clear action**

- Urgency score & plain-language reasons  
- Suggested who to notify and what to do  
- **Human approval** before sensitive steps  
- Full history of what was suggested & done  

</td>
</tr>
</table>

<br/>

### CAO — our in-house small model *(not open yet)*

We are **indirectly training a compact smart model called CAO**, built only for **Croc Nexus AI Technologies**. It is designed to help coordinate alerts, scoring, and follow-up inside our own stack.

| | |
|:--|:--|
| **Status** | Internal development — **not publicly released** |
| **Purpose** | Smarter coordination on top of fixed safety rules |
| **Availability** | Exclusive to Croc Nexus products and partner deployments |

When CAO opens to wider use, we will announce it here. Until then, production sites rely on **proven rules** plus the smart features already in Croc Coordination.

---

## On-site hardware · CS-M series

| Model | Role on site |
|:-----:|:-------------|
| **CS-M401** | Emergency button |
| **CS-M402** | Motion detection |
| **CS-M403** | Siren / sound alert |
| **CS-M404** | Site controller / relay |
| **CS-M405** | Camera link unit |
| **CS-M406** | Multi-sensor hub |
| **CS-M407** | All-in-one field unit |

Add devices with a **QR code** or **serial number**. Software updates can be sent remotely after a unit is online.

---

## How the system is layered

<p align="center">
  <img src="assets/images/architecture-four-layers.svg" alt="Four layers: on site, cloud, mobile app, smart layer" width="880" />
</p>

| Layer | Role |
|:------|:-----|
| **On site** | CS-M401–M407 sense and act locally |
| **Cloud** | Secure online service, live updates, notifications |
| **Mobile app** | Map, events, arm/disarm, patrol view |
| **Smart layer** | Scores urgency, routes alerts, escalates if unanswered |

**Typical flow:** something triggers on site → cloud processes → phones notify staff → team responds on the map.

---

## Network at each site *(required)*

```text
  CS-M devices on site
         │
         │  Wi‑Fi or wired internet  ← must be available
         ▼
       Cloud
         │
         ▼
    Phones & dashboards
```

| Requirement | Notes |
|:------------|:------|
| **Internet at the site** | Wi‑Fi or Ethernet; devices must stay online for alerts and updates |
| **Signal quality** | Weak signal may slow alerts; we surface battery & link health in the app |
| **Cameras** | Usually on the same local network; photos upload through the field unit when an alarm fires |
| **Phones** | Staff apps need mobile data or Wi‑Fi to receive push alerts |

We can advise on placement and network checks during **site planning** — especially for campuses, clinics, and remote buildings.

---

## Built to adapt & customize

As a startup, we work **with** customers rather than only selling a fixed package.

**Examples of what we can tailor** *(feasibility confirmed per project)*:

| Your idea | How we usually approach it |
|:----------|:---------------------------|
| Extra device types | New roles in the CS-M family or partner hardware — **if** it fits our cloud model |
| Custom alert rules | Different groups, schedules, escalation paths per building or tenant |
| Branded mobile experience | Colours, logos, and workflow screens for large deployments |
| Extra notification channels | Email, messaging apps, on-duty call lists — scoped per contract |
| Future: drones, robots, mobile SOS | Architecture allows new inputs; we scope each idea in a discovery call |
| Deeper smart automation | CAO and advanced coordination — roadmap; early partners by invitation |

> **How to start:** tell us your site type, number of buildings, and how your team responds today.  
> We will come back with what is **ready now**, what needs **custom work**, and an honest timeline.

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

<p align="center"><sub>Home · Events · Add device · Activity</sub></p>

---

## Smart features (summary)

- Sort events: emergency, security, maintenance, and more  
- **0–100 urgency** with readable reasons  
- Camera images when a unit is linked  
- Notify the nearest available responder  
- Escalate by phone if nobody acknowledges in time  
- **People approve** before high-impact actions  

---

## Project layout

| Folder | Contents |
|:-------|:---------|
| `docs/` | Product & structure notes |
| `assets/` | Brand and app imagery |
| `samples/` | Example event data |
| `src/` | Shared helpers |

```bash
git clone https://github.com/DD-111/CROC-AI-SYSTEMS.git
```

---

<p align="center">
  <strong>Croc Nexus AI Technologies</strong><br/>
  partnerships@crocnexus.com · +084-349525<br/>
  <sub>© Croc Nexus AI Technologies · <a href="LICENSE">MIT License</a></sub>
</p>
