# Architecture

**Croc Nexus AI Technologies** is a two-person AI startup in Malaysia. Croc Sentinel is its trial-stage site alarm and incident-response product.

> A cloud-connected deployment requires a working network. Equipment compatibility and integration scope are assessed per project.

## High-level shape

```text
Supported site devices
        │
        ▼
Croc Sentinel server
        │
        ├── browser Command Center / PWA
        ├── configured notification providers
        └── incident and audit records

Incident OS (product spine)
        ├── Before  → response plans · readiness · optional drills
        ├── During  → incident workspace · alerts · optional AI/dispatch
        └── After   → timeline · response summary · post-incident review

Optional, default-off modules
        ├── rules-first incident analysis
        ├── camera snapshots
        ├── responder dispatch and phone location
        ├── voice calls and automation
        └── experimental multi-responder coordination
```

For the detailed Incident OS concept, artifacts, and architecture, see [INCIDENT_OS.md](INCIDENT_OS.md).

## Baseline source

The private source includes:

- Device identity, ownership, status, telemetry, and commands
- Alarm records and grouped siren behavior
- Incident lists, workspaces, and timelines
- Response-plan versioning and internal review marking
- Advanced-profile readiness configuration checks
- Audit records, read-only incident summaries, and post-incident reviews
- Account, role, customer-account, and device-ownership boundaries

“Certified response plan” means an authorized Sentinel user marked that version as reviewed. It is not third-party or regulatory certification.

## Optional deployment integrations

Camera snapshots, AI enrichment, responder dispatch, phone location, voice calls, automation, health, simulations, and coordination are separate capabilities. Most are disabled by default and require configuration, permissions, external services, and field validation.

The basic alarm path is designed not to depend on optional AI analysis.

## Interfaces that are not operational integrations

The source includes generic future-resource contracts and mock drone/robot adapters. They do not control physical hardware.

There is currently no production DJI Dock or Matrice integration, live drone video, city-patrol routing, return-to-home control, docking, or charging telemetry.

## Mobile

The audited product includes a responsive browser application and installable PWA shell. This repository does not prove a native iOS or Android application or an end-to-end mobile push deployment.

## Records and security boundaries

Supported workflows can emit event and audit records. These records are not claimed to be cryptographically tamper-evident or legally sufficient proof.

Security depends on deployment configuration. The source contains role and ownership checks, CSRF and login controls, signed device paths, selected approval gates, and encrypted manual backup paths; it does not establish a public compliance certification.

## Status

- **Baseline source** — code path exists; this does not prove deployment.
- **Optional deployment integration** — disabled by default or provider/site dependent.
- **Experimental or contract-only** — mock, dry-run, or incomplete operational integration.
- **Future** — not available today.

Advanced staging, security, performance, mobile-field, and extended live-environment validation remains incomplete.

See [PRODUCT_OVERVIEW.md](PRODUCT_OVERVIEW.md), [ORCHESTRATOR.md](ORCHESTRATOR.md), and [EXTENSIBILITY.md](EXTENSIBILITY.md).
