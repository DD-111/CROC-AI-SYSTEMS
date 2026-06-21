"""Edge sketch only — not production code.

Hints at how Croc AI Orchestrator chains steps internally.
Incomplete, cannot run our cloud stack. Public repo illustration only.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class OrchestratorStep(ABC):
    @abstractmethod
    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        ...


class RouteStep(OrchestratorStep):
    """Who to call — production logic runs on Croc Nexus cloud only."""

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError(
            "Production routing runs on Croc Nexus cloud only."
        )


class FollowUpStep(OrchestratorStep):
    """Escalation if nobody answers — not implemented in this repository."""

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError(
            "Follow-up timers are internal to Croc AI Orchestrator."
        )


PIPELINE_SHAPE = {
    "published_here": ["score_urgency", "write_summary"],
    "trial_production_with_sentinel": [
        "score_urgency",
        "use_camera_context",
        "summarise_for_operator",
        "route_call_and_alert",
        "escalate_if_unanswered",
        "log_and_audit",
    ],
    "in_development_not_open": [
        "cao_agent_model",
        "digital_employee_teams",
        "ai_control_panel",
        "token_relay",
        "embodied_intelligence",
        "drones",
        "security_devices",
        "personal_home_use",
    ],
}
