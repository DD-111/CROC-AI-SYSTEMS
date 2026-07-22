# Incident OS

**Incident OS** is the product spine of Croc Sentinel: the system that turns a device alarm into a prepared, coordinated, and reviewable response.

This page explains, in plain language:

- what Incident OS is
- what was built
- which public artifacts describe it
- how the technical architecture fits together
- what is core, optional, experimental, or future

It does **not** publish production source, credentials, or deployment runbooks.

---

## 1. Product concept

### Plain language

Most security products are good at **detection** — a sensor trips, a siren rings, a notification arrives.

Incident OS focuses on the harder part that comes after detection:

| Phase | Question | What Incident OS is for |
|:------|:---------|:------------------------|
| **Before** | Are we ready? | Response rules, readiness checks, drills |
| **During** | Who goes, and what happens next? | Incident workspace, alerts, optional AI and dispatch |
| **After** | What really happened? | Timeline, response summary, post-incident review |

Incident OS is **not** “another louder alarm panel.”  
It is also **not** a replacement for every camera platform, building system, or emergency service.

It is the **response layer** that sits with Sentinel’s devices and console so operators share one incident picture.

### How it relates to other Croc concepts

| Concept | Role |
|:--------|:-----|
| **Croc Sentinel** | Site product: devices, alarms, console, records |
| **Incident OS** | Inside Sentinel — Before / During / After response lifecycle |
| **Croc AI Orchestrator** | Optional enrichment and coordination direction |
| **Response plan** | Versioned response rules for event types |
| **Proof of response** | Read-only summary assembled from available records |
| **PIR** | Post-incident review after closure |
| **Automatic Response Team** | Future / experimental multi-resource coordination idea (swarm) |

---

## 2. What was built

Incident OS was built as a **three-phase product**, with a core path that always exists and advanced modules that can be enabled per deployment.

### Before — Response Readiness

Built capabilities:

- Import, version, and mark response rules as internally reviewed
- Readiness score and gap list for configuration checks
- Optional side-effect-free drills (simulation executors)
- Bridges toward health / SOP / predictive checks when those modules are enabled

Operator surfaces:

- Response plans console
- Readiness console
- Response drill console (when simulation is enabled)

### During — Response Orchestration

Built capabilities:

- Alarm → incident list and incident workspace
- Timeline of supported event and operator activity
- Siren / alert channel from the response console
- Commander assign / handoff / override (authorized roles)
- SLA clocks for acknowledgement and response timing
- Optional rules-first AI analysis and recommendations
- Optional responder assignment and status tracking
- Optional multi-resource coordination (incident cell / swarm)
- Optional camera evidence when camera workflows are enabled

Operator surfaces:

- Home / overview
- Incidents and incident detail
- Response queue and siren tab
- Intelligence console (AI)
- Orchestration console (swarm / actuators, when enabled)

### After — Proof of Response

Built capabilities:

- Read-only response summary assembled from available records
- Closure checks
- Post-incident review drafts and submissions
- Audit and export paths for supported activity

Operator surfaces:

- Incident workspace proof panel
- Review form
- Audit / activity history

---

## 3. Artifacts (what exists as deliverables)

The private product repository contains several **classes of artifacts**. The public GitHub repo documents them at a high level; production code stays private.

### 3.1 Normative plans

| Artifact | What it defines |
|:---------|:----------------|
| Atomic master plan | North Star, Before/During/After atoms, release gates |
| Deployment runbook | How modules are enabled safely (flags, order, rollback) |
| Advanced authorization ledger | What may be claimed publicly vs what remains gated |
| Security / performance / release plan | Staging and field evidence still required for Live promotion |

### 3.2 Reference matrices (source of truth for editors and engineers)

| Artifact | What it locks |
|:---------|:--------------|
| Glossary | Official vocabulary (incident, dispatch, response plan, proof, PIR, swarm…) |
| Capability matrix | Which modules exist and which are default-off |
| Frontend routes | Canonical console pages and redirects |
| API integration | Incident BFF and related HTTP surfaces |
| Realtime transport matrix | Poll vs SSE ownership for live screens |
| Dispatch correlation | How human dispatch and automation dispatch join without merging stores |
| Screen / widget matrix | Which UI pieces are real, gated, or forbidden to fake |

### 3.3 Backend domains

| Domain | Responsibility |
|:-------|:---------------|
| Alarm / event bus | Accept alarms, persist events, notify first |
| Incidents BFF | List, detail, timeline, proof, SLA, review, command |
| Dispatch rules | Response-plan import / certify / compare |
| Readiness | Score and gaps |
| AI incident | Optional rules-first analysis and enrichment hooks |
| Responder dispatch | Optional human assignment and status machine |
| Incident cell / swarm | Optional multi-resource coordination |
| Simulation | Optional drills without live side effects |
| Voice alert | Optional phone-call provider path |
| Actuators | Future / stub resource interface |
| Durable jobs | Delayed work and failure queues when armed |
| Metrics | Segment latency instrumentation |

### 3.4 Console pages

| Page | Phase |
|:-----|:------|
| Overview / home | During entry |
| Incidents + incident workspace | During / After |
| Response (queue + siren) | During |
| Response plans | Before |
| Readiness | Before |
| Response drill | Before (optional) |
| Intelligence | Optional AI |
| Orchestration | Optional swarm / actuators |
| Snapshots / cameras | Optional evidence |
| Audit / activity | After / continuous |

### 3.5 Contracts and verification

Private verification artifacts include:

- Focused Incident OS contract tests (API, UI wiring, capability matrices)
- Dashboard route / verify scripts
- Staging and field checklists (many advanced gates still open)

Public takeaway: **repository delivery is substantial; full Live promotion of the Advanced profile is not claimed.**

---

## 4. Technical architecture

