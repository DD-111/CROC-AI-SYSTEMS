# Extensibility

Croc Sentinel is configured per project on Croc Nexus–controlled product infrastructure. There is no white-label offering.

## Per-site scope

A trial scope can define:

- Supported devices and groups
- Alarm behavior and quiet periods
- Notification recipients and enabled providers
- Response rules and internally reviewed plan versions
- Authorized users and roles
- Optional cameras, dispatch, voice, automation, or reporting modules

Compatibility, provider setup, permissions, validation steps, and availability must be agreed before rollout.

## Maturity labels

### Baseline source

Device management, alarm records, incident views, timelines, response plans, advanced-profile readiness checks, audit records, read-only incident summaries, and post-incident reviews exist in the private source.

This does not by itself prove that a customer deployment is configured or field-ready.

### Optional deployment integration

The source contains optional paths for:

- Camera snapshots
- Rules-first incident analysis and external AI enrichment
- Responder assignments and consent-aware phone location
- Voice calls
- Automation
- Advanced exports and backup workflows

Most are disabled by default and require configuration and site validation.

### Experimental or contract-only

- Side-effect-free response simulation
- Device-health and predictive-maintenance experiments
- Experimental multi-responder coordination
- Generic future-resource contracts
- Mock drone and robot adapters with no physical execution

### Future direction

- Production computer vision
- Real drone or robotic control
- Verified native mobile applications
- Broader third-party integrations
- Personal or home use
- Wider AI-agent and digital-team products

Future items have no delivery date or availability promise unless separately agreed in writing.

## Principles

1. The core alarm path should not wait for optional AI analysis.
2. Optional analysis may assist an operator; it does not replace human responsibility.
3. Selected high-impact actions require permissions and configured approval.
4. Supported actions can produce event and audit records; no claim is made that every external action is captured.
5. Customer-account and device-ownership boundaries are enforced in supported paths.
6. Deployment-specific security, privacy, retention, provider, and backup settings must be reviewed per site.

See [ARCHITECTURE.md](ARCHITECTURE.md) and [PRODUCT_OVERVIEW.md](PRODUCT_OVERVIEW.md).
