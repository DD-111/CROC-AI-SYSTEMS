<p align="center">
  <img src="assets/images/logo-croc-nexus-4k.png" alt="Croc Nexus AI Technologies" width="400" />
</p>

<h1 align="center">Croc Sentinel</h1>

<p align="center">
  <strong>Turns a loud alarm into a clear answer:<br/>how serious is it, and who should go?</strong><br/>
  <sub>By Croc Nexus AI Technologies · a two-person startup from Malaysia</sub>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/Stage-Early%20(trial)-f59e0b" alt="Trial" />
  <img src="https://img.shields.io/badge/People-Always%20in%20control-16a34a" alt="Human in control" />
  <img src="https://img.shields.io/badge/From-Malaysia-006847" alt="Malaysia" />
</p>

<p align="center">
  <a href="#what">What is Sentinel</a> ·
  <a href="#problem">The Problem</a> ·
  <a href="#philosophy">Our Philosophy</a> ·
  <a href="#fail">Why Existing Systems Fail</a> ·
  <a href="#why">Why Sentinel</a> ·
  <a href="#benefits">Benefits</a>
</p>
<p align="center">
  <a href="#incident">What an Incident Looks Like</a> ·
  <a href="#where">Where AI Works</a> ·
  <a href="#architecture">Architecture</a> ·
  <a href="#how">How It Works</a> ·
  <a href="#use">How To Use</a>
</p>
<p align="center">
  <a href="#command-center">Command Center</a> ·
  <a href="#mobile">Mobile App</a> ·
  <a href="#trust">Built For Trust</a> ·
  <a href="#highlights">Technical Highlights</a> ·
  <a href="#roadmap">Roadmap</a> ·
  <a href="#ecosystem">Ecosystem</a> ·
  <a href="#faq">FAQ</a> ·
  <a href="#contact">Contact</a>
</p>

<br/>

---

<h2 id="what">What is Sentinel</h2>

Almost every building already has alarms and cameras. The trouble is, an alarm only shouts *"something happened."* It never tells you **how bad it is** or **who should go check.**

**Croc Sentinel** answers those two questions for you.

The moment an alert comes in, Sentinel gives it a simple urgency score, explains why in one plain sentence, calls the right person by phone and app, keeps trying the next person if no one answers, and writes down every step so nothing gets lost.

Think of it as a calm, tireless helper sitting next to your alarm system — one that never panics and never forgets.

> **Status:** early / trial stage. It runs on real sites today, and we keep improving it. A real person still goes to check — Sentinel makes sure the right person knows fast, and knows why.

---

<h2 id="problem">The Problem</h2>

When an alarm goes off today, this is what usually happens:

- **Everything feels equally urgent.** A door left open sounds the same as a real emergency.
- **Nobody knows how serious it is.** Someone has to stop and guess.
- **Nobody knows who should go.** People wait, or the wrong person gets bothered.
- **If the first person misses the call, the chain breaks.** Nothing moves until someone happens to notice.
- **There's no clear record.** Afterwards, no one can say who did what, or when.

The result: slow response, constant noise, and no one clearly responsible.

---

<h2 id="philosophy">Our Philosophy</h2>

We believe in a simple idea: **the machine should do the first round of thinking, and a person should make the final call.**

Three rules guide everything we build:

1. **Safety first, always.** The system can make something *more* urgent, but it can **never quietly make it less** urgent.
2. **People stay in charge.** The system suggests and prepares; a human approves anything that matters.
3. **Nothing hides.** Every decision — by the machine or the person — is written down in plain words.

We are not trying to replace people. We are trying to make sure the right person acts **fast, and for the right reason.**

---

<h2 id="fail">Why Existing Systems Fail</h2>

Traditional alarm systems were designed decades ago to do one thing: **make noise.** They ring, and all the thinking is dumped on whoever is watching.

That breaks down in real life:

- A person watching ten screens **can't rank** what matters.
- At 3 a.m., tired staff **miss or misjudge** alerts.
- When the first contact doesn't answer, **there's no plan B.**
- After an incident, there's **no honest trail** of what actually happened.

Adding more cameras or louder sirens doesn't fix any of this. The missing piece was never more noise — it was **judgment and follow-through.**

---

<h2 id="why">Why Sentinel</h2>

Sentinel adds the part that was always missing: a helper that reads the situation and drives the first response.

