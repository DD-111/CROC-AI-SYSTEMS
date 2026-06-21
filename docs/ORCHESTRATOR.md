# Croc AI Orchestrator (brief)

**Croc AI Orchestrator** is Croc Nexus’s **agent coordination layer**: AI agents **score urgency**, **route who to call**, and **keep a full log** — working with **Croc Sentinel Systems** on each deployment.

| | |
|:--|:--|
| **Rules first** | Fixed safety rules always run; AI adds detail |
| **People in charge** | Sensitive steps wait for human approval |
| **Our platform** | Cloud, apps, and logic are **Croc Nexus exclusive** |

Production systems and full source are **not** published in this repository.

---

## Tiny sample

A minimal illustration lives in `src/croc_orchestrator/` — fictional event in, urgency score and summary out:

```bash
python -m src.croc_orchestrator.demo_assess samples/orchestrator/alarm_event.json
```

See also [PRODUCT_OVERVIEW.md](PRODUCT_OVERVIEW.md) and [ARCHITECTURE.md](ARCHITECTURE.md).
