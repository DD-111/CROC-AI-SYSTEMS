"""Sample workflow + skill for public artifact — not production code."""

from __future__ import annotations

from typing import Any

from .agent_stub import AgentContext, RiskAgentStub, SummaryAgentStub


def school_zone_skill(context: dict[str, Any]) -> dict[str, Any]:
    """Example domain skill: night escalation in school zones."""
    zone = str(context.get("zone", ""))
    hour = context.get("local_hour", 22)
    if "school" in zone.lower() and hour >= 20:
        return {
            "incident_level": 2,
            "actions": ["notify_guard", "check_camera_feed"],
            "rationale": "school zone night policy",
        }
    return {"incident_level": 1, "actions": ["standard_ack"], "rationale": "default"}


def run_demo_pipeline(event: dict[str, Any]) -> dict[str, Any]:
    ctx = AgentContext(event=event)
    ctx = RiskAgentStub().run(ctx)
    ctx = SummaryAgentStub().run(ctx)
    skill = school_zone_skill({**event, "local_hour": 22})
    ctx.extensions["commander"] = {
        "incident_level": skill["incident_level"],
        "actions": skill["actions"],
        "status": "awaiting_approval",
    }
    return {
        "event_id": event.get("event_id"),
        "extensions": ctx.extensions,
        "artifact_notice": "stub output — private repo has full 7-agent pipeline",
    }
