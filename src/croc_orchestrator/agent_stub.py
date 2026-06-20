"""Example urgency scoring from sample event data."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EventContext:
    event: dict[str, Any]
    extensions: dict[str, Any] = field(default_factory=dict)


class RiskStep:
    def run(self, context: EventContext) -> EventContext:
        event = context.event
        score = 35
        if event.get("trigger_count", 0) >= 3:
            score += 27
        if str(event.get("signal_strength", "")).lower() == "weak":
            score += 15
        if not event.get("photo_received", False):
            score += 12
        context.extensions["risk"] = {
            "urgency_score": min(score, 100),
            "level": "high" if score >= 70 else "medium" if score >= 40 else "low",
        }
        return context


class SummaryStep:
    def run(self, context: EventContext) -> EventContext:
        risk = context.extensions.get("risk", {})
        context.extensions["summary"] = {
            "text": (
                f"Device {context.event.get('device_id')} raised an alarm; "
                f"urgency {risk.get('urgency_score', '?')}/100."
            ),
            "category": "emergency" if risk.get("urgency_score", 0) >= 70 else "security",
        }
        return context