| The usual way | With Croc Sentinel |
|:--------------|:-------------------|
| Every alarm sounds the same | Each one gets a **score** and a **plain reason** |
| People guess how urgent it is | The system suggests, a person confirms |
| Someone must figure out who to call | It **calls the right person automatically** |
| If no one answers, it stops | It **moves to the next person** |
| No clear record afterwards | It **keeps a simple record of everything** |

---

<h2 id="benefits">Benefits</h2>

- **Less noise** — you focus only on what truly matters.
- **Faster response** — alerts reach a phone in seconds, with a call when it's serious.
- **Clear responsibility** — everyone can see who was told and what they did.
- **Fits your place** — a hospital, a mall, and a park each get their own rules.
- **You stay in control** — anything important waits for a human "yes."
- **Peace of mind** — nothing important slips through the cracks at 3 a.m.

---

<h2 id="incident">What an Incident Looks Like</h2>

Here's a real-feeling example, start to finish:

```text
  10:42:03   A sensor at the north gate triggers.
  10:42:04   Sentinel reads it: repeated triggers, weak signal, no photo.
  10:42:05   Urgency scored 89 / 100 — "high."
             Reason: "Repeated triggers at north gate after hours."
  10:42:06   It calls the on-duty officer's phone and pings the app.
  10:42:20   No answer. It automatically calls the backup — the site admin.
  10:42:31   Admin answers, sees the map and reason, heads to the gate.
  10:49:00   Admin marks it resolved in the app.
             Every step above is saved, with the exact time.
```

No guessing. No "who was supposed to handle this?" Just a clear, recorded response.

---

<h2 id="where">Where AI Works</h2>

Croc Sentinel is useful anywhere people need to respond to real events:

<p align="center">

| | | |
|:-:|:-:|:-:|
| Government buildings | Shopping malls | Hospitals & clinics |
| Plazas & squares | Parks | Roads & streets |
| Traffic junctions | Commercial districts | Campuses & industrial parks |
| Housing communities | *(Homes — coming later)* | |

</p>

For each place, we set up its own rules — who to call, when, and how urgent different events should be.

---

<h2 id="architecture">System Architecture</h2>

Under the hood, Sentinel is made of three simple parts working together:

<p align="center">
  <img src="assets/images/architecture-four-layers.svg" alt="The cloud, the app, and the AI brain" width="720" />
</p>

| Part | In plain words |
|:-----|:---------------|
| **The cloud** | The always-on service that receives events and does the thinking |
| **The app** | What people see — the map, the alerts, the buttons — on iPhone and Android |
| **The AI brain** | The helper that scores urgency, picks who to call, and follows up |

Behind the scenes, the brain (we call it **Croc AI Orchestrator**) works like a small team where each helper has one job — one reads the event, one decides urgency, one picks who to call, one follows up. It runs on our own cloud, and everything stays under the Croc Nexus name.

---

<h2 id="how">How It Works</h2>

```text
  Something happens on site
          │
          ▼
  Sentinel sees it (the eyes)
          │
          ▼
  The AI scores it and explains why
          │
          ├──►  Calls + app alert to the right person
          └──►  Saves a record of every step
          │
          ▼
  A real person goes to check
          │
          ▼
  Resolved — or passed to the next person if still open
```

Five things the AI does, in order:

1. **Understands** the event — emergency, security, or maintenance?
2. **Scores** how urgent it is, with a one-line reason.
3. **Chooses** who to call, based on role, area, and who's on duty.
4. **Follows up** on its own if no one answers.
5. **Records** everything, with exact times.

---

<h2 id="use">How To Use</h2>

**For a real site**, we set it up for you — the rules, the call list, and who gets notified are all configured for your specific place. Everything runs through **our own app**; we don't put your logo on someone else's software.

**To see the idea yourself**, this page includes a tiny demo. It takes a made-up alarm and prints a score and a short summary:

```bash
git clone https://github.com/DD-111/CROC-AI-SYSTEMS.git
cd CROC-AI-SYSTEMS
python -m src.croc_orchestrator.demo_assess samples/orchestrator/alarm_event.json
```

> This demo is just for illustration. The real system and app stay private.

---

<h2 id="command-center">Command Center</h2>

The command center is the **big-screen view** — a live map of the whole site, every active event, and its urgency at a glance. It's built for a control room or a front desk where someone keeps an eye on everything and can step in with one tap.

- See every site and event on one map
- Sort by urgency automatically — the serious ones rise to the top
- Watch a live timeline of what the AI did and what people decided
- Take over or confirm any step yourself

