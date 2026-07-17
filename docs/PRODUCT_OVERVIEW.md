# Product overview

**Croc Nexus AI Technologies** is a two-person AI startup in Malaysia.

Its current product direction includes:

- **Croc Sentinel** — trial-stage site devices, alarms, incidents, operator workflows, and response records.
- **Croc AI Orchestrator** — private, optional analysis and coordination work that is not included in this public repository.

## What Sentinel is

Croc Sentinel helps operators move from a device alarm to an organized incident record.

## How Sentinel and AI work together

- **Sentinel handles the operational core:** device events, alarms, incidents, the web console, response rules, timelines, and records.
- **Sentinel’s optional analysis runs rules first:** when enabled, it can produce a score, category, reason, and recommendation.
- **Croc AI Orchestrator is separately optional:** when configured, it can enrich the human-readable summary and recommendation.
- **Operators stay responsible:** AI provides context and recommendations; permissions and configured approval still control high-impact actions.
- **The alarm does not wait for AI:** optional analysis is not the foundation of the alert path.

This combination is intended to help sites bring event context, guided response, and reviewable records into one operational view.

## Practical benefits

- Designed to bring related incident context into one workspace
- Supports more consistent handling through versioned response rules
- Optional prioritization support without making AI mandatory
- A shared incident view for authorized operators
- Supported response-status tracking when dispatch is enabled
- Brings available records together for operational review
- Gradual adoption of optional modules per site

Compared with a basic alarm workflow, Sentinel adds an incident workspace, response-plan lifecycle, optional decision support, and structured after-incident review. It does not claim to replace people, emergency procedures, or every existing security product.

The private baseline source includes:

- Device identity, ownership, status, telemetry, and commands
- Alarm records and grouped siren behavior
- A browser-based Command Center
- Incident lists, workspaces, and timelines
- Response-plan versioning and internal review marking
- Advanced-profile readiness configuration checks
- Audit records and CSV export
- Read-only incident summaries
- Post-incident review drafts and submissions

A cloud-connected deployment requires a working network. Equipment and integration suitability are assessed per project.

## Optional modules

The private source also contains default-off or deployment-dependent modules for:

- Camera snapshots
- Rules-first incident scoring with optional external AI enrichment
- Responder assignments and phone location
- Voice calls
- Automation
- Health and predictive experiments
- Response simulations
- Experimental multi-responder coordination
- Advanced reporting and platform controls

Code and focused tests do not mean a module is enabled, field-proven, or release-ready.

## AI reality

The core alarm path does not depend on AI.

Optional incident analysis can produce a rules-based score, category, reason, and recommendation. External AI enrichment requires separate configuration. The current computer-vision module is a placeholder, not a production visual-recognition system.

## Mobile reality

The audited source contains a responsive web console and installable PWA shell. It does not prove a native iPhone or Android application or an end-to-end mobile push deployment.

## Drone reality

There is no production DJI Dock, Matrice, drone, or robot integration today. The private source contains generic future-resource contracts and mock adapters only.

## Status

Croc Sentinel is actively developed and trial-stage. Advanced staging, field, security, performance, mobile, and extended live-environment validation remains incomplete.

Future work includes production computer vision, real physical-resource integrations, verified native mobile applications, broader third-party integrations, and personal/home use. No delivery date is promised.

## Docs

[ARCHITECTURE.md](ARCHITECTURE.md) · [ORCHESTRATOR.md](ORCHESTRATOR.md) · [EXTENSIBILITY.md](EXTENSIBILITY.md) · [VISION_AND_CONCEPTS.md](VISION_AND_CONCEPTS.md)

**Contact:** partnerships@crocnexus.com

---

© Croc Nexus AI Technologies