### 4.1 Layered shape

```text
┌──────────────────────────────────────────────────────────┐
│  Browser Command Center / PWA                            │
│  overview · incidents · response · plans · readiness …   │
├──────────────────────────────────────────────────────────┤
│  Incident OS HTTP / BFF                                  │
│  incidents · readiness · dispatch-rules                  │
│  + optional AI · dispatch · cell · simulation · actuators│
├──────────────────────────────────────────────────────────┤
│  Domain services                                         │
│  alarm fan-out · AI · dispatch · cell · proof · PIR …    │
├──────────────────────────────────────────────────────────┤
│  Event / notify spine                                    │
│  emit event → email / messaging / push (configured)      │
│  AI analysis runs off the alarm-critical path            │
├──────────────────────────────────────────────────────────┤
│  Data & workers                                          │
│  event/audit stores · optional PG domains · job workers  │
│  device path (MQTT) · optional Redis / camera paths      │
└──────────────────────────────────────────────────────────┘
```

### 4.2 Canonical flow

```text
Supported device alarm
        │
        ▼
Accept + persist event
        │
        ├──► Notify first (alert path must not wait for AI)
        │
        ├──► Incident appears in console / workspace
        │
        ├──► Optional rules-first analysis
        │         └── optional Orchestrator enrichment
        │
        ├──► Optional human assignment / status tracking
        │
        ├──► Optional multi-resource coordination
        │
        ├──► Optional camera evidence
        │
        ▼
Timeline + response summary + closure + post-incident review
        │
        ▼
Audit / export of supported records
```

### 4.3 Design rules that shape the architecture

1. **Notify first** — basic alerting is not blocked by optional analysis.
2. **Rules before model output** — baseline score and reason stay reviewable.
3. **Human control** — high-impact optional actions use permissions and configured approval.
4. **Join, don’t fake-merge** — human dispatch and automation dispatch stay separate stores, joined by correlation identifiers.
5. **Fail closed on incomplete advanced bundles** — enabling AI/dispatch/swarm without required storage configuration is rejected rather than silently degraded into a false Live state.
6. **Disabled means unavailable** — optional modules return not-found / unavailable UI when off, instead of pretending to be live.

### 4.4 Data and realtime (high level)

| Concern | Approach |
|:--------|:---------|
| Events | Immutable event rows; alarms drive incident UX |
| Human dispatch | Dedicated responder-dispatch records |
| Response plans | Versioned dispatch rules |
| AI / swarm / PIR / durable jobs | Separate domains, often PostgreSQL-backed when armed |
| Overview cards | Short-interval HTTP refresh |
| Some live feeds | Server-sent events with polling fallback |
| Mobile deep links | Server payload contracts into console hashes (PWA / client interpretation) |

---

## 5. Capability inventory and status

Use these labels consistently:

| Label | Meaning |
|:------|:--------|
| **Core / always available in source** | Mounted as baseline Incident OS path |
| **Built, default off** | Implemented and contract-tested; needs flags, config, and site validation |
| **Experimental** | Dry-run, mock, or incomplete operational integration |
| **Future** | Direction only |
| **Not release-complete** | Advanced Live promotion still requires staging / field evidence |

### Core

- Device alarm ingest and event records
- Configured notifications / siren paths
- Incident list and workspace
- Timeline, commander controls, SLA views
- Response-plan lifecycle
- Readiness configuration score
- Proof-of-response assembly
- Post-incident review
- Audit history

### Built, default off

- Rules-first AI incident analysis
- Optional Orchestrator enrichment
- Responder assignment queue and status machine
- Consent-aware phone location for candidate selection
- Voice-call provider path
- Automation engine
- Camera snapshot evidence
- Health / SOP / predictive bridges
- Durable delayed jobs / failure queues
- Intelligence / orchestration consoles

### Experimental / contract-only

- Side-effect-free drills
- Multi-resource swarm / incident-cell coordination
- Generic future actuator interface
- Mock drone / robot adapters (no physical control)

### Future

- Production computer vision
- Real DJI / robot hardware control
- Native mobile releases verified from this public repository
- Broader third-party system replacements

### Honest release note

The private master plan still treats full Advanced Live promotion as **not complete**.  
Public materials may describe **core Incident OS paths** and **built optional modules**, but must not claim every advanced module is Live at every site.

---

## 6. What operators see (console map)

```text
Before
  ├── Response plans   → import / version / mark reviewed
  ├── Readiness        → score + gaps
  └── Drill            → optional simulation

During
  ├── Overview         → live alarms / fleet entry
  ├── Incidents        → list + workspace
  ├── Response         → my queue + siren
  ├── Intelligence     → optional AI queue / settings
  └── Orchestration    → optional cell / actuator console

After
  ├── Proof panel      → read-only response summary
  ├── PIR              → post-incident review
  └── Audit            → supported activity history
```

---

## 7. How this helps — and how it differs

Incident OS is designed so that:

- detection becomes a **shared incident**, not only a noise
- optional AI can add **score + reason + recommendation** without owning the alarm
- people keep **authority**
- the site keeps a **working record** for review

Compared with a basic alarm workflow, the main architectural difference is the closed Before → During → After loop, with optional modules attached to the same incident identity.

---

## 8. Related public docs

- [Product overview](PRODUCT_OVERVIEW.md)
- [Architecture](ARCHITECTURE.md)
- [Orchestrator](ORCHESTRATOR.md)
- [Extensibility](EXTENSIBILITY.md)
- [Vision and concepts](VISION_AND_CONCEPTS.md)

---

## 9. Public repository limit

This public repository explains Incident OS and includes small fictional samples.

It does **not** include:

- production backend or firmware secrets
- private models or customer configuration
- live staging evidence packages
- vendor credentials or deployment keys
