"""MQTT alarm event stub for public artifact — not production code."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any


@dataclass
class MqttAlarmEnvelope:
    topic: str
    payload: dict[str, Any]

    @classmethod
    def from_device_alarm(cls, device_id: str, owner: str, group: str) -> MqttAlarmEnvelope:
        return cls(
            topic=f"sentinel/{device_id}/alarm",
            payload={
                "proto": 2,
                "type": "alarm",
                "device_id": device_id,
                "owner_admin": owner,
                "notification_group": group,
                "triggered_by": "button",
            },
        )

    def to_json(self) -> str:
        return json.dumps({"topic": self.topic, "payload": self.payload}, ensure_ascii=False)


def fan_out_siblings(alarm: MqttAlarmEnvelope, fleet: list[dict[str, Any]]) -> list[str]:
    """Return device IDs that would receive siren fan-out (same owner + group)."""
    owner = alarm.payload.get("owner_admin")
    group = alarm.payload.get("notification_group")
    return [
        d["device_id"]
        for d in fleet
        if d.get("owner_admin") == owner and d.get("group") == group
    ]
