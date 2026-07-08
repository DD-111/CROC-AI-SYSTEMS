<p align="center">
  <img src="assets/images/logo-croc-nexus-4k.png" alt="Croc Nexus AI Technologies" width="400" />
</p>

<h1 align="center">Croc Nexus AI Technologies</h1>

<p align="center">
  <strong>We build AI that works like a small team — it looks at what happened, decides how serious it is, and calls the right person.</strong><br/>
  <sub>A two-person startup from Malaysia.</sub>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/Stage-Early%20(trial)-f59e0b" alt="Trial" />
  <img src="https://img.shields.io/badge/From-Malaysia-006847" alt="Malaysia" />
</p>

<p align="center">
  <a href="#what">What is this</a> ·
  <a href="#problem">The problem</a> ·
  <a href="#different">What's different</a> ·
  <a href="#benefits">Benefits</a> ·
  <a href="#ai">Where the AI is</a> ·
  <a href="#use">How to use</a> ·
  <a href="#next">What's next</a> ·
  <a href="#contact">Contact</a>
</p>

<br/>

---

<h2 id="what">What is this</h2>

Most places — a mall, a hospital, a school, an office park — have alarms and cameras. When something happens, an alarm goes off. But an alarm only says *"something happened."* It does not say **how bad it is**, or **who should go look**.

We built software that answers those two questions for you.

When an alert comes in, our system:

1. **Looks at what happened** and gives it a simple score from 0 to 100 (how urgent).
2. **Explains why** in one plain sentence anyone can read.
3. **Calls the right person** — by phone and app — and tells them where to go.
4. **Keeps trying** the next person if the first one does not answer.
5. **Writes down** every step, so later you can see exactly what happened.

We have two products working together:

- **Croc Sentinel** — the eyes. It watches the site and shows everything on a map.
- **Croc AI Orchestrator** — the brain. It decides how serious something is and who to call.

> Both are **early / trial stage** — they run on real sites today, and we keep improving them.

---

<h2 id="problem">What problem does it solve</h2>

Today, when an alarm goes off, this is what usually happens:

- **Everything feels equally urgent.** A door left open and a real emergency sound the same.
- **Nobody knows how serious it is.** Someone has to stop and guess.
- **Nobody knows who should go.** People wait, or the wrong person gets bothered.
- **If the first person misses the call, the chain breaks.** Nothing happens until someone notices.
- **There is no record.** Afterwards, no one can say who did what, or when.

The result: slow response, a lot of noise, and no one clearly responsible.

---

<h2 id="different">Why not just keep using what exists — and how are we different</h2>

Normal alarm systems were built to make **noise**. They ring, and that's it. The thinking is left entirely to people.

We take the opposite approach: the system does the **first round of thinking** for you, then hands a clear decision to a real person.

| The usual way | Our way |
|:--------------|:--------|
| Every alarm sounds the same | Each one gets a **score** and a **plain reason** |
| People guess how urgent it is | The system suggests, a person confirms |
| Someone has to figure out who to call | It **calls the right person automatically** |
| If no one answers, it stops | It **moves on to the next person** |
| No clear record afterwards | It **keeps a simple record of everything** |

**Important:** we do not try to replace people. Today, a real person still goes to check. We just make sure the **right person knows fast, and knows why.**

---

<h2 id="benefits">What you get</h2>

- **Less noise** — you only pay attention to what actually matters.
- **Faster response** — alerts reach a phone in seconds, with a call if it's serious.
- **Clear responsibility** — everyone can see who was told and what they did.
- **Fits your place** — a hospital, a mall, and a park each get their own rules.
- **You stay in control** — anything important waits for a human "yes."

Works for: government buildings, malls, hospitals, plazas, parks, roads, campuses, and housing areas.

---

<h2 id="ai">Where the AI is — and how we designed it</h2>

The AI is the part that **reads the situation and makes the first call**, instead of leaving everything to a tired person at 3 a.m.

Here is what it actually does:

- **Understands** the event — is this an emergency, a security issue, or just maintenance?
- **Scores** how urgent it is, and says why in one sentence.
- **Chooses** who to call, based on their role, area, and whether they're on duty.
- **Follows up** on its own if no one picks up.

### How the AI is designed — and why

We did not build one big "answer everything" robot. We built it more like a **small team of helpers**, where each helper has one job (one reads the situation, one decides urgency, one picks who to call, one follows up).

We designed it this way on purpose:

- **Safety rules always come first.** The AI can make things *more* urgent, but it can **never quietly make something less urgent**. That's a hard rule.
- **A person approves anything important.** The AI suggests; people decide the big steps.
- **If the smart part is ever unavailable, the basic rules still work.** It never goes silent.
- **Everything is written down.** You can always see what the AI suggested and what the person chose.

In short: **helpful and fast, but never reckless, and never in charge of the final call.**

---

<h2 id="use">How to use it</h2>

For real sites, we set it up **for you** — the rules, the call list, and who gets notified are configured for your specific place. Everything runs through **our own app** (iPhone and Android); we don't put your logo on someone else's software.

This public page also includes a **tiny demo** so you can see the idea in action. It takes a made-up alarm and prints a score and a short summary:

```bash
git clone https://github.com/DD-111/CROC-AI-SYSTEMS.git
cd CROC-AI-SYSTEMS
python -m src.croc_orchestrator.demo_assess samples/orchestrator/alarm_event.json
```

> This demo is just for illustration. The real system, the app, and the smart parts stay private.

What's in this repository:

| Folder | What's inside |
|:-------|:--------------|
| [`docs/`](docs/) | Plain explanations of how things fit together |
| [`assets/`](assets/) | Logo and app pictures |
| [`samples/`](samples/) | Example made-up alarms |
| [`src/`](src/) | The tiny demo above |

<p align="center">
  <img src="assets/images/app-overview-dashboard.jpeg" alt="App home" width="220" />
  &nbsp;
  <img src="assets/images/app-events-timeline.jpeg" alt="Events" width="220" />
  &nbsp;
  <img src="assets/images/app-device-activation.jpeg" alt="Setup" width="220" />
  &nbsp;
  <img src="assets/images/app-signals-routing.jpeg" alt="Activity" width="220" />
</p>

<p align="center"><sub>Our app — the map, recent events, setup, and activity.</sub></p>

---

<h2 id="next">Why we build it this way — and what's next</h2>

We started with site safety because it's a clear, real problem where a smart "first responder" genuinely helps — and where getting it wrong is not an option, so **keeping humans in control matters most.**

But the bigger idea is simple: **AI that works like a reliable team member** — it does the routine thinking, stays visible so you can watch it, and always leaves the important decisions to you.

Some things we're still building, and are **not open yet**:

- A smarter in-house helper that gets better at deciding over time.
- A "team of AI helpers" for everyday work beyond alarms.
- A simple screen where you can watch what the AI is doing and step in anytime.
- Sending the alert to on-site helpers (like patrol devices) instead of only people.
- A version for homes and individuals.

We add these **slowly and carefully**, only when they're genuinely ready.

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