---

<h2 id="mobile">Mobile App</h2>

<p align="center">
  <img src="assets/images/app-overview-dashboard.jpeg" alt="Home" width="220" />
  &nbsp;
  <img src="assets/images/app-events-timeline.jpeg" alt="Events" width="220" />
  &nbsp;
  <img src="assets/images/app-device-activation.jpeg" alt="Setup" width="220" />
  &nbsp;
  <img src="assets/images/app-signals-routing.jpeg" alt="Activity" width="220" />
</p>

<p align="center"><sub>Home map · recent events · quick setup · live activity — on iPhone and Android.</sub></p>

The app is what most people use day to day: get the alert, see where and why, and respond — all from your phone.

---

<h2 id="trust">Built For Trust</h2>

Safety software only works if you can trust it. So we built trust in from the start:

- **The machine never overrules safety.** It can raise urgency, never quietly lower it.
- **People approve the big steps.** The AI prepares; a human decides.
- **Everything is written down.** A full, honest record of every event.
- **It keeps working even if the smart part is down.** Basic rules still ring the right phones.
- **Your data stays yours.** Each customer's information is kept separate.

---

<h2 id="highlights">Technical Highlights</h2>

In plain terms, here's what makes it work well:

- **Seconds, not minutes** — alerts reach a phone within a few seconds.
- **A reason you can read** — every score comes with one plain sentence.
- **Never a dead end** — if one person misses it, the next is called automatically.
- **Camera-aware** — if a photo is linked to the event, the AI takes it into account.
- **Rules plus smarts** — dependable safety rules first, AI on top for the finer judgment.
- **One brain, many places** — the same system adapts to malls, hospitals, parks, and more.

---

<h2 id="roadmap">Roadmap</h2>

| What | Where it stands |
|:-----|:----------------|
| **Croc Sentinel** (the eyes) | **Early / trial** — running on real sites |
| **Croc AI Orchestrator** (the brain) | **Early / trial** — running on real sites |
| A smarter in-house AI helper | **In development — not open yet** |
| A team of AI helpers for everyday work | **In development — not open yet** |
| A live screen to watch and steer the AI | **In development — not open yet** |
| Sending alerts to on-site helpers (patrol devices, etc.) | **In development — not open yet** |
| A version for homes and individuals | **In development — not open yet** |

We add new things **slowly and carefully**, only when they're genuinely ready.

---

<h2 id="ecosystem">Ecosystem</h2>

Croc Sentinel is the first piece of a bigger idea from **Croc Nexus AI Technologies**: **AI that works like a reliable team member** — doing the routine thinking, staying visible so you can watch it, and always leaving the important decisions to you.

```text
Croc Nexus (the bigger vision)
   ├── Croc Sentinel        →  the eyes on your site        (trial)
   ├── Croc AI Orchestrator →  the brain that decides       (trial)
   └── More AI helpers      →  everyday work, coming later  (not open yet)
```

Site safety is where our AI meets the real world first — but the same approach is meant to help with far more over time.

---

<h2 id="faq">FAQ</h2>

**Does this replace my security guards?**
No. People still respond on site. Sentinel just makes sure the right person knows fast, and knows why.

**Do I need to throw out my current cameras and alarms?**
Generally no — Sentinel is about adding judgment on top. Each site is reviewed before setup.

**What do I need at my site?**
A working internet connection (Wi‑Fi or wired), so alerts can travel and reach phones.

**Can it fit my specific building?**
Yes. We set the rules, urgency levels, and call list for your place.

**Is the AI making decisions on its own?**
It makes the *first* suggestion and handles the routine. Anything important waits for a human "yes."

**Can I get the source code or put my own brand on it?**
No. The app and the smart parts stay ours — no white-label, no rebranding. This page shares only a small demo and plain explanations.

**What does "early / trial" mean?**
It runs on real sites today, and we keep improving it. It's honest work in progress, not a finished mass-market product.

---

<h2 id="contact">Contact</h2>

**Croc Nexus AI Technologies** · Malaysia  
partnerships@crocnexus.com · +084-349525

---

<p align="center">
  <strong>Croc Nexus AI Technologies</strong><br/>
  Croc Sentinel · Croc AI Orchestrator<br/>
  <sub>© Croc Nexus AI Technologies · <a href="LICENSE">MIT License</a> (this repository's materials only)</sub>
</p>
