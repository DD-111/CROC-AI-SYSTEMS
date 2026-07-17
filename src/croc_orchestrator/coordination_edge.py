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
    """Routing shape only — no working router is published here."""

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError(
            "Production routing runs on Croc Nexus cloud only."
        )


class FollowUpStep(OrchestratorStep):
    """Future follow-up shape — no automatic contact ladder is claimed."""

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError(
            "Automatic contact-list escalation is not implemented here."
        )


PIPELINE_SHAPE = {
    "published_here": ["score_urgency", "write_summary"],
    "optional_private_source": [
        "score_urgency",
        "summarise_for_operator",
        "route_assigned_responder",
        "emit_supported_audit_records",
    ],
    "not_claimed_as_complete": [
        "computer_vision",
        "automatic_next_contact_escalation",
        "complete_external_action_log",
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
