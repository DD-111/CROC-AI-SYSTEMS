# Croc Coordination (brief)

**Croc Coordination** is Croc Nexus’s AI layer for site alerts: it **scores urgency**, **routes who to call**, and **keeps a full log** — between monitoring and people on the ground.

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
