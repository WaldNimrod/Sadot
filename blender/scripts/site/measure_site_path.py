#!/usr/bin/env python3
# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project
# scripts/inspect/measure_site_path.py on 2026-07-08 — Sadot blender/ pipeline bootstrap
# (WP: SDT-S001-P001-WP001). NOTE: SHELL_WALLS/SHELL_FOOTPRINT/GEN_NAMES/AC_NAMES object-name
# prefixes below are the origin container-farm model's naming convention — re-tune once Sadot's
# own model/BUILD_DATA naming convention exists (Stage 3, 3D Modeling).
"""Measure container footprint, equipment AABB, and plan paver path (matrix_basis only)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import bpy
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[2]
LOG = ROOT / "logs" / "assembly" / "site_path_plan.txt"
FOUND_LOG = ROOT / "logs" / "assembly" / "site_foundation_verify.txt"

PATH_W = 0.8
PATH_HALF = PATH_W * 0.5
PATH_THICK = 0.05
PATH_Z = -0.184
GRADE_Z = -0.20
FOUNDATION_DEPTH = 0.40
FOUNDATION_MARGIN = 0.10
FOUNDATION_REVEAL = 0.015  # slab top 15 mm above grade

SHELL_WALLS = ("SHELL.wall_l", "SHELL.wall_r", "SHELL.wall_back")
SHELL_FOOTPRINT = ("SHELL.wall_l", "SHELL.wall_r", "SHELL.wall_back", "SHELL.floor_main")
GEN_NAMES = ("ELE.gen_unit", "mat_GENSET")
AC_NAMES = ("HVAC.ac_body", "HVAC.compr_body")


def aabb_basis(obj):
    mw = obj.matrix_basis
    cs = [mw @ Vector(v) for v in obj.bound_box]
    mn = Vector((min(c.x for c in cs), min(c.y for c in cs), min(c.z for c in cs)))
    mx = Vector((max(c.x for c in cs), max(c.y for c in cs), max(c.z for c in cs)))
    return mn, mx


def first_obj(names):
    for n in names:
        o = bpy.data.objects.get(n)
        if o and o.type == "MESH":
            return o
    return None


def shell_footprint():
    """Outer AABB from SHELL walls (XY) + floor (X only for length)."""
    wall_pts = []
    for name in SHELL_WALLS:
        o = bpy.data.objects.get(name)
        if not o or o.type != "MESH":
            continue
        mn, mx = aabb_basis(o)
        wall_pts.extend([mn, mx])
    if not wall_pts:
        raise RuntimeError("No SHELL wall objects found")
    x0 = min(p.x for p in wall_pts)
    x1 = max(p.x for p in wall_pts)
    y0 = min(p.y for p in wall_pts)
    y1 = max(p.y for p in wall_pts)
    floor = bpy.data.objects.get("SHELL.floor_main")
    if floor and floor.type == "MESH":
        mn, mx = aabb_basis(floor)
        x0 = min(x0, mn.x)
        x1 = max(x1, mx.x)
    return x0, x1, y0, y1


def door_x_end(x0, x1):
    """Door is on high-X end (right / access side per model convention)."""
    door = bpy.data.objects.get("SHELL.door_leaf_closed") or bpy.data.objects.get("SHELL.door_main")
    if door:
        mn, mx = aabb_basis(door)
        return mx.x if abs(mx.x - x1) < abs(mn.x - x0) else mn.x
    return x1


def plan_path_segments(x0, x1, y0, y1, door_x):
    """3 sides: both long walls (Y±) + door end (X at door). Wrap genset/AC at head-end."""
    gen = first_obj(GEN_NAMES)
    ac = first_obj(AC_NAMES)

    # Long walls: path centerline offset PATH_HALF outside outer wall face
    y_long_l = y0 - PATH_HALF
    y_long_r = y1 + PATH_HALF

    equip_ymax = y1
    equip_xmax = x0
    if gen:
        _, mx = aabb_basis(gen)
        equip_ymax = max(equip_ymax, mx.y)
        equip_xmax = max(equip_xmax, mx.x)
    if ac:
        _, mx = aabb_basis(ac)
        equip_ymax = max(equip_ymax, mx.y)
        equip_xmax = max(equip_xmax, mx.x)

    # Door end: strip along X at door side, spanning Y from long-L path to equip wrap
    door_is_high_x = abs(door_x - x1) < abs(door_x - x0)
    if door_is_high_x:
        x_door_center = x1 + PATH_HALF
        x_span_lo, x_span_hi = x0 - 0.05, x1 + PATH_W
    else:
        x_door_center = x0 - PATH_HALF
        x_span_lo, x_span_hi = x0 - PATH_W, x1 + 0.05

    y_wrap_outer = max(y_long_r, equip_ymax + PATH_HALF)
    y_door_span = max(abs(y_long_l), y_wrap_outer)

    segments = []

    # Side L (-Y long wall)
    cx = (x_span_lo + x_span_hi) * 0.5
    sx = (x_span_hi - x_span_lo) * 0.5
    segments.append({
        "name": "SITE_path_side_l",
        "side": "long_wall_-Y",
        "center": (cx, y_long_l, PATH_Z),
        "scale_half": (sx, PATH_HALF, PATH_THICK * 0.5),
    })

    # Side R (+Y long wall) — base strip along container length
    segments.append({
        "name": "SITE_path_side_r",
        "side": "long_wall_+Y",
        "center": (cx, y_long_r, PATH_Z),
        "scale_half": (sx, PATH_HALF, PATH_THICK * 0.5),
    })

    # Equipment wrap at head-end (+Y bulge around genset/AC)
    if equip_ymax > y1 + 0.01 or equip_xmax > x0 + 0.5:
        wrap_cy = (y_long_r + y_wrap_outer) * 0.5
        wrap_hy = (y_wrap_outer - y_long_r) * 0.5 + 0.02
        wrap_cx = (x0 + equip_xmax) * 0.5
        wrap_hx = (equip_xmax - x0) * 0.5 + PATH_HALF
        segments.append({
            "name": "SITE_path_equip_wrap",
            "side": "head_end_equip_wrap",
            "center": (wrap_cx, wrap_cy, PATH_Z),
            "scale_half": (wrap_hx, wrap_hy, PATH_THICK * 0.5),
        })

    # Door end (3rd side) — connects long paths at door X
    segments.append({
        "name": "SITE_path_door_end",
        "side": "door_end",
        "center": (x_door_center, 0.0, PATH_Z),
        "scale_half": (PATH_HALF, y_door_span, PATH_THICK * 0.5),
    })

    return segments, {
        "gen": gen.name if gen else None,
        "ac": ac.name if ac else None,
        "equip_ymax": equip_ymax,
        "equip_xmax": equip_xmax,
        "door_x": door_x,
        "door_is_high_x": door_is_high_x,
    }


def foundation_dims(x0, x1, y0, y1, offset_y=0.0):
    m = FOUNDATION_MARGIN
    fx0, fx1 = x0 - m, x1 + m
    fy0, fy1 = y0 + offset_y - m, y1 + offset_y + m
    top_z = GRADE_Z + FOUNDATION_REVEAL
    cz = top_z - FOUNDATION_DEPTH * 0.5
    return {
        "footprint_m": [fx0, fx1, fy0, fy1],
        "size_mm": [
            round((fx1 - fx0) * 1000, 1),
            round((fy1 - fy0) * 1000, 1),
            round(FOUNDATION_DEPTH * 1000, 1),
        ],
        "top_z_m": top_z,
        "center_z_m": cz,
        "reveal_above_grade_mm": round(FOUNDATION_REVEAL * 1000, 1),
    }


def emit(lines, text=""):
    lines.append(text)
    print(text)


def main():
    x0, x1, y0, y1 = shell_footprint()
    door_x = door_x_end(x0, x1)
    segments, meta = plan_path_segments(x0, x1, y0, y1, door_x)
    found_main = foundation_dims(x0, x1, y0, y1, 0.0)

    lines = []
    emit(lines, f"site_path_plan — {bpy.data.filepath}")
    emit(lines, f"matrix_basis measurements (mm)")
    emit(lines, "")
    emit(lines, "=== CONTAINER FOOTPRINT (SHELL walls/floor) ===")
    emit(lines, f"  X: [{x0*1000:.1f}, {x1*1000:.1f}]  span={(x1-x0)*1000:.1f} mm")
    emit(lines, f"  Y: [{y0*1000:.1f}, {y1*1000:.1f}]  span={(y1-y0)*1000:.1f} mm")
    emit(lines, f"  door_x={door_x*1000:.1f} mm  door_is_high_x={meta['door_is_high_x']}")
    emit(lines, "")
    emit(lines, "=== EQUIPMENT AABB ===")
    for label, nm in (("genset", meta["gen"]), ("ac", meta["ac"])):
        o = bpy.data.objects.get(nm) if nm else None
        if o:
            mn, mx = aabb_basis(o)
            emit(lines, f"  {label} ({nm}):")
            emit(lines, f"    X [{mn.x*1000:.1f}, {mx.x*1000:.1f}]  Y [{mn.y*1000:.1f}, {mx.y*1000:.1f}]")
        else:
            emit(lines, f"  {label}: NOT FOUND")
    emit(lines, f"  equip_ymax={meta['equip_ymax']*1000:.1f} mm  equip_xmax={meta['equip_xmax']*1000:.1f} mm")
    emit(lines, "")
    emit(lines, f"=== PATH PLAN (width={PATH_W*1000:.0f} mm, Z={PATH_Z*1000:.1f} mm) ===")
    for seg in segments:
        cx, cy, cz = seg["center"]
        hx, hy, hz = seg["scale_half"]
        emit(lines, f"  {seg['name']} [{seg['side']}]")
        emit(lines, f"    center=({cx*1000:.1f}, {cy*1000:.1f}, {cz*1000:.1f}) mm")
        emit(lines, f"    half_extents=({hx*1000:.1f}, {hy*1000:.1f}, {hz*1000:.1f}) mm")
        emit(lines, f"    full_size=({hx*2*1000:.1f}, {hy*2*1000:.1f}, {hz*2*1000:.1f}) mm")
    emit(lines, "")
    emit(lines, "=== FOUNDATION (main container) ===")
    emit(lines, f"  footprint X [{found_main['footprint_m'][0]*1000:.1f}, {found_main['footprint_m'][1]*1000:.1f}]")
    emit(lines, f"  footprint Y [{found_main['footprint_m'][2]*1000:.1f}, {found_main['footprint_m'][3]*1000:.1f}]")
    emit(lines, f"  size_mm (L×W×D): {found_main['size_mm']}")
    emit(lines, f"  grade_z={GRADE_Z*1000:.1f} mm  slab_top={found_main['top_z_m']*1000:.1f} mm  reveal={found_main['reveal_above_grade_mm']} mm")

    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    emit(lines, f"\nWROTE {LOG}")

    found_lines = [
        f"site_foundation_verify — {bpy.data.filepath}",
        f"GRADE_Z={GRADE_Z*1000:.1f} mm",
        f"FOUNDATION_DEPTH={FOUNDATION_DEPTH*1000:.0f} mm",
        f"MARGIN={FOUNDATION_MARGIN*1000:.0f} mm per side",
        f"slab_top_z={found_main['top_z_m']*1000:.1f} mm (reveal {found_main['reveal_above_grade_mm']} mm above grade)",
        f"footprint_mm: {found_main['size_mm'][0]} × {found_main['size_mm'][1]} × {found_main['size_mm'][2]}",
    ]
    FOUND_LOG.write_text("\n".join(found_lines) + "\n", encoding="utf-8")
    print("WROTE", FOUND_LOG)

    if "--json" in sys.argv:
        out = ROOT / "logs" / "assembly" / "site_path_plan.json"
        out.write_text(json.dumps({
            "footprint": {"x0": x0, "x1": x1, "y0": y0, "y1": y1},
            "segments": segments,
            "foundation_main": found_main,
            "meta": meta,
        }, indent=2), encoding="utf-8")
        print("WROTE", out)


if __name__ == "__main__":
    main()
