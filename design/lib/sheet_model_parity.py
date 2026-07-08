# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project
# _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/sheet_model_parity.py on
# 2026-07-08 — Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
# NOTE: ROOT/REPO path-climbing below (`parent.parent` then `.parents[2]`) encodes the origin
# repo's folder depth (lib/ under _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/).
# Verify/adjust this path arithmetic against design/lib/'s actual depth under the Sadot repo root
# before relying on MEAS in this spoke.
"""Verify drawing generator uses measurement JSON — block schematic drift."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parents[2]
MEAS = REPO / "exports" / "ai_bridge"


def check_sheet(sheet_id: str, svg_path: Path) -> list[str]:
    errs: list[str] = []
    json_path = MEAS / f"sheet_measurements_{sheet_id}.json"
    if not json_path.exists():
        return [f"missing {json_path}"]
    data = json.loads(json_path.read_text(encoding="utf-8"))
    svg = svg_path.read_text(encoding="utf-8")
    svg_check = re.sub(r'href="data:image[^"]*"', "", svg)

    if "plx(" in svg or "ply(" in svg:
        errs.append("schematic plx/ply coordinates detected")

    if (
        "matrix_basis" not in svg_check
        and "model coords" not in svg_check.lower()
        and "mesh extract" not in svg_check.lower()
    ):
        errs.append("missing model source annotation")

    for obj in data["objects"]:
        if obj.get("missing"):
            errs.append(f"model missing required object: {obj['name']}")
            continue
        w = obj["size_mm"][0]
        if w > 100 and str(int(round(w))) not in svg_check and str(int(w)) not in svg_check:
            if obj["name"].startswith("WTR.tank") and "_hatch" not in obj["name"]:
                errs.append(f"tank width {w} mm not found in SVG for {obj['name']}")

    return errs


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if len(argv) < 2:
        print("usage: sheet_model_parity.py <sheet_id> <svg_path>")
        return 1
    errs = check_sheet(argv[0], Path(argv[1]))
    if errs:
        print("PARITY_FAIL", errs)
        return 1
    print("PARITY_PASS", argv[1])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
