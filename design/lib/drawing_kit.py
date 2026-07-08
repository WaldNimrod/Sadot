# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project
# _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/drawing_kit.py on 2026-07-08 —
# Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
"""
drawing_kit.py — Phase 5 shared SVG/DXF primitives (extracted from water-system generators).

Revision lineage: Phase-5 sheets use "Phase-5 Technical Package vN" (independent from water C-r3).
"""
from __future__ import annotations

import os
from typing import Iterable, Sequence

# Standard AutoCAD Color Index layer table (reuse across all systems)
STANDARD_LAYERS: tuple[tuple[str, int], ...] = (
    ("STRUCT", 6),
    ("WATER", 5),
    ("DRAIN", 3),
    ("ELEC", 1),
    ("LIGHT", 2),
    ("HVAC", 4),
    ("DIM", 8),
    ("TEXT", 7),
    ("BALLOON", 30),
)

INK = "#111"
GREEN = "#234d24"
GREY = "#6f6f6f"
BALL = "#c9622f"
BLUE = "#2f6fb0"

PAGE_LANDSCAPE = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" '
    'viewBox="0 0 420 297"><rect width="420" height="297" fill="#fff"/>{b}</svg>'
)
PAGE_PORTRAIT = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="297mm" height="420mm" '
    'viewBox="0 0 297 420"><rect width="297" height="420" fill="#fff"/>{b}</svg>'
)


# --- SVG primitives (raw string-building, no external SVG library) ---


def esc(s) -> str:
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def T(
    x,
    y,
    s,
    size=2.4,
    fill=INK,
    anc="middle",
    bold=False,
    ital=False,
    rot=None,
    rtl=True,
) -> str:
    fw = ' font-weight="bold"' if bold else ""
    fs = ' font-style="italic"' if ital else ""
    tr = f' transform="rotate({rot[0]} {rot[1]} {rot[2]})"' if rot else ""
    return (
        f'<text x="{x}" y="{y}" font-family="Arial" font-size="{size}" '
        f'fill="{fill}" text-anchor="{anc}" direction="ltr"{fw}{fs}{tr}>{esc(s)}</text>'
    )


def L(x1, y1, x2, y2, stroke=INK, w=0.4, dash=None, cap="round") -> str:
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
        f'stroke="{stroke}" stroke-width="{w}"{d} stroke-linecap="{cap}"/>'
    )


def Rt(x, y, w, h, fill="none", stroke=INK, sw=0.4, dash=None, rx=0) -> str:
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
    )


def Ci(cx, cy, r, fill="#fff", stroke=INK, sw=0.4) -> str:
    return (
        f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{sw}"/>'
    )


def PATH(d, fill="none", stroke=INK, sw=0.4) -> str:
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def dim_h(x1, x2, y, txt, color=GREY) -> str:
    return (
        L(x1, y, x2, y, color, 0.3)
        + L(x1, y - 1.3, x1, y + 1.3, color, 0.3)
        + L(x2, y - 1.3, x2, y + 1.3, color, 0.3)
        + T((x1 + x2) / 2, y - 1.0, txt, 2.4, color, "middle")
    )


def dim_v(y1, y2, x, txt, color=GREY, anc="start") -> str:
    return (
        L(x, y1, x, y2, color, 0.3)
        + L(x - 1.3, y1, x + 1.3, y1, color, 0.3)
        + L(x - 1.3, y2, x + 1.3, y2, color, 0.3)
        + T(x + 1.0 if anc == "start" else x - 1.0, (y1 + y2) / 2, txt, 2.4, color, anc)
    )


def frame() -> str:
    return Rt(6, 6, 408, 285, stroke=INK, sw=0.7) + Rt(8, 8, 404, 281, stroke=INK, sw=0.35)


def titleblock(title, sheet, scale, revision="Phase-5 Technical Package v2") -> str:
    s = Rt(8, 272, 404, 18, fill="#fafbf7", stroke=INK, sw=0.45)
    for x in (158, 258, 338, 383):
        s += L(x, 272, x, 290, "#bbb", 0.25)
    s += L(8, 281, 412, 281, "#bbb", 0.25)
    s += T(
        409,
        277.5,
        "Israel Organic Greens — Grow Container — Phase 5",
        3.0,
        GREEN,
        "end",
        True,
        rtl=False,
    )
    s += T(409, 286.5, title, 2.9, INK, "end", rtl=False)
    s += (
        T(155, 277.5, "Scale", 2.4, "#888", "end", rtl=False)
        + T(155, 286.5, scale, 3.0, INK, "end", rtl=False)
    )
    s += (
        T(255, 277.5, "Units", 2.4, "#888", "end", rtl=False)
        + T(255, 286.5, "mm", 3.0, INK, "end", rtl=False)
    )
    s += (
        T(335, 277.5, "Sheet", 2.4, "#888", "end", rtl=False)
        + T(335, 286.5, sheet, 3.0, INK, "end", rtl=False)
    )
    s += (
        T(380, 277.5, "Rev", 2.4, "#888", "end", rtl=False)
        + T(380, 286.5, revision, 2.6, BALL, "end", True, rtl=False)
    )
    return s


