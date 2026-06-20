<p align="center">
  <img src="assets/images/logo-croc-nexus-4k.png" alt="Croc Nexus AI Technologies" width="420" />
</p>

<h1 align="center">Croc Nexus AI Technologies</h1>

<p align="center">
  <strong>Hardware, software, and smart assistance for safer public spaces</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/Status-Production-success" alt="Production" />
</p>

---

## Company

**Croc Nexus AI Technologies** connects on-site equipment, cloud services, mobile apps, and smart decision support into one system.

| What we focus on | In plain terms |
|------------------|----------------|
| **On-site hardware** | Buttons, sensors, sirens, and site controllers that talk to the cloud |
| **Smart workflows** | Automated steps that help staff decide faster, with people still in control |
| **Live site views** | Maps, device status, and event history across many locations |
| **Rules & records** | Approvals, logs, and clear reasons behind each action |
| **cMax workspace** | A single screen to watch sites, teams, and outcomes in 2D and 3D |

**Contact:** partnerships@crocnexus.com · +084-349525

---

## Our products

| Product | What it does |
|---------|----------------|
| **Croc Sentinel** | Alarm and monitoring — devices, cloud, and mobile app |
| **Croc Coordination** | Turns raw alerts into clearer risk levels, next steps, and follow-up |
| **cMax** | Big-picture view — maps, timelines, and team activity |

---

## On-site hardware (CS-M series)

| Model | Typical use |
|-------|-------------|
| **CS-M401** | Emergency button |
| **CS-M402** | Motion detection |
| **CS-M403** | Siren / sound alert |
| **CS-M404** | Site controller / relay |
| **CS-M405** | Camera link unit |
| **CS-M406** | Multi-sensor hub |
| **CS-M407** | All-in-one field unit |

Devices are added with a QR code or serial number. Remote software updates are supported.

---

## Croc Sentinel

Built for schools, hospitals, government sites, and city-wide networks.

**What you get**

- One **map** showing many sites and live alarm markers
- **Fast alerts** to phones — usually within 3–30 seconds
- **iPhone and Android** apps for daily use and emergencies
- **Separate accounts** for different organisations; shared groups when needed
- **Photos from linked cameras** when an alarm fires
- Simple **add-device** flow and **remote updates** for field hardware

<p align="center">
  <img src="assets/images/architecture-four-layers.svg" alt="How the system is layered" width="860" />
</p>

| Layer | What it means |
|-------|----------------|
| **On site** | CS-M401–M407 devices — buttons, sensors, sirens |
| **Cloud** | Secure online service, live updates, phone notifications |
| **Mobile app** | Map, event list, arm/disarm all, patrol view |
| **Smart layer** | Scores urgency, suggests who to notify, escalates if unanswered |

**When something happens:** detect → cloud checks → notify everyone → staff responds on the map

---

## Croc Coordination

Helps turn alarms into clear, actionable information.

- Reads device signals and camera snapshots
- Gives a **simple risk score** and plain-language reasons
- Suggests **who to call** and **what to do next**
- Can use **models running on your own machines** or in the cloud — the system finds what is available
- Important actions wait for **human approval**
- Keeps a **full history** of what was suggested and what was done

---

## Mobile app

<p align="center">
  <img src="assets/images/app-overview-dashboard.jpeg" alt="Home screen" width="240" />
  &nbsp;
  <img src="assets/images/app-events-timeline.jpeg" alt="Event list" width="240" />
  &nbsp;
  <img src="assets/images/app-device-activation.jpeg" alt="Add device" width="240" />
  &nbsp;
  <img src="assets/images/app-signals-routing.jpeg" alt="Activity summary" width="240" />
</p>

Home · Events · Add device · Activity summary

---

## Smart features

- Sorts events by type (emergency, security, maintenance, and more)
- **0–100 urgency score** with clear reasons — not a black box
- Uses camera images when available
- Notifies the nearest available responder
- Calls or escalates if nobody acknowledges in time
- **People approve** before high-impact actions run

---

## Room to grow

The same platform can later support:

- Drone patrol over large sites
- Robots and automated field tasks
- Mobile SOS from phones
- Campus-wide and city-wide live models
- Legal and compliance review steps

New site types and workflows can be added without replacing the core system.

---

## Repository

```
docs/      Product and structure notes
assets/    Logo and app images
samples/   Example event data
src/       Shared helpers
```

```bash
git clone https://github.com/DD-111/CROC-AI-SYSTEMS.git
```

---

## License

[MIT License](LICENSE) · © Croc Nexus AI Technologies
