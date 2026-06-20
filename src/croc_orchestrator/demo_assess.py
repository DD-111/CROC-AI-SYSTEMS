#!/usr/bin/env python3
"""Run sample event through example scoring flow."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from .workflow_sample import run_sample_flow


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("samples/orchestrator/alarm_event.json")
    event = json.loads(path.read_text(encoding="utf-8"))
    result = run_sample_flow(event)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