def head(title, sub, color=GREEN) -> str:
    return T(12, 18, title, 6.5, color, "start", True) + T(12, 24, sub, 3.2, "#6f6f6f", "start")


def enode(cx, cy, code, color, r=1.7, fs=2.0) -> str:
    return Ci(cx, cy, r, "#fff", color, 0.5) + T(cx, cy + 0.7, code, fs, color, "middle", True, rtl=False)


def balloon(num, bx, by, tx, ty, r=3.4, color=BALL) -> str:
    return (
        L(bx, by, tx, ty, color, 0.4)
        + Ci(bx, by, r, "#fff", color, 0.7)
        + T(bx, by + 1.3, str(num), 3.8, color, "middle", bold=True)
    )


def write_sheets(
    out_dir: str,
    sheets: Sequence[tuple[str, str]],
    page_template: str = PAGE_LANDSCAPE,
    html_name: str = "Drawings.html",
) -> list[str]:
    """Write one .svg per sheet plus a combined RTL HTML file for PDF conversion."""
    os.makedirs(out_dir, exist_ok=True)
    written: list[str] = []
    for nm, svg in sheets:
        path = os.path.join(out_dir, nm + ".svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page_template.format(b=svg))
        written.append(path)
    htmlpgs = "".join(
        f'<div class="pg">{page_template.format(b=svg)}</div>' for _, svg in sheets
    )
    size = "420mm 297mm" if page_template is PAGE_LANDSCAPE else "297mm 420mm"
    w, h = size.split()
    html = (
        f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><style>'
        f"@page{{size:{size};margin:0}} html,body{{margin:0;padding:0}}"
        f".pg{{width:{w};height:{h};page-break-after:always;overflow:hidden}}"
        f"svg{{display:block;width:{w};height:{h}}}"
        f"</style></head><body>{htmlpgs}</body></html>"
    )
    html_path = os.path.join(out_dir, html_name)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    written.append(html_path)
    return written


# --- DXF export helpers (real CAD output, ezdxf library) ---


def new_dxf_doc(layers: Iterable[tuple[str, int]] | None = None):
    """layers = [(name, aci_color_int), ...]. Returns (doc, msp)."""
    import ezdxf

    doc = ezdxf.new("R2010", setup=True)
    msp = doc.modelspace()
    for n, c in layers or STANDARD_LAYERS:
        if n not in doc.layers:
            doc.layers.add(n, color=c)
    return doc, msp


def dxf_rect(msp, x, y, w, h, layer: str) -> None:
    msp.add_lwpolyline(
        [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)],
        dxfattribs={"layer": layer},
    )


def dxf_line(msp, x1, y1, x2, y2, layer: str) -> None:
    msp.add_line((x1, y1), (x2, y2), dxfattribs={"layer": layer})


def dxf_text(msp, x, y, s, h=40, layer="TEXT", align=None) -> None:
    from ezdxf.enums import TextEntityAlignment as AL

    align = align or AL.LEFT
    msp.add_text(s, dxfattribs={"layer": layer, "height": h}).set_placement((x, y), align=align)


def dxf_vdim(msp, x, y1, y2) -> None:
    d = msp.add_linear_dim(
        base=(x, (y1 + y2) / 2),
        p1=(x, y1),
        p2=(x, y2),
        angle=90,
        dimstyle="EZDXF",
        override={"dimtxt": 45, "dimasz": 30},
    )
    d.render()


def dxf_hdim(msp, y, x1, x2) -> None:
    d = msp.add_linear_dim(
        base=((x1 + x2) / 2, y),
        p1=(x1, y),
        p2=(x2, y),
        angle=0,
        dimstyle="EZDXF",
        override={"dimtxt": 45, "dimasz": 30},
    )
    d.render()


def dxf_balloon(msp, num, bx, by, tx, ty, r=70) -> None:
    from ezdxf.enums import TextEntityAlignment as AL

    msp.add_circle((bx, by), r, dxfattribs={"layer": "BALLOON"})
    msp.add_text(str(num), dxfattribs={"layer": "BALLOON", "height": 50}).set_placement(
        (bx, by), align=AL.MIDDLE_CENTER
    )
    msp.add_line((bx, by), (tx, ty), dxfattribs={"layer": "BALLOON"})
