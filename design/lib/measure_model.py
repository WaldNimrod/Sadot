# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project
# _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/measure_model.py on 2026-07-08 —
# Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
# NOTE: ROOT = parents[4] encodes the origin repo's folder depth. Verify/adjust against
# design/lib/'s actual depth under the Sadot repo root before relying on load_measurements().
"""Read sheet measurement JSON produced by scripts/inspect/measure_sheet.py."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def load_measurements(sheet_id: str) -> dict:
    path = ROOT / "exports" / "ai_bridge" / f"sheet_measurements_{sheet_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"Missing measurements: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def mm(obj: dict, axis: str) -> float:
    """Axis min/max/center/size in mm from measurement record."""
    b = obj["bounds_m"]
    if axis == "size_x":
        return round((b["x"][1] - b["x"][0]) * 1000, 1)
    if axis == "size_y":
        return round((b["y"][1] - b["y"][0]) * 1000, 1)
    if axis == "size_z":
        return round((b["z"][1] - b["z"][0]) * 1000, 1)
    if axis in ("x", "y", "z"):
        c = obj["center_m"]
        return round(c[axis] * 1000, 1)
    raise KeyError(axis)


def fmt_mm(val: float) -> str:
    v = round(val)
    if abs(v) >= 1000:
        return f"{v / 1000:.2f} m"
    return f"{v} mm"
