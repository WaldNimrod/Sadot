#!/usr/bin/env python3
# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project scripts/drawing/compose_sheet.py
# on 2026-07-08 — Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
# NOTE: this file's `build_p101()` function and lib imports (rear_site_projection, tank_specs) are
# origin-project-specific (microgreens reservoir sheet P-101) — they were intentionally NOT
# re-harvested into design/lib/ (see 08_REPLICATION_GUIDE.md "what NOT to copy blindly"). This
# script is kept verbatim as a worked reference for the compose_sheet.py pattern; it will not run
# as-is against Sadot's own lib/ (which omits rear_site_projection.py, tank_specs.py). Write a
# Sadot-specific compose_sheet.py (own build_<sheet>() function over design/lib/ modules) when
# Sadot's drawing-production WP opens.
"""
compose_sheet.py — assemble model-native SVG extracts + measurement annotations → PDF.

  python3 scripts/drawing/compose_sheet.py --sheet P101 --preset P-101_reservoir
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "_communication" / "team_100_engineering" / "WP_PHASE5_TECHNICAL_DOCS"
sys.path.insert(0, str(DOCS))

from lib import drawing_kit as dk  # noqa: E402
from lib import sheet_layout as sl  # noqa: E402
from lib.measure_model import load_measurements  # noqa: E402
from lib.rear_site_projection import RearSitePlan, dim_mm  # noqa: E402
from lib.sheet_export import export_sheet  # noqa: E402
from lib.tank_specs import DRAIN_DN_MM, MAIN_TANK, NURSERY_TANK, PROTRUSION_ABOVE_GRADE_MM  # noqa: E402

PRESETS = DOCS / "drawings" / "view_presets"
BLUE = "#2f6fb0"
ORANGE = "#c2410c"
GREEN2 = "#2e7d32"


def load_preset(name: str) -> dict:
    path = PRESETS / (name if name.endswith(".yaml") else f"{name}.yaml")
    raw = subprocess.check_output(
        ["python3", "-c", "import yaml, json, sys; print(json.dumps(yaml.safe_load(open(sys.argv[1]))))", str(path)],
        text=True,
    )
    return json.loads(raw)


def obj_map(data: dict) -> dict:
    return {o["name"]: o for o in data["objects"] if not o.get("missing")}


def embed_extract_svg(svg_path: Path, x: float, y: float, w: float, h: float) -> str:
    if not svg_path.exists():
        return dk.Rt(x, y, w, h, fill="#fee", stroke="#c00") + dk.T(x + w / 2, y + h / 2, "MISSING EXTRACT", 2.5, "#c00", "middle", rtl=False)
    text = svg_path.read_text(encoding="utf-8")
    m = re.search(r'viewBox="([^"]+)"', text)
    inner = re.sub(r"<\?xml[^>]*\?>", "", text)
    inner = re.sub(r"<svg[^>]*>", "", inner, count=1)
    inner = inner.replace("</svg>", "")
    # Scale group to fit zone
    if m:
        parts = m.group(1).split()
        vbw, vbh = float(parts[2]), float(parts[3])
    else:
        vbw, vbh = w, h
    sx, sy = (w - 2) / vbw, (h - 6) / vbh
    s = dk.Rt(x, y, w, h, fill="#fff", stroke="#bbb", sw=0.25)
    s += f'<g transform="translate({x + 1},{y + 2}) scale({sx:.5f},{sy:.5f})">{inner}</g>'
    return s


def build_p101(data: dict, preset: dict) -> str:
    m = obj_map(data)
    main = m["WTR.tank_main"]
    nur = m["WTR.tank_nursery"]
    wall = m["SHELL.wall_back"]
    mb, nb = main["bounds_m"], nur["bounds_m"]
    mc, nc = main["center_m"], nur["center_m"]
    gz = m["SHELL.grade_ground"]["bounds_m"]["z"][0]

    comp = preset.get("compose", {})
    extract_dir = DOCS / preset.get("extract_dir", "drawings/_extracts/P101")
    zones = comp.get("zones", {})
    scale = preset.get("scale", 20)

    s = dk.frame()
    s += sl.head_for_construction(
        comp.get("title", "Sheet P-101 — Reservoirs"),
        "Model-native extract + matrix_basis _022 annotations",
    )
    s += sl.layer_legend(12, 32)

    # View frames + embedded extracts
    labels = {
        "plan": "Plan 1:20 — rear yard (mesh extract)",
        "section_aa": "Section A-A 1:20 — longitudinal",
        "section_bb": "Section B-B 1:20 — transverse",
        "detail": f"Detail 3 — drain O{DRAIN_DN_MM} 1:10",
    }
    files = {
        "plan": extract_dir / "P101_plan.svg",
        "section_aa": extract_dir / "P101_section_aa.svg",
        "section_bb": extract_dir / "P101_section_bb.svg",
        "detail": extract_dir / "P101_detail_drain.svg",
    }
    for key, label in labels.items():
        z = zones.get(key, {})
        zx, zy, zw, zh = z.get("x", 14), z.get("y", 40), z.get("w", 100), z.get("h", 80)
        s += dk.Rt(zx, zy, zw, zh, fill="none", stroke="#ccc", sw=0.25, dash="2 1")
        s += dk.T(zx + zw / 2, zy - 2.5, label, 2.6, dk.GREEN, "middle", True, rtl=False)
        s += embed_extract_svg(files[key], zx, zy, zw, zh)

    # Context thumbnail top-right
    ctx = DOCS / comp.get("context_image", "drawings/_assets/C4_context_plan.png")
    if ctx.exists():
        rel = "../_assets/C4_context_plan.png"
        s += dk.Rt(360, 40, 48, 36, fill="#fff", stroke="#888", sw=0.35)
        s += (
            f'<image x="361" y="41" width="46" height="30" preserveAspectRatio="xMidYMid meet" href="{rel}"/>'
        )
        s += dk.T(384, 73, "Context", 1.5, "#666", "middle", ital=True, rtl=False)

    # Dimension overlay on plan zone
    px, py = zones.get("plan", {}).get("x", 14) + 6, zones.get("plan", {}).get("y", 40) + 8
    plan = RearSitePlan(px, py, scale=scale)
    setback_mm = abs(mb["x"][1]) * 1000
    s += plan.dim_h_site(0, mb["x"][1], mb["y"][1] + 0.12, dim_mm(setback_mm))
    s += plan.dim_h_site(mb["x"][0], mb["x"][1], mb["y"][0] - 0.1, dim_mm(main["size_mm"][0]))
    gap_mm = (nb["y"][0] - mb["y"][1]) * 1000
    if gap_mm > 0:
        s += plan.dim_v_site(mb["y"][1], nb["y"][0], mb["x"][1] + 0.1, dim_mm(gap_mm))
    s += dk.enode(plan.sx(mc[0]), plan.sy(mc[1]), "1", BLUE, 1.5, 1.6)
    s += dk.enode(plan.sx(nc[0]), plan.sy(nc[1]), "2", ORANGE, 1.4, 1.5)

    notes = [
        "Primary views: mesh orthographic edge extract from IsraelMicrogreens_022.",
        f"HE-TNK O{int(main['size_mm'][1])} L{int(main['size_mm'][0])} mm; N-TANK O{int(nur['size_mm'][1])} L{int(nur['size_mm'][0])} mm.",
        f"Crowns {PROTRUSION_ABOVE_GRADE_MM} mm AFL; drain O{DRAIN_DN_MM} elbow mid-depth — no air gap.",
        "Fill/service from top ports per TANK_PRODUCT_SPECS.md.",
    ]
    s += sl.contractor_notes(notes, 14, 212, 188, 44)

    parts = [
        ("1", "HE-TNK", f"O{int(main['size_mm'][1])} x L{int(main['size_mm'][0])} mm"),
        ("2", "N-TANK", f"O{int(nur['size_mm'][1])} x L{int(nur['size_mm'][0])} mm — 1000 L"),
        ("3", f"DR-O{DRAIN_DN_MM}", "Detail 3 — mesh section extract"),
        ("4", "PERGOLA", "SHELL.pergola_* @ model"),
    ]
    s += sl.parts_index_table(parts, 208, 212)
    s += sl.scale_bar(318, 268, 1000, 40, f"Scale 1:{scale}")
    rev = comp.get("revision", "Phase-5 model-native v1")
    s += dk.titleblock(comp.get("title", "Sheet P-101"), "P-101", f"1:{scale} @ A3", revision=rev)
    s += dk.T(14, 262, "Source: matrix_basis _022 + mesh extract + TANK_PRODUCT_SPECS.md", 1.8, "#666", "start", ital=True, rtl=False)
    return s


def main():
    argv = sys.argv[1:]
    sheet = "P101"
    preset_name = "P-101_reservoir"
    for i, a in enumerate(argv):
        if a == "--sheet" and i + 1 < len(argv):
            sheet = argv[i + 1]
        if a == "--preset" and i + 1 < len(argv):
            preset_name = argv[i + 1]

    preset = load_preset(preset_name)
    data = load_measurements(sheet)
    body = build_p101(data, preset)
    comp = preset.get("compose", {})
    out_dir = DOCS / comp.get("output_dir", "drawings/P_reservoir")
    stem = comp.get("stem", "P-101_reservoir")
    paths = export_sheet(out_dir, stem, body, "P-101 Reservoirs")
    print("EXPORT", paths)


if __name__ == "__main__":
    main()
