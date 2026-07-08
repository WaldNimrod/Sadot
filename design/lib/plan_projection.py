# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project
# _communication/team_100_engineering/WP_PHASE5_TECHNICAL_DOCS/lib/plan_projection.py on
# 2026-07-08 — Sadot design/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
"""World-space (metres, matrix_basis) -> SVG sheet coordinates at architectural scale."""
from __future__ import annotations

from . import drawing_kit as dk


def mm_on_sheet(mm_real: float, scale: int = 25) -> float:
    """Real millimetres to drawing millimetres (SVG viewBox units)."""
    return mm_real / scale


def m_on_sheet(m_real: float, scale: int = 25) -> float:
    return mm_on_sheet(m_real * 1000, scale)


class PlanView:
    """Top view: world X right, world Y up on sheet."""

    def __init__(self, ox: float, oy: float, scale: int = 25):
        self.ox = ox
        self.oy = oy
        self.scale = scale

    def x(self, xm: float) -> float:
        return self.ox + m_on_sheet(xm, self.scale)

    def y(self, ym: float) -> float:
        return self.oy + m_on_sheet(ym, self.scale)

    def rect(self, bounds: dict, **kw) -> str:
        b = bounds
        x0, x1 = b["x"]
        y0, y1 = b["y"]
        return dk.Rt(self.x(x0), self.y(y0), self.x(x1) - self.x(x0), self.y(y1) - self.y(y0), **kw)

    def capsule(self, bounds: dict, **kw) -> str:
        """Top view of horizontal cylinder — rounded ends."""
        b = bounds
        x0, x1 = b["x"]
        y0, y1 = b["y"]
        w = self.x(x1) - self.x(x0)
        h = self.y(y1) - self.y(y0)
        rx = min(w, h) / 2
        return dk.Rt(self.x(x0), self.y(y0), w, h, rx=rx, **kw)

    def dim_h_world(self, x0m: float, x1m: float, ym: float, label: str, pad: float = 4) -> str:
        y = self.y(ym) - pad
        return dk.dim_h(self.x(x0m), self.x(x1m), y, label)

    def dim_v_world(self, y0m: float, y1m: float, xm: float, label: str, pad: float = 4, anc: str = "start") -> str:
        x = self.x(xm) + (pad if anc == "start" else -pad)
        return dk.dim_v(self.y(y0m), self.y(y1m), x, label, anc=anc)


class SectionXZ:
    """Longitudinal section: world X horizontal, Z vertical (grade at bottom)."""

    def __init__(self, ox: float, base_y: float, grade_z: float, scale: int = 25):
        self.ox = ox
        self.base_y = base_y
        self.grade_z = grade_z
        self.scale = scale

    def x(self, xm: float) -> float:
        return self.ox + m_on_sheet(xm, self.scale)

    def z(self, zm: float) -> float:
        return self.base_y - m_on_sheet(zm - self.grade_z, self.scale)

    def rect_xz(self, bounds: dict, **kw) -> str:
        b = bounds
        x0, z0 = b["x"][0], b["z"][0]
        x1, z1 = b["x"][1], b["z"][1]
        return dk.Rt(self.x(x0), self.z(z1), self.x(x1) - self.x(x0), self.z(z0) - self.z(z1), **kw)

    def capsule_xz(self, bounds: dict, **kw) -> str:
        """Side elevation of horizontal cylinder (axis parallel to world X)."""
        b = bounds
        x0, z0 = b["x"][0], b["z"][0]
        x1, z1 = b["x"][1], b["z"][1]
        w = self.x(x1) - self.x(x0)
        h = self.z(z0) - self.z(z1)
        rx = min(w, h) / 2
        return dk.Rt(self.x(x0), self.z(z1), w, h, rx=rx, **kw)

    def grade_line(self, x0m: float, x1m: float, color: str = "#8a6d3b") -> str:
        y = self.z(self.grade_z)
        return dk.L(self.x(x0m), y, self.x(x1m), y, color, 0.8)

    def dim_v_z(self, z0m: float, z1m: float, xm: float, label: str, anc: str = "start") -> str:
        return dk.dim_v(self.z(z1m), self.z(z0m), self.x(xm) + 3, label, anc=anc)

    def draw_pipe_xz(self, bounds: dict, cut_y: float, tol: float = 0.01, **kw) -> str:
        y0, y1 = bounds["y"]
        if cut_y < y0 - tol or cut_y > y1 + tol:
            return ""
        return self.rect_xz(bounds, **kw)


class SectionYZ:
    """Transverse section: world Y horizontal, Z vertical."""

    def __init__(self, ox: float, base_y: float, grade_z: float, scale: int = 25):
        self.ox = ox
        self.base_y = base_y
        self.grade_z = grade_z
        self.scale = scale

    def y(self, ym: float) -> float:
        return self.ox + m_on_sheet(ym, self.scale)

    def z(self, zm: float) -> float:
        return self.base_y - m_on_sheet(zm - self.grade_z, self.scale)

    def rect_yz(self, bounds: dict, **kw) -> str:
        b = bounds
        y0, z0 = b["y"][0], b["z"][0]
        y1, z1 = b["y"][1], b["z"][1]
        return dk.Rt(self.y(y0), self.z(z1), self.y(y1) - self.y(y0), self.z(z0) - self.z(z1), **kw)

    def circle_yz(self, bounds: dict, **kw) -> str:
        """End view of horizontal cylinder (cut perpendicular to axis X)."""
        b = bounds
        y0, y1 = b["y"][0], b["y"][1]
        z0, z1 = b["z"][0], b["z"][1]
        cy = (y0 + y1) / 2
        cz = (z0 + z1) / 2
        r_m = min(y1 - y0, z1 - z0) / 2
        r = m_on_sheet(r_m, self.scale)
        return dk.Ci(self.y(cy), self.z(cz), r, **kw)
