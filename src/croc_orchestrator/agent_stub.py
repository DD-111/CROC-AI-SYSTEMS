"""Minimal agent stub for public artifact demo — not production code."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentContext:
    event: dict[str, Any]
    extensions: dict[str, Any] = field(default_factory=dict)


class BaseAgentStub:
    name: str = "base"

    def run(self, context: AgentContext) -> AgentContext:
        raise NotImplementedError


class RiskAgentStub(BaseAgentStub):
    name = "risk"

    def run(self, context: AgentContext) -> AgentContext:
        event = context.event
        score = 35
        if event.get("trigger_count", 0) >= 3:
            score += 27
        if event.get("rssi", 0) < -85:
            score += 15
        if not event.get("snapshot_exists", False):
            score += 12
        context.extensions["risk"] = {
            "risk_score": min(score, 100),
            "level": "HIGH" if score >= 70 else "MEDIUM" if score >= 40 else "LOW",
            "method": "rules",
        }
        return context


class SummaryAgentStub(BaseAgentStub):
    name = "summary"

    def run(self, context: AgentContext) -> AgentContext:
        risk = context.extensions.get("risk", {})
        context.extensions["summary"] = {
            "text": (
                f"Device {context.event.get('device_id')} alarm; "
                f"risk {risk.get('risk_score', '?')}/100."
            ),
            "category": "Emergency" if risk.get("risk_score", 0) >= 70 else "Security",
        }
        return context
