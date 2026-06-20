"""Example cloud alarm message helpers."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any


@dataclass
class AlarmMessage:
    channel: str
    payload: dict[str, Any]

    @classmethod
    def from_device(cls, device_id: str, owner: str, group: str) -> AlarmMessage:
        return cls(
            channel=f"site/{device_id}/alarm",
            payload={
                "type": "alarm",
                "device_id": device_id,
                "site_owner": owner,
                "device_group": group,
                "triggered_by": "button",
            },
        )

    def to_json(self) -> str:
        return json.dumps({"channel": self.channel, "payload": self.payload}, ensure_ascii=False)


def linked_devices(alarm: AlarmMessage, fleet: list[dict[str, Any]]) -> list[str]:
    """Devices in the same organisation and group that would react together."""
    owner = alarm.payload.get("site_owner")
    group = alarm.payload.get("device_group")
    return [
        d["device_id"]
        for d in fleet
        if d.get("site_owner") == owner and d.get("group") == group
    ]
