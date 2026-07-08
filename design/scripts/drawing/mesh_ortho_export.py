# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project scripts/drawing/mesh_ortho_export.py
# on 2026-07-08 — Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
# NOTE: object-prefix filter ("SHELL.", "WTR.", "DRN.") and the rear-yard projection offset
# (-1.175) below are origin-project-specific conventions — re-tune once Sadot's own model/BUILD_DATA
# naming convention exists.
"""Orthographic mesh edge projection to SVG — model-native vector extract (no hand geometry)."""
from __future__ import annotations

from pathlib import Path


def _world_verts(obj):
    import bpy
    from mathutils import Vector

    mw = obj.matrix_basis
    return [mw @ v.co.copy() for v in obj.data.vertices]


def _world_edges(obj):
    verts = _world_verts(obj)
    for e in obj.data.edges:
        yield verts[e.vertices[0]], verts[e.vertices[1]]


def _in_crop(p, crop):
    if not crop:
        return True
    return (
        crop["x"][0] <= p.x <= crop["x"][1]
        and crop["y"][0] <= p.y <= crop["y"][1]
        and crop["z"][0] <= p.z <= crop["z"][1]
    )


def _edge_in_crop(a, b, crop):
    return _in_crop(a, crop) or _in_crop(b, crop)


def _project_plan(p):
    """Rear-yard local: site_x = -world_x, site_y = world_y - (-1.175)."""
    return (-p.x, p.y - (-1.175))


def _project_section_y(p):
    """Longitudinal: site_x vs Z."""
    return (-p.x, p.z)


def _project_section_x(p):
    """Transverse: site_y vs Z."""
    return (p.y - (-1.175), p.z)


def _mm(v, scale):
    return v * 1000.0 / scale


def collect_objects(prefixes, collection_names=None):
    import bpy

    allowed_coll = set(collection_names or [])
    objs = []
    for obj in bpy.data.objects:
        if obj.type != "MESH":
            continue
        if not any(obj.name.startswith(p) for p in prefixes):
            continue
        if allowed_coll:
            names = {c.name for c in obj.users_collection}
            if not names & allowed_coll:
                continue
        objs.append(obj)
    return objs


def extract_edges(view_type: str, crop: dict | None, cut_m: float | None, cut_tol: float = 0.15):
    """Return list of ((u0,v0),(u1,v1)) in world-derived 2D coords (metres)."""
    import bpy

    prefixes = ["SHELL.", "WTR.", "DRN."]
    objs = collect_objects(prefixes)
    lines = []
    for obj in objs:
        for a, b in _world_edges(obj):
            if crop and not _edge_in_crop(a, b, crop):
                continue
            if view_type == "ortho_top":
                lines.append((_project_plan(a), _project_plan(b)))
            elif view_type == "ortho_side":
                if cut_m is not None:
                    if abs(a.y - cut_m) > cut_tol and abs(b.y - cut_m) > cut_tol:
                        if not (a.y <= cut_m <= b.y or b.y <= cut_m <= a.y):
                            continue
                lines.append((_project_section_y(a), _project_section_y(b)))
            elif view_type == "ortho_side_x":
                if cut_m is not None:
                    if abs(a.x - cut_m) > cut_tol and abs(b.x - cut_m) > cut_tol:
                        if not (a.x <= cut_m <= b.x or b.x <= cut_m <= a.x):
                            continue
                lines.append((_project_section_x(a), _project_section_x(b)))
    return lines


def bounds_2d(lines):
    us = [u for seg in lines for u, _ in seg]
    vs = [v for seg in lines for _, v in seg]
    if not us:
        return 0, 0, 1, 1
    return min(us), min(vs), max(us), max(vs)


def lines_to_svg(lines, scale: int, stroke: str = "#111", sw: float = 0.35, margin_mm: float = 8) -> str:
    if not lines:
        return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text x="10" y="50">empty</text></svg>'
    u0, v0, u1, v1 = bounds_2d(lines)
    w = _mm(u1 - u0, scale) + 2 * margin_mm
    h = _mm(v1 - v0, scale) + 2 * margin_mm
    ox = margin_mm - _mm(u0, scale)
    oy = margin_mm + _mm(v1, scale)  # flip Y for SVG

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" '
        f'width="{w:.2f}mm" height="{h:.2f}mm">',
        f'<rect width="{w:.2f}" height="{h:.2f}" fill="#fff"/>',
    ]
    for (ua, va), (ub, vb) in lines:
        x1 = ox + _mm(ua, scale)
        y1 = oy - _mm(va, scale)
        x2 = ox + _mm(ub, scale)
        y2 = oy - _mm(vb, scale)
        parts.append(
            f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" '
            f'stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"/>'
        )
    parts.append("</svg>")
    return "\n".join(parts)


def write_view_svg(view: dict, preset: dict, out_path: Path) -> int:
    vtype = view["type"]
    crop = view.get("crop") or preset.get("crop")
    cut = view.get("cut_m")
    scale = view.get("scale") or preset.get("scale", 20)

    if vtype == "ortho_top":
        lines = extract_edges("ortho_top", crop, None)
        stroke = "#2f6fb0"
    elif vtype == "ortho_side":
        lines = extract_edges("ortho_side", crop, cut)
        stroke = "#111"
    elif vtype == "ortho_side_x":
        lines = extract_edges("ortho_side_x", crop, cut)
        stroke = "#111"
    else:
        raise ValueError(f"unknown view type {vtype}")

    svg = lines_to_svg(lines, scale, stroke=stroke)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(svg, encoding="utf-8")
    return len(lines)
