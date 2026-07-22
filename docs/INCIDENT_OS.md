# Incident OS

**Detection tells you something happened.  
Incident OS is built for the expensive minutes that come next.**

Inside Croc Sentinel, Incident OS is the **response operating system**: one incident identity that carries the site from preparation, through live response, into a reviewable record.

This page explains:

- the product idea (why it exists)
- what was built (not only planned)
- the artifacts and architecture behind it
- what is core, attachable, experimental, or future

It does **not** publish production source, credentials, or deployment runbooks.

---

## 1. The idea — why “OS”, not “another alarm page”

Most security buying still concentrates on **detection**: more sensors, more cameras, more notifications.

Sites do not usually fail because nobody heard the alarm. They lose time because the response is fragmented:

- the plan is in someone’s head or a PDF
- context is split across apps
- AI, if any, sits beside the workflow instead of on the incident
- after the night shift, nobody can reconstruct a clean story

Incident OS is designed as the layer that owns that gap:

| Phase | Operator question | Product job |
|:------|:------------------|:------------|
| **Before** | Are we ready for this shift? | Response plans, readiness gaps, optional drills |
| **During** | Who goes, and what happens next? | Shared incident workspace, alerts, optional AI and dispatch |
| **After** | What really happened? | Timeline, response summary, post-incident review |

So the metaphor is deliberate:

- **Sentinel** is the site product (devices, console, records)
- **Incident OS** is the spine that makes response behave like a system, not a pile of screens
- **Croc AI Orchestrator** is optional enrichment / coordination behind that spine
- people remain accountable; AI assists; the alarm path does not wait for a model

Incident OS is **not** a replacement for every camera platform, building system, or emergency service.  
It is the **response layer** that gives operators one shared incident picture.

---

## 2. What was built — product, not brochure

Incident OS was implemented as a three-phase spine: a **core path that always exists in source**, plus **attachable modules** that can be enabled per deployment.

### Before — Response Readiness

Built so a site can prepare before the next alarm:

- Import, version, and mark response rules as internally reviewed
- Readiness score and gap list for configuration checks
- Optional side-effect-free drills
- Bridges toward health / SOP / predictive checks when those modules are armed

Operator surfaces: response plans, readiness, response drill (when simulation is enabled).

### During — Response Orchestration

Built so the night shift is not improvising from chat:

- Alarm → incident list and incident workspace
- Timeline of supported event and operator activity
- Siren / alert channel from the response console
- Commander assign / handoff / override (authorized roles)
- SLA clocks for acknowledgement and response timing
- Optional rules-first AI analysis and recommendations
- Optional responder assignment and status tracking
- Optional multi-resource coordination (incident cell / swarm)
- Optional camera evidence when camera workflows are enabled

Operator surfaces: overview, incidents, response queue / siren, intelligence, orchestration (when enabled).

### After — Proof of Response

Built so the story does not die with the shift:

- Read-only response summary assembled from available records
- Closure checks
- Post-incident review drafts and submissions
- Audit and export paths for supported activity

Operator surfaces: proof panel, review form, audit / activity history.

---

## 3. Why this can feel ordinary if written badly

Incident OS is easy to undersell.

If you only list modules — “incidents, plans, readiness, optional AI” — it sounds like every SaaS ticket tool.

The distinctive claim is the **closed loop under one incident identity**:

1. prepare the response rules before the beep
2. keep alert-first behavior when something happens
3. put optional AI context on the same incident, without letting AI own the alarm
4. track supported response steps when dispatch is enabled
5. leave a timeline + summary + review that the next shift can open

That is the product story. Feature inventory is only evidence that the story was engineered, not invented for a deck.

---

## 4. Artifacts (engineering deliverables)

The private product repository contains several classes of artifacts. This public repo documents them at a high level; production code stays private.

### 4.1 Normative plans

| Artifact | What it defines |
|:---------|:----------------|
| Atomic master plan | North Star, Before/During/After atoms, release gates |
| Deployment runbook | How modules are enabled safely (flags, order, rollback) |
| Advanced authorization ledger | What may be claimed publicly vs what remains gated |
| Security / performance / release plan | Staging and field evidence still required for Live promotion |

### 4.2 Reference matrices

| Artifact | What it locks |
|:---------|:--------------|
| Glossary | Official vocabulary (incident, dispatch, response plan, proof, PIR, swarm…) |
| Capability matrix | Which modules exist and which are default-off |
| Frontend routes | Canonical console pages and redirects |
| API integration | Incident BFF and related HTTP surfaces |
| Realtime transport matrix | Poll vs SSE ownership for live screens |
| Dispatch correlation | How human dispatch and automation dispatch join without merging stores |
| Screen / widget matrix | Which UI pieces are real, gated, or forbidden to fake |

### 4.3 Backend domains

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

### 4.4 Console pages

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

### 4.5 Contracts and verification

Private verification includes focused Incident OS contract tests, dashboard route / verify scripts, and staging / field checklists.

Public takeaway: **delivery is substantial; full Advanced Live promotion is not claimed.**

---

## 5. Technical architecture

### 5.1 Layered shape

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

### 5.2 Canonical flow

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

### 5.3 Design rules that shape the architecture

1. **Notify first** — basic alerting is not blocked by optional analysis.
2. **Rules before model output** — baseline score and reason stay reviewable.
3. **Human control** — high-impact optional actions use permissions and configured approval.
4. **Join, don’t fake-merge** — human dispatch and automation dispatch stay separate stores, joined by correlation identifiers.
5. **Fail closed on incomplete advanced bundles** — incomplete AI / dispatch / swarm packs are rejected instead of faking Live.
6. **Disabled means unavailable** — optional modules do not pretend to be live when off.

### 5.4 Data and realtime (high level)

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

## 6. Capability inventory and status

| Label | Meaning |
|:------|:--------|
| **Core** | Mounted as baseline Incident OS path in source |
| **Built, default off** | Implemented and contract-tested; needs flags, config, site validation |
| **Experimental** | Dry-run, mock, or incomplete operational integration |
| **Future** | Direction only |
| **Not release-complete** | Advanced Live promotion still needs staging / field evidence |

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

## 7. What operators see

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
