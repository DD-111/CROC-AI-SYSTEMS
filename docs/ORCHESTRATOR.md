# Croc AI Orchestrator

**Croc AI Orchestrator** is Croc Nexus’s private direction for optional event analysis and response coordination.

It is not a universal, always-on AI layer. In the current private source:

- The core alarm path does not depend on AI.
- Optional incident analysis is disabled by default.
- Rules produce the baseline score and reason.
- External AI enrichment can be added when configured.
- Failed enrichment can fall back to rules.
- Selected high-impact actions remain subject to permissions and configured approval.

Optional responder dispatch, voice calls, phone location, automation, and experimental multi-responder coordination are separate modules. Their presence in source does not mean they are enabled or field-validated at a deployment.

The current computer-vision module is a placeholder and does not perform production visual recognition.

The current drone and robot adapters are mocks for a possible future interface. They do not control hardware.

## Public sample

The sample under `src/croc_orchestrator/` applies fixed Python rules to fictional event data:

```bash
python -m src.croc_orchestrator.demo_assess samples/orchestrator/alarm_event.json
```

It does not call an AI model and is not the production Orchestrator.

Production systems and full private source are not published here.

See [PRODUCT_OVERVIEW.md](PRODUCT_OVERVIEW.md) and [ARCHITECTURE.md](ARCHITECTURE.md).
