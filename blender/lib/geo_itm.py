# Provenance: harvested verbatim from IsraelMicrogreens-BlenderV2-Project lib/geo_itm.py
# on 2026-07-08 — Sadot blender/ pipeline bootstrap (WP: SDT-S001-P001-WP001).
# Pure-Python WGS84 <-> Israeli TM (EPSG:2039) converter — no external deps, reusable as-is.
"""Israel TM (EPSG:2039) forward transform — no external deps."""
from __future__ import annotations

import math

# EPSG:2039 — Israel 1993 / Israeli TM Grid (GRS80)
_LAT0 = math.radians(31.73439361111111)
_LON0 = math.radians(35.20451694444445)
_K0 = 1.0000067
_X0 = 219529.584
_Y0 = 626907.39
_A = 6378137.0
_F = 1 / 298.257222101


def _meridional_arc(phi: float) -> float:
    e2 = 2 * _F - _F * _F
    e4, e6 = e2 * e2, e2 * e2 * e2
    aa = _A * (1 - e2)
    return aa * (
        (1 - e2 / 4 - 3 * e4 / 64 - 5 * e6 / 256) * phi
        - (3 * e2 / 8 + 3 * e4 / 32 + 45 * e6 / 1024) * math.sin(2 * phi)
        + (15 * e4 / 256 + 45 * e6 / 1024) * math.sin(4 * phi)
        - (35 * e6 / 3072) * math.sin(6 * phi)
    )


def wgs84_to_itm(lat_deg: float, lon_deg: float) -> tuple[float, float]:
    """Return (easting_m, northing_m) for WGS84 lat/lon."""
    lat = math.radians(lat_deg)
    lon = math.radians(lon_deg)
    e2 = 2 * _F - _F * _F
    ep2 = e2 / (1 - e2)
    n = _A / math.sqrt(1 - e2 * math.sin(lat) ** 2)
    t = math.tan(lat) ** 2
    c = ep2 * math.cos(lat) ** 2
    a = (lon - _LON0) * math.cos(lat)
    m = _meridional_arc(lat) - _meridional_arc(_LAT0)
    easting = _K0 * n * (
        a + (1 - t + c) * a**3 / 6 + (5 - 18 * t + t**2 + 72 * c - 58 * ep2) * a**5 / 120
    ) + _X0
    northing = _K0 * (
        m
        + n
        * math.tan(lat)
        * (a**2 / 2 + (5 - t + 9 * c + 4 * c**2) * a**4 / 24 + (61 - 58 * t + t**2 + 600 * c - 330 * ep2) * a**6 / 720)
    ) + _Y0
    return round(easting, 3), round(northing, 3)


def local_blender_to_wgs84(
    x_m: float,
    y_m: float,
    anchor_lat: float,
    anchor_lon: float,
    plus_x_bearing_deg: float,
) -> tuple[float, float]:
    """Map Blender XY (metres) to WGS84 using anchor + +X bearing from true north."""
    bx = math.radians(plus_x_bearing_deg)
    # EN offset from anchor: +X_bl -> (sin(bx), cos(bx)), +Y_bl -> (cos(bx), -sin(bx))
    de = x_m * math.sin(bx) + y_m * math.cos(bx)
    dn = x_m * math.cos(bx) - y_m * math.sin(bx)
    lat = math.radians(anchor_lat)
    lon = math.radians(anchor_lon)
    r = 6378137.0
    dlat = dn / r
    dlon = de / (r * math.cos(lat))
    return math.degrees(lat + dlat), math.degrees(lon + dlon)


def north_vector_blender(plus_x_bearing_deg: float, length_m: float = 3.0) -> tuple[float, float, float]:
    """Unit true-north direction in Blender XY for given +X bearing (deg from N, clockwise)."""
    bx = math.radians(plus_x_bearing_deg)
    # Solve for north in Blender basis
    nx_en, ny_en = 0.0, 1.0
    # Inverse of [[sin(bx), cos(bx)], [cos(bx), -sin(bx)]]
    det = -math.sin(bx) * math.sin(bx) - math.cos(bx) * math.cos(bx)
    det = -1.0  # sin^2+cos^2
    bx_bl = (-math.sin(bx) * nx_en - math.cos(bx) * ny_en) / det
    by_bl = (-math.cos(bx) * nx_en + math.sin(bx) * ny_en) / det
    mag = math.hypot(bx_bl, by_bl)
    return (bx_bl / mag * length_m, by_bl / mag * length_m, 0.0)
