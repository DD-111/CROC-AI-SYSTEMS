"""Example handling flow for sample events."""

from __future__ import annotations

from typing import Any

from .agent_stub import EventContext, RiskStep, SummaryStep


def school_zone_policy(context: dict[str, Any]) -> dict[str, Any]:
    zone = str(context.get("zone", ""))
    hour = context.get("local_hour", 22)
    if "school" in zone.lower() and hour >= 20:
        return {
            "priority": 2,
            "actions": ["notify_guard", "check_camera"],
            "note": "school area after hours",
        }
    return {"priority": 1, "actions": ["standard_ack"], "note": "default"}


def run_sample_flow(event: dict[str, Any]) -> dict[str, Any]:
    ctx = EventContext(event=event)
    ctx = RiskStep().run(ctx)
    ctx = SummaryStep().run(ctx)
    policy = school_zone_policy({**event, "local_hour": 22})
    ctx.extensions["next_steps"] = {
        "priority": policy["priority"],
        "actions": policy["actions"],
        "status": "waiting_for_approval",
    }
    return {
        "event_id": event.get("event_id"),
        "extensions": ctx.extensions,
    }
