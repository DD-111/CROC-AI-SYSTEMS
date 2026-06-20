"""Example handling flow — minimal illustration only."""

from __future__ import annotations

from typing import Any

from .agent_stub import EventContext, RiskStep, SummaryStep


def run_sample_flow(event: dict[str, Any]) -> dict[str, Any]:
    ctx = EventContext(event=event)
    ctx = RiskStep().run(ctx)
    ctx = SummaryStep().run(ctx)
    return {
        "event_id": event.get("event_id"),
        "extensions": ctx.extensions,
    }
