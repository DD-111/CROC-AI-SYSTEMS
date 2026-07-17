# Vision and concepts

This document preserves Croc Nexus’s product direction without presenting future work as current capability.

## Status language

- **Current** — part of the baseline private source; deployment still requires configuration and validation.
- **Optional** — source exists but is disabled by default or depends on providers and site setup.
- **Experimental** — prototype, dry-run, mock, or contract-level work.
- **Concept** — a future direction with no operational integration or delivery promise.

## Current foundation

Croc Sentinel’s current foundation covers supported devices, alarm records, incidents, operator workflows, response plans, readiness configuration checks, audit records, read-only incident summaries, and post-incident reviews.

Optional analysis, camera, dispatch, location, voice, automation, and coordination modules are documented separately and must not be assumed to be enabled.

## Drone-response concept

**Current status: concept only.**

The private source contains a generic future-resource interface and mock drone adapter. It does not connect to production drone hardware.

### Evaluated targets

- DJI Dock 3
- Matrice 4D
- Matrice 4TD

These are possible research targets only. Croc Nexus does not currently claim compatibility or support.

### Desired future experience

The concept explores:

- Human-approved aerial response suggestions
- Dock and aircraft readiness checks
- Map-based mission planning and route display
- Live mission state, aircraft telemetry, and video return
- Authorized voice summaries
- Incident-linked mission records
- Safe cancellation and emergency handling
- Return-to-home, precision landing, and charging status
- Scheduled city or facility patrols that remain subordinate to legal and human controls

### Staged plan

#### Stage 0 — concept and safety boundaries

- Define user value, non-goals, and operator responsibility
- Keep physical execution blocked
- Model approvals, cancellation, and audit records
- Review local aviation, privacy, and site rules

#### Stage 1 — vendor sandbox

- Obtain approved vendor APIs and licensing
- Build an adapter in a non-flight environment
- Validate identity, authentication, permissions, and telemetry schemas
- Keep every command simulated

#### Stage 2 — hardware-in-the-loop

- Connect one dock and one aircraft in a controlled site
- Test command acknowledgements and state reconciliation
- Verify video, telemetry, geofence, weather, battery, link-loss, and return behavior
- Exercise failed launch, aborted mission, degraded link, and failed landing scenarios

#### Stage 3 — supervised pilot

- Limit missions, operators, geography, time, and weather
- Require human approval and direct supervision
- Record safety, reliability, privacy, and incident evidence
- Stop the pilot if exit criteria are not met

#### Stage 4 — deployment decision

- Review field evidence and regulatory conditions
- Define supported hardware and software versions
- Publish operating limits, responsibilities, and support scope
- Decide whether the capability is safe and useful enough to offer

No stage has a promised delivery date.

## AI-agent direction

Croc Nexus is also exploring:

- Narrow AI agents that explain their work
- Digital employee teams for routine non-safety operations
- A visual control panel for observing and approving actions
- Token relay for model routing, cost, metering, and policy
- Selected security devices and embodied systems

The guiding principles are:

1. Core alarm handling must not wait for optional AI.
2. High-impact actions remain under human and permission control.
3. AI recommendations must be visible and reviewable.
4. Experimental systems must fail safely.
5. Public documentation must separate current, optional, experimental, and concept work.

## Concept media

The public concept film is available at:

- [MP4 concept film](../assets/video/sentinel-future-drone-concept.mp4)
- [GIF preview](../assets/video/sentinel-future-drone-concept.gif)

Every frame is permanently marked:

> CONCEPT SIMULATION — NO CURRENT DRONE INTEGRATION

The film is generated product-vision material. It is not live footage, real telemetry, a DJI demonstration, or evidence of deployment.
