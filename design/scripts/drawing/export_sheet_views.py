#!/usr/bin/env python3
# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project scripts/drawing/export_sheet_views.py
# on 2026-07-08 — Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
# NOTE: paths below (DOCS, PRESETS) still point at the origin repo's
# `_communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS` layout — update ROOT-relative
# paths to Sadot's own design/ tree (see 06_STANDARDS_PROJECT.md) when this pipeline is activated.
"""
export_sheet_views.py — extract orthographic SVG views from _022 per YAML preset.

Model-native mesh edge projection. Section Toolbox optional (see install_section_toolbox.md).

  blender --background blender/IsraelMicrogreens_022.blend \\
    --python scripts/drawing/export_sheet_views.py -- --preset P-101_reservoir
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "_communication" / "team_100_engineering" / "WP_PHASE5_TECHNICAL_DOCS"
PRESETS = DOCS / "drawings" / "view_presets"
LOG = ROOT / "logs" / "drawing" / "export_sheet_views.json"


def load_preset(path: Path) -> dict:
    raw = subprocess.check_output(
        ["python3", "-c", "import yaml, json, sys; print(json.dumps(yaml.safe_load(open(sys.argv[1]))))", str(path)],
        text=True,
    )
    return json.loads(raw)


def main():
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    preset_name = "P-101_reservoir"
    for i, a in enumerate(argv):
        if a == "--preset" and i + 1 < len(argv):
            preset_name = argv[i + 1]

    preset_path = PRESETS / (preset_name if preset_name.endswith(".yaml") else f"{preset_name}.yaml")
    preset = load_preset(preset_path)

    # Import sibling module (Blender adds script dir to path)
    script_dir = Path(__file__).resolve().parent
    if str(script_dir) not in sys.path:
        sys.path.insert(0, str(script_dir))
    from mesh_ortho_export import write_view_svg

    extract_rel = preset.get("extract_dir", "drawings/_extracts/P101")
    out_dir = DOCS / extract_rel
    out_dir.mkdir(parents=True, exist_ok=True)

    stb_status = "not_installed"
    try:
        import bpy

        for k in bpy.context.preferences.addons.keys():
            if "section" in k.lower() or "stb" in k.lower():
                stb_status = f"enabled:{k}"
                break
    except ImportError:
        stb_status = "no_bpy"

    report = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "preset": preset_name,
        "blend": "",
        "section_toolbox": stb_status,
        "method": "mesh_ortho_edge_projection",
        "views": [],
    }

    try:
        import bpy

        report["blend"] = bpy.data.filepath
    except ImportError:
        pass

    for view in preset.get("views", []):
        out_name = view.get("output", f"{view['id']}.svg")
        out_path = out_dir / out_name
        n = write_view_svg(view, preset, out_path)
        report["views"].append({"id": view["id"], "file": str(out_path), "edge_segments": n})
        print("WROTE", out_path, "segments", n)

    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("LOG", LOG)


if __name__ == "__main__":
    main()
