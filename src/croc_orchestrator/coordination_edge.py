"""Edge sketch only — not production code.

This file hints at how Croc Coordination chains steps internally.
It is incomplete, cannot run our cloud stack, and omits models,
APIs, and tenant wiring. For illustration in the public repo only.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

# Production uses more stages and real routing; we publish only the shape.


class CoordinationStep(ABC):
    @abstractmethod
    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        ...


class RouteStep(CoordinationStep):
    """Who to call and what to do first — runs in production, not here."""

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError(
            "Production routing runs on Croc Nexus cloud only."
        )


class FollowUpStep(CoordinationStep):
    """Escalation if nobody answers — not implemented in this repository."""

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError(
            "Follow-up and SLA timers are internal to Croc Coordination."
        )


# Stages we use in production vs what this repo exposes.
PIPELINE_SHAPE = {
    "published_here": ["score_urgency", "write_summary"],
    "runs_in_production": [
        "score_urgency",
        "use_camera_context",
        "summarise_for_operator",
        "route_call_and_alert",
        "escalate_if_unanswered",
        "log_and_audit",
    ],
    "evolving_with_cao": [
        "deeper_coordination",
        "richer_follow_up",
        "learning_from_outcomes",
    ],
}
