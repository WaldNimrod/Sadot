#!/usr/bin/env python3
# Sadot — IFC ingest smoke verifier (SDT-S002-P007-WP001).
#
# Opens an IFC, reports schema / unit scale / storeys / type counts / bbox, and
# exits non-zero on hard failures (unreadable file, missing length unit, zero geometry).
#
# Run from repo root:
#   /Library/Developer/CommandLineTools/usr/bin/python3 blender/scripts/ingest/verify_ifc.py \
#     raw-materials/from-client/NSB02_v2_2026-07-13.ifc

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import ifcopenshell
import ifcopenshell.geom as geom
import ifcopenshell.util.unit as unit_util

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_IFC = REPO_ROOT / "raw-materials/from-client/NSB02_v2_2026-07-13.ifc"
FALLBACK_IFC = REPO_ROOT / "raw-materials/from-client/NSB02.ifc"

COUNT_TYPES = (
    "IfcWall",
    "IfcWindow",
    "IfcDoor",
    "IfcRoof",
    "IfcSlab",
    "IfcStair",
    "IfcBuildingStorey",
    "IfcSpace",
)


def resolve_ifc(path: Path | None) -> Path:
    if path is not None:
        p = path if path.is_absolute() else REPO_ROOT / path
        if not p.is_file():
            raise FileNotFoundError(f"IFC not found: {p}")
        return p
    if DEFAULT_IFC.is_file():
        return DEFAULT_IFC
    if FALLBACK_IFC.is_file():
        return FALLBACK_IFC
    raise FileNotFoundError(
        f"No fixture IFC at {DEFAULT_IFC} or {FALLBACK_IFC}"
    )


