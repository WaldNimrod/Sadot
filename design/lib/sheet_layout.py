# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project
# _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/sheet_layout.py on 2026-07-08 —
# Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
"""Multi-view A3 landscape sheet layout helpers (420 x 297 mm)."""
from __future__ import annotations

import base64
from pathlib import Path

from . import drawing_kit as dk

# Zone rectangles in SVG page units (420 x 297 mm landscape)
ZONES = {
    "legend": (12, 28, 396, 14),
    "context": (12, 44, 118, 88),
    "primary": (134, 44, 274, 130),
    "detail": (12, 178, 396, 72),
    "parts": (12, 254, 396, 14),
}


def head_for_construction(title: str, sub: str) -> str:
    st = dk.Rt(12, 10.5, 52, 12, fill="#e7f3e9", stroke="#1c6b2e", sw=0.7, rx=1.5)
    st += dk.T(38, 17.5, "FOR CONSTRUCTION", 2.6, "#1c6b2e", "middle", True, rtl=False)
    return (
        st
        + dk.T(408, 18, title, 5.5, dk.GREEN, "end", True, rtl=False)
        + dk.T(408, 24.5, sub, 2.8, dk.GREEN, "end", rtl=False)
    )


def layer_legend(x: float, y: float) -> str:
    rows = [
        (dk.BLUE, "Water"),
        ("#3a1d6e", "Electrical"),
        ("#5e35b1", "Control"),
        (dk.GREY, "Structure"),
        (dk.BALL, "Dims / notes"),
    ]
    s = dk.T(x, y, "Layer key", 2.6, dk.GREEN, "start", True, rtl=False)
    xx = x
    for col, txt in rows:
        s += dk.L(xx, y + 4, xx + 8, y + 4, col, 1.2)
        s += dk.T(xx + 10, y + 5, txt, 2.2, "#333", "start", rtl=False)
        xx += 52
    return s


def zone_frame(name: str, label: str, dash: str | None = "3 1.5") -> str:
    x, y, w, h = ZONES[name]
    return (
        dk.Rt(x, y, w, h, fill="none", stroke="#bbb", sw=0.25, dash=dash)
        + dk.T(x + 2, y + 4, label, 2.0, "#888", "start", ital=True, rtl=False)
    )


def scale_bar(x: float, y: float, mm_real: float, mm_draw: float, label: str) -> str:
    s = dk.L(x, y, x + mm_draw, y, "#333", 0.5)
    s += dk.L(x, y - 1, x, y + 1, "#333", 0.4)
    s += dk.L(x + mm_draw, y - 1, x + mm_draw, y + 1, "#333", 0.4)
    s += dk.L(x + mm_draw / 2, y - 0.8, x + mm_draw / 2, y + 0.8, "#333", 0.35)
    s += dk.T(
        x + mm_draw / 2,
        y - 2.5,
        f"{label} = {int(mm_real)} mm",
        2.2,
        "#333",
        "middle",
        rtl=False,
    )
    return s


def parts_index_table(rows: list[tuple[str, str, str]], x: float, y: float) -> str:
    s = dk.T(x, y, "Parts index", 2.8, dk.GREEN, "start", True, rtl=False)
    col_w = [8, 22, 80]
    headers = ["#", "Tag", "Description"]
    hx = x
    for w, h in zip(col_w, headers):
        s += dk.Rt(hx, y + 3, w, 6, fill="#234d24", stroke="#234d24", sw=0.2)
        s += dk.T(hx + w / 2, y + 7.5, h, 2.2, "#fff", "middle", True, rtl=False)
        hx += w + 1
    ry = y + 10
    for num, tag, desc in rows:
        hx = x
        for w, val in zip(col_w, [num, tag, desc]):
            s += dk.Rt(hx, ry, w, 5.5, fill="#fafbf7", stroke="#cdd6c4", sw=0.2)
            s += dk.T(hx + 1.5, ry + 4, val, 2.0, "#111", "start", rtl=False)
            hx += w + 1
        ry += 6
    return s


def embed_context_image(
    png_path: str | Path,
    zone: str = "context",
    caption: str = "Model context (_022)",
    *,
    file_href: str | None = None,
) -> str:
    x, y, w, h = ZONES[zone]
    path = Path(png_path)
    if not path.exists():
        return dk.Rt(x, y, w, h, fill="#f5f5f5", stroke="#ccc") + dk.T(
            x + w / 2, y + h / 2, "Context image missing", 2.5, "#999", "middle", rtl=False
        )
    inner = 2
    if file_href:
        href = file_href
    else:
        data = base64.b64encode(path.read_bytes()).decode("ascii")
        href = f"data:image/png;base64,{data}"
    return (
        dk.Rt(x, y, w, h, fill="#fff", stroke="#888", sw=0.4)
        + f'<image x="{x + inner}" y="{y + inner}" width="{w - 2 * inner}" height="{h - 2 * inner}" '
        f'preserveAspectRatio="xMidYMid meet" href="{href}"/>'
        + dk.T(x + w / 2, y + h - 2, caption, 1.8, "#666", "middle", ital=True, rtl=False)
    )


def contractor_notes(notes: list[str], x: float, y: float, w: float, h: float, title: str = "Site notes") -> str:
    s = dk.Rt(x, y, w, h, fill="#fff8ef", stroke="#e0a060", sw=0.4, rx=1.5)
    s += dk.T(x + w - 2, y + 5, title, 2.8, "#b06000", "end", True, rtl=False)
    for i, note in enumerate(notes):
        s += dk.T(x + w - 2, y + 11 + i * 4.5, f"• {note}", 2.0, "#444", "end", rtl=False)
    return s


def embed_image_in_zone(png_path: str | Path, x: float, y: float, w: float, h: float, caption: str = "") -> str:
    path = Path(png_path)
    if not path.exists():
        return dk.Rt(x, y, w, h, fill="#f5f5f5", stroke="#ccc")
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    inner = 1.5
    s = dk.Rt(x, y, w, h, fill="#fff", stroke="#888", sw=0.35)
    s += (
        f'<image x="{x + inner}" y="{y + inner}" width="{w - 2 * inner}" height="{h - 2 * inner - 4}" '
        f'preserveAspectRatio="xMidYMid meet" href="data:image/png;base64,{data}"/>'
    )
    if caption:
        s += dk.T(x + w / 2, y + h - 1.5, caption, 1.7, "#555", "middle", ital=True, rtl=False)
    return s