def bbox_sample(f, scale: float, max_elems: int = 40) -> dict | None:
    """World-coord bbox from a sample of walls+slabs (meters).

    Attribute elevations still need unit_scale_to_m, but ifcopenshell.geom with
    USE_WORLD_COORDS on NSB02 already yields meter-scale verts (matches the
    existing export_house_shell_obj.py which writes verts without re-scaling).
    Do NOT multiply geom verts by unit_scale again.
    """
    del scale  # elevations use scale elsewhere; geom verts are already meters
    settings = geom.settings()
    settings.set(settings.USE_WORLD_COORDS, True)
    candidates = list(f.by_type("IfcWall"))[:max_elems]
    candidates += list(f.by_type("IfcSlab"))[: max(5, max_elems // 4)]
    xs_m, ys_m, zs_m = [], [], []
    for elem in candidates:
        try:
            shape = geom.create_shape(settings, elem)
        except Exception:
            continue
        verts = shape.geometry.verts
        for i in range(0, len(verts), 3):
            xs_m.append(verts[i])
            ys_m.append(verts[i + 1])
            zs_m.append(verts[i + 2])
    if not xs_m:
        return None
    return {
        "min_m": [min(xs_m), min(ys_m), min(zs_m)],
        "max_m": [max(xs_m), max(ys_m), max(zs_m)],
        "span_m": [
            max(xs_m) - min(xs_m),
            max(ys_m) - min(ys_m),
            max(zs_m) - min(zs_m),
        ],
        "sample_elements": len(candidates),
        "note": "geom verts treated as meters (no unit_scale multiply)",
    }


def verify(ifc_path: Path) -> dict:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        f = ifcopenshell.open(str(ifc_path))
    except Exception as e:
        return {
            "ok": False,
            "path": str(ifc_path),
            "errors": [f"open failed: {e}"],
        }

    scale = unit_util.calculate_unit_scale(f)
    if scale <= 0:
        errors.append(f"invalid unit_scale_to_m={scale}")

    storeys = []
    for s in sorted(f.by_type("IfcBuildingStorey"), key=lambda x: (x.Elevation or 0)):
        elev = (s.Elevation or 0) * scale
        storeys.append({"name": s.Name, "elevation_m": round(elev, 4)})

    if not storeys:
        warnings.append("no IfcBuildingStorey entities")

    counts = {t: len(f.by_type(t)) for t in COUNT_TYPES}
    if counts.get("IfcWall", 0) == 0 and counts.get("IfcSlab", 0) == 0:
        errors.append("zero walls and slabs — empty or non-building IFC?")

    # Known Sadot failure-mode hints
    walls = f.by_type("IfcWall")
    if walls:
        exteriors = 0
        for w in walls:
            for rel in getattr(w, "IsDefinedBy", []) or []:
                if not rel.is_a("IfcRelDefinesByProperties"):
                    continue
                pdef = rel.RelatingPropertyDefinition
                if not pdef.is_a("IfcPropertySet"):
                    continue
                for p in pdef.HasProperties:
                    if (
                        p.is_a("IfcPropertySingleValue")
                        and p.Name == "IsExternal"
                        and p.NominalValue
                        and p.NominalValue.wrappedValue is True
                    ):
                        exteriors += 1
        if exteriors == len(walls) and len(walls) > 10:
            warnings.append(
                f"IsExternal=True on all {len(walls)} walls — flag unreliable (Sadot known issue)"
            )

    bbox = None
    try:
        bbox = bbox_sample(f, scale)
    except Exception as e:
        warnings.append(f"bbox sample failed: {e}")

    if bbox and bbox["span_m"][0] < 5 and bbox["span_m"][1] < 5:
        warnings.append("bbox XY span <5m on wall/slab sample — possible unit/scale problem")

    # Known length check: first two storeys elevation delta (Sadot entrance→parents ≈ 3.1m)
    storey_delta_m = None
    if len(storeys) >= 2:
        storey_delta_m = round(storeys[1]["elevation_m"] - storeys[0]["elevation_m"], 4)
        if not (2.0 <= abs(storey_delta_m) <= 5.0):
            warnings.append(
                f"storey[0]→[1] delta {storey_delta_m}m outside 2–5m — check unit scale"
            )

    report = {
        "ok": len(errors) == 0,
        "path": str(ifc_path),
        "schema": f.schema,
        "unit_scale_to_m": scale,
        "storeys": storeys,
        "counts": counts,
        "bbox_sample_m": bbox,
        "storey_delta_0_to_1_m": storey_delta_m,
        "warnings": warnings,
        "errors": errors,
        "ifcopenshell": getattr(ifcopenshell, "version", "unknown"),
    }
    return report


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Sadot IFC ingest verifier")
    ap.add_argument("ifc", nargs="?", type=Path, help="Path to .ifc (default: NSB02_v2 fixture)")
    ap.add_argument("--json", action="store_true", help="Emit JSON only")
    ap.add_argument("-o", "--out", type=Path, help="Write JSON report to this path")
    args = ap.parse_args(argv)

    try:
        ifc_path = resolve_ifc(args.ifc)
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    report = verify(ifc_path)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=2) + "\n")

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"path={report['path']}")
        if not report.get("schema"):
            print("FAILED:", "; ".join(report.get("errors") or ["unknown"]))
            return 1
        print(f"schema={report['schema']} unit_scale_to_m={report['unit_scale_to_m']}")
        print(f"ifcopenshell={report['ifcopenshell']}")
        print("-- storeys --")
        for s in report["storeys"]:
            print(f"  {s['name']!r}  elevation_m={s['elevation_m']}")
        print("-- counts --")
        for k, v in report["counts"].items():
            print(f"  {k}: {v}")
        if report.get("bbox_sample_m"):
            b = report["bbox_sample_m"]
            print(
                f"-- bbox sample (m) -- span XY={b['span_m'][0]:.2f}×{b['span_m'][1]:.2f} "
                f"Z={b['span_m'][2]:.2f}"
            )
        if report.get("storey_delta_0_to_1_m") is not None:
            print(f"-- scale check -- storey[0]→[1] delta_m={report['storey_delta_0_to_1_m']}")
        for w in report.get("warnings") or []:
            print(f"WARN: {w}")
        for e in report.get("errors") or []:
            print(f"ERROR: {e}")
        print("RESULT:", "PASS" if report["ok"] else "FAIL")

    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
